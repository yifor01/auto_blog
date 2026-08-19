---
title: Frontier Model Cost and Open-Weights Popularity is Driving Demand for Model
  Routing
source: Latent Space
url: https://www.latent.space/p/glean-model-routing
model: claude-code/sonnet
generated_at: '2026-08-19T06:43:22.394042'
score: 76
---

📌 Stripe 70 億美元買下 OpenRouter，Glean 靠模型路由衝上 3 億美元 ARR

TL;DR：企業 AI 平臺 Glean 用「先省 token、再選模型」的路由架構，過去 15 個月 ARR 成長三倍。

Stripe 才剛以超過 70 億美元的價碼買下 OpenRouter，證明「該用哪個模型」已經是門好生意。同一股風潮也吹進了企業內部：Glean 共同創辦人暨執行長 Arvind Jain（前 Google Distinguished Engineer）告訴 Latent Space，他們常看到員工在 Glean 裡輸入兩個數字要模型幫忙相加或相乘，「他們大可以用計算機。」

🤔 背景：模型越來越貴，企業帳單先扛不住

Jain 描述了一個很直接的成本壓力：「像 Opus 或最新版的 GPT，這些最先進的模型，不只能力更強、能處理更複雜的任務，就算用同樣的 token 數計算，單價也更貴，有時候是舊模型的兩倍到四倍。加上使用者現在會拿它們跑更長的任務，換算下來，每個使用者的花費可能是去年的十倍、二十倍。」Glean 於去年 6 月完成 1.5 億美元 Series F 募資後估值達到 72 億美元，今年 ARR 達到 3 億美元，較 15 個月前成長三倍。

🧩 架構：Glean 提供三層模型選擇機制

Glean 讓員工可以自己明確指定要用哪個模型；管理員可以限制可用模型或設定用量上限；而多數客戶實際採用的是 Glean 的自動模式，由系統依任務動態挑選模型。Jain 表示，自動模式會被大量採用，主要原因就是成本：「大家會討論、會興奮於模型路由，多半是因為成本。」

Glean 共同創辦人暨工程負責人 Tony Gentilcore 近期提到，Glean「比 Claude Code 便宜 4 倍」，平均每個任務花費 0.45 美元，相對於 Claude Cowork 的 1.84 美元，並將這歸功於 Glean 自家的 harness 與路由能力。

Glean 架構裡還有一個叫 Waldo 的模型，Jain 形容它「架在大型語言模型之上」。Waldo 於今年 4 月推出，被定位為 Glean 的第一個 agentic search 模型：它負責決定如何拆解問題、該用哪些工具、下一步要讀什麼，以及什麼時候證據已經足夠，可以交給前沿模型（frontier model）給出高品質答案。換句話說，模型路由是在 Glean 已經備妥「原料」之後才發生的，Jain 說：「我們能在不燒掉 LLM token 的情況下，先把工作需要的原料組裝好。」這也代表一個推論：一個上下文抓得夠準的便宜模型，表現可能超過一個塞滿無關資料的前沿模型。

📊 開源模型的態度轉變：從「幾乎沒人用」到「企業策略的一部分」

Jain 證實企業對開源模型的興趣明顯上升，主因同樣是成本。「去年，開源 LLM 的使用量微乎其微，幾乎沒有人認真考慮它，」他說，部分原因是這些模型多半在美國以外開發，帶有某種「污名」。但情況在最近三個月出現轉變：「因為 AI 變得太貴，企業開始覺得維持現有的 AI 投資難以為繼。開源在完成任務的成本上便宜了一個數量級，這讓大家產生很大的興趣。今天我可以說，在大多數企業裡，開源模型都被視為 AI 策略的關鍵一環。」他也觀察到企業不再只依賴一兩家模型供應商：「沒有人再願意只依賴一兩家模型供應商，也沒有人認為自己能離得開開源。」

在 eval（模型評估）機制上，Glean 用「內部測試系統」把真實世界的工作負載依查詢類型拆分後，讓模型路由器選一條路徑，同時平行用其他模型（有的更便宜、有的更貴）跑同樣的任務，再用 AI 判官（AI-based judges）評估路由器的選擇有多準。Jain 說這個比對流程只針對「一小部分」真實流量執行，但以 Glean 的規模來說已經足夠持續訓練與改進路由系統。

💡 深入分析：Glean 的優勢來自「看得到企業怎麼用 AI」

Glean 客戶案例中，Zillow 有 7,000 名員工、80% 採用率；Booking.com 則是「第一個全公司採用的 AI 平臺」。Jain 認為，正是這種大規模的部署，讓 Glean 能觀察到員工實際在不同任務上會先選哪個模型、什麼時候不滿意會換到另一個模型，這個大規模的人類回饋迴圈，反過來持續改善路由系統本身。Glean 創立於 2019 年初，最早的定位是企業搜尋；即使到了 2023 年，公司重心仍主要放在企業搜尋上，如今在 2026 年，企業使用 AI 的範圍已經遠遠不只搜尋。

🎯 實務啟示

如果團隊正在幫企業內部工具做模型選型，Glean 的經驗提供一個值得參考的分工順序：先用便宜、快速的步驟把「回答這個問題需要的原料」準備好，再決定要不要動用前沿模型，而不是一開始就把整段上下文丟給最貴的模型；同時，路由決策本身也該被持續評估，用平行跑其他模型的方式驗證路由器的選擇是不是真的划算。

🔗 來源
- 標題：Frontier Model Cost and Open-Weights Popularity is Driving Demand for Model Routing
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/glean-model-routing

#ModelRouting #Glean #LLM #EnterpriseAI #OpenWeights #AICost #AgenticAI #LLMOps #AIInfrastructure #FrontierModels
