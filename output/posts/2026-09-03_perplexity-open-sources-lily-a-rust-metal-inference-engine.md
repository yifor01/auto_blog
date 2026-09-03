---
title: 'Perplexity Open Sources Lily: A Rust + Metal Inference Engine for Qwen3.6-35B-A3B
  on Apple Silicon'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/02/perplexity-open-sources-lily-a-rust-metal-inference-engine-for-qwen3-6-35b-a3b-on-apple-silicon/
model: claude-code/sonnet
generated_at: '2026-09-03T20:15:55.265850'
score: 103
---

📌 Perplexity開源Lily:捨棄PyTorch與MLX,手寫Metal引擎跑贏官方棧up to 35%

TL;DR:Perplexity開源本地推理引擎Lily,只服務Qwen3.6-35B-A3B這一顆模型與Apple Silicon這一種硬體,換來prefill最高1.42倍、decode最高1.37倍的實測加速。

通用推理框架講究「一套邏輯服務所有模型」,但Perplexity給出了另一個答案:把範圍縮到極窄,效能天花板完全不同。這正是Lily的核心論點。

🤔 通用棧的代價,窄範圍的籌碼

Mac上的預設推理棧是MLX加MLX-LM,已經內建了Qwen的實作,包括grouped expert運算、融合的recurrent Metal kernel,以及支援GQA(grouped-query attention)的attention機制。但MLX的運算元必須維持跨架構可重用,這是通用框架必然的取捨。Lily放棄了這種通用性,把模型結構、執行計畫與kernel選擇全部寫死在同一個runtime裡。它是單一process:Rust層負責載入checkpoint與驅動生成迴圈,一個OpenAI相容的chat-completions API負責串流輸出token,手寫的Metal kernel負責實際執行,整條路徑上沒有PyTorch也沒有MLX。

🧩 模型結構與量化,三種形態疊在一起

Qwen3.6-35B-A3B總共儲存350億參數,但每個token只啟用約30億。一個router會在256個expert中評分並挑出8個,再加上一個對每個token都生效的shared expert。同時,模型混合了10層full-attention(GQA,16個query head、2個KV head)與30層Gated DeltaNet。這意味著Lily要同時處理三種截然不同的運算形態:大小不均的expert分組、隨著KV cache成長的attention,以及固定大小的recurrence。

checkpoint使用groupwise affine 4-bit量化,每64個權重共用一組bfloat16的scale與bias,原本約70GB的bfloat16權重被壓縮到19.4GB。但Metal 4的tensor運算只吃bfloat16,權重必須先被還原。Lily的做法是在grouped GEMM內部逐個tile還原,結果暫存在threadgroup記憶體,並以FP32累加,展開後的完整陣列從頭到尾不會進入unified memory。

📊 一連串kernel最佳化的實測收益

| 最佳化項目 | 場景 | 效能提升 |
|---|---|---|
| dequant融合進grouped GEMM | 512-token prompt prefill | +77.4% |
| routing histogram/prefix scan/scatter/block map塞進單一GPU command buffer | 512-token prefill | +89% |
| tile從16-row換成32-row、四個simdgroup | 2K prefill | +13.2% |
| register-resident Gated DeltaNet scan | — | +5.6% |
| GQA packing(4個query head共用一個threadgroup) | 32K decode | +23.8% |
| 固定區塊attention layout | 32K / 64K / 128K decode | +7.7% / +27.4% / +40.2% |

expert GEMM約佔prefill時間的90%,長prompt會以固定大小的chunk處理,避免暫存activation跟權重、cache搶記憶體。batch-1 decode幾乎沒有權重重用,頻寬因此成為天花板;coalesced cache讀取把key頻寬從33.8提升到47.9 GB/s、value頻寬從42.0提升到61.8 GB/s。文章還提到,原本一個decode step會launch 795個kernel、形成555個循序階段,Lily改用concurrent Metal pass記錄真實的依賴關係,讓彼此獨立的kernel可以重疊執行,並把選出的token直接寫進下一步GPU-resident的輸入槽,省掉每個token一次的CPU往返。

在一臺40核心、128GB記憶體的M5 Max上,batch為1,涵蓋256到128K共十組長度,Lily平均prefill達4,156 tokens/s(MLX-LM為3,388,約1.23倍),decode達170.0 tokens/s(MLX-LM為126.4,約1.35倍)。在4K prompt、4K context這一組,Lily是5,749.9與186.6 tokens/s,對比MLX-LM的4,737.5與140.9;整體上prefill在1.12至1.42倍之間、decode在1.31至1.37倍之間都領先。一項192個位置的teacher-forced檢查顯示,Lily的perplexity只高0.04%,top-ranked token與MLX-LM一致的比例達96.35%。

⚠️ 窄到只服務一顆模型

Lily的效能建立在犧牲通用性之上:目前只支援Qwen3.6-35B-A3B與Apple Silicon這一種組合,4-bit checkpoint本身就有19.4GB,官方建議至少32GB unified memory才能穩定運作(產品面則列出24GB為最低門檻)。這不是一個可以直接套用到其他模型或其他硬體的推理框架。

🎯 實務啟示

如果你的部署場景高度固定,例如單一模型、單一硬體家族,Lily示範了放棄通用性、把架構與kernel寫死能拿到多少效能。pplx-garden已經公開了一個standalone demo,提供最基本的greedy生成與OpenAI相容API,有興趣在Apple Silicon上做本地推理的工程師可以直接拉下來跑。

🔗 來源
- 標題:Perplexity Open Sources Lily: A Rust + Metal Inference Engine for Qwen3.6-35B-A3B on Apple Silicon
- 作者/機構:Asif Razzaq / MarkTechPost
- 連結:https://www.marktechpost.com/2026/09/02/perplexity-open-sources-lily-a-rust-metal-inference-engine-for-qwen3-6-35b-a3b-on-apple-silicon/

#Perplexity #Rust #Metal #AppleSilicon #LLMInference #Qwen #MoE #GPUOptimization #EdgeAI #OpenSource
