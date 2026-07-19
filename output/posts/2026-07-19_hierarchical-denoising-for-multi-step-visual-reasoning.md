---
title: Hierarchical Denoising For Multi-Step Visual Reasoning
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.15278
score: 99
model: tencent/hy3:free
generated_at: '2026-07-19T08:02:52.914329'
---

📌 【HuggingFace Papers】分層去噪讓影片模型學會多步視覺推理

TL;DR：HDR 框架以樹狀分層 latent 做粗到細推理，成功率達 60.29 且延遲僅 0.70 秒。

影片模型正朝向 vision foundation models 發展，但在需要多步驟邏輯推演的任務上，仍遠不如人類。現有的 streaming autoregressive diffusion 雖有效率，卻難以做複雜推理；bidirectional diffusion 能全域性修訂，卻因密集的 frame-level denoising 而推論成本過高。兩者都無法同時兼顧邏輯一致性與低延遲串流。

🤔 **現有範式在複雜推理上的兩難**

Streaming autoregressive diffusion 走因果式生成、效率佳，但受限於推理能力；bidirectional diffusion 可做全域性修訂，卻因為要對每個影格做密集去噪，推論開銷極大。兩種路線都難以在複雜多步推理任務中，同時做到邏輯連貫與低延遲輸出。

🧩 **HDR：把視覺 latent 排成樹狀階層做粗到細推理**

作者提出 HDR（Hierarchical Denoising for Visual Reasoning），一個統一架構，將分層 latent 整合進 causal video generation 中。其核心設計為：

- 將 video latents 組織成 tree-structured hierarchy，在串流輸出前先進行 coarse-to-fine 推理。
- 較粗的去噪層（coarse denoising layers）保留不確定的假設，供全域性規劃使用。
- 較細的層逐步把假設精煉成具體的視覺狀態（visual states）。
- 搭配 sparse hierarchical attention pattern（SHAP），進一步降低 temporal attention 的成本。

📊 **六項推理基準上，成功率從 34.22 升至 60.29**

論文引入一個 level-stratified 多步影片推理基準，不含 out-of-distribution 案例，涵蓋六項任務：maze navigation、Tower of Hanoi、one-line drawing、sliding puzzle、Sokoban、water pouring。

與 streaming autoregressive diffusion baseline 相比：

| 指標 | Baseline | HDR | 提升 |
|------|----------|-----|------|
| 成功率 | 34.22 | 60.29 | 相對 +76.2% |
| 平均進度 | 76.00 | 89.56 | 推理軌跡更一致 |

在效率面，HDR 維持低延遲串流，每個 latent 僅 0.70 秒，推論速度比 bidirectional diffusion 快 54.2 倍。資料效率上，只用 2% 訓練資料可保留 82.9% 的全資料效能，而 bidirectional diffusion 僅有 52.0%。

💡 **真實機器人實驗驗證世界模型潛力**

README／摘要指出，真實世界的 robot experiments 進一步展示 HDR 在物理互動與 world modeling 上的潛力，說明該框架不只停留在合成基準。

🎯 **實務啟示**

對做影片生成或視覺推理的 ML 工程師來說，HDR 展示了一條兼顧「全域性規劃」與「低延遲串流」的設計路線：用樹狀分層 latent 與稀疏注意力，取代要麼太淺、要麼太慢的舊範式。若你的應用需要多步邏輯（如機器人操作、謎題求解），這套分層去噪思路值得跟進。

🔗 **來源**
- 標題：Hierarchical Denoising For Multi-Step Visual Reasoning
- 連結：https://huggingface.co/papers/2607.15278

#VisualReasoning #VideoGeneration #DiffusionModels #HierarchicalDenoising #LowLatency #WorldModeling #Robotics #Benchmark #Attention #MLResearch
