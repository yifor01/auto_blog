---
title: Intelligent transcription with Gemini 3.5 Transcribe
source: Google DeepMind
url: https://deepmind.google/blog/intelligent-transcription-with-gemini-3-5-transcribe/
model: claude-code/sonnet
generated_at: '2026-08-27T17:15:56.801480'
score: 119
---

📌 【Google DeepMind】Gemini 3.5 Transcribe:讓語音轉文字更懂你的意圖

TL;DR：Google DeepMind 推出新一代語音轉文字模型 Gemini 3.5 Transcribe,主打即時串流低延遲與智慧語意清理,已開放 API 給開發者使用。

「等一下,我是說星期三,不是星期二」——這種日常對話裡的自我修正,對多數語音辨識系統來說仍是雜訊。Gemini 3.5 Transcribe 想做的,正是把這種「人話」直接轉成乾淨、可用的文字。

🤔 **傳統語音辨識卡在哪裡**

Google DeepMind 指出,傳統語音辨識模型在背景噪音、專業術語與語句不流暢（disfluency）的清理上表現不佳。Gemini 3.5 Transcribe 的設計目標,就是把原始音訊直接轉換為精準、經過潤飾且格式化的文字,而不只是逐字轉寫。

🧩 **兩套 API,對應即時與離線兩種場景**

Gemini 3.5 Transcribe 透過兩個獨立 API 提供服務：
- 即時串流：透過 Live API 的 `gemini-3.5-transcribe-live`,提供雙向連續串流,延遲低於一秒,適合互動式語音應用。
- 預錄音訊處理：透過 Interactions API 的 `gemini-3.5-transcribe`,可處理錄音、會議與通話紀錄,並支援語者辨識（speaker attribution）與詞級時間戳記。

模型能力上,官方列出幾項重點：自動處理自我修正、去除「嗯」「啊」等贅字並自動格式化文字；支援 function calling,能將圖片生成、檔案分析等任務委派給其他 Gemini 模型；可辨識自訂詞彙表中的專有名詞與特殊拼法；自動偵測並轉錄超過 85 種語言,涵蓋不同口音與方言；預錄音訊最多可準確歸屬三位語者的發言（三位以上仍屬實驗性功能）。

📊 **實測數據：延遲與錯誤率雙雙下降**

根據 Artificial Analysis 的測試,Gemini 3.5 Transcribe 的平均詞錯誤率（WER）在串流情境下為 4.0%,非串流情境下為 2.6%,在嘈雜的真實環境中仍能準確辨識郵遞區號、訂單編號等英數字組合。相較前代模型 Chirp 3,最終轉錄完成時間縮短了 70%。在 FLEURS 基準測試的多語言評測中,串流模式 WER 為 5.50%,非串流模式為 5.04%,同樣優於 Chirp 3。

💡 **重點不在模型本身,而在「無處不在」的整合**

比起單一的辨識精度數字,這次更新的重心其實是把語音理解嵌入到日常使用場景中：Android 上的 Gboard 透過新功能 Rambler,能把口述內容轉成格式整齊的文字,並支援語音修改、修正錯字與調整寫作風格；Google Antigravity 會在使用者授權下結合螢幕內容與對話紀錄,提升檔名、agent 思考過程與文件內容的轉錄準確度；Google AI Studio 的 Build 模式可用語音直接「vibe coding」；macOS 版 Gemini App 除了轉錄,還能呼叫其他 Gemini 模型完成摘要檔案、跨應用改寫文字、在遊標處生成圖片等操作；Chrome 也將支援在任何網頁欄位以語音輸入。生態系方面,Agora、Fishjam、LangChain、LiveKit、Pipecat、Vercel、Vision Agents 等開發平臺已透過 Live API 打造語音互動應用,vivo、Intellitek Health、Lingopal 等公司也對其延遲、準確度與多語言支援給予正面回饋。

🎯 **實務啟示**

對開發者而言,值得關注的是它把「轉錄」與「後續動作」串在一起：透過 function calling,語音輸入不只是文字輸出,還能直接觸發下游任務。若你正在打造語音代理、即時字幕或通話後分析管線,這種即開即用的雙 API 架構（串流 + 預錄）加上自訂詞彙表支援,能省下不少客製化語音清理的工程量。

🔗 **來源**
- 標題：Intelligent transcription with Gemini 3.5 Transcribe
- 作者／機構：Google DeepMind（Diego Melendo Casado、Luke Leonhard,代表 Gemini Audio 團隊）
- 連結：https://deepmind.google/blog/intelligent-transcription-with-gemini-3-5-transcribe/

#Gemini #SpeechToText #GoogleDeepMind #VoiceAI #ASR #LiveAPI #AgenticAI #DeveloperTools #MultilingualNLP #RealTimeTranscription
