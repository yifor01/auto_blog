---
title: "LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.18739
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:34:44.375248
---

📌 【NVIDIA】LongLive-2.0：長影片生成的 NVFP4 加速架構  

你以為長影片 AI 生成只靠堆砌算力就能變快？實際上，記憶體與計算瓶頸才是真正的限制。  

🤔 **長影片生成訓練與推理的記憶體與算力瓶頸**  
隨著影片長度增加，傳統擴散模型在訓練階段需要儲存巨大的激活與中間特徵，導致 GPU 記憶體爆炸；推理時則受限於 KV cache 大小與逐步去噪的迭代次數，吞吐量難以提升。這些瓶頸直接制約了長影片生成的實用性與成本效益。  

🧪 **以 NVFP4 為基礎的序列並行自回歸訓練架構**  
論文提出 Balanced SP（序列並行）訓練方式，將乾淨歷史與噪聲目標的時間塊配對於每個 rank 上，從而在 SP 執行中自然產生 teacher‑forcing mask。配合 NVFP4 4‑bit 精度，既降低了 GEMM 運算的記憶體佔用，又提升了矩陣乘法的吞吐量；隨著影片長度增長，這項優勢會變得更明顯。此外，高品質的基礎設施與資料集使得訓練管線乾淨穩定，無需額外的 ODE 初始化或後續的分布匹配蒸餾（DMD）。  

🚀 **直接調整擴散模型為多槽互動自回歸模型，並支援即時生成**  
與現有 Self‑Forcing 系列不同，LongLive-2.0 直接把擴散模型調整為長影片、多槽、互動的自回歸（AR）擴散模型。經過調整後，可獨立使用 LoRA 權重將去噪步驟壓縮至 4→2 步，實現近乎即時的生成。在 Blackwell GPU 上，進一步啟用 W4A4 NVFP4 推理、將 KV cache 量化為 NVFP4 以節省記憶體，並採用非同步串流 VAE 解碼提升端到端吞吐量；在非 Blackwell 架構上，則透過序列並行推理匹配 Blackwell 的速度，同時量化 KV cache 減少跨卡通信量。  

📈 **實驗顯示訓練與推理速度顯著提升**  
在長影片生成任務上，Balanced SP + NVFP4 使訓練階段的速度最高可達 2.15× 基線，推理階段最高可達 1.84×。LongLive-2.0-5B 模型在推理時可達 45.7 FPS，同時在多個基準測試上保持強大的生成品質。這代表該架構是目前首個同時支援 NVFP4 精度的訓練與推理系統，專門針對長影片生成場景設計。  

⚠️ **研究限制：尚未開放原始碼，實際部署需自行實作**  
論文未提供程式碼庫，因此直接落地需要團隊自行根據所述方法重現序列並行訓練、NVFP4 量化與非同步 VAE 解碼等細節。此外，實驗主要聚焦在特定長度範圍與特定硬體（Blackwell 與非 Blackwell）上的表現，其他架構或極端長影片的行為尚需進一步驗證。  

🎯 **對工程師的啟示：優先考慮混合精度與序列並行的組合**  
- 在訓練長影片擴散模型時，結合序列並行與 4‑bit NVFP4 可同時緩解記憶體壓力與提升 GEMM 吞吐量。  
- 推理階段可先嘗試 KV cache 量化與非同步 VAE 解碼，以在不換硬體的情況下提升 FPS。  
- 若目標是即時生成，可探索 LoRA 壓縮去噪步驟的可行性，但需權衡品質與速度的 trade‑off。  

🔗 **論文連結**  
📝 LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation  
👤 Yukang Chen, Luozhou Wang, Wei Huang, Shuai Yang, Bohan Zhang @ NVIDIA  
🔗 https://arxiv.org/abs/2605.18739  

你在長影片生成專案中是否已嘗試過序列並行或低精度訓練？歡迎在留言區分享經驗或問題 👇  

#AI #VideoGeneration #NVFP4 #NVIDIA #LongLive2.0 #深度學習 #電腦視覺 #機器學習 #CVPR2026 #技術分享
