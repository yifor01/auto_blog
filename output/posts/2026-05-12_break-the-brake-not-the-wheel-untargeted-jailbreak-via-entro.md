---
title: "Break the Brake, Not the Wheel: Untargeted Jailbreak via Entropy Maximization"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.10764
score: 109
model: tencent/hy3-preview:free
generated_at: 2026-05-12T20:55:00.046949
---

📌 【ANU 等最新研究】透過熵最大化實現 VLMs 越獄  

你以為越獄必須針對特定模型才能成功？新研究顯示，只需在決策點上最大化熵，就能讓多種視覺語言模型（VLM）失去防禦能力。  

🤔 **越獄的瓶頸在於過度限定的目標**  
先前的梯度 기반 普遍圖像越獄研究發現，跨模型遷移性極低，令多人質疑可遷移的多模態越獄是否可行。作者們指出，這種限制源於過度嚴格的優化目標——強制固定前綴或特定回應模式，導致攻擊難以在不同模型間傳遞。  

🧪 **在無目標威脅模型下測量熵行為**  
團隊先以未設定固定前綴或回應模式的「無目標」威脅情境，觀察三種主流 VLM 在兩個安全基準上的自回歸解碼過程。實驗顯示，模型的拒絕行為集中在高熵 token；而非拒絕 token 在攻擊前已具備較高的機率質量。  

🚀 **UJEM‑KL：輕量化的熵最大化攻擊**  
基於上述發現，他們提出 **Untargeted Jailbreak via Entropy Maximization (UJEM‑KL)**：在決策 token 上最大化 entropy（透過 KL 散度目標），以翻轉拒絕結果；同時對低熵位置進行穩定，以保持輸出品質。該方法被描述為「輕量級」，易於實作，並在三種 VLM 與兩個安全基準上取得具競爭力的白盒攻擊成功率，且在代表性防禦下仍持續有效。  

💡 **為什麼熵最大化能提升遷移性？**  
作者進一步分析指出，傳統越獄常因過度針對特定 token 分佈而導致模型特有的對抗性；而熵最大化則鼓勵模型在決策點上保持不確定性，使攻擊不易被模型特有的梯度結構鎖定，從而提升跨模型的遷移性。  

⚠️ **實驗範圍與長效性尚待驗證**  
論文僅報告了三種 VLM 與兩個安全基準的結果，未涉及更廣泛的模型族群或更長時間的防禦演變。此外，攻擊效果是在白盒設定下評估，黑盒或更複雜的防禦機制尚未探討。  

🎯 **對工程師的啟示**  
- 在評估 VLM 安全時，可將 UJEM‑KL 作為基線攻擊，快速檢視模型對熵最大化的敏感度。  
- 防禦策略應該考慮如何降低決策點的熵或增加低熵位置的穩定性，而非仅依賴於特定前綴檢測。  
- 若需跨模型測試越獄風險，這種輕量化的無目標方法提供了更具普遍性的評估途徑。  

🔗 **論文連結**  
📝 Break the Brake, Not the Wheel: Untargeted Jailbreak via Entropy Maximization  
👤 Mengqi He, Xinyu Tian, Xin Shen, Shu Zou, Jinhong Ni (Australian National University; The University Of Queensland; Peking University; Waymo; CSIRO)  
🔗 https://arxiv.org/abs/2605.10764  

你在使用 VLM 時，是否曾注意到模型在某些 token 上的不確定性？歡迎在留言區分享你的觀察與經驗 👇  

#AI #VisionLanguageModel #Jailbreak #MultimodalSecurity #ANU #CVPR #ModelRobustness
