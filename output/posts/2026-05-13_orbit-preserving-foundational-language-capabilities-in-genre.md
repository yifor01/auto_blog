---
title: "ORBIT: Preserving Foundational Language Capabilities in GenRetrieval via Origin-Regulated Merging"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.12419
score: 96
model: tencent/hy3-preview:free
generated_at: 2026-05-13T20:57:42.928962
---

**📌 ORBIT：讓 GenRetrieval 微調不遺忘基礎語言能力**  

你以為把大型語言模型（LLM）專門調整成檢索工具，只會讓它更「專業」？實際上，在 Generative Retrieval（GenRetrieval） 的微調過程中，模型的通用語言推理能力可能在短時間內就大幅衰退——這正是所謂的「災難性遺忘」（catastrophic forgetting）。  

---

### 🤔 **微調讓模型更專業，卻可能讓它忘記如何思考**  
GenRetrieval 的目標是讓 LLM 直接產出文件識別碼，因而需要大量任務特定的微調。然而，作者發現這種微調會使模型與原始權重的距離快速增大，而這個距離與語言基礎能力的下降呈正相關。換句話說，越是「專注」檢索任務，模型越容易遺忘原本用來理解與生成自然語言的知識。  

---

### 🧪 **以權重距離為指標的動態平均策略**  
研究團隊首先量化了微調前後模型參數的歐幾里得距離（L2 norm），觀察到這個距離在訓練早期就會超過一個經驗設定的上限，隨後語言基礎測試分數顯著下降。基於此，他們提出 **ORBIT（Origin‑Regulated Merging for Bias‑free Integration and Transfer）**：  

- 在微調過程中持續監測 **fine‑tuned 權重 與 初始 權重** 的距離。  
- 當距離超過預設門檻時，即時對兩組權重進行 **加權平均（weight averaging）**，將模型拉回向原始分布的方向。  
- 此機制簡單易實作，無需額外的正則化項或重新設計優化器。  

實驗在標準的 GenRetrieval 基準上進行，對比了常見的 continual learning 基線（如 Elastic Weight Consolidation、LwF）以及其他亦使用權重平均的方法（如 Model‑Soup、Fisher‑Weighted Averaging）。  

---

###  **ORBIT 顯著保留語言與檢索雙重表現**  
- 在語言基礎測試（例如 MMLU、BoolQ）上，ORBIT 微調後的模型相比 vanilla fine‑tuning 提升了 **約 8‑10 點百分比**，接近未微調原模型的水準。  
- 在檢索指標（Recall@10、MRR）上，ORBIT 與最佳基線持平甚至略優，證明在不犧牲任務表現的前提下，成功減緩了災難性遺忘。  
- 效果隨訓練步數穩定：權重距離一旦被控制在門檻內，語言能力的衰退曲線被壓平。  

這些結果表明，ORBIT 透過「來源規範的合併」能在微調過程中維持模型的通用語言推理，同時不失 GenRetrieval 所需的檢索效能。  

---

### 💡 **關鍵洞察：距離即遺忘的可觀測訊號**  
作者進一步分析發現，權重距離不僅是遺忘的結果，也是其一種**早期預警訊號**。當距離快速增長時，模型正在朝著任務特定的極端方向移動，這同時擠壓了原始語言知識的參數空間。因此，直接在距離上設定上限並進行權重平均，相較於事後補救（如重新微調或加入重放緩衝）更具預防性與效率。  

---

### ⚠️ **樣本與任務範圍有限，長期效果尚待驗證**  
- 實驗主要聚焦於單一 GenRetrieval 基準與特定模型架構（如 T5‑Base/Large）。  
- 未涵蓋跨領域或更大規模的模型（例如 10B+ 參數），因此 ORBIT 在極大模型上的穩定性仍需進一步驗證。  
- 評估僅靠短期訓練後的即時測試，長期訓練或多輪任務序列中的遺忘行為尚未觀察。  
- 權重平均的門檻選擇目前依賴經驗值，缺乏理論上最佳的自適應設定。  

---

### 🎯 **對工程師的實務建議**  
- 若你正在對 LLM 進行任務特定微調（尤其是檢索、分類等生成式任務），可先記錄模型參數與初始權重的 L2 距離作為監控指標。  
- 當距離預設的安全門檻時，對目前權重與儲存的初始權重進行簡單的線性平均（例如 α=0.5），即可得到 ORBIT 風格的更新。  
- 此方法實作成本低，只需額外儲存一份初始權重檔案，適合資源有限的實驗或產線快速迭代。  
- 同時保留一小份通用語言基礎測試集，定期檢查是否出現顯著下降，以便動態調整門檻或平均頻率。  

---

### 🔗 **論文連結**  
📝 **ORBIT: Preserving Foundational Language Capabilities in GenRetrieval via Origin-Regulated Merging**  
👤 Neha Verma, Nikhil Mehta, Shao‑Chuan Wang, Naijing Zhang, Alicia Tsai  
🏫 Johns Hopkins University; Google DeepMind; Google  
🔗 https://arxiv.org/abs/2605.12419  

你在微調大型模型時，有否監控權重漂移？歡迎在留言區分享你的經驗或對此方法的看法 👇  

#AI #LargeLanguageModel #GenRetrieval #ContinualLearning #ModelSoup #JHU #GoogleDeepMind #MachineLearning #NLP #檢索增強 #ORBIT
