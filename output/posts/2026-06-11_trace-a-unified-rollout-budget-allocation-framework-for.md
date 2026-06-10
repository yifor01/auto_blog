---
title: 'TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic
  Reinforcement Learning'
source: arXiv
url: http://arxiv.org/abs/2606.11119v1
score: 96
model: google/gemma-4-31b-it:free
generated_at: '2026-06-11T00:42:09.449208'
---

📌 **TRACE：把多回合 LLM 代理的 Rollout 資源細分到樹狀前綴，讓 Reward 變得更「有對比」！**

隨著大型語言模型越來越會「思考」與「行動」，研究者開始用 **RL with Verifiable Rewards (RLVR)** 讓模型在多回合對話中自行學習。但傳統的 rollout 方式往往只在 **prompt 層級** 分配樣本，導致同一條對話路徑上不同回合的資訊差異被忽略，最終的 reward 變得「平淡」── 甚至每一步都得到相同的終局分數。  

**TRACE**（Tree Rollout Allocation for Contrastive Exploration）正是為了解決這個「Reward 對比不足」的痛點，將資源從根 prompt 延伸到每一個 **ReAct‑style 思考‑行動‑觀察** 的回合前綴，形成 **樹狀 Rollout**，在固定的取樣預算下自動聚焦在最可能產生 **混合終端獎勵** 的節點。

---

### 🤔 為什麼「Reward 對比」這麼重要？

在多回合代理任務中，若所有 rollout 最終只得到「好」或「壞」兩種相同的評分，策略更新的訊號會極度弱化，模型難以辨識哪一步的決策真正影響結果。提升 reward 的 **variance**（對比度）等同於給予政策更清晰的學習方向。

---

### 🧪 研究設計：從 Prompt 到前綴的細粒度分配

1️⃣ **節點化每回合**：把 ReAct 風格的「思考 → 行動 → 觀察」視為語意上獨立的節點。  
2️⃣ **樹狀 Rollout**：根節點是原始 prompt，子節點是每一步的前綴，向下展開形成多條分支。  
3️⃣ **共享成功率預測器**：一個可泛化的模型根據已觀測的前綴歷史，估算「在此節點繼續下去」的成功機率。  
4️⃣ **動態預算分配**：根據預測的混合終端獎勵機率，將有限的 rollout 數量分配給最具資訊價值的根或中間前綴。  

這樣的設計讓 **TRACE** 能在同樣的取樣成本下，產出更具差異性的回饋，進而放大政策更新的信號。

---

###  **核心發現：在同樣預算下，Qwen‑3‑14B 多跳 QA 準確率提升 2.8 分**

- 基準模型（未使用 TRACE）平均分：**78.4%**  
- TRACE 加持後：**81.2%**  
- 與其他同類型的 rollout 分配方法相比，TRACE 同樣的樣本數下 **效能提升 2–3%**，且計算開銷僅略高於傳統隨機分配。

---

### 💡 深入分析：為何樹狀分配比單一 Prompt 更有效？

- **資訊不均衡**：同一條對話的前半段往往決定後半段的搜索空間。TRACE 把預算集中在「分岔點」上，讓模型更快發現「關鍵決策」所在。  
- **混合獎勵的概率提升**：預測器會挑選那些在歷史上既出現過好結果也出現過壞結果的前綴，這類節點的 reward variance 最大，最能驅動梯度更新。  
- **可共享的預測器**：不需要為每個節點訓練獨立模型，降低了額外的訓練成本，且在不同任務間具備一定的遷移能力。

---

### ⚠️ 研究限制

- **預測器依賴歷史資料**：在全新領域或極少樣本的情況下，成功率估計可能不夠可靠。  
- **只在 Outcome‑Only Reward 設定下驗證**：若引入更細緻的中間獎勵（例如 step‑wise feedback），TRACE 的效益尚未測試。  
- **實驗以 Qwen‑3‑14B 為主**：其他模型（如 GPT‑4、Claude）上的表現仍需進一步驗證。

---

### 🎯 實務啟示：如何把 TRACE 帶入自己的代理系統？

1️⃣ **接入前綴預測器**：將已有的成功率估計模型（可用簡單的二分類器）作為 TRACE 的「錨點」評分器。  
2️⃣ **設定預算上限**：根據硬體資源，先在小規模測試（如 1k rollouts）觀察 variance 改善幅度，再逐步擴大。  
3️⃣ **結合現有 RLVR 框架**：TRACE 只改變 **budget allocation** 部分，與現有的 PPO / REINFORCE 等演算法兼容，無需大幅改寫訓練流程。  
4️⃣ **監控混合獎勵比例**：在訓練過程中持續追蹤「高/低獎勵」的分布，確保預算分配仍聚焦在資訊豐富的節點上。

---

🔗 **論文資訊**  
📝 **TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning**  
👤 Heming Zou, Qi Wang, Yun Qu, Yuhang Jiang, Lizhou Cai  
📄 arXiv: 2606.11119v1 [http://arxiv.org/abs/2606.11119v1](http://arxiv.org/abs/2606.11119v1)  
💻 開源代碼（若有）已於作者 GitHub 公布，直接下載即可在自己的 RLVR pipeline 中測試。

---

💬 **你在多回合 LLM 代理中，有遇到過「reward 變平」的問題嗎？**  
試試把資源拉到「關鍵回合」上，或許能看到意想不到的提升！歡迎在下方分享你的實驗心得或問題，讓大家一起討論。👇

#RLVR #AgenticAI #ReinforcementLearning #LLM #TreeSearch #TRACE #MachineLearning #AIResearch #Qwen3 #PromptEngineering
