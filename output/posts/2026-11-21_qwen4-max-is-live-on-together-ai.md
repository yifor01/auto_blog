---
title: Qwen4 Max is live on Together AI
source: Together AI
url: https://www.together.ai/blog/qwen4-max
model: claude-code/sonnet
generated_at: '2026-11-21T22:24:07.156250'
score: 81
---

📌 【阿里巴巴 Qwen4 Max】百萬 Token 一次讀完整個 Repo，修好一個 Bug只要 69 美分

TL;DR：Together AI 上架 Qwen4 Max，用 1M 上下文一次餵進整個程式庫修 bug，不用檢索也能定位正確修法。

修 bug 的標準流程通常是先篩選相關檔案、做 retrieval，再把精選內容塞進 prompt。這次 Together AI 的示範反過來做：把整個開源專案的 344 個檔案原封不動丟進一次請求，完全不做檢索，看模型自己能不能找到答案。

🤔 **一個真實的 bug，一整個 repo**

Together AI 把 Qwen4 Max 上架到 Together Serverless Inference，提供 1M token 的上下文窗口。測試用的是 Python 網頁框架 Tornado 的完整程式庫：344 個檔案、652,519 個 tokens，對應到 Tornado 維護者在 2026 年 11 月 18 日（即 Qwen4 Max 發布兩天後）送出的一個真實修復，測試時使用的是該次 commit 之前的程式碼狀態。模型沒有任何工具，也沒有人工挑選相關檔案，bug report 只描述症狀：websocket 連線關閉時，未被 await 的 write_message() 呼叫會誤報「Task exception was never retrieved」錯誤。

🧩 **模型自己找到了關鍵的參照寫法**

第一個 token 在 54 秒後出現，72 秒後完整輸出結束。Qwen4 Max 把問題定位到 tornado/websocket.py 中的 WebSocketProtocol13.write_message，並提出修法：把例外標記為「已被取回」，讓沒被查看的例外不再誤報，但仍保留給真正 await 該呼叫的呼叫端應有的錯誤。更值得注意的是，模型在解釋中提到這個修法應該採用跟 tornado/iostream.py 裡 BaseIOStream.write 相同的處理方式——而 bug report 從未提及這個檔案，Tornado 維護者自己的修復 commit 恰好也引用了同一段程式碼作為參照。

📊 **通過全部 1,673 項測試**

Together AI 用 Tornado 維護者針對這個 bug 新增的兩個 regression 測試驗證：修復前的程式碼會讓其中一個測試失敗，套用模型產生的修補後兩個測試都通過。接著再跑 Tornado 的完整測試套件，共 1,673 項測試，套用修補後沒有任何一項失敗。

💡 **成本與 prompt caching 的落差**

這次請求在促銷價下約花費 69 美分（原價則約 98 美分），幾乎全部花在 652,519 個輸入 tokens 上。促銷期（至 2026 年 11 月 22 日）的價格為每百萬輸入 tokens 1.05 美元、每百萬快取輸入 tokens 0.0525 美元、每百萬輸出 tokens 3.15 美元（原價分別為 1.50、0.075、4.50 美元）。Together AI 會自動快取 prompt 輸入，文中提到重複送出約 630,000 tokens 的同一份內容時，幾乎全部命中快取，第一個 token 出現時間從 54 秒降到 8 秒，輸入成本也從約 66 美分降到約 3 美分。

⚠️ **使用上的限制**

在 Together AI 上，Qwen4 Max 只接受串流（streaming）請求；thinking（推理）功能預設開啟，推理過程的 tokens 會被計入輸出 tokens 計費，若要跳過可額外傳入 reasoning 參數關閉。Alibaba 於 2026 年 11 月 16 日發布 Qwen4 Max，官方描述其為「Qwen 家族迄今最強模型」，定位於長時間 agent 工作，包含跨大型程式庫的程式開發。模型架構為稀疏混合專家（MoE），總參數 2.4 兆、每個 token 啟用 71 億參數。在 Alibaba 自家的 Work360 基準（涵蓋 721 個專業領域）上，官方宣稱整體表現優於 Qwen3.8 Max，在高推理強度下省下 35% tokens，平均每個任務成本降低約 60%——這些數字均為 Alibaba 官方公布的數據。

🎯 **對工程團隊的參考價值**

對需要在大型程式庫裡定位跨檔案問題的團隊，這個案例說明了超長上下文窗口搭配自動 prompt caching 的組合，能讓「整包程式庫丟進去」這種原本不切實際的做法變得可行，尤其在需要反覆查詢同一份程式碼基底時，快取能大幅壓低重複呼叫的成本與延遲。模型目前以 Qwen/Qwen4-Max 的名稱在 Together Serverless Inference 上提供，支援 1M 上下文、文字與圖片輸入。

🔗 **來源**
- 標題：Qwen4 Max is live on Together AI
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/qwen4-max

#Qwen #Alibaba #TogetherAI #LLM #LongContext #CodeGeneration #OpenSourceAI #MoE #AIInference #DeveloperTools
