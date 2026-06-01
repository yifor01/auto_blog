---
title: "GDSD: Reinforcement Learning as Guided Denoiser Self-Distillation for Diffusion Language Models"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.29398
score: 100
model: tencent/hy3-preview:free
generated_at: 2026-06-01T22:08:14.553561
---

📌 【GDSD】用強化學習引導去噪自蒸餾，提升擴散語言模型  

你以為擴散模型只能靠ELBO來訓練？研究顯示，直接從自身優勢導師蒸餾去噪器，可能帶來更好的效果。  

🤔 **擴散語言模型的訓練瓶頸**  
目前的擴散大型語言模型（LLM）多依賴ELBO（證據下界）似然作為 surrogate loss 來訓練去噪網路。這種間接目標會引入偏差，使訓練目標與最終生成品質的對齊不夠緊密。雖然強化學習（RL）能直接優化回報，但把RL套用在高維的去噪過程上仍缺乏成熟框架。  

🧪 **以優勢導師進行去噪器自蒸餾**  
GDSD（Guided Denoiser Self‑Distillation）提出一種新訓練範式：  
1. 使用當前模型自行生成軌跡，並以某種回報函式（例如基於任務獎勵的優勢估計）計算每一步的advantage。  
2. 以這些advantage作為引導訊號，將去噪器的學習目標設定為模仿「優勢導師」——即在高advantage步驟下表現更好的去噪器版本。  
3. 透過這種自蒸餾過程，模型直接從自身的優勢行為中學習，繞過ELBO似然 surrogate loss，減少訓練‑推論之間的 mismatch。  

📈 **在基準測試上表現優於既有方法**  
實驗顯示，採用GDSD訓練的擴散語言模型在多個基準任務上均達成比傳統ELBO訓練更好的成績。具體提升幅度與使用的模型大小、任務類型有關，但論文明確指出「優於既有方法」的觀察結果。  

🔍 **優勢導師提供更直接的品質回饋**  
與依賴似然的間接目標不同，advantage訊號能更貼近模型在實際生成時所關注的品質（例如任務特定的獎勵或人類偏好）。因此，去噪器在學習時能更聚焦於提升最終輸出的實用品質，而不只是在似然空間裡尋找局部最優。  

⚠️ **未公開程式碼、實驗規模有待進一步驗證**  
論文目前未明確釋出完整的訓練程式碼，重現實驗需依賴作者後續補充。此外，報告的結果主要集中在特定基準與模型規模上，是否同樣適用於更大規模的擴散LLM或不同的回報設計，尚需更多研究驗證。  

🎯 **為擴散LLM提供新的訓練選項**  
GDSD表明，強化學習不必只停留在政策梯度或PPO等傳統框架；它可以透過自蒸餾的方式成為去噪器的訓練信號。對於希望減少對ELBO偏差依賴、探索更直接品質優化的GenAI工程師與研究者而言，這提供了一個值得嘗試的新方向。  

🔗 **論文連結**  
📝 GDSD: Reinforcement Learning as Guided Denoiser Self-Distillation for Diffusion Language Models  
🔗 https://huggingface.co/papers/2605.29398  

你認為這種「自導師」的蒸餾方式會在未來的擴散模型訓練中扮演什麼角色？歡迎在留言區分享你的看法 👇  

#AI #DiffusionModels #ReinforcementLearning #LLM #GenAI #HuggingFace #MachineLearning
