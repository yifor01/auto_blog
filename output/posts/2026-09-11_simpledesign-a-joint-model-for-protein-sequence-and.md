---
title: 'SimpleDesign: A Joint Model for Protein Sequence and Structure Codesign'
source: Apple ML
url: https://machinelearning.apple.com/research/simpledesign-protein-codesign
model: claude-code/sonnet
generated_at: '2026-09-11T19:57:55.659783'
score: 68
---

📌 【Apple ML 研究】蛋白質設計真的需要兩階段訓練嗎？

TL;DR：Apple 提出 SimpleDesign，用單階段端對端目標同時生成蛋白質序列與結構，挑戰主流的兩階段訓練框架。

蛋白質的功能，取決於胺基酸序列與三維結構之間複雜的交互作用。想要打造能理解這種跨模態關係的生成模型，對藥物開發與蛋白質工程至關重要——但現行做法真的有必要那麼複雜嗎？Apple ML 團隊在這篇發表於 TMLR（Transactions on Machine Learning Research）的論文中給出了否定的答案。

🤔 **核心問題：兩階段訓練是必要的嗎**

論文指出，現有的蛋白質序列與結構 co-design（聯合設計）模型通常依賴多階段訓練流程：第一階段先訓練 autoencoder，把資料 tokenize 成 latent representation；第二階段再基於這個 latent 空間訓練生成模型。作者團隊提出假設：這種多階段訓練並非取得高效能 co-design 模型的必要條件，並以此為出發點設計了 SimpleDesign，一個直接在原始資料空間（data space）中訓練的多模態蛋白質設計模型。

🧩 **架構設計：模態各自處理，但共享全域注意力**

SimpleDesign 採用單階段端對端目標，同時結合兩種損失：針對序列部分使用離散的 cross-entropy，針對結構部分則採用 regression 目標。為了有效處理序列與結構這兩種本質不同的模態，團隊以 Transformer 為基礎打造多模態骨幹網路，讓模型能對兩種模態分別做 modality-specific（模態專屬）的處理，同時仍保留橫跨兩種模態的全域 self-attention。

📊 **訓練規模與成果**

論文提到，SimpleDesign 在超過 200 萬筆序列—結構配對資料上進行訓練，並在 co-design 與 unconditional（無條件）序列／結構生成的基準測試中取得「competitive performance」（具競爭力的表現）。摘要未提供具體的評估指標數字或與哪些 baseline 相比，因此無法在此進一步展開比較細節。

💡 **延續 SimpleFold 的簡化哲學**

這篇研究與 Apple 團隊此前發表的 SimpleFold（探討是否真的需要把領域專業知識刻進架構設計才能做出高效能蛋白質折疊模型）呼應，延續了同一條研究路線：質疑生成建模領域中行之有年的「兩階段」慣例，嘗試以更簡潔的端對端方案取而代之。

⚠️ **侷限**

論文摘要未提及具體的效能數字、失敗案例或作者自陳的侷限，這部分留待原文細讀。

🎯 **實務啟示**

對做多模態生成模型的工程師而言，SimpleDesign 提供的思路值得參考：與其預設「必須先做表徵學習、再做生成建模」的兩階段管線，不如先問一句「這個多階段設計，真的是效能的必要條件，還是工程慣性？」當不同模態的資料型態差異明顯（如離散序列 vs. 連續結構）時，用共享 backbone 搭配 modality-specific 處理層，或許是比另外訓練 autoencoder 更省事的起點。

🔗 **來源**
- 標題：SimpleDesign: A Joint Model for Protein Sequence and Structure Codesign
- 作者／機構：Jiarui Lu, Yuyang Wang, Yizhe Zhang, Jiatao Gu, Navdeep Jaitly, Joshua M. Susskind, Miguel Ángel Bautista（Apple）
- 連結：https://machinelearning.apple.com/research/simpledesign-protein-codesign

#ProteinDesign #GenerativeAI #Transformer #ProteinEngineering #DrugDiscovery #MachineLearning #AppleML #MultimodalLearning #StructureGeneration #TMLR
