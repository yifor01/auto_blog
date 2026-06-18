---
title: 'Jun 18, 2026Frontier Red TeamProject Fetch: Phase two'
source: Anthropic Research
url: https://www.anthropic.com/research/project-fetch-phase-two
score: 98
model: google/gemma-4-31b-it:free
generated_at: '2026-06-18T20:49:52.078641'
---

📌 【Anthropic 最新研究】從「輔助人類」到「獨立操作」：Claude 遠端控制機器狗的進化

當我們談論 LLM 進入實體世界時，通常是在討論端到端的控制策略（Control Policy）。但 Anthropic 最近分享的 Project Fetch 實驗揭示了另一個有趣的路徑：當模型強大到能獨立處理複雜的指令與工具調用時，它能直接接管現成的機器人操作。

🤔 **AI 讓工作變快，但能獨立完成任務嗎？**

在 2025 年 8 月的第一階段實驗中，Anthropic 測試了 Claude Opus 4.1 如何協助非機器人專家的員工操作一台市售四足機器狗（Robodog）。結果很明確：有 AI 輔助的團隊效率遠高於僅依賴網路搜尋的團隊。

然而，當時的 AI 並非「主導者」。如果讓 Opus 4.1 獨立操作，它甚至連最基礎的「如何連接到機器人」這個步驟都會卡住，完全無法獨立完成任務。

🧪 **從 2025 到 2026：一次跨年度的能力對比**

一年後，Anthropic 啟動了 Project Fetch Phase Two。研究團隊將最新的 Claude Opus 4.7 放入同樣的場景中，這次不再是「輔助人類」，而是讓模型在「完全沒有人類協助」的情況下獨立操作。

這次的對比對象是去年表現最優秀的人類團隊，結果令人驚訝。

🚀 **獨立操作的 Opus 4.7，速度快過人類 20 倍**

在所有去年參與者完成的任務中，完全獨立運作的 Claude Opus 4.7 完成速度約為當時最快人類團隊的 20 倍。這顯示模型在處理高階指令、邏輯規劃以及與硬體介面互動的能力上，在短短一年內有了質的飛躍。

💡 **能力演進的三個階段：從助手到主導者**

Anthropic 在這次研究中觀察到一個重複出現的模式，這不僅發生在機器人領域，在網路安全（Cybersecurity）等領域也同樣適用：

1. **模型輔助人類**：AI 提供建議，人類執行操作（AI $\rightarrow$ Human）。
2. **人類輔助模型**：模型主導流程，人類在關鍵時刻修正（Human $\rightarrow$ AI）。
3. **模型獨立完成**：模型能自行處理大部分任務（AI $\rightarrow$ Task）。

Project Fetch 的進化過程正精準地走過這三個階段，顯示 LLM 正在從「知識庫」轉變為「行動代理（Agent）」。

⚠️ **尚未解決低階控制，精準操作仍是難題**

儘管速度驚人，但這並不代表 LLM 已經解決了機器人學的所有問題。研究團隊坦言：
- **精準度不足**：模型在嘗試精準移動沙灘球（即 Project Fetch 的核心「撿回」動作）時依然感到吃力。
- **缺乏底層控制**：實驗僅涉及高階指令調用，並未涉及最困難的低階控制（Low-level control），例如開發特定的驅動策略（Actuation policy）。

🎯 **LLM 與機器人結合的新方向：高階規劃與低階控制的分離**

這項實驗給我們的啟示是：我們或許不需要讓 LLM 學習如何控制每一個馬達的電流，而應該讓 LLM 扮演「大腦」負責高階邏輯規劃，而將低階控制交給專門的控制策略。當 LLM 的推理能力達到一定強度，它能極速地調用現有工具來達成目標，這將大幅縮短機器人部署的開發週期。

🔗 **研究連結**
📝 Project Fetch: Phase two
👤 Michael Ilie, C. Daniel Freeman, and Kevin K. Troy @ Anthropic
🔗 連結：https://www.anthropic.com/research/project-fetch-phase-two

你認為 LLM 最終會成為所有機器人的通用大腦，還是僅僅是個強大的指令翻譯機？歡迎在下方討論 👇

#AI #Robotics #Anthropic #Claude #LLM #Agent #機器人 #人工智慧
