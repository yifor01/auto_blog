---
title: Formally verifying agent-written full-stack web apps with PDD Kit
source: Microsoft Research
url: https://www.microsoft.com/en-us/research/blog/formally-verifying-agent-written-full-stack-web-apps-with-pdd-kit/
model: claude-code/sonnet
generated_at: '2026-11-05T22:54:28.390421'
score: 109
---

📌 Agent 一口氣寫出十萬行程式碼，審查該怎麼跟上？微軟改用「證明」補位

TL;DR：微軟研究院的 PDD Kit 把自然語言意圖轉成正式規格與證明，驗證 agent 寫的程式碼是否真的對，而不只是測試有過。

Agent 現在動輒一次 PR 就是數萬、甚至數十萬行程式碼，逐行人工審查早已不現實。於是多數團隊退而求其次：描述需求給 agent、反覆確認計畫與測試看起來沒問題，再放手讓它實作。問題是，agent 會悄悄偏離原本的計畫，寫出一套跟你要的不太一樣的東西，再補上剛好能通過自己實作的測試。CI 燈號全綠、覆蓋率數字健康，缺口卻一直藏著，直到使用者回報 bug 或踩到邊角案例才現形。

🤔 **測試能抓到的，只是程式能做的所有事情裡的一小片**

審查問的是「這看起來對嗎」，而數學證明回答的是「這真的對嗎」——證明能涵蓋所有輸入，包括測試套件漏掉的那些，提供比單靠測試更強的保證。過去形式化證明對一般軟體來說太昂貴：需要專家、不熟悉的語言，證明篇幅常常比程式碼本身還大，開發週期動輒數年。但現在的 coding agent 讓產生正式證明、以及協助撰寫正式規格都變得務實許多，這套新的開發模式被微軟稱為 Proof-Driven Development（PDD），PDD Kit 就是對應的工具。

🧩 **PDD Kit 的設計理念：把「信任邊界」畫清楚**

PDD Kit 的角色相當於 Spec-Driven Development 裡 Spec Kit 的形式化版本，運作在 GitHub Next 的多人即時規劃環境 Chopin 裡。整個工作流程分兩半：團隊先用白話審查「意圖」，PDD Kit 會像一個嚴謹的審查者一樣逐一提問、邊問邊解釋相關程式碼，並把答案記錄成一份「意圖文件」（intent artifact）。能被形式化的部分轉成正式規格並自動產生證明，其餘必須靠信任的部分，則轉成非正式規格並自動產生高品質測試。每一個驗證結果都明確標示它靠的是哪種保證，而證明所假設「程式碼如預期運作」的那部分，就是信任運算基底（Trusted Computing Base, TCB）——PDD Kit 會把這條線畫清楚，要求你針對每一塊明確簽核，整個過程不需要形式化方法背景。

🧩 **實測案例：用一個 Rust 全端寵物店 App 驗證登入邏輯**

微軟團隊打造了一個約 5000 行 Rust 程式碼的全端範例「Pet Store」：後端用 Axum 與 SQLite 處理庫存、促銷、訂單與結帳，前臺則是編譯成 WebAssembly 的 Leptos 應用。開發者在 Chopin 裡提出的需求只有兩句話，要求驗證登入邏輯（backend/src/handlers/auth.rs）。PDD Kit 的 pdd-plan 在動手寫任何東西之前，先讀程式碼、回來在「Decisions」頁籤中提出問題，遇到需要理解程式碼才能回答的問題，會先解釋目標、元件如何串接、以及牽涉的確切函式，讓開發者不用自己翻原始碼就能回答。

其中一個看似吹毛求疵的問題很關鍵：「只有密碼正確才會拿到 token」只排除了「密碼錯誤卻拿到 token」這種壞情況，而「密碼正確一定能登入」才是另一半保證——兩者合起來才構成完整的「若且唯若」。若放著 agent 自己決定，它可能只挑一邊卻不告訴你；這次開發者兩邊都選了。隨著對話推進，PDD Kit 會把一份摘要重點放在計畫最上方，裡面包含登入流程的流程圖、哪些部分要被證明、哪些要被信任的規格地圖，以及把每項需求連結回開發者原話、並對應到 Verus 證明合約片段與測試的意圖對照表。

🧩 **開發者主動擴大驗證範圍**

PDD Kit 原本的預設做法，是證明核心的資料表查詢與密碼比對邏輯，而把外圍的 handler 留在「信任且測試」的範圍內。但這次開發者認為，handler 正是等待查詢結果、簽發 token 的地方，重構時最容易悄悄換錯兩行，因此要求把整個登入 handler 也納入正式規格，交由新增的 async 函式 login_flow 承接從請求欄位到 token 或 HTTP 錯誤的完整合約。這個決定讓幾乎所有邏輯都被納入證明範圍，PDD Kit 也因此重新把修訂後的計畫拿回來要求團隊再次簽核——畢竟符合意圖不等於已經證明，範圍擴大與新增信任都需要重新確認。

⚠️ **證明之外，仍要靠測試補位**

登入邏輯裡仍有一些無法單靠證明涵蓋的部分，PDD Kit 的做法是把這些信任邊界明確列出：用 Verus 的 external_body 或 external_fn_specification 把每個被信任的元件包成一個帶假設合約的小函式，要求開發者逐一確認接受，並為每一條被假設的條件在計畫中補上對應測試。

🎯 **對工程師的實務啟示**

不需要具備形式化方法背景，就能從最敏感的程式碼（像登入、金流）開始，漸進式導入證明，而不是要求全有或全無。更重要的是，把「信任邊界」老實標示出來，遠比盲目信任 agent 產出的測試套件更可靠——這正是審查規模跟不上 agent 產出速度時，一個可行的補強方案。

🔗 **來源**
- 標題：Formally verifying agent-written full-stack web apps with PDD Kit
- 作者／機構：Microsoft — Alex Lavaee, Matthai Philipose
- 連結：https://www.microsoft.com/en-us/research/blog/formally-verifying-agent-written-full-stack-web-apps-with-pdd-kit/

#FormalVerification #AIAgents #ProofDrivenDevelopment #Rust #CodeReview #MicrosoftResearch #Verus #SoftwareEngineering #DeveloperTools #AICoding
