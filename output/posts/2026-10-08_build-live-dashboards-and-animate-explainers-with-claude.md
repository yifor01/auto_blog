---
title: Build live dashboards and animate explainers with Claude
source: Claude Blog
url: https://claude.com/resources/articles/dashboards-and-motion
model: claude-code/sonnet
generated_at: '2026-10-08T22:26:01.940766'
score: 86
---

📌 Claude 新增即時 Dashboard 與程式碼動畫，資料問答不再要寫 SQL

TL;DR：Claude Dashboards 直連 BigQuery 等資料平臺即時產圖，Claude Motion 用程式碼生成可編輯動畫。

問公司資料常常要先開一張 ticket、等人寫 SQL；想做一段動畫說明，最後往往又變成另一張靜態投影片。Anthropic 這次直接把這兩個「等待」的環節拿掉。

🧩 **Claude Dashboards：接上資料庫，直接用白話問問題**

Claude Dashboards 可以連接 Amazon Redshift、BigQuery、ClickHouse、Databricks、Snowflake 等資料平臺，或是 Salesforce 這類 CRM 工具，用自然語言問問題，Claude 會從資料中拉出答案、建出 Dashboard，並隨資料更新持續保持最新狀態。每張圖表都能點開看背後的查詢語句，也能直接請 Claude 解釋查詢邏輯，每張圖還會標示資料最後更新的時間。目前是在付費方案上公測，官方定位是用來處理「這週註冊數和上個月比怎樣」這類探索性、快問快答的場景；若需要更深入的分析，Dashboard 可以直接送到 Amplitude、Grafana、Hex、Mixpanel、Omni、Perplexity、PostHog 或 Sigma 接手，Looker、monday.com、Tableau 則表示即將支援。

🧩 **Claude Motion：把報表變成可編輯的動畫，不是生成影片**

Claude Motion 可以把一份季報變成全員會議用的 30 秒說明動畫，或是在董事會投影片的圖表上加動態效果，目前在 Team 與 Enterprise 方案上公測。關鍵設計是：Claude Motion 寫的是會animate文字、圖表、形狀與圖片的程式碼，而不是呼叫影片生成模型，所以不會有生成的影像片段，也沒有 AI 生成的人物。使用者可以在編輯器裡調整，或直接請 Claude 改動畫，完成後下載成 MP4。想進一步加工，還能匯出到 Adobe、Descript、HeyGen、Higgsfield、invideo、Luma AI、Runway，Canva 與 Captions 也即將支援。

🧩 **Docs、Slides、Design 正式脫離公測**

Anthropic 表示自從把 Docs、Slides、Design 整合進 Claude 對話之後，使用者已經累積做出超過 4500 萬份文件、投影片與設計稿。這次更新把三者的 beta 標籤拿掉，並補上企業向功能：Artifacts 支援 CMEK 加密、管理員可以指定組織可用的 artifact 範本、團隊能共同編輯同一份文件／Dashboard、分享範圍可以擴大到組織外部、匯出的 PowerPoint／PDF 會保留編輯器裡的排版，甚至能直接變成可編輯的 Google Slides 檔案，手機上也能直接編輯。獨立站 claude.ai/design 會在 12 月 14 日關閉，現有設計系統需要透過 Artifacts 頁面的「Migrate team design systems」一次性搬移過去，專案本身在關閉前不需要任何動作，但聊天紀錄與留言不會被保留。

⚠️ **企業版預設關閉，需要手動開啟**

Dashboards 和 Motion 對 Enterprise 管理員來說預設是關閉的，需要在組織設定的 Artifacts 分頁手動開啟；Docs、Slides、Design 則會在 10 月 15 日自動開啟，也可以提前手動開啟。

🎯 **實務啟示**

對工程師與資料分析角色來說，Claude Dashboards 降低了「臨時想知道一個數字」的門檻，省去開 ticket 或臨時寫 SQL 的往返成本，但官方自己也把它定位為探索性工具，複雜分析仍要交給既有 BI 系統；Claude Motion 因為輸出是可編輯程式碼而不是生成影片，意味著動畫的每個細節都可以被追溯與修改，這對需要頻繁更新同一份說明素材的團隊會比一次性生成影片更實用。

🔗 **來源**
- 標題：Build live dashboards and animate explainers with Claude
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/dashboards-and-motion

#Claude #Anthropic #DataVisualization #BusinessIntelligence #Dashboards #AIProductivity #BigQuery #Snowflake #Databricks #Automation
