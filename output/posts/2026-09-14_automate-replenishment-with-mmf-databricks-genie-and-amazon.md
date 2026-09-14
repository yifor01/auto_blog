---
title: Automate replenishment with MMF, Databricks Genie, and Amazon Quick
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/automate-replenishment-with-mmf-databricks-genie-and-amazon-quick/
model: claude-code/sonnet
generated_at: '2026-09-14T21:09:47.700895'
score: 81
---

📌 補貨自動化實戰：用 Databricks Genie 串接 Amazon Quick 自動下單

TL;DR：AWS 技術文件示範如何用 Databricks Genie Agent 偵測需求異常，再讓 Amazon Quick 自動比對供應商並下單，全程可用附帶的程式庫重現。

零售補貨最怕的不是預測不準,而是預測太慢生效。當計劃人員把預測匯出、對照供應商庫存、再逐一處理數萬個 SKU（stock keeping unit,庫存單位）時,賣得最快的商品早就已經缺貨。這篇 AWS Machine Learning Blog 的文章要解決的,正是「預測做得再好,也來不及變成訂單」的落差。

🤔 預測系統與下單系統,從來不是同一套

作者指出,基礎模型（foundation model）已經解決了預測本身的難題,能在不需逐項調校的情況下對整個商品目錄做需求預測。真正的瓶頸移到了下游:預測結果存放在受治理的資料平臺裡,供應商的即時庫存卻在另一套維運系統中,而負責下單的人往往兩邊都沒有登入權限。這篇文章要補上的,就是這段「偵測、決策、行動」之間缺失的自動化迴路,而且僅在沒有規則可循時才升級給真人處理。

🧩 Databricks 做智慧判斷,Amazon Quick 負責動手

整套方案分成四個階段:Forecast（預測）由 Databricks 端負責一次性完成,之後 Detect（偵測）、Decide（決策）、Act（行動）三個階段則由 Amazon Quick 依排程反覆執行。

具體的角色分工是:
- Databricks 這一側跑 MMF accelerator 附帶的 fresh_retail_net 範例,用 Chronos-2 做零樣本（zero-shot）預測,產出的表格再透過一個 Databricks Genie Agent 對外開放,讓使用者能用自然語言詢問「哪裡出現需求激增」。
- Amazon Quick 是唯一同時碰到「預測世界」和「行動世界」的元件。它透過 Model Context Protocol（MCP）的 Genie 連接器讀取預測,用 Amazon QuickSight 把 Amazon S3 Tables 裡的供應商即時庫存讀成一個 Direct Query 資料集,再由 Amazon Quick Flows 以共同的 retailer_product_id 對齊需求與供給,最後透過 OpenAPI 連接器呼叫供應商訂單 API 下單,規則對不上時就轉開一張例外工單。

文章特別強調,這套架構刻意不把所有資料搬進同一個資料倉儲,而是在決策當下用共同的商品鍵值把兩邊的資料接起來,Databricks 產生智慧,Amazon Quick 負責行動。

⚠️ 重現前要先過兩道帳戶層級的關卡

要跑通這套流程,環境準備並不輕鬆。文中列出的前置需求包括:Databricks CLI 0.299.0 以上、AWS CLI 2.36.2 以上、jq 1.7,以及跑供應商資料載入器要用的 uv 或 Python 3.11。更關鍵的是兩個帳戶層級的門檻:Amazon Quick 使用者必須是 Author 或 Author Pro 角色（因為 Quick Flows 與 MCP/OpenAPI 連接器都需要這個等級的權限),而 Databricks 身分則需要在 metastore 上有 CREATE CATALOG 權限,否則就得請管理員先建好 mmf catalog。

註冊供 Amazon Quick 存取 Genie Agent 的 OAuth 應用程式,是一個帳戶層級（account-level)的動作,權限高於一般工作區操作,若不是 Databricks 帳戶管理員,得請管理員代為執行並拿到 client ID 與 secret,且該 secret 只會顯示一次。

附帶的程式庫提供兩個腳本涵蓋幾乎所有可自動化的步驟:setup_databricks.sh(建立 notebook、Genie Agent、OAuth 應用程式)與 setup_aws.sh(建立訂單 API、S3 供應商資料、Quick 帳戶、資料來源、空間與流程),但兩者都會在四個只能在主控臺完成的步驟前暫停,包括兩個行動連接器、S3 Tables 存取授權與資料集設定。供應商資料本身是從公開的 FreshRetailNet-50K 商品鍵值衍生出的合成供應商目錄,存放在 Amazon S3 Tables(Apache Iceberg)中,與預測資料完全獨立。

🎯 實務啟示

這篇文章示範的其實是一種常見但常被低估的整合難題:當「智慧」與「行動」分別長在不同系統裡,真正的自動化瓶頸往往不是模型能力,而是打通權限、資料鍵值與排程的工程細節。對正在評估類似補貨或供應鏈自動化場景的工程團隊,這份可重現的參考架構(以及明確列出的帳戶前置需求)比單純的預測模型示範更有實作參考價值。

🔗 來源
- 標題：Automate replenishment with MMF, Databricks Genie, and Amazon Quick
- 作者／機構：Venkatavaradhan Viswanathan(AWS Machine Learning Blog)
- 連結：https://aws.amazon.com/blogs/machine-learning/automate-replenishment-with-mmf-databricks-genie-and-amazon-quick/

#AWS #Databricks #AmazonQuick #RetailAI #DemandForecasting #SupplyChain #Chronos2 #MCP #GenAI #Automation
