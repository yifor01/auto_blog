---
title: Mathematical proof, powered by AI. And no hallucinations!
source: Amazon Science
url: https://www.amazon.science/blog/mathematical-proof-powered-by-ai-and-no-hallucinations
model: claude-code/sonnet
generated_at: '2026-11-18T23:33:25.656577'
score: 108
---

📌 讓AI證明數學定理，但每一步都被電腦檢查過

TL;DR：Amazon用MCP把AI agent接上形式證明助手Isabelle，讓生成與驗證交錯進行，杜絕幻覺。

AI模型解奧林匹亞數學題、甚至碰觸研究級open problem的消息屢見不鮮，但AI agent出了名地容易「編故事」。既然如此，證明到底可不可信？答案其實很簡單：讓電腦親自檢查這些證明就好，而且驗證可以跟生成同步進行，邊寫邊查。

🤔 **形式證明助手：給電腦看得懂的數學語言**

要讓電腦檢查證明，證明必須寫成某種精確的邏輯形式語言。Proof assistant就是為撰寫與檢查形式證明設計的應用程式，其中Lean廣受數學家喜愛，HOL Light被AWS用來驗證高效能密碼學程式碼（包括後量子密碼學），Isabelle則被AWS用於驗證Nitro Isolation Engine。這些工具原本是為人類使用者設計，現在「使用者」換成了AI agent，而大多數proof assistant都適合這個新角色。本文聚焦在Isabelle上。

要讓AI agent跟proof assistant對話，需要一條兩者都懂的「線」，這正是Model Context Protocol（MCP）的角色，目前主流AI agent都支援它。像HOL Light這類提供簡單command-line REPL介面的工具，接上agent相對容易；但像Lean常搭配VS Code這種為人類設計的精密介面，就需要額外改造才能讓agent直接溝通。

🧩 **三個工具：I/Q、I/R、Isabelle Assistant**

Amazon在AutoCorrode驗證套件中公開了三個工具：
- **I/Q**：讓AI agent與電腦上正在執行的Isabelle session溝通，使用者可以暫時把proof assistant的控制權交給AI，讓它填入形式化內容或評估上下文並給建議。
- **I/R**：讓agent在使用者仍持續操作proof assistant的同時，獨立開發證明或其他形式化內容；agent依然直接跟proof assistant對話以確認證明是否成立，但不會像I/Q那樣取得控制權。
- **Isabelle Assistant**：建立在I/Q之上，提供一個聊天視窗讓使用者與AI agent互動，AI可以觀察並修改使用者的session、開發或修正證明，功能不如完整的I/Q與I/R組合，但開箱即用，操作方便。

📊 **三個範例：從根號2到微積分**

文章用Isabelle Assistant示範了幾個經典問題。第一個是根號2為無理數的古典證明，Claude Opus 4.6把它形式化，產出的證明「出乎意料地道地」，雖然比嚴格必要的篇幅略長。第二個是「存在N個連續合數」的證明：作者先給Claude一個其實有瑕疵的證明草稿（用N!推導，實際上只能得到N-1個連續整數），Claude不只發現了這個錯誤，還自行修正並補出完整證明。第三個是sin x在0到π區間的定積分，作者只用一句「給我一個簡單的微積分範例」的plain English請求，Claude就生成了完整且正確的Isabelle證明，包含必要的輔助定理（-cos x的導數是sin x）與註解。

💡 **生成與檢查交錯，才是避免幻覺的關鍵**

這幾個範例的共同點是：AI不需要使用者事先知道如何用proof assistant的語言寫下證明，只要給出數學主張甚至plain English描述即可。因為每一步推理都會立刻被Isabelle檢查，生成過程本身就帶有即時糾錯能力，這正是「用電腦檢查AI的證明」優於單純信任AI輸出的地方。

⚠️ **真正困難的問題仍需要人類導航**

作者坦言，對於更困難的研究級專案，才真正需要I/Q與I/R這類更進階的工具：透過I/R，agent可以在背景默默地開發或修正證明，而不觸動使用者正在編輯的文件，讓人類與AI能同時工作、互不干擾。文中也強調，最困難的問題仍然需要人類思考，AI更適合承擔重構雜亂證明、追蹤除錯軌跡這類冗長但直接的任務，讓人類保留精力做關鍵決策。

🎯 **實務啟示**

對想結合LLM與形式驗證的工程團隊來說，MCP提供了一條把AI agent接上既有proof assistant生態（Lean、HOL Light、Isabelle）的標準路徑，不必自行設計通訊協定。這個模式不只適用於數學證明，也呼應了AWS已經在用形式驗證保護密碼學程式碼與隔離引擎的實務場景：讓生成與驗證緊密耦合，才是用AI處理高風險正確性問題時可信任的做法。

🔗 **來源**
- 標題：Mathematical proof, powered by AI. And no hallucinations!
- 作者／機構：Amazon Science
- 連結：https://www.amazon.science/blog/mathematical-proof-powered-by-ai-and-no-hallucinations

#AI #FormalVerification #TheoremProving #Isabelle #MCP #MathAI #Claude #AmazonScience #Lean #NoHallucinations
