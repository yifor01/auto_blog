---
title: AI-powered metadata correction and harmonization
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/ai-powered-metadata-correction-and-harmonization/
model: claude-code/sonnet
generated_at: '2026-08-25T06:23:14.516601'
score: 93
---

📌 【AWS 實作案例】用 LLM 分層架構，自動校正跨來源的 metadata

TL;DR：AWS 用 Bedrock LLM 搭配 embedding 與規則驗證，分層自動校正 metadata schema，同時保留人工核准。

資料產出的速度早已超越人類標準化它的能力，當不同來源的 metadata（元資料）對不齊，再強大的分析管線也會卡在起點——這正是許多開放科學計畫長期以來的隱形瓶頸。

🤔 **metadata harmonization 為何一直靠人工**

metadata harmonization（協調不同來源資料集的標籤、識別碼與格式，使其能互通）長期仰賴人工處理。隨著資料量加速成長，這個手動流程會延遲分析、複雜化資料解讀，並限制共享資料集的全球價值。作者團隊因此在 AWS 上打造了一套集中式的 metadata 校正與協調工作流程。

🧩 **人在迴圈中的循環式工作流程**

系統採用循環式（cyclical）工作流程：使用者上傳 metadata 檔案後，系統同時執行兩條平行驗證：schema alignment（確認欄位結構是否符合預期格式）與 metadata field validation（檢查個別欄位值是否合規）。偵測到問題後，系統產生針對性的修正建議並交由使用者核准，維運者始終保有最終決定權——這種 human-in-the-loop 設計讓自動化加速流程，同時保留研究者的專業判斷。

系統架構使用 Amazon Bedrock 進行 LLM 驅動的 schema 對齊與修正建議、Amazon S3 儲存 schema 與結果、Amazon DynamoDB 追蹤工作進度、Amazon Cognito 負責身分驗證、Amazon ECS 提供運算資源。

在 schema alignment 階段，常見問題包括命名不一致（同義詞、拼字錯誤、縮寫）、欄位缺漏或多餘，以及欄位需要拆分或合併。模糊字串比對（fuzzy string matching）能處理基本的命名差異，但更複雜的對齊問題需要語意理解：Bedrock 上的 LLM 能辨識產業特定的同義詞、從周邊欄位推斷含義，並判斷來源欄位是否該拆分成多個目標欄位，這是規則式系統難以處理的情境。

在 metadata field validation 階段，系統把驗證失敗分為三類：必填欄位驗證（找出缺漏、空白或僅含空白字元的必填欄位）、列舉值驗證（比對欄位內容與 schema 定義的受控詞彙表，例如儀器類型只能是特定清單內的值）、格式驗證（用正則表達式檢查格式慣例，例如日期欄位需符合 YYYY-MM-DD）。每個驗證失敗都會被分類並附上足夠脈絡，供後續建議系統使用。

🧩 **從規則到 LLM 的分層修正建議**

系統以分層方式結合傳統 NLP 與 AI 技術產生修正建議，優先使用傳統 NLP 與 embedding 相似度，僅在必要時才呼叫 LLM，藉此在成本與效能之間取得平衡，並依信心門檻動態選擇要使用哪種技術（可組成 bagging 或 boosting 架構）。

向量 embedding 讓系統能語意比對 metadata 值，例如將「Human」對應到「Homo sapiens」，或將「NYC」對應到「New York City」。團隊評估了多個 embedding 模型，包括領域專屬的生醫模型與 Amazon Titan，最終選用 Amazon Titan，理由是它在一般與生醫 metadata 任務上表現穩定、具商業可用性，且與 Amazon Bedrock 模型推論相容，適合需要受支援、可擴展 embedding 方案而不想自行維運領域模型的組織。

另一種機制是 contextual inference：透過分析資料集內部的相似列（row），推斷缺漏或不一致的欄位值，不需依賴大型外部訓練資料。實作上採混合方法，結合距離加權 k-nearest neighbors、TF-IDF 特徵表示與共現統計。每一列資料會轉換成複合向量：文字欄位轉為 TF-IDF 表示，類別欄位以 one-hot 或緊湊的學習式表示編碼，數值欄位則做尺度縮放；接著用 cosine 或 Euclidean 距離衡量列與列之間的相似度，透過加權投票（距離越近影響力越大）預測缺漏值，並進一步以 Pointwise Mutual Information（PMI）分析共現統計，找出資料集中自然一起出現的值組合，精煉推論結果。

💡 **分層設計的用意：先便宜後精準**

這套架構的核心思路是把成本可預測性放在優先位置：規則驗證與 embedding 相似度能處理大多數常規修正，只有遇到模糊或新穎案例，才動用推理成本較高的 LLM。這種「簡單方法先上、複雜模型收尾」的設計，讓系統在資料量成長時仍能維持可預測的推論成本。

🎯 **實務啟示**

對於需要整合跨機構、跨資料集（尤其是生醫或科學領域）metadata 的工程團隊，這套架構提供了一個可參考的落地路徑：用 LLM 處理語意層級的 schema 對齊問題，用便宜的 embedding 相似度處理常規值校正，用規則驗證守住格式與必填欄位的底線，並始終保留人工核准這道防線，而不是追求全自動化。

🔗 **來源**
- 標題：AI-powered metadata correction and harmonization
- 作者／機構：Joseph Cottingham（AWS ML Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/ai-powered-metadata-correction-and-harmonization/

#AWS #AmazonBedrock #MetadataHarmonization #LLM #DataQuality #HumanInTheLoop #OpenScience #VectorEmbeddings #DataEngineering #MachineLearning
