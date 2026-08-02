---
title: 'VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization'
source: Apple ML
url: https://machinelearning.apple.com/research/videoflextok
score: 91
model: google/gemma-4-31b-it:free
generated_at: '2026-07-02T19:52:12.407988'
---

📌 【Apple 研究】VideoFlexTok：用「粗到細」的可變長度 Token 降低影片生成門檻

TL;DR：透過將影片轉化為由淺入深的變長序列，在維持品質下將模型規模縮小 5 倍，並大幅降低長影片生成成本。

目前的影片 Tokenization 習慣將影片視為一個 3D 網格（3D grid），這意味著無論影片內容簡單或複雜，後端模型都必須「逐畫素」地學習所有低階細節。這種做法導致學習複雜度極高，且在處理長影片時會面臨巨大的計算壓力。

🤔 **擺脫 3D 網格的固定成本**

傳統的 3D 網格 Tokenizer 強制要求模型處理所有局部資訊，而 Apple 提出的 VideoFlexTok 改變了這個邏輯。它將影片表示為一個「可變長度」的 Token 序列，並採用「由粗到細」（coarse-to-fine）的結構：

- 前段 Token：捕捉抽象資訊，例如語義（semantics）與動作（motion）。
- 後段 Token：逐步補足細粒度的細節。

🧩 **可靈活調整的生成流解碼器**

VideoFlexTok 搭配一個生成流解碼器（generative flow decoder），使其能根據任何 Token 數量還原出真實的影片。這種設計帶來兩個核心優勢：
1. 根據下游需求調整 Token 數量。
2. 在相同預算下，能對比基準模型編碼更長的影片。

📊 **模型規模縮小 5 倍，品質依然相當**

在類別生成（class-to-video）與文字生成影片（text-to-video）的任務評估中，VideoFlexTok 展現了極高的效率：
- **效能對比**：僅使用 1.1B 參數的模型，即可達到與 5.2B 參數模型相當的生成品質（評估指標為 gFVD 與 ViCLIP Score）。
- **長影片生成**：在生成 10 秒（81 幀）的影片時，僅需 672 個 Token，比對應的 3D 網格 Tokenizer 減少了 8 倍的 Token 數量，有效避免了昂貴的計算成本。

🎯 **實務啟示**

對於開發生成式 AI 的工程師而言，這項研究證明了「資訊分層」比「均等取樣」更有效率。如果能將語義與細節在 Token 層級就完成分離，下游模型就不需要浪費大量參數去學習低階畫素分佈，從而能在更小的模型規模下實現高品質的長影片生成。

🔗 **來源**
- 標題：VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization
- 連結：https://machinelearning.apple.com/research/videoflextok

#ComputerVision #VideoGeneration #Tokenization #AppleML #ICML #VideoFlexTok #MachineLearning #TextToVideo #EfficientAI #DeepLearning
