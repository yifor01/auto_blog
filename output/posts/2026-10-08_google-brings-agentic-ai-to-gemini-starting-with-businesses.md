---
title: Google brings agentic AI to Gemini, starting with businesses
source: TechCrunch AI
url: https://techcrunch.com/2026/10/08/google-brings-agentic-ai-to-gemini-starting-with-businesses/
model: claude-code/sonnet
generated_at: '2026-10-08T22:29:15.595396'
score: 80
---

📌 Gemini 導入 agentic 功能，先從企業端下手

TL;DR：Google 把 Gemini 做成能跨平臺「代辦事情」的 agent，優先開放給企業客戶。

當 ChatGPT 有 Dots、Meta 有 Muse，Google 這次沒有選擇先討好一般消費者，而是把新的 agentic 能力直接丟進企業的工作流程裡——這個順序本身就是個訊號。

🤔 從「回答問題」到「把事情做完」

Google Cloud 於週四的活動上宣布，將為 Gemini 推出一個統一的 agent，除了回答問題之外，還能代替使用者實際完成任務。這呼應了整體產業的趨勢：AI 工具正從單純的對話體驗，轉向能主動接下任務、產生程式碼、安排會議、預訂行程等「把事情做完」的角色，也跟上了 Meta Muse、Instinct 等訊息類 agent，以及 ChatGPT Dots 的腳步。

Google CEO Sundar Pichai 在活動開場提到，Gemini 目前已有超過 10 億月活躍使用者，而近 90% 的《財星》100 大企業已在使用 Gemini Enterprise。正因企業端採用率已高，Google 選擇先在商業場景落地，之後才推向一般消費者；Pichai 表示，這麼做能先解決「安全性、規模、效能方面較難的問題」。

🧩 給目標，不只是給指令

Google Cloud CEO Thomas Kurian 說明，這個新 agent 可以被賦予「目標，而不只是指令」：它能自行規劃工作、呼叫自訂技能與工具，並連接企業內部系統來完成目標。預設情況下 AI 會自動挑選最適合的模型執行任務，但使用者也能手動選擇模型，第一步開放的第三方模型就是 Anthropic 的 Claude 系列，Google 表示未來會再擴大到開源模型與其他私有模型。

請求內容可以附加檔案、資料夾，或是結合檔案與技能的特定工作流程專案。這個 agent 能連接 Google Workspace、Microsoft 365、Slack、Jira、Confluence、Git、BigQuery、Databricks、Postgres、Snowflake 等系統，也能與公司網路內外任何 Model Context Protocol（MCP）伺服器安全互動。使用者可以透過「任務收件匣」介面，追蹤 Gemini 的思考過程、subagent 任務分派、技能載入與進度。

值得注意的是，這個 agent 擁有自己的 Workspace 帳號，就像另一位同事：有自己的 email、自己的 context，知道公司裡誰在哪個團隊、時區、誰需要核准事項，以及行事曆資訊。使用者可以透過標記、寄信、分享或拉進群組聊天來呼叫它，而它採取的每個行動都會寫入歸屬於該 agent（而非某個人）的稽核紀錄。此功能可在 iOS、Android、Windows、Mac 桌面、CLI、Google Workspace、Microsoft 365、ServiceNow 與 Slack 上使用。

📊 早期測試者與企業客戶

Google 提到早期測試者包括運動品牌 On、Shopify 與 PayPal；Gemini Enterprise 的客戶名單則包括 BNP Paribas、Bradesco、Merck、Orange Spain、Santee Cooper、SOMPO、Ulta Beauty 與 Wesfarmers。同時，Google 也推出新的彈性付費選項，包括多模型協同調度、智慧路由與即時花費上限，協助企業控管 AI 支出。

💡 產品敘事多於架構細節

整篇發布內容偏向描述 agent 能連接哪些系統、在哪些平臺可用，以及企業客戶名單，但對於這個統一 agent 背後的技術實作——例如規劃模組如何運作、subagent 之間如何協調——並未提供太多細節。這讓這次發布讀起來更像是一次產品與市場定位的宣告，具體的技術差異仍待後續觀察。

🎯 實務啟示

對企業內的工程團隊而言，值得關注的重點是模型選擇權（包含可指定 Anthropic Claude）與 MCP 相容性，這代表既有的 MCP 工具生態系有機會直接銜接上 Gemini 的企業版 agent，而不必重新打造整合層。

🔗 來源
- 標題：Google brings agentic AI to Gemini, starting with businesses
- 作者／機構：Sarah Perez（TechCrunch AI）
- 連結：https://techcrunch.com/2026/10/08/google-brings-agentic-ai-to-gemini-starting-with-businesses/

#Gemini #GoogleCloud #AgenticAI #EnterpriseAI #MCP #Anthropic #Claude #AIAgents #GoogleWorkspace #TechNews
