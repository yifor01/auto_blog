---
title: 'Meituan Releases LongCat-2.0: A 1.6T-Parameter Open MoE Model with Native
  1M Context and LongCat Sparse Attention'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/05/meituan-releases-longcat-2-0-a-1-6t-parameter-open-moe-model-with-native-1m-context-and-longcat-sparse-attention/
score: 97
model: google/gemma-4-31b-it:free
generated_at: '2026-07-06T20:25:00.287774'
---

📌 美團發布 LongCat-2.0：1.6T 引數 MoE 模型，支援 1M 上下文  

TL;DR：Meituan 釋出 1.6T 引數開放 MoE 模型 LongCat-2.0，原生支援 1M token 上下文，專注代理編碼。  

🎣 當大型語言模型仍被 GPU 卡住時，美團卻在國產 AI 晶片上跑出千億引數的 MoE。這意味著什麼？對從事代理編碼的工程師來說，是機會還是挑戰？  

🤔 背景或問題  
隨著代理（Agent）工作流程對程式碼理解、產生與執行的需求升長，單一密集模型在計算與記憶體上的成本成為瓶頸。Meituan 之前已發布 LongCat‑Flash（560B 引數），但業界亟需更大規模、更長上下文且能在非 Nvidia 硬體上穩執行的模型，以支援真實的代理編碼場景。  

🧩 方法或架構  
LongCat‑2.0 採用 Mixture‑of‑Experts（MoE）設計，總引數達 1.6 兆，每個 token 只啟用約 48 億引數。模型具備原生 100 萬 token 的上下文視窗。訓練與推理完全在國產 AI ASIC 超級計算平臺（superpod）上進行。為降低規模成本，架構結合了四項技術：  
- 6D 並行方案  
- prefill‑decode 分離架構  
- 超核（super kernels）  
- L2 快取權重預取（L2‑cache weight prefetching）  
預訓練階段處理了超過 35 兆個 token，佔用數百萬加速器小時，期間未出現回滾或無法復原的損失尖峰。  

📊 資料或結果  
Meituan 在內部測試中報告：  
- 在 SWE‑bench Pro 上，LongCat‑2.0 得分 58.6，略領先於 GPT‑5.5  
- 整體表現與 Google Gemini 3.1 Pro 相當  
- 在較廣泛的代理基準 FORTE 與 BrowseComp 上，模型落後於領先的前沿系統  
目前尚無獨立排行榜確認結果。  

💡 深入分析  
該模型的穩定宣告尤為重要：在非 Nvidia 硬體上能進行大規模 MoE 訓練且不出現損失波動，顯示國產 ASIC 工具鏈已達到可用於千億引數級別工作的成熟度。同時，LongCat‑2.0 明確定位為「代理編碼」模型，最佳化於程式碼理解、生成與執行，而非一般對話聊天。這意味著在特定軟體工程工作流程中可能獲得更佳效能，但在更廣泛的通用代理任務上仍有提升空間。  

⚠️ 限制  
- 模型針對代理編碼最佳化，在一般代理基準（FORTE、BrowseComp）上表現不如領先系統  
- 缺乏公開的獨立基準驗證，實際表現仍需社群進一步確認  
- 使用國產 ASIC 超級計算平臺，對於習慣 Nvidia 生態系統的團隊可能需要適應新的硬體與軟體棧  

🎯 實務啟示  
從事代理編碼或自動化程式生成的工程團隊，可評估 LongCat‑2.0 作為後端模型的可行性，特別是當他們擁有或可存取國產 AI ASIC 計算資源時。由於模型專注於長上下文與穩定的 MoE 推理，適合需要處理大型程式碼庫或多輪對話的代理工作流。同時，團隊應該注意模型目前尚未開放完整的推理或微調工具，需關注後續社群或官方發布的 SDK 與範例。  

🔗 來源  
- 標題：Meituan Releases LongCat-2.0: A 1.6T-Parameter Open MoE Model with Native 1M Context and LongCat Sparse Attention  
- 作者／機構：Asif Razzaq @ MarkTechPost  
- 連結：https://www.marktechpost.com/2026/07/05/meituan-releases-longcat-2-0-a-1-6t-parameter-open-moe-model-with-native-1m-context-and-longcat-sparse-attention/  

#LongCat2 #Meituan #MoE #1MContext #AgenticCoding #AIASIC #SWEbench #Gemini3.1Pro #GPT5.5 #OpenModel
