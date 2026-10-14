---
title: How Third Moment Research runs 10,000 agents for 36+ hours
source: OpenAI Blog
url: https://openai.com/index/third-moment-research
model: claude-code/sonnet
generated_at: '2026-10-14T20:47:48.004484'
pinned: true
---

📌 【OpenAI 官方案例】一個 AI 實驗室如何同時跑 10,000 個 Agent，連續運作超過 36 小時？

TL;DR：Third Moment Research 用 GPT-6 Astra、GPT-6.1 Sol、Codex 與 Daybreak，打造能連續專注數天、且越用越強的 agent。

多數人操作 agent 的經驗,是跑個幾分鐘到幾小時就得人工介入收尾。但這篇案例描述的場景完全不同：一萬個 agent 同時運行，而且持續專注超過 36 小時不中斷。這個規模本身就值得工程師停下來想一想，背後需要什麼樣的系統設計。

🤔 **規模與持續性是兩個不同的難題**

標題點出的兩個關鍵數字，「10,000 個 agent」與「36 小時以上」，分別對應著 agent 系統的兩種挑戰：橫向的規模擴展（同時管理大量 agent 實例），以及縱向的持續性（讓單一 agent 長時間維持任務焦點而不漂移或失效）。素材將這間機構定位為「AI lab」,但沒有進一步說明其具體研究領域或這一萬個 agent 執行的任務內容。

🧩 **模型組合：GPT-6 Astra、GPT-6.1 Sol、Codex、Daybreak**

這個案例動用的模型陣容頗為完整：GPT-6 Astra 與 GPT-6.1 Sol 作為核心推理模型，Codex 處理程式碼相關任務，Daybreak 則專門支援網路安全場景（與素材 2 中 SentinelOne 使用的是同一工具）。摘要特別提到這些 agent「隨著使用而進步」，暗示系統具備某種持續學習或經驗累積的機制,但具體是透過 fine-tuning、記憶體機制還是其他方式達成，摘要並未說明。

💡 **「越用越強」背後的含義**

如果 agent 真的能在長時間運行中「improve with use」，這意味著系統設計不只是單次任務執行，而是具備某種跨任務、跨時間的學習迴圈。這對正在設計長時效 agent 系統的工程師來說是一個值得關注的方向,但目前素材尚未揭露實作細節。

🎯 **實務啟示**

如果你的 agent 應用正卡在「跑幾小時就需要人工重啟」或「規模一大就難以管理」，這則案例至少證明了同時兼顧大規模並行與長時間持續運作是可行的,後續可以留意 GPT-6.1 Sol 與 Daybreak 釋出的技術文件,了解實現這種持續性的具體機制。

🔗 **來源**
- 標題：How Third Moment Research runs 10,000 agents for 36+ hours
- 作者／機構：OpenAI
- 連結：https://openai.com/index/third-moment-research

#OpenAI #AIAgents #GPT6 #Codex #Daybreak #AgenticAI #AIResearch #LLM #Cybersecurity #ScalableAI
