---
title: 'Google AI Introduces TabFM: A Hybrid-Attention Tabular Foundation Model for
  Zero-Shot Classification and Regression'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/01/google-ai-introduces-tabfm-a-hybrid-attention-tabular-foundation-model-for-zero-shot-classification-and-regression/
score: 94
model: google/gemma-4-31b-it:free
generated_at: '2026-07-01T20:35:14.025631'
---

📌 【Google AI】TabFM：將表格預測轉化為 In-Context Learning 的基礎模型

TL;DR：TabFM 讓表格資料能像 LLM 一樣透過零樣本（Zero-Shot）預測，無需針對新資料集進行訓練或調參。

面對企業最常見的表格資料，資料科學家長年陷入一個迴圈：為了讓 XGBoost 或 Random Forest 達到理想效能，必須花費大量時間進行特徵工程（Feature Engineering）與超引數最佳化。

🤔 **擺脫 .fit() 的繁瑣流程**

在傳統的結構化資料處理中，每一組新資料集都需要重新訓練模型。即便使用強大的 tree-based 方法，從原始資料中提取可靠訊號的過程依然耗時且重複。Google 推出的 TabFM 旨在打破這個瓶頸，將表格預測重新定義為一個「上下文學習」（In-Context Learning, ICL）問題。

🧩 **將表格視為一個統一的 Prompt**

TabFM 的核心設計理念是將表格預測邏輯與大型語言模型（LLM）對齊。它不再為每個資料集的分佈更新引數，而是採取以下運作方式：

- **單次前向傳播**：預測結果僅需一次 forward pass 即可產出。
- **統一 Prompt 結構**：將整個資料集（包含訓練範例與目標測試行）視為一個統一的 Prompt 輸入。
- **推理時讀取關係**：模型在推理階段直接分析欄位與行之間的關係，而非依賴預訓練的權重更新。

💡 **克服二維結構的挑戰：混合注意力機制**

表格資料與文本有本質上的不同：文本是一維且有序的序列，但表格是二維且「無序」的（交換兩行或兩列的順序不會改變其含義）。為了彌補這個差異，TabFM 採用了一種混合設計，將 TabPFN 與 TabICL 兩者結合，以處理表格特有的結構特性。

📊 **定位與應用場景**

Google 將 TabFM 定位為 TimesFM（其零樣本時間序列模型）在表格領域的對應版本。其目標是處理如客戶流失分析（Customer Churn）或金融欺詐檢測（Financial Fraud Detection）等典型的企業級結構化資料任務。

⚠️ **資料獲取的限制**

作者指出，基礎模型的強大依賴於海量且多樣化的資料，然而在開源社群中，高品質的表格資料集相對稀缺，這對基礎模型的發展構成了挑戰。

🎯 **實務啟示**

對於 ML 工程師而言，TabFM 提供了一種全新的工作流可能性：如果零樣本預測能達到足夠的精準度，開發者將能省去繁瑣的特徵工程與超引數調優時間，直接將資料集輸入模型獲取結果。目前該模型已在 Hugging Face 與 GitHub 上開源，可直接嘗試整合至現有的資料管線中。

🔗 **來源**
- 標題：Google AI Introduces TabFM: A Hybrid-Attention Tabular Foundation Model for Zero-Shot Classification and Regression
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/07/01/google-ai-introduces-tabfm-a-hybrid-attention-tabular-foundation-model-for-zero-shot-classification-and-regression/

#GoogleAI #TabFM #TabularData #ZeroShot #InContextLearning #MachineLearning #FoundationModel #XGBoost #DataScience #OpenSource
