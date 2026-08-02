---
title: 'Weblica: Scalable and Reproducible Training Environments for Visual Web Agents'
source: Apple ML
url: https://machinelearning.apple.com/research/weblica-visual-web-agents
score: 108
model: google/gemma-4-31b-it:free
generated_at: '2026-07-07T21:01:54.336890'
---

📌 Weblica：可擴展且可重現的視覺網頁代理訓練框架  

TL;DR：Weblica 透過 HTTP 快取與 LLM 合成環境，讓視覺網頁代理能在數千種網路上進行 RL 訓練，模型在基準上優於同尺度開放權重模型且使用較少推理步驟。  

🎣 當網頁的複雜度與變化速度遠超傳統資料收集能力時，如何讓視覺網頁代理獲得足夠多樣化的訓練經驗成為瓶頸。  

🤔 背景或問題  
網頁是開放且不斷變化的系統，現有的訓練資料多半侷限於離線軌跡（用於監督微調）或僅有少數模擬環境（用於強化學習），難以涵蓋真實網頁的多樣性。這導致擴大視覺網頁代理的訓練規模變得困難。  

🧩 方法或架構  
作者提出 **Weblica（Web Replica）** 框架，結合兩種技術來建構可重現且可擴展的網頁環境：  

1. **HTTP‑level 快取**：透過在伺服器層級快取網頁資源，能夠捕獲並重播穩定的視覺狀態，同時保留原始網頁的互動行為。  
2. **LLM‑based 環境合成**：利用大型語言模型，以真實網頁為基礎並結合核心網頁導航技能，合成出多樣化的網頁環境。  

透過此框架，研究團隊得以將強化學習訓練規模擴展至 **數千種不同的網頁環境與任務**。  

📊 資料或結果  
使用 Weblica 框架訓練得到的 **Weblica‑8B** 模型在多個網頁導航基準上：  

- 優於相同參數規模的開放權重基線模型。  
- 達到同等或更好的表現時，**使用較少的推理步驟**。  
- 隨著額外的測試時間運算（test‑time compute）增加，效能呈 favourable（有利）的擴展趨勢。  
- 與商業 API 模型的表現具有競爭力。  

💡 深入分析  
HTTP 快取確保環境在重播時保持視覺穩定與互動正確，這對於強化學習中需要一致的狀態回饋至關重要。同時，LLM 合成能夠基於真實網頁的結構與導航模式產出大量變體，從而在不需蒐集真實流量的情況下擴展環境多樣性。兩者結合使得訓練既可重現（因快取保證相同輸入）又可擴展（因 LLM 能生成無限變體），從而在同等模型尺度下達到更佳的樣本效率。  

🎯 實務啟示  
對於希望打造視覺網頁代理或其他網頁互動任務的工程師，可參考 Weblica 的思路：  
- 利用現有網站的 HTTP 快取機制建立可重播的互動場景。  
- 搭配語言模型進行環境或任務的程式化合成，以快速產出大規模訓練資料。  
此種「快取 + LLM 合成」的組合不僅降低對真實網頁流量的依賴，也有助於在訓練階段減少推理開銷，適合資源受限的實驗或產線原型。  

🔗 來源  
- 標題：Weblica: Scalable and Reproducible Training Environments for Visual Web Agents  
- 作者／機構：Oğuzhan Fatih Kar, Roman Bachmann, Yuanzheng Gong, Anders Boesen Lindbo Larsen, Afshin Dehghan @ Apple ML  
- 連結：https://machinelearning.apple.com/research/weblica-visual-web-agents  

#Weblica #VisualWebAgent #RLTraining #HTTPCaching #LLMSynthesis #AppleML #WebNavigation #AIAgents #ScalableAI #ReproducibleEnvironments
