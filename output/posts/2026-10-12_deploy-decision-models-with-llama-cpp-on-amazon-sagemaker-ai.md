---
title: Deploy decision models with llama.cpp on Amazon SageMaker AI
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/deploy-decision-models-with-llama-cpp-on-amazon-sagemaker-ai/
model: claude-code/sonnet
generated_at: '2026-10-12T23:56:03.298889'
score: 85
---

📌 用 llama.cpp 在 Amazon SageMaker AI 上部署決策模型：一份模型，兩種服務形態

TL;DR：同一份 GGUF 模型，既能跑 OpenAI 相容對話，也能直接吐出選項機率做路由決策。

路由請求、挑選 agent 動作、判定政策結果，這類應用要的往往不是一段生成文字，而是「在幾個固定選項裡，每個選項的機率是多少」。AWS 這篇文章示範了怎麼用同一個 llama.cpp 容器，同時服務這兩種截然不同的需求。

🤔 要解決的問題
生成式對話 API 回傳的是一段文字，應用端還要自己解析、猜測模型選了哪個選項。這篇文章延續 AWS 針對生成式 AI 推論打造的專用 Deep Learning Container（DLC）系列（先前已涵蓋 WhisperX、vLLM-Omni 兩篇），這次聚焦 llama.cpp：先用 AWS 官方 llama.cpp DLC 透過 SageMaker AI 的 InvokeEndpoint 提供 OpenAI 相容的 chat completions，再用 SemIf（前身叫 OpenJev）這個擴充，讓同一套 runtime 能在不解碼任何答案 token 的前提下，直接回傳每個候選選項的機率。

🧩 兩條部署路徑，同一份模型
標準路徑很直接：把模型打包成 model.tar.gz 放上 Amazon S3，直接引用官方發布的 DLC 映像檔。容器會自動找出 /opt/ml/model 底下第一個 .gguf 檔，把 POST /invocations 對應到 llama-server 的 /v1/chat/completions，並把 SM_LLAMA_CPP_* 環境變數轉換成 llama.cpp 的啟動參數。請求格式就是標準的 OpenAI Chat Completions schema（messages 陣列加上 max_tokens、stream 等生成參數），回應也是標準的 choices 陣列，從 choices[0].message.content 讀出生成文字。

但 llama-server 的 HTTP API 並不會把最後一個位置的 logits 與內部狀態操作暴露出來，而這正是 SemIf 需要的東西。因此結構化決策路徑改用 AWS CodeBuild 建置一個子映像檔，存進 Amazon ECR：子映像檔沿用原本 DLC 已編譯好的 CPU／CUDA 函式庫，只是把進入點換成相容 SageMaker 的 adapter。SemIf 的請求格式不是對話訊息，而是一組決策 schema：呼叫端自訂的 ID、一段非結構化的 state、一個問題，以及一組排好順序的允許選項。回應則會依同樣順序回傳 option_ids、probabilities 與原始 option_logits，外加 prompt、時間與固定模型版本的中繼資料。有了穩定的選項 ID，應用端就能直接套用門檻值、fallback 與政策檢查，不必再解析生成式文字。

💡 SemIf 不是唯一一種做法
文章指出，SemIf 屬於一整類「從非結構化 state 為應用自訂結果打分」的決策模型，同類實作還包括 TypeSafe 的 Jev（搭配 /v1/systemone API）、為相容 TypeSafe API 設計的模型伺服器 Kev，以及專為 agent workflow 設計、具校準輸出的 Strands Decider 2B。適合套用這套模式的場景包括：把案件路由到對的佇列、從已知集合中抽出單一值、判定事件優先等級、檢查政策結果，或是挑選 agent 的下一步動作。授權邏輯與確定性的商業規則仍應放在模型之外，模型吐出的機率也要先驗證，才能當作營運上的信心指標。值得注意的是，拿掉答案 token 的生成並不代表省掉推論，模型仍需完整處理 state、問題與選項描述，才能讓 SemIf 讀出最後的 logits。

📊 CPU 與 GPU 的實測差距
文章用同一組 231 筆公開的 JevBench 任務，分別序列送往一個 CPU endpoint 與一個 GPU endpoint 測試。GPU endpoint 在 p50 快了 4.9 倍，在 p95 快了 32.2 倍。範例用 SageMaker AI 的 instance pools 功能，依優先序列出相容的 GPU 機型（g6e、g6、g5、g4dn），實際測試中 SageMaker 選到 ml.g6e.xlarge，啟動紀錄顯示 llama.cpp 把全部 34 層模型都卸載到一張 NVIDIA L40S 上。另外，CPU 與 GPU 映像檔用的是不同的 llama.cpp 編譯版本，在 6 道較難的任務上給出不同答案，文章特別提醒，這該視為執行環境的差異，而不是「GPU 卸載讓模型品質變好」的證據。模型大小方面，較小的模型確實降低了中位延遲，但 2B 與 0.8B 候選模型的準確率只有 66.7% 與 58.4%，因此範例仍以 4B、Q4_K_M 量化版本作為預設的「品質優先」選擇。

⚠️ 使用時機與限制
文章建議：只有生成式對話需求時，直接用標準 SageMaker 文字生成路徑就好；只有當你需要 SemIf 這種直接存取 logits、state 的能力時，才值得多建一個子映像檔。CPU 適合背景、離線、低流量且能忍受數秒延遲的場景；GPU 適合互動式決策、長 prompt，或是對尾端延遲（tail latency）要求嚴格的場景。實務上建議把 state 與選項描述寫得精簡，把共用同一個 state 的多個決策合併成一次請求（可重複利用相同的 prompt 前綴），並透過增加 endpoint 執行個體數來處理併發；adapter 在內部 llama.cpp context 滿載時，會回傳可重試的 HTTP 503，而不是讓請求佇列無限堆積。文中也提醒，這些測試數據包含網路延遲，並非正式的服務等級承諾，實際上線前仍應針對自己的決策情境重新 benchmark。

🎯 實務啟示
如果你的系統本來就要做路由、分類、優先權判定這類「固定選項打分」的工作，卻一直在用生成式 API 加上後處理去解析答案，這篇教學提供了一個更直接的替代方案：同一份量化模型，用 SemIf 這類 adapter 直接拿機率，省掉解析生成文字的不確定性，也能用 option_logits 做更細緻的信心門檻設計。

🔗 來源
- 標題：Deploy decision models with llama.cpp on Amazon SageMaker AI
- 作者／機構：Jyothirmai Kottu／AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/deploy-decision-models-with-llama-cpp-on-amazon-sagemaker-ai/

#AWS #SageMaker #llamacpp #DecisionModels #MachineLearning #MLOps #GPU #QuantizedModels #AIInfrastructure #AgentWorkflows
