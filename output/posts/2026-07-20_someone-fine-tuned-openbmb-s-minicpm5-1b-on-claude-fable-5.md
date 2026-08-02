---
title: Someone Fine-Tuned OpenBMB’s MiniCPM5-1B on Claude Fable 5 Traces to Ship a
  657MB Local Thinking Model
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/19/someone-fine-tuned-openbmbs-minicpm5-1b-on-claude-fable-5-traces-to-ship-a-657mb-local-thinking-model/
score: 100
model: tencent/hy3:free
generated_at: '2026-07-20T08:50:21.378034'
---

📌 【社群專案】用 Claude 輸出微調 MiniCPM5-1B，推出 657MB 本地思考模型

TL;DR：開發者以 Fable 5 追蹤資料 SFT 小型基模，產出可離線執行的 1B 思考模型。

社群有人把一個 1B 等級的模型塞進筆電就能跑，還宣稱帶有「思考」能力、不連雲端。但它真的學到前沿推理了嗎？

🤔 **從 OpenBMB 基模出發的社群衍生版**

開發者 GnLOLot 發布了 MiniCPM5-1B-Claude-Opus-Fable5-Thinking，這是一個基於 openbmb/MiniCPM5-1B 的微調版本。基模本身是 OpenBMB 正式發布的密集式（dense）1.08B 參數模型，採用標準 LlamaForCausalLM 架構，具備 24 層、grouped-query attention，以及 131,072 token 的上下文長度。OpenBMB 在其對比集合中宣稱達到 1B 級開源 SOTA，且基模原生就帶有 thinking 模板，可透過 enable_thinking 切換 Think 與 No Think 模式。衍生模型保留了該模板與 MiniCPM5 的工具呼叫格式。

🧩 **不是蒸餾，是用教師輸出做監督式微調**

作者強調這不是古典蒸餾（distillation）。做法上是先用教師模型生成大量對話，擷取回覆與 reasoning traces 成為文字，再對較小的基模做 supervised fine-tuning（SFT）。由於沒有人能取得 Claude 的權重或 logits，因此這屬於「對生成輸出做 SFT」，而非權重層級的蒸餾。相對地，OpenBMB 原基模自身使用的是有檔案的 On-Policy Distillation 階段。衍生模型卡片寫明「further fine-tuned on Fable 5 data」以強化 coding 與指令遵循，GGUF 卡片則重述為「post-trained on Fable 5 data」。

⚠️ **1B 參數預算裝不下前沿推理**

實務上，這個 1B 模型學到的是回應格式與風格的模仿，而非教師模型底層的能力。1B 參數的規模無法容納 frontier-scale 的推理能力。上下文視窗繼承基模 config.json 的 131,072（即 128K）token。GGUF 版本提供給 llama.cpp 相容執行環境使用，不需 API key、不呼叫雲端。

🎯 **離線小模型的務實定位**

對工程師來說，這類專案適合做本地指令遵循與工具呼叫的原型驗證，但不要期待它具備與教師模型同等的解題深度。若要在邊緣裝置跑思考型任務，應把預期放在「格式與流程模仿」，而非能力轉移。

🔗 **來源**
- 標題：Someone Fine-Tuned OpenBMB’s MiniCPM5-1B on Claude Fable 5 Traces to Ship a 657MB Local Thinking Model
- 作者／機構：Michal Sutter @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/19/someone-fine-tuned-openbmbs-minicpm5-1b-on-claude-fable-5-traces-to-ship-a-657mb-local-thinking-model/

#LocalLLM #MiniCPM5 #FineTuning #SFT #SmallLanguageModel #EdgeAI #llamacpp #GGUF #ThinkingModel #OpenBMB
