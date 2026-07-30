---
title: "Boris Cherny：Claude Code 之後，寫代碼正在變成“管理 Agent”"
source: 寶玉 baoyu.io
url: https://baoyu.io/blog/anthropics-boris-cherny-why-coding-is-solved-and-what-comes-next
score: 100
model: tencent/hy3-preview:free
generated_at: 2026-05-05T20:09:29.718418
---

📌 零手寫代碼、150 PR/日：Boris Cherny 說寫代碼已變成「管理 Agent」

你以為 AI 寫 Code 只是讓你敲鍵盤變快？但 Anthropic 內部已經沒有人類手寫任何一行產品或 SQL 代碼，靠 Slack 互 ping 的 Claude 彼此解決不確定問題，夜間還有數千 Agent 透過 Loop 排程「自己把項目寫完」——而這樣的組織，才是十億美元收入真正的來源。

🤔 **寫代碼變快不是終點，組織流程的重構才是**

2024 年底，Claude Code 還只是一個三人孵化項目：IDE 裡按 Tab 自動補全一行已經是當時最強的體驗。當時 Anthropic 內部用「產品懸置（Product Overhang）」來描述這個狀態——模型能力已經到位，但還沒有產品把它釋放出來。真正的目標從一開始就不是「補一行」，而是讓 Agent 負責寫完整功能。

🧪 **從「寫 10% 代碼」到「全年未寫一行、每天合併數十個 PR」**

Boris Cherny 承認，Claude Code 上線前半年幾乎無人使用，自己也只用它寫 10% 的代碼；即便對外釋出，也沒有立即出現指數增長。真正的拐點是 Opus 4 在 2025 年 5 月釋出之後：每一代新模型都讓曲線再往上拐，從 4.0 到 4.5、4.6，再到 4.7，能力與穩定性逐代疊代。

到了 2026 年，Boris 整年沒有手寫一行代碼，單日最多合併 150 個 PR；日常操作從手機完成，Claude App 內常駐 5–10 個 session、數百個 Agent，夜間更有數千個在執行深度任務。核心調度模式稱為 Loop：透過 cron 啟動定時循環，讓 Claude 持續分解、重構與交付。

💡 **寫代碼是簡單的，懂業務才是稀缺的**

Boris 用印刷術作類比：軟體開發正逐漸像「識字」一樣普及，最合適寫會計軟體的不再是工程師，而是會計師本身。因為模型已經能處理編程的機械層面，真正難的是對業務邏輯的精準理解。

他也借用「七種護城河」框架指出 AI 時代 SaaS 的重構：  
- 會被抹平的：切換成本、流程效力（模型能協助遷移與自我迭代）  
- 保持不變的：網絡效應、規模經濟、獨占資源  

⚠️ **十億美元不是技術勝出，而是組織與流程勝出**

Anthropic 內部已經沒有人類手寫代碼：所有 SQL 與產品代碼皆由模型生成；員工之間的 Claude 透過 Slack 互相溝通，把不確定問題直接 ping 給對方模型求解。這意味著真正的差距不在模型本身，而在組織怎麼改造、Agent 之間怎麼協作，以及公司如何系統性地把「手寫」從流程中移除。

🎯 **管理 Agent 取代親自寫代碼，將成為工程師的新常態**

- 工程價值將從「寫得多」轉向「驗證與調度得多好」  
- 將重複性任務包裝成可排程的 Loop，透過多 Agent 分工與互動完成  
- 業務專家直接使用 Agent 實現需求的能力，會逐漸比工程實作更關鍵  

🔗 **論文/文章連結**  
📝 Boris Cherny：Claude Code 之後，寫代碼正在變成「管理 Agent」  
👤 宝玉 / baoyu.io  
🔗 https://baoyu.io/blog/anthropics-boris-cherny-why-coding-is-solved-and-what-comes-next  
📺 原始訪談（AI Ascent 2026）：https://www.youtube.com/watch?v=SlGRN8jh2RI  

你現在的開發流程裡，Claude 或其他 AI 助手負責了多少百分比的決策與交付？你覺得工程師的角色會怎麼改變？歡迎在留言區分享 👇

#AI #ClaudeCode #軟體工程 #Agent #開發流程 #Anthropic #SaaS護城河
