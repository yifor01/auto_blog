---
title: Serve Qwen3.8-2.4T-A95B, a 2.4T-Parameter Model, with Configurable Reasoning
  on NVIDIA GB300 NVL72
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/
model: claude-code/sonnet
generated_at: '2026-08-13T07:33:08.085332'
score: 98
---

📌 2.4兆參數、95B 啟用：Qwen3.8-Max 在 GB300 NVL72 上的服務首發

TL;DR：Alibaba 開源 2.4 兆參數 Qwen3.8-Max，NVIDIA GB300 NVL72 Day 0 就跑出 4K token/s/GPU。

一個 2.4 兆參數的模型要怎麼塞進生產環境還維持低延遲？NVIDIA 與 Alibaba 用一份 Day-0 效能報告給出了答案。

🤔 背景：為何一個 2.4T 模型能落地

Alibaba 釋出 Qwen3.8-2.4T-A95B（Qwen3.8-Max）開放權重，是其目前最大的開放權重模型，號稱把接近前沿等級的能力帶進開放生態系。模型總參數量 2.4T，每個 token 僅啟用 95B 參數；架構為細粒度 MoE，混合 full attention 與 linear attention，context window 最高支援一百萬 token，輸出長度最高 128K，設計目標是應付高難度推理與 agentic workload。部署這種規模的模型需要資料中心等級的加速運算，NVIDIA 正與開源生態系合作，透過最佳化 kernel、推理 runtime 與分散式 serving 配方，把模型帶到 multinode 部署環境。

🧩 架構設計：Full Attention 加 Linear Attention 混合，搭配細粒度 MoE

Qwen3.8-2.4T-A95B 是為編碼、大規模文件分析、長時間多步驟工作流等高難度 agentic 場景打造的。與單輪對話模型不同，agentic 應用會在工作流中不斷累積系統指令、工具輸出、檢索文件、程式碼、日誌與多步推理軌跡，context 一旦拉長，attention、運算與 KV cache 記憶體就成為主要瓶頸。模型採用 full attention 與 linear attention 交替的混合架構：在 full-attention 層，每個 token 會關注所有其他 token；在 linear-attention 層，持續成長的 KV cache 被替換成有界的循環狀態（gated delta network），讓運算與記憶體在 context 擴展到一百萬 token 時仍維持有界。

細粒度 MoE 則讓 2.4T 參數量可實際服務：容量不是集中在少數大型專家，而是分散到更多小型專家上，提升專精程度與每單位啟用運算的路由效率；一個學習到的 router 只會為每個 token 啟用需要的專家，因此服務成本跟著啟用參數走，而非全部 2.4T，等於用一小部分成本提供與同等級稠密模型相當的前沿容量。模型還內建可配置的推理深度控制（low／high／xhigh），讓開發者依任務需求在推理品質與運算成本之間取捨：複雜多步推理可調高，高吞吐文件處理則可調低。

📊 GB300 NVL72 實測：每 GPU 超過 4K tokens/秒

GB300 NVL72 是機架等級架構，整合 72 顆 NVIDIA Blackwell Ultra GPU，其大型 72-GPU NVLink domain 提供 130 TB/s 的 all-to-all 通訊頻寬，消除 expert 流量跨越傳統網路時會出現的瓶頸。在 FP8 精度、且未經任何額外模型調校的情況下，Qwen3.8-2.4T-A95B 在 GB300 NVL72 上 Day 0 即達到每 GPU 超過 4K tokens/秒、每使用者超過 350 tokens/秒的表現。NVIDIA 表示，後續包含 NVFP4 精度在內的最佳化，預期會隨時間帶來更多效能提升。

🎯 實務啟示：多種 serving 路徑與後訓練工具

NVIDIA 提供多種推理堆疊選擇：SGLang、vLLM 與 NVIDIA Dynamo 提供開源推理配方，適合需要對效能有更大掌控權的開發者；也可以透過 model-free 的 NVIDIA NIM（單一推理容器可服務任何支援模型）部署，下載模型權重即可 Day-0 部署、服務 fine-tuned checkpoint 並擴展到生產環境。若需要針對特定領域客製化，可用 NVIDIA NeMo AutoModel，這是一套 PyTorch 原生的微調函式庫，支援 Day-0 Hugging Face checkpoint，可直接在既有 checkpoint 上訓練而無需模型轉換，並支援完整 SFT 或記憶體效率較高的 LoRA 微調。模型權重可從 Hugging Face 或 ModelScope 下載，並透過 NGC 上的 model-free NVIDIA NIM 部署。

🔗 來源
- 標題：Serve Qwen3.8-2.4T-A95B, a 2.4T-Parameter Model, with Configurable Reasoning on NVIDIA GB300 NVL72
- 作者／機構：Michelle Horton，NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/

#Qwen3 #Alibaba #NVIDIA #GB300NVL72 #Blackwell #MoE #LLMInference #OpenWeights #AgenticAI #LongContext
