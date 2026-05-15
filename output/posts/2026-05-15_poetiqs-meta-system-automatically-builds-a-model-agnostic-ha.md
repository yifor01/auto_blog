---
title: "Poetiq’s Meta-System Automatically Builds a Model-Agnostic Harness That Improved Every LLM Tested on LiveCodeBench Pro Without Fine-Tuning"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/14/poetiqs-meta-system-automatically-builds-a-model-agnostic-harness-that-improved-every-llm-tested-on-livecodebench-pro-without-fine-tuning/
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:40:26.227440
---

📌 Poetiq 的模型無關 harness 提升 LiveCodeBench Pro 分數，無需 fine‑tuning  

你以為只有重新訓練模型才能讓 AI 寫 Code 變得更強？事實上，Poetiq 的 Meta-System 只改變推論方式，就讓多個 LLM 在 LiveCodeBench Pro 上皆出現顯著提升。  

🤔 **LiveCodeBench Pro 為何與眾不同**  
LiveCodeBench Pro (LCB Pro) 取材自主要競賽程式題目，且不公開標準答案，僅透過完整測試框架驗證輸出是否符合正確答案、記憶體與執行時間限制。基準會持續更新，避免資料洩漏與過度適配，特別聚焦 C++ 的創意編程與高效程序邏輯，與評估工具使用或除錯的 SWEBench 有本質區別。  

🧪 **Poetiq Meta‑System 的運作方式**  
研究團隊設計了一個模型無關的推論 harness，該系統會自動為目標 LLM 建構並優化推論流程，不需要存取模型內部參數或進行任何 fine‑tuning。harness 在 Gemini 3.1 Pro 上進行調優，但設計上可直接套用於其他模型。  

🚀 **核心發現：各模型分數皆上揚**  
- GPT‑5.5 High：基線 89.6% → 使用 harness 後 93.9%（+4.3%）  
- Gemini 3.1 Pro：基線 78.6% → 使用 harness 後 90.9%（+12.3%），此分數甚至超過 Google 自家的 Gemini 3 Deep Think（88.8%），後者無法透過 API 取得外部驗證。  
所有測試過的 LLM 在 LCB Pro 上均出現提升，顯示該 harness 具備廣泛的適用性。  

💡 **為何 harness 能帶來提升**  
透過自動搜尋與組合最適合的推論設定（例如取樣溫度、token 限制、後處理規則），harness 能在不改變模型權重的情況下，讓模型產出更符合 LCB Pro 所需的正確輸出與資源限制。這意味著效能提升來自於更好的推論策略，而非模型知識的增加。  

⚠️ **研究限制**  
- harness 的最佳化目前是以 Gemini 3.1 Pro 為目標進行，其他模型的最終表現仍需實際驗證。  
- 實驗僅在 LiveCodeBench Pro 基準上進行，未涵蓋其他類型的程式設計或軟體工程任務。  
- 未詳細說明 harness 在較長時間或不同硬體環境下的穩定性。  

🎯 **對工程師的實務啟示**  
- 若目標是提升特定程式設計基準的分數，先考慮優化推論 harness，而非立即投入昂貴的 fine‑tuning。  
- 該方法提供一種「即插即用」的途徑，可快速在現有 API 上獲得效能提升，特別適合於無法取得模型權重或希望保持模型原始狀況的場景。  
- 團隊指出，未來可進一步探索 harness 與檢索增強或工具使用的結合，以擴展至更廣的程式設計工作流。  

🔗 **參考資訊**  
📝 Poetiq’s Meta-System Automatically Builds a Model‑Agnostic Harness That Improved Every LLM Tested on LiveCodeBench Pro Without Fine‑Tuning  
👤 Asif Razzaq (MarkTechPost 報導)  
🔗 https://www.marktechpost.com/2026/05/14/poetiqs-meta-system-automatically-builds-a-model-agnostic-harness-that-improves-every-llm-tested-on-livecodebench-pro-without-fine-tuning/  

你是否曾嘗試過只改變提示或取樣方式就顯著提升 Code 模型的表現？歡迎在留言區分享你的經驗與想法 👇  

#AI #LLM #CodeGeneration #LiveCodeBench #Poetiq #MachineLearning #軟體工程 #推論優化
