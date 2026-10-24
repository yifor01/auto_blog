---
title: 'Build Your Own Reasoning Model: A Full Video Course'
source: Sebastian Raschka
url: https://magazine.sebastianraschka.com/p/building-reasoning-models
model: claude-code/sonnet
generated_at: '2026-10-24T19:36:14.891076'
score: 97
---

📌 Sebastian Raschka 推出「從零打造推理模型」完整影片課程，11小時實作 RLVR 全流程

TL;DR：Raschka 把《Build a Reasoning Model (From Scratch)》書稿拍成 8 支教學影片，從 Qwen3 0.6B 基礎模型一路做到推理評估與強化學習。

當幾乎所有主流 LLM 都內建了「推理模式」，你是否真正理解這層能力是怎麼長出來的？Sebastian Raschka 這次沒有再寫一篇文章解釋，而是直接把整套實作過程錄成影片，讓讀者跟著程式碼從頭做一遍。

🤔 **推理模型與 Agent 是什麼關係**

Raschka 在第一支影片就先釐清一個常被問到的問題：推理模型不是 Agent 的替代品，而是 Agent 的「引擎」。他的說法是，推理模型本質上是在一般 LLM 基礎上，透過可驗證獎勵的強化學習（reinforcement learning with verifiable rewards）加上推理時擴展（inference-time scaling）技術做後訓練，讓模型更能處理高難度問題；而 Agent harness 則是外層的軟體框架，負責上下文管理與工具呼叫，把這個引擎接上更複雜的任務。他用引擎與車身的比喻，說明傳統 LLM、推理模型與 Agent harness 三者的分工。

🧩 **八支影片，從預訓練模型做到驗證器**

課程不從零訓練一個 LLM 開始（那是另一本書的範疇），而是直接載入 Qwen3 0.6B 的預訓練權重作為起點，聚焦在「評估與改進」這個更有趣的部分。素材中提到的內容包含：

- 環境設置：用 uv 安裝 Python/PyTorch 依賴、挑選硬體、檢查 CUDA 或 Apple Silicon 支援，以及用 VS Code 連遠端 GPU。
- 基礎模型實作：文字 token 化與解碼、理解 logits 與 next-token 預測、實作 greedy decoding 與串流文字生成、加入 KV cache 並搭配 torch.compile 比較不同硬體的效能。
- 評估：逐步打造一個數學答案驗證器，涵蓋答案抽取、正規化、數學等價性判斷,再用它在 MATH-500 資料集上評估基礎模型表現。這個驗證器之後還會在強化學習階段扮演提供獎勵訊號的角色。

💡 **搭配書本的學習路徑**

Raschka 建議的學習順序是：先讀書中對應章節，再跟著影片過一次程式碼，最後動手做練習題。他也提到，書的印刷版是彩色的，若想要更精簡的概念版，另有一個約 90 分鐘的 LinkedIn Learning 課程，涵蓋推理時擴展、強化學習與知識蒸餾的核心概念，但不包含完整程式實作。

🎯 **實務啟示**

對想理解推理模型內部機制而不只是調用 API 的工程師來說,這種「跟著程式碼做一遍」的學習方式比看論文更能建立直覺,尤其是 KV cache、torch.compile 與驗證器設計這些工程細節,往後在自建評估流程或 RLVR pipeline 時都能直接參考。

🔗 **來源**
- 標題：Build Your Own Reasoning Model: A Full Video Course
- 作者／機構：Sebastian Raschka
- 連結：https://magazine.sebastianraschka.com/p/building-reasoning-models

#ReasoningModels #LLM #PyTorch #Qwen3 #ReinforcementLearning #RLVR #MachineLearning #DeepLearning #AIEducation #SebastianRaschka
