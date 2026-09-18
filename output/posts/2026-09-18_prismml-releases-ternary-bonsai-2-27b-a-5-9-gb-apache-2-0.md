---
title: 'PrismML Releases Ternary Bonsai 2 27B: A 5.9 GB Apache 2.0 Model Retaining
  98.2% of Qwen3.8 27B Performance'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/18/prismml-releases-ternary-bonsai-2-27b-a-5-9-gb-apache-2-0-model-retaining-98-2-of-qwen3-8-27b-performance/
model: claude-code/sonnet
generated_at: '2026-09-18T19:45:27.818243'
score: 103
---

📌 27B 模型壓進 5.9GB,三元量化保住 98.2% 效能

TL;DR：PrismML 把 Qwen3.8 27B 轉成三元權重,體積縮小 9 倍,單張 24GB GPU 就能跑。

一個 53.8GB 的 27B 模型,能不能塞進 5.93GB,同時保住近乎完整的能力?PrismML 這次給出的答案是 98.2%——但這個平均數背後,藏著幾個值得工程師留意的取捨。

🧩 **架構不變,只把大部分權重壓成三值**

Ternary Bonsai 2 27B 沿用 Qwen3.8 27B 的架構,共 27.36B 參數,拆解為 24.35B 的語言骨幹、2.54B 的 embedding 與 LM head、以及 0.47B 的視覺塔。骨幹採混合注意力,約 75% 為 linear-attention、25% 為 full-attention。三元量化覆蓋 embedding、attention 投影、MLP 投影與 LM head,只有 26.2M 參數(佔比 0.0976%)維持高精度,分別是 recurrent state path 與正規化權重。在 GGUF 格式中,視覺塔以獨立的 0.63GB 檔案存在,僅在輸入影像時才載入。

三元權重每個值取 -1、0 或 +1,每 128 個權重共享一個 FP16 scale。理論上一個三元值攜帶 log2(3)≈1.585 bit,加上每 128 個權重分攤的 16-bit scale,平均約 1.71 bit/權重,連同高精度張量後總計約 1.72 bit。白皮書描述了兩種實際打包格式:PTQ1_0 密集打包,達 1.76 bit/權重、5.93GB;PQ2_0 每個 trit 佔用 2-bit 槽位,體積來到 7.25GB,但解包成本更低。權重在存放前還經過 block size 1,024 的分塊 Hadamard 旋轉(白皮書引用 SpinQuant 的概念),runtime 會在每次乘法前對 activation 套用對應的變換。PrismML 並未公開三元值的具體指派方法。

📊 **對比一般量化的差距,以及長任務上的短板**

PrismML 用 EvalScope 搭配 vLLM 在 H100 上以 thinking mode 評測。與傳統量化相比,同樣體積量級的 IQ2_XXS 版 Qwen3.8 27B(7.3GB)平均只有 75.2 分;AIME26 上 IQ2_XXS 拿 78.6,Bonsai 2 則是 95.83;LiveCodeBench v6 上分別為 70.05 對 90.07。

不過 98.2% 是 20 項 benchmark 的平均值,各項落差並不均勻。視覺任務保留 96.3%,知識與推理保留 96.9%,但長任務的 agent 表現掉得更多:Terminal-Bench 2.1 上 52.8 分對照原版 69.7 分,SWE-bench Verified 上 60.8 分對照 80.6 分,保留率約 75%,兩者都落在整體平均之外。推理強度同樣有影響:medium 模式下平均 79.3,FP16 基準則是 82.6;low 模式目前不支援。

⚠️ **這是 PrismML 自家測試的數字**

文中所有結果均為 PrismML 自行測得,尚未經第三方複現。速度數據為 batch size 1 解碼、使用 PrismML 自家 kernel、於 2026 年 9 月 16 日測得:RTX 5090 達 142.5 tokens/秒,耗能 0.582 mWh/token;RTX 4090 搭配 PTQ1_0 為 96.7 tokens/秒;72W 的 L4 為 32.1;Apple M5 Max 為 46.8,M5 Pro 為 27.7。兩種打包格式各有優勢:PTQ1_0 在 Ada 世代顯卡與 L4 上較快,PQ2_0 則在 Blackwell、Hopper、Ampere、Apple Silicon,以及所有平臺的 prompt processing 階段較快。PrismML 團隊另宣稱能效比一款全精度 8B 模型高出 40%。

🎯 **實務啟示**

要跑起來,需要 PrismML 自家的 llama.cpp fork 或 MLX runtime,原生 llama.cpp 不認得 PTQ1_0 與 PQ2_0 這兩種格式。官方支援路徑是走 Bonsai-demo repo:執行 `./setup.sh` 再跑 `./scripts/start_llama_server.sh`,即可在 localhost:8080 使用含 vision 與工具呼叫的 chat 介面;Mac 用戶可用 MLX pack(需搭配專屬 loader);也有一個可在瀏覽器內直接執行的 WebGPU demo。如果你的場景偏重一般知識或視覺任務,這顆模型的性價比相當可觀;但若工作流仰賴長任務 agent(如 SWE-bench 類型的多步驟修 bug),保留率明顯較低,值得先用自己的任務實測。

🔗 **來源**
- 標題:PrismML Releases Ternary Bonsai 2 27B: A 5.9 GB Apache 2.0 Model Retaining 98.2% of Qwen3.8 27B Performance
- 作者/機構:Asif Razzaq, MarkTechPost
- 連結:https://www.marktechpost.com/2026/09/18/prismml-releases-ternary-bonsai-2-27b-a-5-9-gb-apache-2-0-model-retaining-98-2-of-qwen3-8-27b-performance/

#TernaryQuantization #LLM #Quantization #OpenSource #Apache2 #EdgeAI #Qwen #ModelCompression #GGUF #OnDeviceAI
