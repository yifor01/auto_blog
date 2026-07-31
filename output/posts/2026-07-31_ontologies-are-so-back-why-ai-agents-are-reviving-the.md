---
title: 'Ontologies Are So Back: Why AI Agents Are Reviving the Semantic Web'
source: Latent Space
url: https://www.latent.space/p/ontologies-agentic-systems
model: tencent/hy3:free
generated_at: '2026-07-31T08:45:31.480177'
score: 80
---

📌 【AI Engineer World’s Fair 焦點】為何 AI Agent 時代正讓「本體論 (Ontologies)」重新回歸？

TL;DR：LLM 擅長機率推理，但 Agent 需要本體論提供「邏輯護欄」來實現規模化運作。

🎣 **從機率推理到邏輯護欄的轉向**

在 AI Engineer World’s Fair 上，UC Berkeley 教授 Frank Coyle 指出，雖然大型語言模型 (LLM) 在提供機率推理 (probabilistic reasoning) 方面非常有效，但若要讓 Agentic systems (代理系統) 真正發揮作用，它們需要「邏輯護欄 (logical guardrails)」，也就是本體論 (ontologies)。

🧩 **本體論就是「資料的圖譜化」**

本體論的概念可以追溯至亞里斯多德，在人工智慧發展史上也扮演重要角色。從技術角度來看，本體論可以被簡單定義為「資料即圖譜 (data as graphs)」，它是對特定知識領域中類別 (classes)、屬性 (properties) 與關係 (relationships) 的資料結構描述。

📊 **Neo4j 提出的三種本體論應用層次**

圖譜資料庫領導廠商 Neo4j 的 CEO Emil Eifrem 提到，為了讓 Agent 能夠在大規模場景下運行，需要建立一個更聰明的「共享基底 (shared substrate)」，這包含三種不同類型的本體論：

* **面向業務的本體論 (Business-facing ontology)**：描述組織中的核心概念。
* **技術本體論 (Technical ontology)**：包含企業生態系統中所有資料來源與資料資產的元數據 (metadata)。
* **執行軌跡 (Execution traces)**：來自 Agent 運行時 (runtime) 的訊號。

💡 **利用既有的 Web 本體論與 LLM 訓練資料**

Frank Coyle 特別強調，Web 本體論對於構建代理系統非常有益。開發者可以利用已有的成熟技術，例如：
* 既有的 Web 本體論：Schema.org、FOAF、Dublin Core。
* 增強技術 (augmenting technologies)：RDFS (Resource Description Framework Schema) 與 OWL (Web Ontology Language)。

這裡有一個對工程師極大的優勢：由於這些既有的本體論已經存在於 LLM 的訓練資料中，開發者可以直接透過 Prompt (提示詞) 要求模型遵循這些結構，這比從零開始定義要有效得多。

🎯 **實務啟示**

當開發者試圖將 Agent 從單純的對話機器人轉向複雜的自動化代理時，不應僅依賴 LLM 的機率預測。引入結構化的本體論，可以為 Agent 提供必要的邏輯框架，讓其在處理複雜的企業資料與業務邏輯時，具備更強的可靠性與可擴展性。

🔗 **來源**
- 標題：Ontologies Are So Back: Why AI Agents Are Reviving the Semantic Web
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ontologies-agentic-systems

#AI #AIagents #Ontology #LLM #GraphDatabase #Neo4j #SemanticWeb #MachineLearning #DataStructure #ArtificialIntelligence
