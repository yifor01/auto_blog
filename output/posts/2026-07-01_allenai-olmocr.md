---
title: allenai/olmocr
source: GitHub Trending
url: https://github.com/allenai/olmocr
score: 120
model: google/gemma-4-31b-it:free
generated_at: '2026-07-01T20:29:59.001628'
---

📌 【AI2 開源】olmOCR：將複雜 PDF 與影像高效轉換為乾淨 Markdown 的工具集

TL;DR：基於 7B VLM 的檔案轉換工具，能處理複雜版面並將 PDF/影像轉為 Markdown，成本低於每百萬頁 200 美元。

PDF 轉文字一直是工程師的噩夢，尤其是面對多欄位、插圖、頁首頁尾或手寫內容時，傳統 OCR 往往會讓閱讀順序大亂。AI2 (Allen Institute for AI) 推出的 olmOCR 試圖透過視覺語言模型 (VLM) 解決這個痛點。

🧩 **將複雜版面轉化為自然閱讀順序**

olmOCR 是一個專為 PDF、PNG 和 JPEG 等影像格式設計的工具集，其核心目標是將這些檔案轉換為乾淨且可讀的純文字（Markdown）格式。

其技術設計重點在於處理複雜的視覺結構：
- 支援方程式、表格、手寫文字以及複雜的格式。
- 自動移除頁首 (headers) 與頁尾 (footers)。
- 即使在存在插圖、多欄位佈局 (multi-column layouts) 或內嵌圖表 (insets) 的情況下，仍能將內容轉換為自然的閱讀順序。

📊 **基於 7B VLM 的效能與成本控制**

該工具採用一個 7B 引數的 VLM 驅動，因此需要 GPU 支援。在成本方面，作者宣稱轉換每百萬頁的費用低於 200 美元。

從版本更新紀錄可看出其演進路徑：
- 推出的 olmOCR-Bench 評測分數在 v0.1.68 時為 77.4。
- v0.2.1 透過預設使用 FP8 精度，顯著提升了執行速度並減少了每份檔案的重試次數。
- v0.4.0 引入了合成資料 (synthetic data) 與 RL (強化學習) 訓練，使 olmOCR-bench 分數提升約 4 分。

💡 **開發者友好的部署與訓練支援**

為了降低工程師的部署門檻，olmOCR 在基礎設施上做了以下調整：
- 推理管線：從 sglang 切換至 vLLM，並更新 Docker 映像檔至 CUDA 12.8。
- 部署方式：提供官方 Docker 支援與映像檔。
- 自定義訓練：v0.2.0 版本清理了訓練程式碼，簡化了使用者自行訓練 olmOCR 模型的流程。

🎯 **實務啟示**

對於需要處理大量非結構化 PDF 資料以建立 RAG (檢索增強生成) 知識庫的工程師來說，olmOCR 提供的「自然閱讀順序」與「自動移除頁首頁尾」功能，能大幅減少後處理的清理工作，且 FP8 的支援讓大規模轉換的運算成本更具可行性。

🔗 **來源**
- 標題：olmocr
- 作者／機構：AI2 — allenai
- 連結：https://github.com/allenai/olmocr

#OCR #VLM #PDF #Markdown #AI2 #OpenSource #vLLM #DocumentAI #MachineLearning #RAG
