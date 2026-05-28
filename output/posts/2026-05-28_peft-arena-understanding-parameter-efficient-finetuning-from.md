---
title: "PEFT-Arena: Understanding Parameter-Efficient Finetuning from a Stability-Plasticity Perspective"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.28819
score: 88
model: tencent/hy3-preview:free
generated_at: 2026-05-28T21:37:59.857628
---

【PEFT-Arena】穩塑性視角下的參數效率微調  

你以為參數越少就越安全？  
隨著適應能力的提升，模型原先學到的知識也可能被稀釋。  
這篇研究從「穩塑性」視角，揭示哪種方法能在兩者間取得最佳平衡。  

🤔 **穩塑性衝突：為何參數效率微調不是雙贏？**  
大型語言模型在預訓練階段積累了廣泛的通用知識（穩定性），而在下游任務上需要快速學習新行為（可塑性）。參數效率微調旨在用極少的額外參數達成適應，但若更新方式與原始權重干擾過大，就會導致舊知識遺忘；反之，若過於保守，則新任務表現受限。這正是穩塑性 trade‑off 的核心。  

🧪 **在相同參數預算下的比較實驗**  
研究團隊將多種 PEFT 方法（包括 LoRA、Adapter、Prefix‑Tuning 等）置於相同的可訓練參數預算中，分別測量它們在保留預訓練能力（穩定性）與適應新任務（可塑性）上的表現。這種設計讓比較聚焦於更新方式本身，而非參數數量的差異。  

📌 **正交微調在穩塑性上表現最佳**  
在相等參數條件下，正交 fine‑tuning（orthogonal fine‑tuning）展現出最穩定的穩塑性平衡：它既能保留較多的預訓練知識，又不犧牲對新任務的適應能力。相比之下，其他方法要麼在可塑性上更強但穩定性較低，要麼則相反。  

💡 **穩塑性視角下的設計啟示**  
正交更新的核心是使新增的權重變化與原始權重在向量空間中保持正交，從而在參數更新時減少對既有知識的干擾。這種幾何約束自然地降低了灾难性遺忘的風險，同時仍提供足夠的自由度來學習新模式。對工程師而言，這意味著在選擇 PEFT 時，除了參數預算外，還應考慮更新方向的正交性是否被納入設計。  

⚠️ **實驗僅靠相同參數預算，未涉及實際成本與推論延遲**  
分析前提是所有方法擁有相同數量的可訓練參數，但沒有深入探討實際部署時的記憶體佔離、推論延遲或優化器開銷。因此，正交微調在理論上最佳的穩塑性表現，是否在所有硬體與延遲限制下仍保持優勢，仍需進一步驗證。  

🎯 **選擇 PEFT 時，先看穩塑性需求再比較參數效率**  
- 明確任務對預訓練知識保存的容忍度（穩定性需求）。  
- 在符合該穩定性需求的方法中，比較參數效率與正交性等設計特徵。  
- 若資源允許，可優先考慮正交 fine‑tuning 或同類導向的更新規則，以獲得更可靠的穩塑性平衡。  

🔗 **論文連結**  
📝 PEFT-Arena: Understanding Parameter-Efficient Finetuning from a Stability-Plasticity Perspective  
👤 作者：未註明機構（來源：HuggingFace Daily Papers）  
🔗 https://huggingface.co/papers/2605.28819  

你在選 PEFT 時，會更看重保留舊知識還是快速學習新技能？歡迎在留言區分享你的經驗與考量 👇  

#PEFT #ParameterEfficientFinetuning #StabilityPlasticity #LLM #AIEngineering #HuggingFace #MachineLearning #GenAI
