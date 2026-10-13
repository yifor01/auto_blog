---
title: Run fast, private agents on-device with LFM2.5-24B-A2B
source: HuggingFace Blog
url: https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b
model: claude-code/sonnet
generated_at: '2026-10-13T22:01:11.505529'
score: 107
---

📌 【LiquidAI 開源】24B 參數只點亮 2B，端側 Agent 也能跑推理

TL;DR：LFM2.5-24B-A2B 是只啟用 2B 參數的 24B MoE 推理模型，專為在自己硬體上長時間跑 agent 設計。

如果你曾經想在筆電或單張消費級 GPU 上跑一個會思考、會呼叫工具、還要連續運作好幾輪的 agent，多半會卡在一個問題：reasoning token 太貴，模型一邊想一邊燒錢也燒顯卡。LiquidAI 這次釋出的 LFM2.5-24B-A2B，用「總參數 24B、每個 token 只啟用 2B」的設計,試著把這個成本壓下來。

🤔 **為什麼端側 agent 需要「便宜的 reasoning token」**

Agent 任務的特徵是多步驟、要呼叫工具、還要在過程中反覆推理。如果每個 reasoning token 都要動用大量運算,在自己的裝置上連續跑 agent 幾乎不現實。LiquidAI 的切入點是:既然推理模型本身就要先想再答,那不如讓每個 token 的運算成本降到最低,這樣才能在自己的硬體上「持續」跑 agent,而不是跑一次就要等很久。

🧩 **架構沿用 LFM2-24B-A2B,但把 context 和詞表都做大**

LFM2.5-24B-A2B 延續前代 LFM2-24B-A2B 的架構:40 層、每個 MoE block 有 64 個專家、top-4 路由,並維持 gated short convolution 與 GQA 的混合設計。相較前代,這一版把 context window 從 32K 擴到 131K token,並透過 in-place tokenizer 擴充,把詞表從 65K 翻倍到 128K,改善非拉丁語系文字的 tokenization。與前代不同的是,這一版被設計成「純推理模型」,也就是回答前一定會先產出明確的 chain of thought。

訓練規模也同步放大:預訓練 token 量從約 17T 拉到約 33T。中段訓練再加上 2T token(32K context,偏重推理、數學、程式碼、指令遵循與多語言)以及 300B token(131K context,偏重長文本),且工具呼叫與多輪軌跡資料貫穿這兩個階段。後訓練則分五個階段:SFT、教師模型專精化、非 agentic 的多領域 on-policy distillation(MOPD)、agentic 的 MOPD,最後在 OpenClaw、Hermes Agent、Pi、OpenCode 等 agent harness 裡做 agentic 強化學習。

📊 **用 50% 更少的參數,打平甚至打贏更大的 MoE**

LiquidAI 用 16 個橫跨工具使用、知識、指令遵循、數學與程式碼的 benchmark,拿 LFM2.5-24B-A2B 和總參數、啟用參數都多出約 50% 的 Qwen3.6-35B-A3B,以及 Gemma-4-26B-A4B-it、Nemotron-3.5-Lightning(30B-A3B)比較:

| Benchmark | LFM2.5-24B-A2B | Qwen3.6-35B-A3B | Gemma-4-26B-A4B-it | Nemotron-3.5-Lightning |
|---|---|---|---|---|
| AutomationBench | 27.69 | 8.72 | 5.46 | 2.61 |
| BFCLv4 | 65.01 | 65.00 | 57.09 | 53.78 |
| ToolSandbox | 80.71 | 75.02 | 72.09 | 75.13 |
| LiveClaw | 48.09 | 38.19 | 41.25 | 37.72 |
| IFEval | 96.75 | 93.06 | 92.00 | 94.19 |
| SWE-Bench Verified (OpenCode) | 51.00 | 66.20 | 25.80 | 53.40 |

在 8 個工具使用/agentic benchmark 中,LFM2.5-24B-A2B 在 5 項領先或打平,AutomationBench 更是拿到next-best 模型三倍以上的分數,三項指令遵循 benchmark 也全部領先。

💡 **強在工具呼叫,弱在純知識與程式碼**

在 GPQA Diamond、HLE、AA-Omniscience 這類知識密集型 benchmark,以及 SWE-Bench Verified(OpenCode)、SciCode 這類程式碼 benchmark 上,較大的模型仍保有優勢。LiquidAI 自己的建議是:知識密集的工作負載,搭配 retrieval 或網路搜尋來補強,而不是硬要模型自己記住所有知識。

推理速度方面,官方數據顯示在 Apple M5 Max 上可達 184 tok/s,在 Ryzen AI Max+ 395 上為 114 tok/s,號稱是同尺寸 MoE 中最快且記憶體用量最低;單張 NVIDIA B300 在高併發下則可衝到超過 21K output tokens/s。

⚠️ **仍是既有稀疏化架構的延伸**

LFM2.5-24B-A2B 本質上是在 LFM2-24B-A2B 的 MoE 架構上做規模放大與後訓練強化,並非全新的稀疏化設計。對於知識廣度與程式碼生成要求較高的場景,仍需要搭配外部工具或更大的模型。

🎯 **怎麼接進你的 agent harness**

模型已開源在 Hugging Face,支援 transformers、llama.cpp、MLX、vLLM、SGLang、ONNX 等推理生態系。只要用你偏好的後端把模型跑成 OpenAI 相容的服務,再把 Hermes Agent、OpenClaw、Pi 等 agent harness 指向對應的 port(llama.cpp/MLX 用 8080,vLLM 用 8000,SGLang 用 30000,LM Studio 用 1234),就能快速接上既有的 agent 流程。

🔗 **來源**
- 標題:Run fast, private agents on-device with LFM2.5-24B-A2B
- 作者／機構:LiquidAI(HuggingFace Blog)
- 連結:https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b

#MixtureOfExperts #OnDeviceAI #LLM #AgenticAI #OpenSource #LiquidAI #EdgeInference #ToolUse #ReasoningModel #HuggingFace
