---
title: 'Soofi Consortium Releases Soofi S 30B-A3B: An Open Hybrid Mamba-Transformer
  MoE Foundation Model For German And English'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/15/soofi-consortium-releases-soofi-s-30b-a3b-an-open-hybrid-mamba-transformer-moe-foundation-model-for-german-and-english/
score: 101
model: tencent/hy3:free
generated_at: '2026-07-16T08:12:26.514005'
---

📌 【Soofi Consortium 開源】Soofi S 30B-A3B：德英雙語混合 Mamba-Transformer MoE 基礎模型

TL;DR：開放德英 base model，31.6B 引數每 token 僅啟用 3.2B，開源基礎模型中雙語均分最高。

當多數開源基礎模型仍由英語語料主導，一組德國研究聯盟直接發表了一個專為德語與英語設計、且號稱在完全開放 base model 中雙語總分最高的模型——而且它把 Mamba-2 與 MoE 塞進了同一個架構裡。

🤔 **德國聯盟打造、全程在慕尼黑工業雲訓練的開放模型**

Soofi Consortium 發布了 Soofi S 30B-A3B 的預訓練報告，這是一個針對德語與英語的開放 base model。整段訓練在 Deutsche Telekom 位於慕尼黑的 Industrial AI Cloud 端到端完成，預覽權重已放上 Hugging Face。報告指出，在部分受測的完全開放 base model 中，Soofi S 拿下最高的英語與德語綜合分數。

🧩 **52 層混合堆疊：Mamba-2、MoE 與少量 GQA**

Soofi S 是一個 Mixture-of-Experts (MoE) 混合 Mamba Transformer 基礎模型，總引數約 31.6B，每個 token 啟用約 3.2B。網路共有 52 層，組成如下：

- 23 層 Mamba-2 sequence-mixing 層
- 23 層 granular MoE 層
- 6 層 Grouped-Query Attention (GQA) 層（僅這 6 層維護 KV cache）

每個 MoE 層包含 128 個 routed experts，每 token 啟用 6 個，並額外加上 2 個 shared experts。其他架構細節：model dimension 為 2688、使用 squared ReLU、RMSNorm，且沒有 positional embeddings。

⚙️ **沿用 Nemotron 3 Nano 參考設計，只動資料配方**

Soofi S 直接採用 Nemotron 3 Nano 的參考設計且未修改。研究團隊給出三個理由：可在 vLLM 等堆疊上部署、服務效能（serving efficiency）、以及科學控制（scientific control）。因為骨幹固定，Nemotron 3 Nano 成為架構完全相同的 baseline，唯一的變因是資料配方。

資料訓練遵循 Warmup–Stable–Decay (WSD) 排程，並帶有 minus_sqrt decay 段：

- 階段 1：約 20T tokens，多樣且分級品質的語料混合，學習率在 1e-3 高原期
- 階段 2：約 6.58T tokens 高品質退火資料，學習率從 1e-3 降到 1e-5，再維持常數 1e-5
- 階段 3：約 0.10T tokens，序列長度 1,048,576，將可用上下文視窗延伸至 1M tok

⚠️ **純 base model，無指令與安全微調**

需特別留意，Soofi S 作為 base model，並未進行 instruction tuning、alignment 或 safety tuning。這代表它不適合直接當作對話助手使用，工程師需自行後續微調。

🎯 **實務啟示**

對需要在德語與英語場景下自建模型的團隊，Soofi S 提供了一個架構透明、權重開放且聲稱雙語基準領先的起點。其固定骨幹搭配可替換資料配方的設計，也方便研究者做受控的訓練實驗；但部署前務必規劃後續對齊與安全處理。

🔗 **來源**
- 標題：Soofi Consortium Releases Soofi S 30B-A3B: An Open Hybrid Mamba-Transformer MoE Foundation Model For German And English
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/15/soofi-consortium-releases-soofi-s-30b-a3b-an-open-hybrid-mamba-transformer-moe-foundation-model-for-german-and-english/

#Mamba #MoE #Transformer #FoundationModel #OpenWeights #German #English #Nemotron #Pretraining #Soofi
