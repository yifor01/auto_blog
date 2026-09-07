---
title: 'OpenBMB Releases MiniCPM5-2B: A 2.52B Dense Model Averaging 53.9 Across 34
  Benchmarks and Built to Run On Device'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/07/openbmb-releases-minicpm5-2b-a-2-52b-dense-model-averaging-53-9-across-34-benchmarks-and-built-to-run-on-device/
model: claude-code/sonnet
generated_at: '2026-09-07T20:41:22.318055'
score: 100
---

📌 OpenBMB MiniCPM5-2B：25億參數的工具呼叫分數，贏過4B對手

TL;DR：25億參數的 MiniCPM5-2B 用標準 Llama 架構，在工具呼叫與程式碼推理上超越更大模型，訓練資料與中間 checkpoint 全部公開可查驗。

一款端側模型如果只會刷知識類 benchmark，對正在建 agent 的工程師其實沒太大用處。OpenBMB 最新釋出的 MiniCPM5-2B，把賭注押在完全不同的地方：工具呼叫與程式碼 agent 任務，而且拿標準架構就做到了開箱即用。

🤔 不是知識模型，是為端側代理設計的小模型

MiniCPM5-2B 是 MiniCPM5 系列的第二顆 checkpoint，接續先前的 MiniCPM5-1B。這是一個稠密（dense）的因果語言模型，總參數 2,516,756,480，扣除 embedding 後為 1,981,982,720；架構為 42 層、grouped-query attention（16 個 query head、2 個 key/value head），原生支援 131,072 token 的上下文窗口。

🧩 標準 LlamaForCausalLM，主流引擎免改動就能載入

架構上採用標準的 LlamaForCausalLM，代表主流推理引擎不需要客製核心、也不必為它另外 fork 模型程式碼。權重以 Apache 2.0 授權釋出，vLLM、SGLang、Transformers、llama.cpp、Ollama、LM Studio、MLX、FlagOS 都能直接載入運行，對端側部署相當友善。

🧩 UltraData 分層資料 + JustRL II 教師 + OPD 蒸餾

訓練流程延續 OpenBMB 自家研究提出的 UltraData 分層資料管理方法。基礎訓練歷經穩定與衰減兩個階段，接著中訓練把模型調整到目標資料分佈。後訓練先用 4,000 億 token 的深度思考 SFT 資料起步，再用 critic-based 的 JustRL II 演算法，分別針對數學、程式碼、agentic 任務與寫作訓練出多個專用 RL 教師模型。最後一步是 on-policy distillation（OPD）：把 16 個 RL 專家模型（其中 5 個是 agentic 專家）合併蒸餾進單一最終模型，在每個回應位置計算學生與教師 logits 之間的全詞彙表反向 KL 散度，作為優勢估計值，取代原本以驗證結果為基礎的優勢；蒸餾資料直接沿用 RL 階段的 prompt，不另外建立新語料。OpenBMB 表示 RL 加 OPD 這個階段，在推理與通用 benchmark 上平均拉高 10.96 分，在 agentic 類別上拉高 6.96 分。

📊 34 項 benchmark 平均 53.9，工具呼叫拉開最大差距

OpenBMB 把 MiniCPM5-2B 拿去對比同量級的 LFM2.5-2.6B、Qwen3.5-2B、Gemma-4-E2B-it，並列出 Qwen3.5-4B、granite-4.2-3B、Nemotron-3-Nano-4B、Gemma-4-E4B-it、LFM2.5-8B-A1B 作為參考。34 項 benchmark 平均分數為 53.9，同組最佳基準 Qwen3.5-4B 只有 51.1，granite-4.2-3B 為 42.7，LFM2.5-2.6B 為 33.2。

| 項目 | MiniCPM5-2B | 對比基準 |
|---|---|---|
| LiveCodeBench v6 | 69.1 | 56.4 |
| SWE-bench Verified | 46.4 | 33.6 |
| τ²-Bench Telecom | 97.1 | — |
| BFCL v4 | 66.6 | — |
| τ³-Bench Banking | 20.8 | 6.8 |
| NoLiMa | 68.1 | 43.5 |
| AA-LCR | 59.0 | 61.0 |
| LongBench v2 | 43.7 | 47.3 |
| MMLU-Pro | 70.8 | 78.0 |
| Humanity's Last Exam | 8.9 | 9.9 |

OpenBMB 有特別區分哪些數字來自 Artificial Analysis、哪些是內部覆現，方便讀者查驗。

💡 工具呼叫贏最多，通用知識還是輸大模型

從表格可以看出一個清楚的模式：差距最大的都在 agentic 與工具呼叫類任務，τ³-Bench Banking 更是拉開近 3 倍的差距；長上下文表現分裂，NoLiMa 這類檢索型任務表現亮眼，但 AA-LCR、LongBench v2 略遜於對比基準。通用知識類則是這顆模型的明顯弱項，MMLU-Pro、Humanity's Last Exam 都落後參考模型，官方文字也承認在 GPQA-Diamond、MATH-500 上同樣落後更大的模型。

⚠️ 定位要清楚：不是全能模型

MiniCPM5-2B 的強項高度集中在工具使用、程式碼 agent 與特定長上下文檢索場景，若拿來做純知識問答或高難度推理測驗，表現並不突出。這也是為什麼 OpenBMB 自己把它定位為「可信賴的端側 agentic 選項」，而非通用知識模型。

🎯 實務啟示

如果你要在端側跑一個負責呼叫工具、寫程式碼補丁的 agent，MiniCPM5-2B 的分數組合（尤其是 SWE-bench Verified 與 τ 系列 benchmark）值得列入候選；而且訓練釋出的 Ultra-FineWeb、UltraData-SFT-Agent-2609、UltraData-RL-2609 等資料集與 Base／Midtrain／SFT 中間 checkpoint 全部公開，代表 RL 加 OPD 這一步帶來的提升是可以自己覆現驗證的，而不用只信官方的平均分數。

🔗 來源
- 標題：OpenBMB Releases MiniCPM5-2B: A 2.52B Dense Model Averaging 53.9 Across 34 Benchmarks and Built to Run On Device
- 作者／機構：Sana Hassan，MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/07/openbmb-releases-minicpm5-2b-a-2-52b-dense-model-averaging-53-9-across-34-benchmarks-and-built-to-run-on-device/

#MiniCPM5 #OpenBMB #OnDeviceAI #SmallLanguageModel #ToolUse #AgenticAI #SWEBench #OpenSource #LLM #EdgeAI
