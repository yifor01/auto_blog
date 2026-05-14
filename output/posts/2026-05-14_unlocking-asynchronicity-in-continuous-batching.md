---
title: "Unlocking asynchronicity in continuous batching"
source: HuggingFace Blog
url: https://huggingface.co/blog/continuous_async
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:46:19.825184
---

📌 【HuggingFace 最新技術博文】解鎖異步批次：讓 GPU 永遠滿載的秘訣  

你以為持續批次已經把 GPU 用到極限？其實 CPU 與 GPU 仍在輪流等待，閒置時間可能佔總執行時間的四分之一。  

🤔 **持續批次的同步瓶頸**  
HuggingFace 團隊指出，現有的 Continuous Batching 能透過 tightly packed batches 減少 padding 浪費，但預設是同步執行：CPU 準備好一批後才把資料送給 GPU，GPU 完成前向運算再把結果傳回 CPU。這種「輪流等待」的模式會讓雙方都有 idle 隙間，在每秒數百步的迴圈中累積下來，幾乎浪費了 25% 的總運行時間。  

🧪 **異步批次的設計概念**  
為了讓 GPU 持續忙碌，作者提出 **asynchronous batching**：將 CPU 的批次準備（選擇請求、更新 KV cache、驅逐已完成請求、填入新請求）與 GPU 的批次計算（前向運算、取樣）分離，讓兩者可以平行進行。這樣只要有一端有工作可做，另一端就不會被迫等待。  

🚀 **核心發現：閒置時間大幅下降**  
透過將 CPU 與 GPU 工作流程解耦，理論上可以把先前因同步造成的 ~25% idle time 消除，從而讓 GPU 的 utilisation 接近 100%。實際上，這意味著在同樣的硬體（例如 H200）下，吞吐量可顯著提升，相應的每小時成本也能被更有效地攤薄。  

💡 **為何這對 LLM 服務很重要**  
- **成本效益**：H200 在 Inference Endpoints 上約 $5/hr，一天運行即 $120。提升 GPU 使用率直接降低每 token 的服務費用。  
- **擴展性**：在高併發場景中，減少 idle 時間意味著相同硬體能服務更多請求，或在相同流量下使用更少的卡數。  
- **與現有技術互補**：異步批次不取代 FlashAttention、KV cache 等優化，而是與它們疊加，進一步壓榨硬體潛力。  

⚠️ **目前說明的限制**  
- 博文僅介紹概念與理論分析，未提供具體基準測試數據或 ablation 研究。  
- 實作細節（例如如何在現有框架中切換為異步模式）尚未在該篇文章中展開。  
- 討論焦點在單一 GPU 情境，多節點或 pipeline parallelism 的互動仍需進一步探討。  

🎯 **實務啟示**  
1. 若你正在使用 HuggingFace 的 Text Generation Inference (TGI) 或自行建構的 LLM serving 服務，可評估是否能將批次準備與模型運算解耦。  
2. 關注庫或框架是否已提供非同步批次的 API（例如 torch.cuda.Stream、CUDA Graphs 或自訂的 producer-consumer 模式）。  
3. 在成本模型中納入 GPU utilisation 的提升預估，以更精確地規劃擴容或縮容決策。  

🔗 **原始連結**  
📝 Unlocking asynchronicity in continuous batching  
👤 Rémi Ouazan Reboul, Pedro Cuenca, Aritra Roy Gosthipaty @ HuggingFace  
🔗 https://huggingface.co/blog/continuous_async  

你有在服務端嘗試過將 CPU 與 GPU 工作流程分離的經驗嗎？歡迎在留言區分享你的觀察與實作心得 👇  

#HuggingFace #LLMInference #ContinuousBatching #AsynchronousBatching #GPUUtilization #AIEngineering #深度學習 #推理最佳化
