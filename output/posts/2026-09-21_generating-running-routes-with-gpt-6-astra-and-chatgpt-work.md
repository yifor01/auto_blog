---
title: Generating running routes with GPT-6 Astra and ChatGPT Work
source: Simon Willison
url: https://simonwillison.net/2026/Sep/12/astra-running-routes/
model: claude-code/sonnet
generated_at: '2026-09-21T21:22:24.422430'
score: 74
---

📌 GPT-6 Astra 花 27 分鐘規劃跑步路線，卻交不出自己寫的程式碼

TL;DR：Simon Willison 實測 ChatGPT Work 用 GPT-6 Astra 產生路跑路線，卻因對話壓縮而拿不回原始程式碼。

叫一個 AI agent 幫你規劃 5K、10K 跑步路線，聽起來是個討喜的小任務。結果它確實做到了，還附上互動地圖與可下載的 GPX、GeoJSON 檔案。但當 Simon Willison 事後想看看它到底是怎麼算出這條路線時，卻撞上了一個看似技術細節、實則牽動所有 agent 系統設計的問題。

🤔 **一個看似完美的任務**

Willison 給 ChatGPT Work（搭載 GPT-6 Astra Max）的指令很簡單：告訴它自己家的地址，要求規劃從家裡出發再繞回來的 5K 與 10K 跑步路線，並且要用 OSM（OpenStreetMap）資料。Agent 花了 27 分鐘運作，產出的結果完全符合要求：一份嵌入式的視覺化地圖，加上可下載的 GPX 與 GeoJSON 檔案。

🧩 **它是怎麼做到的**

當被問到具體作法，ChatGPT 回答：用 Nominatim 定位地址，用 Overpass 下載當地 OpenStreetMap 的道路與步道資料,然後在本地端計算出迴圈路線。地圖的呈現則是透過內建的 visualize skill，產生一個名為 `/workspace/el-granada-5k-share.html` 的檔案直接嵌入 ChatGPT 介面，其中包含渲染路線與地圖所需的完整幾何資料，並使用從白名單 CDN 載入的 D3.js 來畫圖。

⚠️ **壓縮吃掉了原始程式碼**

問題出在後續：當 Willison 想要那段實際執行的 Python 程式碼副本時，ChatGPT 卻給不出來了。原因似乎是對話串已經被「壓縮」（compacted）過，原始的程式碼內容因此遺失。Willison 直接把這一點定性為「反功能」（anti-feature）：使用者原本以為 agent 執行過程是可回溯、可稽核的，結果因為系統內部的上下文管理機制，事後連自己要求它做的事到底怎麼做的都拿不回來。

💡 **給所有做 agent 系統的工程師的提醒**

Willison 提出一個明確的設計建議：任何採用壓縮（compaction）機制的 LLM 系統，都應該同時保留壓縮前的原始文字，並讓這份文字能透過 agent 的工具呼叫（tool calls）被取用。換句話說，壓縮可以拿來節省上下文視窗的空間，但不該變成一道單向門，把使用者原本能看到的執行細節就此鎖死。這對正在自建 agent 框架、尤其是會做長任務、多輪工具呼叫並帶壓縮機制的團隊來說,是一個值得提前設計進去的稽核需求。

🎯 **實務啟示**

如果你的 agent 系統會執行程式碼、呼叫外部工具，並且有上下文壓縮或摘要機制，這個案例提醒你：務必把「原始執行紀錄」與「呈現給使用者的摘要」分開儲存,並且保留可事後查詢的介面，而不是只靠模型當下的記憶去回答「你剛剛做了什麼」。對於需要可稽核性（例如金融、醫療場景的 agent 應用）,這不是錦上添花的功能，而是基本要求。

🔗 **來源**
- 標題：Generating running routes with GPT-6 Astra and ChatGPT Work
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Sep/12/astra-running-routes/

#GPT6 #ChatGPT #AIAgents #LLM #Astra #AgentTransparency #OpenStreetMap #PromptEngineering #AIProductivity #ContextCompaction
