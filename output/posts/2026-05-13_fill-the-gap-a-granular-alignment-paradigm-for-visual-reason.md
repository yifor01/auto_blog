---
title: "Fill the GAP: A Granular Alignment Paradigm for Visual Reasoning in Multimodal Large Language Models"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.12374
score: 115
model: tencent/hy3-preview:free
generated_at: 2026-05-13T20:30:54.945486
---

📌 【University of Waterloo 最新研究】GAP：細粒度對齊提升多模態推理  

你以為在 MLLM 中直接回饋潛在視覺特徵就能提升推理？研究發現，特徵空間不匹配可能讓這種做法變得不可靠。  

🤔 **視覺潛在推理的隱藏瓶頸：特徵空間不匹配導致不穩定提升**  
現有的視覺潛在 reasoning 方法多半採用「output‑as‑input」範式，將解碼器的隱藏狀態直接當作潛在視覺輸入。然而，這些狀態所處的 norm 與模型在訓練時期望的輸入嵌入有顯著差異，造成特徵空間不匹配，進而導致潛在反饋的穩定性下降。  

🧪 **在 Qwen2.5‑VL 7B 上實施三層對齊範式 GAP 的實驗設計**  
作者提出 GAP（Granular Alignment Paradigm），在三個層面進行對齊：  
- **特徵層對齊**：透過一個輕量的 PCA‑aligned latent head，將解碼器輸出映射至與輸入嵌入相容的視覺潛在空間。  
- **情境層對齊**：引入可檢查的輔助視覺監督，使潛在目標具有可觀測的視覺依據。  
- **容量導向對齊**：僅在基礎 MLLM 在該樣本上表現不佳時才提供潛在監督，以有效利用模型容量。  
實驗以 Qwen2.5‑VL 7B 為基礎模型，驗證上述三層對齊的效果。  

🔬 **核心發現：GAP 讓監督變體在感知與推理上的平均表現達到最佳**  
在監督變體中，採用 GAP 的模型在平均感知與推理性能上表現最佳。進一步的推理時介入探測表明，生成的潛在特徵不僅僅增加了 token 長度，而是提供了與任務相關的視覺訊號。  

💡 **深入分析：三層對齊如何解決特徵‑空間不匹配並提供任務相關視覺訊號**  
特徵層的 PCA‑aligned latent head 直接將解碼器隱藏狀態投射到與輸入嵌入相容的子空間，消除 norm 差異；情境層的輔助視覺監督為潛在目標提供可驗證的視覺錨點；容量導向則避免在模型已能處理的樣本上進行不必要的監督，聚焦於模型真正薄弱的區域。這三層設計共同使潛在反饋變得更穩定且具備任務相關資訊。  

⚠️ **研究限制：僅在單一模型規模上驗證，長期泛化與更大規模適用性尚待探究**  
本研究僅在 Qwen2.5‑VL 7B 上進行驗證，未涉及更大或更小模型的表現；此外，僅評估了短期的感知與推理任務，長期學習效果及在更廣泛多模基準上的適用性仍需後續工作檢驗。  

🎯 **實務啟示：輕量 PCA 對齊頭可作為插件式模組，選擇性監督減少計算開銷**  
對於工程師而言，GAP 提供了一個可插拔的輕量模組（PCA‑aligned latent head），可在不重訓練整個 MLLM 的情況下提升視覺潛在 reasoning 的穩定性。選擇性監督機制則有助於在資源受限的部署情境下，將計算開銷聚焦於最需要改進的樣本上。  

🔗 **論文連結**  
📝 Fill the GAP: A Granular Alignment Paradigm for Visual Reasoning in Multimodal Large Language Models  
👤 Yanting Miao, Yutao Sun, Dexin Wang, Mengyu Zhou, Pascal Poupart (University of Waterloo; Zhejiang University; Qwen Large Model Application Team, Alibaba; Vector Institute)  
🔗 https://arxiv.org/abs/2605.12374  

你的多模態系統是否也面臨特徵空間不匹配的挑戰？歡迎在留言區分享你的看法與經驗 👇  

#AI #MultimodalLLM #VisualReasoning #GAP #Qwen #ComputerVision #MachineLearning #UniversityOfWaterloo #Alibaba #VectorInstitute
