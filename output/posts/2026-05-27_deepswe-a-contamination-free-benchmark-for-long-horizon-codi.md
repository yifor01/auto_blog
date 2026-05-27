---
title: "DeepSWE: A contamination-free benchmark for long-horizon coding agents"
source: Hacker News
url: https://deepswe.datacurve.ai/blog
score: 100
model: tencent/hy3-preview:free
generated_at: 2026-05-27T21:03:19.832958
---

📌 **DeepSWE：無污染的長時程編碼基準，讓前沿模型差距一目了然**

你以為現在的 SWE‑bench Pro 已經夠嚴苛？實際上它的驗證器會錯判近三分之一的答案，而且很多題目其實模型在預訓練時就見過。DeepSWE 從零設計任務，手寫驗證器，讓真正的能力差距浮現。

🤔 **基準需求：避免污染與提升真實性**  
現有的編碼基準多半改寫自既有的 commit 或 PR，導致模型在預訓練階段已經看到解答；同時，任務往往過於簡短，驗證器只檢查實作細節而非軟體行為。這使得排名難以反映實際開發中的表現，也讓前沿實驗室對基準可信度產生疑慮。

🧪 **DeepSWE 的四項核心改進**  
- **無污染**：所有任務從頭編寫，未改編自任何既有程式碼，確保模型在預訓練時未見過解答。  
- **高多樣性**：涵蓋 91 個倉儲、五種程式語言，題目類型廣泛。  
- **真實複雜度**：提示長度僅為 SWE‑bench Pro 的一半，但所需程式碼量是其 5.5 倍，輸出 token 約增加 2 倍。  
- **可靠驗證**：驗證器完全手寫，專注於軟體行為而非實作細節，減少誤判。

🔍 **與 SWE‑bench Pro 的對比**  
SWE‑bench Pro 的任務平均約 120 行程式碼，審計顯示其驗證器誤判率為 8% 假陽性、24% 假陰性。這意味著近三分之一的答案可能被錯誤評分。相比之下，DeepSWE 的設計讓模型在同一基準上的表現拉開明顯且有序的間隔，與開發者在日常使用代理時感受到的能力差距相吻合。

📊 **領先模型在 DeepSWE 的表現（部分）**  
- gpt-5.5 [xhigh] 70 % ± 4 %  
- gpt-5.4 [xhigh] 56 % ± 5 %  
- claude-opus-4.7 [max] 54 % ± 5 %  
- claude-sonnet-4.6 [high] 32 % ± 4 %  
- gemini-3.5-flash [medium] 28 % ± 4 %  
- gpt-5.4-mini [xhigh] 24 % ± 4 %  
- kimi-k2.6 24 % ± 4 %  
- mimo-v2.5-pro 19 % ± 4 %  
- glm-5.1 18 % ± 4 %  

（數據來源：DeepSWE 官部落格）

💡 **為何這個基準重要**  
DeepSWE 提供了一個更乾淨、更具區辨度的評估平台，使研究者和工程師能夠更客觀地比較不同代理的長時程軟體工程能力。其無污染特性也直接回應了業界對基準可重複性的擔憂。

⚠️ **目前已知的限制**  
- 基準仍屬新發布，長期穩定性與擴展性有待社群進一步驗證。  
- 目前公開的領先模型名單僅涵蓋部份模型，未涵蓋所有可能的候選系統。  
- 部分驗證器雖為手寫，但隨著任務複雜度提升，維護成本亦會增加。

🎯 **對開發者與研究者的啟示**  
- 在評估或選擇編碼代理時，優先考慮在無污染基準上的表現，以減少因預訓練重複導致的虛高分數。  
- 關注基準的驗證方式：手寫行為級驗證器比僅比對程式碼片段更能反映真實軟體品質。  
- 多語言、多倉儲的題目設計有助於檢驗模型的泛化能力，適合用於跨專業領域的代理測試。

🔗 **論文／專案連結**  
📝 DeepSWE: A contamination-free benchmark for long-horizon coding agents  
👤 作者：ammar_x （來自 Hacker News 發布）  
🔗 部落格與基準頁面：https://deepswe.datacurve.ai/blog  

你在使用 AI 編碼助手時，有否注意到基準分數與實際體驗的落差？歡迎在留言區分享你的觀察與經驗 👇

#AI #CodingAgent #Benchmark #DeepSWE #MachineLearning #軟體工程 #LLM #CodeGeneration
