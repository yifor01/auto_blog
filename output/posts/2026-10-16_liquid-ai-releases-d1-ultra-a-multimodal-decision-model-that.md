---
title: 'Liquid AI Releases d1-ultra: A Multimodal Decision Model That Scores 65 on
  the AA Decision Index'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/15/liquid-ai-d1-ultra-decision-model/
model: claude-code/sonnet
generated_at: '2026-10-16T20:09:57.606991'
score: 96
---

📌 Liquid AI d1-ultra:不輸出任何文字的決策模型,拿下 AA Decision Index 第一

TL;DR:d1-ultra 用單次前向傳播直接輸出答案機率、零輸出 token,專為路由、審核、分類場景設計,API 已開放試用。

如果你呼叫 LLM 只是要一個「是/否」或分類標籤,為什麼要付生成整句話的費用?Liquid AI 的答案是:把輸出壓縮成一組機率分布,連一個 token 都不用生成。

🤔 **決策模型:用機率取代自由文字**

Liquid AI 釋出了 d1-ultra,是其目前最強的決策模型。它讀取文字、影像或兩者,針對有範圍限制的問題,直接回傳每個可能答案的機率,僅需一次前向傳播,不產生任何輸出 token。Liquid 的決策模型文件描述了 3 種問題類型,並建議將決策模型用於路由、內容審核、守門機制、分流(triage)以及取代 LLM-as-judge 的場景;至於摘要、聊天與程式碼生成,文件仍建議使用一般語言模型。

🧩 **一次呼叫評估多個問題**

每個請求帶著一個 state(也就是上下文)、可選的影像,以及一個或多個「有型別」的問題,模型會在同一次呼叫中,針對同樣的輸入評估每一個問題。d1 的 API 參考文件顯示,回應中的 output_tokens 永遠為 0。

Liquid AI 團隊表示,d1-ultra 使用比 d1 更大的開源權重骨幹,並疊加了大量 Liquid 專屬的客製化,搭配 Liquid 的決策訓練 pipeline,在知識型任務上的提升最為明顯。團隊舉的應用例子包括:對照規格檢查電路板是否有瑕疵,或是比對客戶照片來核實理賠申請,這類「雜亂」的實務場景正是 d1-ultra 的設計目標。

📊 **在 Artificial Analysis Decision Index 排名第一**

Liquid AI 將 d1-ultra 與前代 d1,以及 TypeSafe 的 Jev 1.14 在 112 項評測上做比較,根據官方公告,d1-ultra 在相同價格下於所有任務上都勝過 Jev 1.14。在獨立的 Artificial Analysis Decision Index 上,Liquid 回報 d1-ultra 以 65 分排名第一,該指數由 4 項評測各佔 25% 權重平均而成。作為對照,Artificial Analysis 在 10 月 13 日的發布文章中,Jev 1.13 以 58 分排名首位,GLiDE 與 Microsoft-Decision-1 則並列 54 分。

💡 **計費只算輸入 token,但影像會被重複計費**

d1-ultra 透過 Liquid API 的 /decisions/v1/systemone 端點提供服務,model 參數設為 "d1-ultra",目前已可在 Liquid API 上使用,定價為每百萬輸入 token 0.042 美元;Liquid 表示 Vercel AI Gateway 與 OpenRouter 的支援即將推出,也可以先在 d1 Playground 試用。

計費只計算輸入 token。根據 Liquid 的定價說明,影像以每個 32×32 像素 patch 計 1.5 個 token,一張 1024×1024 的影像因此要價 1,536 個 token。需要注意的是,每個問題都會被當作獨立的 prompt 計費,包含其文字與所有附帶影像,所以如果對同一張影像提出 3 個問題,這張影像會被計費 3 次。端點文件也設定上限:單次請求最多 8 張影像、10,000 個影像 patch,完整 JSON body 需低於 4.5MB。

🎯 **實務啟示**

對於分類、路由、內容審核、分流這類「只要一個答案機率、不需要生成文字」的場景,d1-ultra 提供了比一般 LLM 呼叫更直接的成本結構。但在設計請求時要留意:把多個問題疊加在同一張影像上,會讓該影像的 token 成本隨問題數線性增加,批次設計時值得先估算好影像與問題的組合方式,避免費用超出預期。

🔗 **來源**
- 標題:Liquid AI Releases d1-ultra: A Multimodal Decision Model That Scores 65 on the AA Decision Index
- 作者／機構:Asif Razzaq,MarkTechPost
- 連結:https://www.marktechpost.com/2026/10/15/liquid-ai-d1-ultra-decision-model/

#LiquidAI #DecisionModel #MultimodalAI #LLMAlternative #AIRouting #ContentModeration #MachineLearning #ArtificialAnalysis #AIInference #ModelPricing
