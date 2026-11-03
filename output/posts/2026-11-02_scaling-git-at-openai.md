---
title: Scaling Git at OpenAI
source: OpenAI Blog
url: https://openai.com/index/scaling-git-at-openai
model: claude-code/sonnet
generated_at: '2026-11-02T23:57:00.840139'
pinned: true
---

📌 OpenAI 自建 Pando，Git 基礎設施也要為 Codex 升級

TL;DR：OpenAI 打造 Git 相容後端 Pando，應對 Codex 帶來的開發規模。

當一個模型可以同時幫上千名工程師寫程式碼、開分支、送 PR，你手上那套用了二十年的 Git 基礎設施，還撐得住嗎？OpenAI 在官方部落格給出了自己的答案：自己重寫一套。

🤔 **Codex 讓「開發規模」變成一個新問題**

OpenAI 在部落格中指出，Codex 讓大規模的程式碼開發變得可能，而這種規模對既有的 Git 基礎設施提出了新的挑戰。換句話說，當程式碼變更的速度與數量不再只由人類工程師決定，底層版控系統也需要重新設計。

🧩 **Pando：一套 Git 相容的後端**

OpenAI 介紹了他們建構的 Pando，一套與 Git 相容（Git-compatible）的後端系統。「相容」這點很關鍵：工程師與工具鏈仍可以用熟悉的 Git 指令與工作流程互動，但底層的儲存與服務架構是針對 Codex 帶來的開發規模重新設計的。至於 Pando 具體在儲存結構、效能最佳化上做了哪些取捨，原文並未進一步展開細節。

💡 **為什麼這件事值得關注**

這釋出一個訊號：AI 輔助編程不只是改變「寫程式碼」這個環節，也在往上游推動整個開發基礎設施（版控、CI/CD、程式碼審查）必須重新思考規模問題。對於正在導入 AI coding agent 的團隊，Git 伺服器、權限模型、甚至分支策略，可能都需要提早評估是否能承受爆發性的變更量。

🎯 **實務啟示**

如果你的團隊已經讓 AI agent 大量參與程式碼產出，不妨檢視現有版控系統在高頻率、高併發變更下的瓶頸在哪裡，這可能是下一個被低估的基礎設施議題。

🔗 **來源**
- 標題：Scaling Git at OpenAI
- 作者／機構：OpenAI
- 連結：https://openai.com/index/scaling-git-at-openai

#OpenAI #Codex #Git #DeveloperInfrastructure #SoftwareEngineering #AIcoding #VersionControl #Scalability #DevTools #Pando
