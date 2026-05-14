---
title: "Respecting Self-Uncertainty in On-Policy Self-Distillation for Efficient LLM Reasoning"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.13255
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:51:11.628759
---

📌 **EGRSD Approach**  

當大型語言模型自己教自己時，不是所有 token 都同等重要。  
高不確定性的位置如果被平均加權，可能會拉低推理品質。  
這篇論文提出以熵為導向的門控，自適應調整每個 token 的監督強度。  

🤔 **均等加權忽略了教師模型的不確定性變化**  
在 on-policy self-distillation 中，學生模型會從自己的 rollout 中學習，而教師模型（通常是同一模型但在 privileged context 下）提供 token 級別的監督。現有目標函式往往對鏈式思考序列中的每個 token 給予相同權重，卻沒有考慮教師預測分布的 entropy 差異。高 entropy 表示教師對該位置的確信度低，盲目平均加權可能引入噪訊號。  

🧪 **以 Qwen3-4B/8B 為基礎的 on-policy 實驗**  
研究團隊採用 Qwen3-4B 與 Qwen3-8B 的思考模式進行實驗。學生模型在自生成的推理軌跡上進行訓練，教師則是在 privileged context 下給予密集的 token 級別監督。針對現有目標函式，他們提出了 EGRSD（Entropy-Guided Reinforced Self-Distillation），並進一步設計了 CL‑EGRSD（causal-lookahead variant）。  

💡 **EGRSD 與 CL‑EGRSD 提升了準確度與長度的權衡**  
EGRSD 將 token 級別的更新統一為三個訊號：基於 reward 的方向、教師‑學生 likelihood-ratio 的大小，以及新提出的教師 entropy confidence gate。該門控會降低高 entropy token 的權重，但對每個 token 保留非零下界，避免完全忽略任何位置。CL‑EGRSD 在此基礎上加入因果前瞻機制，能區分短暫的高 entropy 與後續語境快速變低 entropy 的持續高 entropy 區段。實驗結果顯示，這兩種方法在訓練可行的基線中，將準確度與生成長度的 trade-off 向前推進。  

🔍 **熵門控如何抑制高不確定性位置的過度影響**  
教師的 entropy 作為不確定度的代理，使得模型在學習時能自動降低對不確定 token 的依賴。因為每個 token 仍保有最小權重，學生不會完全喪失對該位置的資訊，而是在保持學習穩定性的同時，減少噪訊號對最終推理品質的衝擊。CL‑EGRSD 的 causal-lookahead 進一步辨識哪些高 entropy 是暫時波動（後文很快變得確定），哪些是真正需要更謹慎處理的持續不確定區域，從而在序列層級上獲得更精細的權重分配。  

⚠️ **僅在特定思考模式下驗證，泛化能力尚待觀察**  
實驗僅針對 Qwen3 系列的思考模式進行，未涵蓋其他推理風格或不同架構的模型。此外，論文未探討訓練成本的具體變化或在更長序列、更複雜任務上的表現，這些都是未來工作可以補充的方向。  

🎯 **在訓練推理模型時，可考慮加入教師熵作為動態權重**  
對於希望透過 self-distillation 提升推理效率的工程師與研究者，這項結果暗示：單靠均等監督可能無法充分利用教師的知識；引入基於 entropy 的門控或因果前瞻機制，能在不犧牲收斂穩定性的前提下，提升模型在長鏈思考上的表現。實作上，可先計算教師每個 token 的預測 entropy，然後依門控函式調整 loss 權重，亦可參考 CL‑EGRSD 的前瞻窗口設計。  

🔗 **論文連結**  
📝 Respecting Self-Uncertainty in On-Policy Self-Distillation for Efficient LLM Reasoning  
👤 Junlong Ke, Zichen Wen, Weijia Li, Conghui He, Linfeng Zhang (Shanghai Jiao Tong University; Tsinghua University; Shanghai AI Laboratory)  
🔗 https://arxiv.org/abs/2605.13255  

#LLM #SelfDistillation #EntropyGuided #Reasoning #Qwen3 #MachineLearning #AIResearch #ShanghaiJiaoTong #Tsinghua #ShanghaiAILab
