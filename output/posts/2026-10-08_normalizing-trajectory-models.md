---
title: Normalizing Trajectory Models
source: Apple ML
url: https://machinelearning.apple.com/research/normalizing-trajectory-models
model: claude-code/sonnet
generated_at: '2026-10-08T22:18:08.593651'
score: 98
---

📌 【Apple ML @ NeurIPS】用「正規化流」重寫擴散軌跡，四步生成也能保留精確似然

TL;DR：NTM 把擴散模型每一步換成可逆 normalizing flow，四步生圖還能算精確機率。

擴散模型（diffusion model）能生成極高品質的圖片，代價是要跑很多次小幅度的去噪（denoising）步驟。當步驟數被壓縮到只剩幾步時，現有加速方法大多得靠蒸餾（distillation）、一致性訓練（consistency training）或對抗式目標（adversarial objective），但這些方法都得放棄擴散模型最珍貴的特性：精確的似然（likelihood）計算。Apple 機器學習團隊發表於 NeurIPS 的新論文，提出 Normalizing Trajectory Models（NTM），試圖在「少步生成」與「精確似然」之間兩者兼得。

🤔 **擴散模型的假設，在少步時會失效**

擴散模型的理論基礎，是把生成過程拆成許多個高斯去噪步驟，每一步都很小、很接近線性。但當生成被壓縮成少數幾個「粗粒度」的轉移步驟時，這個假設就不再成立，原本依賴小步近似所建立的似然框架也隨之瓦解。

🧩 **每一步換成一個條件式 normalizing flow**

NTM 的做法，是把擴散的每個反向步驟（reverse step）都改建模成一個具表達力的條件式 normalizing flow，並維持精確的似然訓練。架構上，NTM 結合兩個層次：每一步內部用淺層的可逆區塊（invertible block），整條軌跡（trajectory）上則疊加一個深層的平行預測器（parallel predictor），兩者組成一個可端到端（end-to-end）訓練的網路。這個網路可以從零開始訓練，也可以用預訓練好的 flow-matching 模型來初始化。

由於整條軌跡的似然是精確可算的，NTM 因此支援一種自我蒸餾（self-distillation）機制：用模型自身誘導出的 score function 訓練一個輕量化的去噪器（denoiser），就能在四步之內產生高品質的生成結果。

📊 **文字生圖任務上，四步打平甚至超越強力基準**

論文指出，在文字生圖（text-to-image）的基準測試上，NTM 僅用四個取樣步驟，就能打平或超越強力的圖像生成基準模型，而且是在所有基準方法都放棄的「精確似然」這一點上獨家保留下來。論文摘要並未提供具體的基準名稱或數值分數，僅陳述上述結論。

⚠️ **摘要未揭露的部分**

目前公開的素材僅為論文摘要，並未附上實驗章節的具體資料集名稱、訓練成本或消融實驗（ablation）細節，這些留待完整論文公開後再確認。

🎯 **對從事生成模型工程的啟示**

如果你的應用場景同時需要「快速取樣」與「可計算似然」（例如需要用似然做異常偵測、資料評分或不確定性估計的場景），NTM 提出的「每步可逆 flow 加跨步驟平行預測器」架構，是值得關注的設計方向，尤其是它宣稱可以直接從現成的 flow-matching 預訓練模型初始化，降低了重新訓練的門檻。

🔗 **來源**
- 標題：Normalizing Trajectory Models
- 作者／機構：Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind（Apple Machine Learning）
- 連結：https://machinelearning.apple.com/research/normalizing-trajectory-models

#AppleML #NeurIPS #NormalizingFlow #DiffusionModel #GenerativeAI #TextToImage #LikelihoodModel #ComputerVision #FlowMatching #DeepLearning
