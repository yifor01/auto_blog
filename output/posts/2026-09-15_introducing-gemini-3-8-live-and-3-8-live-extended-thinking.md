---
title: Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking
source: Google DeepMind
url: https://deepmind.google/blog/introducing-gemini-3-8-live-and-3-8-live-extended-thinking/
model: claude-code/sonnet
generated_at: '2026-09-15T20:25:11.701895'
pinned: true
---

📌 【Google DeepMind 最新發布】Gemini 3.8 Live 能一邊想一邊說，還能背著你先做事

TL;DR：Gemini 3.8 Live 系列主打即時視覺理解與背景執行任務，多項語音 benchmark 拿下第一。

當你問語音助理一個複雜問題時，通常得等它想完才開口。Google DeepMind 這次推出的新模型，試圖打破這種「先想後說」的順序，讓 AI 一邊組織答案一邊開口回應，同時在背景默默把任務做掉。

🤔 **語音助理的老問題：思考會打斷對話**

Google DeepMind 發布 Gemini 3.8 Live 與 Gemini 3.8 Live Extended Thinking 兩款語音對話模型，目標是讓語音互動更自然流暢、更聰明。兩者定位不同：Gemini 3.8 Live 針對規模化與成本效率設計，結合對話智慧、流暢對話與視覺理解（visual grounding）；Gemini 3.8 Live Extended Thinking 則針對高複雜度任務，具備更強的智慧與多步驟推理能力。

🧩 **視覺理解、97 種語言、背景執行工具呼叫**

兩款模型共通的能力包括：近乎即時地處理視覺輸入，用畫面內容豐富對話上下文；自動偵測並在對話中途切換支援的 97 種語言；在背景執行工具與 API 呼叫，讓模型能先確認請求、繼續對話，同時任務在背後完成。對於需要更深度推理的任務，Extended Thinking 版本能做到「邊推理邊說話」，用「讓我查一下…」這類自然的口語提示來承接請求，並透過即時進度敘述帶使用者走過多步驟的背景任務。

📊 **多項語音 benchmark 排名**

| Benchmark | 模型 | 成績 |
|---|---|---|
| Artificial Analysis Speech to Speech Quality Index | 3.8 Live Extended Thinking | 82.6（整體第一） |
| τ-Voice（agentic 任務完成率） | 3.8 Live Extended Thinking | 68.6% |
| Sierra τ-Voice-banking benchmark | 3.8 Live Extended Thinking | 35.1% |
| Big Bench Audio | 3.8 Live Extended Thinking | 97.7% |
| Speech Agent Arena | 3.8 Live | 第二名 |

在 ServiceNow 的 EVA-Bench（評估語音 agent 的 benchmark）上，Google DeepMind 表示這兩款模型在準確度與對話品質之間取得平衡，把複雜工作流的 Pareto Frontier 往前推進。

💡 **「邊想邊說」在工程上意味著什麼**

對開發語音 agent 的工程師來說，這代表模型不再是「等待完整回應生成完畢才播放語音」的單一流程，而是把推理、工具呼叫、語音輸出拆成可以並行的多條路徑。Extended Thinking 版本用口語銜接詞先安撫使用者，再用進度敘述交代多步驟任務狀態，這種設計本質上是把 agent 的「思考中」狀態變得對使用者可見，而非黑箱等待。

🎯 **實務啟示**

Gemini 3.8 Live 已開放於 Gemini API、Google AI Studio、Search Live；3.8 Live Extended Thinking 則開放於 Gemini API、Google AI Studio、Gemini Live app，以及 Google Workspace 的 Docs Live（Google AI Pro/Ultra 訂閱）、Gmail Live 與 Keep Live。兩者在 Gemini Enterprise 皆為私有預覽階段。Google DeepMind 也提到 Agora、Fishjam、LangChain、LiveKit、Pipecat、Vercel、Vision Agents 等開發平臺已支援 Gemini Live API，讓開發者不必自己處理即時串流基礎設施。所有生成音訊都以 SynthID 浮水印標記，方便後續辨識 AI 生成內容。若你正在打造語音 agent，這是目前少數同時公布多項第三方語音 benchmark 成績的模型系列，值得納入選型比較清單。

🔗 **來源**
- 標題：Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking
- 作者／機構：Google DeepMind
- 連結：https://deepmind.google/blog/introducing-gemini-3-8-live-and-3-8-live-extended-thinking/

#GoogleDeepMind #Gemini #VoiceAI #ConversationalAI #LLM #AIAgents #SpeechRecognition #MultimodalAI #GeminiLive #AIBenchmark
