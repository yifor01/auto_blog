---
title: Moonshot AI Launches Kimi Work, a Local Desktop Agent Reportedly Running on
  Kimi K2.6 With a 300-Sub-Agent Agent Swarm
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/12/moonshot-ai-launches-kimi-work-a-local-desktop-agent-reportedly-running-on-kimi-k2-6-with-a-300-sub-agent-agent-swarm/
score: 103
model: google/gemma-4-31b-it:free
generated_at: '2026-06-12T20:34:07.684533'
---

📌 【Moonshot AI 最新發表】Kimi Work：將 AI Agent 從雲端搬到桌面，實現本地化自動化工作流

過去兩年的 AI Agent 大多運行在雲端沙盒（Sandbox）中，你輸入目標，遠端伺服器啟動瀏覽器幫你操作。但這種模式有一個致命傷：它無法直接觸及你電腦裡的本地文件，也無法操作你正在使用的真實瀏覽器會話。

Moonshot AI 最近推出的 Kimi Work 試圖打破這個限制，將 Agent 的執行環境直接搬到使用者的 macOS 與 Windows 桌面。

🤔 **從「雲端沙盒」轉向「本地執行」的權衡**

傳統雲端 Agent 的邏輯是「隔離與便利」，雖然設定簡單且安全，但與本地數據之間隔了一道牆。Kimi Work 的核心差異在於它是一個可下載的應用程式，而非網頁對話框。

這意味著 Kimi Work 能直接讀取本地文件、驅動你的真實瀏覽器，並在你的機器上執行任務。這對那些瓶頸在於「文件存取」與「即時會話管理」的知識工作者來說，是更實用的解決方案。

🧪 **基於 Kimi K2.6 MoE 模型與 300 子代理人協作**

根據社群報告，Kimi Work 的底層由 Moonshot 的旗艦模型 Kimi K2.6 驅動。這是一個具有以下技術特性的模型：
- **架構**：採用 Mixture-of-Experts (MoE) 開放權重模型。
- **運算效率**：每個 token 約激活 32B 參數。
- **長文本能力**：具備 256K-token 的上下文窗口，足以處理複雜的多步驟工作流。
- **協作模式**：據報導採用了包含 300 個子代理人 (Sub-Agent) 的 Agent Swarm 架構，用以分工處理複雜任務。

💡 **將自然語言轉化為本地執行指令**

Kimi Work 的實作邏輯將自然語言與系統級工具結合，提供三個關鍵功能：
1. **金融數據預整合**：內建 A 股、港股與美股的市場數據，使用者無需自行設定複雜的 API 即可獲取即時資訊。
2. **端到端產出**：研究完成後，可直接將結果轉換為 PowerPoint 簡報或 Excel 表格。
3. **Cron 引擎排程**：其排程器採用標準的 cron 格式（分、時、日、月、週），讓使用者可以用自然語言定義任務，並由 cron 引擎精確執行（例如：每天早晨自動生成簡報）。

⚠️ **本地執行雖增加控制權，但失去雲端管理便利**

本地化執行是一把雙面刃。雖然數據留在設備上更私密，且能觸及真實文件，但相對地，使用者需要承擔本地運行的資源消耗，且失去了雲端管理所提供的「零設定便利性」與集中式安全管理。

🎯 **對工程師與 PM 的實務啟示：重新思考數據流向**

對於注重數據隱私或需要處理大量本地文件的團隊，Kimi Work 提供了一種新路徑：
- **數據私密性**：不再需要將所有私密文件上傳至雲端才能讓 AI 處理。
- **真實環境操作**：能直接操作真實瀏覽器會話，而非在受限的沙盒中運行。
- **自動化整合**：結合 cron 排程與自然語言，可將重複性的本地研究工作流自動化。

🔗 **詳細資訊**
📝 Moonshot AI Launches Kimi Work, a Local Desktop Agent
👤 Asif Razzaq @ MarkTechPost
🔗 來源：https://www.marktechpost.com/2026/06/12/moonshot-ai-launches-kimi-work-a-local-desktop-agent-reportedly-running-on-kimi-k2-6-with-a-300-sub-agent-agent-swarm/

你傾向於使用便利的雲端 Agent，還是更看重能操作本地文件的桌面 Agent？歡迎在下方分享你的看法 👇

#AI #Agent #MoonshotAI #KimiWork #MoE #LocalAI #自動化 #生產力工具
