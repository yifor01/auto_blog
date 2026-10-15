---
title: Meta’s Muse Spark Open now available in Amazon SageMaker JumpStart
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/metas-muse-spark-open-now-available-in-amazon-sagemaker-jumpstart/
model: claude-code/sonnet
generated_at: '2026-10-15T20:53:31.634541'
score: 82
---

📌 【Meta Muse Spark Open】816B Coding Agent 模型登陸 AWS SageMaker

TL;DR：Meta 的 agentic coding 模型 Muse Spark Open 上架 SageMaker JumpStart，可一鍵部署到自己的 AWS 帳戶。

🎣 一個宣稱擁有 816B 參數的模型，推論時卻只動用其中 42B，聽起來像是數字遊戲。但當它同時能吃下 1M tokens 的上下文、讀懂整個 repo 的相依關係與歷史程式碼時，問題就不再是參數量夠不夠大，而是：這麼大的模型，要怎麼部署才划算？

🤔 **為 debugging 與 refactor 而生的模型**

Meta 將 Muse Spark Open 定位為 coding-optimized 的 agentic 模型，訓練素材取自真實的開發者工作流程：多檔案 refactor、長時間 debugging，以及需要跨越整個專案脈絡才能完成的任務。有了 1M tokens 的 context window，使用者不必再把一個任務拆成好幾段餵給模型，整個專案（包含相依套件與歷史程式碼）都能一次放進去。

🧩 **MoE 架構與兩種部署規格**

Muse Spark Open 採用 mixture-of-experts（MoE）架構，總參數量 816B，每個 token 僅啟動其中 42B，因此它擁有大型網路的容量，但單 token 的運算成本接近小得多的 dense 模型。這是一個 reasoning 模型，輸入支援文字、圖片、文件、音訊與影音，輸出為文字；SageMaker JumpStart 提供兩個變體：

| 變體 | 權重格式 | 部署機型 |
|---|---|---|
| Muse-Spark-Open-816B-A42B | BF16 | ml.p6-b300.48xlarge |
| Muse-Spark-Open-816B-A42B-NVFP4 | NVIDIA 4-bit 浮點量化 | ml.p5e.48xlarge |

由於 sparse activation 省下的是運算量，而不是記憶體，伺服端仍必須有足夠的 GPU 記憶體放下全部 816B 參數；NVFP4 量化後的權重大小約為 BF16 的四分之一，因此成為評估成本時該優先嘗試的版本。Meta 以 Muse Model License（內含 Muse Spark Usage Policy）釋出權重，模型屬於 gated model，部署前須同意 EULA。

📊 **部署流程：從 Studio 點擊到一次推論**

透過 SageMaker Studio 的模型詳情頁，或是 SageMaker Python SDK（設定 accept_eula=True），都能把模型部署成你 AWS 帳戶內的即時 endpoint，整個佈建與載入權重的過程約需 15–20 分鐘。Endpoint 接受 OpenAI 相容的 chat payload，回應中的 message.content 是最終答案，message.reasoning_content 則是模型的推理過程，usage.reasoning_tokens 會回報推理耗用的 token 數；由於這是 reasoning 模型，呼叫時要替 max_tokens 留出推理與最終回答的空間。Endpoint 也支援串流，在 request body 加上 "stream": true 並呼叫 invoke_with_response_stream 即可。

💡 **把模型留在自己的 VPC 裡**

因為模型跑在使用者自己帳戶的 endpoint 上，原始碼與 prompt 的處理可以綁定自己設定的 VPC，用 KMS 金鑰加密儲存磁碟，並開啟容器的網路隔離；版本也能鎖定，模型只有在重新部署時才會改變行為。對需要把程式碼與內部資料留在自己基礎設施內的團隊，這種「開放權重＋自管 endpoint」的組合，比呼叫第三方 API 多了一層可控性。

⚠️ **別忘了關掉 endpoint**

承載 Muse Spark Open 的都是多 GPU 大型機型，計費方式是按 endpoint 執行時間，不論有沒有在處理請求都會持續計費，用完務必刪除 endpoint、模型與 endpoint configuration。

🎯 **實務啟示**

這篇文章本身是部署教學而非模型研究，Meta 才是模型的訓練方，AWS 提供的是即插即用的託管層。真正要判斷值不值得用，仍得拿自己的 repo 去跑過 BF16 與 NVFP4 兩個版本，比較品質與成本後再決定要用哪個機型上生產。

🔗 **來源**
- 標題：Meta's Muse Spark Open now available in Amazon SageMaker JumpStart
- 作者／機構：Aris Tsakpinis（AWS ML Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/metas-muse-spark-open-now-available-in-amazon-sagemaker-jumpstart/

#MuseSparkOpen #Meta #AmazonSageMaker #MoE #CodingAgent #OpenWeightModels #LLMDeployment #AgenticAI #NVFP4 #AWS
