---
title: 'AMD Releases Instella-MoE-16B-A3B: A Fully Open Mixture-of-Experts LLM With
  2.8B Active Parameters Trained On Instinct GPUs'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/01/amd-instella-moe-16b-a3b-fully-open-mixture-of-experts-llm/
model: tencent/hy3:free
generated_at: '2026-08-02T08:00:42.519378'
score: 98
---

📌 【AMD 全新開源】Instella-MoE-16B-A3B：用 2.8B 參數實現高效能 MoE 架構

TL;DR：AMD 發布全開源 MoE 模型，透過系統級設計實現 12.7% 訓練加速與顯著推理效能提升。

AMD 釋出了全新開發的 Instella-MoE-16B-A3B 模型，這是一個完全開源的 Mixture-of-Experts (MoE) 語言模型。該模型不僅從頭開始訓練，更展現了在 Instinct GPU 上的強大實作能力，對需要高性能且高透明度的研究人員來說，這是一個極具價值的開源資產。

🧩 **16B 總參數僅需 2.8B 運算：高效能 MoE 架構設計**

Instella-MoE 採用 Decoder-only 架構，具備 27 層、2048 隱藏層維度（hidden size）以及 128,896 個 token 的詞彙表。其核心設計如下：

- **MoE 結構**：每個 MoE 層包含 2 個共享專家（shared experts）以及從 64 個專家中選出的 6 個路由專家（routed experts）。
- **運算效率**：雖然總參數達 16B，但每個 token 僅需啟動 2.8B 參數，大幅降低運算成本。
- **關鍵技術創新**：
  - **Gated MLA (Multi-head Latent Attention)**：在 MLA 基礎上加入輕量級的學習輸出閘（learned output gate），透過線性投影（linear projection）得出輸入條件閘，並在輸出投影前進行乘法運算。
  - **FarSkip-Collective 連結技術**：將過時或部分的 activations 傳遞至 MoE 與 attention 層，藉此將專家並行（expert-parallel）的通訊與運算進行重疊（overlap）。

📊 **訓練與評估：在多項指標中領先全開源模型**

該模型在 Instinct MI300X 與 MI325X GPU 上進行訓練，並在多個階段進行優化：

- **訓練流程**：
  - **預訓練**：使用 7.1T tokens（包含 Nemotron-CC-v2、MegaMath 等資料集）。
  - **中段訓練**：使用 Dolma3 資料集進行權重平均（weight averaging）。
  - **長文本擴展**：透過 YaRN 與增加 RoPE theta，將上下文窗口從 4K 擴展至 64K。
  - **後訓練（Post-training）**：經歷 SFT、DPO 以及基於 Miles 框架的強化學習（RL），並透過 Multi-Teacher On-Policy Distillation 整合增益。
- **效能數據**：
  - **訓練加速**：預訓練速度提升 12.7%。
  - **推理效能**：在使用專家並行時，首字延遲（time to first token）最高可減少 39.2%。
  - **基準測試**：Base 模型平均分數為 76.7，在全開源模型中表現最強（優於 Moonlight-16B-A3B 與 OLMo 系列），但在 Qwen3.5-4B-Base (79.5) 之後。
  - **程式碼與邏輯能力**：在 HumanEval+ 獲得 65.7 分；在 WinoGrande 獲得 86.5 分。

⚠️ **使用限制與授權**

需要注意的是，雖然 AMD 釋出了訓練各階段的權重、資料組合、訓練配置與推理程式碼，但**模型權重僅根據 ResearchRAIL 授權，僅限學術與研究用途，並非直接可用的商業模型**。不過，其訓練程式碼採用 MIT 授權，對工程師而言是極具重用價值的技術資源。

🎯 **實務啟示**

對於研究者而言，Instella-MoE 的價值不在於直接部署商業產品，而於其「透明度」。AMD 提供了從預訓練到強化學習的完整技術細節與程式碼，這對於想要優化 MoE 架構、研究系統級通訊（如 FarSkip-Collective）或探索長文本擴展技術的工程師來說，是極佳的參考範本。

🔗 **來源**
- 標題：AMD Releases Instella-MoE-16B-A3B: A Fully Open Mixture-of-Experts LLM With 2.8B Active Parameters Trained On Instinct GPUs
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/01/amd-instella-moe-16b-a3b-fully-open-mixture-of-experts-llm/

#AMD #MoE #LLM #MachineLearning #OpenSource #InstinctGPU #AIResearch #DeepLearning #Transformer #LargeLanguageModels
