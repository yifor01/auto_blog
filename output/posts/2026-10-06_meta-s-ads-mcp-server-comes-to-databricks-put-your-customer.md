---
title: 'Meta’s ads MCP server comes to Databricks: Put your customer intelligence
  to work in advertising campaigns'
source: Databricks
url: https://www.databricks.com/blog/meta-ads-mcp-databricks
model: claude-code/sonnet
generated_at: '2026-10-06T22:05:57.182929'
score: 68
---

📌 Meta 廣告工具搬進 Databricks，數據團隊與投放團隊終於同桌

TL;DR：Meta 的 ads MCP server 上架 Databricks Marketplace，讓行銷團隊能用自然語言直接拿企業資料驅動 Meta 投放操作。

每週一早上，媒體投放團隊盯著 Meta Ads Manager 調預算，數據團隊的流失預測模型、LTV 分數卻躺在另一套系統裡，兩邊靠 CSV 匯出或每週例會才對得上話。這次 Meta 與 Databricks 的整合，想解決的正是這個老問題。

🤔 **洞察與決策之間，永遠差一個手動搬資料的步驟**

根據 Databricks 官方部落格，企業內常見情境是：流失模型已上線、LTV 分數能辨識高價值客戶、歸因資料能看出哪支創意帶來營收，但這些洞察要真正影響廣告預算分配，仍得靠人工匯出、自建 Marketing API 整合，或每週同步會議「寄望」洞察被採納。

🧩 **MCP 把 Meta 廣告操作變成 Genie 對話裡的一個工具**

MCP（Model Context Protocol）是讓 AI 代理人呼叫工具與資料來源的開放標準。Meta 的 ads MCP server 透過 Databricks Marketplace 提供，暴露超過 25 項涵蓋廣告生命週期的工具：建立廣告活動與廣告組、調整預算與出價、定義受眾、管理素材與產品目錄、拉取成效數據、診斷訊號品質等。接上 Databricks 的 Genie One 後，行銷人員可以直接提問，例如「用我們的流失風險分數找出高價值且有流失風險的客戶，用每日 8000 美元預算啟動一個挽留活動」，Genie One 會同時搜尋企業內部資料與 Meta 工具，再建立對應的廣告活動。另一個情境是預算分配：毛利數據留在 Databricks，廣告花費與投遞指標留在 Meta，有了兩邊存取權的代理人就能建議把預算移往真正帶來獲利營收、而非單純便宜轉換的廣告組。若企業已透過 Conversions API 把轉換事件送到 Meta，這套整合還能讓代理人存取訊號診斷，包括事件量、Event Match Quality、資料新鮮度，方便判斷「購買事件下降是銷售變差，還是資料管線出了問題」。

⚠️ **權限不是提示詞禮貌拜託，而是伺服器端強制卡控**

文中特別強調治理層面：在 Databricks，管理員透過 Unity Catalog 控制 Meta 連線的存取權限，Unity Gateway 負責治理工具呼叫並記錄使用與稽核日誌；在 Meta 端，廣告主可在 Business Settings 設定規則，例如封鎖超過 20% 的預算調漲，或完全禁止在特定帳號建立廣告活動。文章強調，這些規則是在每次工具呼叫前被伺服器端檢查執行，違規會被擋下並回傳結構化錯誤，而不是靠模型「自律」，且規則也能透過 Marketing API 批量管理，適合同時操作上百個廣告帳號的團隊。

🎯 **實務啟示**

這本質上是一則產品上架公告，價值大小取決於你的企業是否「已經」在 Databricks 裡有成熟的客戶分數與歸因資料。如果答案是有，這條路徑確實把洞察到投放決策之間的手動搬資料步驟去掉了；如果企業還沒建立起這些模型與治理基礎，這次整合本身並不會替你補上那塊地基，單純接上 MCP 不等於自動產生好的投放策略。

🔗 **來源**
- 標題：Meta's ads MCP server comes to Databricks: Put your customer intelligence to work in advertising campaigns
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/meta-ads-mcp-databricks

#MCP #Databricks #Meta #AdTech #Genie #UnityCatalog #MarketingAI #DataPlatform #AgenticAI #CustomerIntelligence
