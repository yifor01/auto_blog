---
title: Cohere Releases Rerank 5 With Passage-Level Context Focus and Calibrated Scores
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/22/cohere-rerank-5-context-focus/
model: claude-code/sonnet
generated_at: '2026-10-22T20:46:46.098678'
score: 97
---

📌 RAG 送進 LLM 的 token，Cohere Rerank 5 砍掉四成還升準

TL;DR：Cohere Rerank 5 用段落級 Context Focus 與校準分數，讓 RAG 系統少送 token 又準一點。

RAG 系統常見的痛點是：檢索回來一整份文件，真正有用的可能只有兩三句話,剩下的全部塞進 LLM 的 context window,既浪費成本又稀釋模型的注意力。Cohere 這次針對的正是這個問題。

🤔 **Reranker 要解決的不是檢索,是「送什麼給 LLM」**

Cohere Rerank 5 是一款在搜尋結果送進 LLM 之前,負責重新排序的檢索模型,分成 Pro 與 Fast 兩個等級。Pro 主打推理密集查詢與長篇領域文件的排序品質,Fast 主打低延遲、高吞吐量,適合需要大量搜尋的 agent 場景。兩者都支援超過 100 種語言與 32K context window,也能處理 JSON、表格、YAML 這類半結構化資料。對既有系統而言,升級不需要重新索引,只要換掉 model 參數,原本的關鍵字、向量或混合搜尋架構都能照常使用。

🧩 **Context Focus：只回傳文件裡真正有用的段落**

Context Focus 是一項預設關閉的選用功能。開啟後,單次 Rerank 呼叫會回傳文件分數,外加帶有分數的字元範圍(character span),每個 span 都帶有起止的字元位移。開發者透過 `relevant_spans` 欄位設定,可以調整 threshold 與 max_spans 這兩個參數,精準控制要抽取多少段落。

📊 **token 省了多少,準度掉了多少:實測數據攤開來看**

Cohere 在 30 個 QA 資料集上測試,拿掉一半檢索到的文字,仍保留 96% 的答案品質;拿掉四分之三,仍保留 87%。Cohere 表示團隊可以把 context 壓到十分之一,但會有一定的品質代價。

在 17 個資料集組成的 search-agent 測試中,單用 BM25 準確率是 46%,加上 Rerank 5 Pro 提升到 49%。開啟 Context Focus,threshold 設在預設的 0.1 時,每個任務的 token 數減少 19%,準確率反而拉到 57%;threshold 提高到 0.4,token 減少 34%,準確率來到 58%。相較單用 BM25,整套流程省下 35% 的 token。在另外 6 個 deep-search 基準測試中,token 減少 41%,準確率從 39% 提升到 52%。

另一項改動是校準分數(calibrated scores)。Rerank 5 回傳的分數可以直接當機率解讀,比如 0.7 代表「有 70% 機率這份文件有用」。Cohere 用 expected calibration error(ECE)對照人類評審與 NIST TREC-DL 標註者測量,Rerank 5 在兩邊都約 0.06,對照 Voyage AI Rerank 3 的 0.234 與 0.307,以及自家前代 Rerank 4 Pro 的 0.384 與 0.309。實務上,這讓開發團隊可以用固定 threshold 過濾,而不是硬性抓固定的 top-k,agent 也能據此判斷「這次檢索根本沒找到相關內容」。

以下數字均為 Cohere 自行測得的 RCP-nDCG@10(Cohere 自訂的 nDCG 變體),競品模型也是由 Cohere 自己跑出來的分數,未經第三方驗證。Pro 在四項主要基準全面領先:ViDoRe V3 拿下 92.2、BEIR 90.4、BRIGHT 82.2、nanoMTEB 87.3,其中 BRIGHT 比前代 Rerank 4 Pro 高出 12.4 分。Fast 在四項基準上勝過 Voyage AI Rerank 3 Lite、Qwen3-Reranker-8B 與 Rerank 4 Pro,在 ViDoRe V3 上以 90.6 與 Voyage AI Rerank 3 打平,但在 BEIR 上以 88.1 略輸給對方的 88.6。在 47 個解析後 PDF 資料集的平均表現中,Pro 拿下 89.9、Fast 拿下 88.5,均優於 Voyage AI Rerank 3 的 88.4。在 Cohere 內部的多語言測試中,Pro 在 19 種非英語語言中的 14 種排名第一。

🎯 **對 RAG／agent 團隊的實務意義**

Context Focus 的價值在於把「檢索品質」與「token 成本」解耦:不用整篇塞進 context,也能保留大部分資訊量。Rerank 5 已全面上線 Cohere API 與 Model Vault,也能在 Microsoft Foundry 與 Amazon SageMaker 上執行,North 用戶同樣可用。API 計費為 Pro 每百萬 token $0.05、Fast $0.02,Model Vault 在 Medium tier 上兩個等級都是每個 instance-hour $4.00。LangChain、Haystack、Elasticsearch、Weaviate 都已提供整合,換模型的遷移成本不高,值得既有 RAG pipeline 評估導入。

🔗 **來源**
- 標題：Cohere Releases Rerank 5 With Passage-Level Context Focus and Calibrated Scores
- 作者／機構：Michal Sutter，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/22/cohere-rerank-5-context-focus/

#Cohere #Rerank #RAG #InformationRetrieval #LLM #AgentOps #SearchEngineering #ContextEngineering #VectorSearch #MachineLearning
