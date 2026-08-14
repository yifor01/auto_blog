---
title: Building a Streaming Local AI Agent
source: KDnuggets
url: https://www.kdnuggets.com/building-a-streaming-local-ai-agent
model: claude-code/sonnet
generated_at: '2026-08-14T07:29:53.481901'
score: 89
---

📌 打造本地端 Streaming AI Agent：兩階段過濾術省下算力

TL;DR：本地 Ollama Agent 監看維基百科編輯，兩階段過濾省算力。

「Streaming」這個詞在 Agent 語境裡其實有兩種意思，一種是 Agent 持續接收即時事件流而不是等人輸入訊息，另一種是 Agent 的輸出逐字元串流而不是等一大段話生成完才顯示。KDnuggets 這篇教學指出，多數教學只做了其中一種，這次的範例則刻意兩者都做，因為它們解決的是兩個不同的問題，一個真正「常駐」的 Agent 兩者都需要。

🤔 常駐型 Agent：由事件喚醒，而非等人開口

文章借用了「ambient agent」的框架來描述這種設計，LangChain 將其定義為「由事件觸發，而非由人類訊息觸發」，Google 的 Agent Development Kit 則從基礎設施角度描述類似概念：Agent 是被串流上抵達的東西喚醒，而不是坐等請求、回應式的呼叫。

這次的範例場景很具體：一個完全在本機執行的 Agent，透過 Ollama 監看維基百科公開、即時的編輯事件流，判斷哪些編輯疑似是破壞行為（vandalism），全程不需要任何 API Key。前置需求是 Python 3.11 以上、本機安裝好 Ollama 並拉取一個支援結構化 JSON 輸出的模型（例如 llama3.1:8b），以及安裝 fastapi、uvicorn、httpx、pydantic、ollama、sse-starlette 等套件，除了自家電費，沒有任何雲端帳號或額外成本，唯一對外連線的對象是維基百科公開、不需驗證的 EventStreams 端點。

🧩 最關鍵的設計決策：一個兩階段漏斗

維基百科的編輯事件流量相當大，活躍時段跨所有語言版本合計每秒能推送好幾筆編輯。文章指出，如果把每一筆事件都丟給語言模型處理，會同時發生兩件壞事：機器算力被浪費在根本不有趣的編輯上，而且 Agent 會跟不上它原本該即時監看的事件流，徹底違背「常駐」這個設計初衷。

解法是一個兩階段漏斗，也是整個專案最重要的設計：第一階段完全是便宜的純 Python 數學運算，不涉及任何模型，針對每一筆事件計算刪除了多少位元組、該使用者最近幾分鐘內編輯了幾次，絕大多數編輯都很無聊，而判斷「無聊」是不花錢的。第二階段才是真正的本地 LLM，只對第一階段篩選後、觸發門檻的少數事件才會被喚醒，文章形容這正是任何監控系統的共通原則：前端用便宜的過濾器，把昂貴的推理留給真正通過篩選的候選者。

專案目錄拆成 stream_source.py、filters.py、agent.py、broadcaster.py、config.py、schemas.py、main.py 等檔案，每個檔案剛好對應漏斗的一個階段，方便獨立理解與測試。stream_source.py 負責消費維基百科以 Server-Sent Events 形式透過純 HTTP 推送的編輯事件，不需金鑰、也不需額外的握手動作。文章特別提到一個實作細節：維基百科的事件流本身並沒有明確標示「這是不是匿名使用者」的欄位，匿名編輯是以編輯者的 IP 位址作為使用者名稱，所以程式碼改用正規表示式判斷使用者名稱是否長得像 IPv4 或 IPv6 位址來偵測匿名編輯，這個判斷方式在作者撰寫測試時，也抓到了先前草稿裡的一個真實錯誤。連線邏輯包在一個永久迴圈中，遇到 HTTP 錯誤就等待五秒後自動重連，避免一次網路波動就讓整個服務中斷，這對號稱「常駐」的服務很重要。

filters.py 中的 EditVelocityTracker 類別會用滑動視窗追蹤每個使用者最近的編輯時間戳記，藉此抓出短時間內連續大量編輯的異常行為，而不只是抓單一次的大量刪除。為了避免記憶體無限成長，這個追蹤器會設定 max_tracked 上限，把太舊的使用者資料淘汰掉。

💡 這套漏斗模式的通用性

這個「便宜過濾在前、昂貴推理在後」的架構，並不是維基百科監看場景獨有的技巧，而是任何要用 LLM 處理高流量事件流的系統都會遇到的取捨。把規則型判斷放在第一線，能讓真正需要模型推理的請求量下降好幾個數量級，這也是讓一個完全跑在本機、沒有雲端算力支援的 Agent 能夠跟上即時事件流的關鍵。

🎯 實務啟示

如果你想打造一個真正常駐、而不是等人下指令才動作的 Agent，這篇教學提供了一個可以直接照搬的骨架：先用零成本的規則過濾掉大部分事件，只把少數真正可疑的候選交給本地或雲端模型判斷，同時搭配自動重連機制，讓服務能夠真正長時間無人值守運作。對於想控制 LLM 呼叫成本、又需要處理高頻事件流的場景，這個兩階段漏斗值得直接借鏡。

🔗 來源
- 標題：Building a Streaming Local AI Agent
- 作者／機構：Shittu Olumide
- 連結：https://www.kdnuggets.com/building-a-streaming-local-ai-agent

#AIAgent #Streaming #Ollama #LocalLLM #AmbientAgent #Python #EventDriven #Wikipedia #OpenSource #LLMEngineering
