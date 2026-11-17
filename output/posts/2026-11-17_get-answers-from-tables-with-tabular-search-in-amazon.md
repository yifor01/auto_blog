---
title: Get answers from tables with tabular search in Amazon Bedrock Managed Knowledge
  Base
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/get-answers-from-tables-with-tabular-search-in-amazon-bedrock-managed-knowledge-base/
model: claude-code/sonnet
generated_at: '2026-11-17T01:10:00.487289'
score: 83
---

📌 Bedrock 知識庫新增表格搜尋，RAG 終於能跨列算數字

TL;DR：Amazon Bedrock Managed Knowledge Base 新增 tabular search，agentic retrieval 現在能對 CSV/Excel 執行程式碼計算，不再只是檢索片段。

財務團隊月底結帳時問一句「哪些部門需要寫 variance commentary（差異說明）」，答案卻散落在三個地方：差異政策的門檻、季末備忘錄的預算調整、還有整張 P&L 工作表裡每個部門的數字。傳統 RAG 擅長比對文字段落，面對這種需要「先查規則、再對整張表算一遍」的問題，往往無能為力。AWS 這次針對這個落差，在 Bedrock Managed Knowledge Base 裡加入了 tabular search。

🤔 **表格被切成段落檢索，資訊天生就會流失**

RAG 回傳固定數量、與問題最相似的段落，這種做法對文章內容有效，但表格依形狀切片時會丟失上下文：一列數字脫離欄位標題和單位後，檢索出來的片段可能完全看不懂。更麻煩的是用語落差——使用者問的是「controllable spend（可控支出）」，表格裡存的卻是 cost center 代碼和帳目名稱；而賦予這些數字意義的規則，通常寫在另一份政策文件裡，不是表格本身。此外，草稿版工作表和正式版在語意檢索上看起來幾乎一樣，純檢索很難分辨。

🧩 **把工作拆開：檢索找檔案，程式碼讀整張表**

Tabular search 的核心思路是把任務拆成兩段：檢索只需要負責找到「對的那個檔案」裡的一個段落，剩下的計算交給程式碼讀取整張原始表格。整個流程走的是既有的 AgenticRetrieveStream 請求：

1. 應用程式送出問題，agentic retrieval 先透過檢索判斷哪些文件和表格檔案相關；
2. 若取回的段落來自 CSV、XLSX 或 XLS，且問題需要跨列計算或查特定值，就會觸發 tabular search；
3. 系統把相關的表格檔案送進一個沙箱——沒有網路存取，模型在裡面寫程式碼讀取原始檔案；
4. 程式碼執行並印出結果，與文件中檢索到的事實一起組成答案；
5. 答案連同引用來源、以及記載程式碼讀取了哪個檔案的 trace 事件，串流回應用程式。

這套流程對任何把檔案帶進知識庫的連接器都適用，包括 Amazon S3、Microsoft SharePoint、Atlassian Confluence 等。值得注意的是，只有 AgenticRetrieveStream 才會跑程式碼，單純的 Retrieve API 仍然只回傳段落，不會執行計算；而程式碼執行預設隨 generateResponse 一起開啟，若手動關閉該參數，則只拿回檢索結果，不跑程式碼。

📊 **範例：政策門檻加上預算調整才能算出答案**

AWS 用 AnyCompany Retail 的虛構財務檔案示範。其中一個問題是「本季支出是否仍在修訂後預算之內」——這個預算只存在於備忘錄的調整之後。答案結合了備忘錄的預算修訂，以及工作表裡的 Q3 實際支出與原始預算，得出支出比修訂後預算少了 49,572.40 美元，因此答案是「是」，即便同一筆支出其實已超過原始預算。若只用純檢索，拿到的備忘錄與工作表段落裡根本沒有這些數字。

開頭提到的完整問題，則需要把差異政策門檻（超過核定預算 5%，含核准修訂）、備忘錄裡 Marketing 增加與 Engineering 削減的調整，以及工作表數字三者串起來，最終算出 Sales 部門差異為 -6.50% 屬於需要說明的範圍。

⚠️ **不是萬能：多一次 agent 回合，也不取代 BI**

跑程式碼至少會多一個 agent turn，所以牽涉表格計算的回答會比純文字回答慢；長時間呼叫時，串流會每 10 秒重複一次 IN_PROGRESS 事件避免逾時，若某個程式碼步驟跑不完則回報 FAILED，agent 通常會重試或改走其他路徑。AWS 也明確提醒：治理級指標、常態性儀表板、倉儲規模的 join 運算，以及報表控制，仍然該交給正規 BI 工具，tabular search 定位在「表格檔案就放在文件旁邊、不想另外定義 schema」的場景。

🎯 **實務啟示**

對在做企業知識庫或 RAG 系統的工程師來說，重點是：把表格和相關文件放在同一個前綴或資料來源下，讓檢索能先命中正確檔案；問問題時具名提到文件和表格檔案，有助於檢索先鎖定目標；第一次同步後務必確認檔案型別被正確判定為表格，再送出需要計算的問題。AWS 在 sample-managed-knowledge-base-patterns 的 GitHub repo 裡提供了 CDK 部署範例與測試腳本，值得先跑一遍再評估是否套用到自己的資料。

🔗 **來源**
- 標題：Get answers from tables with tabular search in Amazon Bedrock Managed Knowledge Base
- 作者／機構：Josh DeMuth @ AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/get-answers-from-tables-with-tabular-search-in-amazon-bedrock-managed-knowledge-base/

#AWS #AmazonBedrock #RAG #KnowledgeBase #AgenticRetrieval #TabularData #LLM #EnterpriseAI #CloudComputing #MachineLearning
