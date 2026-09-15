---
title: Build an AI-powered product tagging system with Amazon SageMaker serverless
  model customization
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-an-ai-powered-product-tagging-system-with-amazon-sagemaker-serverless-model-customization/
model: claude-code/sonnet
generated_at: '2026-09-15T20:32:13.513536'
score: 91
---

📌 微調小模型，打造零伺服器產品標籤系統

TL;DR：AWS 示範用 SFT+GRPO 微調 Qwen3-8B 做產品標籤，比找前沿大模型下 prompt 更划算。

零售目錄裡的商品名稱、描述、分類路徑來自四面八方且持續變動，人工替上千個 SKU 貼標籤又慢又難保持一致。找前沿大模型寫 prompt 固然能生成標籤，但如果任務本身只需要「在固定 schema 裡回傳正確屬性」，而且輸出可以程式化評分，那麼客製化一個開源小模型往往是更合適的選擇。

🤔 為什麼不用前沿大模型硬解

當分類體系（taxonomy）穩定、輸出格式固定時，通用大模型的廣泛能力其實用不到。與其每次呼叫都為用不到的能力付費，不如直接把 schema 教給小模型，並針對「漏標」與「多標」這兩種錯誤之間的取捨做最佳化。

🧩 SFT 打底，GRPO 修正細節

整套流程刻意拆成三個獨立環節：資料準備、模型客製化、推論服務。資料先用 Amazon SageMaker Processing job 做一次性轉換，讀取 Amazon S3 上的原始檔（此例採用 Kaggle 的 Amazon Sales Dataset，含超過 1,000 筆商品紀錄），正規化商品文字與分類路徑，過濾不可用的資料列，映射成既有的九大類標籤目標，切分訓練／驗證集後寫回 JSONL，並註冊為 Amazon SageMaker AI Registry 中的版本化資料集。每筆 SFT 資料是一個 messages 陣列：system 與 user 組成 prompt，最後的 assistant 內容則是監督式學習的目標答案。

第一階段用 SFTTrainer（Amazon SageMaker Python SDK v3 的無伺服器客製化訓練工具）套用 LoRA，讀取已註冊資料集的 ARN 進行監督式微調（SFT），讓 Qwen3-8B 先學會指令對應標籤的基本模式。第二階段接續 SFT 產出的模型套件，改用 RLVRTrainer 進行 RLVR（reinforcement learning with verifiable rewards），以 Group Relative Policy Optimization（GRPO）針對剩餘的品質取捨做強化。RLVR 資料把 SFT 那一列的 assistant 內容移到 reward_model.ground_truth 當作參考答案，每列附上 split-aware ID，並在 extra_info 保留答案供評分器使用。GRPO 對每個 prompt 產生一組候選回答（此例 rollout_n=8），評分器獨立為每個候選打分，GRPO 再計算組內相對優勢，並以 KL 正則化限制模型偏離 SFT 參考模型太遠。

📊 用可驗證的獎勵函式取代人工判斷

獎勵函式是決定性（deterministic）的：先檢查是否符合九大類輸出格式，再用 0.5 門檻的模糊比對（fuzzy matching）比較預測標籤與參考答案，公式為：

Overall = 0.30 × recall + 0.30 × precision + 0.30 × accuracy + 0.05 × match_quality + 0.05 × formatting

訓練過程採漸進式獎勵排程：早期偏重 recall，讓模型先學會不要漏標;後期加重 precision，讓模型學會不要多標出沒有依據的屬性。這等於把「漏標 vs. 多標」這個業務取捨直接寫進獎勵設計，而不是隱含在 prompt 措辭裡。整個訓練過程用 MLflow 搭配 model package group 追蹤超參數、獎勵權重、指標與模型血緣，方便比較 SFT 與 RLVR 版本並重現選定的模型。

💡 訓練無伺服器，推論仍要備妥算力

值得注意的是，「無伺服器」在這個案例中只指訓練階段：SFT 與 RLVR 都由 Amazon SageMaker serverless model customization 代管訓練容量，不需自行選擇 GPU 執行個體。但最終服務走的是 Amazon SageMaker Asynchronous Inference，架設在一臺 provisioned 的 ml.g6.2xlarge 執行個體上，搭配自訂的 vLLM 映像檔，適合可以排隊、非即時的批次型目錄增補作業;推論請求以 OpenAI 相容格式送出，較大的負載可先上傳到 Amazon S3，再用 S3 URI 呼叫並輪詢 OutputLocation。

⚠️ 這是一個示範，不是現成產品

文中示範採用 temperature=0，且未預設自動擴縮政策;若要正式上線,仍需依佇列深度自行加上 Asynchronous Inference 的 autoscaling 設定。

🎯 實務啟示

當分類體系穩定、輸出能被程式化評分時，與其持續為前沿大模型的通用能力付費，不如把 schema 直接教給小模型，並用 RLVR 的獎勵權重把業務端在意的精確率／召回率取捨明確寫進訓練訊號中。

🔗 來源
- 標題：Build an AI-powered product tagging system with Amazon SageMaker serverless model customization
- 作者／機構：Linpo Guo（AWS）
- 連結：https://aws.amazon.com/blogs/machine-learning/build-an-ai-powered-product-tagging-system-with-amazon-sagemaker-serverless-model-customization/

#AI #MachineLearning #AmazonSageMaker #LLM #FineTuning #GRPO #ReinforcementLearning #Qwen3 #AWS #ProductTagging
