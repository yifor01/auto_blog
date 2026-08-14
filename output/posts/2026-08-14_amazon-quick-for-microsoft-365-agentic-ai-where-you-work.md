---
title: 'Amazon Quick for Microsoft 365: Agentic AI where you work'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/amazon-quick-for-microsoft-365-agentic-ai-where-you-work/
model: claude-code/sonnet
generated_at: '2026-08-14T07:34:30.483341'
score: 72
---

📌 Amazon Quick 進駐 Word、Excel、PowerPoint、Outlook

TL;DR：Amazon Quick 推出 Microsoft 365 擴展，把連接資料與 agentic 編輯能力直接搬進日常辦公軟體。

企業的資料散落在數十個系統裡，但真正的工作往往還是在 Microsoft 365 裡完成。Amazon Quick 這次選擇的做法，不是把使用者拉去新工具，而是把 AI 助理直接送進使用者早已打開的視窗。

🤔 **不換工具，直接把 AI 帶進既有介面**

Amazon Quick 現在推出可安裝於 Word、Excel、PowerPoint、Outlook（桌面版與網頁版皆可）的擴展，Plus、Professional 或 Enterprise 方案的客戶無需額外授權即可使用。這些擴展把使用者原本在 Quick 中設定的 Quick Sight 儀表板、Spaces、AWS 資料來源以及 Salesforce、Jira、Slack、SharePoint 等第三方整合，直接帶進 Word、Excel、PowerPoint、Outlook，不必離開這些應用程式本身。

🧩 **不是問答機器人，而是會動手編輯的 agent**

在 Word 中，Quick 以常駐側邊面板呈現，使用者從功能區開啟後提問或下指令，agent 能在文件情境內找尋並替換文字、插入段落、重新排版內容,完成後會顯示一份視覺化的異動比較，每一次 agent 的動作都會被記錄成稽核軌跡（audit trail），並附上可回溯到受影響內容的參照連結。對話紀錄也不會因為關閉面板而消失，在 Outlook 中，每一封郵件串都有各自獨立且持續保留的對話紀錄，切換不同郵件串時，擴展會記得每個串的對話內容。

在 Excel 中，使用者可以請 agent 分析目前工作表、標記出月增率超過 10% 的異常，或把 Quick Sight 儀表板中的季度營收依地區拉進新的分頁；遇到複雜公式時，也可以請 agent 解釋公式並追蹤其相依關係，最後再請 agent 建立圖表比較實際值與預測值。文章作者本人的工作流程也提到，過去需要團隊花幾週才能彙整完成的客戶提案回覆，現在可以在幾小時內完成初稿；原本要一到兩天完成的客製化簡報，現在能在一小時內整合結構化與非結構化資料來源完成。

🧩 **部署方式：零用戶端安裝，管理員一次推送**

這些擴展完全在雲端執行，用戶端不需要安裝任何東西。管理員可以透過 Microsoft 365 管理中心，用標準的 manifest 機制將套件推送給指定使用者與群組，這與其他 Microsoft 365 增益集的部署方式相同；使用者也可以自行從 Microsoft 增益集商店搜尋「Quick」並自行安裝。無論哪種方式，之後的更新都會自動推播，不需要 IT 再次介入。唯一的例外是 Outlook，由於大多數組織會限制 Graph API 權限，Outlook 擴展通常需要管理員核准才能取得完整功能。驗證機制使用 Quick 原生身分驗證，不需要額外建立 Entra 應用程式；若使用 Free 或 Plus 方案，也可以用企業帳號或 Google、Apple 社群登入，不需要另外設定身分系統。目前擴展可在美國東部（維吉尼亞北部）、美國西部（奧勒岡）、歐洲（愛爾蘭）、歐洲（倫敦）、歐洲（法蘭克福）、亞太（雪梨）、亞太（東京）共七個 AWS 區域使用，資料留在所選區域內，後端基礎架構完全隔離且不對外連網。

🎯 **實務啟示**

對於已經在使用 Amazon Quick 的企業，這次的擴展等於是把既有的 Spaces、儀表板與整合原封不動地延伸進 Microsoft 365，不需要重新建置知識庫或串接。值得留意的是 Outlook 需要額外的管理員審核流程，規劃部署時間表時應提前納入。

🔗 **來源**
- 標題：Amazon Quick for Microsoft 365: Agentic AI where you work
- 作者／機構：Art Chan，AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/amazon-quick-for-microsoft-365-agentic-ai-where-you-work/

#AmazonQuick #AWS #Microsoft365 #AgenticAI #Excel #Outlook #EnterpriseAI #Productivity #MCP #CloudAI
