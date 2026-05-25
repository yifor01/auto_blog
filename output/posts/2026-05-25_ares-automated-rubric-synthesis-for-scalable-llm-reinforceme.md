---
title: "ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.23454
score: 120
model: tencent/hy3-preview:free
generated_at: 2026-05-25T20:26:16.707085
---

📌 【USTC + Alibaba + NUS】ARES：自動合成題目專用評分規則，讓 LLM 強化學習規模化

你是否曾想過，讓大型語言模型在開放式任務上靠強化學習持續進步，最大的阻礙其實是怎麼設計出「好用」且能大量產出的獎勵函數？現有做法常依賴專家手寫評分規則或固定題目集，難以應對每個問題的細節差異。

🤔 **從原始文件直接產出題目與評分規則**

ARES（Automated Rubric synthEsis for Scalable RL）提出一個端到端的管線：從未標註的預訓練文件出發，自動生成自包含的問答對，並同時為每個問題合成對應的加權評分規則。這樣得到的資料能提供「逐題」的獎勵監督，讓強化學習不再受限於只有可自動驗證答案的任務。

🧪 **條件生成與多重過濾提升品質**

為確保產出的問答具備多樣性與正確性，ARES 在生成過程中加入領域標籤與角色資訊作為條件，並施加三種驗證過濾：題目自包含性、答案忠實度、以及評分規則的有效性。經過這些篩選，最終得到 100K 份帶有題目專用評分規則的標註樣本，橫跨十個不同領域。

📊 **在七個基準上強於多種基線**

實驗顯示，以 ARES 建構的資料進行規則基礎的強化學習，相較於持續預訓練、監督微調以及傳統二元獎勵強化學習，在所有七個基準上均有提升。特別是在多維度開放式任務（例如醫療諮詢與指令遵循）上，改善幅度最為顯著。

💡 **關鍵在於「題目層級」的獎勵設計**

與過去依賴任務級固定規則不同，ARES 的評分規則是針對每個具體問題而生成的，能更精準地反映該問題的評估需求。這意味著模型在學習過程中能得到更細緻、符合情境的回饋，從而在需要同時考慮正確性、風格、安全等多個維度的開放式生成任務中獲得更好的表現。

⚠️ **目前僅證明資料規模與跨領域有效性，長期效果尚待觀察**

論文主要報告了建構 100K 規模資料集以及在七個基準上的即時表現提升。尚未針對長期訓練穩定性、不同模型規模的泛化潛力，或是真實部署環境中的成本效益進行深入探討。

🎯 **對 RLHF 與獎勵建模研究的直接啟發**

- 若你正在從事基於人類回饋的強化學習（RLHF）或獎勵模型開發，ARES 提供了一種可擴展的方式來自動產出高質量的題目‑評分規則對。  
- 在需要多維度評估的應用（如醫療建議、客服對話、複雜指令遵循）中，採用題目專用規則有望減少對人工標註的依賴。  
- 未來工作可探索將此管線與更大規模的預訓練語料結合，或是在不同強化學習演算法上進行更細緻的 ablation 研究。

🔗 **論文連結**  
📝 ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning  
👤 Xiaoyuan Li, Keqin Bao, Moxin Li, Yubo Ma, Yichang Zhang  
🏫 University of Science and Technology of China; Alibaba Group; National University of Singapore  
🔗 https://arxiv.org/abs/2605.23454  

你認為在開放式任務中，題目層級的獎勵設計是否能成為下一代 LLM 訓練的標準？歡迎留言討論 👇

#LLM #ReinforcementLearning #RLHF #RewardModeling #ARES #USTC #Alibaba #NUS #AIResearch #MachineLearning
