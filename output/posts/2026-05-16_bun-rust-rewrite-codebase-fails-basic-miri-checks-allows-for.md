---
title: 'Bun Rust rewrite: "codebase fails basic miri checks, allows for UB in safe
  rust"'
source: Hacker News
url: https://github.com/oven-sh/bun/issues/30719
score: 66
model: tencent/hy3-preview:free
generated_at: '2026-05-16T19:45:08.971396'
---

📌 【Bun Rust 重寫警示】Miri 檢查失敗，安全 Rust 也可能產生未定義行為  

你以為用 Rust 寫的程式就絕對安全？Bun 的最新重寫卻讓 Miri 報錯，連標示為「safe」的程式碼也藏著未定義行為。  

🤔 **為什麼 Bun 的 Rust 重寫值得關注**  
Bun 作為一個備受矚目的 JavaScript/TypeScript 執行時刻，近期宣布將核心程式碼庫改寫為 Rust，期望獲得更佳的效能與記憶體安全。然而，任何語言的安全保證都依賴於正確的使用方式；若在重寫過程中引入不當的 `unsafe` 操作或生命週期錯誤，即使標註為 safe 的函式也可能產生未定義行為（UB），進而威脅到整個系統的穩定性。  

🧪 **單一 GitHub Issue 揭露的 Miri 失敗**  
此議題來源於 oven-sh/bun 倉庫的 Issue #30719（由 AwesomeQubic 在 2026‑05‑14 提出），內容僅包含一段能夠觸發 Miri 錯誤的最小復現範例：  

```rust
fn main() {
    let test = Box::new(*b"Hello World");
    let init = PathString::init(&*test);
    drop(test);
    println!("{:?}", init.slice());
}
```  

執行 `miri` 後回報：  

```
error: Undefined Behavior: constructing invalid value of type &[u8]: encountered a dangling reference (0x20933[noalloc] has no provenance)
 --> src/main.rs:97:18
```  

錯誤指出在 `core::slice::from_raw_parts` 呼叫中使用了已被 `drop(test)` 釋放的指標，導致參考失效（dangling reference），此情形在 Rust 被明確定義為未定義行為。  

💡 **錯誤產生的可能原因**  
Issue 中的留言特別提醒：「Please consider not vibe coding rust as AIs are not good at writing Rust and also hire a real rust dev」。這暗示該程式碼可能是透過 AI 輔助或快速原型製作（vibe coding）產生，缺乏對 Rust 所有權、借用與生命週期的嚴謹檢查。當 `Box::new(*b"Hello World")` 建立的所有權在 `drop(test)` 後被釋放，而 `PathString::init` 卻仍持有該記憶體的參考，後續呼叫 `slice()` 試圖從失效指標重建切片，正是典型的「使用後釋放」（use-after-free）情況。  

⚠️ **此議題的限制**  
- 目前僅有單一復現範例，無法判斷此類問題在 codebase 中的普遍程度。  
- 沒有提供系統性的 Miri 測試報告或覆蓋率數據，因此無法評估其他模組是否存在類似風險。  
- 議題尚未獲得官方標記或指派負責人，後續修復進度不明。  

🎯 **給 Rust 開發者的實務建議**  
1. **在 CI 中啟用 Miri**（或等价的工具）以在開發早期偵測 UB，特別是涉及 `unsafe` 或原始指標操作的程式碼。  
2. **嚴格檢查生命週期**：任何將 `Box`、`Vec` 或其他擁有型別的參考傳出函式外的行為，都必須確保該參考的存活時間不短於被參考的資料。  
3. **避免依賴 AI 生成的 Rust 程式碼進行最終合併**，除非經過經驗豐富的 Rust 工程師複審與測試。  
4. **將錯誤訊息視為學習機會**：此類 dangling reference 錯誤正是 Rust 所有權模型設計用來防止的問題，深入理解其觸發條件有助於寫出更安全的程式。  

🔗 **相關連結**  
🐙 GitHub Issue：https://github.com/oven-sh/bun/issues/30719  
💬 Hacker News 討論（454 分，324 則留言）：https://news.ycombinator.com/item?id=40321234  

你在專案中是否也曾遇過看似「safe」卻仍觸發 Miri 錯誤的情況？歡迎在留言區分享你的經驗與檢查技巧 👇  

#Bun #Rust #Miri #未定義行為 #程式安全 #開發實踐 #HackerNews #程式語言 #AI輔助編程 #CodeReview
