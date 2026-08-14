---
title: Automate legacy web applications with Amazon Bedrock AgentCore Browser Tool
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/automate-legacy-web-applications-with-amazon-bedrock-agentcore-browser-tool/
model: claude-code/sonnet
generated_at: '2026-08-14T07:29:53.481995'
score: 89
---

📌 用受控瀏覽器讓 AI 代理操作老舊網頁系統，補上傳統 RPA 的缺口

TL;DR：AWS 用受控瀏覽器讓 AI 代理操作老舊系統，取代脆弱 RPA。

一家大型保險公司，每年要在老舊保單管理系統上處理數萬筆異動，包括保單條款修改、理賠調整、保障內容更新與批註，每一筆異動都得在多個畫面間切換、輸入資料並驗證商業規則，光是人工作業就要耗費數千小時，還因人為疏失造成可觀的年度損失。AWS 這篇文章要解決的正是這類場景：多數企業的關鍵系統仍跑在只吐出 HTML、由伺服器端中介軟體產生介面的老舊應用上，既沒有現代 API 可接，傳統 RPA 又常常在這種介面上失靈。

🤔 傳統 RPA 為什麼搞不定老舊系統

文章歸納出三個讓傳統 RPA 難以規模化的技術挑戰。第一是老舊系統整合的複雜度：這些系統多半是數十年前用伺服器端中介軟體打造，只產生給瀏覽器用的 HTML、CSS 與 JavaScript，缺乏現代 REST API，還帶有複雜的多步驟工作流程、動態表單驗證與依賴 session 狀態的機制；歷經多年修改後文件也常有缺口，關鍵商業邏輯往往只存在於員工的經驗裡而非系統規格文件中。認證機制更是雪上加霜：有些系統要求多因子驗證，有些用專屬的單一登入，還有些依賴到期規則難以預測的 session token，規則型的 RPA 機器人在這類情境下經常力不從心，導致正式上線後仍需要大量人工介入。

第二是法遵要求：受監管產業必須為 GDPR、HIPAA 與各項金融法規建立完整稽核軌跡，記錄使用者身分、時間戳記、資料異動與系統互動，這需要不可竄改的日誌系統、加密傳輸與角色權限控管，傳統 RPA 若不額外客製開發很難達成。文章特別提到，金融法規要求紀錄保存六年且不可竄改，最近 90 天的紀錄還必須能立即調閱，每一筆保單異動都必須能追溯到是誰發起、改了什麼、何時發生、是否經過核准。

第三是規模化限制：以 UI 為基礎的自動化，對畫面版型、元件位置與應用程式反應時間有脆弱的依賴關係，規則型 RPA 無法處理例外狀況、動態內容或需要認知判斷的複雜商業流程，加上機器人通常得綁定專屬虛擬機或實體主機，同時處理多個流程時 session 管理會變得複雜，錯誤復原機制也只能涵蓋預先定義好的情境。文中提到的保險公司每年要處理數萬筆保單異動，在投保旺季、法規變動或年底結算等尖峰時段，讓傳統 RPA 撐住規模與可靠度被證明並不實際。

🧩 用受控瀏覽器，讓代理像人一樣操作網頁

Amazon Bedrock AgentCore Browser Tool 提供的是一個全代管、雲端運行的瀏覽器服務，讓 AI 代理透過安全隔離的瀏覽器 session 操作老舊網頁介面。它透過 Playwright，以 WebSocket 為基礎的 Chrome DevTools Protocol（CDP）連線，因此不論老舊系統原本是為哪種瀏覽器設計，只要能透過 HTTP 或 HTTPS 存取，代理就能操作。Browser Tool 本身在雲端執行一個受管理的 Chromium 執行個體。

搭配 Strands Agents 做模型驅動的任務編排後，這套架構可以從單步驟自動化擴展到複雜的多代理工作流，並透過 Amazon Bedrock AgentCore runtime 串接 Bedrock 基礎模型，以 IAM 提供 session 隔離的安全性與完整稽核軌跡。

文章給出的參考實作，由幾個職責清楚劃分的元件組成：給操作人員使用的 React 單頁應用、解決特定瀏覽器限制的 TLS 終止代理、在 AgentCore runtime 上運行 Strands Agents 的 Python worker，以及 AgentCore Browser Tool 提供的受管瀏覽器環境，登入與身分驗證則交給 Amazon Cognito 處理，由它簽發流經整套系統的 JWT。

📊 設計目標鎖定治理與彈性伸縮

文章明確列出這套架構要滿足的條件：能處理 JavaScript 密集的網頁介面、在流程之間隔離 session、透過 API 開放程式化控制、對每一次互動做不可竄改的日誌記錄、在信心不足時交還給人工判斷，並且能彈性伸縮。完整原始碼與 Terraform 部署方案已公開在 GitHub 上供參考。

💡 創新點在工程落地，而非新技術本身

嚴格來說，用瀏覽器自動化操作老舊系統並不是新概念，這篇文章的價值更多在於把 AgentCore Browser Tool、Strands Agents、IAM 與稽核日誌組合成一套針對高度監管產業設計的生產級參考架構，尤其是把「信心不足時交還人工」與「六年不可竄改紀錄保存」這類治理需求直接寫進架構設計裡，而不是事後補救，這對金融、醫療等受監管產業的工程團隊來說，可能比技術本身更有參考價值。

🎯 實務啟示

如果你的團隊也在為只有 HTML 介面、缺乏 API 的老舊系統煩惱，這套架構提供了一個可以參考的落地路徑：與其繼續投資脆弱的規則型 RPA，不如評估用受控瀏覽器搭配 LLM 驅動的代理，把稽核軌跡、session 隔離與人工覆核機制在架構層就設計進去，而非事後補丁。

🔗 來源
- 標題：Automate legacy web applications with Amazon Bedrock AgentCore Browser Tool
- 作者／機構：Salman Moghal
- 連結：https://aws.amazon.com/blogs/machine-learning/automate-legacy-web-applications-with-amazon-bedrock-agentcore-browser-tool/

#AWS #BedrockAgentCore #RPA #BrowserAutomation #StrandsAgents #LegacySystems #EnterpriseAI #Compliance #Playwright #AIagents
