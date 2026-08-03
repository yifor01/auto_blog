---
title: 'Alibaba Qwen Releases Qwen3.8-Max: A 2.4 Trillion Parameter MoE Model and
  the Most Capable One in the Qwen Family to Date'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/03/alibaba-qwen-releases-qwen3-8-max/
model: tencent/hy3:free
generated_at: '2026-08-03T09:05:32.706830'
score: 100
---

📌 【Alibaba Qwen】2.4 兆參數 MoE 模型 Qwen3.8-Max 登場，多模態與 Agent 能力大幅躍升

TL;DR：Qwen3.8-Max 採用 2.4T MoE 架構，提供 1M context window 與強大 Agent 能力，API 已開放。

Alibaba Qwen 團隊正式推出 Qwen3.8-Max，這是目前 Qwen 系列中能力最強大的模型。該模型不僅規模達到 2.4 兆參數，更在多模態（Multimodal）與代理任務（Agentic）表現上展現出顯著的世代進步。

🧩 **2.4 兆參數的 MoE 架構與多模態輸入**

Qwen3.8-Max 採用 Mixture-of-Experts (MoE) 架構，總參數規模達 2.4 兆（2.4T）。
- **輸入與輸出**：支援文本、圖像與影片輸入，並輸出文本。
- **上下文長度**：提供 1M token 的上下文視窗。其中最大輸入為 991K tokens；若啟用「思考模式（thinking mode）」，最大輸入會降至 983K tokens。最大輸出則維持在 131K tokens，最大推理預算（reasoning budget）為 262K tokens。
- **部署說明**：由於參數規模巨大，2.4T 的權重（weights）屬於多節點資料中心級別的產物。目前已透過 Hosted API 開放使用，且相容於 OpenAI 與 DashScope 介面，開發者只需更改 Base-URL 與 Model-ID 即可快速整合。

📊 **基準測試：多模態與 Agent 表現是最大亮點**

根據 Alibaba 發布的測試數據，Qwen3.8-Max 在多模態與代理任務上的增長最為顯著。

**軟體工程與推理能力：**
- **Terminal-Bench 2.1**：Qwen3.8-Max 取得 86.6 分，領先 Claude Opus 4.8 (84.6)，僅次於 GPT-5.6 Sol (max) (88.8)。
- **SWE-bench Pro**：取得 67.7 分（對比 Fable 5 的 80.0）。
- **FrontierSWE**：取得 73.5 分（對比 Fable 5 的 88.8）。
- **DeepSWE 1.1**：從前代 Qwen3.7-Max 的 21.6 分大幅躍升至 56.6 分。

**多模態能力（對標 Qwen3.7- Plus）：**
- **OSWorld-Verified**：86.1
- **Parametric CAD Bench**：91.5
- **OmniDocBench 1.5**：92.1

⚠️ **技術限制與觀察**
作者指出，多模態測試是與 Qwen3.7- Plus 進行對比而非 Max 版本，這可能會放大世代間的差異。此外，Alibaba 的 RL scaling curve 在接近 4,000 個訓練環境時達到 0.725 的峰值後，隨後會下降至 0.719 與 0.689。

💰 **API 價格與功能特性**

Qwen3.8-Max 提供完整的開發者工具與功能集。

- **定價結構**：
    - 輸入：$2.00 / 1M tokens
    - 輸出：$6.00 / 1M tokens
    - 隱含快取讀取 (Implicit cache reads)：$0.25 / 1M tokens
    - 顯式快取建立 (Explicit cache creation)：$2.50 / 1M tokens
    - 顯式快取讀取 (Explicit cache reads)：$0.17 / 1M tokens
    - *註：使用快取輸入的成本僅為原始輸入的 1/8，因此前綴穩定性（Prefix stability）對成本的影響大於 Prompt 長度。*
- **內建工具**：Responses API 提供 code_interpreter、web_search、web_extractor、t2i_search 與 i2i_search 五種工具。
- **支援功能**：Function calling、Structured outputs、Batches、Prefix completion 與 Fine-tuning。

🎯 **實務應用與工程啟示**

Qwen3.8-Max 的能力範疇涵蓋了四大產業需求，特別適合需要高複雜度邏輯與多模態理解的場景：
1. **軟體工程**：用於大規模程式碼庫規模的 Coding Agents。
2. **法律與金融**：處理長文件審閱與知識庫。
3. **媒體與電商營運**：進行長影片索引與結構化資料擷取。
4. **設計領域**：支援多步驟的研究助手。

對於資源有限的開發者，Alibaba 也將推出 Qwen3.8-27B 的開源權重版本，該版本更適合在一般的地端 GPU 硬體上運行。

🔗 **來源**
- 標題：Alibaba Qwen Releases Qwen3.8-Max: A 2.4 Trillion Parameter MoE Model and the Most Capable One in the Qwen Family to Date
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/03/alibaba-qwen-releases-qwen3-8-max/

#Alibaba #Qwen #MoE #LLM #Multimodal #MachineLearning #AI #SoftwareEngineering #AgenticAI #LargeLanguageModels
