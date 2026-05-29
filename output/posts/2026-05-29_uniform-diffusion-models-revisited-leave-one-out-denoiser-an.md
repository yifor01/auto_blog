---
title: "Uniform Diffusion Models Revisited: Leave-One-Out Denoiser and Absorbing State Reformulation"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.22765
score: 97
model: tencent/hy3-preview:free
generated_at: 2026-05-29T21:12:22.068598
---

📌 **Uniform Diffusion Models Revisited：Leave-One-Out 去噪器與吸收態重新表述**  

🎣 **你以為均勻擴散模型（UDM）已經發揮極限？最新研究指出，其一個關鍵的訓練目標與實際去噪後驗之間存在不匹配，導致生成品質受限。**  

🤔 **離散擴散模型的訓練方式與預測用途不完全對齊**  
論文指出，離散擴散模型多以乾淨資料預測來訓練，但這個預測可以用不同方式定義逆向動態。在 Masked Diffusion Models（MDM）中，這兩種選擇基本重疊；而在 Uniform Diffusion Models（UDM）中，它們卻分離。這種分離造成標準 plug‑in bridge 參數化並未被去噪後驗優化，而是被一種「leave‑one‑out」後驗優化——也就是在預測每個乾淨 token 時，不使用其自身的噪聲觀測。  

🧪 **理論分析與參數化重新設計**  
研究團隊首先刻畫了這個 leave‑one‑out 目標，並推導出去噪器、leave‑one‑out 後驗與得分之間的精確轉換關係。這些轉換使參數化與訓練目標得以解耦。基於此，他們提出了一種無需額外訓練的「知情預測‑校正」採樣器，並以 leave‑one‑out 預測為基礎改進了取樣溫度。此外，他們進一步提出一種吸收態重新表述的 UDM：在保持 UDM 聯合律的同時，將其分解為類似 MDM 的採樣操作，帶來更簡單的去噪後驗、遮罩延續機制與自然的重新遮罩過程。  

📈 **在語言建模上的實證提升**  
在語言建模任務中，採用 leave‑one‑out 參數化的一致提升了 UDM 的生成品質；而吸收態結構的表現則匹配甚至超越了傳統的 Masked Diffusion。這些結果顯示，UDM 與 MDM 之間的經驗差距更多源於參數化與採樣設計，而非邊際分布的選擇本身。  

⚠️ **摘要中未提供的實驗細節**  
提供的摘要未說明使用的資料集大小、訓練時長或具備的消融實驗，因此無法從此處判斷模型在特定基準上的絕對分數或泛化情況。  

🎯 **對研究與工程的啟示**  
- 透過留出自身觀測的 leave‑one‑out 去噪器，可以修正傳統 UDM 訓練目標與推理目標之間的不匹配。  
- 吸收態重新表述讓 UDM 能以較簡單的操作流程進行採樣，同時保留原始分布特性。  
- 所提出的預測‑校正採樣器與溫度調整無需額外訓練，即可直接帶來生成品質的提升。  
- 程式碼與模型已於 https://github.com/samsongourevitch/rev_udm 公開，方便後續實驗與應用。  

🔗 **論文連結**  
📝 Uniform Diffusion Models Revisited: Leave-One-Out Denoiser and Absorbing State Reformulation  
👤 作者：未在提供的資訊中列出  
🔗 論文：https://huggingface.co/papers/2605.22765  
💻 程式碼：https://github.com/samsongourevitch/rev_udm  

你在使用擴散模型時，是否也曾疑惑訓練目標與實際生成品質之間的落差？歡迎在留言區分享你的經驗與看法 👇  

#UniformDiffusion #LeaveOneOut #AbsorbingState #DiffusionModels #LanguageModeling #AIResearch #HuggingFace #MachineLearning #生成模型 #UDM #MDM #採樣改進 #開源程式碼
