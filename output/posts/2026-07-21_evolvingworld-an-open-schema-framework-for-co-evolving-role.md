---
title: 'EvolvingWorld: An Open-Schema Framework for Co-Evolving Role-Play Agents and
  World Model in Interactive Literary World'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.17250
score: 84
model: tencent/hy3:free
generated_at: '2026-07-21T08:34:32.394119'
---

📌 【EvolvingWorld】突破靜態模擬：實現角色與世界觀的長期共演

TL;DR：透過開放式架構，讓角色與世界狀態能隨著劇情發展持續演進。

🤔 **目前的文學模擬系統面臨兩大瓶頸**

現有的互動式文學模擬系統，通常將模擬視為「靜態的人格模仿」或是「孤立的場景生成」。這種做法無法捕捉角色與世界之間「隨時間共同演進」的動態過程，導致模擬內容缺乏長期連貫性。

🧩 **EvolvingWorld：角色與世界的雙模態共演架構**

為瞭解決上述問題，EvolvingWorld 將文學模擬建模為一個「長程過程 (long-horizon process)」，其中角色互動、場景推進以及角色與世界的狀態更新，都必須持續且一致地進行。

該架構由兩個耦合模組組成：
- **角色代理 (Character Agent)**：負責多角色角色扮演 (role-play) 以及持久的角色設定演進 (profile evolution)。
- **世界模型 (World Model)**：基於 LLM，負責維護全域、地點及實體層級的狀態，並驅動場景推進。

與以往依賴固定 Schema（結構化綱要）的系統不同，EvolvingWorld 採用了「開放式架構 (open-schema framework)」，使其能支援各種不同文學世界中的模擬需求。

📊 **大規模資料集與評估協定**

研究團隊透過以下方式來驗證與訓練此框架：
- **任務設計**：定義了 7 個可訓練任務，涵蓋場景初始化、互動生成與狀態更新。
- **資料來源**：從 57 本書籍中構建資料集，產生了 138,596 筆監督式訓練樣本與 222 個測試快照 (snapshots)。
- **評估方式**：引入了一種軌跡層級 (trajectory-level) 的 LLM-as-Judge 評估協定，橫跨 10 個維度與 20 個指標。

💡 **實驗結果顯示，長程模擬效能獲得提升**

實驗證明，EvolvingWorld 能透過有效維護持久且連貫的角色與世界發展，成功改善長程模擬 (long-horizon simulation) 的表現。

🔗 **來源**
- 標題：EvolvingWorld: An Open-Schema Framework for Co-Evolving Role-Play Agents and World Model in Interactive Literary World
- 連結：https://huggingface.co/papers/2607.17250

#AI #LLM #RolePlay #WorldModel #EvolvingWorld #MachineLearning #NLP #LiterarySimulation #CharacterAI #ArtificialIntelligence
