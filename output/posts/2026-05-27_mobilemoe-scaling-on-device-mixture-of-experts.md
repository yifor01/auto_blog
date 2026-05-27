---
title: "MobileMoE: Scaling On-Device Mixture of Experts"
source: arXiv
url: http://arxiv.org/abs/2605.27358v1
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-27T20:53:12.284476
---

📌 MobileMoE：手機端稀疏專家模型新突破  

你以為手機 AI 只能靠堆參數才能變強？實際上，稀疏專家結構或許讓小模型跑得更快、更準。  

🤔 **手機記憶與運算限制下，傳統密集模型難以發揮 MoE 優勢**  
現有百億參數語言模型普遍採用 Mixture‑of‑Experts (MoE) 架構，但在記憶體和算力受限的手機端，此類模型的潛力尚未被充分探索。作者提出，需要一套專為行動記憶與運算約束設計的 MoE 縮放律，才能在不犧牲效能的前提下獲得更好的效率。  

🧪 **先推導行動 MoE 縮放律，再訓練四階段食譜**  
研究團隊首先推導出一個同時考慮手機記憶體與運算限制的 MoE 縮放律，發現「中等稀疏度、細粒度且共享的專家」是同時最省記憶又最省運算的甜點。基於此結構，他們採用四階段訓練流程：預訓練 → 中期訓練 → 指令微調 → 感知量化訓練，全部在開源資料集上完成。  

🚀 **在 14 個基準上，MobileMoE 與或超越同等規模的密集模型，且運算需求更低**  
實驗顯示，MobileMoE 系列（0.3‑0.9B 有效參數，1.3‑5.3B 總參數）在相同或更少的推論 FLOPs 下，能匹配或領先目前領先的手機端密集 LLMs，相較於最先進的 MoE OLMoE‑1B‑7B，參數數量可減少多達 60%。  

⚡ **首次在商用智慧手機上實現高效 MoE 推論，速度顯著提升**  
為了貼近真實部署，團隊在商用智慧手機上進行了完整的 on-device 分析。在相同的 INT4 權重記憶體下，MobileMoE-S 的前填充階段比密集基準 MobileLLM-Pro 快 1.8‑3.8 倍，解碼階段快 2.2‑3.4 倍。  

⚠️ **樣本與實驗範圍有限，長期效果尚未驗證**  
研究主要聚焦於推論效率與基準表現，未涵蓋長期使用時的模型漂移或熱管理影響，且實驗基於特定硬體平台，推廣至其他機型仍需進一步驗證。  

🎯 **對邊緣 AI 工程師的啟示：稀疏專家可作為手機端模型設計的新選項**  
此工提供了一種在嚴格記憶與運算預算下，透過調整專家數量、粒度與共享度來達到更好準確度‑效率平衡的方法論。開發團隊已公開訓練食譜與推論程式碼，可直接用於後續的手機端 LLM 實驗。  

🔗 **論文連結**  
📝 MobileMoE: Scaling On-Device Mixture of Experts  
👤 Yanbei Chen, Hanxian Huang, Ernie Chang, Jacob Szwejbka, Digant Desai  
🔗 https://arxiv.org/abs/2605.27358v1  

你認為稀疏專家在手機端的潛力有多大？歡迎在留言區分享你的看法 👇  

#AI #MobileLLM #MoE #OnDevice #EdgeAI #GenAI #研究分享
