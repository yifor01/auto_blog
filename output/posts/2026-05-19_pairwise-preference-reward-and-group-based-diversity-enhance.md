---
title: "Pairwise Preference Reward and Group-Based Diversity Enhancement for Superior Open-Ended Generation"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.18191
score: 109
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:46:33.779208
---

📌 【Xingchen AGI Lab 最新研究】Pairwise Preference Reward 與 Group-Based Diversity 如何提升開放式生成？

你以為用強化學習讓 AI 更會說話就是提升多樣性？實際上，常見做法往往讓 outputs 越來越單調。

🤔 **標量獎勵難以捕捉主觀好惡，開放式任務陷入多樣性崩塊**

在可驗證的場景中，標量獎勵強化學習表現強大；但在開放式生成（如角色扮演、創意對話）中，正確性難以自動判斷，訓練獎勵模型又需要大量標註與運算。現有 RLVR 常導致多樣性崩塊，產出刻板或僵硬的文字，這與開放域應用的初衷背道而馳。

🧪 **以角色扮演任務為實驗平台，提出 PPR-GDE 框架**

研究團隊在角色扮演任務上實作了 Pairwise Preward Reward 與 Group‑Based Diversity Enhancement（PPR‑GDE）。該方法不依賴標量獎勵，而是透過成對偏好來保留主觀評估的比較結構；通過交換回答順序的重複比較來減少裁判位置偏見；並引入群組層級的多樣性獎勵，明確鼓勵同一批回答在語義上更分散。所有獎勵被整合為一個群組相對的策略優化目標。

🔑 **對齊品質與表達多樣性同時提升，勝過強 RL 基線**

實驗結果顯示，PPR‑GDE 在對齊品質與表達多樣性兩個維度上均優於現有的強化學習基線。進一步分析表明，成對偏好是實現主觀角度對齊的關鍵因子；群組多樣性指標則對獲得更佳的表達多樣性與更廣的語義覆蓋起著必不可少的作用。

💡 **偏好學習與顯式多樣性控制是開放式生成的新思路**

該工作指出，單純依賴標量獎勵難以兼顧對齊與多樣性；將偏好學習（透過成對比較）與顯式多樣性獎勵結合，能在不額外標註細粒度分數的情況下，維持主觀評估的比較資訊，同時主動推動語義分散。這為角色扮演、開放域對話及可控生成等場景提供了一種潛在的改進方向。

⚠️ **方法尚處早期階段，未公開程式碼，實際落地需進一步驗證**

論文尚未附帶開源實作，且實驗僅在角色扮演任務上進行。方法的泛化能力、在更大規模模型上的訓練成本以及與現有 RLHF 流程的整合方式，都需要後續工作進一步探索。

🎯 **實務上可先嘗試在偏好資料上加入群組多樣性獎勵，觀察對話多樣性變化**

對於正在使用 RLHF 或類似偏好對齊管線的團隊，可在現有的成對偏好資料基礎上，加入一個鼓勵批次內語義分散的獎勵項目，作為低成本的先驗實驗。同時，注意評估是否因而帶來對齊品質的下降，並根據具體應用場景調整兩個獎勵項目的權重。

🔗 **論文連結**
📝 Pairwise Preference Reward and Group-Based Diversity Enhancement for Superior Open-Ended Generation  
👤 Guining Cao, Jiaxin Peng, Chu Zeng, Yu Zhao, Shuangyong Song @ Xingchen AGI Lab; China Telecom Artificial Intelligence Technology (Beijing) Co., Ltd; Peking University; Tsinghua University  
🔗 https://arxiv.org/abs/2605.18191  

你在使用 AI 輔助寫作或對話時，有否留意到多樣性隨著使用次數而下降？歡迎在留言區分享你的經驗與看法 👇

#AI #ReinforcementLearning #OpenEndedGeneration #RolePlaying #PPR_GDE #XingchenAGILab #RLHF #創意對話 #多樣性控制
