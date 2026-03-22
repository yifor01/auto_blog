---
title: "Mozi: Governed Autonomy for Drug Discovery LLM Agents"
source: ChatPaper/AI
url: https://arxiv.org/abs/2603.03655
score: 108
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-05T12:28:28.795202
---

📌 【Mozi 架構】AI 藥物發現的雙層治理革命：從「幻覺」到「可追溯」

AI 藥物發現的夢想很美：讓 LLM 代理人統一科學推理與計算，自動探索新藥物。但現實很殘酷：這些代理人常常因為不受控的工具使用和長期決策失誤，讓早期的「幻覺」一路乘積到最後的失敗。

🤔 **為什麼 AI 藥物發現這麼難？**

想像你讓 AI 探索一個化合物空間，它可能：
- 在 Target Identification 階段就做出錯誤假設
- 用不可信的工具組合執行計算
- 在 Lead Optimization 階段無法回頭修正錯誤
- 最終產出一個在理論上說得通、實際上完全不可行的藥物候選

這就是目前 LLM 代理人的核心困境：它們擅長創意推理，但缺乏長期決策的治理機制。

🧪 **Mozi 的雙層架構：從混亂到可控**

Mozi 的創新在於將 LLM 代理人切分成兩個層級：

**Layer A (Control Plane) - 治理層**
- 建立主管-工作者階層架構
- 強制角色基礎的工具隔離
- 限制執行在受控的動作空間
- 推動基於反思的重新規劃

**Layer B (Workflow Plane) - 工作流程層**
- 將藥物發現的標準階段（從靶點識別到先導物優化）建模為有狀態的技能圖
- 整合嚴格的資料合約
- 在高不確定性的決策邊界設置策略性的人工檢查點

這種設計的核心哲學是：「自由推理用於安全任務，結構化執行用於長期管線」

 **實驗結果：從理論到實踐**

在 PharmaBench 評測集上，Mozi 展現了：
- 比現有基準更好的調度準確性
- 能夠在巨量的化學空間中導航
- 能夠執行嚴格的毒性過濾
- 能夠生成極具競爭力的計算內候選物

更重要的是，透過端到端的治療案例研究，Mozi 證明了它能將 LLM 從一個脆弱的對話者轉變為可靠、受治理的共同科學家。

💡 **核心創新：錯誤累積的完全緩解**

Mozi 的關鍵突破在於提供：
- 內建的穩健性機制
- 追蹤級的可追溯性
- 完全緩解錯誤累積的能力

這意味著你可以追蹤 AI 在每個決策點的推理過程，並在錯誤擴散之前進行修正。

⚠️ **為什麼這很重要？**

這不只是一個技術改進，而是 AI 在高風險領域應用的範式轉移：
- 從「不可信的黑箱」到「可治理的夥伴」
- 從「幻覺驅動的探索」到「結構化推理」
- 從「無法追蹤的失敗」到「可解釋的成功」

🎯 **實務啟示**

對於藥物發現領域的從業者：
- 這套架構可以作為評估其他 LLM 代理人的標準
- 治理層的概念可以應用到其他高風險領域
- 人為檢查點的設計原則值得借鑑

🔗 **論文連結**
📝 Mozi: Governed Autonomy for Drug Discovery LLM Agents
👤 He Cao, Siyu Liu, Fan Zhang, Zijing Liu, Hao Li @ International Digital Economy Academy (IDEA)
🔗 論文：arxiv.org/abs/2603.03655

你怎麼看待 AI 在藥物發現領域的應用？歡迎分享你的觀點 👇

#AI #DrugDiscovery #LLM #機器學習 #藥物研發 #人工智慧 #計算生物學 #BiomedicalEngineering
