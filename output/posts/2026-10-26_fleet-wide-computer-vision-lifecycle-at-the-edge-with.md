---
title: Fleet-wide computer vision lifecycle at the edge with SageMaker SDK v3
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/
model: claude-code/sonnet
generated_at: '2026-10-26T21:55:54.154117'
score: 75
---

📌 工廠要40條線各自的視覺模型，這套Pipeline怎麼管

TL;DR：AWS用SageMaker SDK v3重寫邊緣電腦視覺機群MLOps範例，以雙分支Pipeline管理每支相機各自的異常偵測與缺陷分類模型。

一支相機、一個模型跑得很漂亮，然後工廠要求把同樣的效果複製到40條生產線、每條線好幾支相機——問題在這一刻從「訓練好一個模型」變成「同時管理數千個模型的生命週期，而且不能每一個都靠人工把關」。

🤔 **一個模型打天下，實測反而不如多個專屬模型**

AWS在這篇部落格中指出，根據他們參與過的實際部署經驗，用匯集所有相機畫面訓練出的單一模型，效能表現往往不如為每支相機分別微調的個別模型，原因在於每支相機的角度、同一不鏽鋼表面反射出的眩光、以及隨廠房捲門開關而變化的環境光都不一樣。這篇文章是2023年「Build an end-to-end MLOps pipeline for visual quality inspection at the edge」系列的更新版，改用當前的Amazon SageMaker Python SDK v3，並以Amazon SageMaker Neo取代已被棄用的Amazon SageMaker Edge Manager做邊緣最佳化。

🧩 **雙分支Pipeline：異常偵測＋缺陷分類，各自過質量閘**

核心是一個以相機為參數、每次執行跑13個步驟的SageMaker Pipeline。三個進入點步驟（Preprocess、Fetch Latest Anomaly、Fetch Latest Classifier）並行執行：先前處理該相機的影像，同時抓取該相機各分支最近一次核准的模型版本，接著訓練兩個模型——一個小型卷積自編碼器（convolutional autoencoder）學習正常產品的樣貌，透過重建誤差（reconstruction error）標記異常；另一個是微調過的ResNet18分類器，用來確認缺陷類型。兩個分支各自將模型輸出為ONNX格式，針對匯出後的ONNX artifact（而非記憶體中的PyTorch模型）進行評估，再通過質量閘才能往下走。異常分支的質量閘門檻設定在AUROC至少0.8。通過閘門後，模型會依設定的邊緣目標用SageMaker Neo編譯，最後才註冊進SageMaker Model Registry。每個模型封裝都帶有相機ID中繼資料，讓各分支的warm-start抓取都能精準對應到該相機自己的歷史版本。

🧩 **機群節奏由Step Functions與DynamoDB語義鎖把關**

訓練之外，還有一層編排邏輯負責控制整個機群的訓練節奏：重訓練請求先進入Amazon SQS的FIFO佇列，由一個AWS Lambda函式為每個請求啟動一次Step Functions執行；每次執行要先透過DynamoDB語義鎖（semaphore）取得名額才能真正啟動Pipeline，讓一波湧入的請求以穩定速率逐一消化，而不是一次全部啟動。執行完成後透過Amazon SNS發出通知，若執行過程失敗，則透過EventBridge規則把原始錯誤訊息送到同一個SNS主題。這套編排層預設最多同時容許5個Pipeline執行，剛好落在標準帳戶配額內，不需要額外申請配額提升。

📊 **最終輸出與部署成本**

系統最終輸出的是版本化、經過質量閘把關的每相機模型組合：Model Registry保存可攜的ONNX模型，S3則保存Neo編譯後的版本，也就是由DLR runtime載入的裝置最佳化共享函式庫，兩者都可以對接任何工廠既有的部署方式。整套範例以AWS CDK部署，用合成資料跑一次完整Pipeline的運算成本約0.07美元。

💡 **SDK v3的兩個「非破壞性變更」陷阱**

SDK v3把SageMaker Python SDK拆成模組化套件：`sagemaker-core`、`sagemaker-train`、`sagemaker-serve`、`sagemaker-mlops`，v2時期分散在Estimator建構子參數裡的訓練設定，現在改成傳入`ModelTrainer`的型別化設定物件。文章特別點出兩個v3在CDK應用中會遇到、卻沒有被列為breaking change的行為：第一，v3會在建構Pipeline定義時就對照即時IAM驗證執行角色，這個驗證發生在synthesis時而非執行時，導致CDK應用無法在同一次部署裡同時建立角色與Pipeline，因為驗證發生時角色還不存在，角色ARN也必須是具體字串，不能是未解析的CDK token；文中範例的解法是兩階段部署，第一次用`-c bootstrap=true`建立角色、bucket與ECR repository，第二次再針對已存在的角色合成Pipeline。第二，v3的角色驗證器在模擬ECR pull權限時不帶resource ARN，導致只被授權存取單一ECR repository的執行角色會驗證失敗，即使它在實際執行時其實可行，因此範例中的角色改用較寬的ECR授權。另外，用`PipelineSession(default_bucket=your_bucket)`建構Pipeline，可以把SDK管理的上傳（如step code）導向Pipeline自己的bucket，讓所有artifact集中在一處，執行角色的權限也只需覆蓋單一bucket。

⚠️ **部署前要注意的環境細節**

文章提醒，CDK CLI版本過舊會因為與近期`aws-cdk-lib`版本不相容的cloud assembly schema而失敗；若部署到非CLI預設的Region，必須在部署指令本身同時設定`AWS_REGION`、`AWS_DEFAULT_REGION`與`CDK_DEFAULT_REGION`三個環境變數，而不是寫在shell profile裡，因為CDK CLI、Boto3與AWS CLI各自讀取的變數集合有所重疊但不完全相同，設定不一致會造成令人困惑的部分部署。完整範例程式碼公開在aws-samples的GitHub repository。

🎯 **實務啟示**

這套範例示範了邊緣CV機群MLOps的幾個可直接複用的設計：用相機ID做warm-start的鍵、永遠對匯出後的部署artifact做評估而非對記憶體中的模型評估、用佇列加語義鎖控制機群重訓練節奏避免配額爆表。對正要把SDK從v2升級到v3、或正在設計多裝置、多模型版本管理機制的團隊，文中列出的IAM時序與ECR權限兩個陷阱，值得在升級前先排進檢查清單。

🔗 **來源**
- 標題：Fleet-wide computer vision lifecycle at the edge with SageMaker SDK v3
- 作者／機構：Kiowa Jackson（AWS Machine Learning Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/

#AmazonSageMaker #MLOps #EdgeAI #ComputerVision #SageMakerNeo #AWSCDK #ONNX #AnomalyDetection #ModelLifecycle #AWSMachineLearning
