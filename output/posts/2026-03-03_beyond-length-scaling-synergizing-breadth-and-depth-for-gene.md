---
title: "Beyond Length Scaling: Synergizing Breadth and Depth for Generative Reward Models"
source: ChatPaper/AI
url: https://arxiv.org/abs/2603.01571
score: 130
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-03T19:48:08.054301
---

📌 **Mix-GRM：重新定義獎勵模型，用「廣度+深度」超越單純長度擴增**

你可能聽過 Chain-of-Thought (CoT) 推理，也知道擴增長度能提升模型表現。但你知道嗎？**不是所有推理都一樣有效**。

🤔 **長度擴增的盲點：廣度與深度的差異化效應**

現有的 Generative Reward Models (GRMs) 普遍採用「無結構長度擴增」策略，也就是單純讓模型思考更久。然而，City University of Hong Kong 與騰訊的研究團隊發現：**不同的推理機制，效果差異極大**。

他們將 CoT 分為：
- **廣度推理 (B-CoT)**：多維度原則覆蓋，擅長處理主觀偏好判斷
- **深度推理 (D-CoT)**：實質判斷的合理性，擅長處理客觀正確性任務

🧪 **Mix-GRM：模組化合成架構的突破**

Mix-GRM 的核心創新在於**重新配置原始推理文本**，透過模組化合成管道，將其轉化為結構化的 B-CoT 和 D-CoT。接著分別透過 Supervised Fine-Tuning (SFT) 和 Reinforcement Learning with Verifiable Rewards (RLVR) 進行訓練。

🎯 **為什麼這很重要？**

- 平均超越領先的開源獎勵模型 **8.2%** (State-of-the-Art)
- 在五個不同評測集上都展現優勢
- 揭示了推理機制與任務類型之間的關聯性

 **推理機制與任務類型的精準匹配**

研究發現了明確的分工：
- **B-CoT 擅長**：主觀偏好任務（如評論分數、風格偏好）
- **D-CoT 擅長**：客觀正確性任務（如數學推理、事實驗證）

⚠️ **錯配的代價：直接導致表現下降**

如果將深度推理用在主觀任務，或將廣度推理用在客觀任務，都會**直接導致表現下降**。這意味著：不是越長越好，而是越「對」越好。

💡 **RLVR 的極化效應：模型會自動切換推理模式**

更有趣的是，當模型經過 RLVR 訓練後，會表現出**自發的極化效應**：
- 遇到主觀任務 → 自動傾向使用 B-CoT
- 遇到客觀任務 → 自動傾向使用 D-CoT

這種「推理風格分配」的能力，是 RLVR 訓練的**自發行為**，而非人工設計。

🎯 **實務啟示：獎勵模型的設計原則**

- 長度擴增 ≠ 效果保證
- 理解任務本質，選擇對應的推理機制
- RLVR 不只是優化，還能誘發模型的高階行為

🔗 **論文連結**
📝 Beyond Length Scaling: Synergizing Breadth and Depth for Generative Reward Models
👤 Qiyuan Zhang, Yufei Wang, Tianhe Wu, Can Xu, Qingfeng Sun
🔗 論文：arxiv.org/abs/2603.01571
🔗 GitHub：github.com/Don-Joey/Mix-GRM
🔗 Hugging Face：huggingface.co/collections/DonJoey/mix-grm

#AI #RewardModel #CoT #RLVR #大語言模型 #獎勵建模 #技術進展

---

**你的看法呢？** 你認為未來的 AI 評估系統應該更重視「推理品質」還是「推理長度」？歡迎留言討論 👇
