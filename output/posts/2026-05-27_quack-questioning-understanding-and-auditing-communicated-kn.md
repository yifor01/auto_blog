---
title: "QUACK: Questioning, Understanding, and Auditing Communicated Knowledge in Multimodal Social Deduction Agents"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.27068
score: 88
model: tencent/hy3-preview:free
generated_at: 2026-05-27T21:25:41.288539
---

📌 **QUACK：多模態社交代理知識審計**

當 AI 代理開始在「狼人殺」等社交遊戲中說話，我們怎麼知道它們的話是真的理解還是只是複製？  
QUACK 提供了一種三層審計方法，從遊戲結果到語句一致性，逐層檢驗代理的知識 grounding。  
這套框架旨在讓研究者能夠更清楚地看到代理是否真的把語言與所感知的多模態世界連結起來。

🧩 **多模態社交推理環境填補了評估空白**  
現有的代理評估多聚焦於單一模態或純文字任務，難以觀察代理在需要同時處理視覺、語音與文字的社交情境下如何表現。QUACK 建立了一個可以同時呈現多種感官輸入的社交推理平台，讓代理的決策過程在更貼近真實互動的條件下被觀察。

🔍 **三層審計框架：從結果到語句的逐層檢驗**  
QUACK 的核心是三層結構：第一層看代理在遊戲中的最終勝負或任務完成度；第二層追蹤代理的行為軌跡，檢查其決策是否與環境變化同步；第三層則深入到 utterance‑level，比較代理說出的句子與其所觀察到的多模態內容是否在語義上一致。這樣的層層遞進，使得評估不僅停留在「是否成功」，更能釐清「成功背後的理解深度」。

⚠️ **為何 grounding 評估對對齊與安全至關重要**  
如果代理只是學會了說出令人信服的話，卻沒有真正將語言與世界狀況掛鉤，則在開放式環境中容易產生幻覺或惡意操作。通過 QUACK 提供的三層檢驗，研究者能夠更早發現代理在理解上出現的斷層，從而在對齊訓練或安全防護上有據可依。

🚧 **目前的局限與未來方向**  
摘要僅說明了環境與框架的設計，未具體報告實驗結果、參與者數量或基線比較；因此難以判斷該方法在不同模態或規模上的穩定性。若後續能公開程式碼與基準測試，將有助於社群快速驗證並擴展至更複雜的社交情境（例如談判、合規對話等）。

💡 **對研究者的實務建議**  
- 先以 QUACK 作為診斷工具，觀察自家代理在多模態社交任務中的 grounding 情況。  
- 注意三層指標之間的關聯：單看勝率可能掩蓋語句層面的不一致。  
- 若資源允許，嘗試在不同的社交推理遊戲（如隱藏身份、資訊 asymmetrical 場景）上重現該框架，以評估其普遍性。

🔗 **論文連結**  
📝 QUACK: Questioning, Understanding, and Auditing Communicated Knowledge in Multimodal Social Deduction Agents  
🔗 https://huggingface.co/papers/2605.27068  

你是否曾在測試多模態代理時感到「它說得對，但好像不太明白」？歡迎在留言區分享你的經驗與想法 👇

#AI #Multimodal #SocialDeduction #AgentEvaluation #Grounding #HuggingFace #Research #MachineLearning #Alignment #Safety
