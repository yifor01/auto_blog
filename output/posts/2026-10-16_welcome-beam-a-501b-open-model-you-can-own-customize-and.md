---
title: 'Welcome Beam: a 501B open model you can own, customize, and scale'
source: HuggingFace Blog
url: https://huggingface.co/blog/reflection-beam
model: claude-code/sonnet
generated_at: '2026-10-16T20:09:57.606835'
score: 109
---

📌 Reflection 首發即王炸:501B 開源模型 Beam 附完整訓練配方

TL;DR:新創實驗室 Reflection 推出首款模型 Beam,501B 參數、23B 啟動、1M context,Apache 2.0 授權並附推理/微調/RL 全套配方。

一間新創實驗室的「第一個模型」,通常是驗證概念的小模型。但 Reflection 一出手就是 501B 參數的開源 MoE,還把推理、監督微調(SFT)與強化學習(RL)的配方全部公開。這不只是放話,而是把整套可落地的工具鏈一起交給社群。

🤔 **Reflection 是誰,Beam 為何而生**

Beam 是美國新實驗室 Reflection 的首款模型,鎖定程式碼與 agentic 場景,鎖定的對象是想在自己的硬體、基礎設施或雲端上擁有並客製化 frontier 等級模型的團隊。模型以 Apache 2.0 授權釋出,純文字輸入輸出,context window 達 1M tokens。

🧩 **架構拆解:混合 attention、群組限制路由與等比例殘差流**

Beam 是 52 層的 MoE 模型,hidden size 5,120,共 501B 參數、每 token 啟動 23B。

Attention 設計分兩種:大多數層使用滑動視窗(sliding-window)attention,只看前 512 個 token;每第 6 層以及最後一層則採全域 attention,看得到完整 context。結果是 43 個滑動視窗層加上 9 個全域層。滑動視窗層使用 RoPE 處理相對位置;全域層則完全不用位置編碼,改為讓每個 query 乘上一個隨可見 token 數緩慢增長的縮放因子 (1 + (pos + 1) / 2048) ** 0.1,官方稱之為「scalable-softmax query scaling」,作用類似溫度參數,讓 softmax 在長 context 下仍保持精準度而不致攤平。Attention 本身採用分組查詢注意力(GQA),48 個 query head 對 8 個 key-value head,並在 query 與 key 上做 RMSNorm,另有一個學習得來的 sigmoid gate 在輸出投影前對每個 channel 做縮放。

MoE 部分:前 3 層是密集的 SwiGLU MLP,其餘 49 層換成 MoE 區塊,每層 256 個專家,每個專家是 intermediate size 2,560 的 SwiGLU MLP(約 3,900 萬參數),專家合計佔了全模型 98.4% 的參數。路由機制沿用 DeepSeek-V3 的群組限制方案:先用 sigmoid 為全部 256 個專家評分,分成 8 組、每組 32 個,依每組前兩名分數之和挑出最好的 4 組,再從中選出 top 8 個專家。Beam 沿用 DeepSeek-V3 的分組大小但不設共享專家,專家輸出以正規化後的路由權重合併,並再乘上 2.5 的縮放係數。每個 token 實際只跑 8 個專家,運算量相當於約 23B 參數的模型,但 256 個專家全部常駐記憶體,因此部署時仍需準備 501B 等級的記憶體。

殘差流的設計也值得一提:標準 transformer 每層把子層輸出以權重 1 加進殘差流,深度越深數值越大。Beam 則把輸入 embedding 視為第 1 步,第 k 步以權重 1/sqrt(k) 加入子層輸出,並以權重 sqrt((k-1)/k) 保留既有殘差流,兩個權重的平方和為 1,因此殘差流從第一層到最後一層都維持固定量級。所有子層都在前後做正規化,最終 logits 則通過 ±30 的 tanh softcap,並在 FP32 精度下計算。路由、SwiGLU 乘積、各種 norm、RoPE、query scaling 與 softcap 皆固定以 FP32 運算。

📊 **長 context 下的 KV cache 效率**

因為只有 9 個全域層需要保留完整序列,43 個滑動視窗層的 cache 固定在 512 個 token,整體 KV cache 成長速度只有「全部層都是全域 attention」情境的約六分之一:1M context 下,前者約 208 GiB,Beam 只需約 36.08 GiB。

📊 **跨精度的 Benchmark 表現**

Reflection 官方提供了 BF16、FP8、NVFP4 三種精度下的評測結果:

| 類別 | 指標 | BF16 | FP8 | NVFP4 |
|---|---|---|---|---|
| Agentic Coding | SWE-Bench Pro v2-Hard | 76.5% | 78.4% | 78.6% |
| Agentic Coding | SWEBench Verified | 81.6% | 80.2% | 80.7% |
| Agentic Coding | Terminal-Bench v2.1 | 80.1% | 78.9% | 78.2% |
| Reasoning | AIME 2026 | 97.7% | 98.0% | 97.5% |
| Reasoning | GPQA Diamond | 90.6% | 90.3% | 89.3% |
| Tool Calling | MCP Atlas | 80.8% | 81.5% | 80.5% |
| Tool Calling | BrowseComp w/ context management | 76.8% | 76.7% | 75.6% |

可以看到三種精度之間的分數差距大多在 1 個百分點以內,代表量化後的 NVFP4 版本幾乎不損失能力。

💡 **從 Day-0 支援到社群獎勵**

Beam 在 transformers、SGLang、vLLM 都有原生支援,另附 DFlash2 推測性解碼(speculative decoding)drafter 模型加速生成,並以自家 Rust harness 提供最佳效能。全參數 RL 由 Miles 框架支援。BF16 checkpoint 約 1TB,NVFP4 透過 4-bit 量化把大部分參數壓到約 280GB,適合 Blackwell GPU;FP8 版本則鎖定 Hopper 與 Ampere 系列晶片。Reflection 另外釋出 10,000 美元 Hub credits,獎勵用 Beam 做出 demo、量化版本、合成資料集或 RL 環境並分享到 Hub 的社群專案。

🎯 **實務啟示**

對於想要「擁有並客製化」frontier 等級模型、而非只租用 API 的團隊,Beam 的完整配方(推理、SFT、RL)降低了自建 pipeline 的門檻;NVFP4 把 1TB 壓到 280GB,是目前在自有硬體上部署 500B 級模型最務實的路徑。

🔗 **來源**
- 標題:Welcome Beam: a 501B open model you can own, customize, and scale
- 作者／機構:HuggingFace(與 Reflection 團隊合作)
- 連結:https://huggingface.co/blog/reflection-beam

#Beam #Reflection #OpenSourceLLM #MixtureOfExperts #HuggingFace #LongContext #ApacheLicense #LLMInference #AgenticCoding #ModelQuantization
