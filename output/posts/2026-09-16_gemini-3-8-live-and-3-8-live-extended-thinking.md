---
title: Gemini 3.8 Live and 3.8 Live Extended Thinking
source: Hacker News
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/
model: claude-code/sonnet
generated_at: '2026-09-16T20:20:47.149745'
score: 88
---

📌 Google發布Gemini 3.8 Live，語音對話模型奪下Speech-to-Speech評測冠軍

TL;DR：Gemini 3.8 Live與Extended Thinking主打即時視覺理解與背景工具呼叫，在多項語音評測拿下第一。

當語音助理還在為「聽懂你在說什麼」而努力時，Google已經把重點轉向另一個問題：AI能不能一邊聽、一邊想、一邊動手做事，而不打斷對話節奏？這就是Gemini 3.8 Live與3.8 Live Extended Thinking想解決的問題。

🤔 **讓語音Agent真正能執行複雜任務**

Google將這兩款模型定位為「近即時推理」的進化：3.8 Live訴求規模化與成本效益，結合對話智慧、流暢對答與視覺理解（visual grounding）；3.8 Live Extended Thinking則訴求高複雜度任務，具備更強的智慧與多步推理能力。兩者的共同目標，是讓開發者與企業能建構可靠、可上生產環境的語音Agent，同時也讓一般使用者在Gemini App、Google Workspace與Search裡的語音互動更流暢、更有協作感。

🧩 **邊推理邊說話，背景執行工具呼叫**

3.8 Live能近即時處理視覺輸入，為對話補充上下文，並自動偵測、切換97種支援語言。它可以在背景執行工具與API呼叫，模型會先回應請求、持續對話，同時讓任務在背景完成，不需要使用者乾等。

面對需要更深入推理的任務，3.8 Live Extended Thinking採取「邊推理邊說話」的策略：用「讓我確認一下…」這類自然的口語提示先承接使用者的請求，並在多步驟背景任務進行時，用即時進度敘述帶著使用者一起走完整個流程，藉此在維持對話流暢度的同時完成更複雜的工作。

📊 **多項語音評測拿下第一**

根據Artificial Analysis的Speech to Speech Quality Index，3.8 Live Extended Thinking拿下總分82.6，排名第一；在τ-Voice上的agentic任務完成率達68.6%，在Sierra的τ-Voice-banking基準上為35.1%；在Big Bench Audio上的推理表現則達到97.7%。3.8 Live在Speech Agent Arena中則取得第二名的使用者偏好排名。在ServiceNow的EVA-Bench（用來評估語音Agent的基準）中，Google表示其模型在處理複雜工作流程時，成功在準確度與對話品質之間取得帕雷托最優（Pareto Frontier）的平衡。

💡 **開發生態系與企業導入**

透過Gemini Live API，Agora、Fishjam、LangChain、LiveKit、Pipecat、Vercel與Vision Agents等開發者平臺，能替開發者處理背後複雜的即時媒體串流基礎設施，讓開發者專注在使用者體驗設計上。Google也提到正與Salesforce、Genspark、Lumeris等公司合作，這些公司對3.8 Live系列的低延遲、流暢度與工具呼叫能力表示認可。此外，所有生成的音訊都以SynthID技術嵌入不可感知的浮水印，用於防止AI生成內容被誤用於製造不實資訊。

🎯 **實務啟示**

如果你要建構語音Agent，兩款模型分工明確：對話量大、追求成本效益與流暢度的場景適合3.8 Live；牽涉多步驟推理、需要背景任務協調（例如多步驟訂位、非同步函式呼叫）的場景則該用3.8 Live Extended Thinking。兩者都已透過Gemini API與Google AI Studio開放，並可與LiveKit、Pipecat、LangChain等現有語音框架直接整合，降低自建即時串流基礎設施的成本。

🔗 **來源**
- 標題：Gemini 3.8 Live and 3.8 Live Extended Thinking
- 作者／機構：Tom Ouyang（Principal Engineer）、Malini Jaganathan（Member of Technical Staff），代表Gemini Audio Team
- 連結：https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/

#Gemini #GoogleAI #VoiceAI #ConversationalAI #SpeechToSpeech #AIAgents #LiveAPI #MultimodalAI #VoiceAgents #GenerativeAI
