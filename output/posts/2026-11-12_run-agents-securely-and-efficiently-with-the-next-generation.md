---
title: Run agents securely and efficiently with the next generation AgentCore runtime
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/run-agents-securely-and-efficiently-with-the-next-generation-agentcore-runtime/
model: claude-code/sonnet
generated_at: '2026-11-12T22:58:47.763876'
score: 90
---

📌 【AWS基礎設施】Agent會話啟動快15倍，隔離安全與用量計價怎麼兼顧

TL;DR：新一代Bedrock AgentCore runtime用Firecracker微型VM隔離每個會話，啟動更快、計費更貼近實際用量。

AI Agent 能夠自主完成的任務長度，大約每四個月翻倍（METR），McKinsey 的調查也顯示大型企業正在規模化部署 AI Agent 的比例，一年內從27%升到40%。但 Deloitte 的數據同時指出，只有15%的組織真正做到規模化的多 Agent 協作，70%的組織坦承還無法信任或治理自己的 Agent——規模化的瓶頸,正從「Agent能做什麼」轉向「能否安全、可靠、經濟地大規模運作」。

🤔 **隔離要夠強，成本和速度卻常常互相拖累**

Agent 會執行程式碼、操作瀏覽器、存取敏感資料、代表使用者行動，這些能力比傳統軟體帶來更高的安全與基礎設施要求，每個 Agent 會話都需要獨立隔離的環境。但預先佈建（pre-provisioned）的環境即使閒置也持續耗用資源、拉高成本；隨需（on-demand）環境雖然減少浪費，卻引入冷啟動延遲。當企業從部署少數幾個 Agent 走向同時執行數千個會話，自建與管理沙箱環境的複雜度、成本和不可預測性都會急速上升。

🧩 **核心保證不變，效能與計價全面升級**

AWS 宣布更新 Amazon Bedrock AgentCore runtime（AgentCore 的受管運算層），核心安全保證維持不變：每個會話都在自己專屬的、硬體層級隔離的 Firecracker 微型虛擬機（MicroVM）中執行，擁有自己的身分、政策與稽核紀錄。在這個保證之上，這次更新把會話啟動速度最多提升15倍，可擴充的運算資源提高到4倍，執行效率最多提升68%。

具體規格上，會話現在最多可擴充到8個vCPU與32GB記憶體，支援最大10GB的容器映像檔，而且啟動時間縮短到2秒以內,不受映像檔大小或併發數量影響,不再需要維護warm pool或預先佈建叢集來應付冷啟動。

計價邏輯也同步調整：runtime 會在 Agent 釋放記憶體後的幾分鐘內就回收資源，閒置中的 Agent 會自動縮減到零用量,對於多輪對話之間常有自然停頓的 Agent 來說，這能讓每個會話的記憶體耗用減少最多68%。對於24小時運作的 Agent，則提供承諾基線（committed baseline）計價：設定一個記憶體基線作為最低計費量，並允許臨時爆發（burst）到該基線的4倍，以接近 AWS Lambda MicroVM 的費率計價。

📊 **多家企業的實測數字**

文章引用了幾家客戶的早期數據：Mission Cloud 比較新舊兩版 runtime 後，推論請求的冷啟動快了35%，健康檢查啟動快了77%，單次呼叫的runtime成本下降17%；Zuora表示在許多使用情境下，每次呼叫的記憶體用量減少了約60%；Coinbase則用它來跑隔離的程式碼生成 Agent 會話，Rescale 用它跑工程模擬相關的 Agent，Deloitte Consulting 也提到新版本讓啟動更快、記憶體使用更有效率。

💡 **隔離不能只管運算，資料邊界也要補上**

文章指出,許多企業的 Agent 安全模型存在一個長期缺口：Agent 本身跑在隔離會話內，但它需要的資料卻在這個邊界之外。長時間運作的 Agent 會不斷累積檔案、憑證、工具輸出等上下文，團隊因此得自己建一套規則管理資料怎麼進出，每多一個 Agent 就多一分複雜度與風險。只隔離運算層,等於只做了一半的邊界。

⚠️ **侷限**

文章並未提供資料邊界這部分具體如何封閉的技術細節，僅點出這是現有安全模型的缺口，值得持續關注後續釋出的機制。

🎯 **實務啟示**

對正在評估 Agent 執行環境的團隊來說，這次更新提供了一個可以直接比較的參考點：是否支援秒級啟動、是否按實際用量計費、以及隔離邊界是否只停在運算層。在挑選基礎設施時，這些都是值得向供應商具體詢問的問題。

🔗 **來源**
- 標題：Run agents securely and efficiently with the next generation AgentCore runtime
- 作者／機構：Madhu Parthasarathy
- 連結：https://aws.amazon.com/blogs/machine-learning/run-agents-securely-and-efficiently-with-the-next-generation-agentcore-runtime/

#AWSBedrock #AgentCore #AIAgents #Firecracker #MicroVM #CloudInfrastructure #AgenticAI #Serverless #AIInfra #AWS
