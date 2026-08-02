---
title: Inkling – Open-Weights 975B Parameter LLM
source: Hacker News
url: https://thinkingmachines.ai/inkling/
score: 93
model: tencent/hy3:free
generated_at: '2026-07-16T08:16:49.404760'
---

📌 【Thinking Machines】Inkling：開放權重 975B MoE 多模態模型

TL;DR：975B 參數 MoE 開放權重模型，支援文圖音輸入與微調，上下文達 1M tokens。

Hacker News 上一篇貼文指出，有一個總參數 975B 的開放權重 LLM 悄然現身，不只能吃文字，還原生支援圖片與音訊輸入。當多數前沿多模態能力仍鎖在閉源API後，這種可自由 tinker 的龐然大物值得工程師關注。

🤔 **開放權重、可微調的通用模型定位**

Inkling 由 Thinking Machines 釋出（Hacker News 貼文作者標注為 htrp），標榜是「efficient open model for text, images, and audio, available to fine-tune」。它並非純研究發表，而是一個對外開放的模型專案，提供 Model card 與 Hugging Face 權重，目標使用者是想要自行客製化的開發者與研究者。

🧩 **975B 總參數、41B 活躍的 MoE 架構**

根據模型概覽，Inkling 採用 Mixture of Experts (MoE) 架構：
- 總參數 975B，每次推理活躍參數為 41B
- 上下文視窗（context window）為 1M tokens，在官方 Tinker 平臺上可達 64K 或 256K（素材未說明此處單位差異細節，僅列原述）
- 輸入模態（input modalities）包含文字、圖片、音訊

README 指出它是「well-rounded, generalist model」，並在十項評測上與 Nemotron 3 Ultra、GLM 5.2、GPT 5.6 Sol、Claude Fable 5 比較（未提供具體分數，僅有雷達圖視覺化）。

💡 **原生多模態與可控推理成本**

專案頁列舉的能力重點包括：
- General intelligence：在知識、數學、科學表現良好
- Agentic coding & tools：能寫程式並使用工具完成任務
- Audio & image input：輸入端原生多模態，且在開源語音前沿
- Controllable effort：可調整思考時間以平衡速度與效能
- Forecasting & confidence：具備校準過信心的水準預測
- Instruction following：可靠處理多步驟細節指令
- Ready to customize：可在 Tinker 訓練平臺針對領域微調

🎯 **實務啟示**

對 ML 工程師而言，Inkling 提供了一個少見的「大規模 + 開放權重 + 多模態輸入」組合。若團隊需要在自有領域做 fine-tuning，且不想被閉源模型綁死，可從 Hugging Face 拉權重，在 Tinker 上評估微調成本與 41B 活躍參數的推理負載。不過實際部署前，仍建議等待社群跑出獨立基準，確認雷達圖未列出的細項表現。

🔗 **來源**
- 標題：Inkling – Open-Weights 975B Parameter LLM
- 作者／機構：htrp（釋出於 Hacker News）
- 連結：https://thinkingmachines.ai/inkling/

#LLM #OpenWeights #MoE #Multimodal #FineTuning #Inkling #ThinkingMachines #HuggingFace #AI #ModelRelease
