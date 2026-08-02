---
title: 'Thinking Machines Lab Releases Inkling: A 975B-Parameter Open-Weights Multimodal
  MoE With 41B Active Parameters And Controllable Thinking Effort'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/15/thinking-machines-lab-releases-inkling-a-975b-parameter-open-weights-multimodal-moe-with-41b-active-parameters-and-controllable-thinking-effort/
score: 102
model: tencent/hy3:free
generated_at: '2026-07-16T08:11:36.828072'
---

📌 【Thinking Machines Lab 釋出 Inkling】975B 多模態 MoE 開放權重，思考力可調

TL;DR：Inkling 是 975B 參數開放權重多模態 MoE，41B 活化參數，主打可微調客製化。

當多數實驗室把最強模型鎖在 API 後面，Thinking Machines Lab 直接把從零訓練的 975B 參數多模態模型權重開放出來，還說「這只是拿來給你改的基底」。

🤔 **從零訓練、開放權重，定位在客製化基底**

Inkling 是 Thinking Machines Lab 第一個從頭訓練的模型，權重開放、可在 Tinker 上 fine-tune。實驗室將它定位為「客製化的基礎」，強調 customization / fine-tuning 是核心差異點，因此架構本身值得關注。

🧩 **66 層解碼器 MoE，每 token 喚醒 6 個路由專家**

模型為 decoder-only transformer，共 66 層，採稀疏 MoE feed-forward 主幹。每個 MoE 層含 256 個 routed experts 與 2 個 shared experts；每個 token 啟用 6 個 routed experts，2 個 shared experts 則對每個 token 都啟用。路由用 sigmoid-based router，搭配 auxiliary-loss-free 的負載平衡 bias；routed 與 shared 分數聯合正規化後加權合併輸出。MoE 設計大致沿用 DeepSeek-V3。

⚠️ **注意力層不走常規：滑窗與全域性交錯、不用 RoPE**

Attention 與常規不同：sliding-window 與 global layers 以 5:1 比例交錯，配 8 個 KV heads。位置編碼用 relative positional embedding 而非 RoPE，實驗室表示外推效果更好。key、value 投影後與 residual 分支輸出都會接 short convolutions。

🧩 **無編碼器的多模態：音訊與影像直接投影進解碼器**

多模態為 encoder-free。音訊以 dMel spectrograms 輸入，影像經四層 hMLP 切成 40×40 pixel patches；兩者皆由輕量 embedding 層投影，再與文字 token 一起由 decoder 聯合處理。輸入支援文字、影像、音訊，輸出僅 UTF-8 文字。

📊 **預訓練規模與小模型預覽**

Pretraining 涵蓋 45 trillion tokens 的文字、影像、音訊、影片；context window 最高 1M tokens。實驗室也預覽 Inkling-Small：276B 參數 MoE、12B 活化參數，多數 benchmark 持平或超越大型版本，權重待測試結束後釋出。

🧩 **訓練與後訓練設定**

訓練在 NVIDIA GB300 NVL72 系統上進行，大矩陣權重用 Muon、其餘參數用 Adam。後訓練從 SFT 起步，使用合成資料，包含由 Kimi K2.5 生成的資料；摘要指出多數運算（most compute）投入此階段，但未說明細節。

🎯 **實務啟示**

對想自建領域模型的團隊，Inkling 提供一個開放權重、支援百萬上下文與多模態輸入的大規模基底，可在 Tinker 上 fine-tune。其可控活化參數（41B / 12B）與可客製定位，適合做為自架推論與下游微調的起點，但仍需等權重與基準細節完整公開再評估實際成本。

🔗 **來源**
- 標題：Thinking Machines Lab Releases Inkling: A 975B-Parameter Open-Weights Multimodal MoE With 41B Active Parameters And Controllable Thinking Effort
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/07/15/thinking-machines-lab-releases-inkling-a-975b-parameter-open-weights-multimodal-moe-with-41b-active-parameters-and-controllable-thinking-effort/

#Inkling #ThinkingMachinesLab #MoE #OpenWeights #Multimodal #LLM #FineTuning #MixtureOfExperts #Transformer #AI
