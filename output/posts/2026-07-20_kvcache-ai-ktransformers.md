---
title: kvcache-ai/ktransformers
source: GitHub Trending
url: https://github.com/kvcache-ai/ktransformers
score: 104
model: tencent/hy3:free
generated_at: '2026-07-20T08:48:41.981864'
---

📌 【kvcache-ai 開源】KTransformers：用 CPU-GPU 異質運算跑 LLM 推理與微調

TL;DR：KTransformers 透過 CPU-GPU 異質計算，讓消費級硬體也能體驗前沿 LLM 推理與 SFT。

在 GPU 記憶體永遠不夠用的年代，要把最新大型語言模型塞進個人電腦，往往得在量化與效能間反覆妥協。kvcache-ai 的 KTransformers 直接把 CPU 也拉進運算陣容，走一條異質計算的路。

🤔 **專為 CPU-GPU 異質計算設計的研究專案**

KTransformers 是一個聚焦於大型語言模型高效推理與 fine-tuning 的研究專案，核心手段是 CPU-GPU heterogeneous computing（異質運算）。README 指出，專案從 kt-kernel 原始碼樹中對外開放兩項使用者功能：Inference（推理）與 SFT（監督式微調）。

🧩 **對外暴露推理與 SFT 兩大能力**

框架目前明確提供兩個面向的入口：
- Inference：在 kt-kernel 下進行模型推理，並有獨立的 Quick Start 檔案。
- SFT：同樣從 kt-kernel 提供，配有專屬快速上手路徑，與推理分開管理。

📊 **近期模型支援與功能更新時間軸**

從更新紀錄來看，專案保持頻繁的 Day0 支援節奏，並持續擴充套件硬體與精度支援：
- 2026/06/21：MiniMax-M3 Day0 支援
- 2026/06/17：GLM-5.2 Day0 支援
- 2026/05/02：DeepSeek-V4-Flash 支援
- 2026/03/26：KT-Kernel 推理支援 AVX2-only CPU backend
- 2026/01/22：支援 CPU-GPU Expert Scheduling、Native BF16 與 FP8 per channel 精度、AutoDL 統一微調與推理
- 2025/12/22：透過 LLaMA-Factory 支援 RL-DPO fine-tuning

此外，2026/05/06 專案將於 GOSIM Paris 2026 的「Agentic AI on Edge」軌道，展示在消費級硬體上的推理效能。

🎯 **邊緣與消費級硬體的實務價值**

對資源有限的工程師而言，KTransformers 把最新模型（如 GLM-5.2、MiniMax-M3）的推理與微調門檻往下降：利用既有 CPU 協同 GPU 分攤負載，並提供 AVX2-only 後端，意味著不一定需要最新指令集的 CPU 也能介入運算。想跟進前沿模型但又只有消費級裝置的團隊，可優先從其 Inference / SFT Quick Start 入手試跑。

🔗 **來源**
- 標題：kvcache-ai/ktransformers
- 作者／機構：kvcache-ai
- 連結：https://github.com/kvcache-ai/ktransformers

#LLM #Inference #FineTuning #CPUGPU #HeterogeneousComputing #KTransformers #SFT #EdgeAI #OpenSource #kvcacheai
