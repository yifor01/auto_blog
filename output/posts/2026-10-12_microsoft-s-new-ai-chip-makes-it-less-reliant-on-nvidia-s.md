---
title: Microsoft’s new AI chip makes it less reliant on Nvidia’s GPUs
source: The Verge AI
url: https://www.theverge.com/news/1009465/microsoft-maia-300-chip-improvements-rollout
model: claude-code/sonnet
generated_at: '2026-10-12T23:59:43.451033'
score: 80
---

📌 微軟 Maia 300：想甩開對 Nvidia GPU 的依賴

TL;DR：微軟發布第三代自研 AI 晶片 Maia 300，宣稱效能大幅提升，2027 年起成為自家產品的主力推理系統。

當全世界的雲端巨頭都在排隊搶購 Nvidia GPU 時，微軟選擇走另一條路：自己做晶片，而且宣布這次要讓它成為公司 AI 服務的「主力」——不再只是備援方案。

🤔 **第三代自研晶片，目標是「主力推理系統」**

微軟今日發布第三代自研 AI 晶片 Maia 300，定位為「微軟產品與服務的主力 AI 推理系統」。它是去年一月才發布的 Maia 200 的後繼產品，而 Maia 200 目前已經在 Microsoft Copilot、GitHub Copilot、Microsoft Foundry 以及微軟自家 AI 模型的生產工作負載上運行。Azure 雲端部門執行副總裁 Scott Guthrie 表示，Maia 200 是公司機隊中，以實際 AI 服務指標衡量表現最好的基礎設施。

🧩 **用 chiplet 架構換效能**

Maia 300 採用新的 chiplet 架構，建構於 TSMC N2P 製程節點，將運算、記憶體控制器與 I/O 功能拆分開來。Azure 硬體與基礎設施團隊表示，這樣的設計讓更多矽晶面積能分配給運算效能，同時讓每個功能都能使用最適合自己的技術。

📊 **宣稱 40% 更高能效，7 倍機架輸出量**

Guthrie 表示，相較於主流 GPU 系統，Maia 300 預期能帶來「每百萬瓦 40% 更多 token 輸出量」；在 96 加速器的完整機架配置下，更可達到 Maia 200 的 7 倍機架層級 token 輸出量。微軟計畫從 2027 年開始，把 Azure Maia 家族擴展至數十億瓦等級的部署規模。

💡 **為全端自研鋪路**

Maia 300 的設計目標明確指向目前 LLM 工作負載的新趨勢：長上下文推理、延遲敏感的對話體驗，以及持續多步驟的 agentic 任務。微軟 AI 部門 CEO Mustafa Suleyman 表示，「我們必須從全端一路做到矽晶片層級」，並強調在 Maia 上運行微軟自家 AI 模型，是團隊的關鍵焦點——這也被視為微軟追趕 Google DeepMind、OpenAI、Anthropic 的策略之一。

⚠️ **目前仍是公司自己的說法**

Maia 300 要到 2027 年才開始大規模投入生產工作負載，報導中引用的效能提升數字（40% 能效、7 倍輸出量）皆來自微軟自身說法，尚未見第三方獨立驗證；報導本身也未揭露具體的晶片微架構細節（如核心數、記憶體頻寬規格），對工程師而言目前還難以據此做出技術選型判斷。

🎯 **實務啟示**

如果你的團隊已經在 Azure 上跑推理工作負載，可以留意 Maia 300 於 2027 年量產後，是否會開放給一般客戶使用、以及屆時的定價與 API 相容性；在那之前，這則消息更適合當作觀察雲端廠商晶片自研趨勢的參考，而非立即影響架構決策的依據。

🔗 **來源**
- 標題：Microsoft's new AI chip makes it less reliant on Nvidia's GPUs
- 作者／機構：Tom Warren（The Verge）
- 連結：https://www.theverge.com/news/1009465/microsoft-maia-300-chip-improvements-rollout

#Microsoft #Maia300 #AIChip #Azure #Nvidia #AIInfrastructure #Chiplet #CloudComputing #Semiconductors #AIInference
