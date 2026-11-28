---
title: Opus 5.5 and Fable 5.2 made my overoptimized Rust code even more overoptimized
source: Max Woolf
url: https://minimaxir.com/2026/11/opus-fable/
model: claude-code/sonnet
generated_at: '2026-11-28T00:39:31.290515'
score: 91
---

📌 【實測筆記】Opus 5.5把我的Rust效能又推進一步

TL;DR：實測Opus 5.5／Fable 5.2，讓已最佳化的Rust再提速1.2至1.5倍。

幾個月前，部落客Max Woolf發表一篇文章，示範如何用agentic LLM把Rust程式碼最佳化到比業界最先進的函式庫還快。這次他換了一顆大腦——Anthropic的Claude Opus 5.5——結果連他自己都沒料到，原本已經「最佳化過頭」的程式碼，竟然又被推進了一截。

🤔 **從GPT換到Opus 5.5，原因是一次「質的躍進」**

作者此前的agentic iteration pipeline主要用OpenAI的GPT模型，搭配嚴格的檢查機制，確保程式碼品質、避免迴歸，並防止LLM針對benchmark作弊。他的目標不只是追上現有SOTA函式庫，而是要把基準測試的單位從毫秒壓到微秒。文章發布翌日，Anthropic發布Claude Opus 5.5；上一代Opus 5表現平庸，市場起初反應冷淡，但很快被證實是一次顯著的能力躍升，能完成OpenAI與Anthropic其他模型都做不到的高難度技術任務。作者先花20美元／月試用，兩天後就加碼到100美元／月的方案，持續測試數個月後確認Opus 5.5及其後續的Fable 5.2，確實帶來了實際的效能突破。

🧩 **為了用上Opus 5.5，得先解決一堆harness怪癖**

作者在Opus 5.5出現前曾因為對Claude Code的不滿轉向OpenAI的Codex，主要原因包括：Claude Code長期忽略AGENTS.md、只認CLAUDE.md（直到最近才改善），以及Claude Code長期封鎖第三方harness並關閉既有的繞過方式。為了在不大改現有pipeline的前提下用上Opus 5.5，他試過用Zed Agent透過Agent Client Protocol呼叫Claude Code，但Opus 5.5偏好同時開多個背景任務非同步工作，而Zed Agent對背景任務的支援不佳，導致作者很難掌握Agent實際在做什麼；Opus 5.5也幾乎不用內建的Edit工具改程式碼，而是偏好寫一支Python腳本去做find/replace。他也試回Claude Code終端機應用程式，但上述問題反而更難處理。

最終，作者改用Claude桌面應用程式作為主要harness：它能清楚列出進行中的背景任務，直接顯示目前session與每週用量，讀取圖片時會內嵌顯示內容，還有Remote Control功能，可以讓長時間的prompt在背景執行，自己去忙別的事。非同步背景任務的好處是：主模型Opus 5.5可以邊寫程式碼、邊跑長時間benchmark，同時讓子代理（這裡用的是Haiku 5.5）同步做非阻塞的程式碼審查。另一個怪癖是prompt排隊機制：用Codex／Zed Agent時可以把類似「來吧，來個突破」的指令排隊，等目前任務做完才送出；但Claude Code會在Agent閒置（例如等待背景任務或benchmark結果）時就把排隊訊息送出去，等於提前洩漏「現在該有突破了」的訊號。作者的解法是把這句指令寫進環境外、另一個資料夾的Markdown檔案裡，避免Opus 5.5提前讀到；實測下來Opus 5.5確實沒有提前偷看，下指令後也真的做出了效能突破。

📊 **單次執行就拿下1.2至1.5倍加速**

用更新版的Ur-Prompt（明確要求在不造成迴歸、不作弊的前提下，把benchmark速度提升到指定幅度以上），Opus 5.5在多個「已經用GPT 6.1 Astra最佳化過」的獨立專案上，單次執行就取得1.2倍到1.5倍的額外加速。

💡 **會整個重寫模組，程式碼量也變多**

作者觀察到，Opus 5.5寫的程式碼行數明顯比GPT模型多；對Rust這種需要編譯的語言而言，這不必然等於效能差，但代表技術債增加。例如許多專案用Rust的png crate處理PNG編解碼，一旦PNG處理落在熱路徑上，Opus 5.5常會整個重寫一個客製化的PNG模組——重新設計平行處理與串流方式，讓它更貼合原始程式碼的資料處理邏輯——雖然確實達到1.2至1.5倍加速且沒有造成迴歸，作者形容自己是「不情願地接受」。他固定會跑一種「在不造成迴歸的前提下砍掉20%程式碼量」的維護pass，但即使如此，Opus 5.5在這項任務上也表現得很吃力。另一個困擾是：Claude Code跑criterion benchmark時，不會即時顯示中間結果，而是先導向暫存檔案，也不會在跑完前回傳結果，即使prompt明確要求即時回報也沒用，只能等待。

⚠️ **agentic LLM已經高度同質化**

作者坦言，各家agentic LLM的操作方式已經相當同質化，真正的差異多半落在可能被刷的benchmark，或者更難量化的「vibes」。Opus 5.5在Claude Code這個harness上也有明顯的使用摩擦：背景任務不透明、不支援慣用的第三方harness、prompt排隊邏輯特殊，最終逼得作者改用桌面App，而非自己慣用的CLI或Zed Agent工作流程。

🎯 **把pipeline從GPT系搬到Opus 5.5，不能原封不動**

如果你的agentic coding pipeline原本是為GPT系模型設計，直接套用Opus 5.5未必順利：需要針對它偏好開背景任務、prompt會在閒置時被意外送出、以及傾向整個重寫模組而非小修小補的習慣，調整AGENTS.md與工作流程；同時可以善用像Haiku 5.5這類輕量模型做非阻塞的程式碼審查，讓它和主模型的長時間benchmark並行執行，節省等待時間。

🔗 **來源**
- 標題：Opus 5.5 and Fable 5.2 made my overoptimized Rust code even more overoptimized
- 連結：https://minimaxir.com/2026/11/opus-fable/

#ClaudeOpus #AnthropicAI #AgenticCoding #Rust #ClaudeCode #PerformanceEngineering #LLM #AICoding #Benchmarking #DeveloperTools
