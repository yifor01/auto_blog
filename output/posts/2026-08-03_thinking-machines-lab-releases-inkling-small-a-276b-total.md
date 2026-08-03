---
title: 'Thinking Machines Lab Releases Inkling-Small: A 276B Total, 12B Active Open
  Weights Multimodal MoE Model'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/02/thinking-machines-lab-releases-inkling-small-276b-open-weights-multimodal-moe-model/
model: tencent/hy3:free
generated_at: '2026-08-03T09:02:06.607332'
score: 111
---

📌 【Thinking Machines Lab】276B 多模態 MoE 模型 Inkling-Small 開源：單顆 GPU 即可驅動的高效能推理

TL;DR：Inkling-Small 是一個 276B 參數的開源多模態 MoE 模型，僅需單顆 B300 即可執行，且在編碼與推理能力上超越了其大型版本 Inkling。

隨著開源模型規模不斷擴張，如何在有限的硬體資源下實現強大的多模態推理能力，一直是工程師面臨的挑戰。Thinking Machines Lab 近期釋出的 Inkling-Small 正是為了打破這個僵局。

🧩 **混合專家架構 (MoE) 與原生多模態設計**

Inkling-Small 採用了 42 層的 decoder-only transformer 架構，並結合了稀疏 MoE (Mixture-of-Experts) 的 feed-forward backbone。其核心設計特點如下：

* **稀疏路由機制**：每層共有 256 個專家，每個 token 會路由至其中的 6 個專家，此外還有 2 個共享專家 (shared experts) 會在每個 token 上保持活躍。
* **原生多模態處理**：該模型無需 encoder，直接對文字、圖像與音訊進行原生處理。
    * **圖像**：將圖像切分為 40×40 像素的 patches，並透過四層 hMLP 進行轉換。
    * **音訊**：以 dMel spectrograms 表示，輸入格式為 16 kHz 的 WAV 檔（建議長度 2 分鐘以內）。
    * **融合方式**：圖像與音訊會透過輕量級 embedding 層，與文字 token 進行聯合處理。
* **可調式思考強度**：模型具備可調整的「思考程度 (thinking effort)」，並支援高達 1M tokens 的上下文視窗 (context window)。

📊 **超越「老師」的推理與編碼效能**

研究團隊在開發過程中，先對 Inkling-Small 的早期版本進行了預訓練，並利用較大的模型 Inkling 進行 on-policy distillation（策略內蒸餾）。有趣的是，這個較小的模型在特定任務上反而超越了它的「老師」：

| 評估基準 (Benchmark) | Inkling-Small 分數 | Inkling (大型版) 分數 |
| :--- | :--- | :--- |
| **Humanity’s Last Exam (Text)** | 31.6% | 29.7% |
| **SWE-bench Verified** | 80.2% | 77.6% |
| **Toolathlon Verified** | 54.4% | 45.5% |
| **ARC-AGI-2** | 40.1% | 36.5% |

而在多模態表現上，Inkling-Small 在 CharXiv RQ 任務中，若結合 Python 進行圖像縮放與檢查，分數可從 77.4% 提升至 81.3%。

⚠️ **硬體需求與部署路徑**

Inkling-Small 的釋出大幅降低了部署大型模型的門檻，尤其是透過量化技術，讓單一 GPU 部署成為可能：

* **BF16 精度**：需要至少 600 GB 累計 VRAM（例如 4x NVIDIA B300 或 8x NVIDIA H200）。
* **NVFP4 量化**：將硬體門檻降至 180 GB。
* **單 GPU 方案**：透過 W4A4 格式可在單顆 B300 上執行（需 SM100+），或透過 W4A16 在兩顆 H200 上執行。

🎯 **實務啟示：從開發者到受監管產業的應用**

這款模型透過 Apache 2.0 授權釋出，為不同規模的組織提供了實用的部署路徑：
* **新創公司**：可以直接在單臺租用的 B300 執行個體上進行自託管 (self-host)。
* **中型企業**：若已有 H200 算力資源，無需額外採購硬體即可直接服務。
* **應用場景**：涵蓋程式碼代理人 (coding agents)、終端機自動化 (terminal automation)、圖表理解、客服分析、語音介面及會議摘要。

對於需要高度安全性與隱私的受監管產業（如金融、醫療、保險、電信與公共部門），這種私有權重 (private-weights) 的選擇提供了極大的安全性保障。

🔗 **來源**
- 標題：Thinking Machines Lab Releases Inkling-Small: A 276B Total, 12B Active Open Weights Multimodal MoE Model
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/02/thinking-machines-lab-releases-inkling-small-276b-open-weights-multimodal-moe-model/

#AI #MachineLearning #MoE #Multimodal #OpenSource #LLM #DeepLearning #AIInfrastructure #InklingSmall #ThinkingMachinesLab
