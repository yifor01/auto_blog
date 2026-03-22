---
title: "We rewrote our Rust WASM parser in TypeScript and it got faster"
source: Hacker News
url: https://www.openui.com/blog/rust-wasm-parser
score: 85
model: gpt-4o-free
generated_at: 2026-03-22T18:33:02.504789
---

📌 **用 TypeScript 重寫 Rust WASM parser，速度竟提升 3 倍**

你以為 Rust 編譯到 WASM 一定是瀏覽器端高效能的首選？Thesys 團隊在實作 openui-lang parser 時卻發現，恰好是「錯誤的優化點」讓效能受限。

🎣 **折疊區優化 (The Hook)**  
當每個串流 chunk 都需要解析時，延遲直接影響使用者體驗。你以為換成更快的語言就能解決問題，但實際瓶頸可能根本不在演算法，而在於語言邊界本身。

🤔 **將 Rust 編譯到 WASM 的延遲來源**  openui-lang parser 是一個六階段管線（autocloser → lexer → splitter → parser → resolver → mapper），設計為在每個 LLM 輸出的串流片段上運行，因而對延遲極為敏感。團隊最初選擇 Rust 並編譯為 WASM，期望利用其近原生速度。然而，每次呼叫 WASM 函式都必須付出固定的邊界成本：將 JavaScript 堆積中的輸入字串複製到 WASM 線性記憶體，解析完後再將結果複製回去。這段「複製 + 配額」的開銷與 Rust 程式碼本身的執行速度無關，卻在每個 chunk 上累積。

🧪 **重寫為純 TypeScript 的實驗**  
為了驗證假設，團隊將同樣的六階段管線重新實作為純 TypeScript，直接在 JavaScript VM 中運行。這樣做可以完全避免 WASM 與 JavaScript 之間的資料複製與記憶體分配開銷。

🚀 **TypeScript 版本比 Rust/WASM 快 3 倍**  
在相同的串流輸入下，TypeScript 實作的解析延遲約為原本 Rust/WASM 版本的三分之一。由於管線本身的演算法未變，效能提升主要歸因於**消除了 WASM 邊界的固定開銷**。

💡 **為什麼「更快的語言」不一定帶來更低延遲**  
這個案例凸顯了一個常見的誤區：在瀏覽器環境中，**語言的原始運算速度**並不是唯一決定因素。當頻繁在 JavaScript 與 WASM 之間傳遞大量資料時，邊界開銷可能會掩蓋底層語言的優勢。對於需要處理許多小型、頻繁輸入的管線（如串流解析、即時編譯），將邊界減少或完全移除往往比換用更快的後端語言更有效。

⚠️ **研究限制（實際觀察的侷限）**  - 觀察基於單一特定 parser（openui-lang）及其六階段管線，其他類型的應用程式可能有不同的權衡。  - 未對不同輸入大小或不同 WASM 編譯優化層級（例如 -O3、帶有自訂記憶體分配器）進行廣泛基準測試。  
- 未探索混合方案（例如只將熱點函式編譯為 WASM，其餘保留在 JavaScript）。

🎯 **給開發者的實務啟示**  1. **先量測邊界成本**：在決定使用 WASM 前，先以代表性的資料量測量 JS↔WASM 資料複製與記憶體分配的開銷。  
2. **考慮保留在 JavaScript 中**：對於延遲敏感且資料量不大的工作負載，純 JavaScript/TypeScript 實作有時能提供更好的整體表現。  
3. **優化資料傳遞**：若必須使用 WASM，嘗試減少複製次數（例如使用共享記憶體、TypedArray 零拷貝）或批量處理輸入以攤薄固定開銷。

🔗 **文章連結**  
📝 We rewrote our Rust WASM parser in TypeScript and it got faster  
👤 zahlekhan (Thesys Engineering Team) – Hacker News  
🔗 https://www.openui.com/blog/rust-wasm-parser  你的專案是否也在為「選擇更快的語言」而犧牲了實際的延遲表現？歡迎在留言區分享你的經驗或疑問 👇  

#WebAssembly #TypeScript #Rust #效能優化 #前端開發 #Thesys #HackerNews #工程實踐
