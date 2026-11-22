---
title: 'Fast-Anything: Don''t rewrite it in Rust. Rewrite the 5% that''s slow'
source: Hacker News
url: https://github.com/EL4CTEO/fast-anything
model: claude-code/sonnet
generated_at: '2026-11-22T22:38:41.550512'
score: 88
---

📌 不重寫全部成 Rust，只動效能熱點那 5%

TL;DR：開源工具 fast-anything 自動找出拖慢程式的函式，請 coding agent 搬到 Rust，並用真實呼叫紀錄驗證無誤後才切換上線。

把整個應用程式重寫成 Rust，聽起來很美好,但換來的常是數個月的工期、動輒上分鐘的編譯時間，以及一個佔滿硬碟的 target/ 資料夾。而多數時候，真正拖慢程式的只是少數幾個函式。fast-anything 的切入點很直接：既然 runtime 大部分時間都花在少數函式上，那就只動那一小塊。

🤔 **為什麼不整包重寫**

作者指出三個代價：編譯時間（整包重寫動輒數分鐘，單函式 crate 只要幾秒）、快取管理（整包重寫的 build cache 龐大難管理）、以及風險（原始程式碼大範圍改動，出錯難追查）。fast-anything 的設計哲學是讓 Rust 的導入變成「逐函式、可驗證、可逆」的操作，而不是一次性的豪賭。

🧩 **掃描、移植、驗證、再啟用的四步流程**

工具的核心流程拆成幾個指令：
- `scan` 先對整個程式 profiling，依「耗時 × 可移植性」排序出最值得搬的函式。
- `port` 記錄該函式最多 500 次真實呼叫，自動生成一個單函式的 Rust crate 以及一份 TASK.md，交給 coding agent（支援 `--agent claude`、`codex` 或任何讀 stdin 的 agent）動手改寫。
- `verify` 用 release build 重新編譯 Rust 版本，並把所有錄到的呼叫一一回放比對結果。除此之外，它還會從錄到的呼叫自動衍生邊界案例（NaN、正負無限大、-0.0、非 ASCII 文字、放大 16 倍或清空的輸入）與縮減案例（極小與隨機切片），交給原始函式當作「正確答案」比對。只要數值不在 1e-9 誤差內吻合，或者該丟錯誤卻沒丟，整個 port 都不會被啟用。連「Rust 版本是對的但比原本還慢」（呼叫 Rust 的開銷大於省下的運算）這種情況也不會被啟用。
- `enable` / `disable` 則是用一段標記好的區塊，位元組級別地切換要不要用 Rust 版本，隨時可以用環境變數 `FAST_ANYTHING_DISABLE=1` 強制跑回原始邏輯。

這個驗證機制本身也抓到過真實的 bug：README 提到有個移植版本「看起來沒問題」，實際上是把 byte 比對錯當成字元比對，500 次錄到的真實呼叫裡有 148 次就抓到了這個落差。

📊 **多語言實測倍數**

README 列出在 i5-10500 / Windows 11（C 與 C++ 則用 4 核心的 GitHub Actions Linux runner）上的實測結果：

| 應用（語言） | 移植前 | 移植後 | 倍數 |
|---|---|---|---|
| Python 模糊去重複（700 筆姓名） | 4.91s | 42ms | 116× |
| TypeScript 模糊去重複（2,000 筆） | 3.11s | 155ms | 20× |
| PHP 模糊去重複（600 筆） | 2.94s | 53ms | 55× |
| Go 模糊去重複（3,000 筆） | 3.02s | 144ms | 21× |
| Ruby 模糊去重複（400 筆） | 3.13s | 228ms | 14× |
| C# 模糊去重複（4,000 筆） | 4.03s | 312ms | 13× |
| Java 模糊去重複（4,000 筆） | 3.50s | 1.18s | 3×（函式本身 11×，其餘是 JVM 啟動時間） |
| C 曼德博集合（8 個縮放層級） | 431ms | 127ms | 3.4× |
| C++ 模糊去重複（6,000 筆） | 3.02s | 1.09s | 2.7× |

作者特別提到一個設計細節：fast-anything 會選擇移植「最外層」可移植的迴圈，而不是裡面被呼叫上百萬次的小函式，這樣整個程式只需要跨越一次 Rust 邊界，而不是每次迴圈都跨越一次。README 提到若只移植最內層的 levenshtein 函式，同一個案例的倍數會從 116× 掉到 35×，從 55× 掉到 1.9×。

🧰 **支援的語言與整合方式**

目前支援 Python、JavaScript/TypeScript（Node、Bun、Deno）、Ruby、Java、Kotlin/JVM、Go、PHP、C/C++、C#/.NET，透過 PyO3、napi-rs 或統一的 C ABI + JSON 橋接。除了 CLI，也提供 Claude Code plugin、內建的 MCP server（含 `fast_scan`、`fast_port`、`fast_verify` 等 8 個工具），以及教 agent 跑完整流程的 skill。

⚠️ **能移植什麼，不能移植什麼**

fast-anything 只處理「頂層、確定性（deterministic）、吃一般資料（數字、字串、list、dict、typed array 等）」的函式，包括放在 `if __name__ == "__main__":`（或各語言對應寫法）下的程式碼。SYCL kernel 跑在裝置上不會被移植；用 `-fsycl` 編譯時只有 host 函式會被 profiling 和移植。`scan` 指令會說明哪些函式暫時無法移動的原因。

🎯 **實務啟示**

對已經在維運的專案來說，這種「只動 5%、全程可驗證、隨時可退回」的做法，比起全面重寫 Rust 更貼近實際工程決策:風險集中在單一函式、而不是整個程式庫，而且驗證流程把「這段改寫有沒有改變行為」這個最怕出錯的問題，變成自動化、有真實呼叫紀錄背書的步驟。對效能瓶頸明確、但沒有餘力做大改版的團隊，這類工具值得放進 CI 或 PR 流程試試。

🔗 **來源**
- 標題：Fast-Anything: Don't rewrite it in Rust. Rewrite the 5% that's slow
- 作者／機構：BaselAshraf81（Hacker News 貼文）
- 連結：https://github.com/EL4CTEO/fast-anything

#Rust #PerformanceEngineering #CodingAgent #OpenSource #FFI #DevTools #Python #Optimization #SoftwareEngineering #LLMAgent
