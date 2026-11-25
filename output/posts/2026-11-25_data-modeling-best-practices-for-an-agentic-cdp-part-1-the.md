---
title: 'Data Modeling Best Practices for an Agentic CDP, Part 1: The Data Foundation'
source: Databricks
url: https://www.databricks.com/blog/agentic-cdp-data-modeling-data-foundation
model: claude-code/sonnet
generated_at: '2026-11-25T01:52:58.174954'
score: 71
---

📌 【Databricks】打造 Agentic CDP，資料地基怎麼蓋

TL;DR：Databricks 揭露 Agentic CDP 的資料建模法，身分解析成為 gold 層的關鍵 join key。

一位顧客 9 天前把一件外套加進願望清單，今天早上它降價 30%。要不要通知他？這個看似簡單的決定，agent 必須在幾秒內拿到六類資料的答案才能下判斷——而大多數公司的資料架構，根本撐不起這種速度。

🤔 傳統 CDP 夠用嗎？Agentic CDP 要的是「對一個人」的即時決策

Databricks 指出，Agentic CDP 仍然需要傳統 CDP 的一切：正確的來源、乾淨的資料、每人一個身分、行銷信任的黃金檔案（golden profile）。差別在於由誰做、多快要做對。傳統做法是「區隔，定期重新整理」；Agentic 做法是「針對單一個人，隨時決策」。Agent 負責比對紀錄、擬草稿這類重活，人類負責選來源、審核比對結果、核准最終輸出。一個資料缺口，幾秒內就會變成一個錯誤決策，這點和傳統 CDP 的風險等級完全不同。

🧩 架構核心：medallion 架構裡，身分解析跑在 silver 之後

Databricks 建議的資料流是一個 medallion 架構，但有一條硬規則：identity resolution 在 silver 層清理完資料之後、gold 層建立之前執行，產生的 canonical ID 成為 gold 層所有表的 join key。整條管線用 Spark Declarative Pipelines 建層、Lakeflow Jobs 排程、Unity Catalog 治理每一層。Databricks 自家的 CustomerLake 產品就是依循同一套邏輯：資料團隊透過 Databricks 與 Unity Catalog 一次定義好信任資料集與模型，行銷端再用專用介面問問題、建 audience、活化，不必再繞過 IT 或把資料匯出到管不到的工具裡。

身分解析的做法是：先跑 deterministic 規則（精確比對 email、電話、能對應到顧客 ID 的 partner ID），再用 probabilistic matching 對缺口打分，接著把比對結果聚類，產生或保留一個 persistent ID。這一步可以自己用 SQL 規則加開源 matcher（如 Splink 或 Zingg）搭建，也可以用 CustomerLake 的 Profile Agents 處理比對與黃金紀錄存續（survivorship）的重活。Databricks 把這套結合 deterministic、probabilistic 與 LLM-based matching 的做法稱為「Agentic Identity Resolution」，並保留人工資料管理員（data steward）覆寫的空間。每一筆合併背後的規則與信心分數，都記錄在一張叫 id_graph 的表裡——Databricks 直言這是整個架構裡最重要的一張表。

💡 consent 與行為資料：一張表管同意，event 表要分清新鮮度

同意（consent）的做法是：在 silver 層保留完整歷史，每人、每個管道、每個目的、每個來源、每個時間點都是一行，退訂與退信這類抑制清單（suppression）也放在這裡，再由此派生出一張 1:1 的 consent 表，讓 audience 建構和 agent 在發送前都查這一張表，而不是各自判斷。

Gold 層的每張表還要標記新鮮度：批次（batch）資料按排程更新，事件（event）資料則隨事件即時進來、一行對應一個時間戳記，像網站與 App 行為、購物車、交易，或是購物車提醒這類即時觸發判斷都屬於這一類。事件表用 Spark Declarative Pipelines 的 streaming table 建，新鮮度標記記錄成 Unity Catalog 的 tag；像購物車提醒這種觸發式場景，要用 continuous 模式維持資料即時更新。只按排程進來的行為（例如夜間門店銷售）則維持 batch，等到真的串流化才轉換。另外兩個好習慣：用宣告好的 as-of 日期計算時間窗，確保重跑結果一致；只維護一份治理過的資料拷貝，每個活化工具只拿它需要的表。

🎯 架構到位之後，決策只定義一次

有了這套模型，一個 audience 或一個決策只要在治理過的 gold 表上定義一次，就能送到顧客實際使用的管道。CustomerLake 用原生 Reverse ETL connector 直接把 audience 與訊號同步到 martech、adtech、CX 管道，不需要客製 pipeline 或額外的活化層。

⚠️ 這篇是 Databricks 自家視角的最佳實踐指南，具體把哪些資料集對應到文章開頭六個問題，作者表示會留到系列文章的第二篇說明，目前讀到的只有架構原則，還沒有實際案例的驗證數字。

🔗 來源
- 標題：Data Modeling Best Practices for an Agentic CDP, Part 1: The Data Foundation
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/agentic-cdp-data-modeling-data-foundation

#Databricks #AgenticAI #CDP #DataModeling #IdentityResolution #DataEngineering #Lakehouse #UnityCatalog #MarTech #CustomerData
