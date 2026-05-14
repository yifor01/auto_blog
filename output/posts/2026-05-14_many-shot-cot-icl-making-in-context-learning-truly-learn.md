---
title: "Many-Shot CoT-ICL: Making In-Context Learning Truly Learn"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.13511
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:31:18.103437
---

📌 **Many-Shot CoT-ICL：讓上下文學習真正學會**

你以為把更多範例塞進 prompt 就能讓 AI 變聰明？在推理任務上，這個假設可能完全錯誤。

🤔 **推理任務下，多範例並不一定穩定提升**  
先前的 many-shot ICL 研究多聚焦於非推理任務，認為示例越多效果越好。本論文在推理導向與非推理導向的 LLMs 上，測試了 chain-of-thought (CoT) 示例的數量影響，發現擴展示例數對非推理 LLMs 的表現不穩定，而主要受益於推理導向的模型。

🧪 **跨模型與跨任務的系統化實驗**  
研究團隊在多種 LLMs（包括推理導向與非推理導向版本）與多種任務（非推理與推理導向）上，分別變更 CoT 示例的數量、檢索方式與排序，觀察準確率的變化。實驗設計涵蓋了示例數從少到多（達到幾十至上百個）的縮放測試。

🔑 **三個關鍵發現**  
1. **設定依賴的縮放效應**：增加 CoT 示例對非推理 LLMs 的影響不穩定，主要提升出現在推理導向的模型上。  
2. **相似度檢索的局限**：在非推理任務中，基於語義相似度的示例檢索能帶來幫助；但在推理任務中，語義相似度無法預測 CoT 的程序兼容性，檢索反而失效。  
3. **順序縮放效應**：隨著 CoT 示例數量增加，模型的表現方差變大，說明示例的排序對最終結果有顯著影響。

💡 **將 many-shot CoT-ICL 視為情境下的學習而非單純模式匹配**  
基於上述觀察，作者提出兩條設計原則：  
- 示例應該對目標模型而言易於理解；  
- 示例應該被排序以支撐概念的平滑遞增。  
依此原則，他們提出一種簡單的排序方法——Curvilinear Demonstration Selection (CDS)。在幾何推理基準上，使用 64 個示例時，CDS 能帶來最高 5.42 個百分點的提升。

⚠️ **研究的主要限制**  
實驗主要集中在特定的幾何與邏輯推理基準，未涵蓋更廣泛的推理領域；此外，分析多為後處理觀察，未深入探討模型內部機制為何會產生這些順序與設定依賴效應。

🎯 **對實務的啟示**  
在構建推理任務的 prompt 時，單純堆砌更多示例並不一定有效；應該注意示例的易懂度與概念遞增排序。簡單的 CDS 排序方式可作為一個低成本的啟發式工具，尤其在使用較長上下文窗口的模型時，可將緩衝區的概念轉為結構化的課程，促進真正的情境學習。

🔗 **論文連結**  
📝 Many-Shot CoT-ICL: Making In-Context Learning Truly Learn  
👤 Tsz Ting Chung, Lemao Liu, Mo Yu, Dit-Yan Yeung (HKUST; Fudan University; Wechat AI, Tencent)  
🔗 https://arxiv.org/abs/2605.13511  

你在設計 CoT 示例時，是否會考慮示例的難易度與排序？歡迎在留言區分享你的經驗 👇

#AI #InContextLearning #ChainOfThought #PromptEngineering #HKUST #Fudan #Tencent #WechatAI #LLM #推理任務
