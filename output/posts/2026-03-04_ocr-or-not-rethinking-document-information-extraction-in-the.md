---
title: "OCR or Not? Rethinking Document Information Extraction in the MLLMs Era with Real-World Large-Scale Datasets"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2603.02789
score: 126
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-04T18:58:32.573180
---

# 📌 【SAP & Stanford 最新研究】OCR 還是不用 OCR？MLLM 時代的文檔資訊擷取真相

隨著 GPT-4V、Gemini、Claude 等多模態大模型問世，一個關鍵問題浮出水面：在處理文檔時，傳統的 OCR 步驟還有必要嗎？

🤔 **傳統 OCR+MLLM 架構還是最佳解嗎？**

過去幾年，文檔資訊擷取的標準做法是：先用 OCR 將圖片轉文字，再用 MLLM 理解內容。但隨著 MLLM 對圖片理解能力的提升，這個兩步驟流程是否還是最佳選擇？

🧪 **SAP 與史丹佛大學的實證研究**

這是一項由 SAP 與史丹佛大學聯合進行的實證研究，針對真實企業文檔進行大規模評測。研究團隊測試了多種現成 MLLM 模型，比較「圖片輸入」與「OCR 文字輸入」的表現差異。

 **圖片輸入 vs. OCR 文字輸入的驚人結果**

- 在多種商業文檔上，**圖片輸入的 MLLM 表現與 OCR 輸入相當甚至更優**
- 某些情況下，OCR 反而會引入額外錯誤，影響最終結果
- 這意味著對於強大的 MLLM 來說，**OCR 可能不是必要的中間步驟**

💡 **關鍵發現：設計比技術更重要**

研究顯示，影響表現的關鍵因素不是是否使用 OCR，而是：

- **精心設計的 schema**（資料結構規範）
- **提供具體的 exemplars**（範例說明）
- **清晰的 instructions**（操作指示）

這些設計元素對 MLLM 表現的影響，可能比技術架構本身還大。

⚠️ **錯誤分析框架揭示隱藏問題**

為了深入理解失敗模式，研究團隊開發了一套自動化分層錯誤分析框架，利用 LLM 系統性診斷錯誤類型。這讓我們看到：

- 某些 OCR 錯誤實際上是「偽問題」，對 MLLM 理解沒有影響
- 圖片輸入可以保留原始空間資訊，有時比文字更有利
- 不同 MLLM 模型對不同文檔類型的偏好差異

🎯 **對開發者的實務啟示**

- **簡化架構**：如果使用強大 MLLM，可考慮直接圖片輸入
- **重視設計**：投入時間優化 schema 和說明，效果可能超過技術選擇
- **錯誤分析**：建立系統性錯誤診斷流程，才能持續改進

🔗 **論文連結**
📝 OCR or Not? Rethinking Document Information Extraction in the MLLMs Era with Real-World Large-Scale Datasets
👤 Jiyuan Shen, Peiyue Yuan, Atin Ghosh, Yifan Mai, Daniel Dahlmeier
🏢 SAP; Stanford University
🔗 論文：arxiv.org/abs/2603.02789

你現在的文檔處理流程是什麼？有考慮過跳過 OCR 嗎？歡迎分享你的經驗 👇

#AI #MLLM #OCR #文檔處理 #資訊擷取 #SAP #Stanford #機器學習 #多模態模型
