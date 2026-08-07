---
title: 'Liquid AI Releases LFM2.5-2.6B: An On-Device Agentic Model With 128K Context,
  Tool Calling, And Open Weights'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/06/liquid-ai-lfm2-5-2-6b-on-device-agentic-model/
model: tencent/hy3:free
generated_at: '2026-08-07T07:25:40.771228'
score: 115
---

📌 【Liquid AI】推出 LFM2.5-2.6B：專為裝置端設計，具備 128K 上下文與強大工具呼叫能力

TL;DR：Liquid AI 發布 LFM2.5-2.6B 開源模型，可在手機與筆電本地端執行，具備強大的 Agentic 任務處理能力。

隨著邊緣運算（Edge Computing）需求增加，如何在裝置端（On-device）實現具備代理能力（Agentic）的 AI 成為關鍵。Liquid AI 推出的 LFM2.5-2.6B 模型，旨在讓手機、筆電、PC 甚至機器人，都能在不將數據傳送到雲端的情況下，執行多步驟的複雜任務。

🧩 **混合架構設計：結合捲積與 Attention**

LFM2.5-2.6B 擁有 2.69B 總參數，結構包含 30 層，其設計核心在於結合了兩種不同的機制：
- 22 層雙閘門短捲積區塊（double-gated short convolution blocks）。
- 8 層群組查詢注意力區塊（grouped-query attention blocks）。

為了提升效率，Liquid AI 並非從頭訓練，而是透過以下方式優化：
- **詞彙表擴張**：透過對現有 tokenizer 進行就地（in place）擴展，將詞彙量提升至 128,000。
- **上下文延伸**：透過專門的中期訓練（mid-training）階段，將上下文長度延伸至 131,072 tokens。

📊 **效能表現：以小體量挑戰大規模模型**

根據 Liquid AI 的測試，LFM2.5-2.6B 在指令遵循（instruction-following）與工具使用（tool-use）的表現，足以媲美規模大其近四倍的模型。

| 模型名稱 | 參數規模 | 說明 |
| :--- | :--- | :--- |
| LFM2.5-2.6B | 2.69B | 本專案核心模型 |
| gemma-4-E2B-it | 5.1B | 對照組 |
| gemma-4-E4B-it | 8B | 對照組 |
| Qwen3.5-4B | 4.7B | 對照組 |
| Qwen3.5-9B | 9.7B | 對照組 |

- **指令遵循與工具使用**：LFM2.5-2.6B 在多項基準測試中領先，僅在 BFCLv4 測試中略遜於 Qwen3.5-9B。
- **程式碼能力**：在 LiveCodeBenchv6 測試中，LFM2.5-2.6B 取得 59.41 分，而 Qwen3.5-9B 則為 69.86 分，顯示大型模型在編程領域仍保有優勢。

📦 **開源與落地：支援多種本地端格式**

為了讓開發者能立即部署，Liquid AI 釋出了兩個版本：
1. **LFM2.5-2.6B-Base**：適合用於進一步微調（fine-tuning）。
2. **LFM2.5-2.6B post-trained**：針對代理任務（agentic workloads）進行過後訓練。

這兩個版本皆透過 lfm1.0 授權在 Hugging Face 上公開。此外，權重支援多種原生格式（GGUF、MLX、ONNX），並在發布首日即支援 llama.cpp、vLLM、SGLang 與 LM Studio 等主流工具。

🎯 **實務啟示**

對於開發者而言，LFM2.5-2.6B 提供了一個極具潛力的本地端 Agent 解決方案。由於推理（inference）完全在裝置端完成，這不僅解決了隱私疑慮（數據無需離開裝置），更將每次運行的邊際成本降至接近於零，非常適合需要高頻率、低延遲且具備隱私需求的應用場景。

🔗 **來源**
- 標題：Liquid AI Releases LFM2.5-2.6B: An On-Device Agentic Model With 128K Context, Tool Calling, And Open Weights
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/06/liquid-ai-lfm2-5-2-6b-on-device-agentic-model/

#LiquidAI #LFM #OnDeviceAI #AgenticModel #OpenWeights #MachineLearning #LLM #EdgeAI #EdgeComputing #AIModels
