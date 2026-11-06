---
title: 'Google Releases Gemini Omni 1.2 Flash: 15-Second AI Video at $0.07 per Second'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/05/google-gemini-omni-1-2-flash-15-second-video/
model: claude-code/sonnet
generated_at: '2026-11-06T22:29:18.876684'
score: 78
---

📌 【Google DeepMind】Gemini Omni 1.2 Flash：15 秒影片、每秒降價 3 成

TL;DR：Gemini Omni 1.2 Flash 開放 15 秒影片生成，720p 降價約 3 成。

當同業還在比誰的影片生成模型解析度更高，Google 這次主打的卻是「少重新生成幾次」——用對話式多輪編輯，把成本真正壓下來。

🤔 這次更新了什麼

Gemini Omni 1.2 Flash 是 Google DeepMind 的多模態影片生成與編輯模型，原生支援長達 15 秒的影片片段，目前已在 Google Cloud 與 Gemini API 上正式開放（generally available）。輸入可以是文字、圖片、短影片片段與音訊，輸出則是「帶音訊的影片」。Google 開發者文件把 Omni 系列定義為原生多模態，編輯功能透過 Interactions API 處理。

💡 把「降成本」包裝成工作流程，不只是降價

官方建議的流程是：先用 360p 或 720p 草稿，用後續編輯指令修正細節（而不是整段重新生成），最後再把滿意的結果升頻到 1080p 或 4K。多輪對話式編輯現在可以套用在完整的 15 秒片段上，實務上可以逐輪替換產品、背景、光線或長寬比。開發文件顯示這是透過 `previous_interaction_id` 實現，所以不需要重新上傳前一段影片。

📊 價格：720p 每秒 0.07 美元

Omni 1.2 Flash 的定價是每秒 720p 影片 0.07 美元，其他解析度也有類似幅度的降價。作為對比，Omni 1.1 Flash 的定價頁面顯示 720p 大約每秒 0.10 美元，換算下來一段完整的 15 秒 720p 影片，1.2 版大約要價 1.05 美元。Google Vids 使用者可以免費生成 15 秒片段；另外提供 Provisioned Throughput 選項，所有輸出都會帶有 SynthID 水印。

⚠️ 沒有公開的 1.2 版 benchmark 分數

Google 目前沒有公布 1.2 版的 benchmark 成績，相關說法以跟 1.1 版的並排示範為主。DeepMind 的模型頁面針對 Omni Flash 系列公布了人工評分結果，其中包含 1,003 筆 MovieGenBench prompt 的測試，但這些資料屬於系列整體背景，並非針對 1.2 版。今年 6 月，較早期的 Omni Flash 版本曾在 Arena 的文字轉影片排行榜上取得第一名，但那個排名在 1.2 版發布之前，只能當作系列背景參考。早期合作夥伴的回饋偏正面但屬於自選樣本：根據 Google 的發布頁面，invideo 的工程副總表示模型會貼著 prompt 走，物理效果與聲音都很真實；QuickFrame AI 則表示 15 秒、1080p 的輸出讓他們能一次生成就做出完整的 CTV 廣告。

🎯 實務啟示

對有影片生成需求的工程團隊來說，重點不是單次生成品質，而是「草稿 → 編輯 → 升頻」這套可控制成本的流程設計；善用 `previous_interaction_id` 做多輪編輯，可以明顯減少整段重新生成的花費。由於官方尚未公布 1.2 版的 benchmark，評估時仍需用自己的場景實測，不能只看合作夥伴的自選回饋或系列整體排名。

🔗 來源
- 標題：Google Releases Gemini Omni 1.2 Flash: 15-Second AI Video at $0.07 per Second
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/05/google-gemini-omni-1-2-flash-15-second-video/

#Gemini #GoogleDeepMind #VideoGeneration #GenerativeAI #MultimodalAI #GeminiAPI #GoogleCloud #AIVideo #TextToVideo #SynthID
