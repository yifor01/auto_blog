---
title: "BERAG: Bayesian Ensemble Retrieval-Augmented Generation for Knowledge-based Visual Question Answering"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.22678
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-04-27T20:17:13.626021
---

📌 【劍橋大學研究】用貝氏集成解決 RAG 的 Lost-in-the-Middle 痛點

你以為把文件全部塞進 Context 就解決了檢索問題？在處理包含視覺資訊的長文問答時，這種「串接式 RAG」正讓模型陷入「視而不見」的困境，且運算成本正以平方級飆升。

🤔 **傳統 RAG 的擴展瓶頸與視覺理解障礙**

檢索增強生成（RAG）的常見做法是將多份文件拼接成單一長上下文。這在文本處理中已顯吃力，一旦涉及視覺問答（VQA），包含圖像的長上下文會讓計算成本呈現二次方增長。更嚴重的是，這導致了「Lost-in-the-Middle」效應，即模型無法有效利用位於上下文中段的重要資訊，且難以追溯答案的具體來源。

🧪 **貝氏集成與 Token 級動態加權**

來自 University of Cambridge 的研究團隊提出 BERAG（Bayesian Ensemble RAG）。不同於傳統串接，BERAG 讓語言模型分別基於單一檢索文件進行條件生成，並利用貝氏法則（Bayes' rule）在生成每個 Token 時動態更新文件的後驗機率（Posterior Probabilities）。

這種方法將後驗機率作為集成權重，實現了平行記憶使用與清晰的文件歸因（Attribution）。

 **顯著緩解 Lost-in-the-Middle，提升多模態推理**

論文主要在知識型視覺問答（Knowledge-based VQA）任務上進行驗證。結果顯示，BERAG 在 Document VQA 和多模態「大海撈針」（Needle-in-a-Haystack）基準測試中均取得顯著提升。這證明了該框架能有效處理長且帶有雜訊的檢索列表，並解決了資訊被遺漏的問題。

💡 **從歸因到防禦，構建更可靠的生成機制**

BERAG 的創新不僅在於效能。透過文件後驗機率，系統能偵測「接地不足」（Insufficient Grounding）的情況並觸發偏轉（Deflection，即拒答或澄清），提升系統可靠性。同時，透過文件剪枝（Document Pruning），其解碼速度甚至比標準 RAG 更快。

⚠️ **主要驗證集中於特定 VQA 場景**

目前評估重點在於知識型視覺問答，雖然框架具通用性，但在純文本或極端長度的通用場景下的表現仍需進一步觀察。此外，引入貝氏更新機制增加了系統的複雜度，需權衡計算資源與準確率的取捨。

🎯 **重新思考 RAG 的資訊整合方式**

對於開發多模態應用的工程師來說，BERAG 提供了一個強大的替代方案。當你的應用面臨複雜的文件推理或視覺資料處理時，考慮將「串接」轉變為「機率集成」，或許能突破現有的效能天花板。

🔗 **論文連結**
📝 BERAG: Bayesian Ensemble Retrieval-Augmented Generation for Knowledge-based Visual Question Answering
👤 Jinghong Chen, Jingbiao Mei, Guangyu Yang, Bill Byrne @ University of Cambridge
🔗 https://arxiv.org/abs/2604.22678

你目前在 RAG 專案中，最常被哪種「資訊遺漏」問題困擾？歡迎留言討論 👇

#AI #RAG #MultimodalAI #VisualQuestionAnswering #MachineLearning #Cambridge #DeepLearning
