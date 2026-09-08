---
title: NVIDIA Announces CUDA Rust with cuda-oxide (SIMT) and cutile-rs (Tile) for
  Compile-Time-Safe GPU Kernels
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/08/nvidia-announces-cuda-rust-with-cuda-oxide-simt-and-cutile-rs-tile-for-compile-time-safe-gpu-kernels/
model: claude-code/sonnet
generated_at: '2026-09-08T20:07:46.905413'
score: 91
---

📌 同一個記憶體錯誤，兩種編譯期報錯：CUDA Rust 的安全承諾差在哪

TL;DR：NVIDIA 用 Rust 的所有權規則讓 GPU kernel 的別名錯誤在編譯期就被擋下，其中 cutile-rs 已進入實際專案，cuda-oxide 仍是早期 alpha。

把 SIMT kernel 輸出的 buffer，同時當成自己的輸入傳進去，在 cuda-oxide 裡會得到 `error[E0502]: cannot borrow c_dev as mutable because it is also borrowed as immutable`；在 cutile-rs 的 Tile 版本裡做同樣的事，得到的是 `error[E0382]: use of moved value`。兩個都是編譯期就攔下的別名（aliasing）錯誤，但背後的保護強度並不一樣。

🤔 GPU kernel是Rust系統層最後的缺口

NVIDIA 宣布 CUDA Rust，目標是讓 Rust 成為寫 GPU kernel 的一級語言。過去 Rust 程式碼已經可以啟動 CUDA kernel，但 kernel 本體通常得用其他語言寫。AI 的系統層，從推論引擎到驅動程式和 agent runtime，正越來越多用 Rust 撰寫：NVIDIA 的 Nova Linux driver 用 Rust 寫成，NVIDIA Dynamo 有 Rust core，NVTX 也提供 Rust bindings，GPU kernel 一直是唯一的例外。CUDA Rust 透過兩個 NVlabs 開源專案補上這塊：對應 SIMT 模型的 cuda-oxide，以及對應 Tile 模型的 cutile-rs，兩者都能原生編譯 Rust kernel，並利用 Rust 的所有權規則在編譯期擋下別名錯誤。

🧩 兩種所有權保護，強度不同

cuda-oxide 是自訂的 rustc codegen backend，把 `#[kernel]` 函式一路經過 Rust MIR、Pliron IR framework、LLVM IR 編譯到 PTX，其餘程式碼交給標準 backend。安全性寫在 kernel 簽名裡：輸入 `a`、`b` 是一般共用 slice，輸出 `c` 則是 `DisjointSlice<f32>`，讓每個 thread 只拿到自己那格的獨佔存取權——因為普通的 `&mut [f32]` 會要求每個 thread 持有同一個可變借用，這在 Rust 裡本來就不合法。`c.get_mut(idx)` 回傳 `Option`，越界存取因此變成要處理的分支而非記憶體錯誤。`#[launch_contract]` 屬性宣告了區塊形狀，產生出來的 `prepare_vecadd` 方法會在安全的啟動流程執行前，拿實際的 launch 設定去對照這份宣告做驗證。

cutile-rs 則工作在更高一層，每個 tile block 把 kernel body 當作單一邏輯 thread，在一整個子張量上執行一次，實際要用多少 GPU thread 由編譯器決定。host 端呼叫的 `.partition([128])` 一次做三件事：讓每個 tile 對自己的 128 個元素區塊有獨佔所有權、把 grid 固定成 1024/128=8 個 tile、並提供常數 tile 寬度。輸入張量可以用 -1 表示由啟動時決定的動態維度，而且在 `.sync_on(&stream)` 之前不會有任何東西真正執行，之前的呼叫都只是記錄在同一條鏈上的延遲描述。

NVIDIA 表示，cuda-oxide 是在每次啟動呼叫（launch call）時做檢查，而 cutile-rs 的所有權則是跨越啟動邊界、一路跟著張量走，這也是 NVIDIA 所稱「更強的保證」。Tile 這一側完全不對外暴露 shared memory 或 thread indexing 讓人誤用；SIMT 保留了這些控制權，但目前在 cuda-oxide 裡使用 shared memory 需要 unsafe。

⚠️ 能不能真的拿去部署：兩個專案進度不一樣

cutile-rs 已經發佈在 crates.io 上，可在 stable Rust 1.89 以上執行，且已經被用在 Hugging Face 的 Grout 推論引擎和 mistral.rs 裡。cuda-oxide 目前仍是早期 alpha，兩個專案都還沒被確認可用於生產環境。環境需求也差很多：cuda-oxide 需要 Linux、compute capability 8.0 以上的 GPU、CUDA 12.x 以上、含 libclang 的 clang，以及被釘死的 nightly toolchain；cutile-rs 只需要 compute capability 8.0 以上、CUDA 13.3、stable Rust 1.89 以上與 Linux，不需要 nightly，也不用自備 LLVM。

🎯 實務啟示

如果你現在就想在專案裡用 Rust 寫 GPU kernel，cutile-rs 因為已有 Hugging Face Grout、mistral.rs 這類實際使用案例、且跑在 stable Rust 上，是風險較低的起點；cuda-oxide 提供的細粒度 thread／記憶體控制更貼近傳統 SIMT 開發習慣，但目前仍是 alpha 階段，要有踩坑的心理準備。

🔗 來源
- 標題：NVIDIA Announces CUDA Rust with cuda-oxide (SIMT) and cutile-rs (Tile) for Compile-Time-Safe GPU Kernels
- 作者／機構：Asif Razzaq／MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/08/nvidia-announces-cuda-rust-with-cuda-oxide-simt-and-cutile-rs-tile-for-compile-time-safe-gpu-kernels/

#CUDA #Rust #GPUProgramming #MemorySafety #NVIDIA #OwnershipModel #Compilers #OpenSource #HuggingFace #SystemsProgramming
