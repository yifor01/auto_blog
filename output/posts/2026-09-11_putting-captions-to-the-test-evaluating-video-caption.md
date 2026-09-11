---
title: 'Putting Captions to the Test: Evaluating Video Caption Quality through Multiple-Choice
  Question Answering'
source: Apple ML
url: https://machinelearning.apple.com/research/video-caption-quality
model: claude-code/sonnet
generated_at: '2026-09-11T19:53:51.551855'
score: 80
---

📌 Apple 提出 CapQuiz：用選擇題來評分影片字幕好壞

TL;DR：Apple 研究團隊發表 reference-free 的影片字幕評測基準 CapQuiz，改用人類驗證的選擇題來衡量字幕品質。

一段影片可以有無數種「正確」的描述方式，那麼該怎麼給一句字幕打分數？Apple 這篇被 ACL 收錄的論文認為，答案不該是「跟標準答案的文字有多像」，而是「這句字幕能不能讓你答對關於這段影片的問題」。

🤔 **「一對多」問題：好字幕也可能被扣分**

評估影片字幕（video captioning）品質，一直是 Visual Large Language Models（VLLMs）研究中的難題。現有指標大多仰賴「生成文字對照標準參考答案」的比對方式，但影片描述天生具有「一對多」的特性：同一段影片可以有多種同樣正確的描述角度。這種比對方式容易讓高品質但用詞不同、或聚焦視覺重點不同的字幕被誤判為低分。此外，這類評估通常是單一維度的分數，無法細緻拆解字幕到底哪裡好、哪裡不好。

🧩 **CapQuiz：把字幕品質重新定義為「資訊保真度」**

論文團隊將字幕品質重新定義為資訊保真度（information fidelity）：一句好字幕，應該在確保嚴格事實正確（factuality）的前提下，盡可能涵蓋影片中的重要視覺資訊（coverage）。

CapQuiz 是一個 reference-free（不依賴標準參考答案）的基準，做法是根據影片內容，評估這句字幕能否用來回答人類驗證過的細粒度選擇題。具體設計包含：

- 一套涵蓋 10 種問題類型的階層式分類體系，分為描述性（Descriptive）與推論性（Inferential）兩大類。
- 涵蓋 24 個不同影片領域，確保評測涵蓋面夠廣。

在這個基礎上，研究團隊進一步提出 CapF1，一個綜合指標，由兩個子指標合成：CapP 衡量字幕的事實正確性，CapR 衡量字幕對影片資訊的覆蓋程度。

📊 **與人類判斷的相關性更高**

論文指出，大量實驗顯示 CapQuiz 與人類評判的相關性顯著優於既有指標，並且能提供可解釋、細粒度的模型表現分析，而不只是一個籠統的分數。

🎯 **實務啟示**

如果你的團隊正在訓練或評估影片字幕／影片理解模型，傳統的文字比對式指標（例如依賴標準參考答案的 n-gram 匹配）可能會系統性地低估某些其實描述精準、只是措辭不同的輸出。CapQuiz 提供的「用選擇題檢驗資訊覆蓋與事實正確」思路，值得在建立內部評測集時參考，尤其適合用來定位模型在哪一類問題（描述性 vs. 推論性）上表現較弱。

🔗 **來源**
- 標題：Putting Captions to the Test: Evaluating Video Caption Quality through Multiple-Choice Question Answering
- 作者／機構：Zizhen Wang, Bo Feng, Zhengfeng Lai, Shiyu Li, Yang Lu, Meng Cao, Ping Huang, Simon Wang（Apple ML，ACL 2026）
- 連結：https://machinelearning.apple.com/research/video-caption-quality

#AppleML #VideoCaptioning #VLLM #ComputerVision #Benchmark #ACL2026 #MultimodalAI #EvaluationMetrics #NLP #ModelEvaluation
