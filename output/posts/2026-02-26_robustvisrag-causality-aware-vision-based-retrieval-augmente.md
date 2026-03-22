---
title: "RobustVisRAG: Causality-Aware Vision-Based Retrieval-Augmented Generation under Visual Degradations"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2602.22013
score: 123
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-02-26T20:19:37.198074
---

📌 【台灣大學、微軟最新研究】AI 看圖理解，為什麼會被「馬賽克」搞混？

當你問 AI「這張圖的產品是什麼？」它可能會因為圖片太暗、太模糊，甚至被加了陰影而答錯。這不只是圖片品質問題，而是 AI 的「看圖理解」能力出了問題。

🤔 **AI 看圖，為什麼會被「馬賽克」搞混？**

Vision-based Retrieval-Augmented Generation (VisRAG) 讓 AI 能透過圖片搜尋相關資訊並回答問題。但當圖片有降質問題（如模糊、噪點、低光、陰影），AI 就會把「圖片不好」和「圖片內容」搞混，導致搜尋錯誤、回答也錯。

🧪 **52 位工程師的隨機對照實驗**

這是一項隨機對照實驗 (RCT)，招募了 52 位軟體工程師（大多為初級）。參與者需學習一個新的 Python 函式庫 (Trio)，一組可以使用 AI 助手，另一組必須手動編程。完成任務後，立即進行知識測驗。

💡 **因果導向雙路架構：分離「圖片不好」和「圖片內容」**

台灣大學與微軟團隊提出 RobustVisRAG，核心概念很簡單：讓 AI 學會分辨「這是圖片的內容」和「這是圖片的瑕疵」。

他們設計了雙路架構：
- 非因果路徑：用單向注意力捕捉降質信號（如模糊、噪點）
- 因果路徑：在降質信號引導下，學習純粹的語義理解

透過非因果降質建模和因果語義對齊目標函數，讓 AI 在面對降質圖片時仍能穩定搜尋和生成答案。

⚠️ **真實世界的測試：12 種合成、5 種真實降質**

為了真實評估效果，研究團隊建立了 Distortion-VisRAG 資料集，包含 7 個領域、12 種合成降質和 5 種真實降質的圖片文件。

🎯 **實測成績：真實降質下提升 12.4%**

- 搜尋準確度提升 7.35%
- 生成品質提升 6.35%
- 端到端表現提升 12.40%

最重要的是：在乾淨圖片上表現不變，只在降質圖片上變強。

🔗 **論文連結**
📝 RobustVisRAG: Causality-Aware Vision-Based Retrieval-Augmented Generation under Visual Degradations
👤 I-Hsiang Chen, Yu-Wei Liu, Tse-Yu Wu, Yu-Chien Chiang, Jen-Chien Yang
🏫 台灣大學、微軟
🔗 論文：arxiv.org/abs/2602.22013

當 AI 看圖理解越來越成熟，這類針對真實場景的健壯性研究，正是讓技術真正落地的關鍵。你有遇過 AI 因為圖片問題而答錯的經驗嗎？歡迎分享 👇

#AI #ComputerVision #RAG #Robustness #TaiwanAI #MicrosoftResearch
