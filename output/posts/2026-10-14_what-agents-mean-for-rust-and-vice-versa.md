---
title: What agents mean for Rust (and vice versa)
source: Hacker News
url: https://smallcultfollowing.com/babysteps/blog/2026/10/14/agentic-dev-and-rust/
model: claude-code/sonnet
generated_at: '2026-10-14T21:09:34.704279'
score: 72
---

📌 Rust為何在agent時代逆勢爆紅？一位語言設計者的觀察

TL;DR：資深語言設計者分析，Rust的型別系統正成為agent寫程式碼時不可或缺的護欄。

當AI agent寫出的前幾個測試一路綠燈通過，接下來某個測試卻冒出一個你完全無法想像來源的詭異bug——這正是型別系統該站出來擋一道的時刻。

🤔 **LLM讓他對程式語言設計產生existential dread**

作者從五年級就開始在一臺5MHz、硬碟容量約5MB、記憶體512K的x86電腦上寫程式。硬體雖然天差地遠,但「把程式碼打進檔案」這件事本身,數十年來出乎意料地穩定,直到近幾年LLM出現才徹底翻轉。這讓他一度對自己身為程式設計者、語言設計者的技能是否還有價值感到存在性的焦慮。他在這篇文章給出的結論是：人類在程式設計中仍有角色,程式語言設計仍然重要,而Rust恰好特別適合agentic開發——雖然還能做得更好。

📊 **Rust正夯：Meta今年寫的Rust比過去九年總和還多**

文章引用的語言成長圖表顯示,TypeScript是成長最快的「breakout language」,年成長率達1200%;Rust則是成長第二快的語言。David Tolnay的說法被引用：Meta工程師今年寫的第一方Rust程式碼量，已經是過去九年加總的兩倍。作者認為原因之一是agent讓嘗試新語言的門檻變低,加上Rust效能的口碑,但他更傾向認為,Rust本身的特性恰好適合agentic coding。

🧩 **軟體工廠的三支柱：設計、構建、最佳化**

作者提出,一套有效的「軟體工廠」仰賴三個環節：設計（明確定義程式該做什麼）、構建（寫出符合規格的程式碼）、最佳化（讓程式碼高效運作）。這三者都還沒被完全解決,但各自的進展程度不同。

🧩 **agent正在讓效能調校的黑魔法變簡單**

Rust的設計哲學是「預設就有好效能」,符合慣例的寫法通常也就是最快的寫法,同時保留手動調校的空間：可以控制變數是配置在堆疊還是heap、指標間接層發生在哪裡、強制struct的記憶體排列方式，甚至決定async堆疊框架中何時進行boxing,極限情況下還能寫inline組合語言。過去學習「調這些效能旋鈕」帶點黑魔法色彩,作者觀察到agent正在讓這件事變得容易許多：原本靠手工調校組合語言做高效能密碼學演算法的工程師,現在也開始改用agent完成同樣工作;許多打造網路服務的工程師搭配像dial9這類profiler,讓agent有效診斷出async效能陷阱,例如長時間polling或blocking的問題。

💡 **編譯過幾乎就是對的：型別系統是agent的護欄**

作者認為,效能口碑吸引人們接觸Rust,但真正讓人留下來的,是「用起來感覺比較不容易出錯」。他引用Greg Brockman的說法：「Rust對agent來說是完美的語言,因為只要能編譯過,幾乎就是對的。」作者認同Rust、OCaml、Haskell這類具備「編譯過就能動」特性的語言,會讓agent明顯受益。他也引用Dijkstra的名言「測試只能證明bug存在,不能證明bug不存在」,並根據自身經驗描述：用agent寫程式碼時,最初幾個測試常常看起來很棒,但下一個測試卻會冒出完全無法理解來龍去脈的詭異bug,深入追查後往往發現agent根本誤解了想表達的邏輯。這正是型別系統能發揮作用的地方——Rust的guardrails不只檢查欄位名稱是否正確這類基本錯誤,還能保證像「socket一定會被關閉」這樣的性質。

⚠️ **型別系統能證明沒bug，不能證明程式正確**

作者也自嘲提出一句話：型別系統能證明bug不存在,卻不能證明程式正確。型別系統終究只是一套簡單規則,遵守它能避免特定種類的錯誤,但不保證你做了對的事。若要進一步驗證更豐富的性質,需要證明系統,他點出Rust生態中已有Verus、Creusot、Aeneas、Kani等證明工具,舉例來說可以用來證明程式碼panic-free,但他也提醒,這仍是一種類似型別檢查器的性質保證,而非完整的正確性證明。

🎯 **給正在評估agent大量產碼的團隊**

如果團隊正考慮讓agent大量產出程式碼,這篇文章給出一個明確方向：選用型別系統嚴謹的語言,讓編譯器成為agent即時的回饋迴圈與安全網,而不是只靠測試把關;若追求效能,搭配profiler與agent的組合,正在取代過去仰賴手工調校的黑魔法技藝;同時Verus、Creusot等形式驗證工具,值得留意作為型別系統之外更進一步的正確性保障。

🔗 **來源**
- 標題：What agents mean for Rust (and vice versa)
- 作者／機構：mfrw（Hacker News）
- 連結：https://smallcultfollowing.com/babysteps/blog/2026/10/14/agentic-dev-and-rust/

#Rust #AgenticCoding #ProgrammingLanguages #TypeSystems #AIAgents #SoftwareEngineering #FormalVerification #LanguageDesign #DeveloperTools #CodeGeneration
