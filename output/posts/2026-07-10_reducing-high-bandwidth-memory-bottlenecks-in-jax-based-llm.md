---
title: Reducing High-Bandwidth Memory Bottlenecks in JAX-Based LLM Training with Host
  Offloading
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/reducing-high-bandwidth-memory-bottlenecks-in-jax-based-llm-training-with-host-offloading/
score: 95
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T08:12:47.923658'
---

📌 JAX 主機卸載緩解 HBM 瓶頸，提升大模型訓練吞吐  

TL;DR：將啟用移至 pinned 主記憶體並流回反向傳播，可將吞吐提升最高 57% 並支援更大批次。  

🎣 當模型、序列長度與批次持續增大時，GPU 高頻寬記憶體（HBM）常在運算資源被充分利用前就成為瓶頸，導致訓練效能受限。  

🤔 背景或問題  
大型語言模型訓練需要同時容納模型權重、梯度、最佳化器狀態、通訊緩衝區以及中間啟用，這些都佔用 GPU 的 HBM。隨著模型規模、序列長度與批次增大，HBM 容量往往成為首要擴展瓶頸。  

🧩 方法或架構  
NVIDIA 部落格介紹的 JAX 主機卸載（host offloading）機制，會選擇性地將部分啟用移至 pinned 主記憶體，並在反向傳播階段透過管線化傳輸（pipelined transfers）將資料流回 GPU。為了隱藏延遲，該方法結合了 Latency Hiding Scheduler 與專用的複製串流（dedicated copy streams），並透過 XLA 自訂排程旗標（custom scheduling flags）來排程啟用傳輸與運算、通訊的重疊。正確的重疊是達到最佳效能的關鍵，需透過分析工具（如 NVIDIA Nsight Systems）驗證非同步資料移動與記憶體使用率是否符合預期。  

📊 資料或結果  
在 NVIDIA GB200 NVL72 平臺上，使用 MaxText 框架對 DeepSeek‑V3 671B 與 Llama 3.1 405B 進行實驗，結果顯示：  
- 與僅依賴啟用重新計算（activation rematerialization）相比，主機卸載結合 Latency Hiding Scheduler 與管線化傳輸可帶來最高 **57%** 的吞吐提升。  
- 此技術解鎖了原本受限於 GPU 記憶體的批次大小，使得更大批次成為可能。  
- 收益在大規模稀疏混合專家（sparse MoE）模型上最為顯著。  

💡 深入分析  
作者強調，僅啟用 host offloading 不一定能自動帶來效能提升；必須確保啟用的主機↔GPU 傳輸與計算、通訊有足夠的時間重疊。此重疊透過 XLA 的排程旗標與專用複製串流來實現，建議使用 Nsight Systems 進行設定檢視與調整，以確認非同步資料移動的效果是否達到預期的記憶體緩解與吞吐提升。  

⚠️ 限制  
文章未提及具體的硬體或軟體版本號，僅說明在 Grace Blackwell 與 Vera Rubin 平臺（受益於高頻寬 NVLink‑C2C 互連）上觀察到改善。實際部署時，仍需依具體模型與工作負載進行調校，且未涵蓋所有模型型別的普遍適用性。  

🎯 實務啟示  
對於使用 JAX 進行大規模 LLM 訓練的工程師，可考慮：  
1. 在 JAX 啟用 host offloading 旗標，並搭配 Latency Hiding Scheduler 與管線化傳輸設定。  
2. 使用 XLA 自訂排程旗標排程啟用傳輸，使其與矩陣乘法、All‑Reduce 等運算重疊。  
3. 透過 Nsight Systems 檢視記憶體頻寬與複製串流的使用率，確認資料移動確實隱藏了延遲。  
此做法特別適合在具備高頻寬 NVLink‑C2C 互連的 NVIDIA Grace Blackwell 或 Vera Rubin 系統上訓練巨大稀疏 MoE 模型，可在不增加 GPU 記憶體的前提下，提升批次與序列長度，進而提升訓練效能。  

🔗 來源  
- 標題：Reducing High-Bandwidth Memory Bottlenecks in JAX-Based LLM Training with Host Offloading  
- 作者／機構：Jane (Zhenying) Liu, Ming Huang, Johannes Reifferscheid, Michael Goldfarb, Tejash Shah @ NVIDIA Developer  
- 連結：https://developer.nvidia.com/blog/reducing-high-bandwidth-memory-bottlenecks-in-jax-based-llm-training-with-host-offloading/  

#JAX #HostOffloading #HBM #LLMTraining #NVIDIA #GraceBlackwell #VeraRubin #MaxText #DeepSeekV3 #Llama3
