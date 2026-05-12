---
title: "microsoft/data-formulator"
source: GitHub Trending
url: https://github.com/microsoft/data-formulator
score: 134
model: tencent/hy3-preview:free
generated_at: 2026-05-12T20:21:25.309717
---

📌 **microsoft/data-formulator：AI 驅動的資料視覺化平台**

你是否曾在切換不同資料來源、調整圖表樣式、以及嘗試從過去的分析中累積經驗時感到費時？Data Formulator 試圖用一個具備對話記憶的 AI 代理人，將資料連接、探索、視覺化與知識沉澱整合在同一個工作流程中。

🤔 **資料探索需要反覆切換工具與記住先前發現**

傳統的資料分析流程常需要在 SQL 編輯器、BI 工具、notebook 以及圖表設計器之間來回切換。每次換工具都意味著失去先前的思考脈絡，而重複建立相同的過濾條件或樣式調整則佔據了不少時間。此外，團隊成員難以將個人會話中的技巧（例如特定的過濾組合或圖表調整方式）有效地共享給後續的分析師。

🧪 **多來源連接器 + 對話式代理人 + 持久工作區**

Data Formulator 0.7（alpha 2）提供以下核心功能：

- **資料連接器**：支援 Superset、Kusto、Cosmos DB、MySQL、PostgreSQL、MSSQL、S3、Azure Blob、BigQuery 等，具備 SSO、惰性目錄載入、搜尋與智慧過濾器。
- **Conversational Agent with Thread Memory**：統一的 DataAgent 能在同一對話線程中進行說明、探索、視覺化與建議，並保持跨輪對話的上下文。
- **Persistent Session & Workspace Management**：以身份隔離的工作區，支援本機與 Azure Blob 兩種後端，工作階段在重啟後仍能保留時間戳與排序。
- **Expressive Visualization**：透過新增的語義圖表引擎提供 30+ 圖表類型（區域圖、流形圖、K 線圖、餅圖、雷達圖、地圖等），並配備圖表樣式精煉代理人，可透過自然語言一次調整字體、顏色、佈局與標註。
- **Knowledge Distillation（實驗性）**：代理人會從每次會話中提煉可重複使用的技巧與經驗，存入共享知識庫，以供未來的會話參考。

安裝方式（預發布版）：  
`pip install --pre data-formulator`  
或鎖定特定版本：`pip install data-formulator==0.7.0a2`

💡 **一個能記住對話的代理人讓探索更連貫**

因為代理人具備線程記憶，使用者可以在同一對話中先要求「顯示上月銷售依區域分布」，然後自然地追問「把低於 10 萬的區域隱藏起來」，接著再說「把這張圖改成藍色調並加上標題」。這種上下文貫穿減少了重新說明需求的成本，也讓探索過程更像是與同事討論而非反覆下指令。

⚠️ **仍處於早期階段，功能為實驗性與預發布版**

- 目前版本為 0.7.0 alpha 2，屬於預發布（pre‑release）階段，可能仍有錯誤或變動。
- Knowledge Distillation 功能標示為實驗性，尚未保證在所有場景下都能產出可靠的可重複使用知識。
- 某些進階圖表類型或樣式調整可能仍依賴於後續版本的完善。

🎯 **適合希望將 AI 融入日常資料工作流程的分析師與資料科學家**

如果你的團隊正在評估能減少工具切換、保持思考連續性並逐步累積最佳實踐的平台，Data Formulator 提供了一個可嘗試的起點。建議先在非關鍵專案上安裝 alpha 版，觀察對話式代理人在實際探索會話中的使用感受，並注意官方文件對於知識庫與持久工作區的最新說明。

🔗 **專案連結**  
📦 GitHub：https://github.com/microsoft/data-formulator  

你有試過在資料分析中使用具備對話記憶的 AI 代理人嗎？歡迎在留言區分享你的經驗或疑問 👇

#AI #DataVisualization #DataFormulator #Microsoft #資料探索 #機器學習 #開源工具 #資料科學 #GitHubTrending
