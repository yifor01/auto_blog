---
title: Thinking Machines amps up its bet against one-size-fits-all AI with its first
  open model, Inkling
source: TechCrunch AI
url: https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/
score: 99
model: tencent/hy3:free
generated_at: '2026-07-16T08:12:42.784591'
---

📌 【Thinking Machines 首款開放權重模型 Inkling】反對一刀切 AI 的 MoE 路線

TL;DR：前 OpenAI CTO 創辦的 Thinking Machines 釋出開放權重模型 Inkling，可自訂思考強度。

當主流實驗室都在賣「一個模型通吃」的封閉旗艦，有一間新創反其道而行，把模型權重直接交給開發者改。

🤔 **從封閉旗艦到開放權重：一種不同的賭注**

Thinking Machines Lab 由前 OpenAI CTO Mira Murati 創辦，週三上午釋出首個自研模型 Inkling。不同於 OpenAI、Anthropic 或 Google 的旗艦模型，Inkling 是 open-weight（開放權重），外部開發者與企業可直接下載並修改。這也是該公司潛心打造 AI 基礎設施一年半以來，第一個公開的實證。

🧩 **975B 引數的 MoE，每次只動用 41B**

Inkling 採用 mixture-of-experts（MoE，混合專家）架構，總引數達 9750 億，但單一任務只呼叫其中約 410 億引數。這種常見設計能讓極大模型在推理時更快、更省成本。公司發布資料稱，模型以 45 兆 tokens 的文、圖、音、影資料訓練，並原生跨這四種模態推理；不過目前輸出僅限文字，包含程式碼、帶樣式的成品與結構化資料。

💡 **可校正不確定性，思考強度自己調**

Inkling 設計上會給出經校準（calibrated）的答案，包含主動標註不確定性而非硬猜；使用者也能依需求調高或調低「thinking effort（思考強度）」來換取速度。公司表示，在某項基準上，Inkling 達到相同程式碼效能所耗 tokens 僅為 Nvidia 最新開放權重模型 Nemotron 3 Ultra 的三分之一。

⚠️ **公司自己說：不是最強，但要全面均衡**

Thinking Machines 並未宣稱 Inkling 是頂尖模型，其最新部落格明確寫道：Inkling「不是當前最強的整體模型，無論開放或封閉」。他們顯然追求的是 well-rounded（全面均衡）表現，而非單點極致。

🎯 **實務啟示**

對工程師而言，Inkling 的開放權重意味著可針對組織內部場景 fine-tuning 或修改；可調思考強度也方便在延遲敏感與品質優先的任務間切換。若你的需求剛好是「可自適應、非黑箱」而非「排行榜最高分」，這類模型比通用封閉 API 更值得評估。

🔗 **來源**
- 標題：Thinking Machines amps up its bet against one-size-fits-all AI with its first open model, Inkling
- 作者／機構：Connie Loizos @ TechCrunch AI
- 連結：https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/

#AI #OpenWeight #MoE #Inkling #ThinkingMachines #LLM #ModelRelease #FineTuning #AIBenchmark #OpenSourceAI
