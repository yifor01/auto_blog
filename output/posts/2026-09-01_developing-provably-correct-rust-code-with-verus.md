---
title: Developing provably correct Rust code with Verus
source: Amazon Science
url: https://www.amazon.science/blog/developing-provably-correct-rust-code-with-verus
model: claude-code/sonnet
generated_at: '2026-09-01T10:45:21.966841'
score: 112
---

📌 【Amazon 出品】Verus：讓 Rust 程式碼「數學證明」正確無誤

TL;DR：Amazon 開源自動化驗證工具 Verus，能在 Rust 原始碼內直接寫規格並證明程式碼正確，已用於 Nitro Isolation Engine 關鍵元件。

Rust 的型別系統能防止記憶體錯誤，但無法保證你的程式「算出來的答案是對的」，也無法保證它不會洩漏不該洩漏的機密。C 語言裡陣列越界存取是危險的未定義行為；Rust 會讓程式直接當掉，這確實比較安全，但一個真正正確的程式，本來就不該去做那次越界存取。這道「更安全」與「真的正確」之間的落差，正是 Verus 想要填補的空間。

🤔 **從測試到證明：程式驗證器在做什麼**

Verus 是一個開源、自動化的 Rust 程式驗證工具。所謂「程式驗證器」，是輸入一份程式行為的正式數學規格，機械式地檢查程式碼在「所有可能輸入」下都符合這份規格。以二分搜尋為例：傳統測試頂多挑幾組陣列來跑，容易漏掉邊界情況（目標值是陣列最後一個元素，或根本不存在於陣列中）；而驗證器會檢查規格在所有輸入陣列與目標值下都成立。

🧩 **規格寫在原始碼裡，Rust 開發者不必學新語言**

Verus 讓開發者直接在 Rust 原始檔中，用 Rust 風格的語法替既有函式加上規格與證明。以二分搜尋為例，用 `requires` 關鍵字標示前置條件（例如陣列必須是排序過的），用 `ensures` 標示後置條件：若函式回傳 `Some(index)`，則該索引在陣列範圍內且對應的值等於目標值；若回傳 `None`，則目標值確實不存在於陣列中——少了這條，一個永遠回傳 `None` 的實作也能「通過」規格。

這正是 Verus 的關鍵設計取捨：規格與證明用 Rust-like 語法寫在原始碼裡，驗證失敗時看到的是 Rust 風格的錯誤訊息，讓寫程式碼的人（最了解程式碼的人）能直接參與證明過程，也讓規格與程式碼保持同步。一般 Rust 編譯器會忽略這些 Verus 註解，因此加了註解的程式碼仍可被未使用 Verus 的專案（包含 Cargo）正常消費。

Verus 也著重快速、強大的自動化：它用多種求解器處理程式與規格所產生的證明義務，開發者通常能在一秒內拿到回饋，快到足以支援互動式開發（像 VS Code 裡的紅色波浪底線）。在專案層級，Verus 能在過去某些驗證工具驗證單一函式所需的時間內，驗證數千行程式碼與證明。這個快速回饋迴圈不只幫助人類開發者，也讓 AI agent 能更快地反覆迭代其撰寫的證明。

💡 **證明 unsafe 程式碼安全、證明並行程式碼正確**

Rust 允許開發者標記 `unsafe` 程式碼以換取效能，但編譯器不再機械式檢查這些程式碼是否真的安全，一切取決於開發者自己。Verus 讓開發者能用數學方式證明這些 unsafe Rust 程式碼的安全性，重新建立機器可檢查的安全保證。

Rust 著名的「無畏並行」透過型別系統防止許多並行程式常見的錯誤，Verus 則在此之上讓開發者能證明並行程式碼不只安全、而且正確。例如針對鎖（lock），Verus 允許開發者加上不變量屬性（invariant）：任何取得鎖的人拿到的值都滿足這個屬性（例如永遠是偶數），釋放鎖時也必須證明該值仍滿足此屬性；Verus 甚至支援證明鎖實作本身的正確性——這對依賴複雜自訂鎖機制以追求高效能的 Nitro Isolation Engine 這類程式格外重要。

⚠️ **保證的邊界在哪裡**

如同所有程式驗證器，Verus 的保證仰賴幾件事的正確性：Verus 工具本身、程式意圖行為的「頂層」規格、對底層執行環境（例如 Rust 標準函式庫）所做的「底層」假設，以及把原始碼轉成可執行程式的編譯工具鏈。Amazon 表示未來會進一步說明如何提升對這些環節的信心。

🎯 **實務啟示**

對於負責關鍵基礎設施的工程師而言，Verus 提供了一條漸進式路徑：不必重寫語言或引入全新工具鏈，就能在既有 Rust 專案裡，針對最關鍵的函式（例如底層 unsafe 程式碼或自訂鎖）補上機器可檢查的正確性證明。Amazon 已將其用於 Nitro Isolation Engine 的關鍵元件與內部多項基礎設施，顯示這類工具在高保證需求的系統程式設計場景中具備實戰價值。

🔗 **來源**
- 標題：Developing provably correct Rust code with Verus
- 作者／機構：Amazon
- 連結：https://www.amazon.science/blog/developing-provably-correct-rust-code-with-verus

#Rust #FormalVerification #Verus #ProgramVerification #AWS #Amazon #SoftwareSecurity #MemorySafety #Concurrency #SystemsProgramming
