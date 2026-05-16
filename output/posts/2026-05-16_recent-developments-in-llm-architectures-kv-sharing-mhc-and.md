---
title: "Recent Developments in LLM Architectures: KV Sharing, mHC, and Compressed Attention"
source: Sebastian Raschka
url: https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-05-16T19:27:45.737596
---

📌 【Sebastian Raschka】LLM 架構新趨勢：KV Sharing、mHC 與壓縮注意力  

長上下文變成瓶頸？最新開源模型正在悄悄重塑 Transformer 內部結構。  

🤔 **為何長上下文效率成為當下重點**  
隨著推理模型與 Agent 工作流需要保留更多 token 時間，KV‑cache 大小、記憶體傳輸與注意力運算成本快速成為系統瓶頸。Sebastian Raschka 指出，近期多個開源 LLM 開始在架構層面加入技巧，以緩解這些限制，而這些技巧多半聚焦在 Transformer block、殘差流、KV‑cache 或注意力計算上。  

🧪 **文章覆蓋的四個架構變化**  
文章分別介紹了：  
- **Gemma 4** 中的 KV sharing 與 per‑layer embeddings  
- **ZAYA1‑8B** 的壓縮卷積注意力（compressed convolutional attention）  
- **Laguna XS.2** 的層級注意力預算（layer‑wise attention budgeting）  
- **DeepSeek V4** 的 mHC 與壓縮注意力（mHC + compressed attention）  

這些被描述為在架構圖上可能只是小調整，但實際涉及較精細的設計決策。  

🔍 **核心概念與動機**  
- **KV sharing**：透過讓不同層共享部分鍵值對（key‑value）來降低快取重複與記憶體佔用。  
- **per‑layer embeddings**：為每層提供獨特的嵌入，使共享 KV 仍能保有層別特徵。  
- **壓縮卷積注意力**：將標準點積注意力替換為較輕量的卷積運算，同時保持長距離資訊捕捉能力。  
- **層級注意力預算**：根據每層的任務重要性分配不同的注意力運算量，避免在不需要細粒度匹配的層浪費資源。  
- **mHC（mixed‑head concatenation）**：將多頭注意力的輸出以不同方式結合，以在效率與表達力之間取得平衡。  

💡 **這些設計對長上下文應用的啟示**  
文章強調，上述技巧並非互斥，開發者可根據模型規模、硬體預算與目標任務（例如長文件問答、多步驟 Agent 推理）選擇組合。例如，KV sharing 直接降低快取記憶體，而壓縮卷積注意力則在計算密集的注意力層提供替代方案；層級預算則允許在早期層保留完整注意力，後期層則可適度裁減。  

⚠️ **文章說明的範圍與限制**  
Sebastian Raschka 明確表示，本文僅討論架構層面的變化，並不涉及資料混合、訓練排程、後訓練細節、強化學習配方或基準表現。因此，讀者若想了解這些技巧在實際訓練或推論中的具體效益，仍需參考原始論文或模型卡片。此外，文章僅挑選作者覺得有趣且尚未在先前文章中討論過的設計，未涵蓋所有近期 LLM 架構創新。  

🎯 **實務上的參考方向**  
- 若正在設計或選擇長上下文模型，可先檢查模型是否採用 KV sharing 或 per‑layer embedding 來減少快取壓力。  
- 對於計算資源受限的環境，壓縮卷積注意力或層級注意力預算提供可行的替代方案。  
- 在實驗時，建議將上述架構變化與訓練策略分開評估，以清楚隔離其對效率與準確度的貢獻。  

🔗 **文章連結**  
📝 Recent Developments in LLM Architectures: KV Sharing, mHC, and Compressed Attention  
👤 Sebastian Raschka  
🔗 https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures  

你在長上下文模型設計上有試過哪些架構技巧？歡迎在留言區分享經驗與問題 👇  

#LLM #Transformer #KVSharing #mHC #CompressedAttention #Gemma4 #ZAYA1 #LagunaXS2 #DeepSeekV4 #SebastianRaschka #AI架構 #長上下文 #推理模型 #AgentWorkflow
