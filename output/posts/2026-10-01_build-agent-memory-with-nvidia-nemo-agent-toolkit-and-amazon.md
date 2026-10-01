---
title: Build agent memory with NVIDIA NeMo Agent Toolkit and Amazon S3 Vectors
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-agent-memory-with-nvidia-nemo-agent-toolkit-and-amazon-s3-vectors/
model: claude-code/sonnet
generated_at: '2026-10-01T22:08:56.162045'
score: 86
---

📌 用 NVIDIA NeMo Agent Toolkit 打造多 Agent 記憶層

TL;DR：AWS 示範如何用 Amazon S3 Vectors 當作 NAT 的自訂記憶後端，並部署在 EKS 上實戰。

多 Agent 系統最大的痛點之一，是每次呼叫都像失憶重啟：上一輪蒐集的資料、分析出的模式，下一次對話全部歸零。AWS 這篇文章接續前一篇「為多 Agent AI 系統建立持久記憶」的架構討論，這次直接動手，示範如何把 Amazon S3 Vectors 接進 NVIDIA NeMo Agent Toolkit（NAT），變成真正可用的記憶層。

🤔 **NAT 的記憶子系統，缺的是一塊規模化後端**

NAT 是 NVIDIA 推出的開源框架，用來建構、分析與最佳化 AI agent，並且框架無關（framework-agnostic），可搭配 Strands Agents、LangChain、LlamaIndex、CrewAI 或自訂實作。它內建的記憶子系統負責儲存與擷取對話歷史、使用者偏好與長期知識，並透過 MemoryEditor 外掛介面讓開發者接上自訂後端。NAT 原生支援 Mem0、MemMachine、Redis、Zep 這幾種記憶提供者，涵蓋常見情境；但若要支撐生產環境中彈性向量儲存、強寫入一致性、並且能成本效率地擴展到數十億筆向量，文章認為 Amazon S3 Vectors 是更合適的選擇。

🧩 **三步驟接上 S3 Vectors**

實作拆成三個步驟：

1. **建立 S3 Vectors 基礎設施**：建立 vector bucket 與 index，index 維度設為 1024，對應 Amazon Titan Text Embeddings V2 的輸出，並將內容量較大的欄位標記為不可過濾（non-filterable）的 metadata。
2. **實作自訂 MemoryEditor 外掛**：這個外掛用 Titan Text Embeddings V2 產生 embedding，把每一筆記憶連同範圍化（scoped）的 metadata 一起寫入向量，並把搜尋條件轉譯成 S3 Vectors 的 metadata 查詢語法，再向 NAT 註冊讓它能被發現。
3. **設定 Agent 工作流程**：在 NAT 的 YAML 設定檔中接上這個外掛，並透過 `auto_memory_agent` 包裝器，讓使用者訊息與 Agent 回覆自動被儲存，相關上下文也會在每次呼叫前自動注入，不需要讓 LLM 主動呼叫記憶工具。

💡 **多 Agent 共用同一個記憶索引**

文章用一個投資研究情境做示範：Research Agent、Analysis Agent、Synthesis Agent 三個角色共用同一個 S3 Vectors index，各自以自己的 `agent_id` 寫入，再用 metadata 過濾來讀取彼此的成果。Research Agent 能回想起之前蒐集過的資料，避免重複呼叫 API；Analysis Agent 能延續先前識別出的模式；Synthesis Agent 則能存取累積下來的研究發現，逐步產出更完整的報告。NAT 原生的 `user_id` 用於多租戶的使用者層級隔離，文章額外引入 `team_id` 這個 metadata 欄位，在同一個索引內做多 Agent 團隊協作的分組。隨著時間推移，瑣碎的情境記憶（episodic memory）會持續累積，文章建議定期把它們整合（consolidate）成通用知識（semantic memory），觸發方式可以是排程的 cron job、向量數量門檻，或是 Agent 在完成若干研究週期後主動發出的訊號。

⚠️ **別忘了資料治理**

因為這套架構會持久化對話歷史與使用者記憶，文章特別提醒要規劃好留存政策，利用文中提到的記憶整合與刪除路徑來淘汰不再需要的資料；metadata 中不應儲存個資（PII），敏感欄位在送進 embedding 前要先遮罩或代符化（tokenize）；並且建議用每租戶獨立的 index 搭配最小權限（least-privilege）的 IAM 政策，確保每個 Agent 只能存取屬於自己的那部分記憶。至於效能面，文章雖然提供了 `nat eval` 評估框架可以比較有無記憶的兩種跑法，但也明確說明這些只是「方向性的預期，而非已經實測出的基準數據」，實際效果會因上下文重用程度、Agent 協作數量、以及檢索的 top-k 預算大小而有所不同。

🎯 **實務啟示**

部署面上，文章選擇 Amazon EKS 而非全託管的 Amazon Bedrock AgentCore，理由是團隊若需要完整掌控擴展、網路與生命週期管理，EKS 搭配 IAM Roles for Service Accounts（IRSA）能原生整合 IAM 權限。每個 Agent 類型是獨立的 Kubernetes Deployment，透過 HorizontalPodAutoscaler 依 CPU 使用率自動擴展，而 S3 Vectors 的強寫入一致性代表任何 Pod 寫入的記憶都能立即被其他 Pod 看到，不需要額外處理快取失效。如果你的團隊正在評估客服、DevOps 自動化、法律研究或科學研究這類需要「越用越聰明」的多 Agent 場景，這套模式值得作為記憶層架構的參考起點。

🔗 **來源**
- 標題：Build agent memory with NVIDIA NeMo Agent Toolkit and Amazon S3 Vectors
- 作者／機構：Venkata Sistla（AWS）
- 連結：https://aws.amazon.com/blogs/machine-learning/build-agent-memory-with-nvidia-nemo-agent-toolkit-and-amazon-s3-vectors/

#AIAgents #AgentMemory #NVIDIA #NeMoAgentToolkit #AmazonS3Vectors #AWS #EKS #MultiAgentSystems #VectorDatabase #LLMOps
