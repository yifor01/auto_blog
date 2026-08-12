---
title: 'Open-sourcing Metals v2: Databricks’ Java and Scala language server for multi‑million
  line codebases'
source: Databricks
url: https://www.databricks.com/blog/open-sourcing-metals-v2-databricks-java-and-scala-language-server-multi-million-line-codebases
model: claude-code/sonnet
generated_at: '2026-08-12T07:35:33.389405'
score: 90
---

📌 26M 行 monorepo 也能秒開：Databricks 開源 Metals v2 語言伺服器

TL;DR：Databricks 開源 Metals v2，把 Scala 語言伺服器擴充成支援 Java 的大型 monorepo 導航利器。

當「大部分程式碼由 agent 撰寫」成為常態，工程師手動開 IDE 的場景反而更看重一件事：打開一個數千萬行的 monorepo 後，多快能開始有效導航？Databricks 這篇文章詳細拆解了他們如何為此重寫 Metals 語言伺服器的三層核心架構。

🤔 **IntelliJ 撐得住規模，但團隊想換掉它**

Databricks 自 2025 年 5 月起將日常編輯器工作流標準化到 Cursor，Cursor 與 VS Code 在前端與非 JVM 程式碼上已被廣泛使用，且對雲端開發環境有良好的 SSH remote 支援。唯一的例外是 Scala 與 Java：在 Databricks monorepo 的規模下，過去唯一撐得住的編輯器是 IntelliJ。文章指出，因為現在大部分程式碼由 agent 撰寫，「快速掌握程式碼結構」比「完整的 LSP 補全與重構功能」更重要，這也重新定義了問題的優先順序。

🧩 **三層重寫：repo index、編譯器 pipeline、build 整合邊界**

團隊從 Metals v1 出發，重寫了三個核心層：

- **mbt 索引（Metals Build Tool index）**：一個內容定址（content-addressed）的工作區原始碼索引，用 `git ls-files --stage` 與 Git blob OID 判斷哪些索引項目可以重用。每個項目記錄檔案的 package 宣告、定義位置，以及用於快速篩掉不相關檔案的 compact bloom filter，讓 Metals 在 build 同步完成前就能回答符號搜尋與跳轉定義等「第一哩路」問題。
- **Scala／Java 編譯器 pipeline**：核心是 presentation compiler，一種會快取並重用符號表資訊的 Scala 型別檢查模式。它有兩種運作模式：build 同步前用「寬鬆」的 fallback compiler，把倉庫中所有原始碼都視為候選依賴，讓導航在程式碼尚未能編譯時也能運作；build 同步後切換成「精確」compiler，依 build server 回報的 classpath／sourcepath 邊界限縮範圍，讓診斷與依賴資訊與 build 結果一致。
- **build 整合邊界**：讓上述兩種模式能無縫切換，是達成「開啟即可用」承諾的關鍵環節。

📊 **關鍵數字**

| 指標 | 數值 |
|---|---|
| mbt 索引大小 | 936MB（未壓縮） |
| 索引涵蓋 | 290 萬個符號、超過 14.2 萬個 Scala／Java／Protobuf 檔案 |
| 索引 clean build | 32 核心全速下 22 秒 |
| 從磁碟解析已建索引 | 5 秒 |
| Time-to-Initial-Intelligence (TTII) | p50 8.7 秒，p90 36.7 秒 |
| 工作區符號模糊搜尋（290 萬符號） | p50 10ms，p90 95ms |
| Scala 診斷發布延遲（24M 行 Scala 程式碼） | p50 0.9 秒，p90 8.9 秒 |
| 週活躍 IDE 使用者（截至 2026 年 7 月） | Cursor 92% vs. IntelliJ 12% |
| 僅用單一 IDE 的工程師人數 | Cursor 2.4k vs. IntelliJ 120 |
| Scala／Java 檔案開啟事件中 Cursor 佔比 | 2025 年 10 月起從 40% 升至 78% |

⚠️ **取捨：犧牲部分 LSP 完整度換取啟動速度**

文章坦言，把「快速掌握程式碼結構」定為優先目標後，問題確實被縮小了，但並沒有讓解法變得顯而易見——他們仍必須為一個這麼大的 Scala／Java Bazel monorepo，從零打造出低延遲、易安裝的導航能力，因為現成的 LSP 方案並不是為這種規模設計的。

🎯 **實務啟示**

Metals v2 現已在 Cursor、VS Code、Neovim 中提供，安裝說明可在 Metals 官網取得，後續開發由 VirtusLab 主導。如果你的團隊維護大型 JVM monorepo、正苦於 IntelliJ 啟動與索引速度，或是想擺脫對單一重量級 IDE 的依賴，Metals v2 提供了一條有實測數據支撐、且已在生產環境驗證過的替代路徑；其 mbt 索引與雙模式編譯器的設計思路，也值得作為自建大型程式碼庫工具鏈時的參考架構。

🔗 **來源**
- 標題：Open-sourcing Metals v2: Databricks' Java and Scala language server for multi‑million line codebases
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/open-sourcing-metals-v2-databricks-java-and-scala-language-server-multi-million-line-codebases

#Metals #Scala #Java #LanguageServer #LSP #Databricks #DeveloperTools #Cursor #Monorepo #OpenSource
