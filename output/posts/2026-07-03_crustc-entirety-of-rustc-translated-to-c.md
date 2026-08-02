---
title: 'crustc: entirety of `rustc`, translated to C'
source: Hacker News
url: https://github.com/FractalFir/crustc
score: 89
model: google/gemma-4-31b-it:free
generated_at: '2026-07-03T19:57:22.514475'
---

📌 將整個 `rustc` 翻譯成 C：4,600 萬行程式碼的極端實驗

TL;DR：開源專案 `crustc` 將 Rust 編譯器轉譯為 C 語言，讓你能用 GCC 編譯出一個可執行的 Rust 編譯器。

如果一個用 Rust 寫的編譯器，可以被轉譯成 C 語言，然後再用 GCC 編譯回來，這會發生什麼事？這不僅僅是一個技術挑戰，更是一場關於轉譯規模的極端實驗。

🧩 **將 1.98.0-nightly 轉譯為 4,600 萬行 C 程式碼**

`crustc` 是一個功能完備的 Rust 編譯器，其核心特點在於它並非用 Rust 撰寫，而是將 `rustc 1.98.0-nightly` (版本號 c712ea946) 的全部內容轉譯成 C 語言。

這個過程產生了高達 4,600 萬行的 C 程式碼。作者 Philpax 指出，這其實是他開發的一套名為 `cilly` 的 Rust-to-C 編譯工具鏈的展示 Demo。這套 `cilly` 工具鏈能夠將 Rust 程式碼轉譯為 C，且支援任意目標平臺（arbitrary targets）。

🛠️ **如何構建與執行這個「C 版 Rust 編譯器」**

根據 README，這個專案可以直接使用 GCC 與 make 進行構建。由於 `rustc` 依賴 LLVM，使用者需要提供 LLVM 函式庫的路徑。

構建與執行的基本流程如下：
1. **編譯**：使用 `make` 並指定 `LLVM_LIB_DIR` 指向對應的 LLVM 函式庫路徑（例如 `libLLVM.so.22.1-rust-1.98.0-nightly`）。
2. **執行**：設定 `LD_LIBRARY_PATH` 以便在執行時能找到 LLVM 函式庫，隨後即可執行 `./rustc/rustc`。

作者宣稱該編譯器是可執行的（functional），能夠編譯一般的 Rust 程式碼，包括 `core`、`alloc` 以及 `std` 等核心函式庫。

🎯 **實務啟示：轉譯工具鏈的可能性**

雖然將編譯器轉譯成 4,600 萬行 C 程式碼在日常開發中沒有直接用途，但它證明了 `cilly` 工具鏈在處理大規模複雜專案時的轉譯能力。對於工程師而言，這提供了一個思考方向：將高階語言轉譯為 C 語言，能讓程式碼在缺乏原生語言支援的環境中，只要有 C 編譯器就能執行。

🔗 **來源**
- 標題：crustc: entirety of `rustc`, translated to C
- 作者／機構：Philpax
- 連結：https://github.com/FractalFir/crustc

#Rust #C #Compiler #rustc #LLVM #GCC #Transpiler #OpenSource #ProgrammingLanguages #SystemsProgramming
