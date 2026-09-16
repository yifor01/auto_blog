---
title: Translating CUDA Tile Operations from Python to Rust Using Agentic AI
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/translating-cuda-tile-operations-from-python-to-rust-using-agentic-ai/
model: claude-code/sonnet
generated_at: '2026-09-16T20:15:39.941383'
score: 100
---

📌 用Agentic AI把CUDA Tile Kernel從Python搬到Rust，效能只掉0.5%

TL;DR：NVIDIA用多agent pipeline將24個TileGym kernel從Python移植到Rust，效能達99.5%。

一套累積了大量生產級kernel的CUDA函式庫，要換一種程式語言重寫，通常意味著大量人工、大量bug，以及效能倒退的風險。NVIDIA團隊反其道而行：建了一個agent skill，讓AI agent自己完成從cuTile Python搬到cuTile Rust的轉譯工作，而且轉出來的kernel平均效能只比原本少0.5%。

🤔 **JIT的隱式特化，遇上Rust的顯式宣告**

cutile-rs（cuTile Rust）是一套在Rust中撰寫GPU kernel的tile-based系統，把Rust的ownership模型延伸到tile運算，將可變輸出切成互不重疊的區塊，並在host端跨kernel launch維持ownership契約，同時允許開發者在需要更底層控制時局部退出、直接操作Tile IR。

TileGym這個CUDA tile kernel函式庫已經累積大量用cuTile Python與Triton-TileIR寫成的生產kernel，NVIDIA團隊希望這些kernel在Rust中也能用。轉譯的主要難題在於：cuTile Python的JIT編譯器會在呼叫當下隱式地為每個kernel做特化，而Rust要求你在kernel簽名中明確宣告每一種特化情境。舉例來說，Python裡未走到的if ct.Constant分支在編譯前就會被丟棄，但在Rust中兩條分支都必須通過型別檢查；一個Python kernel因此可能拆成多個結構不同的Rust entry（例如layer_norm會因為分支改變tile rank，拆成2-D的nchw與1-D的w1兩個entry）。

🧩 **每個轉譯階段都有機器可驗證的判定**

三種前端（cuTile Python、Triton-TileIR、cuTile Rust）其實都是同一份CUDA Tile IR（cuda_tile dialect）的表層語法，最終都餵給同一個tileiras編譯器，產出相同的GPU binary。這個共享的IR基礎讓轉譯不是「重新最佳化」的問題，而是「用更安全的host語言重新表達同一個tile程式」，底層編譯器與效能模型完全相同。

正因為三種前端輸出同一種dialect，一次忠實的移植應該重現參考kernel的IR結構：相同的memory-op家族、相同的tile shape、相同的reduction。團隊因此可以直接把參考kernel與轉譯後kernel的Tile IR dump出來做diff，在跑任何測試之前就先結構性地驗證正確性——這能抓出「看似正確但實際有問題」的轉譯，例如TMA load用錯cost hint，或漏掉divisibility屬性；這類問題可能通過功能測試，卻在測試覆蓋不到的地方造成效能退化。

整個轉譯流程是一個有邊界的多agent pipeline，依序涵蓋分析、device kernel撰寫、host與FFI程式碼、以及benchmark，每個階段都由validator script與Tile IR diff給出可機器判讀的結果，決定是否放行進入下一階段。文章以softmax kernel為例，逐行對照展示cuTile Python中的ct.load、ct.max、ct.exp等操作，如何對應成Rust中的make_partition_view、reduce_max、exp等呼叫，兩者結構幾乎一一對應，這正是因為兩種前端都只是同一組Tile IR操作的薄層介面。

📊 **24個算子、約40個kernel，效能達99.5%**

團隊用這套skill把全部24個公開的TileGym算子（合計約40個GPU kernel，涵蓋element-wise運算到flash-attention decode、Multi-head Latent Attention（MLA）、mixture-of-experts（MoE）等）移植到cuTile Rust，平均達到cuTile Python效能的99.5%。

⚠️ **顯式化不是免費的，安全網也要另外補**

除了branch必須全部型別檢查外，任何dtype組合在Python中可即時編譯，但在Rust中FFI要透過固定的symbol/dtype table分派，代表新增一種dtype支援是明確的ABI擴充工作（範例中共用的table涵蓋f32/f16/bf16/i32/i64/f8e5m2/f8e4m3fn）。另外，Python的型別系統原本兼任輸入驗證，但跨過C ABI之後就沒有安全網，一個錯的stride可能造成靜默的記憶體損毀而非丟出例外，團隊為此在Python wrapper加上語意檢查，並在FFI背後加上帶命名回傳碼的ABI檢查（null/dtype/device）作為兩層防護。

🎯 **實務啟示**

這個案例示範了agentic AI在「跨語言移植底層系統程式碼」這種高風險任務上的可行做法：關鍵不是讓agent一次生成完美程式碼，而是把每個轉譯階段都綁定一個機器可驗證的判定（IR diff、functional test、benchmark），讓agent的輸出可以被結構性地審查，而不只是靠通過測試來背書。這套skill已隨TileGym repo釋出，工程師可以直接套用在自己的kernel移植工作上。

🔗 **來源**
- 標題：Translating CUDA Tile Operations from Python to Rust Using Agentic AI
- 作者／機構：Tanya Lenz, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/translating-cuda-tile-operations-from-python-to-rust-using-agentic-ai/

#CUDA #Rust #GPU #AgenticAI #NVIDIA #TileGym #CompilerEngineering #SystemsProgramming #GPUKernel #Triton
