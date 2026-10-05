---
title: Mold Linker Version 3.0.0 Release – Rewritten in Rust
source: Hacker News
url: https://github.com/rui314/mold/releases/tag/v3.0.0
model: claude-code/sonnet
generated_at: '2026-10-05T23:31:36.009966'
score: 67
---

📌 高速連結器 mold 3.0：從 C++ 全面改寫成 Rust

TL;DR：mold linker 的首個 Rust 版本正式發布,效能維持不變,相容性朝 GNU ld 再靠近一步。

一個以「快」聞名的連結器,為什麼要冒著效能風險把整套 C++ 程式碼重寫成 Rust?mold 3.0.0 的發布說明給出了答案:這不是為了炫技,而是為了讓專案能走得更遠。

🤔 **mold 的目標：取代 GNU ld 成為 Linux 預設連結器**

mold 是知名的高速連結器（linker）。根據發布說明,mold 2.42.1 是 C++ 版本的最後一版,而 3.x 系列的目標是補齊與 GNU ld 之間剩餘的相容性缺口（特別是 linker script 支援）,並為 mold 成為 Linux 發行版預設連結器鋪路。要達成這個目標,專案選擇了一條大膽路線:整個重寫成 Rust。

🧩 **「Drop-in replacement」：命令列、架構、輸出都不變**

mold 3.0 被定位為 2.42.1 的 drop-in replacement（直接替換）：接受相同的命令列選項,支援相同的目標架構,產出相同的輸出內容（除了本版修復的錯誤）。連結效能也與 2.42.1 相當。作者團隊表示,他們在所有支援的目標架構上執行測試套件,比對大量真實世界工作負載與選項組合下的連結器輸出,並建置了所有 Gentoo 套件,結果沒有發現回歸（regression）。

改寫成 Rust 帶來的額外好處是記憶體安全:面對損壞的輸入檔案,C++ 版本可能發生記憶體越界讀取而直接 segfault；Rust 版本因為有邊界檢查,遇到同樣的錯誤存取會改以 panic 的方式停止,而不是未定義行為的崩潰。

建置方式也因此改變:mold 現在用 Cargo 取代 CMake 建置,需要 Rust 1.95 以上版本與一個 C 編譯器,執行 `cargo build --release` 建置、`./install-mold.sh` 安裝（支援 PREFIX 與 DESTDIR 參數）。CMake 的選項全數移除,原本的 MOLD_TARGETS CMake 變數改為 Cargo features。它不再依賴 oneTBB,但仍靜態連結 mimalloc 3.5.3（可用 `--features system-allocator` 改用系統 malloc）,並視系統是否有 zlib 決定是否連結系統版本,同時內建 zstd 與 BLAKE3。測試套件也從 ctest 改為 `cargo test`。

📊 **一長串的 bug 修復與架構支援擴充**

除了語言遷移,這個版本也修了相當多邊緣案例,例如:使用 version script 或 `--default-symver` 建立靜態連結執行檔時的崩潰；輸出檔案同時是輸入檔案時（`mold -r -o foo.o foo.o bar.o`）的崩潰或輸出損壞；`--gc-sections` 誤刪 `--init`/`--fini` 指定函式的問題；以及多項在 AArch64、ARM32、RISC-V、LoongArch、PPC32/64、m68k、SH4 等架構上的 relocation 修正。另外,mold 不再於啟動時保留 8 GiB 虛擬位址空間,因此可以在 `ulimit -v` 限制下正常運作。

💡 **為什麼這個重寫值得注意**

對連結器這種工具鏈底層基礎設施而言,「效能不退步、相容性變好、記憶體安全變強」是很難同時滿足的三個目標。mold 團隊選擇用 Rust 的邊界檢查取代 C++ 手動記憶體管理,換來的是面對惡意或損壞輸入時更可預期的失敗模式（panic 而非未定義行為）,這對被整合進編譯器工具鏈、CI 系統的基礎工具來說是實質的風險降低。

⚠️ **升級前需注意建置流程的變動**

如果你是自行從原始碼建置 mold 的使用者,升級到 3.0 需要改用 Cargo 工具鏈,並重新確認 MOLD_LIBDIR 等環境變數設定（若將函式庫安裝在非預設路徑,如 `/usr/lib64`）。這對仰賴既有 CMake 建置腳本的發行版維護者來說,是需要額外投入的遷移成本。

🎯 **給工程師的啟示：工具鏈的語言遷移是可行路徑**

mold 3.0 的案例提供了一個具體範本:效能敏感的底層基礎設施,也可以在不犧牲效能與相容性的前提下,逐步從 C++ 遷移到 Rust。如果你的團隊在維護類似的系統工具,這份發布說明中詳盡的相容性驗證方法（跨架構測試、真實世界套件建置比對）值得參考。

🔗 **來源**
- 標題：Mold Linker Version 3.0.0 Release – Rewritten in Rust
- 作者／機構：rui314（Hacker News 轉載 GitHub Release）
- 連結：https://github.com/rui314/mold/releases/tag/v3.0.0

#Rust #Linker #SystemsProgramming #OpenSource #CompilerToolchain #MemorySafety #Linux #DevTools #PerformanceEngineering #GitHub
