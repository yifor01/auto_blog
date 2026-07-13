---
title: Scalable Visual Pretraining for Language Intelligence
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.09657
score: 83
model: google/gemma-4-31b-it:free
generated_at: '2026-07-13T09:05:20.183733'
---

📌 挑戰純文字預訓練：將視覺檔案直接轉化為語言智慧的 scalable 路徑

TL;DR：研究證明直接對視覺檔案進行預訓練，效能優於將其轉為純文字後的預訓練。

目前的基礎模型進步主要依賴大規模文字語料庫的預訓練，但這產生了一個核心矛盾：許多關鍵知識（如圖表、排版公式、頁面佈局）是以視覺形式呈現的，而目前的主流做法是將這些視覺豐富的來源「去視覺化」，將其轉換為純文字後再進行學習。

🤔 **純文字預訓練遺失了關鍵知識**

當我們將檔案或網頁轉換為 plain text 時，實際上捨棄了大量視覺線索。這些視覺表示（visual representations）攜帶的資訊量，是單純的文字提取無法完整或忠實捕捉的，這限制了語言智慧的發展上限。

🧩 **視覺預訓練（Visual Pretraining）的新範式**

本研究挑戰了「語言模型必須在純文字表示上訓練」的預設假設，提出一種非監督式的視覺預訓練範式：

- 直接利用視覺檔案（visual documents）進行學習。
- 過程中完全不進行文字提取（without text extraction）。
- 將視覺預訓練視為一種可擴充套件（scalable）的學習方式，用以提升基礎模型的智慧。

📊 **視覺學習在多項基準測試中表現更佳**

研究團隊在多種模型骨幹（backbones）與基準測試（benchmarks）上進行系統性研究。結果顯示，在使用相同底層語料庫的情況下，視覺預訓練的表現一致優於純文字預訓練，證明瞭這是一條更高效的語言智慧擴充套件路徑。

🎯 **實務啟示**

對於開發基礎模型的工程師而言，這項研究提示我們：提升模型能力的關鍵可能不在於更強的文字提取演算法，而是在於讓模型直接「看」原始檔案。未來在處理包含複雜排版或圖表的資料集時，直接採用視覺預訓練而非先轉成文字，可能會獲得更好的效能。

🔗 **來源**
- 標題：Scalable Visual Pretraining for Language Intelligence
- 連結：https://huggingface.co/papers/2607.09657

#VisualPretraining #FoundationModels #LanguageIntelligence #Multimodal #MachineLearning #DeepLearning #LLM #VisualDocuments #Pretraining #AI
