---
title: Google will now let any AI agent run your smart home
source: The Verge AI
url: https://www.theverge.com/tech/996310/google-home-mcp-integration-agentic-ai-smart-home-price-release-date
model: claude-code/sonnet
generated_at: '2026-09-16T20:26:00.461661'
score: 71
---

📌 Google 把智慧家庭的控制權,交給任何一個 AI agent

TL;DR：Google Home MCP 整合開放第三方 agent 分析居家資料、控制裝置並打造自訂儀表板,是 Google 佈局智慧家庭基礎設施層的關鍵一步。

「如果這禮拜的新聞頭條不是清一色在講 AI 可能毀滅人類,我應該會對這個消息感到非常興奮。」The Verge 資深編輯 Jennifer Pattison Tuohy 在報導 Google Home 新整合功能時,這樣寫道。她口中的功能,是 Google 對智慧家庭生態系統的一次重大開放:讓 Claude、Open Claw 等第三方 AI agent,直接存取並控制你家中的裝置與資料。

🤔 **不是取代 Gemini for Home,而是疊加一層新的控制介面**

根據報導,Google Home 智慧喇叭仍將由 Gemini for Home 負責控制,MCP 整合並不會取代這個介面。Google Home & Nest 的產品經理 Taylor Lehman 在部落格文章中表示,Home MCP 整合會讓 AI agent 連接到真實世界的事件,開啟一系列新的應用情境,例如跨攝影機分析(讓你的 agent 回答「小孩放學回家後做了什麼」這類問題),或是利用裝置狀態歷史紀錄,回答「上週洗了幾次衣服」「燈開了多久」這類問題。

MCP 啟用後,第三方 agent 甚至能透過 Google Home 喇叭以語音方式與使用者互動,例如在完成任務後主動發送語音通知。使用者也可以讓 agent 建立自訂儀表板來控制整個 Google Home 系統。

🧩 **安全防護:agent 目前無法解鎖你家大門**

報導特別指出,把 AI agent 接上智慧鎖、溫控器、HVAC 系統等核心居家基礎設施,自然引發資安、隱私與安全性方面的疑慮。Google 表示,Home MCP 內建速率限制與安全防護機制,舉例來說,agent 目前無法透過這個介面解鎖房門。不過 Lehman 也提醒,根據所使用的 agent 不同,連接 Home MCP 仍可能導致非預期甚至不理想的行為,建議使用者詳閱 Google 的開發者政策與服務條款。

報導也提到,開源智慧家庭平臺 Home Assistant 先前已推出類似的 MCP 整合。作者本人曾在去年實測用 Claude 透過 Home Assistant 的 MCP 完成「vibe coding」智慧家庭,親身體驗到 agent 能輕鬆處理故障排除、建立自動化規則、設計儀表板、以自然語言完成進階設定等多數介面(甚至多數使用者)都感到吃力的任務。

📊 **開放時程與定價與素材 3 相同**

與 Home MCP 相關的定價與時程資訊:目前僅限美國地區訂閱 Google Home Premium Advanced(月費 20 美元、年費 200 美元)的用戶,存取權限將於未來幾週內陸續開放,設定流程同樣需要先建立 Google Cloud 專案並配置 Home MCP。

💡 **這是 Google 在智慧家庭基礎設施層的長期布局**

報導的深入分析指出,這次整合的意義不只是「透過 Claude app 開關電燈」這麼單純,更重要的是 Claude(或使用者選擇的任何 agent)現在能存取智慧家庭底層的資料與控制層。作者將此類比為 Google 想成為智慧家庭領域的 AWS:Google 提供 AI 與智慧家庭基礎設施,其他公司則在其上打造面向消費者的服務與產品。文中也提到,Google 已在 2024 年開放智慧家庭 API 存取,近期又推出全端的 Gemini for Home,顯示這是一套持續多年的基礎設施策略,而不是單一次性的功能更新。

⚠️ **Google 過去平臺屢屢半途而廢的紀錄**

報導也直言不諱地指出一個現實隱憂:Google 過去推出並放棄的智慧家庭平臺不在少數,包括 Android@Home、Weave、Project Brillo、Works with Nest,乃至於已經走入歷史的 Google Assistant。這段紀錄意味著,開發者是否願意押注 Google 這次真的會堅持到底,仍是一個懸而未決的問題。

🎯 **實務啟示**

對於正在評估是否把產品深度整合進特定智慧家庭生態系的開發者而言,MCP 作為標準協定確實降低了跨平臺接入的門檻,但 Google 智慧家庭平臺過往的「半途而廢史」提醒我們,選擇長期依賴單一廠商基礎設施前,仍值得評估替代方案(例如報導中提到、已支援 MCP 的開源方案 Home Assistant)的成熟度與延續性。

🔗 **來源**
- 標題：Google will now let any AI agent run your smart home
- 作者／機構：Jennifer Pattison Tuohy, The Verge
- 連結：https://www.theverge.com/tech/996310/google-home-mcp-integration-agentic-ai-smart-home-price-release-date

#GoogleHome #MCP #ModelContextProtocol #SmartHome #AIAgents #Claude #GeminiForHome #IoT #SmartHomeInfrastructure #HomeAssistant
