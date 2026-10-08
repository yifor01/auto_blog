---
title: 'Building Reliable Data Analytics Agents: Lessons from the KDD Cup'
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/building-reliable-data-analytics-agents-lessons-from-the-kdd-cup/
model: claude-code/sonnet
generated_at: '2026-10-08T22:21:21.251632'
score: 92
---

📌 KDD Cup 亞軍的秘訣：把 agent 的自由度收緊，而不是放大

TL;DR：NVIDIA 團隊靠「收緊工具、留下證據」的 harness 設計，拿下 KDD Cup 資料代理競賽第二名。

多數人直覺認為，agent 越聰明、工具越多，表現就會越好。但 NVIDIA KGMON 團隊在 KDD Cup 2026 Data Agents 競賽中拿下第二名的做法恰恰相反：把 agent 能做的事情收得更小、更清楚、更容易檢查。

🤔 **固定小模型、異質資料來源的硬限制**

這場競賽要求 agent 回答跨異質資料來源的自然語言問題，資料來源包含資料庫、CSV／JSON 檔案、文字文件、PDF 以及簡報影片。每個任務都不只是單純檢索，agent 需要檢視可用資料、選擇正確工具、跨來源推理、產出最終答案檔，還要應付分析流程中常見的陷阱。更關鍵的限制是，KDD 要求所有團隊使用同一個固定、規模較小的 LLM，這使得 harness（agent 的外部框架與工具設計）本身成為唯一的最佳化空間。

🧩 **兩個核心原則，五項具體作法**

團隊的設計圍繞兩個原則：第一，收緊行動空間，因為太多種檢查資料、呼叫工具、寫檔案或錯誤恢復的方式，反而會導致更多失敗；第二，讓每一次嘗試都可被檢查，方便從執行紀錄、重複嘗試與軌跡檢視中找出失敗原因並改進 harness。

在這兩個原則下，團隊落實了五項作法：

1. **統一結構化資料的查詢介面**：把 CSV、JSON 檔案全部轉成現有 SQLite 資料庫裡的表格，讓 agent 只用一套 SQL 介面存取所有結構化資料，並透過自訂的持久化 Python 環境提供 schema() 與 sql(query) 兩個內建函式。單一 SQL 介面減少了路由失敗與浪費的回合，讓固定的小模型有更多餘裕專注在推理上。

2. **預先提供 schema 情境**：在主要推理迴圈開始前，加入一個 schema 探勘步驟，檢查表格、欄位、可能的 join 鍵、重複命名、容易混淆的欄位、單位以及空值分佈等問題，並把這些情境一次性交給 agent，省下一個早期探索回合，減少因為用錯欄位或漏掉 join 而產生的錯誤。

3. **打造小而講究的工具集**：環境只提供 schema()、sql(query)、write_answer(df)、prose_helper() 這幾個函式，middleware 會修復格式錯誤的工具呼叫，避免一次錯誤呼叫就毀掉整次嘗試；持久化的 Python 環境讓變數可以在工具呼叫之間保留，agent 能重複利用中間結果。簡短、有效的嘗試留下更多回合可以用在額外執行、評估與多次結果的整合（ensembling）上。

4. **把文字文件當作一級輸入，但與結構化資料分開處理**：競賽中的 PDF、Markdown、政策文件常包含門檻值、定義與類似表格的紀錄，但完整讀入會佔用大量 context。團隊封鎖了直接讀整份檔案的方式，改提供依字數或正規表達式（regex）限制範圍的預覽與搜尋工具；找到相關段落後，再呼叫 prose_helper，把文件片段丟給另一個溫度設為 0、關閉推理的獨立 LLM 呼叫，回傳答案或抽出表格，讓原始文件內容不進入主 agent 的 context。prose_helper 有 answer（抽取規則、門檻值或簡短答案）與 table（把重複出現的紀錄轉成 SQL 表格）兩種模式。

5. **提前預處理影片**：為避免在 agent 迴圈內處理影片的運算成本，團隊提前抽取關鍵畫面、轉錄音訊、將逐字稿片段與畫面對齊，再把整理好的證據交給 agent。每個任務最多只有一支影片，通常包含投影片形式的限制條件與干擾值，逐字稿與畫面對齊能把口語內容和正確的視覺證據連結起來。

📊 **結果：第二名，而不是用更強的模型堆出來的**

這套系統最終在 KDD Cup 2026 Data Agents 競賽中拿下第二名，而整套方法的前提是所有參賽隊伍都被限定使用同一個規模較小的固定 LLM，說明名次差異主要來自 harness 設計，而不是模型本身的規模優勢。

⚠️ **這些作法有適用邊界**

團隊自己也提出了重要提醒：表格抽取（table extraction）這一步適合競賽中「文件內嵌結構化資訊」的任務型態，正式產品可能只需要針對性的文字查詢，表格抽取可以是選配功能；影片預處理的設計也是針對競賽情境調整的，例如每個任務最多一支影片這個前提，在真實產品中未必成立。

🎯 **實務啟示**

這篇文章給出的核心教訓很直接：想讓使用小型開源模型的 agent 系統變可靠，重點往往不是讓模型更自由發揮，而是把它能做的事情收緊、把每一步的過程做成可檢查的軌跡。具體可以照搬的做法包括：在 agent 開始前先做一次只讀的 schema 探勘簡報、把結構化資料統一到單一查詢層、用少量定義明確的工具函式取代開放式檔案存取、以及為長文件提供有範圍限制的查詢工具而非整份讀入。

🔗 **來源**
- 標題：Building Reliable Data Analytics Agents: Lessons from the KDD Cup
- 作者／機構：Jiwei Liu（NVIDIA Developer / NVIDIA KGMON 團隊）
- 連結：https://developer.nvidia.com/blog/building-reliable-data-analytics-agents-lessons-from-the-kdd-cup/

#AIAgent #DataAnalytics #KDDCup #NVIDIA #LLMEngineering #AgentHarness #SQL #PromptEngineering #RAG #SmallLanguageModels
