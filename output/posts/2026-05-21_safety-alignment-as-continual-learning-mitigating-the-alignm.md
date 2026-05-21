---
title: "Safety Alignment as Continual Learning: Mitigating the Alignment Tax via Orthogonal Gradient Projection"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2602.07892
score: 98
model: tencent/hy3-preview:free
generated_at: 2026-05-21T21:12:59.344081
---

📌 【HuggingFace Daily Papers】OGPSA：用正交梯度投影緩解對齊稅  

你是否曾注意到，讓大型語言模型更安全，常常伴隨著能力的下降？這篇論文提出了一種方法，試圖在不犧牲通用能力的前提下提升安全性。  

🤔 **安全與通用能力的權衡亟需新思路**  
隨著 LLM 安全對齊（Safety Alignment）成為標準流程，研究者發現頻繁的安全微調會導致模型在一般任務上的表現下降——這被稱為「對齊稅」（Alignment Tax）。如何在提升安全性的同時保留原有能力，成為當前對齊研究的核心挑戰。  

🧪 **OGPSA：將安全梯度投影至通用能力子空間的正交方向**  
論文提出 Orthogonal Gradient Projection for Safety Alignment (OGPSA)。其核心思路是把安全訓練時的梯度投射到模型通用能力子空間的正交補空間，從而在更新參數時盡量不影響已學會的通用知識。由於採用低秩投影，實作上只需顯式維護一個低維基底，計算開銷相對較低。  

💡 **原理：正交投影如何緩解對齊稅**  
當安全梯度與通用能力子空間正交時，參數更新的分量將不會投射到通用能力方向，理論上能夠減少安全微調對現有能力的干擾。這種「梯度正規化」的做法將連續學習（Continual Learning）的概念引入對齊領域，提供了一種可原則性地分離安全與通用目標的途徑。  

⚠️ **目前資訊僅涵蓋方法概念，實驗驗證細節尚未在摘要中說明**  
摘要與評分理由著重於方法的提出與其理論優勢，未具體說明資料集、基線模型或消融實驗。因此，讀者在評估其实際效益時，仍需參考全文中的實驗章份或後續社群驗證。  

🎯 **對實務工作者的啟示**  
- 若你正在進行多輪安全微調，可考慮將安全梯度投射到通用子空間的正交補空間，以嘗試降低對齊稅。  
- 低秩投影的實作方式（例如使用 SVD 或隨機投影）使得該技術可直接嵌入現有的訓練管線，對資源需求較為友好。  
- 這一方法與其他緩解 catastrophic forgetting 的技術（如投影式正則化、記憶重播）有概念上的相似性，可視為對齊任務的專門變體。  

🔗 **論文連結**  
📝 Safety Alignment as Continual Learning: Mitigating the Alignment Tax via Orthogonal Gradient Projection  
👤 作者／機構：未在提供的摘要中註明  
🔗 https://huggingface.co/papers/2602.07892  

你有在實際專案中嘗試過類似的梯度投影技巧嗎？歡迎在留言區分享經驗或疑問 👇  

#AI #LLM #SafetyAlignment #ContinualLearning #GradientProjection #HuggingFace #MachineLearning #對齊稅 #OGPSA
