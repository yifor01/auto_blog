---
title: "A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.28556
score: 93
model: tencent/hy3-preview:free
generated_at: 2026-06-02T21:58:39.389489
---

📌 【TASTE】讓 Agent 基準測試自己進化：更難、更全面的任務產生法  

你是否覺得目前用來評估 AI Agent 的基準測試太過簡單，無法真正反映複雜工具使用情境？一種全新的自動生成方法正在嘗試讓基準測試「自己」變得更具挑戰性。  

🤔 **現有基準測試的覆蓋度與難度不足**  
當前許多 Agent 基準測試依賴手動設計的任務序列，工具使用的種類和組合往往有限，難以呈現真實世界中可能出現的多樣情境。這使得在基準上表現良好的 Agent，在實際部署時仍可能遇到未見過的工具組合或更高階的推理需求。  

🧪 **TASTE：透過對比 n‑gram 建模與迭代難度提升演化工具序列**  
論文提出 TASTE（Tool‑Use Sequence Evolution via Adaptive Contrastive n‑gram Modeling）框架。其核心 idea 是：  
1. 從一組種子工具序列出發，利用 **自適應對比 n‑gram 建模** 產生新的候選序列，使其在工具使用的統計特徵上與現有基準產生明顯對比。  
2. 透過 **迭代難度 refinement**，不斷提升序列的複雜度（例如增加工具數量、引入條件分支或依賴關係），直至達到預設的難度門檻。  
整個過程是自動化的，且作者指出該方法可使用開源工具實作，適合社群直接採用。  

🚀 **TASTE 能產出工具覆蓋更廣、難度更高的基準測試**  
實驗顯示，透過 TASTE 生成的任務集合在工具種類的多樣性上顯著優於現有手動設計的基準；同時，經過迭代難度提升後，所生成的任務在解決所需的步驟數與推理深度上均有顯著增加。這意味著使用這些基準進行評估時，能更好地區分出真正具備泛化工具使用能力的 Agent。  

💡 **對比 n‑gram 建模是關鍵：讓新序列與既有基準產生明顯區隔**  
自適應對比 n‑gram 模型不僅考慮單一工具的出現頻率，更捕捉連續工具組合的幾gram 分布。透過最大化新序列與現有基準在這些 n‑gram 特徵上的對比，TASTE 能系統地探索尚未被覆蓋的工具組合空間，避免產生重複或過於簡單的任務。  

⚠️ **方法依賴種子序列的多樣性與對比模型的調校**  
TASTE 的效果受到初始種子工具序列多樣性的影響；若種子過於單一，可能限制後續演化的上限。此外，自適應對比 n‑gram 建模的超參數（如對比權重、n‑gram 長度）需要根據目標工具集進行調校，才能獲得理想的難度提升曲線。作者未在摘要中提供大規模人間評估或與既有基準的直接量化比較，故後續工作仍需驗證其在不同 Agent 類型與真實任務中的泛化性。  

🎯 **研究者可直接採用 TASTE 建立更具挑戰性的評估基準**  
- 將 TASTE 作為基準產生管線，快速擴充工具使用的測試庫。  
- 透過調整迭代難度的停止條件，依據所需評估嚴謹度產出對應難度的任務集。  
- 結合開源實作，降低實驗門檻，促進社群在 Agent 評估上的標準化與比較性。  

🔗 **論文連結**  
📝 A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks  
🔗 https://huggingface.co/papers/2605.28556  

你認為自動生成基準測試是否能解決當前 Agent 評估的「太簡單」問題？歡迎在留言區分享你的看法與經驗 👇  

#AI #AgentEvaluation #BenchmarkGeneration #TASTE #HuggingFace #MachineLearning #AIResearch #ToolUse #AutoBenchmarks
