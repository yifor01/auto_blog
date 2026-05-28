---
title: "Advancing Creative Physical Intelligence in Large Multimodal Models"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.26396
score: 89
model: tencent/hy3-preview:free
generated_at: 2026-05-28T21:31:48.054510
---

📌 **視覺對齊提升創意推理**

你有沒有想過，讓 AI 看圖解難題時，總是愛編故事？這篇研究指出，只要訓練時讓模型更看重「看見的事實」，創意問題解決能力就能顯著提升。

🤔 **多模態模型在視覺複雜環境中易產生幻覺**  
當前的大型多模態模型在面對雜亂圖像或需要動手操作的任務時，常依賴內部知識生成合理但不正確的解釋，這會阻礙它們在真實世界中進行創意的肢體推理。

🧪 **以可行動性為基礎的對齊訓練**  
研究提出一種 affordance‑grounded 對齊方法：在訓練過程中，模型被引導優先參考圖像中可見的線索，而非依賴可能的幻覺內容。這種對齊方式把模型的輸出與實際可觀察的視覺證據更緊密地結合起來。

 **在視覺複雜任務中創意表現變好**  
採用 affordance‑grounded 對齊後，模型在需要創意解決問題的視覺情境下，表現出更正確且具備實用性的推論結果。也就是說，當模型被迫「看見才說」，它的創意肢體智慧會隨之提升。

💡 **視覺證據優先減少幻覺，促進真實理解**  
透過將訓練目標放在「什麼是真的看見」而非「什麼是合理猜測」，模型學會將語言輸出錨定在可驗證的視覺事實上。這不只降低了幻覺的發生率，也迫使模型在推理過程中進行更深入的視覺分析，從而在需要靈活應變的場景中展現出更佳的創意表現。

⚠️ **程式碼與實作細節未公開，僅提供概念框架**  
論文主要闡述了對齊的理念與動機，但未釋放完整的實作程式碼或詳細的超參數設定。這意味著想要直接複製或在產品中應用的開發者，仍需自行探索具體的訓練細節與資料準備流程。

🎯 **對具身 AI 與機器人實務的啟發**  
對於從事具身視覺語言模型、機器人規劃或增強現實互動的工程師而言，這個研究提醒我們：在提升模型創意之前，先確保它的輸出有堅實的視覺根據。未來可嘗試在現有的多模態預訓練流程中加入類似的 affordance‑grounded 約束，觀察是否能在真實的視覺運動任務中減少錯誤並提升適應性。

🔗 **論文連結**  
📝 Advancing Creative Physical Intelligence in Large Multimodal Models  
🔗 https://huggingface.co/papers/2605.26396  

你在開發多模態系統時，有否嘗試過讓模型「只信自己看見的」？歡迎在留言區分享你的經驗與想法 👇  

#AI #Multimodal #AffordanceGrounded #EmbodiedAI #CreativeReasoning #HuggingFace #ML #Robotics
