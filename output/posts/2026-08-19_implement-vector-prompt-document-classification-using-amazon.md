---
title: Implement vector-prompt document classification using Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/implement-vector-prompt-document-classification-using-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-08-19T06:29:48.019639'
score: 96
---

📌 保單、宣誓書傻傻分不清？多代理系統把準確率拉到 100%

TL;DR：AWS 用 Claude Haiku 4.5 加 Titan 多模態 embedding 打造多代理文件分類系統，實測準確率完勝傳統方法。

保險公司每天要處理成千上百份長相相似、用途卻南轅北轍的文件：保單、宣誓書、批單、法規表單。傳統自動化方法常常在這種「文字用詞重疊但意義不同」的邊界案例上翻車，分類錯誤更可能直接引發合規問題或理賠延誤。

🤔 **為什麼單一模型不夠用**

AWS 這篇文章指出，實測中單一模型方法在需要同時做文字與視覺分析的複雜文件上表現不佳。解法是把分類任務拆解成專門的子任務，讓不同的模型各自發揮所長。

🧩 **三個代理各司其職，一個代理仲裁**

解決方案使用 Strands Agents SDK 建構多代理架構，包含三個角色：

- **Document Analysis Agent**：使用 Anthropic 的 Claude Haiku 4.5，負責文字推理與法律語言解讀，分析文件內容、metadata 與語言特徵，產生分類假設，並以結構化輸出回傳結果。
- **Vector Similarity Search Agent**：使用 Amazon Titan Multimodal Embeddings G1 把文件轉成高維向量表示，專注於「文件長什麼樣子」而非「文件寫了什麼」，例如表單版面、表格結構等格式特徵。它透過 FAISS 對已知文件範本做快速向量相似度搜尋。
- **Validation Agent**：身兼 orchestrator，採用「agents as tools」模式呼叫前兩個代理，比對兩者輸出、找出一致與分歧之處，產出最終分類結果與信心分數，並把邊界案例標記出來交由人工複核。

這種設計的好處是，Validation Agent 只需呼叫各個專家代理並比較結果、化解分歧，不需要額外撰寫協調邏輯。

📊 **實測數據：多代理系統唯一達到 100% 準確率**

文章提到，這套系統選用 Claude Haiku 4.5 作為推理模型，平均每份文件分類耗時 19.3 秒、信心分數達 93%，適合對速度與成本敏感的正式環境。

團隊將此方案與三種常見 AWS 方法做基準比較：
- Amazon Textract 加 Amazon Comprehend：專精文字擷取與實體辨識，但不是為多類別文件分類設計，準確率僅 25%。
- Amazon Bedrock Data Automation（BDA）：表現明顯較好，達到 70%，能正確處理多數宣誓書與雜項文件，但整體仍有近三分之一文件誤判。
- 多代理系統：是唯一在所有文件類別上都達到 100% 準確率的方法。

其中差距最大的是保單文件，這類文件充滿與其他類別高度重疊的密集法律用語，只有多代理系統能正確分類。

🎯 **實務啟示**

當分類任務的難點在於「文字相似但用途不同」，單靠文字模型或單靠視覺相似度都容易踩雷。把文字推理、版面視覺特徵拆成獨立代理各自判斷，再用一個驗證代理做交叉比對與信心評分，是一個值得在合規敏感的文件處理場景中參考的架構模式。

🔗 **來源**
- 標題：Implement vector-prompt document classification using Amazon Bedrock
- 作者／機構：Pavana Sai Sree Chalamarla, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/implement-vector-prompt-document-classification-using-amazon-bedrock/

#AmazonBedrock #ClaudeHaiku #MultiAgent #DocumentClassification #StrandsAgents #TitanEmbeddings #FAISS #InsuranceTech #AWSML #RAG
