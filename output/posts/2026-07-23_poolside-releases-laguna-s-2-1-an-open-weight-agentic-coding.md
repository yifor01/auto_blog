---
title: Poolside Releases Laguna S 2.1, an Open-Weight Agentic Coding Model Punching
  Above Its Weight Class on SWE-Bench Multilingual
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/21/poolside-releases-laguna-s-2-1/
model: tencent/hy3:free
generated_at: '2026-07-23T08:17:54.903837'
score: 99
---

這是一篇產業新聞型別的技術報導。

📌 【Poolside 新作】Laguna S 2.1 正式發布：118B MoE 模型在多語言編碼任務中展現強大戰力

TL;DR：Laguna S 2.1 為 118B MoE 模型，在 SWE-Bench Multilingual 取得 78.5% 高分，效能超越數倍規模的大型模型。

隨著 Agentic Coding（代理編碼）需求激增，模型是否能在長程任務中保持穩定成為關鍵。Poolside 推出的 Laguna S 2.1 展現了「以小博大」的技術路徑，在多種編碼基準測試中挑戰頂尖閉源系統。

🧩 **118B MoE 架構：以輕量化的引數運算實現高效能**

Laguna S 2.1 採用 Mixture-of-Experts (MoE) 架構，雖然總引數達 118B，但展現了極高的稀疏性優勢：
- 引數運算：每個 token 僅啟用約 8B 引數（約佔總引數的 6.8%）。
- 記憶體需求：所有 118B 引數均需常駐於記憶體中，但單步運算負擔極低。
- 效能優勢：這種稀疏性讓中型規模的模型能展現出接近大型模型的表現，同時大幅降低部署成本。
- 訓練細節：模型是在 4,096 顆 NVIDIA H200 GPU 上訓練而成，從訓練開始到發布僅花費不到九週。值得注意的是，這是 Poolside 首個在強化學習（Reinforcement Learning）中使用 FP8 精度的模型。

📊 **在 SWE-Bench Multilingual 取得榜首成績**

Laguna S 2.1 在長程編碼任務（Long-horizon coding benchmarks）中表現優異，足以與規模大出數倍的模型抗衡：
- **SWE-Bench Multilingual**：取得 78.5% 的分數，直接位居已公開資料的榜單首位。
- **Terminal-Bench 2.1**：在啟用「思考模式（Thinking mode）」下取得 70.2% 的分數，成為 Poolside 彙整排行榜中，在公開引數規模模型中的第一名。
- **DeepSWE v1.1 資料對比**：Laguna S 2.1 取得 40.4% 的成績，而 DeepSeek-V4-Pro-Max 僅為 9.0%，且後者的主動引數規模約為前者的六倍。

⚠️ **模型規模與限制**

儘管表現亮眼，作者也指出目前仍有進步空間。在 DeepSWE v1.1 等指標上，模型仍有成長餘裕。此外，目前的頂尖閉源模型（如 Claude Fable 5 與 Kimi K3）在多項基準測試中依然保持領先地位。

🛠️ **豐富的量化格式與部署支援**

為了方便開發者使用，Poolside 提供了多種權重版本：
- 支援格式：BF16、FP8、INT4、NVFP4。
- 開源支援：提供官方 GGUF 與 MLX 轉換版本，以及 DFlash draft 模型。
- 部署規模：模型規模足以在單臺 NVIDIA DGX Spark 上執行。

🎯 **實務啟示**

對於需要處理複雜編碼任務的工程師而言，Laguna S 2.1 證明瞭透過 MoE 架構與長達 1M tokens 的上下文視窗（Context Window），中型規模模型也能在高度複雜的編碼任務中，展現出足以媲美超大型模型的能力。

🔗 **來源**
- 標題：Poolside Releases Laguna S 2.1, an Open-Weight Agentic Coding Model Punching Above Its Weight Class on SWE-Bench Multilingual
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/21/poolside-releases-laguna-s-2-1/

#AI #MachineLearning #LLM #Poolside #LagunaS #CodingModel #MoE #OpenWeight #SoftwareEngineering #AgenticCoding
