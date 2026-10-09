---
title: How Postman runs Agent Mode for 40 million developers on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-postman-runs-agent-mode-for-40-million-developers-on-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-10-09T21:58:09.593038'
score: 92
---

📌 4000 萬開發者的 Agent，Postman 踩過的三個架構陷阱

TL;DR：Postman 把 AI agent 塞進 11 年歷史的產品時發現，瓶頸不是模型品質，而是工具數量與上下文設計。

多數團隊做 agent demo 時最怕模型不夠聰明，Postman 的 Agent Mode 團隊卻發現，真正拖垮生產環境的是「工具太多」和「上下文不對」,模型本身反而不是最大問題。

🤔 **把一個介面導向的老產品，重新教給 AI 看**

Postman 的 Agent Mode 是讓使用者用 AI-native 的方式操作 API 測試、文件、探索與實作的入口。過去 11 年，使用者習慣靠展開側邊欄、切換分頁、打開 request 來找資訊；但 agent 是直接對資料做推理，不是在畫面上導航。這個落差讓團隊重新發現,產品的 API、UX 以及知識分布方式裡藏著大量「為人類介面設計」的隱性假設，這些假設在餵給 agent 時全部要重新處理。

🧩 **工具超過 40 個，模型就開始選錯**

團隊一開始偏好「原子化工具」：開啟一個 request、更新一個欄位、抓一筆 metadata，每個動作都很精確。但這個設計很快出現兩個問題。第一，真實工作流常常需要一長串工具呼叫，即使每一步都很快，使用者仍感覺整體很慢，因為每個動作都要先回到模型才能進行下一步。第二，Postman 測試發現，當可見工具集超過大約 40 個時，工具選擇錯誤明顯增加：模型會呼叫不存在的工具、在 schema 正確的情況下傳錯參數，或選中語意上合理但情境上錯誤的工具。換成更大或更新的模型能緩解，但無法消除這個問題。

現行架構的做法是動態選工具：root agent 先查詢一個工具 embedding 的向量資料庫，把超過 170 個工具縮小到約 15 個與當前請求相關的工具，再交給一個context 隔離的子 agent 執行,模型最終只看到任務需要的工具。另一個細節是,許多客戶端 API 其實隱性綁定了介面狀態,例如要修改一個 request 得先打開對應分頁，這等於讓 agent 模仿人類操作介面而非直接對資料推理。Postman 正在把工具與分頁解耦,Native Git 功能就大量用了這個做法,例如現在 Agent Mode 可以在背景送出 request 而不需要打開分頁（仍需使用者核准）。

📊 **用 schema 查詢取代一堆單點工具**

對於像 API Catalog 這種暴露大量結構化資料（服務可用度、測試結果、端點回應時間）的產品，Postman 把多個窄視圖整併成單一查詢工具：給模型底層 ClickHouse 資料表的 schema，讓它自己生成帶 join 和 where 子句的複雜查詢，而不是每個分析問題都建一個新工具。這把工程重心從「每個問題建一個工具」轉成「把資料模型建好一次」,agent 能生成的查詢種類遠超團隊能手動列舉的工具數量。

💡 **缺的不是工具，是上下文**

團隊原本以為缺工具才是最大瓶頸，但實際上多數失敗來自上下文缺失或錯誤,context 指的是 agent 對使用者目前在 Postman 裡的位置、哪些實體是啟用狀態、哪些狀態已經成立的理解。直接序列化既有介面資料模型並不管用，因為那些物件是為渲染和資料傳輸設計的，不是為推理設計的。Postman 因此建了專屬的 context handler，把每個實體蒸餾成 agent 真正需要知道的資訊，並區分兩種 context：自動蒐集、壓縮進 prompt 的廣而淺的背景資訊，以及使用者主動選定、經由專屬 handler 處理的深而聚焦的選定資訊。

在模型層，Agent Mode 跑在 Amazon Bedrock 上,取得模型彈性、跨區域推理、依模型決定的零資料保留，以及多層 prompt caching。人工監督也內建在設計裡：修改應用狀態的動作一律要使用者核准，並用 Amazon Bedrock Guardrails 在資料送進 LLM 前過濾個人識別資訊，企業管理員可在 Agent Mode 的 guardrail 設定中開啟。

🎯 **實務啟示**

把工具目錄視為上下文預算的一部分：依任務動態篩選模型能看到的工具，並讓「agent 能做什麼」與「UI 剛好開著什麼」脫鉤。遇到結構化資料時，寧可做好 schema 讓 agent 自己查詢，也不要無限擴增單一用途的讀取工具,這會換來更好的擴充曲線。同時別把上下文建設想得太輕,序列化既有資料模型往往不夠用,專屬的 context 蒸餾邏輯才是讓 agent 在複雜產品裡站穩的關鍵。

🔗 **來源**
- 標題：How Postman runs Agent Mode for 40 million developers on Amazon Bedrock
- 作者／機構：Srinivas Kini, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/how-postman-runs-agent-mode-for-40-million-developers-on-amazon-bedrock/

#AIAgent #AmazonBedrock #Postman #AgenticAI #LLMOps #ProductionAI #AWS #ToolUse #ContextEngineering #APIFirst
