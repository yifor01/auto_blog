---
title: Liquid AI Ships LFM2.5-230M with llama.cpp, MLX, vLLM, SGLang, and ONNX Support
  for On-Device Inference
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/27/liquid-ai-ships-lfm2-5-230m-with-llama-cpp-mlx-vllm-sglang-and-onnx-support-for-on-device-inference/
score: 98
model: google/gemma-4-31b-it:free
generated_at: '2026-06-29T20:25:25.994415'
---

📌 【Liquid AI】推出 LFM2.5-230M：專為邊緣裝置設計的 Agentic 小模型

TL;DR：230M 引數混合架構模型，主打行動裝置與機器人上的資料擷取與工具呼叫。

當大模型追求引數規模時，Liquid AI 選擇往反方向走。他們推出了至今最小的模型 LFM2.5-230M，目標非常明確：不追求通用推理，而是要讓手機、機器人與自動化裝置能高效執行 agentic 任務。

🧩 **混合架構設計：Convolution 與 GQA 的結合**

LFM2.5-230M 採用 LFM2 架構，是一個純文字模型，其設計核心在於最佳化 CPU 推論速度。模型總共由 14 層組成，採取混合佈局：
- 8 層 double-gated LIV convolution blocks。
- 6 層 grouped-query attention (GQA) blocks。

其餘技術規格包括 32,768 tokens 的上下文長度、65,536 的詞彙量，支援包含中文、英文、阿拉伯文與日文在內的 10 種語言。

📊 **從 19 兆 Token 到三階段後訓練**

為了讓 230M 的小規模模型維持競爭力，Liquid AI 在訓練流程上下了功夫：
1. **預訓練**：使用 19 兆 tokens 進行訓練，其中包含一個 32K 的上下文擴充套件階段。
2. **後訓練三部曲**：
   - 第一階段：透過 LFM2.5-350M 進行蒸餾 (distillation) 的監督式微調 (SFT)。
   - 第二階段：直接偏好最佳化 (DPO)。
   - 第三階段：多領域強化學習 (multi-domain RL)。

作者指出，正是透過從較大的 LFM2.5-350M 進行蒸餾，使該模型在特定任務上能繼承較大模型的行為表現。

📈 **小尺寸卻在指令遵循上領先 1B 模型**

Liquid AI 在 10 項基準測試中評估了該模型，結果顯示其在指令遵循與資料擷取方面表現強勁：
- **IFEval**：得分 71.71，超越 Qwen3.5-0.8B (59.94) 與 Gemma 3 1B IT (63.49)。
- **IFBench**：得分 38.40，同樣領先上述兩款模型。
- **CaseReportBench**（臨床資料擷取測試）：得分 22.51。

🎯 **實務啟示：邊緣端 Agent 的新選擇**

LFM2.5-230M 並非通用推理模型，而是一個專精於「資料擷取」與「工具使用」的工具。對於需要部署在資源受限硬體（如手機或嵌入式裝置）且需要執行特定 Agent 任務的工程師來說，這提供了一個低延遲且高效的選擇。目前該模型已提供 Base 與 Instruction-tuned 兩種權重，並支援 llama.cpp, MLX, vLLM, SGLang 與 ONNX 等主流推論框架。

🔗 **來源**
- 標題：Liquid AI Ships LFM2.5-230M with llama.cpp, MLX, vLLM, SGLang, and ONNX Support for On-Device Inference
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/06/27/liquid-ai-ships-lfm2-5-230m-with-llama-cpp-mlx-vllm-sglang-and-onnx-support-for-on-device-inference/

#LiquidAI #LFM2 #OnDeviceAI #EdgeComputing #LLM #SmallLanguageModel #AgenticAI #ModelDistillation #MachineLearning #Inference
