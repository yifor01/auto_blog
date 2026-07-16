---
title: 'Boogu-Image-0.1: Boosting Open-Source Unified Multimodal Understanding and
  Generation'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.13125
score: 98
model: tencent/hy3:free
generated_at: '2026-07-16T08:13:35.293495'
---

📌 【開源多模態】Boogu-Image-0.1：低運算預算逼近封閉系統的統一模型

TL;DR：開源統一多模態家族 Boogu-Image-0.1，以約 40 萬美元訓練成本逼近領先封閉系統。

當 Nano-Banana-Pro、GPT-Image-2 這類封閉多模態系統靠系統級整合拉高效能，但內部做法幾乎不公開時，開源陣營還有機會追上嗎？Boogu-Image-0.1 給出了一個務實的答案。

🤔 **封閉系統靠整合取勝，但細節不透明**

摘要指出，Nano-Banana-Pro 與 GPT-Image-2 等封閉多模態系統透過 system-level integration 而非單一模型達成強效能，然而其內部實作大多未公開。這讓研究社群難以複現或借鑒。

🧩 **四個變體覆蓋理解、生成與編輯**

Boogu-Image-0.1 是一個開源統一多模態理解與生成模型家族，包含四種變體：
- Base：基礎模型
- Turbo：推論速度最佳化版本
- Edit：指令式影像編輯版本
- Edit-Turbo：編輯加速版本

家族目標涵蓋高品質文字轉影像（text-to-image）、快速推論、基於指令的編輯，以及中英雙語文字渲染（bilingual text rendering）。

💡 **在受限運算下靠三件事拉高效能**

作者宣稱，在高度受限的運算預算下，透過以下方向可大幅強化生成與編輯表現：
- 針對模型理解能力做定向改進
- 提升資料品質與訓練流程（training pipelines）
- 搭配 agentic inference-time scaling（推論期 Agent 式擴充套件）

這意味著不一定需要龐大單一模型或系統整合，也能逼近封閉系統結果。

📊 **評測結果與成本資料**

- 綜合評估顯示，Boogu-Image-0.1 在標準基準上穩定持平或超越其他開源模型，並達到接近領先封閉系統的結果。
- 訓練僅使用 2.0862 億張獨特影像（208.62 million unique images）。
- 基礎模型的理論訓練成本約為 40 萬美元（\$400K）。

🎯 **實務啟示**

對資源有限的團隊，這篇工作釋出的權重、程式碼與 recipes（Apache 2.0 授權）提供可落地的統一多模態起點；其「資料品質 + 訓練流程 + 推論期擴充套件」的路線，也比盲目堆引數更適合預算受限的場景。

🔗 **來源**
- 標題：Boogu-Image-0.1: Boosting Open-Source Unified Multimodal Understanding and Generation
- 連結：https://huggingface.co/papers/2607.13125

#Multimodal #TextToImage #ImageEditing #OpenSource #BooguImage #UnifiedModel #InferenceTimeScaling #Apache2 #LLM #GenerativeAI
