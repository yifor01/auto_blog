---
title: "Long-Context Aware Upcycling: A New Frontier for Hybrid LLM Scaling"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.24715
score: 111
model: tencent/hy3-preview:free
generated_at: 2026-04-28T20:26:23.053615
---

📌 **Long‑Context Aware Upcycling：把現有 Transformer 變長上下文混合模型的實作路徑**  

你手頭的 Llama 或 Qwen 模型，明明已有強大的短文理解能力，卻在 64K token 以上就爆記憶體？如果能在不重新從零預訓練的情況下，直接把它「升級」成能處理 2M token 的混合架構，那麼成本與延遲到底能省下多少？  

🤔 **為何現有混合模型難以重用既有 Transformer 權重？**  
近年提出的混合序列模型（Transformer + 線性塊）在長文建模上很有潛力，但多數是從頭開始預訓練，導致無法直接利用已有的 Transformer 權重。這意味著工程團隊必須付出額外的算力與資料成本，才能換取長上下文的好處。  

🧪 **HyLo 的架構與訓練配方**  
AMD 團隊提出 HyLo（Hybrid Long‑context），一套「後訓練 upcycling」食譜：  
- 先對預訓練好的 Transformer 做架構適應，插入高效的 Transformer 塊、Multi‑Head Latent Attention (MLA) 與線性塊（Mamba2 或 Gated DeltaNet）；  
- 採用分階段的長文訓練，搭配師模型導向的蒸餾，使最佳化過程更穩定；  
- 整個流程僅需額外的後訓練步驟，無需從零開始。  

🚀 **可擴展至 2M token、KV‑cache 壓縮 90%+**  
透過 HyLo，可將可用上下文長度擴展至原始模型的 32 倍，實際上在他們的 vLLM 推送堆疊中支援 2M‑token 的 prefill 與 decoding。同時，KV‑cache 的記憶體佔減少超過 90%，相較於傳統 Llama 基線在超過 64K token 時就會記憶體耗盡。  

💡 **在長基準上超越需 400B token 訓練的模型**  
在 1B 與 3B 規模（Llama‑與 Qwen‑變體）的實驗中，HyLo 同時保持短文表現與提升長文能力，在 RULER 等長文評測上明顯優於現有的 upcycled 混合基線。更值得注意的是，HyLo‑Qwen‑1.7B 僅使用 10B token 進行後訓練，就在 GSM8K、LM‑Harness 常識推理以及 RULER‑64K 上顯著擊敗了需要 400B token 訓練的 JetNemotron。  

⚠️ **研究限制：僅在特定規模與基準測試**  
目前結果僅在 1B‑3B 規模的 Llama/Qwen 變體上驗證，長文評估主要依賴 RULER 等合成基準，尚未在更大規模或真實多語料長文任務上進行廣泛測試。此外，後訓練的 token 數量（10B）雖遠低於從頭預訓練，但仍需額外計算資源。  

🎯 **對工程師的啟示：可透過後訓練升級既有模型**  
- 若團隊已擁有 Transformer 權重，不必重新從零預訓練，即可透過 HyLo 的架構適應與階段式長文訓練取得長上下文優勢。  
- KV‑cache 大幅減少意味著在同等硬體下可處理更長的 prompt 或批次，降低推論成本。  
- 在資源受限的情況下，適量的後訓練（如 10B token）就能在常見推理與常識基準上達到甚至超過大規模預訓練模型的表現。  

🔗 **論文連結**  
📝 Long‑Context Aware Upcycling: A New Frontier for Hybrid LLM Scaling  
👤 Parsa Ashrafi Fashi, Utkarsh Saxena, Mehdi Rezagholizadeh, Aref Jafari, Akash Haridas @ AMD  
🔗 https://arxiv.org/abs/2604.24715  

你是否正在評估如何在不犧牲現有模型的前提下擴展上下文？歡迎在留言區分享你的想法或實作經驗 👇  

#AI #LLM #HybridModel #LongContext #AMD #vLLM #機器學習 #自然語言處理
