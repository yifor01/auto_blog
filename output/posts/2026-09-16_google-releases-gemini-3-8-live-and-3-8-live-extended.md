---
title: Google Releases Gemini 3.8 Live and 3.8 Live Extended Thinking for Production
  Grade Voice Agents
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/15/google-releases-gemini-3-8-live-and-3-8-live-extended-thinking-for-production-grade-voice-agents/
model: claude-code/sonnet
generated_at: '2026-09-16T20:17:41.507351'
score: 92
---

📌 Google發布Gemini 3.8 Live，語音Agent推理與說話同時進行

TL;DR：Google推出Gemini 3.8 Live與Extended Thinking，原生語音對語音模型讓voice agent邊思考邊回話，Speech to Speech Quality Index拿下全球第一。

語音agent長期以來卡在一個矛盾：要讓它一邊推理、一邊呼叫工具，又不能打斷對話的流暢度。Google這次發布的Gemini 3.8 Live系列，正是針對這道縫隙而來。

🤔 取代串接式語音管線的原生方案

Gemini 3.8 Live與Gemini 3.8 Live Extended Thinking是Google目前最先進的即時對話模型，屬於原生語音對語音（speech to speech）架構，是繼上月Gemini 3.5 Transcribe之後Gemini Audio家族的最新成員。Google將兩者定位為傳統ASR→LLM→TTS串接式語音管線的替代方案。兩款模型皆已在Gemini Live API與Google AI Studio上線，僅提供託管服務，沒有開放權重可自行部署。

🧩 兩款模型，各司其職

Gemini 3.8 Live鎖定規模化與成本效率，結合對話智能、流暢對答與視覺理解（visual grounding）。Gemini 3.8 Live Extended Thinking則針對高複雜度任務，在說話的同時加入多步驟推理能力。

Extended Thinking的核心設計是「邊想邊說」：模型會先用「讓我確認一下」之類的口頭提示回應使用者，再逐步敘述長任務執行的進度，背景則持續進行可配置的多步驟推理。Google展示的demo包括把手繪草圖搭配語音回饋轉換成可運作的React元件，以及協調多步驟的訂位／預約流程。Live API總共開放5項核心能力，Extended Thinking的可配置推理是其中之一。

📊 語音品質與agent任務雙雙拿下高分

| 基準 | 成績 |
|---|---|
| Speech to Speech Quality Index（Artificial Analysis） | 82.6，全球第一（Extended Thinking） |
| τ-Voice（agent任務完成率） | 68.6%（Extended Thinking） |
| τ-Voice-banking（Sierra） | 35.1%（Extended Thinking） |
| Big Bench Audio（音訊推理） | 97.7%（Extended Thinking） |
| Speech Agent Arena（人類偏好評測） | 第二名（Gemini 3.8 Live） |

在ServiceNow的EVA-Bench上，Google表示這兩款模型把複雜工作流的Pareto Frontier往前推進，在Gemini Enterprise Agent Platform的Live API上同時兼顧任務準確度與對話品質。

💡 定價與生態系整合

音訊輸入定價為每分鐘0.005美元，音訊輸出為每分鐘0.018美元，Google表示此估算基於每百萬輸入token 3美元、每百萬輸出token 12美元計算。開發者也可透過Agora、Fishjam、LangChain、LiveKit、Pipecat、Vercel、Vision Agents等Live API整合夥伴處理即時媒體串流基礎設施。Google並提到Salesforce、Genspark、Lumeris等合作方肯定了模型的低延遲、流暢度與工具呼叫能力，GitHub上也提供了範例應用程式。

🎯 實務啟示

對正在建置語音agent的工程團隊來說，Gemini 3.8 Live系列最大的意義在於把「推理」與「說話」整合進單一原生模型，省去串接ASR、LLM、TTS三個獨立元件的延遲與工程複雜度。若任務涉及多步驟工具呼叫或需要即時敘述進度（例如訂位、查詢、客服流程），Extended Thinking版本的τ-Voice與Big Bench Audio成績值得作為選型參考；但由於僅提供API託管服務、不開放權重，需要自行部署或資料不出境的場景仍需評估替代方案。

🔗 來源
- 標題：Google Releases Gemini 3.8 Live and 3.8 Live Extended Thinking for Production Grade Voice Agents
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/09/15/google-releases-gemini-3-8-live-and-3-8-live-extended-thinking-for-production-grade-voice-agents/

#GeminiLive #VoiceAI #SpeechToSpeech #ConversationalAI #GoogleAI #VoiceAgents #LLM #RealTimeAI #ExtendedThinking #AIProductRelease
