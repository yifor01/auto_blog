---
title: Improve contract search accuracy with auto-generated filters in Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/improve-contract-search-accuracy-with-auto-generated-filters-in-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-08-19T06:34:12.122338'
score: 92
---

📌 【AWS 實務架構】合約搜尋常常「查不到重點」？AIDA 用隱式過濾解題

TL;DR：AIDA 在語意搜尋前先做 metadata 過濾，降低法律合約 RAG 系統漏答關鍵條款的風險。

想像你問系統：「哪些加州法律管轄的授權合約已經到期？怎麼續約？」單純的語意搜尋可能命中數百個相關片段，而 Bedrock 語意搜尋預設只回傳最相關的前 k 個（上限 100 個）候選片段，被篩掉的那些，可能剛好藏著關鍵的續約條款。

🤔 **法律合約搜尋很難只靠語意相似度**

企業依賴大量複雜的法律合約做關鍵商業決策：判斷權利歸屬、續約選項、地域限制、法遵義務。在娛樂媒體這類需要跨多個司法管轄區管理數千份合約的產業，這件事至今大多仍是人工作業，耗時、昂貴、難以規模化。AIDA（AI-Driven Annotation）是 AWS 打造的解決方案，把非結構化合約轉換成可搜尋、可行動的智慧資料，讓使用者能用自然語言對大型合約庫提問。但純語意搜尋（RAG）有個結構性問題：法律文件高度依賴上下文，系統可能撈出比語言模型能有效處理還多的內容；如果沒有妥善控制檢索到的片段、也沒有足夠的文件層級脈絡，重要條款就有被忽略或誤讀的風險。

🧩 **架構：先用 metadata 縮小範圍，再做語意搜尋**

AIDA 建立在 Amazon Bedrock Knowledge Bases 之上，整個工作流程分成幾個階段：

1. **文件擷取與 metadata 設定**：合約連同結構化 metadata（締約方、生效日、終止日、司法管轄區等關鍵屬性）一起同步進 Knowledge Base，這些屬性是後續過濾能力的基礎。
2. **切塊（chunking）**：把合約切成語意完整的片段，兼顧上下文完整度與檢索效率。
3. **向量資料庫儲存**：文件片段轉成向量嵌入，存進 Amazon OpenSearch Service 或 Amazon S3 Vectors，並啟用靜態加密；存取則透過 AWS IAM 政策管控，搭配 Amazon CloudWatch 做稽核日誌。
4. **查詢嵌入**：使用者送出問題後，先經過 Amazon Bedrock Guardrails 防範 prompt injection 與資料外洩，再把查詢轉成嵌入向量。
5. **隱式與顯式過濾**：這是這套架構的核心創新，在做語意搜尋之前，系統先套用 metadata 條件（例如生效日期範圍、特定締約方）做隱式過濾，兩階段做法先用 metadata 限縮搜尋範圍，再在這個子集合裡做語意相似度比對，確保撈回來的文件既符合語意相關性，也符合業務條件。
6. **語意搜尋與檢索**：向量資料庫在已過濾的子集合中，依 cosine similarity 找出最相關的片段，再用來組合成 augmented prompt 交給 LLM。
7. **回應生成**：Bedrock 上的 LLM 根據合約原文而非單純訓練資料生成回答，同時 Bedrock Guardrails 負責內容過濾、PII 防護與 prompt 安全控制。
8. **附來源的回應**：透過 Retrieve API 回傳答案，並可追溯回原始文件，降低幻覺風險，讓使用者能驗證合約情報的正確性。

資料傳輸全程採用 HTTPS/TLS 1.2+ 加密，涵蓋文件上傳、embedding 模型呼叫、向量資料庫查詢與回應傳遞；Bedrock 端的資料則適用 AWS 共同責任模型。存取控制則是透過 AIDA 應用層的 IAM 角色式權限，依專案範圍限制每個使用者能做的事。

💡 **為什麼「先過濾再搜尋」比單純語意搜尋更準**

一般 RAG 系統的痛點在於：語意搜尋預設只回傳 top k（上限 100）個候選片段，被篩掉的片段可能剛好包含關鍵上下文。以「加州法律管轄的到期授權合約」為例，如果檢索階段沒有正確過濾出加州法律管轄的授權合約，系統可能連服務合約、NDA 或其他州法律管轄的合約都一併撈進來，稀釋掉真正相關的內容。AIDA 的做法是把 metadata 過濾放在語意搜尋之前而非之後，先縮小候選集合的範圍，讓語意比對在一個乾淨、業務條件明確的子集合裡進行，而不是對整個合約庫做語意搜尋後再事後篩選。

⚠️ **效果高度依賴 metadata 品質**

這套機制能不能發揮效果，高度仰賴文件擷取階段 metadata 是否完整、正確標註。如果締約方、生效日、司法管轄區等屬性沒有被準確填入，隱式過濾就無從發揮縮小搜尋範圍的效果。

🎯 **實務啟示**

如果你的 RAG 系統處理的是高度依賴上下文與業務條件的文件（不只是合約，任何有明確結構屬性的文件庫都適用），與其在語意搜尋後才想辦法排序、去雜訊，不如在檢索前就先用 metadata 做隱式過濾，直接縮小搜尋空間，讓語意相似度比對在更乾淨的子集合裡進行，同時搭配 Guardrails 做 prompt injection 防護與 PII 過濾，是企業級合規場景值得參考的架構模式。

🔗 **來源**
- 標題：Improve contract search accuracy with auto-generated filters in Amazon Bedrock
- 作者／機構：Ariana Lopez, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/improve-contract-search-accuracy-with-auto-generated-filters-in-amazon-bedrock/

#AWS #AmazonBedrock #RAG #LegalTech #KnowledgeBases #VectorSearch #EnterpriseAI #PromptEngineering #GenAI #DocumentAI
