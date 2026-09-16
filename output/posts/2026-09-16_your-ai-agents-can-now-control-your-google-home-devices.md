---
title: Your AI agents can now control your Google Home devices
source: TechCrunch AI
url: https://techcrunch.com/2026/09/16/your-ai-agents-can-now-control-your-google-home-devices/
model: claude-code/sonnet
generated_at: '2026-09-16T20:26:00.461566'
score: 76
---

📌 Google Home 開放 MCP,讓 Claude、ChatGPT 都能操控你家智慧設備

TL;DR：Google Home 推出 MCP server 早期存取,任何支援 MCP 的 AI agent 都能安全連接並控制智慧家庭裝置。

當你的 AI 助理不只能幫你寫程式碼,還能直接幫你調暗客廳的燈、查看門口攝影機的每日摘要,智慧家庭的入口正在從 app 轉移到對話框。Google 本週宣布,旗下 Home 生態系統正式開放 Model Context Protocol(MCP)server 的早期存取。

🤔 **從單一助理到多元 agent 的智慧家庭**

這項更新讓任何支援 MCP 的 AI agent,包括 Claude、Hermes、OpenClaw、ChatGPT 與 Google 自家的 Antigravity,都能安全地與使用者的智慧家庭裝置互動,並存取設備的事件歷史紀錄。使用者可以用自然語言指令,查看攝影機摘要、監控智慧家庭活動、控制連接的裝置,甚至打造自己專屬的智慧家庭儀表板。

🧩 **設定流程:從 Google Cloud 專案開始**

要啟用這項功能,使用者需要先建立一個 Google Cloud 專案並設定使用 Home MCP,接著將 MCP 的設定資訊提供給自己選用的 agent,並要求該 agent 完成連接設定。agent 接著會引導使用者登入並授權存取權限。Google 也表示,將在 Google Home Developer Center 提供完整的設定指南。

這套系統支援 Google Home 生態系統中的所有裝置類型,包括 Google Nest 門鈴、溫控器,以及所有支援「Works with Google Home」(也就是 Matter 標準)的裝置,例如智慧燈泡。

📊 **限時開放給付費訂閱用戶**

根據報導,這項存取權限將從本週三開始,於未來幾週內陸續開放,目前僅限美國地區訂閱 Google Home Premium Advanced(月費 20 美元)的用戶。這個較高階的訂閱方案原本就提供更長的事件式影片歷史紀錄、描述性通知與詳細警報、影片歷史搜尋工具、每日摘要等功能。Google 並未說明是否、或何時會將 MCP 開放給其他訂閱層級或其他市場的用戶。

Google 也透過其 Smart Home for Developers Community,向早期採用者徵求回饋意見,顯示這項功能目前仍處於持續調整階段。

值得一提的是,MCP 目前已是 Google 產品線中的重複佈局,先前已在 Google Cloud、資料平臺、開發者工具與 Google Workspace 中支援過同樣的協定,這次則是首度將觸角延伸到消費者端的智慧家庭產品。

🎯 **實務啟示**

對開發 agent 應用的工程師來說,這是又一個主流平臺採用 MCP 作為標準連接介面的案例,意味著同一套 MCP client 邏輯,理論上可以跨 Google Cloud、Workspace 與 Home 等多個產品線重複使用。若你正在打造跨裝置的個人 agent 助理,值得留意 Google Home Developer Center 即將釋出的設定指南與 API 細節。

🔗 **來源**
- 標題：Your AI agents can now control your Google Home devices
- 作者／機構：Sarah Perez, TechCrunch AI
- 連結：https://techcrunch.com/2026/09/16/your-ai-agents-can-now-control-your-google-home-devices/

#GoogleHome #MCP #ModelContextProtocol #SmartHome #AIAgents #Claude #ChatGPT #IoT #Automation #GoogleCloud
