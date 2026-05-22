---
title: "Unified Data Selection for LLM Reasoning"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.22389
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:29:36.746120
---

📌 **HES 資料選擇法：統一提升 LLM 推理訓練**

你以為訓練 LLM 必須靠龐大的高品質推理資料？一個只計算最高熵 token 的免訓練指標，竟能讓僅 20% 的資料達到與完整資料相同的效果。

🤔 **高品質推理資料的取得成本過高**

現有方法要麼計算開銷巨大，要么無法可靠地區分高低品質的推理樣本。這使得在監督微調（SFT）、拒絕微調（RFT）與強化學習（RL）等主流訓練範式中，資料選擇成為瓶頸。

🧪 **基於最高‑entropy token 的訓練免費指標 HES**

論文提出 High-Entropy Sum（HES）：對每條推理樣本，僅取最高 entropy（例如前 0.5%）的 token，將它們的 entropy 加總，得到一個無需任何額外訓練即可計算的分數。此分數直接反映樣本的推理品質。

📊 **在 SFT、RFT、RL 三種範式上皆顯著提升**

- **SFT**：使用 HES 排名前 20% 的資料進行微調，其效果與使用全量資料相當；相反，使用最低 HES 的資料則會顯著降低效能。  
- **RFT**：以 HES 為基礎的資料選擇策略明顯優於現有基線方法。  
- **RL**：挑選 HES 分數高的成功軌跡進行強化學習，模型能學到更強的推理模式，顯著超越其他比較方法。

🔍 **最高 entropy token 捕捉了推理的不確定性**

作者認為，推理過程中不確定性最高的 token 往往對應於關鍵的決策點或難以直接推導的步驟。因此，只關注這些 token 的 entropy 能有效過濾掉那些推理過於機械或缺乏深度的樣本，保留真正能提升模型推理能力的資料。

⚠️ **僅針對特定 entropy 切割比例進行驗證，未探討更廣泛的 token 選擇策略**

實驗中將最高 entropy 的比例固定為 0.5%；不同比例或其他 entropy 聚合方式的影響尚未系統測試。此外，評估主要集中在公開基準上，真實世界長鏈結推理任務的適用性仍需進一步驗證。

🎯 **在資料管線中直接採用 HES，先跑小規模篩選再決策訓練比例**

- 計算 HES 幾乎無額外開銷，可作為資料預處理的快速過濾步驟。  
- 依據任務資源，先選取 top‑20% HES 資料進行 SFT，或在 RFT/RL 階段優先使用高 HES 軌跡。  
- 若資源極為有限，甚至可僅使用 top‑10% 來快速驗證模型是否具備基本推理能力。

🔗 **論文連結**  
📝 Unified Data Selection for LLM Reasoning  
👤 Xiaoyuan Li, Yubo Ma, Chengpeng Li, Fengbin Zhu, Yiyao Yu  
🏫 University of Science and Technology of China; Alibaba Group; National University of Singapore  
🔗 https://arxiv.org/abs/2605.22389  

你會在資料選擇 pipeline 中嘗試使用 entropy‑based 指標嗎？歡迎留言分享你的經驗或疑問 👇

#LLM #Reasoning #DataSelection #HES #SFT #RFT #RL #AIResearch #Alibaba #USTC #NUS #MachineLearning
