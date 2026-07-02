---
title: NousResearch/hermes-agent
source: GitHub Trending
url: https://github.com/NousResearch/hermes-agent
score: 95
model: google/gemma-4-31b-it:free
generated_at: '2026-07-02T19:50:37.578384'
---

📌 【NousResearch】Hermes Agent：具備自我學習迴路、能自主建立技能的 AI Agent

TL;DR：一個支援跨平臺、可透過經驗自主建立與最佳化技能，且具備閉環學習能力的開源 AI Agent 框架。

大多數 AI Agent 的能力僅限於預設的 Tool Use，一旦對話結束，經驗便隨之消失。如果 Agent 能像人類一樣，在完成複雜任務後將經驗「沉澱」成技能，並在下次使用時自我最佳化，會發生什麼？

🧩 **核心設計：將經驗轉化為「自我進化」的學習迴路**

Hermes Agent 最關鍵的特點在於其內建的學習迴路（Learning Loop），讓 Agent 不再只是被動執行指令，而是能透過以下機制自我提升：

- **自主技能建立**：在處理完複雜任務後，能自動將經驗轉化為可重複使用的技能。
- **使用中持續最佳化**：技能並非固定不變，而是在實際使用過程中不斷自我改進。
- **記憶管理與回溯**：透過 FTS5 搜尋與 LLM 摘要機制實現跨對話的記憶回溯，並透過定期提醒（Nudges）來鞏固知識。
- **使用者建模**：利用 Honcho 辯證使用者建模（Dialectic User Modeling）來深化對使用者的理解。

🛠️ **高度靈活的部署與模型整合**

為了降低部署門檻並避免供應商鎖定，Hermes Agent 在基礎設施上採取了極高的靈活性：

- **模型解耦**：支援 Nous Portal、OpenRouter、OpenAI 以及自定義端點。使用者可透過 `hermes model` 指令快速切換模型，無需修改程式碼。
- **低成本執行**：可部署於 5 美元的 VPS、GPU 叢集或幾乎零成本的 serverless 基礎設施。
- **跨平臺互動**：透過單一閘道程式（Gateway Process），可同時在 Telegram、Discord、Slack、WhatsApp、Signal 與 CLI 上執行，且支援語音備忘錄轉錄與跨平臺對話連續性。

💻 **完整的 TUI 介面與自動化能力**

除了後端邏輯，Hermes Agent 提供了一個功能完整的終端使用者介面（TUI），包含：
- 多行編輯、斜線指令（slash-command）自動完成。
- 對話歷史管理、中斷與重新導向，以及工具輸出的串流顯示。

此外，它內建了 cron 排程器，允許使用者以自然語言設定自動化任務（如每日報告、每晚備份、每週審計），並將結果交付至指定的通訊平臺。

🎯 **實務啟示**

對於開發者而言，Hermes Agent 展現了從「靜態工具呼叫」轉向「動態技能演進」的可能性。其相容 agentskills.io 開放標準的設計，意味著未來 AI Agent 的能力可能不再依賴於單次 Prompt 工程，而是透過一套可遷移、可演進的技能集來實現。

🔗 **來源**
- 標題：NousResearch/hermes-agent
- 作者／機構：NousResearch
- 連結：https://github.com/NousResearch/hermes-agent

#AI #Agent #OpenSource #NousResearch #LLM #SelfImproving #AutonomousAgents #TUI #MachineLearning #AIInfrastructure
