---
title: 'GEM Training: How Meta Doubled the Efficiency of Its LLM-Scale Ads Foundation
  Model'
source: Meta AI Research
url: https://engineering.fb.com/2026/08/03/ml-applications/training-gem-at-llm-scale-meta-ads-recommendation-foundation-model/
model: tencent/hy3:free
generated_at: '2026-08-04T08:38:13.588098'
score: 85
---

📌 【Meta AI 研究】訓練效率翻倍：揭秘 Meta 廣告推薦基礎模型 GEM 的大規模訓練技術

TL;DR：透過自研 JFA 與 GDPA Kernel，Meta 將廣告推薦模型 GEM 的訓練吞吐量提升了 30% 以上。

在廣告推薦系統中，處理數兆級別的稀疏嵌入（sparse embedding）與數十億級別的密集參數（dense parameters）是一項極大的挑戰。Meta 推出的 GEM 是其廣告系統的核心推薦基礎模型，採用混合架構來處理序列特徵（如使用者活動歷史）與非序列特徵（如使用者位置）。然而，現有的 GPU 軟體棧多針對 LLM 任務優化，面對推薦系統中「長度不一（jagged）的序列」與「複雜的特徵交互」，難以達成高 GPU 運算利用率。

🧩 **將訓練效率拆解為兩個核心維度**

Meta 發現，單純增加 GPU 數量並不能帶來成比例的加速。為了提升效能，他們將端到端（E2E）的 MFU（Model Flops Utilization）拆解為兩個獨立的優化問題：

*   **Local MFU (運算效率)**：衡量單顆 GPU 的運算單元利用率，取決於 Kernel 設計、數值精度以及工作負載與 GPU 架構（如 Tensor cores）的匹配程度。
*   **Scaling Ratio (擴展效率)**：衡量將模型分散至數千顆 GPU 進行訓練時，能保留多少單卡效能。這會受到通訊開銷、負載不平衡與記憶體壓力導致的重算（recomputation）影響。

📊 **針對推薦系統特性開發的自研 Kernel**

為了突破現有 FlashAttention 在處理推薦任務時的限制，Meta 研發了多種專用技術：

*   **JFA (Jagged FlashAttention)**：
    傳統 FlashAttention 針對 LLM 的固定長度序列設計，但在推薦系統中，使用者序列長度差異極大（從數百到數萬個 token 不等）。若進行補齊（padding）會浪弱 50% 的運算量。JFA 直接作用於變長（variable-length）的 jagged tensors，消除了 padding 開銷。其最新版本 JFA v4 在性能上較 v2 提升了 40-140%，並帶來 18.5% 的 Local MFU 增益。
*   **GDPA Kernel**：
    GEM 使用多種類似 Attention 的交互模式（如 self-attention、PMA、cross-attention），但會將 softmax 替換為 GELU 或 SiLU 等激活函數。Meta 開發了 GDPA Kernel 來統一這些模組，在處理短 K/V 序列的生產環境中，其前向傳播速度比 Flash Attention 4 快上 3.5 倍。
*   **TLX Block Attention**：
    針對 Self-attention 的長序列問題，Meta 結合了滑動窗口（Sliding Window Attention）與 Block-aligned attention 技術。透過將 Attention 轉換為獨立的 64x64 問題，並將 RoPE 反向傳播融合進 Attention epilogue，使 Self-attention 層的 MFU 比 Triton 的 Block Attention 提升了 30.6%。

💡 **利用低精度訓練實現效能躍升**

在最新的 GPU 硬體上，使用 FP8 精度可獲得 2 倍於 FP16 的峰值 TFLOPS，而 FP4 則可達 4 倍。為了在不損失模型品質（避免數值不穩定與量化開銷）的前提下利用此特性，Meta 開發了具備數值穩定增強功能的 MXFP8 Attention 與 MLP，並擴展了 FA4 kernel 以支援端到端的 MXFP8 block-scaled MMA。

🎯 **實務啟示**

對於處理大規模推薦系統的工程師而言，GEM 的經驗指出：針對特定資料分佈（如 Jagged sequences）開發專用 Kernel，以及利用低精度（Low-precision）訓練來逼近硬體理論極限，是提升大規模基礎模型訓練效率的關鍵路徑。

🔗 **來源**
- 標題：GEM Training: How Meta Doubled the Efficiency of Its LLM-Scale Ads Foundation Model
- 連結：https://engineering.fb.com/2026/08/03/ml-applications/training-gem-at-llm-scale-meta-ads-recommendation-foundation-model/

#MetaAI #MachineLearning #LLM #RecommendationSystem #GPU #DeepLearning #TrainingEfficiency #FlashAttention #ComputerVision #AIInfrastructure
