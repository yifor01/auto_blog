---
title: 'Introducing CUDA Rust: Two Tracks for Writing GPU Kernels'
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/
model: claude-code/sonnet
generated_at: '2026-09-08T20:07:46.905087'
score: 93
---

📌 GPU 核心終於能用純 Rust 寫：NVIDIA CUDA Rust 雙軌上路

TL;DR：NVIDIA 推出 CUDA Rust，讓 GPU kernel 能用原生 Rust 編譯到 PTX，補上 Rust 在 AI 系統層唯一還沒覆蓋的一塊。

Nova Linux driver 是 Rust 寫的，NVIDIA Dynamo 有 Rust core，NVTX 也提供 Rust bindings。但如果你想寫一個真正在 GPU 上跑的 kernel，Rust 到目前為止只能負責「呼叫」，實際執行的程式碼還是得交給別的語言。NVIDIA 這次要補的，正是這個缺口。

🤔 為什麼系統層都在往 Rust 靠攏，kernel 卻是例外

AI 的系統層，包括推論引擎、serving 基礎設施、驅動程式、agent runtime，都在隨著模型與技術快速變動，而 Rust 能在編譯期擋下一整類 bug，又不用犧牲效能，因此越來越多這類程式碼改用 Rust 撰寫。NVIDIA 這次跟進同一個理由：你可以用 Rust 啟動 CUDA kernel，但 kernel 本體通常還是得用其他語言寫。CUDA Rust 讓 kernel 也能原生用 Rust 寫成，並直接編譯到 PTX，而不是包一層別的語言。

🧩 兩條路徑，對應 CUDA 既有的兩種程式設計模型

CUDA Rust 分成兩個專案，剛好對應 CUDA C++／CUDA Python 已有的兩種模型：

- **SIMT（cuda-oxide）**：你描述「一個 thread」要做什麼，然後啟動成千上萬個 thread，這是 CUDA C++ 或 numba-cuda 使用者熟悉的寫法。
- **Tile（cutile-rs）**：你描述「一個 tile」的資料要做什麼，thread 怎麼映射到硬體交給 Tile IR 編譯器決定，程式碼因此不會綁死特定架構的選擇。

NVIDIA 建議優先考慮 Tile，只有在需要精細控制 thread、記憶體時才下探到 SIMT。選哪種語言（Rust、C++、Python）則是另一個獨立的問題，NVIDIA 也提到未來規劃跨語言互通（inter-language interop），所以選了 Rust 並不會把你鎖死在其他語言之外。

cuda-oxide 是一個自訂的 rustc codegen backend，會攔截編譯流程，把標記 `#[kernel]` 的函式一路經過 Rust MIR、社群的 Pliron IR framework、LLVM IR，最後編譯成 PTX，其餘程式碼則照常交給標準 backend 處理。GPU 相關的 dialect 是 NVIDIA 疊在 Pliron 上寫的，整條 transform 鏈在進入標準 LLVM backend 之前都留在 Rust 世界裡。

cutile-rs 則工作在更高一層。`#[cutile::module]` 巨集會把 kernel 的 AST 嵌進 host 執行檔，等第一次真正呼叫該 kernel 時，才透過 CUDA Tile IR 做 JIT 編譯。

🔒 安全性寫在 kernel 簽名裡

以文中示範的向量加法為例，`a`、`b` 是一般的共用 slice，可以被每個 thread 讀取；輸出 `c` 則是型別為 `DisjointSlice<f32>`，讓每個 thread 只能拿到自己那格元素的獨佔存取權。這是必要設計，因為一般的 `&mut [f32]` 會要求每個 thread 持有同一個可變借用，這在 Rust 裡本來就過不了關，`DisjointSlice` 把這一個可變借用拆成每個 thread 各自獨立的一小塊。`thread::index_1d()` 回傳的是專屬的索引型別而非單純整數，`c.get_mut(idx)` 也只接受這個型別，回傳的是 `Option`，越界存取因此變成你要處理的分支，而不是日後才發現的記憶體錯誤。

啟動流程也被檢查而非單純信任：`#[launch_contract]` 宣告了這個 kernel 用一維索引、256-thread 的區塊配置，`prepare_vecadd` 會拿你傳入的 `LaunchConfig1D` 對照這份宣告與裝置的實際限制做驗證，通過後才產生安全版 `vecadd` 方法所需要的「證明」。沒有宣告 contract 的 kernel，就只能用未受保護的 unsafe 啟動方法。

⚠️ 目前的門檻

要跑 cuda-oxide，需要 Linux、compute capability 8.0 以上的 GPU、CUDA 12.x 以上、含 libclang 的 clang，以及被釘死版本的 nightly toolchain（nightly-2026-04-03），`cargo oxide doctor` 可以幫你檢查整套環境；第一次 `cargo oxide run` 因為要建置 codegen backend，會花比較久時間，之後會用快取加速。

🎯 實務啟示

如果你的系統層已經是 Rust 堆疊，CUDA Rust 讓你不用再為了 kernel 而切語言。實務上先從 Tile 開始（cutile-rs 的環境需求也輕得多，不需要 nightly、也不用自備 LLVM），只有在真的需要手動管理 thread 與記憶體時，才考慮走 SIMT 路線的 cuda-oxide。

🔗 來源
- 標題：Introducing CUDA Rust: Two Tracks for Writing GPU Kernels
- 作者／機構：Elizabeth Goodman／NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/

#CUDA #Rust #GPU #NVIDIA #SystemsProgramming #ParallelComputing #PTX #MemorySafety #GPUKernel #Compilers
