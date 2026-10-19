---
title: 'LangChain vs. LlamaIndex vs. Building From Scratch: Here’s What I Suggest'
source: KDnuggets
url: https://www.kdnuggets.com/langchain-vs-llamaindex-vs-building-from-scratch-heres-what-i-suggest
model: claude-code/sonnet
generated_at: '2026-10-19T21:46:44.900691'
score: 84
---

📌 LangChain、LlamaIndex,還是自己刻?選框架前先想清楚這件事

TL;DR:選框架的關鍵不是生態規模，而是你現在的開發階段到底在優化什麼。

每次有人問「要做LLM應用該用什麼框架」,答案幾乎是反射動作般的LangChain或LlamaIndex。但如果這個反射動作本身就是錯的呢?

🤔 **LLM本身什麼都不記得,協調層才是真正的工程**

LLM本質上是無狀態的文字預測器:輸入prompt、吐出completion，然後完全不記得剛才發生了什麼。要做出真正有用的應用——文件問答、多步驟agent、檢索增強生成（RAG）、對話介面——都需要一層「協調層」:管理context、在工具間路由、檢索相關資訊、處理記憶、串接多個操作。LangChain和LlamaIndex都是為了解決這層協調問題而生，把底層管線抽象掉，讓開發者專注在應用邏輯上。第三種選項，則是直接呼叫模型供應商的base API，自己動手寫這層管線。

🧩 **LangChain:覆蓋範圍廣,但除錯要爬好幾層抽象**

LangChain起步早，建立了龐大的功能範圍,提供chain、agent、memory、tool、retriever、output parser、prompt template等抽象，並與大量外部服務、資料庫、API整合。如果你的應用需要連接多種外部工具與資料源，或是需要LLM在多個工具間做決策、迴圈處理中間結果，LangChain的agent抽象能給你一個現成的起點。

但同樣的廣度也讓系統難以推理。當某個環節出錯時，要穿過好幾層包裝好的class去追蹤問題並不容易。文章指出,許多開發者反映LangChain的抽象層一開始加速了開發，但後續在除錯與客製化階段反而拖慢進度。框架演進速度快，也意味著文件經常落後於目前的API，舊教學可能引用已淘汰的寫法，版本升級偶爾會帶來破壞性變更——對需要穩定性與可預測性的生產系統來說，這是實際的成本。整體而言，LangChain最適合快速原型驗證、探索LLM應用的可能性，或是整合覆蓋範圍比實作細節的掌控更重要的場景。

🧩 **LlamaIndex:專注RAG,但超出檢索範圍就容易卡手**

LlamaIndex（前身為GPT Index）一開始的範圍就比較窄，專注於讓RAG系統更容易建構，而這也仍是它的核心特色。如果你的應用主要是從文件中檢索資訊、再提供給LLM作為context，LlamaIndex非常適合——它的資料連接器、索引策略與查詢引擎都是為這個用例量身打造的，抽象也因此更連貫。LlamaIndex同時提供重排序（re-ranking）、混合搜尋、層級式檢索、查詢路由等進階RAG模式的工具，並在評估工具上投入不少心力，讓你能在影響使用者之前就知道檢索系統是否真的有回傳有用的內容。

它的侷限在於超出檢索範圍的場景。如果你需要豐富的agent行為、複雜的工具使用、或是不以文件檢索為中心的工作流程，可能會發現自己在跟框架的假設打架，而不是順著它走。和LangChain一樣，框架對架構的假設愈多，當你的需求不符合預期模式時，偏離框架就愈困難。

🧩 **從零開始刻:不是重寫LLM,是自己接API**

「從零開始」不代表自己寫一個LLM，而是直接呼叫模型供應商的API，自行實作檢索邏輯，只建構應用真正需要的抽象。隨著OpenAI、Anthropic、Google等供應商的API與用戶端函式庫日趨成熟，加上Pinecone、Weaviate、Qdrant等向量資料庫都有自己的SDK，這條路比過去容易走得多。

這個做法的最大好處是對系統每一步的完全可見性:沒有框架模板隱藏的prompt injection，沒有預期外的重試邏輯，沒有攔截請求的抽象層。當行為不如預期時，你很清楚該去哪裡找問題。文章也指出一個比較不明顯的好處:自己刻迫使你把應用真正需要什麼想清楚——框架常常讓複雜模式唾手可得，進而鼓勵過度設計；而自己實作檢索邏輯時，你會很自然地只做用例真正需要的東西，不多不少。

當然，前期投入是真實存在的:你會寫更多程式碼、做更多明確的決策、花更多時間在框架原本會自動處理的基礎設施上。對於還在驗證LLM應用是否可行的團隊，這份投入可能拖慢學習速度。而且這條路對知識要求不低——打造一個好的RAG管線需要理解嵌入模型、向量相似度、分塊（chunking）策略與context window管理，框架可能掩蓋了這些知識缺口，自己刻則會把它們全部暴露出來。

🎯 **實務啟示**

這三條路沒有絕對贏家。如果你還在快速驗證點子、需要大量現成整合，LangChain的廣度值得借用；如果應用核心就是文件檢索，LlamaIndex的專注度會替你省下不少重工。但當產品進入生產階段、需要穩定性與對客製邏輯的完全掌控時，自己刻往往更划算——你現在用框架省下的開發時間，很可能日後要花在拆解抽象層除錯上。做決定前，先問自己:現在這個階段，我真正要優化的是開發速度、檢索品質，還是長期的可控性？

🔗 **來源**
- 標題：LangChain vs. LlamaIndex vs. Building From Scratch: Here's What I Suggest
- 作者／機構：Vinod Chugani, KDnuggets
- 連結：https://www.kdnuggets.com/langchain-vs-llamaindex-vs-building-from-scratch-heres-what-i-suggest

#LangChain #LlamaIndex #LLM #RAG #AIEngineering #SoftwareArchitecture #AgentFramework #MachineLearning #DeveloperTools #GenAI
