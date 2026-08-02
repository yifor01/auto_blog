---
title: 'UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable
  Risk Understanding in Autonomous Driving'
source: arXiv
url: http://arxiv.org/abs/2606.24759v1
score: 85
model: google/gemma-4-31b-it:free
generated_at: '2026-06-24T20:11:16.794237'
---

📌 【arXiv】UniDrive：結合時序推理與高解析度感知，提升自動駕駛的風險可解釋性

TL;DR：UniDrive 透過雙分支架構解決時序推理與空間精準度的權衡，提升自動駕駛對小目標的定位與風險描述能力。

在自動駕駛的場景理解中，目前的多模態大語言模型 (MLLM) 面臨一個核心矛盾：若追求時序推理（Temporal Reasoning），往往得犧牲解析度；若追求空間精準度，則容易遺漏遠處或被遮擋的動態危險。

🤔 **時序推理與空間精準度的權衡困境**

目前的自動駕駛模型通常在兩個方向中二選一：
- 單幀或低解析度輸入：容易漏掉微小、遠處或部分遮擋的潛在危險。
- 以語言為中心的模型：雖然能提供解釋，但缺乏明確的空間證據（Grounded Evidence）來支援其判斷。

🧩 **UniDrive 的雙分支融合架構**

為了打破上述限制，UniDrive 提出了一個統一的視覺語言與定位框架，其核心設計如下：

1. **時序推理分支 (Temporal Reasoning Branch)**：處理多幀視覺輸入，用以建模場景的動態變化。
2. **高解析度感知分支 (High-resolution Perception Branch)**：保留最新一幀的細粒度空間細節，確保感知精準度。
3. **門控交叉注意力融合模組 (Gated Cross-attention Fusion Module)**：將上述兩個分支的表徵進行整合，使動態上下文能與精確的空間證據對齊。

最終，UniDrive 基於融合後的表徵，同步生成兩項輸出：
- **自然語言描述**：對風險情況進行文字說明。
- **定位邊框 (Bounding-box)**：將風險物件精確標記在畫面中。

📊 **在 DRAMA-Reasoning 基準測試中領先**

根據作者在 DRAMA-Reasoning 測試集上的實驗結果，UniDrive 的表現優於現有的影像（Image-based）與影片（Video-based）基準模型：

- **綜合效能**：在驗證集（Validation split）上取得了最佳的整體表現。
- **關鍵優勢**：在「小目標定位」表現顯著，並在 NuScenes 與 BDD100K 資料集上展現出強大的零樣本泛化 (Zero-shot Generalization) 能力。
- **主觀評估**：在人類評分的「可解釋性」與「可信度」方面具有明顯優勢。

🎯 **實務啟示**

對於開發自動駕駛感知系統的工程師而言，這項研究證明了「時序語義」與「高解析度感知」不應是二選一的關係。透過門控融合機制將動態趨勢與精細空間資訊結合，能有效提升模型對邊緣案例（如遠處小目標）的捕捉能力，這對於提升系統的安全性與可解釋性至關重要。

🔗 **來源**
- 標題：UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving
- 作者／機構：Xiaowei Gao, Pengxiang Li, Yitai Cheng, Ruihan Xu, James Haworth
- 連結：http://arxiv.org/abs/2606.24759v1

#AutonomousDriving #MLLM #ComputerVision #TemporalReasoning #ObjectGrounding #Interpretability #NuScenes #BDD100K #RiskUnderstanding #DeepLearning
