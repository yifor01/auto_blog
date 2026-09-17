---
title: Enhancing industrial safety AI with synthetic data on Amazon SageMaker AI
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/enhancing-industrial-safety-ai-with-synthetic-data-on-amazon-sagemaker-ai/
model: claude-code/sonnet
generated_at: '2026-09-17T20:37:37.660023'
score: 85
---

📌 AWS 用 Diffusion 模型「P 圖」，人員偵測 mAP50 衝高 160%

TL;DR：AWS 用擴散模型在真實影像中合成插入人物，解決工業安全偵測最缺的危險場景訓練資料。

在礦場、工地、農場這些部署自主機具的場域，最需要模型能準確辨識「人站在機具危險範圍內」的那一刻。問題是，這種場景在真實資料裡最稀有，同時也是最危險、最不該為了收集資料而刻意重演的場景。AWS 一篇技術部落格提出用合成資料打破這個兩難。

🤔 越危險的場景，越沒有訓練資料

部署自主設備的產業（農業、營建、礦業、製造業）需要可靠的人員偵測模型，但高風險場景，例如工人站在機具死角、孩童靠近移動中的機具，正是真實資料集裡最罕見的樣本，也是最危險、最不適合實地拍攝收集的樣本。這讓邊緣部署的偵測模型在最關鍵的場景上,長期缺乏足夠訓練訊號。

🧩 不是憑空生成場景，而是在真實影像上「編輯」插入人物

AWS 的 pipeline 分兩階段：照片級真實感影像生成、自動標註。關鍵設計是編輯既有的真實影像，而非從頭生成全合成場景,這樣能保留背景真實度、避免 domain gap（模型在合成場景訓練、套用到真實影像時的效能落差），也讓原本機具的標註維持有效。

具體作法是把 Qwen-Image-Edit-2509 擴散模型部署在 Amazon SageMaker AI 的 ml.g5.12xlarge 執行個體上（4 張 NVIDIA A10G GPU，總計 96GB VRAM）。模型接收結構化的 prompt，在已有機具、但沒有人的真實影像上插入合成人物，同時保留原始場景的光線與比例。這個模型有 60 層 transformer,需要自訂 device map 把層分散到多張 GPU 上,官方建議盡量避免跨裝置通訊,若要更有效率,可改用單張大 VRAM GPU（例如 ml.p5.4xlarge 上的 NVIDIA H100）或搭配權重量化,團隊估計這樣每張影像的推論成本可望降低約 10 倍,但這項數字尚未實測驗證。

標註端則透過 Amazon Rekognition 的 DetectLabels API,信心門檻設定 80%,偵測到的邊界框以 IoU 門檻 0.5 的非極大值抑制（NMS）去重,再轉換成 YOLO 格式,並與原始影像既有的機具標註合併,整套流程不需要人工標註合成影像。

📊 三組實驗,把合成資料當超參數來調

- **放置策略消融實驗**（YOLO11-nano,1,000 張合成影像）：把人物放在「危險位置」讓 person mAP50 從 0.051 翻倍到 0.106,反觀放在背景位置反而讓效能略微下降。結論是,生成內容放在哪裡,比場景如何變化（例如光線、時段）更重要。
- **合成資料量掃描**（250 至 1,000 張,固定危險位置放置、YOLO11-nano）：效能在 750 張時達到高峰,person mAP50 較基準線提升 160%（從 0.051 到 0.134）。超過這個量,累積的生成瑕疵（例如臉部模糊、過度飽和）反而讓偵測定位信心與覆蓋率雙雙下降。
- **模型容量掃描**（5 種 YOLO11 規模,1,000 張合成影像）：YOLO11-medium 拿下最佳整體表現（0.604 mAP50）與最高人員召回率（0.340,較基準線翻倍）;而 5,700 萬參數的 XLarge 模型反而退步到不如 Nano+合成資料的組合,顯示在僅約 4,200 張訓練影像的規模下,容量太大的模型難以被有效正則化。

💡 「插對地方」比「場景多樣化」更關鍵

這幾組實驗共同指向一個結論:合成資料的價值不在於場景變化夠不夠多,而在於是否把人物放在與領域相關的真實危險位置。同時,合成資料量與模型容量都應該被當作需要驗證的超參數,而不是「越多越好、越大越好」。

🎯 實務啟示

對正在打造邊緣部署偵測模型的工程團隊來說,這套 in-place 影像編輯搭配自動標註的思路值得參考:比起從零生成合成場景,編輯真實影像能更有效避免 domain gap;而合成資料量與模型規模的最佳點,需要靠實驗掃描找出來,而非一味放大。

🔗 來源
- 標題:Enhancing industrial safety AI with synthetic data on Amazon SageMaker AI
- 作者／機構:Dimitri Voytan（AWS）
- 連結:https://aws.amazon.com/blogs/machine-learning/enhancing-industrial-safety-ai-with-synthetic-data-on-amazon-sagemaker-ai/

#SyntheticData #ComputerVision #IndustrialSafety #ObjectDetection #DiffusionModel #AmazonSageMaker #YOLO #EdgeAI #MachineLearning #AWS
