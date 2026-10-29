---
title: 'Le Chonk: Built for Coders, Trusted by Defenders.'
source: Mistral AI
url: https://mistral.ai/news/mistral-large-4-oss/
model: claude-code/sonnet
generated_at: '2026-10-29T21:54:37.993696'
pinned: true
---

📌 Mistral Large 4 開源發布，程式與防禦網安雙線領先

TL;DR：Mistral 開源 1 兆參數的 Large 4（Le Chonk），在開放權重模型中拿下程式與防禦網安雙項優勢。

就在公開預覽後短短三週，Mistral 把這顆 1 兆參數的旗艦模型練得更強，而且這次直接把權重交出來，讓所有人都能自己部署、自己調。

🤔 **從預覽到開源，只用三週持續強化學習**

Mistral Large 4（暱稱 Le Chonk）是一款原生多模態的 1 兆參數模型，先前以公開預覽形式推出，獲得開發者社群與早期客戶的大量回饋。團隊表示，在持續擴大強化學習（reinforcement learning）訓練規模後，程式能力與防禦性網路安全能力有了顯著提升，且目前觀察到的進步曲線尚未飽和。這次發布的版本，正式公開了模型權重。

🧩 **三種推理模式，讓開發者自己選成本與精度**

Mistral Large 4 提供三種推理模式，讓開發者依任務需求權衡效能與推理成本：

| 模式 | 建議使用情境 |
|---|---|
| Low | 簡單任務，取代原本的「None」模式 |
| Medium | 日常任務 |
| High（預設） | 需要高精度與充分推理的高難度任務 |

此外，Mistral 強調這顆模型從零開始在歐洲基礎設施上訓練，血統（lineage）從初始訓練到發布全程可追溯，定位為「Sovereign AI（主權 AI）」的基礎模型，讓企業與機構能夠自行掌控、客製化並自架部署。

📊 **程式能力：FrontierCode、Terminal-Bench 都拿下開放權重第一**

在 Cognition 的私有基準 FrontierCode 2.0（評估 agent 修改的程式碼是否足以被 repo 維護者合併）上，Mistral Large 4 以 19.7% 領先其他開放權重模型：

| 模型 | FrontierCode 2.0 分數 |
|---|---|
| Mistral Large 4 | 19.7% |
| DeepSeek V4.1 Flash | 19.3% |
| GLM-5.3 | 17.8% |
| Kimi K3 | 17.3% |
| GLM-5.3 Flash | 14.2% |
| Beam 1.0 | 2.9% |

在 Artificial Analysis 的 Coding Agent Index 上，Mistral Large 4 拿下 48 分，與目前最強的開放權重模型 GLM-5.3 幾乎打平，但平均每個任務少用 47% 的 token。在 Terminal-Bench 4.0 上，分數較預覽版提升 13 個百分點來到 41%，同時輸出 token 減少 30%，在開放權重模型中略微領先 GLM-5.3 的 40%。

人類評測上，根據 Surge Code 的盲測雙兩兩比較，Mistral Large 4 對 GLM-5.3 與 Kimi K3 的勝率都是 64%，對 DeepSeek V4.1 Flash 勝率 56%，僅在對比 Claude Opus 5.5 時落居下風（22%），整體在受測模型中排名僅次於 Claude Opus 5.5。

🔐 **防禦網安：高拒絕率 + 高任務分數並存**

在 Artificial Analysis 的 Cyber Index（衡量模型發現、重現、驗證並修補漏洞而不破壞既有功能的能力）上，Mistral Large 4 取得 51% 的分數。Mistral 特別強調，模型能區分「防禦性」與「惡意攻擊性」的網安任務，不會因為過度謹慎而拒絕合法的防禦性請求；在 JailbreakBench、StrongREJECT、AgentHarm 等網安相關惡意請求測試中，平均拒絕率達 96.6%，是其測量範圍內開放模型中最高的。Booz Allen Hamilton 與 Cisco 的安全團隊也在文中分享了與 Mistral 合作評測與後續協作的看法。

⚠️ **仍是「說自己最強」的官方發布**

以上數據均來自 Mistral 官方部落格引用的第三方基準（Cognition、Artificial Analysis、Surge Code 等），尚未看到獨立第三方的覆核報告，實際表現仍建議開發者在自己的任務情境中實測驗證。

🎯 **實務啟示**

對於需要自架部署、符合資料主權或法規要求的團隊（例如政府、金融、國防相關場景），Mistral Large 4 的開放權重特性加上三段式推理模式，提供了在效能與推理成本之間彈性取捨的空間；若你的應用場景涉及程式代理（coding agent）或防禦性安全掃描，這次釋出的版本值得納入評測清單。

🔗 **來源**
- 標題：Le Chonk: Built for Coders, Trusted by Defenders.
- 作者／機構：Mistral AI
- 連結：https://mistral.ai/news/mistral-large-4-oss/

#Mistral #MistralLarge4 #OpenWeights #LLM #CodingAgent #Cybersecurity #SovereignAI #ReinforcementLearning #AIModels #OpenSourceAI
