---
title: A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth
source: Hacker News
url: https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth
model: gpt-6.1-terra
generated_at: '2026-11-28T05:50:41.301966'
score: 89
---

📌 本機 AI 入門：模型與記憶體怎麼選

TL;DR：用 Unsloth Desktop 在 Windows 執行本機模型，關鍵是替模型和對話上下文預留 VRAM。

🎣 不想一直盯著雲端 AI 的使用額度，卻以為本機部署一定得先設定 Python 環境？這篇指南提供另一條路：在 Windows 上用圖形介面下載模型，並透過家中區域網路分享。

🤔 **本機部署的第一道門檻是 VRAM**

作者希望把研究、資料收集和程式編寫等耗費 token 的任務移到自有硬體，也將隱私列為考量。指南採用的組合包括 Windows 電腦、GPU、Unsloth Desktop，以及適合 GPU 記憶體的模型。

根據原文，硬體準備好之後，設定約需 10 至 15 分鐘，**不含下載時間**。指南中的流程不需要終端機指令、Python 環境或訂閱。

🧩 **量化讓模型變小，但要權衡輸出品質**

量化（quantization）透過降低模型權重的精度來縮小模型，讓原本放不進 GPU 的模型有機會在本機執行。代價是可能損失準確度；原文指出，不同工作負載受到的影響可能很不一樣。

選模型時也不能只看模型檔案大小。上下文視窗（context window）越大，通常需要預留更多記憶體。作者使用具備 32GB VRAM 的 RTX 5090，選擇 4-bit 量化的 Qwen3.8-27B，而不是塞入最大模型，目的是替較長的對話保留空間。

📊 **先依 VRAM 挑模型，再設定上下文大小**

原文提供以下粗略起點，實際需求仍取決於模型、量化版本和上下文大小：

| GPU VRAM | 可嘗試的模型 | 原文建議的上下文大小 |
|---|---|---|
| 8–12GB | Qwen3.5-9B、Gemma 4 12B | 8K–16K |
| 16GB | Qwen3-14B、Inkling 2 Mini | 16K–32K |
| 24GB | Qwen3.8-27B、Inkling 2 Mini | 16K–32K |
| 32GB 以上 | Qwen3.8-27B、Inkling 2 Mini | 64K–128K 以上 |

其中 Inkling 2 Mini 採用混合專家模型（mixture of experts，MoE）架構，每個 token 只啟用部分參數。原文指出，它的 4-bit 版本也能在 16GB 顯示卡上執行，但剩餘部分需放在系統記憶體中，速度會稍慢。

⚠️ **模型標示的上下文長度不等於硬體能裝下**

原文指出，Inkling 2 Mini 支援 1M token 的上下文，但其記憶體估算只涵蓋模型本身，較長的上下文還需要額外空間。使用 Inkling 2 前，指南也建議先更新 Unsloth Desktop。

Mac 使用者則可考慮統一記憶體（unified memory）的機型；原文建議 Apple Silicon 使用專為其打造的 MLX 版本模型。

🎯 **先讓模型跑起來，再調整容量與品質**

依照指南的精簡流程：

1. 在 Windows 安裝 Unsloth Desktop。
2. 下載適合 GPU VRAM 的量化模型。
3. 設定上下文大小，替對話保留記憶體。
4. 開啟區域網路（LAN）存取，讓家中其他人使用。

選型時可從表格中的較小模型與上下文開始，再依工作需求嘗試不同模型與量化版本。

🔗 **來源**
- 標題：A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth
- 作者／機構：Jerry James
- 連結：https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth

#LocalAI #LLM #Unsloth #Qwen #Inkling #Quantization #VRAM #GPU #MoE #Windows
