---
title: 'S-Agent: Spatial Tool-Use Elicits Reasoning for Spatial Intelligence'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.20515
score: 93
model: google/gemma-4-31b-it:free
generated_at: '2026-06-21T19:48:22.627836'
---

📌 S-Agent：透過空間工具呼叫，賦予視覺語言模型 3D 空間推理能力

TL;DR：S-Agent 框架結合時間記憶與階層式空間工具，讓 VLM 能從多視角影像中持續理解 3D 世界。

視覺語言模型（VLM）在處理單張影像時表現優異，但面對需要連續空間感知、跨視角整合的 3D 世界時，往往缺乏深度的空間推理能力。

🤔 **從多視角影像中重建 3D 空間理解**

為了克服 VLM 在空間感知上的不足，S-Agent 提出了一套空間推理框架。其核心目標是讓模型不再僅僅是「看到」影像，而是能透過一套機制，將多視角的影像資訊轉化為對 3D 世界的持續理解。

🧩 **結合時間記憶與階層式工具的設計**

S-Agent 的技術路徑主要由兩個關鍵組成：
- **時間記憶（Temporal Memory）**：讓模型能夠在連續的觀察過程中保留資訊，而非僅處理單一幀影像。
- **階層式空間工具（Hierarchical Spatial Tools）**：透過呼叫特定的空間工具，引導模型進行更精準的空間推理，將視覺資訊轉化為對 3D 環境的認知。

🎯 **實務啟示**

這項研究顯示，提升 VLM 的空間智慧不能僅靠增加引數，而應透過「外部工具呼叫」與「記憶機制」的結合。對於開發 3D 環境感知 AI 或機器人導航系統的工程師來說，這種「工具化推理」的設計方向，提供了一種將 2D 視覺資訊有效對映到 3D 空間的新思路。

🔗 **來源**
- 標題：S-Agent: Spatial Tool-Use Elicits Reasoning for Spatial Intelligence
- 連結：https://huggingface.co/papers/2606.20515

#AI #VLM #SpatialIntelligence #SpatialReasoning #3DUnderstanding #ComputerVision #MultiViewImagery #Agent #MachineLearning #S-Agent
