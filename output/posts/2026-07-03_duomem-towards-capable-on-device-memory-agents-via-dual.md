---
title: 'DuoMem: Towards Capable On-Device Memory Agents via Dual-Space Distillation'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.29961
score: 94
model: google/gemma-4-31b-it:free
generated_at: '2026-07-03T19:52:00.001753'
---

📌 DuoMem：透過雙空間蒸餾將大模型的問題解決能力轉移至裝置端

TL;DR：DuoMem 透過參數與上下文雙空間蒸餾，讓輕量化模型在維持高效能的同時，能具備 LLM 的問題解決能力。

當我們追求將 AI 部署在裝置端（On-Device）時，面臨的最大挑戰始終是「效能與記憶體佔用」的權衡。如何在不增加大量參數的前提下，讓小型模型擁有像大型語言模型（LLM）那樣的邏輯推理與問題解決能力？

🧩 **結合參數與上下文的雙空間蒸餾框架**

DuoMem 提出了一套雙空間蒸餾（Dual-Space Distillation）機制，旨在將 LLM 的程式化問題解決能力（Procedural Problem-solving）轉移到較小的學生模型中。其核心設計包含兩個維度的轉移：

1. Context-space distillation（上下文空間蒸餾）：針對輸入與中間過程的上下文資訊進行最佳化。
2. Parameter-space distillation（參數空間蒸餾）：將知識直接轉移至模型的參數權重中。

這種設計讓學生模型能以極少的額外參數成本，獲取高效能的推理能力，並顯著提升推論速度（Inference speed）。

💡 **對裝置端 AI 部署的實務意義**

對於開發端側 AI 應用的工程師來說，DuoMem 提供了一種新的模型壓縮思路：不再僅僅依賴單一的權重蒸餾，而是同時利用上下文空間與參數空間。這意味著我們可以在受限的硬體資源下，實現更靈活的記憶代理（Memory Agents），在不犧牲反應速度的情況下，提升處理複雜任務的成功率。

🎯 **實務啟示**

若你的目標是開發低延遲且具備複雜推理能力的端側模型，可以關注這種「雙空間蒸餾」的策略。與其單純追求模型縮小，將 LLM 的解題流程（Procedural knowledge）透過雙路徑轉移至小模型，可能是達成高效能端側 AI 的關鍵路徑。

🔗 **來源**
- 標題：DuoMem: Towards Capable On-Device Memory Agents via Dual-Space Distillation
- 連結：https://huggingface.co/papers/2606.29961

#AI #LLM #KnowledgeDistillation #OnDeviceAI #ModelCompression #MachineLearning #DuoMem #MemoryAgents #InferenceOptimization #DeepLearning
