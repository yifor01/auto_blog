---
title: "Artificial Aphasias in Lesioned Language Models"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.16222
score: 99
model: tencent/hy3-preview:free
generated_at: 2026-05-18T20:38:42.411406
---

📌 **病灶法揭示 LM 語言功能組織**  

你是否好奇，如果把語言模型的某些參數「切除」，會產生什麼樣的語言錯誤？這項研究把腦損傷導致的失語症帶入 AI 世界，發現模型的錯誤模式與人類既有相似又有根本不同。  

🤔 **從腦損傷失語症到模型參數「病灶」**  
人類失語症（Aphasia）是由特定腦區受損引發的語言選擇性障礙，能揭示語言功能的組織方式。研究團隊受此啟發，提出以「病灶」（將模型參數設為零）的方式來探測大型語言模型（LM）內部的語言處理結構，並使用臨床上的 Text Aphasia Battery (TAB) 評估所產生的症狀。  

🧪 **在五個 1B 規模模型上進行 112,426 次輸出測試**  
實驗對五個約 10 億參數的語言模型進行參數零化（lesion），共產生 112,426 個模型輸出。每個輸出都經 TAB 評分，以觀察哪些語言症狀（例如語法、語義、音韻、流暢度）會因不同參數的損害而顯現。  

🔍 **注意力與前饋網路的症狀分布差異明顯**  
結果顯示，注意力相關的組件（query、key、value、output）與前饋網路的組件（up、gate、down）在產生的症狀上呈現廣泛但分佈不同的模式。同一機制內的不同子組件之間的差異則較為不明顯。  

🧩 **網路深度影響症狀類型**  
進一步分析發現，網路的位置也很重要：較早的層（early layers）受損時，句法與語義相關的症狀出現較多；而較中到晚期的層（late‑middle layers）受損則較易導致音韻與流暢度方面的缺失。  

⚠️ **與人類失語症的相似度有限**  
雖然某些模型病灶產生的症狀分布在定量上較接近特定類型的人類失語症，但從質itative（質itative）觀點來看，模型與人類的症狀模式仍有顯著差異。這指出，失語症的表現形式很大程度上受到學習與處理細節的影響，而不僅僅是語言處理被破壞的必然結果。  

🎯 **為解釋性研究提供新視角**  
此研究提供了一種神經科學啟發的方法，可用來檢視語言模型內部功能分區的粗略圖景。雖然目前尚未直接產出可立即用於產業的工具，但對於想了解模型如何組織語言知識、以及如何從腦科啟發的角度改進解釋性研究的讀者而言，具備重要的參考價值。  

🔗 **論文連結**  
📝 Artificial Aphasias in Lesioned Language Models  
👤 Nathan Roll, Jill Kries, Laura Gwilliams, Cory Shain (Stanford University; Wu Tsai Neurosciences Institute)  
🔗 https://arxiv.org/abs/2605.16222  

你對用「病灶」來檢視模型內部結構有什麼看法？歡迎在留言區分享！  

#AI #語言模型 #解釋性研究 #神經科學 #Stanford #失語症 #機器學習
