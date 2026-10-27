---
title: Coding From the Himalayas With an Offline AI Agent
source: Latent Space
url: https://latent.space/p/offline-coding/
model: claude-code/sonnet
generated_at: '2026-10-27T21:40:37.733263'
score: 83
---

📌 在喜馬拉雅山腳斷網寫程式:本地 Coding Agent 實測

TL;DR:Thomson Reuters 工程師在斷網環境用 OpenCode + Ollama 跑本地模型,實測能完成多少編碼任務。

當網路和電力都不保證穩定,你的 coding agent 還能工作嗎?一位搬到喜馬拉雅山腳下生活的 Principal Engineer,決定把這個問題當真,直接拔掉 Wi-Fi 測試答案。

🤔 背景:山區生活帶來的新變數

作者是 Thomson Reuters 的 Principal Engineer,日常工作大量仰賴 coding agent 寫程式與審查程式碼。搬到喜馬拉雅山腳下一年後,網路與電力中斷成了生活常態,也讓他開始思考:平常依賴雲端模型的 coding agent 工作流程,能有多少部分搬到完全離線的環境下執行?他指出,像是請 agent 解釋一段陌生函式、調查失敗的測試、重構一小段程式碼、或協助完成一個功能,這類任務只要模型、專案依賴與測試工具都已經在本機,理論上都能離線完成;真正需要連網的,是下載新套件或查詢網路資料。

🧩 架構:OpenCode 負責互動,Ollama 負責跑模型

作者選用開源 coding agent OpenCode(測試版本 1.19.4),它能讀取專案檔案、提出修改建議並執行指令(例如測試套件),且在編輯檔案或跑指令前會跳出權限確認,方便逐步審查。模型執行則交給 Ollama,在同一臺筆電上跑開源權重模型 Qwen,OpenCode 透過 opencode.json 設定檔連到 Ollama 的本機服務(http://127.0.0.1:11434/v1)。作者強調只啟用本機 provider,設定也會在編輯檔案或執行指令前要求確認,並封鎖網頁工具。另一個可替代方案是 Aider,同樣支援 Ollama,但這次 walkthrough 全程使用 OpenCode 以保持設定與結果一致。

作者選擇的模型是 Qwen3.5 9B。依 Qwen 官方 model card 公開的數據,9B 版本在 LiveCodeBench v6(程式碼生成)與 BFCL-V4(function calling,評估模型能否選對工具並給出正確參數)上的表現優於 4B 版本,因此被選為這次實測的起點。作者也提醒,這些是官方公開分數,不是這臺筆電的實測結果,真正的檢驗要看離線情境下的檔案修改與測試結果。記憶體方面,社群工具 Voltti 建議 Qwen3.5 9B(6.6GB 的建置版本)需要 12 至 16GB 記憶體,而這次使用的 64k token 設定可能需要更多,得預留空間給 context 與其他應用程式。

📊 數據:別人的 benchmark,不是這次的實測結果

作者引用了一篇研究預印本《The Scaffold Effect in Coding Agents》,該研究在 50 個 Terminal-Bench Pro 任務上,用雲端模型比較了 OpenCode、Goose 與 OpenHands-SDK 的表現,但作者特別提醒,論文作者自己指出大部分 pass rate 的差異在統計上並不明顯。該研究還指出一個具體數字:OpenCode 的 token 使用量明顯偏高,每完成一個任務大約是 Goose 的 40 倍。作者強調這些測試用的是雲端 API 與不同模型,不能用來預測本機 Qwen3.5 9B 的實際表現。

🧪 實測流程:從斷網檢查到修一個 bug

作者設計了一個簡單的測試專案:一支計算支出總額的 expense_total.py,正確答案應為 25.50,但程式執行後只印出 8.00,原因是加總邏輯在迴圈中被覆寫而非累加。既有測試中,小數運算、退款與範例支出三個案例會失敗,空輸入與單筆輸入則正常,這讓作者有了一個明確且可獨立驗證的修 bug 目標。

在仍連網的狀態下,作者先用診斷提示「讀取 expense_total.py 並執行測試,在不修改任何程式碼的情況下解釋這個 bug」確認 Qwen3.5 9B 能正常回應。過程中 agent 一度誤判測試框架,提議用 pytest,但這個專案其實用的是 Python 內建的 unittest,權限提示讓作者能在執行前先檢查指令是否正確。

確認本機服務可用後,作者關閉 Wi-Fi、拔掉網路線,並確認 Ollama 的本機 API(localhost)仍正常回應且列出已下載的 qwen3.5:9b 模型,而對外部網址的請求則回報「無法解析主機」,確認網路確實中斷。接著在完全離線狀態下重新啟動 OpenCode,agent 提出了一行修正,並在請求權限執行測試後完成修復;因為改動幅度很小,整個過程很容易檢查。

🎯 實務啟示

這次實測說明,只要模型、專案依賴與測試工具都已經下載到本機,像是解釋程式、抓 bug、小幅重構這類日常任務,確實可以在完全離線的環境下完成,這對網路不穩定的工作場景(出差、長途交通,或像作者一樣住在訊號不穩的地方)是個實用的備援方案。但要注意,benchmark 數字來自官方 model card 與其他研究團隊在雲端模型上的測試,並不直接等同於自己筆電上的實際體驗,真正可靠的驗證方式,還是像作者一樣用自己的測試案例跑一遍。

🔗 來源
- 標題:Coding From the Himalayas With an Offline AI Agent
- 作者/機構:Latent Space
- 連結:https://latent.space/p/offline-coding/

#AI #CodingAgent #OpenSource #Ollama #Qwen #OfflineAI #LocalLLM #DeveloperTools #EdgeComputing #LLM
