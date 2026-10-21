---
title: Design Proteins with RFD4-Proteina Using Reward-Guided Inference-Time Search
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/design-proteins-with-rfd4-proteina-using-reward-guided-inference-time-search/
model: claude-code/sonnet
generated_at: '2026-10-21T20:53:55.518318'
score: 104
---

📌 NVIDIA 與華盛頓大學蛋白質設計研究院推出 RFD4-Proteina：用獎勵導向搜尋在天文數字的組合中找答案

TL;DR：開源模型 RFD4-Proteina 同步生成蛋白質序列與全原子結構，並用推理時搜尋把運算集中在最有潛力的候選上。

一個 100 個殘基的蛋白質序列，可能的組合數量超過可觀測宇宙中的原子總數。在這樣的搜尋空間裡找到能開啟新療法的那一個，靠暴力窮舉顯然不可行，關鍵在於知道該往哪裡找。

🤔 **蛋白質設計本質是一個搜尋問題**

一個八殘基的蛋白質序列就有超過 250 億種組合可能,到了 100 個殘基,組合數已經超越可觀測宇宙的原子數量。這讓窮舉搜尋變得不切實際,必須依賴從既有知識中學到的模式來縮小搜尋範圍。RFD4-Proteina 正是 NVIDIA BioNeMo 與華盛頓大學醫學院蛋白質設計研究院（Institute for Protein Design）共同開發的開放模型，利用從自然界學到的規律，在這片巨大的空間中導航。

🧩 **序列與結構共同生成，推理時用獎勵訊號引導搜尋**

RFD4-Proteina 延續 Proteina-Complexa 的「部分潛空間」（partially latent）設計理念，結合明確的 backbone 座標與潛在表示（latent representation）、學習到的序列與原子層級變數。它的 autoencoder decoder 能同步產生序列與全原子結構,因此不再需要像過去那樣，額外交給 ProteinMPNN 之類的模型做 inverse-folding（反向折疊）這一道獨立步驟。

推理時的搜尋迴圈是這個模型投入運算的核心：模型對生成軌跡逐步去噪（denoise）得到結構,對這些設計打分,保留並延伸最有潛力的部分狀態,直到滿足生成條件為止。獎勵訊號可以衡量幾何合理性、分子間交互作用,或是獨立預測模型的信心程度。

📊 **200 個殘基下生成速度快 3.8 倍，峰值記憶體用量大幅下降**

相較前一代 RFD3，RFD4-Proteina 更快也更省記憶體,原因有三：它改用殘基層級（residue-level）的潛在表示而非原子層級，避免記憶體暴增；擴散過程的工程最佳化把取樣步數從 Proteina-Complexa 的約 400 步降到 60 步；推理時搜尋所用的 oracle（如 OF3 與 tmol 等物理方法）皆為 CUDA 加速，搜尋本身也更快。根據官方公布的生成基準測試，在 200 個殘基的設計任務下，RFD4-Proteina 的生成速度是 RFD3 的 3.8 倍，且大幅降低峰值保留記憶體用量。模型與底層 kernel 由 cuEquivariance 與 BioNeMo Inference Runtime（BIR）團隊共同設計以兼顧速度與可擴展性。

🧪 **從設計目標到候選結構：一次 PD-L1 結合蛋白設計示範**

官方教學示範了以腫瘤標靶 PD-L1 為例設計結合蛋白候選物的流程。使用者先透過 AtomWorks（分子資料前處理層）定義哪些原子固定不變、哪些殘基可設計、以及要瞄準的 hotspot。範例中以 PDB 5O45 的裁切結構作為標靶，固定其序列與 backbone 座標、允許側鏈重新排列,並將結合蛋白生成導向 Tyr56、Met115、Tyr123 這幾個 hotspot 原子，新設計的結合蛋白長度在 100 到 150 個殘基之間,序列與座標皆為自由生成。

使用上，RFD4-Proteina 提供兩種路徑：開放模型（透過 Hugging Face 載入 nvidia/RFD4-Proteina 權重，搭配 Python 3.12 與支援的 NVIDIA GPU，可完全掌控取樣程式碼）,或是 NIM 微服務（提供 HTTP 介面,適合快速部署推理,也可透過 build.nvidia.com 的 API 端點呼叫，不需本機 GPU，但官方不建議用於生產環境）。

🎯 **實務啟示**

對計算生物學家、ML 工程師與藥物開發研究者而言，RFD4-Proteina 把「設計、計算評估、實驗驗證」串成一個可反覆迭代的循環，agent 可以協調這些工具並追蹤結果，科學家則專注在定義目標與依據實驗證據引導下一輪設計。對於需要同時控制序列與結構、且在意推理成本的團隊,這類推理時搜尋的設計會是值得評估的方向。

🔗 **來源**
- 標題：Design Proteins with RFD4-Proteina Using Reward-Guided Inference-Time Search
- 作者／機構：Elizabeth Goodman，NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/design-proteins-with-rfd4-proteina-using-reward-guided-inference-time-search/

#ProteinDesign #NVIDIA #BioNeMo #DrugDiscovery #GenerativeAI #DiffusionModels #ComputationalBiology #OpenModel #AIforScience #MachineLearning
