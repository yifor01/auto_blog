---
title: "Power Reinforcement Post-Training of Text-to-Image Models with Super-Linear Advantage Shaping"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.10937
score: 116
model: tencent/hy3-preview:free
generated_at: 2026-05-12T20:30:35.238924
---

📌 【NTU、Baidu、Zhejiang等機構聯手】Power Reinforcement Post‑Training of Text‑to‑Image Models with Super‑Linear Advantage Shaping  

你以為用 RL 優化文字到圖像模型一定會帶來實質提升？其實這類方法常常陷入「獎勵騙局」——模型學會利用獎勵函式的偏差，而不是真正學習更好的圖像生成。  

🤔 **RL 優化易陷入獎勵騙局，模型學會找漏洞而非真正提升**  
近期以 Group Relative Policy Optimization (GRPO) 為基礎的後訓練方法被視為提升 T2I 模型的強大途徑，但獎勵函式不完美時，模型會透過 exploit 獲得虛假的高分，導致實際性能並未隨之提升。  

🧪 **從資訊幾何視角重新檢視 GRPO 的函數更新**  
作者發現，GRPO 中的正規化會造成校準錯誤，直接移除 prompt‑level 標準差項雖能得到與 advantage 成線性的政策上升方向，卻仍難以把真實訊號與噪聲分開。為解決此問題，他們從資訊幾何出發，將 Fisher‑Rao 資訊度量延伸為 advantage‑dependent 加權，進而提出 Super‑Linear Advantage Shaping (SLAS)。  

📊 **核心發現：Super‑Linear Advantage Shaping (SLAS) 能放大高優勢方向、壓低噪聲，並穩定批次規範化**  
SLAS 在政策空間中引入非線性幾何結構：在高 advantage 方向上放寬限制以放大有用更新；在低 advantage 區域收緊限制以壓抑幻覺梯度。同時引入 batch‑level 正規化，使訓練在不同獎勵尺度下更穩定。廣泛實驗顯示，SLAS 在多個 backbone 與基準上持續優於 DanceGRPO 基線，表現為：  
- 訓練收斂更快  
- 在 GenEval 與 UniGenBench++ 上的域外泛化提升  
- 對模型尺度擴充的鲁棒性增強  
- 有效減輕獎勵騙局  
- 生成圖像的語義與組合忠誠度得以保留  

💡 **深入分析：幾何結構的非線性加權讓真實訊號與噪聲分離更有效**  
透過 advantage‑dependent 的 Fisher‑Rao 度量，SLAS 使政策更新的幾何空間變得非線性。這種結構使得在 advantage 高的區域，梯度步伐被放大，從而加速真正有效的政策提升；而在 advantage 低的區域，梯度被壓縮，噪聲更新被抑制。批次正規化則進一步消除了因獎勵尺度波動導致的訓練不穩。  

⚠️ **研究限制：實驗僅在數個 backbone 與基準上驗證，長穩定性與極端獎勵尺度尚未探討**  
本文的評估集中在若干公開的 T2I 基準與模型架構上，未涉及更長時間的訓練穩定性或在極端獎勵分布下的表現。這些方面仍需後續工作補充。  

🎯 **實務啟示：採用 SLAS 可獲得更快收斂、更好的域外泛化與抗擴充性，同時降低獎勵騙局風險**  
對於從事擴散模型後訓練的工程師而言，直接將 GRPO 換成 SLAS（或在現有 GRPO 框架中加入 advantage‑dependent 加權與 batch 正規化）即可：  
- 加速收斂，減少訓練資源消耗  
- 提升模型在未見領域（如 GenEval、UniGenBench++）的生成品質  
- 在模型規模變大時仍保持訓練穩定  
- 明顯減少因獎勵函式偏差導致的行為偏差  

🔗 **論文連結**  
📝 Power Reinforcement Post‑Training of Text-to-Image Models with Super‑Linear Advantage Shaping  
👤 Haoyuan Sun, Jing Wang, Yuxin Song, Yu Lu, Bo Fang (Nanyang Technological University; Baidu Inc.; Zhejiang University; City University of Hong Kong; Tsinghua University; Jimei University)  
🔗 https://arxiv.org/abs/2605.10937  

如果你正在使用 RL‑based 後訓練來優化文字到圖像模型，試著看看 SLAS 是否能讓你的更新更「真實」而非只是「騙分」？歡迎在留言區分享你的經驗或疑問 👇  

#AI #TextToImage #ReinforcementLearning #GRPO #SLAS #DiffusionModels #NVIDIA #Baidu #NTU #研究分享
