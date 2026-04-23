---
title: "RADS: Reinforcement Learning-Based Sample Selection Improves Transfer Learning in Low-resource and Imbalanced Clinical Settings"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.20256
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-04-23T19:53:54.267417
---

📌 RADS強化學習優化臨床樣本選擇

你以為臨床AI低資源場景下，少樣本微調選越多元的樣本效果越好？
研究發現，傳統主動學習方法在極端類別不平衡時，反而會偏好異常值而非有效樣本，導致模型效能下降。

🤔 **低資源臨床場景的遷移學習，樣本品質比數量更重要**
遷移學習中常用的少樣本微調（few shot fine-tuning）策略，成效高度依賴訓練樣本的品質。主動學習方法如不确定性採樣、多樣性採樣雖能篩選出有用的樣本，但在極低資源、類別極度不平衡的臨床場景中，這類方法往往會偏好異常值，而非真正具備資訊量的樣本，反而導致模型效能下滑。臨床場景下標註成本高、罕見病或感染類陽性樣本極少，這個問題尤為突出。

🧪 **多個真實臨床數據集驗證RADS效果**
本研究提出RADS（Reinforcement Adaptive Domain Sampling，強化自適應領域採樣），是一種基於強化學習的穩健樣本選擇策略，核心目標是透過強化學習識別最具資訊量的訓練樣本。團隊在多個真實世界臨床數據集上進行實驗，對比RADS與傳統主動學習方法的表現。

💡 **RADS提升遷移性，極端類不平衡下更穩健**
實驗結果顯示，相較於傳統主動學習方法，RADS的樣本選擇策略能有效提升模型的遷移性；即便在極端類別不平衡的條件下，RADS仍能維持穩健的模型效能，不會像傳統方法那樣出現效能下滑的問題。

💡 **強化學習可避免選到無關異常值**
傳統主動學習方法在低資源、類不平衡場景下失效的核心原因，在於其採樣邏輯容易選取到偏離正常分布的異常值，這些樣本對模型學習真實數據分佈並無幫助。RADS引入強化學習框架，能夠更精準地判斷樣本的資訊價值，避開無參考價值的異常值，從而選出真正有助於模型遷移學習的訓練樣本。

⚠️ **實作門檻高，需自行建置RL框架**
根據研究評估，RADS的實作門檻較高，研究者需要自行建置強化學習框架才能應用該策略，這是當前落地的主要限制。

🎯 **醫療AI研究者可參考RADS選樣邏輯**
對於從事醫療AI、特別是臨床低資源場景的研究者而言，RADS提供了一種全新的樣本選擇思路，能有效解決傳統主動學習在類別不平衡時的痛點。即便暫時無法搭建完整的強化學習框架，其「優先選取具資訊量樣本、避開異常值」的核心邏輯也值得參考，應用於自身的遷移學習流程優化中。

🔗 **論文連結**
📝 論文標題：RADS: Reinforcement Learning-Based Sample Selection Improves Transfer Learning in Low-resource and Imbalanced Clinical Settings
👤 作者：Wei Han, David Martinez, Anna Khanina, Lawrence Cavedon, Karin Verspoor
🏫 所屬機構：RMIT University; The University of Melbourne; National Centre for Infections in Cancer, Melbourne; Department of Infectious Disease, Peter MacCallum Cancer Centre
🔗 論文連結：https://arxiv.org/abs/2604.20256
📂 來源：ChatPaper/Computation and Language

從事醫療AI或遷移學習研究的朋友，你們在低資源、類別不平衡場景下選樣本時，遇到過哪些痛點？歡迎在留言區分享你的經驗👇

#AI #MachineLearning #醫療AI #遷移學習 #強化學習 #臨床AI #RADS #樣本選擇
