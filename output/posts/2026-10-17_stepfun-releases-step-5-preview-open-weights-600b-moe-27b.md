---
title: 'StepFun Releases Step 5 Preview Open Weights: 600B MoE, 27B Active, 1M Context'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/16/stepfun-releases-step-5-preview-open-weights-600b-moe-27b-active-1m-context/
model: claude-code/sonnet
generated_at: '2026-10-17T19:31:27.825975'
score: 94
---

📌 StepFun 開權重 Step 5 Preview：600B MoE、僅啟動 27B、上下文上看 1M

TL;DR：StepFun 開源 600B 參數的 agentic MoE 模型，僅啟動 27B，提供可自架的長任務 coding/金融選項。

一個總參數 600B、每次推理卻只喚醒 27B 的模型，context 長度上看 1M tokens，而且權重直接開放下載——這是 StepFun 為「長時間 agentic 任務」量身打造的旗艦模型。

🤔 **為軟體工程、知識工作與金融而生**

Step 5 Preview 是 StepFun 針對 agentic 工作推出的旗艦模型，定位在軟體工程、專業知識工作與金融三大場景。StepFun 表示這個模型能在大型程式碼庫中導航、協調跨多檔案的修改、執行程式碼並根據結果持續迭代，也能分析長文件、圖表、截圖與影片，產出結構化報告。API 於 9 月 20 日上線，權重則在 10 月 14 日跟進釋出，FP8 與 BF16 兩種 checkpoint 都已經放上 Hugging Face 與 ModelScope。

🧩 **600B 總參數，27B 稀疏啟動**

Step 5 Preview 是一個稀疏 Mixture-of-Experts 模型，總參數量 600B，每個 token 只啟動 27B，context 長度最高可達 1M tokens。部署面，vLLM 與 SGLang 都提供了附帶 OpenAI 相容 API 的專用 Docker image；在 Blackwell 架構上，expert-parallel 模式會使用 MegaMoE backend。StepFun 建議的推理參數是 temperature 1.0、top_p 0.95、top_k 0。

📊 **跑分細節：自評用 High reasoning，對手用 Max effort**

需要留意的是，StepFun 自己的評測是在 High reasoning 設定下進行,而圖表裡的對手模型是在 Max effort 下測試,嚴格說起來並非同條件比較。以下數字出自 Hugging Face 模型卡,其中 Intelligence Index、AA-LCR、Humanity's Last Exam、GDPval-AA 是來自 Artificial Analysis 透過 OpenRouter 取得的獨立測試結果，SRE Bench 與 Harvey's Legal Agent Benchmark 來自 Vals AI，FrontierFinance 則是 StepFun 自家對比圖表中的數字（由 CellCog 與 eesel 轉錄）：

| Benchmark | 來源 | Step 5 Preview |
|---|---|---|
| Intelligence Index | Artificial Analysis | 43.7 |
| AA-LCR | Artificial Analysis | 88.3% |
| Humanity's Last Exam | Artificial Analysis | 46.5% |
| GDPval-AA | Artificial Analysis | 54.3% |
| SRE Bench | Vals AI | 0.4% |
| Harvey Legal Agent Benchmark | Vals AI | 9.2% |
| FrontierFinance | StepFun 自評 | 66.4% |

在 FrontierFinance 上，Step 5 Preview 的 66.4% 勝過 GLM-5.3 與 Kimi K3，但落後 Claude Opus 5 的 69.7%。而 SRE Bench 僅 0.4%、Harvey's Legal Agent Benchmark 僅 9.2%，顯示在 SRE 維運與法律 Agent 這類任務上，這個模型的弱點相當明顯。

⚠️ **權重龐大，部署門檻高**

FP8 checkpoint 單檔就有 650.32 GB，這是一個徹頭徹尾的資料中心級模型，自架需要對應規模的 GPU 叢集，並不適合個人或小團隊在單機上跑完整版本。

🎯 **API 定價與整合方式**

StepFun API 的計價是每 1M input tokens 1.00 美元、每 1M output tokens 2.70 美元，輸出計價含推理 token，cache 命中則降至每 1M 0.10 美元。API 支援 low、medium、high 三種 reasoning effort、工具呼叫（tool calling）與 JSON Schema 輸出，對已經在用其他 OpenAI 相容 API 的 agent 框架來說，切換成本不高，是值得納入 benchmark 清單的新選項。

🔗 **來源**
- 標題：StepFun Releases Step 5 Preview Open Weights: 600B MoE, 27B Active, 1M Context
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/16/stepfun-releases-step-5-preview-open-weights-600b-moe-27b-active-1m-context/

#StepFun #OpenWeights #MixtureOfExperts #LLM #AgenticAI #LongContext #CodingAgent #OpenSourceAI #HuggingFace #MoE
