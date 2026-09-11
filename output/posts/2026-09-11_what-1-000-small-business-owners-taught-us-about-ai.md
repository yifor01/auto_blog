---
title: What 1,000 small business owners taught us about AI
source: Claude Blog
url: https://claude.com/blog/what-1-000-small-business-owners-taught-us-about-ai
model: claude-code/sonnet
generated_at: '2026-09-11T19:47:55.062389'
pinned: true
---

📌 【Anthropic 官方分享】走訪 10 座城市、上千位老闆後,Claude 團隊學到的三件事

TL;DR:Anthropic 巡迴 10 個城市辦工作坊,訪談上千位中小企業主,整理出 AI 導入中小企業的三個關鍵洞察。

當所有 AI 工具都在瞄準財星 500 大與新創獨角獸時,一個問題被長期忽略:貢獻美國 44% GDP、僱用近半私部門勞動力的中小企業,誰來教他們用 AI?Anthropic 這次決定親自下場找答案。

🤔 **從一個 plugin 到一場十城巡迴**

今年五月,Anthropic 推出 Claude for Small Business,一款與 QuickBooks、PayPal、HubSpot、Canva、DocuSign 等中小企業常用工具整合的 Claude Cowork plugin,同時與 PayPal 合作推出「AI Fluency for Small Businesses」課程。隨後六週,Anthropic 團隊與建置夥伴 Tenex 在芝加哥、土爾沙、達拉斯、紐澤西 Hamilton Township、巴頓魯治、伯明罕、鹽湖城、巴爾的摩、聖荷西與印第安納波利斯舉辦免費半天工作坊,每場約 100 位企業主參加,累計超過 1,000 人參與。登記者中八成企業規模落在 5 到 50 人,產業集中在營建、製造、物流、技術工種等實體經濟領域。

🧩 **非技術背景的老闆,也能自己動手打造工具**

最讓團隊意外的模式,是許多完全沒有軟體背景的企業主開始用 AI 打造針對自身痛點的客製工具。芝加哥油漆承包商 Tony Severino 從 1984 年獨立開業至今,現在讓 Claude 逐層讀取 PDF 藍圖來協助估價;達拉斯郊區一家工業系統整合商的現場技師,拍下未標示的零件照片,Claude 幾秒內就能辨識出來,取代過去要花上數小時的人工比對流程。印第安納州三廠拖車製造商 Liberty Trailers 的老闆 Mike Teso,在約 15 分鐘內就為新收購的工廠建好一套對帳工具,原本堅持「不需要 AI」的 IT 主管也因此在幾天內把紙本生產排程換成即時儀表板。

📊 **重要的工作交給 AI,但老闆們仍擔心準確度**

企業主提出的需求裡,約三分之二與「維持營運」有關,三分之一與「成長業務」有關,而報告彙整是除行銷工作外最常見的需求。田納西州一家五人的貨運合規顧問公司,在市場下滑中流失六成客戶,又被核心軟體供應商提前 30 天通知終止服務,團隊用 Claude 自行重建系統,把燃油稅申報錯誤率從 7% 降到零,現在能以相同的五人團隊處理過去尖峰量兩倍的業務。不過幾乎每一場工作坊都聽到同一種焦慮:擔心重要的事情被 AI 漏掉。因此不少企業主養成了「像對待新員工一樣」逐步建立信任的習慣,例如 Broadcast Blinds 老闆 Rick Smith 現在會提示 Claude 標明哪些是假設、哪些是確定的資訊;Severino 也曾抓到 Claude 在估價時誤用樓地板面積乘數而非實際牆面尺寸,此後固定要求 Claude「show me your work」。

⚠️ **資料安全與治理,是採用 AI 前最先被問到的問題**

在正式launch前的調查中,503 位中小企業決策者裡,資料安全是被提及最多的採用障礙。每一場工作坊,關於資料隱私、安全與治理的問題永遠最先被提出:我的資料會不會被拿去訓練模型?連接 QuickBooks 後 Claude 到底能看到什麼?如果 agent 幫忙瀏覽網頁,會不會被惡意網頁挾持?產品數據顯示,對連接工具有信心的企業主能獲得遠高於平均的價值,一旦心存疑慮,採用就會停滯。走得比較前面的企業,做法是刻意把人留在決策鏈上:印第安納 40 人工程顧問公司 KBSO Consulting 讓新進員工逐一審查 Claude 產出的摘要,作為在職訓練的一環;紐澤西一家夫妻檔品牌顧問公司自動化了整條提案到簽約流程,但保留人工按下「寄出」的最後一步;達拉斯 20 人的後勤外包公司 HireEffect 經手客戶薪資資料,上線前先建好 PII 遮蔽機制與 Claude 工作流程登記清單。

🎯 **實務啟示**

這篇分享對正在推廣或導入 AI 工具的團隊有兩個具體提醒:第一,信任不是靠一次性的安全聲明建立的,而是靠可觀察、可追溯的使用習慣(如要求模型標明假設 vs. 事實、保留人工核可節點)逐步累積;第二,權限設計應該延續既有的存取邊界,而非額外開放,例如文中提到員工在 QuickBooks 看不到的資料,透過 Claude 也不應該看得到。這對任何要把 LLM 接入企業內部系統的工程團隊,都是值得直接複用的設計原則。

🔗 **來源**
- 標題:What 1,000 small business owners taught us about AI
- 作者/機構:Lina Ochman,Anthropic
- 連結:https://claude.com/blog/what-1-000-small-business-owners-taught-us-about-ai

#Anthropic #Claude #SmallBusiness #AIAdoption #EnterpriseAI #AIFluency #DataPrivacy #Automation #SMB #AIGovernance
