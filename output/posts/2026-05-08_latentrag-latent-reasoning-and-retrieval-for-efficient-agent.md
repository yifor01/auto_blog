---
title: "LatentRAG: Latent Reasoning and Retrieval for Efficient Agentic RAG"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.06285
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-08T20:25:41.045715
---

📌 **LatentRAG 隐空间Agentic RAG降90%延迟**

Agentic RAG 能處理複雜問題卻因高延遲難落地？阿姆斯特丹大學團隊提出 LatentRAG，把推理與檢索轉到隱空間，延遲直接降 90%。

🤔 **Agentic RAG 效果好但延遲高，難以實時部署**
單步檢索增強生成（RAG）能高效整合外部資訊處理簡單問答，但面對複雜問題時表現不佳。Agentic RAG 擴展了單步範式，改為多步流程：大型語言模型（LLM）作為搜索代理，生成中間思考與子查詢，迭代與檢索系統交互。不過這種迭代流程需要自回歸生成冗長的自然語言思考與子查詢，帶來極高的推理延遲。

🧪 **將推理、檢索從離散語言空間轉到連續隱空間**
為解決上述延遲問題，研究團隊提出 LatentRAG 框架，將推理與檢索從離散語言空間轉移到連續隱空間。不同於現有顯式方法逐 token 生成自然語言思考或子查詢，LatentRAG 直接從 LLM 的隱藏狀態透過單步前向傳播生成對應的隱 token。團隊在隱空間對齊 LLM 與稠密檢索模型，實現基於隱式子查詢 token 的檢索，並支援端到端聯合優化。為提升透明度與語義豐富度，LatentRAG 還加入並行隱解碼機制，可將隱 token 翻譯回自然語言。

📈 **7個基準測試性能媲美顯式Agentic RAG，延遲降90%**
在 7 個基準數據集上的大量實驗顯示，LatentRAG 的任務性能與顯式 Agentic RAG 方法相當，同時推理延遲降低約 90%，大幅縮小了與傳統單步 RAG 的延遲差距。

💡 **隱空間單步生成省去逐token自回歸開銷**
顯式 Agentic RAG 的延遲瓶頸來自於逐 token 自回歸生成自然語言中間內容，每次迭代都需等待完整生成
