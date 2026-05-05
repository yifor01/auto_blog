---
title: "FlexSQL: Flexible Exploration and Execution Make Better Text-to-SQL Agents"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.02815
score: 119
model: tencent/hy3-preview:free
generated_at: 2026-05-05T19:42:03.756940
---

📌 FlexSQL 彈性交互優化 Text-to-SQL 效能

主流Text-to-SQL系統大多採用固定流程，先擷取一次Schema、生成SQL後才做修復，早期錯誤幾乎無法挽回。最新提出的FlexSQL打破這個慣例，使用更小參數的模型，就擊敗了採用更大更強模型的基線系統。

🤔 **固定流程限制Text-to-SQL Agent錯誤恢復能力**
Text-to-SQL（將自然語言問題轉換為SQL查詢的任務）需要處理複雜資料庫Schema、解決模糊查詢、並基於實際數據做決策。但現有主流系統大多遵循固定管線：僅在初始階段擷取一次Schema元素，只有生成SQL後才會重新查詢資料庫做修復，一旦前期出現Schema理解或查詢解讀錯誤，幾乎沒有恢復空間。

🧪 **以彈性資料庫交互為核心的Agent架構**
FlexSQL的核心設計原則是彈性資料庫交互，Agent可在推理過程的任何階段探索Schema結構、檢視數據值、執行驗證查詢；同時會生成多樣化執行計畫以覆蓋多種查詢解讀，再根據任務特性選擇以SQL或Python實作計畫，並採用兩階段修復機制：可從程式碼層級錯誤回溯到執行計畫層級的修正。

研究在Spider2-Snow基準上評估效能，使用gpt-oss-120b作為基礎模型，對比使用更大更強模型（如gpt-o3、DeepSeek-R1）的開源強基線。

💡 **更小模型達65.4%得分，超越更強大模型基線**
在Spider2-Snow基準測試中，採用gpt-oss-120b的FlexSQL取得65.4%的得分，優於那些使用更大、更強模型（如gpt-o3、DeepSeek-R1）的開源強基線。

將FlexSQL作為技能整合到通用編程Agent（如Claude Code）中，可在Spider2-Snow上帶來超過10%的相對效能提升。

消融實驗進一步驗證，彈性探索與彈性執行兩項設計共同貢獻了方法的有效性，證實「彈性」是Text-to-SQL Agent的關鍵設計原則。

🔍 **彈性設計解決固定流程的錯誤累積痛點**
現有固定流程的核心痛點在於「早期錯誤無法修正」：一旦初始Schema擷取不全或查詢解讀偏差，後續生成的SQL必然出錯，且只能做局部修復。FlexSQL允許Agent在推理全程動態與資料庫交互，相當於賦予Agent「隨時查
