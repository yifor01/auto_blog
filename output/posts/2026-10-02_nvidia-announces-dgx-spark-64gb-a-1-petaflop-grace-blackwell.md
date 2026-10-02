---
title: 'NVIDIA Announces DGX Spark 64GB: A 1-PetaFLOP Grace Blackwell Desktop for
  Local AI Agents, Fine-Tuning, and Inference'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/02/nvidia-announces-dgx-spark-64gb-a-1-petaflop-grace-blackwell-desktop-for-local-ai-agents-fine-tuning-and-inference/
model: claude-code/sonnet
generated_at: '2026-10-02T21:41:37.819353'
score: 74
---

📌 【NVIDIA】64GB 版 DGX Spark 來了，桌上型 1 petaFLOP 跑本地 agent

TL;DR：NVIDIA 推出 64GB 版 DGX Spark 桌機，瞄準本地 agent 推論與微調，可堆疊叢集擴充記憶體。

當 agent 工作流一次又一次呼叫工具、重試、累積長上下文，雲端 API 的帳單也跟著一路攀升。NVIDIA 這次給出的答案不是更便宜的 API，而是一臺接上家用插座就能跑的桌上型運算工作站。

🤔 agent 燒 token 的帳單思維要換了

根據報導，agent 的 token 消耗量自 2026 年初以來成長了 14 倍：每一次工具呼叫、重試、長上下文、多步驟規劃都在燒 token，在雲端 API 上每一個 token 都要計費。NVIDIA 的論述很直接：在自己的硬體上運算，沒有這筆持續性的 per-token 費用，這正是新推出 64GB 版 DGX Spark 要解決的問題。

🧩 GB10 統一記憶體，模型不用搬家

64GB 版 DGX Spark 由 Acer、ASUS、Dell、Gigabyte、HP、MSI 等廠商推出，搭載與原版相同的 GB10 Grace Blackwell superchip：Blackwell GPU 配第五代 Tensor Core，加上 20 核心 Grace Arm CPU，FP4（含 sparsity）運算力最高可達 1 petaFLOP。與原本的 128GB 機型差異只在記憶體：64GB 版用統一的 64GB LPDDR5x，NVIDIA 表示這個容量足以應付目前最強的 30 到 35B 級開源模型。

關鍵設計是 CPU 與 GPU 透過 NVLink-C2C 共享同一塊記憶體池，頻寬是 PCIe Gen5 的 5 倍，不需要在系統 RAM 與 VRAM 之間複製權重。對 agent 而言，這代表多個模型、它們的 KV cache 與工具執行行程可以共存在同一個位址空間裡。軟體面則是開機即附 DGX OS，內建 PyTorch、Jupyter、Ollama，可一指令安裝 NVIDIA NemoClaw 為 OpenClaw agent 加上隱私與安全控制，再疊上屬於 Agent Toolkit 一環的 NVIDIA OpenShell 做 policy-based guardrails。

📊 關鍵數字：1 petaFLOP、17GB 量化模型、1.7 倍叢集加速

| 項目 | 數據 |
|---|---|
| FP4 AI 運算力（含 sparsity） | 最高 1 petaFLOP |
| CPU | 20 核心 Grace Arm |
| 記憶體頻寬（NVLink-C2C） | PCIe Gen5 的 5 倍 |
| Muse Glimmer（Meta 由 Muse Spark 蒸餾而成）SWE-Bench Pro | 51.2 |
| Muse Glimmer MCP Atlas | 75.5 |
| Muse Glimmer 情境長度 | 131K tokens |
| Muse Glimmer 量化版本記憶體需求 | 約 17GB（BF16 版需 55GB 以上） |
| 單節點 nanochat 分散式微調速度 | 約 18,400 tokens/s |
| 2 臺叢集 vs 1 臺 128GB 單機 | 最高 1.7 倍效能，合計頻寬 546 GB/s |
| 4 節點 decode 加速 | 約 1.4 倍 |

💡 叢集拚的是 TTFT，不是單純算力翻倍

報導指出，叢集化讓 time to first token（TTFT）大約每倍增節點數就減半，對於需要讀長輸入的 agent 這是最有感的提升；相對地，decode 速度的改善幅度溫和許多。每一臺 DGX Spark 都內建 ConnectX-7 的 200GbE 網路，叢集是原生功能而非外掛，NVIDIA Sync 的 Windows／macOS 應用程式負責在網路上發現機器並管理 SSH 存取，其 Cluster Assistant 可設定最多 4 臺系統的 ConnectX-7 連線，甚至能透過 Tailscale mesh 跨地點連線而不經過雲端。

⚠️ 64GB 仍有天花板，大模型要靠多機

64GB 機型終究只適合 30B 等級模型的量化版本：BF16 全精度的 Muse Glimmer 就需要 55GB 以上記憶體，幾乎吃光可用容量，留給 context 的空間有限，量化到約 17GB 才是現實可行的做法。更大的模型如 DeepSeek V4 Flash，NVIDIA 自己的 benchmark 也是在 4 臺 64GB 叢集上執行，單機依然無法負擔。本文屬 NVIDIA 贊助內容，閱讀時可留意立場。

🎯 把推論、微調、評測都搬回自己的桌子

對正在評估 agent 基礎設施的團隊，這提供了一個新選項：把日常推論、QLoRA 微調與新模型評測都搬到本地端執行，省下反覆呼叫雲端 API 做幾十次 regression eval 的費用；當任務真的超出本地算力，再把問題送往雲端大模型做 fallback，是一種務實的混合部署思路。

🔗 來源
- 標題：NVIDIA Announces DGX Spark 64GB: A 1-PetaFLOP Grace Blackwell Desktop for Local AI Agents, Fine-Tuning, and Inference
- 作者／機構：Jean-marc Mommessin，刊於 MarkTechPost（NVIDIA 贊助文章）
- 連結：https://www.marktechpost.com/2026/10/02/nvidia-announces-dgx-spark-64gb-a-1-petaflop-grace-blackwell-desktop-for-local-ai-agents-fine-tuning-and-inference/

#NVIDIA #DGXSpark #EdgeAI #LocalLLM #AIAgent #FineTuning #GraceBlackwell #QLoRA #OnDeviceAI #AIHardware
