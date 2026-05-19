---
title: "DashAttention: Differentiable and Adaptive Sparse Hierarchical Attention"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.18753
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:35:29.395823
---

📌 **DashAttention：可微分自適應稀疏階層注意力**

你以為稀疏注意力只能犧牲精度才能加速？研究顯示，當選塊數量能隨查詢自適應變化時，梯度也能暢通流動，長文建模卻不打折。

🤔 **稀疏注意力的固定 k 限制梯度流**  
現有階層注意力（如 NSA、InfLLMv2）先用粗粒度分數挑選 top‑k 個 KV 塊，再在被選 token 上做細粒度 softmax。top‑k 的硬閥值假設每個查詢相關 token 數固定，且阻斷了稀疏階段與密集階段間的梯度傳遞，使端到端訓練變得困難。

🧪 **α‑entmax 自適應選塊 + 雙階層結構**  
我們提出 DashAttention，第一階段使用可微分的 α‑entmax 變換，依據當前查詢動態決定保留多少塊（變數 k），這樣的選塊結果直接作為第二階段 softmax 的先驅。由於 α‑entmax 是光滑可導的，整個階層保持端到端可微分，梯度能同時穩定流經稀疏與密集兩個階段。

🔑 **75% 稀疏下精度媲美全注意力，且勝過 FlashAttention-3**  
在大型語言模型上的實驗表明：  
- 在 75% 稀疏度下，DashAttention 的準確度與全注意力相當；  
- 與 NSA、InfLLMv2 相比，其在精度‑速度 Pareto 前緣更優，尤其在高稀疏區域表現突出；  
- 基於 Triton 的 GPU‑aware 實作在推理階段實現了超過 FlashAttention-3 的加速比。

💡 **可微分階層讓梯度暢通，提升長文建模**  
因為選塊過程可導，模型能學習到何時該保留更多塊、何時可更激進地稀疏。這種自適應特性使得 DashAttention 在長序列上不會出現分散（non‑dispersive）現象，從而在保持計算效率的同時獲得更好的長上下文建模能力。

⚠️ **僅在 LLM 上驗證，未見極端長度基準**  
實驗主要聚焦於標準語言模型基準，尚未在極端長度（如 100K+ token）或非語言任務上進行系統化評估；理論上可微分特性預期適用於更廣場景，但需進一步驗證。

🎯 **適合推理加速的 GPU 核心實作**  
- 開發者可直接引用 Triton 內核，在現有 LLM 推理管線中插入 DashAttention 以獲得顯著速度提升；  
- 在追求高吞吐與低延遲的服務場景中，該方法提供了一個「可訓練」的稀疏注意力選項，避免了重新調整 top‑k 超參數的需求。

🔗 **論文連結**  
📝 DashAttention: Differentiable and Adaptive Sparse Hierarchical Attention  
👤 Yuxiang Huang, Nuno M. T. Gonçalves, Federico Alvetreti, Lei Li, Xu Han（Tsinghua University; Instituto Superior Técnico, Universidade de Lisboa; Instituto de Telecomunicações; Carnegie Mellon University; Sapienza University of Rome; University of Edinburgh; TransPerfect; ELLIS Unit Lisbon）  
🔗 https://arxiv.org/abs/2605.18753

你目前的稀疏注意力策略是固定 k 还是自適應？歡迎在留言區分享經驗或疑問 👇

#AI #AttentionMechanism #LLM #EfficientInference #Triton #DashAttention #Tsinghua #CMU #ResearchPaper
