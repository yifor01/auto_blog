---
title: "Policy and World Modeling Co-Training for Language Agents"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.02388
score: 98
model: tencent/hy3-preview:free
generated_at: 2026-06-02T21:43:21.494599
---

📌 【Policy and World Modeling Co‑Training】語言代理訓練新框架：無額外計算開銷提升效能  

訓練基於強化學習（RL）的語言代理常面臨樣本效率低的瓶頸；要讓代理學得更好，通常需要更多的互動資料或額外的世界模型（world model）來進行離線規劃。這些做法往往伴隨額外的計算成本與資料收集負擔，讓實驗與部署變得更為昂貴。  

🤔 **你以為訓練語言代理一定需要更多算力？這篇論文說：不需要**  

論文提出的 PaW（Policy and World Modeling Co‑Training）框架嘗試在不增加額外計算開銷的情況下，同時優化政策（policy）與世界模型（world model），期望藉由共享同一批 on‑policy 強化學習軌跡（rollouts）來提升樣本效率與最終表現。  

🧪 **共享 on‑policy RL rollouts 的聯合優化機制**  

PaW 的核心設計是：在每次強化學習更新時，使用同一批由當前政策產生的 on‑policy 軌跡，既作為政策梯度的估計基礎，也作為訓練世界模型的監督信號。如此一來，政策學習與世界模型學習可以在同一個資料流上進行聯合優化，避免了額外的離線資料收集或獨立的模型訓練步驟。  

📈 **無額外計算開銷下的訓練效率提升（論文主張）**  

根據論文的說明，PaW 能在不增加額外運算資源的前提下，提升語言代理的訓練樣本效率，進而在相同互動步數下達到更好的政策表現。具體的實驗基準、環境或數據分數未在所提供的摘要中透露，因此這裡僅呈現論文所聲稱的主要貢獻：透過共享 on‑policy rollouts 實現政策與世界模型的共訓練，從而在不額外增加計算開銷的情況下改善代理學習。  

💡 **政策與世界模型的互補角色：共同學習 vs. 分離訓練**  

在傳統做法中，政策與世界模型通常是分階段訓練：先以環境互動資料訓練世界模型，再利用該模型進行離線規劃來更新政策。這種分離會導致兩個模型分別看到不同的資料分布，且世界模型的訓練往往需要額外的計算或資源。PaW 透過讓兩個模型同時從同一批 on‑policy 軌跡學習，使得世界模型能更緊貼當前政策的行為分布，政策則能即時受益於較準確的世界模型預測，理論上可減少模型漂移（model drift）並提升整體學習穩定性。  

⚠️ **僅以 on‑policy 為基礎、實驗範圍未詳、長期效果尚未驗證**  

- 該方法依賴 on‑policy rollouts，若離線或離策略（off‑policy）資源豐富的情境下，是否仍能保持優勢尚未說明。  
- 摘要未提供具體實驗環境（例如文字遊戲、工具使用、多輪對話基準）或比較基線的詳細數據，因而難以判斷其在不同任務上的普遍適用性。  
- 長期訓練穩定性、對超參數的敏感度以及在大規模模型（如十億參數級別）上的擴展性，均需後續工作進一步探討。  

🎯 **可直接納入現有 RL‑based 語言代理流程，降低額外資源需求**  

對於正在使用 on‑policy 算法（如 PPO、A2C）訓練語言代理的研究團隊，PaW 提供了一種「免額外成本」的改進途徑：只需在現有訓練迴圈中加入世界模型的預測損失與共享軌跡的更新，即可嘗試獲得樣本效率的提升。這樣的設計對於計算資源受限的實驗室或希望減少資料收集成本的產業應用皆具吸引力。  

🔗 **論文連結**  
📝 Policy and World Modeling Co‑Training for Language Agents  
👤 作者／機構：未在摘要中詳述（請參閱原文）  
🔗 https://huggingface.co/papers/2606.02388  

你是否曾嘗試過在語言代理訓練中加入世界模型？這種共享 on‑policy 軌跡的做法是否能在你的實驗中帶來樣本效率的提升？歡迎在留言區分享你的經驗與想法 👇  

#AI #ReinforcementLearning #LanguageAgents #WorldModeling #PolicyCoTraining #HuggingFace #RLResearch #AgenticAI
