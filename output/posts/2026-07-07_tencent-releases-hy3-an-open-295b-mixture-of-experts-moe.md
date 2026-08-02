---
title: 'Tencent Releases Hy3: An Open 295B Mixture-of-Experts (MoE) Model with 21B
  Active Parameters and 256K Context'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/06/tencent-releases-hy3-open-295b-moe-model/
score: 105
model: google/gemma-4-31b-it:free
generated_at: '2026-07-07T21:02:47.248367'
---

📌 【Tencent 最新釋出】Hy3 開源 295B MoE 模型：256K 長上下文與 MTP 加速推理

TL;DR：騰訊推出 295B 參數 MoE 模型 Hy3，僅 21B 啟用參數，支援 MTP 加速與 FP8 量化。

面對超大規模模型部署時，運算成本與推理速度始終是工程師的痛點。騰訊 Hy 團隊推出的 Hy3 試圖在維持強大推理能力與降低運算開銷之間取得平衡。

🧩 **192 個專家與 MTP 層的架構設計**

Hy3 採用稀疏 MoE (Mixture-of-Experts) 架構，總參數達 295B，但透過 top-8 路由機制，每個 token 僅會啟用 8 個專家，使單次推理的啟用參數降至 21B，有效降低運算量。

此外，Hy3 引入了 Multi-Token Prediction (MTP) 層，允許模型一次預測多個 token 以提升解碼速度。目前 vLLM 與 SGLang 已透過 speculative decoding (投機取樣) 支援此功能。

📊 **在 Coding 與 STEM 領域展現強大推理力**

研究團隊在多項基準測試中公佈了 Hy3 的表現，特別是在軟體工程與理科推理方面：

- **Coding 表現**：SWE-Bench Verified 取得 78.0 分，SWE-Bench Pro 為 57.9，SWE-Bench Multilingual 為 75.8。此外，Terminal-Bench 2.1 達 71.7，DeepSWE 為 28.0。
- **STEM 與推理**：GPQA Diamond 達 90.4，IMOAnswerBench 達 90.0，USAMO 2026 取得 72.0，而使用工具後的 HLE 達 53.2。

在針對 270 位專家的盲測中（共 312 組真實工作流對比），Hy3 的評分（2.67/4）領先 GLM-5.1（2.51/4），在前端開發、CI/CD 以及資料儲存等場景的優勢最為明顯。

💡 **生產環境的可靠性與部署最佳化**

Hy3 針對生產環境的可靠性進行了最佳化，直接處理了三種失效模式。針對部署，官方提供了以下支援：

- **記憶體最佳化**：提供 Hy3-FP8 檢查點，降低記憶體佔用，降低伺服器部署成本。
- **部署框架**：支援 vLLM 與 SGLang，並提供 OpenAI 相容 API。
- **推理控制**：透過 `reasoning_effort` 標記控制思考深度。使用 `no_think` 獲取直接答案，或使用 `high` 處理數學、程式碼等複雜多步驟任務。
- **建議參數**：建議設定 `temperature=0.9` 與 `top_p=1.0`。

🎯 **實務啟示：如何快速上手 Hy3**

對於需要處理長上下文（256K）或 Agent 工作流的工程師，Hy3 提供了較靈活的部署選擇。若無本地硬體，可透過 OpenRouter 的 `tencent/hy3:free` 路由進行測試（該免費額度將於 2026 年 7 月 21 日結束）。

🔗 **來源**
- 標題：Tencent Releases Hy3: An Open 295B Mixture-of-Experts (MoE) Model with 21B Active Parameters and 256K Context
- 作者／機構：Asif Razzaq / MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/06/tencent-releases-hy3-open-295b-moe-model/

#Tencent #Hy3 #MoE #OpenSource #LLM #MultiTokenPrediction #vLLM #SGLang #FP8 #CodingAssistant
