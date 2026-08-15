---
title: Aligning protein-generative models to experimental fitness with ProteinDPO
source: Nature.com
url: https://www.nature.com/articles/s41592-026-03137-3
model: nvidia/nemotron-3-ultra-550b-a55b:free
generated_at: '2026-08-15T06:18:30.683760'
score: 92
---

📌 ProteinDPO：用 DPO 將蛋白質生成模型對齊至實驗適應度

TL;DR：Nature 發表研究，引入 DPO 讓結構條件語言模型直接從生物物理實驗數據學習，提升蛋白質生成的實驗成功率。

生成式模型已能設計新穎蛋白質骨架，但「長得像」天然蛋白與「在實驗室真能折疊、表達、具功能」中間，隔著巨大的生物物理鴻溝。傳統無監督預訓練只學統計分布，不懂熱力學穩定性與表達適應度。

🤔 **從統計模仿到生物物理對齊**

蛋白質生成模型通常在海量無標註序列上預訓練，擅長捕捉演化保守的序列模式，卻缺乏實驗驗證的生物物理約束（如熱穩定性、溶解度、表達量）。這導致生成序列雖通過計算指標，實測卻高比例失敗，成為「設計-構建-測試」迴圈的瓶頸。

🧩 **ProteinDPO：把 DPO 帶進蛋白質工程**

研究提出 **ProteinDPO**，將原為 LLM 對齊人類偏好而設計的 **Direct Preference Optimization (DPO)**，應用於無監督的**結構條件語言模型**。核心思路是：
1.  收集成對實驗數據：同結構下、高適應度與低適應度的序列對。
2.  直接用偏好對最佳化生成策略，免去訓練獨立獎勵模型與 PPO 強化學習的複雜流程。
3.  讓模型在生成階段就內隱「懂」生物物理約束，而非事後過濾。

📊 **穩定性預測達具競爭力表現**

論文指出，經 ProteinDPO 對齊後的模型在**穩定性預測任務**上達成具競爭力的效能（competitive performance），證實 DPO 能有效將實驗適應度資訊注入生成式模型，縮小計算設計與實驗驗證的落差。

🎯 **對蛋白質工程師的實務啟示**

- **基礎設施更輕量**：無需部署 RLHF 完整管線（Reward Model + PPO），DPO 僅需成對實驗數據即可微調，大幅降低工程門檻。
- **數據效率關鍵**：成效取決於高品質「高/低適應度序列對」的可得性，建議優先建構具實驗標註的偏好資料集。
- **迴圈加速**：模型生成即具備生物物理先驗，可減少無效構建，加速「設計-構建-測試」週轉。

🔗 **來源**
- 標題：Aligning protein-generative models to experimental fitness with ProteinDPO
- 作者／機構：Talal Widatalla, Ashir A. Borah, Samuel H. King, Claudia L. Driscoll, Rafael Rafailov, Brian L. Hie
- 連結：https://www.nature.com/articles/s41592-026-03137-3

#ProteinDesign #DPO #LLM #ProteinEngineering #NatureMethods #GenerativeAI #Bioinformatics #MachineLearning #ProteinDPO #Alignment
