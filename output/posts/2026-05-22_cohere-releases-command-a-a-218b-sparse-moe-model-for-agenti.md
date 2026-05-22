---
title: "Cohere Releases Command A+: A 218B Sparse MoE Model for Agentic Workflows That Runs on as Few as Two H100 GPUs"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/21/cohere-releases-command-a-a-218b-sparse-moe-model-for-agentic-workflows-that-runs-on-as-few-as-two-h100-gpus/
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:55:00.584204
---

📌 【Cohere 發布】Command A+：218B 參數穩疏 MoE 模型，僅需兩顆 H100 即可運行  

隨著企業對「Agentic 工作流程」的需求快速上升，單一模型若要同時兼顧推理、多模態、長上下文與多語言處理，往往需要龐大的計算資源。Cohere 最新釋出的 Command A+ 聲稱能在只有兩顆 H100 GPU 的環境下運行，這到底是如何實現的？

🤔 **穩疏架構讓巨模型變得可部署**  

Command A+ 是一個 Decoder‑only 的 Sparse Mixture‑of‑Experts (MoE) Transformer，總參數達 218B，但每個 token 在前向傳遞時只啟用 25B 參數（8 個專家＋1 個共享專家）。這種設計意味著理論上的計算量與一個 25B 參數的密集模型相當，卻保有更大的專家空間來處理不同類別的任務。

🧪 **模型結構與量化選項**  

- **專家配置**：128 個專家，每 token 路由至 8 個專家，另加一個共享專家作用於所有 token。  
- **注意力層**：滑動窗口注意力與全域注意力以 3:1 的比例交錯，滑動窗口使用 Rotational Positional Embedding，全域注意力則不加位置編碼。  
- **輸入/輸出模態**：接受文字、圖像與工具使用；產出文字、推理結果與工具調用。  
- **上下文長度**：最大 128K 輸入、64K 生成。  
- **量化版本**（品質差異可忽略不計）：  
  * BF16 (16-bit)：需 4× B200 或 8× H100  
  * FP8 (8-bit)：需 2× B200 或 4× H100  
  * W4A4 (4-bit)：可在單顆 B200 或 2× H100 上運行  

Cohere 建議大多數部署採用 W4A4 量化，因其在保持基準表現的同時顯著降低顯卡需求。

💡 **為何這對 Agentic 工作流程特別重要？**  

Agentic 系統通常需要模型在推理過程中多次調用工具、進行長鏈結的思考與多模態檢索（RAG）。Command A+ 的穩疏設計讓模型在保持高參數容量（利於知識儲存與多任務能力）的同時，實際運算量只相當於較小的密集模型，這意味著在同等硬體預算下，可以支援更長的思考鏈或更頻繁的工具調用，而不會因顯卡記憶體或算力瓶頸而受限。

⚠️ **已知限制與待驗證點**  

- 文章僅描述了推理端的量化與硬體需求，未提供模型訓練細節（資料規模、訓練時長、優化器設定等）。  
- 基準表現（「品質差異可忽略不計」的說明）缺乏具體數據分析，難以判斷在特定任務（例如複雜推理或細粒度多模態理解）上的實際表現。  
- 目前僅提及了 W4A4、FP8、BF16 三種量化方式，未探討更極端的低位元（如 2-bit）或混合精度的可能性。  

🎯 **實務建議**  

- 若貴公司的 Agentic 應用需要在單節點或雙節點 GPU 伺服器上運行，優先考慮 W4A4 量化版本，這樣可在兩顆 H100 上獲得完整的 218B 模型容量。  
- 在評估時，建議先在貴司的具體工具鏈與 RAG 流程上進行小規模基準測試，觀察延遲與吞吐量的實際表現。  
- 關注後續社區發布的微調指南或 LoRA 適配方案，以便在不犧牲推理效率的前提下，將模型適配至專屬領域任務。  

🔗 **論文／發布連結**  
📝 Cohere Releases Command A+: A 218B Sparse MoE Model for Agentic Workflows That Runs on as Few as Two H100 GPUs  
👤 Michal Sutter (MarkTechPost)  
🔗 https://www.marktechpost.com/2026/05/21/cohere-releases-command-a-a-218b-sparse-moe-model-for-agentic-workflows-that-runs-on-as-few-as-two-h100-gpus/  

你認為這種穩疏 + 極致量化的路線，是否會成為未來企業級 Agentic 系統的標準配置？歡迎在留言區分享你的看法 👇  

#Cohere #CommandAPlus #MoE #AgenticAI #H100 #LLM #開源模型 #AI推理 #量化技術 #多模態 #RAG #工程實務
