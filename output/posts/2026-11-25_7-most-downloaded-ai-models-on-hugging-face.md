---
title: 7 Most Downloaded AI Models on Hugging Face
source: KDnuggets
url: https://www.kdnuggets.com/7-most-downloaded-ai-models-on-hugging-face
model: claude-code/sonnet
generated_at: '2026-11-25T01:54:31.424076'
score: 62
---

📌 Hugging Face下載榜冠軍不是Llama，是一個384維的小模型

TL;DR：下載量排行榜揭露一個反直覺現象：排名靠前的不是最新最強LLM，而是體積小、歷史久的基礎工具模型。

如果你以為Hugging Face下載排行榜前幾名會是Llama、Qwen、DeepSeek這類當紅大型語言模型，那你可能要重新想一下——真正霸榜的，是一群低調到你可能沒注意過的小模型。

🤔 **下載量不等於熱度，而是用量**

KDnuggets整理的榜單顯示，下載量第一的是all-MiniLM-L6-v2，一個把文字轉成384維向量的輕量級sentence embedding模型，下載次數高達1億8千萬次以上。文章解釋，下載數字反映的其實是「模型在應用程式、研究實驗、自動化工作流程與教學中被呼叫的頻率」，而不是模型本身有多強大或多受AI愛好者歡迎。

📊 **榜單一覽：小模型、老模型全部上榜**

依下載量排序：
- all-MiniLM-L6-v2（約1.82億次）：384維句子embedding模型，用於語意搜尋、文件相似度、聚類與RAG。
- ms-marco-MiniLM-L6-v2（約6,640萬次）：cross-encoder重排序（reranking）模型，在RAG管線與企業搜尋中為候選文件打相關性分數。
- bge-small-en-v1.5（約4,940萬次）：由北京智源人工智慧研究院（BAAI）開發的384維特徵提取模型，廣泛整合進向量資料庫與檢索框架。
- MiniMax-H3（約3,180萬次）：為ComfyUI重新打包的影片生成模型檔案，涵蓋文字轉影片、圖片轉影片等工作流程。
- GPT-2（約2,980萬次）：OpenAI於2019年發布，至今仍常見於教學、研究與fine-tuning實驗。
- bert-base-uncased（約2,960萬次）：Google於2018年推出的encoder模型，仍是文字分類、命名實體辨識等任務的標準baseline。
- Chronos-2（約2,430萬次）：1.2億參數的時間序列預測模型，支援單變量與多變量預測，並能納入假日等已知未來事件來改善預測。

💡 **為什麼巨型LLM反而不在榜上**

文章點出幾個原因：教學與Colab notebook執行時會自動觸發下載；BERT、GPT-2這類模型是研究教育的標準baseline，持續被大量實驗引用；embedding模型與reranker是處理大量搜尋查詢的生產系統基礎元件；小模型硬體需求低，CI/CD、雲端部署、容器建置等自動化流程會反覆抓取同一個模型。文章也特別提醒一個技術細節：Hugging Face統計的是符合條件的模型檔案請求（包含特定的HTTP GET與HEAD請求），因此下載數字並不代表唯一使用者數、完整權重下載次數,或實際推論執行次數。

🎯 **實務啟示**

這份榜單對工程師的提醒是：真正撐起RAG、搜尋、分類等日常AI應用的,往往是這些不起眼的embedding與reranking模型,而不是頭條新聞裡的旗艦LLM。如果你在建置檢索系統,all-MiniLM-L6-v2、bge-small-en-v1.5這類小模型搭配ms-marco-MiniLM-L6-v2做重排序,仍是CPU可跑、成本低、驗證過的務實起點。

🔗 **來源**
- 標題：7 Most Downloaded AI Models on Hugging Face
- 作者／機構：Abid Ali Awan, KDnuggets
- 連結：https://www.kdnuggets.com/7-most-downloaded-ai-models-on-hugging-face

#HuggingFace #Embeddings #RAG #BERT #GPT2 #NLP #VectorSearch #MachineLearning #OpenSource #TimeSeriesForecasting
