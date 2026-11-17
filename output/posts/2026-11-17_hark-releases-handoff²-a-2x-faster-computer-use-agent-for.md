---
title: Hark Releases Handoff², a 2x Faster Computer-Use Agent for Hark Pro
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/16/hark-handoff-2-computer-use-agent-2x-faster/
model: claude-code/sonnet
generated_at: '2026-11-17T01:10:00.487534'
score: 79
---

📌 Hark 電腦操作 Agent 升級，靠懲罰等待時間換來 2 倍速度

TL;DR：Hark Handoff² 用 RL 懲罰多餘回合與延遲，讓網頁任務平均比前一版快一倍。

多數 agent 訓練比的是準確率誰更高，Hark 這次反過來，把「慢」本身當成要被懲罰的對象。

🤔 **一個已經處理超過 2000 萬美元訂單的網頁操作 agent**

Handoff 是 Hark Pro 裡的電腦操作 agent，會像人一樣在真實網頁上點擊、輸入、滾動，而不是呼叫 API。Hark 在 8 月先行預覽，10 月正式上線，根據 Hark 的說法，至今已記錄超過 560 萬次瀏覽工作，處理超過 2000 萬美元的購買，使用者請它買生活雜貨、訂機票、約牙醫、辦退款、填保固表單、送出求職申請。Handoff² 是這個 agent 的第二版。

🧩 **把 agent harness 和 RL 訓練配方一起演進**

Hark 表示 Handoff² 同時改動了兩件事：新的 harness 讓模型每一回合可以吐出更多動作；訓練階段則明確懲罰多餘的回合、不必要的思考 token，以及端到端延遲。每個請求都跑在一臺專屬的虛擬電腦上，有自己的瀏覽器、檔案系統與終端機，模型輸出對準螢幕座標的遊標與鍵盤動作。因為節省的時間是逐回合累積的，Hark 的說法是任務越長、越仰賴瀏覽操作，加速效果就越明顯。

📊 **內部比較：和 Claude Opus 5.5 跑在同一套 harness 上**

Hark 公布了相對於 v1 的速度提升，以及兩個內部 benchmark 的結果，但要注意 v1 的數字是在舊版 harness 下量測的，不是在 Handoff² 使用的新 harness 下測的，兩者並非完全同條件比較。Hark 也讓 Claude Opus 5.5（max）跑在與 Handoff² 相同的 harness 上做對照，結果 Handoff² 的表現落在 Opus 5.5 的 5 分之內。在公開的 Online-Mind2Web 人工評測排行榜上，原始版 Handoff 拿到 97.67% 的分數，Yutori 的 Navigator n1.5 則是 97.3%；Hark 目前尚未公布 Handoff² 在這個排行榜上的成績。

⚠️ **目前只能透過 App 使用，細節也有限**

Handoff² 只內建在 Hark Pro 的 web、iOS 和 Android 版本裡，Hark 並未公開 API 或模型權重，外界無法獨立驗證或複現其訓練細節。定價上，Hark Pro 本身免費，Pro² 每月 20 美元可獲得 2 倍用量，Pro³ 每月 100 美元可獲得 10 倍用量，所有方案的功能本身是一致的。

💡 **對做 browser agent 的團隊，這是一個訓練思路的參考**

這起案例值得注意的地方，不在於具體效能數字本身（畢竟缺乏第三方可驗證的公開 benchmark 與論文），而在於訓練目標的設計方式：把多餘回合、冗餘思考 token、端到端延遲明確寫進 RL 的懲罰項，而不是只優化任務成功率。對正在設計 agent harness 與 reward 的團隊來說，這是一個值得參考但仍需自行驗證的方向。

🎯 **實務啟示**

如果你的 agent 也面臨「準確但慢」的問題，可以參考 Hark 的做法：先讓 harness 支援一回合內輸出更多動作，再把延遲和多餘回合直接納入 reward 設計，而不是事後才做效能優化。但由於目前沒有公開論文、權重或可複現的 benchmark，這更適合當作業界訊號，而非可直接照搬的技術方案。

🔗 **來源**
- 標題：Hark Releases Handoff², a 2x Faster Computer-Use Agent for Hark Pro
- 作者／機構：Michal Sutter @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/16/hark-handoff-2-computer-use-agent-2x-faster/

#ComputerUseAgent #ReinforcementLearning #AIAgents #BrowserAutomation #Hark #LLM #AgentHarness #Latency #AIProductivity #AutonomousAgents
