---
title: "Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2603.03205
score: 131
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-04T18:56:39.629480
---

📌 【微軟最新研究】AI 代理安全大突破！MOSAIC 讓 AI 懂得「該做不該做」

隨著 AI 代理越來越多地自主執行任務，從自動化測試到文件處理，一個關鍵問題浮出水面：當 AI 可以自己打開文件、執行程式、甚至輸入密碼時，如何確保它不會誤入歧途？

🤔 **Agent 與 Chatbot 的安全差異**

你可能想說：「GPT 不是已經很安全了嗎？」但這裡有個關鍵差異：Agentic 模型不只是回答問題，它們會**規劃行動、呼叫工具、執行長期任務**。一個錯誤的工具呼叫，例如存取敏感文件或輸入憑證，就可能造成不可逆的傷害。

🧪 **MOSAIC 的創新設計**

微軟研究員提出 MOSAIC（Modeling Safety in Agentic Inference Cycles），一個後續訓練框架，讓代理模型在執行多步驟工具使用時保持安全。

MOSAIC 的核心創新在於將推理過程結構化為**「規劃 → 檢查 → 執行或拒絕」**的迴圈，並將安全判斷和拒絕作為一級行動。這意味著 AI 不只是盲目執行，而是在每一步都會問自己：「我該做這個嗎？」

💡 **如何訓練一個懂得拒絕的 AI**

最困難的是：如何訓練 AI 知道什麼時候該拒絕，而不只是完成任務？MOSAIC 使用基於偏好的強化學習，透過成對的路徑比較來捕捉安全性的細微差異，這是傳統標量獎勵常常忽略的。

🎯 **實驗結果：安全與效能的平衡**

MOSAIC 在三種模型上進行零樣本評估（不需要特定任務的微調）：

- **安全性提升**：有害行為減少高達 50%
- **拒絕率提高**：在注入攻擊中，有害任務的拒絕率提高超過 20%
- **隱私保護**：減少跨領域的隱私洩漏
- **效能不降反升**：在良性任務上的表現保持或提升

 **為什麼這很重要**

這不只是學術研究。隨著 AI 代理越來越多地自主執行任務，從自動化測試到文件處理，確保它們在行動前「三思」變得至關重要。MOSAIC 展示了一種實現這一目標的方法，而不犧牲效能。

⚠️ **研究限制**

目前 MOSAIC 仍處於研究階段，主要在受控環境中評估。現實世界中的工具互動可能更複雜，長期行為也尚未完全驗證。

🎯 **實務啟示**

對於開發 AI 代理的團隊：

- 安全不應該是事後才考慮的問題
- 讓 AI 理解「為什麼拒絕」與「如何執行」同樣重要
- 偏好學習可能是處理複雜安全決策的有效方法

🔗 **論文連結**
📝 Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use
👤 Aradhye Agarwal, Gurdit Siyan, Yash Pandya, Joykirat Singh, Akshay Nambi @ Microsoft Research
🔗 論文：arxiv.org/abs/2603.03205

AI 代理的時代已經到來，你認為安全與自主之間的最佳平衡點在哪裡？歡迎分享你的看法 👇

#AI安全 #AgenticAI #機器學習 #微軟研究 #工具使用 #人工智慧倫理
