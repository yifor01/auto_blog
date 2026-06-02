---
title: "TinyFish Launches BigSet: An Open-Source Multi-Agent System That Builds Structured Live Datasets from Plain-English Descriptions"
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/02/tinyfish-launches-bigset-an-open-source-multi-agent-system-that-builds-structured-live-datasets-from-plain-english-descriptions/
score: 88
model: tencent/hy3-preview:free
generated_at: 2026-06-02T22:06:02.404109
---

📌 **BigSet：用英文描述即時建構結構化資料集**

想要一份即時更新的 YC 公司招聘表？過去你得寫爬蟲、設計 schema、處理重複、排程更新…現在只要說一句話。  
BigSet 讓純文字需求直接變成可下載的 CSV 或 XLSX，免去傳統 ETL 管線的繁瑣步驟。

🤔 **網路資料結構化仍是管線問題**  
從網頁抓取結構化資料傳統上需要確定資料來源、寫或設定爬蟲、設計 schema、去重、排程更新，並在來源網站變更時修復斷裂。無論執行一次或一百次，這個流程幾乎不變，佔據了工程師大量的維護時間。

🧪 **兩層代理人架構：schema 推論 + 即時網路代理人**  
BigSet 採用開源多代理人系統（AGPL-3.0 授權），分為兩個階段。第一階段，使用 Claude Sonnet（經 OpenRouter 呼叫）將自然語言描述轉換為資料表 schema，包括欄位名稱、資料類型、主鍵以及應該在哪裡尋找資料。第二階段，派遣網路代理人執行實際的網頁搜尋、頁面擷取與資料驗證，完成去重後產出可下載的檔案。系統不只是單一 LLM 加上網路搜尋工具，而是明確的兩層流程。

🔑 **純文字輸入即可產出即時資料表**  
使用者只需輸入一句話，例如：「YC companies that are currently hiring engineers, with their funding stage, location, and number of open roles」。BigSet 會自動推論對應的欄位，從網路上尋找符合條件的實體，填入資料列，並產出 CSV 或 XLSX。排程更新功能允許設定 30 分鐘、6 小時、12 小時、每日或每週的重新執行，讓資料表保持最新而無需手動再次觸發任務。實際產生時間約為 2–5 分鐘，因為代理人正在進行真實的網路研究。

💡 **低程式碼替代傳統 ETL 的實用价值**  
對於需要快速取得最新表格的工程師而言，BigSet 提供了一種不必撰寫爬蟲、維護 selector 或處理斷裂的低程式碼方案。其開源特性使得社群可以自行部署與擴充，而 AGPL-3.0 授權則需要注意在商業環境中的使用限制。

⚠️ **依賴外部模型與產生延遲為主要限制**  
schema 推論階段依賴 Claude Sonnet 透過 OpenRouter 存取，這意味著效能與成本受第三方服務影響。此外，資料集產生需要 2–5 分鐘，無法達到即時回應，對於對延遲極度敏感的場景可能不適合。這些事實均來自原始說明，未進行額外效能基準測試。

🎯 **適合快速原型與內部資料需求的工具**  
若您需要快速建立並定期更新的結構化資料表，且能接受數分鐘的產生時間，BigSet 值得嘗試。建議先閱讀專案的 README 了解安裝方式與授權細節，再依實際需求評估其在您工作流中的定位。

🔗 **資料來源**  
📝 TinyFish Launches BigSet: An Open-Source Multi-Agent System That Builds Structured Live Datasets from Plain-English Descriptions  
👤 Asif Razzaq (MarkTechPost)  
🔗 https://www.marktechpost.com/2026/06/02/tinyfish-launches-bigset-an-open-source-multi-agent-system-that-builds-structured-live-datasets-from-plain-english-descriptions/  
（完整程式碼於文中所述 GitHub 倉庫可取得）  

#BigSet #AI Agents #資料工程 #開源 #TinyFish #LowCode #網路爬蟲 #AutoETL
