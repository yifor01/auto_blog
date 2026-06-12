---
title: 'Meet ‘North Mini Code’: Cohere’s 30B Open-Weight Mixture-of-Experts Model
  With 3B Active Parameters for Agentic Coding'
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/11/meet-north-mini-code-coheres-30b-open-weight-mixture-of-experts-model-with-3b-active-parameters-for-agentic-coding/
score: 108
model: google/gemma-4-31b-it:free
generated_at: '2026-06-12T20:33:27.155632'
---

📌 【Cohere 最新發佈】30B 參數卻僅需 3B 運算量：North Mini Code 專為 Agentic Coding 而生

想要在自己的伺服器上運行強大的程式碼模型，但又不想被巨大的 GPU 叢集成本壓垮？Cohere 這次推出的開源權重模型 North Mini Code，試圖在「模型容量」與「推理效率」之間找到一個極端平衡點。

🎣 **30B 的容量，3B 的開銷：讓「主權 AI」成為可能**
大多數開發者在選擇模型時，常面臨兩難：小模型跑得快但能力不足，大模型能力強但部署成本極高。Cohere 提出的解決方案是：用 MoE 架構打造一個 30B 參數模型，但每個 Token 僅激活 3B 參數。這意味著你能擁有大模型的知識庫，卻只需支付小模型的運算成本。

🤔 **填補自託管 Agentic Coding 的效能缺口**
目前的趨勢是從單純的「程式碼補全」轉向「Agentic Software Engineering」（代理式軟體工程），這要求模型不僅能寫 Code，還要能處理終端機任務 (Terminal tasks) 並具備自主執行能力。North Mini Code 的定位正是為了讓團隊能夠在不依賴雲端巨頭的情況下，自行託管 (Self-host) 具備 Agent 能力的編程模型，實現真正的「主權 AI (Sovereign AI)」。

🧪 **稀疏 MoE 架構：128 個專家與混合注意力機制**
North Mini Code 採用 Decoder-only Transformer 架構，其技術設計有幾個關鍵點值得工程師關注：

- **專家系統**：Feed-forward 區塊包含 128 個專家，但每個 Token 僅激活其中 8 個。Router 在進行 top-k 選擇前會先經過 sigmoid 函數。
- **混合注意力機制**：採用 3:1 的比例交錯使用兩種 Attention。Sliding-window attention 搭配 RoPE 處理位置資訊，而 Global attention 則完全不使用位置嵌入。
- **資源需求**：權重以 BF16 形式發佈，最低硬體門檻為單張 H100 (FP8)。

🚀 **後訓練策略：從 SFT 到可驗證獎勵的 RLVR**
為了強化 Agentic Coding 能力，Cohere 的後訓練過程分為兩個階段：
1. **兩階段級聯監督微調 (Cascaded SFT)**：建立基礎的指令遵循與編程能力。
2. **可驗證獎勵的強化學習 (RLVR)**：透過可驗證的獎勵機制，優化模型在複雜編程任務中的邏輯正確性。

這使得模型原生支持「交錯思考 (Interleaved thinking)」與「原生工具調用 (Native tool use)」，這對於構建自動化編程助手至關重要。

📊 **性能表現與規格**
- **評分**：在 Artificial Analysis Coding Index 取得 33.4 分，在同尺寸模型中具有競爭力。
- **上下文窗口**：支持 256K tokens 的長文本輸入，最大輸出長度為 64K tokens。
- **輸入輸出**：純文本輸入輸出 (Text-in, Text-out)，不支援影像或影片。

⚠️ **硬體門檻依然存在，且僅限文本處理**
雖然 MoE 降低了推理成本，但最低仍需 H100 等級的 GPU 才能跑在 FP8 精度。此外，該模型完全不具備多模態能力，僅適用於純文字的編程與終端任務。

🎯 **實務啟示：自建 AI 編程 Agent 的新選擇**
對於需要高度隱私、且希望在私有環境部署編程 Agent 的團隊，North Mini Code 提供了一個極佳的基準。由於其支持長上下文與原生工具調用，開發者可以嘗試將其整合進自有的開發工作流，而非僅僅依賴 API 調用。

🔗 **相關資訊**
📝 Meet ‘North Mini Code’: Cohere’s 30B Open-Weight Mixture-of-Experts Model
👤 Asif Razzaq (via MarkTechPost)
🔗 來源：https://www.marktechpost.com/2026/06/11/meet-north-mini-code-coheres-30b-open-weight-mixture-of-experts-model-with-3b-active-parameters-for-agentic-coding/
📦 權重發佈：Apache 2.0 協議 (Hugging Face) / Cohere API / OpenRouter

你會考慮將編程 Agent 移至自託管的 MoE 模型上嗎？歡迎在評論區討論 👇

#AI #Cohere #MoE #OpenWeight #AgenticCoding #LLM #軟體工程 #主權AI
