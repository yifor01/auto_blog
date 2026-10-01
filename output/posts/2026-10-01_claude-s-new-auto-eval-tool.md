---
title: Claude’s new auto eval tool
source: Hamel Husain
url: https://hamel.dev/blog/posts/claude-auto-evals/
model: claude-code/sonnet
generated_at: '2026-10-01T22:02:28.280565'
score: 93
---

📌 實測 Anthropic 新 eval 工具：好用，但別急著交出判斷權

TL;DR：資深從業者實測 Claude Code 的自動化 eval 外掛，發現它太急著做決定，卻沒先讓人看懂資料。

Anthropic 幫 Claude Code 出了一個能自動幫你「建 eval、檢查 grader、再根據結果迭代改進」的工具，聽起來像是把評估流程整個自動化了。但資深 ML 顧問 Hamel Husain 實際用它跑了一輪真實對話資料後發現，這個工具最大的問題不是做得不好，而是做得「太快」。

🤔 **背景：一個可能改變業界做法的第一方工具**

Anthropic 在 Claude Code 的 claude-api 外掛中加入了新的 `build_eval` 與 `hill-climb` 指令，用來協助使用者建立 eval、檢查 grader 品質，並持續針對應用程式做改進。Hamel Husain 坦言自己平常不太寫 eval 工具的評論，因為軟體變動太快，評論的保鮮期很短；但出自 Anthropic 之手的第一方工具很可能影響整個業界之後怎麼做 eval，因此他和 Isaac Flath 直接拿一個公寓租賃助理的真實對話紀錄做直播實測。

🧩 **實測過程：建議很快給出，但資料還沒被真正看過**

Claude 一開始就主動列出好幾個潛在失敗模式，並要求兩人立刻從中挑一個做成 eval，給出的選單中以「call-transfer 轉接規則」為推薦選項。問題是，兩人當時根本還沒看過原始對話資料，很難判斷這是不是真實存在、值得優先處理的問題；儘管如此，他們還是選了推薦選項，理由是「這應該就是一般使用者會做的選擇」。作者強調，正確的順序應該是先看資料、建立理解，再決定要優先寫哪個 eval——agent 可以幫忙找出問題，但決定哪個失敗值得投入資源，仍然需要人親自做 error analysis。

接下來 Claude 產生了一份 Markdown 檔案讓他們檢視 call-transfer 失敗案例，並要求他們瀏覽 `inputs.md`、「告訴它」哪些標籤標錯了——意思是得在編輯器裡讀完一長串對話紀錄，再另外用聊天訊息回報修正意見。兩人覺得這個設計相當不合理：既然是用 coding agent，理應直接做一個標註用的網頁應用，讓對話好讀、也能就地留下回饋。他們最後只好自己要求 Claude 現場生成一個網頁應用來取代這個流程。

再往後，Claude 嘗試針對 call-transfer 失敗建立 evaluator，呈現了標籤的彙總統計數字，並詢問「你會不會對任何一個案例評分不同？」，但並沒有提供足夠資訊讓人判斷這些標籤本身是否正確。整個流程中反覆出現同一個模式：工具太快跳去產生成品或要求使用者核准，卻沒有先幫使用者真正理解資料。

最終產生的 call-transfer evaluator 一次檢查了四種不同的失敗情況，作者認為這樣綁得太多——應該把一個 eval 聚焦在單一錯誤類型，或至少把「程式碼可判斷的檢查」與「LLM-as-Judge 的檢查」分開處理。Claude 對這個 evaluator 的說明本身也令人困惑：`protocol_ok` 是主要指標，只有四項檢查全部通過才算分；在「不該轉接」的通話中，只要沒有發生轉接，`protocol_ok` 就會是 1。作者形容這種敘述是「難以讀懂的 AI 廢話」，他更希望直接看到程式碼或 judge prompt 本身，才能真正理解系統在判斷什麼——他的經驗是，讀 prompt 永遠是值得的，尤其對 eval 這麼關鍵的東西。

📊 **令人意外的亮點：一次性問題探索能力很強**

儘管流程設計上有諸多意見，作者仍對這個外掛「開箱即用」就能挖出問題的能力印象深刻：它找出了人工轉接、格式問題、語音 agent 等多種失敗模式，是作者目前看過「一次性」問題探索方法中表現最強的一次，即便他仍然認為搭配 agent 反覆查看資料的方式會更好。他也認同 Anthropic 官方部落格文章傳達的理念，例如重視先看資料、聰明取樣、不要讓自己的 eval 過度飽和等原則。

⚠️ **限制：還不建議現在就依賴它**

作者的結論是「現在先觀望」。他希望這個工具能在使用者真正承諾選定某個 evaluator 之前，先幫助探索資料，並從一開始就提供更好的審閱介面。他也提到自己團隊已經有一套搭配 coding agent 使用的 Eval skills（與 Shreya 共同製作），雖然較不具主導性，但更靈活。作者後續已與這個外掛的作者溝通過，對方對回饋表示感謝，也說會據此調整外掛，因此預期這個工具近期會持續改版，未來值得再回頭檢視。

🎯 **實務啟示**

挑選或打造 eval 工具時，關鍵判準是：它有沒有把「先看懂資料」放在整個流程的核心，而不是急著產生 evaluator 或要求你核准。拿到任何自動化產生的 eval 或 judge，務必親自檢查其背後的程式碼或 prompt，而不是只看彙總後的分數——正如作者所說，如果一個 eval 工具沒有把看資料放在工作流程中心，就不值得使用。

🔗 **來源**
- 標題：Claude's new auto eval tool
- 作者／機構：Hamel Husain
- 連結：https://hamel.dev/blog/posts/claude-auto-evals/

#ClaudeCode #Anthropic #LLMEval #AIEngineering #ErrorAnalysis #EvalDriven #AIAgents #MLOps #PromptEngineering #AIQuality
