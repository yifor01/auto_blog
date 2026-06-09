---
title: shareAI-lab/learn-claude-code
source: GitHub Trending
url: https://github.com/shareAI-lab/learn-claude-code
score: 103
model: google/gemma-4-31b-it:free
generated_at: '2026-06-09T20:29:27.258540'
---

📌 **【GitHub 熱門】想打造 AI Agent？先搞懂「模型」與「外殼」的本質區別**

很多人在開發 AI Agent 時，習慣花大量時間撰寫複雜的外部編排邏輯（Orchestration），試圖用程式碼「定義」AI 該如何行動。但事實上，真正的「代理能力」（Agency）並非來自於你的程式碼，而是來自於模型本身的訓練。

🤔 **Agency 是訓練出來的，而不是寫出來的**

shareAI-lab 在其最新的開源專案 `learn-claude-code` 中提出了一個核心觀點：感知、推理與行動的能力（Agency），是由模型在數十億次的梯度更新中學習而來的，而非由外部的程式碼框架所賦予。

簡單來說，如果你試圖用複雜的 `if-else` 或硬編碼的流程來強行定義 Agent 的行為，你其實是在限制模型，而非賦予它能力。

🧪 **Agent 產品的公式：Model + Harness**

為了讓讀者快速進入狀況，該專案將 Agent 產品簡化為一個清晰的公式：
**Agent 產品 = 模型 (Model) + 外殼 (Harness)**

- **模型 (Model) 是「駕駛員」**：負責決策、推理與下指令。
- **外殼 (Harness) 是「車輛」**：提供模型與環境互動的基礎設施（如 API 接口、執行環境、工具集）。

這意味著，開發者的核心任務不應該是教 AI「如何思考」，而是為它打造一台性能強大且穩定的「車輛」，讓模型能將其內在的 Agency 充分發揮在特定環境中。

💡 **從 DeepMind DQN 看 Agent 的演進脈絡**

專案中回溯了 AI Agent 的發展史以證明此論點。早在 2013 年，DeepMind 的 DQN 就能在僅接收原始像素和分數的情況下，學習並精通 7 款 Atari 遊戲，甚至在其中 3 款中擊敗人類專家。

這證明了只要模型經過正確的訓練（學習感知 $\rightarrow$ 推理 $\rightarrow$ 行動），它就能在沒有外部複雜指令的情況下，自發性地產生解決問題的代理能力。到 2015 年，這種能力已擴展到 49 款遊戲並達到專業測試員水準。

⚠️ **實作導向，但需配合強大模型**

由於 Agency 依賴於模型訓練，這意味著如果你使用的基礎模型（Base Model）推理能力不足，無論你的 Harness（外殼）設計得再精巧，最終產出的 Agent 依然會缺乏靈魂。這也是為什麼該專案選擇以 Claude 等高性能模型作為教學基礎的原因。

🎯 **給 AI 工程師的實務啟示：專注於構建「執行環境」**

如果你正準備構建自己的 AI Agent，建議將開發重心從「定義行為流程」轉移到「優化執行環境」：
1. **強化工具集 (Tooling)**：提供更精準、更可靠的 API 讓模型調用。
2. **優化感知輸入**：確保模型能接收到高品質、低雜訊的環境資訊。
3. **簡化編排邏輯**：給予模型更多自主推理的空間，而非用過多的硬性限制鎖死其行為。

🔗 **專案連結**
📝 learn-claude-code
👤 shareAI-lab
🔗 GitHub：https://github.com/shareAI-lab/learn-claude-code

你認為 AI Agent 的成功關鍵在於「更強的模型」還是「更精巧的框架」？歡迎在下方討論 👇

#AI #AIAgents #Claude #GitHubTrending #LLM #軟體工程 #DeepMind #MachineLearning
