---
title: OpenAI Ships GPT-Live-1.1 for Voice Agents, Cuts Idle Cost to $0.02/Min
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/21/openai-gpt-live-1-1-api-standby-mode/
model: claude-code/sonnet
generated_at: '2026-11-21T22:24:07.156076'
score: 86
---

📌 【OpenAI 新品】GPT-Live-1.1 上線：全雙工語音模型加入待機省錢模式

TL;DR：GPT-Live-1.1 開放 API，用 standby 待機計費降低語音 agent 的靜音時段成本。

語音 agent 最尷尬的成本陷阱，往往不是對話本身，而是通話中雙方都沒說話的那幾十秒——過去這段時間照樣全額計費。OpenAI 這次用一個新的計費狀態，直接把這個痛點處理掉。

🤔 **從級聯架構到單一模型**

傳統語音助理多半是 STT（語音轉文字）+ LLM + TTS（文字轉語音）三段式級聯，每一段都有延遲與銜接誤差。OpenAI 表示 GPT-Live 系列是全雙工（full-duplex）模型，在單一模型裡同時推理輸入與輸出音訊，能「邊聽邊說」，並原生處理 turn detection（判斷誰該發言）與回傳 ASR 轉錄文字，不需要額外拼接模組。GPT-Live-1.1 是 GPT-Live-1 的後續版本，官方表示其口音在多語言情境下更自然一致，任務完成也更可靠。GPT-Live-1 於 2026 年 9 月 10 日上線 API，根據 OpenAI 論壇公告，自 10 月 15 日起已用於 ChatGPT Plus 與 Pro 的語音功能。

🧩 **語音模型只負責對話，深度推理外包**

GPT-Live-1.1 的輸入輸出僅限音訊與文字，不支援圖片與影片；串流（streaming）與 function calling 可用，但 structured outputs、fine-tuning、predicted outputs 目前都不支援。較複雜的推理與工具呼叫會委派給後端文字模型，OpenAI 點名 GPT-6 Astra 處理複雜問題、Luna 處理高流量任務，第三方後端也可接入。官方的 Live conversations 指南把這個委派機制稱為 delegation，可設定 type 為 client（接自己的後端）或 responses（使用 OpenAI 模型）。系統指令（instructions）最長可到 16,384 tokens。

📊 **Standby：靜音時連線不斷，但不跑推理**

這次最具體的更新是 standby 待機模式：使用者沉默時，伺服器暫停推理，但 WebRTC 連線維持不中斷。逾時後伺服器會送出 session.paused 事件；使用者一開口，session.resumed 隨即觸發，session ID 與對話歷史都會被保留。官方也提醒，靜音後的第一句回覆可能稍慢，且整個待機期間麥克風音軌要保持啟用。這個機制同時適用於 GPT-Live-1 與 GPT-Live-1.1。

💡 **計費模式分層，待機不等於免費**

語音通話本身按時長計費（GPT-Live-1 的模型頁面說明是按秒計費），後端模型與工具呼叫則另外計費——這意味著即使語音層的待機費率壓低，若後端模型處理頻繁，整體成本仍可能被後端吃掉。原文標題直接點出待機費率已降到每分鐘 0.02 美元，但文章正文並未逐項拆解費率明細，實際金額仍建議以官方計費頁為準。

⚠️ **目前的限制**

GPT-Live-1.1 是純 API 功能，沒有獨立介面；要切換現有通話使用 1.1 版，需把 model 設為 gpt-live-1.1，但更換模型必須開新的 session。GPT-Live-1 與 GPT-Live-1.1 的並行 session 上限是分開計算、且各自依推理區域（inference region）設限，1.1 的分級數字官方頁面目前未公開。

🎯 **對語音 agent 開發者的實務意義**

11 月 2 日起 outbound SIP 通話已開放給所有組織，電話客服類應用可以直接整合。若你正在建置語音 agent，standby 機制代表「長時間保持通話但多數時間靜音」的場景（如客服等待、會議旁聽）成本結構會改善，但真正要省錢，還是要盤點後端模型與工具呼叫的用量，而不只看語音層的待機費率。

🔗 **來源**
- 標題：OpenAI Ships GPT-Live-1.1 for Voice Agents, Cuts Idle Cost to $0.02/Min
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/21/openai-gpt-live-1-1-api-standby-mode/

#OpenAI #VoiceAI #GPTLive #ConversationalAI #VoiceAgents #AIAPI #SpeechAI #RealtimeAI #LLM #AIInfrastructure
