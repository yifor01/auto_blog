---
title: 'Amazon SageMaker Inference: 2026 year-to-date launches in review'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-inference-2026-year-to-date-launches-in-review/
model: claude-code/sonnet
generated_at: '2026-09-19T19:30:04.899410'
score: 72
---

📌 AWS SageMaker Inference：今年七項更新怎麼幫你省下三週的調參時間

TL;DR：SageMaker AI 今年至今推出 13 項推理新功能，其中 7 項 managed endpoint 更新直接處理部署、容量、相容性與觀測性的老問題。

生成式 AI 推理有多難搞：模型動輒數十到數百 GB，延遲要用 tokens/sec 衡量，冷啟動可能長達數分鐘，GPU 容量吃緊，傳統監控工具還完全看不到 token 層級的訊號。AWS 這篇年度盤點，把 SageMaker AI 在 managed endpoint 路徑上的七項更新整理成一份清單，附帶不少實測數字。

🤔 **兩條部署路徑，按 instance 計費**

SageMaker AI 提供兩種部署方式：managed endpoints 讓 AWS 接手 GPU 佈建、擴縮與維運，使用者只要帶著模型和效能目標；SageMaker HyperPod Inference 則給需要 Kubernetes 原生控制權、管理專屬 GPU 叢集的團隊。兩者都是按 instance 計費而非按 token。今年至今合計交出 13 項新功能，這篇文章詳細走過 managed endpoint 那 7 項。

🧩 **七項更新逐一拆解**

- **Inference Recommendations**：自動化過去要花 2-3 週、手動跑 1000 多種組合才能決定的 instance 類型、serving 容器與最佳化設定。使用者指定模型與效能目標（成本、延遲或吞吐量），系統跑完三步驟流程後，輸出一份帶有驗證過指標的 SageMaker Model Package，包含 TTFT、ITL、P50/P90/P99 延遲百分位、吞吐量與成本預估。此功能本身不額外收費，有 ML Reservations 的客戶還能用保留容量免費跑測試。
- **Capacity-aware inference（instance pools）**：過去 endpoint 只綁定單一 instance 類型，一旦缺貨就整個開不起來。現在可設定最多 5 種優先順序的 instance 類型，在建立、scale-out、scale-in 各階段自動 fallback；每種 pool 項目還能對應各自的最佳化設定（高記憶體用 tensor parallelism、中階用 speculative decoding、小型 fallback 用量化）。支援 single-model、inference component、async endpoint，涵蓋所有商用 AWS 區域。
- **OpenAI 相容 API**：新增 `/openai/v1` 路徑，支援串流的 Chat Completions，遷移只需要改 endpoint URL，SDK 呼叫、串流邏輯、prompt 格式都不用動。用 AWS 憑證產生的 bearer token 最長可用 12 小時，省去 SigV4 簽章的複雜度。支援 vLLM、SGLang 的 AWS Deep Learning Containers 以及自建容器，涵蓋 14 個 AWS 區域。
- **Container caching**：自動擴縮時，新 instance 過去得先從 Amazon ECR 拉完整容器映像檔才能服務請求，超過 10 GB 的容器光拉取就多耗好幾分鐘。這項功能會預先快取映像檔，零設定、自動生效。實測案例是 Qwen3-8B 搭配 LMI 容器（壓縮後 17.7 GB）在 ml.g6.2xlarge 上，端到端啟動延遲從 525 秒降到 258 秒，降幅 51%，模型下載時間也從 168 秒降到 77 秒；早期使用客戶則觀察到 38% 到 65% 不等的改善幅度。
- **CloudWatch 詳細指標與 Insights 儀表板**：透過原生 OpenTelemetry 送出超過 100 項詳細推理指標，搭配預先建好的 Insights 儀表板，零額外埋點。新建的 endpoint 預設就開啟觀測性，進入 InService 狀態後兩分鐘內指標就會開始流入；同時提供 PromQL 相容端點，可直接接 Amazon Managed Grafana 或其他 PromQL 工具。
- **Async inference inline payload**：`InvokeEndpointAsync` API 現在可直接在請求中帶最多 128,000 bytes 的 Body 參數，多數 async 工作負載不再需要先把輸入上傳到 S3。好處是少一次網路往返、不用建 S3 bucket 和 IAM 授權、立即完成大小與參數驗證、省下每次呼叫的 S3 PUT 費用，且完全向下相容，涵蓋 31 個 AWS 區域。
- **Prefix-aware routing**：一種新的路由策略，把共用相同 prompt 前綴的請求導向同一臺 instance，藉此降低 LLM 延遲。

📊 **關鍵數字一覽**

| 功能 | 改善幅度 |
|---|---|
| Inference Recommendations（GPT-OSS-20B） | 相同延遲下吞吐量提升 2 倍 |
| Container caching（Qwen3-8B, ml.g6.2xlarge） | 啟動延遲 525 秒 → 258 秒（降 51%）；下載時間 168 秒 → 77 秒 |
| Container caching（早期使用客戶） | 改善幅度 38%-65% |
| Async inline payload | 上限 128,000 bytes，涵蓋 31 個區域 |

⚠️ **涵蓋範圍有限**

這篇文章只詳細介紹了 managed endpoint 路徑的 7 項更新，HyperPod Inference 那一側的其餘 6 項新功能素材中並未展開細節。部分功能也有區域限制，例如 OpenAI 相容 API 目前只在 14 個區域可用。

🎯 **實務啟示**

已經在用 SageMaker 的團隊可以優先檢查幾件事：用 Inference Recommendations 取代手動 benchmark 流程省下數週工時；用 instance pools 提升容量韌性；如果應用是建在 OpenAI SDK 之上，直接切到 `/openai/v1` 幾乎零成本遷移；container caching 屬於零設定自動生效，不需要額外動作就能拿到擴縮加速；小型 async 請求可以直接拿掉 S3 pre-staging 這層架構複雜度。

🔗 **來源**
- 標題：Amazon SageMaker Inference: 2026 year-to-date launches in review
- 作者／機構：Kareem Syed-Mohammed，AWS Machine Learning
- 連結：https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-inference-2026-year-to-date-launches-in-review/

#AWS #SageMaker #MLOps #LLMInference #GenerativeAI #CloudComputing #MachineLearning #ModelDeployment #Kubernetes #AIInfrastructure
