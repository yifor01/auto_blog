---
title: "RayDer: Scalable Self-Supervised Novel View Synthesis from Real-World Video"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.31535
score: 90
model: tencent/hy3-preview:free
generated_at: 2026-06-01T22:25:57.208044
---

📌 **RayDer：統一 Feed‑Forward Transformer 讓真實世界影片也能自監督 Novel View Synthesis**

你以為要得到高品質的新視角合成，必須先知道相機姿勢、建立詳細的幾何模型？RayDer 說「不需要」——它把姿勢估計、場景重建和渲染統一在一個前饋 Transformer 裡，透過動態狀態吸收機制讓模型在真實世界影片上也能穩定訓練，並展現乾淨的擴展行為。

🤔 **真實世界影片訓練的穩定性是 NVS 的 bottleneck**

現有的自監督 Novel View Synthesis 方法多依賴於已知的相機軌跡或合成資料，才能避免姿勢估計誤差導致的訓練發散。當資料來自真實世界的未標註影片時，姿勢與幾何的耦合會讓梯度不穩定，模型難以收斂。這限制了該技術在 AR/VR、機器人與內容創作中的直接應用。

🧪 **一個前饋 Transformer 同時處理姿勢、重建與渲染**

RayDer 的核心設計是將相機姿勢估計、場景幾何重建與視圖渲染三個任務合併為單一的前饋 Transformer 架構。透過「動態狀態吸收」機制，模型在每個前饋步驟中能自適應地吸收與補償姿勢估計的不確定性，從而在未標註的真實世界影片上維持訓練的穩定性。該設計避免了需要迭代優化或外部姿勢估計器的複雜流程。

💡 **乾淨的擴展行為暗示模型可隨資源增長而提升**

實驗表明，當增加模型寬度或深度時，RayDer 的效果隨著資源增加呈現可預測的提升曲線——也就是所謂的「乾淨擴展行為」。這意味著在給予更多計算資源時，我們可以期待系統在新視角合成品質上有線性或近乎線性的改善，為後續規模化應用提供了明確的方向。

⚠️ **未提供開放原始碼與詳細基準，實務落地仍需觀察**

雖然論文描述了創新的架構與穩定訓練策略，但目前尚未公開原始程式碼或詳細的基準測試結果。這使得無法直接驗證其在大規模真實世界資料集上的表現，也難以評估其在不同硬體平台上的推論效能。實務採用的門檻因此仍取決於後續開源與複現工作的進度。

🎯 **對工程師的啟示：統一端到端設計可降低自監督 NVS 的複雜度**

- 若你正在構建需要新視角合成的系統（例如即時 AR 過濾器或機器人視覺），可以考慮將姿勢估計與場景理解納入同一個端到端網路，以減少誤差傳播。  
- 動態狀態吸收的概念提供了一種在訓練階段處理姿勢不確定性的思路，或許可遷移到其他需要同時估計姿勢與形狀的任務。  
- 在等待開放原始碼前，可先嘗試用現有的前饋 Transformer 基礎（如 ViT 或 Swin）搭配簡易的狀態吸收層，作為探索驗證的起點。

🔗 **論文連結**  
📝 RayDer: Scalable Self-Supervised Novel View Synthesis from Real-World Video  
👤 作者：未在摘要中詳列（請參閱原文）  
🔗 https://huggingface.co/papers/2605.31535  

你認為這種「一體化」的姿勢‑重建‑渲染設計，在你的專案中有什麼潛在用途？歡迎留言討論 👇

#RayDer #NovelViewSynthesis #Transformer #SelfSupervised #ARVR #Robotics #HuggingFacePapers #AIResearch
