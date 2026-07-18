---
title: Fine-tune video and image models at scale with NVIDIA NeMo Automodel and 🤗
  Diffusers
source: HuggingFace Blog
url: https://huggingface.co/blog/nvidia/scale-diffusers-finetuning-nemo-automodel
score: 98
model: tencent/hy3:free
generated_at: '2026-07-18T07:32:47.943943'
---

📌 【NVIDIA × Hugging Face】用 NeMo Automodel 大規模微調 Diffusers 擴散模型

TL;DR：NeMo Automodel 與 Diffusers 整合，讓 Hub 上擴散模型免轉檔直接分散式微調。

擴散模型（diffusion models）從 FLUX.1-dev 到 Wan 2.1、HunyuanVideo，已經是開源生成式AI的主流出貨格式。但當你要從單張 GPU 擴到數百張去 fine-tuning 這些模型，記憶體分片、潛在快取、多解析度分桶這些瑣事，往往比模型本身更頭痛。

🤔 **Diffusers 成為擴散模型事實標準，但訓練擴充仍是痛點**

🤗 Diffusers 函式庫已成為 FLUX.1-dev（文字轉影像）、Wan 2.1 與 HunyuanVideo（文字轉影片）等開源模型的預設家園，提供一致的推論、適配與管線組合介面。隨著訓練與微調需求上升，工程師需要具備記憶體高效分片（memory-efficient sharding）、latent caching、multiresolution bucketing，以及能從 1 張 GPU 平滑擴充套件到數百張的配置工具。

🧩 **NeMo Automodel 補上生產級分散式訓練缺口**

NVIDIA 開源的 NeMo Automodel 函式庫正是為了滿足上述技術需求而生。本次 NVIDIA 與 Hugging Face 的合作，將生產級、分散式的擴散訓練能力帶到 Hugging Face Hub 上任何 Diffusers 格式的模型：不需要 checkpoint 轉換，也不需要為新模型重寫程式碼。

💡 **整合亮點：零轉檔、零改寫即可上線**

這項整合已寫入 Diffusers 訓練指南，並以 Apache 2.0 完全開源。對使用者而言，核心解鎖的能力是——任何放在 Hub 上的 Diffusers 模型，都能直接套用分散式訓練流程。

🎯 **實務啟示：從單卡原型到多卡量產的平滑路徑**

對於已經在用 Diffusers 做推論或單卡微調的團隊，這套整合意味著不必綁死特定模型格式或自行開發分散式訓練膠水程式碼。README 指出工作流程包含：預編碼資料集 → 用現有 FLUX YAML 啟動訓練 → 從微調後 checkpoint 生成，並提供其他 Fine-tuned / LoRA 範例可供參考。下一步官方預告將推出 Pythonic recipe APIs，進一步降低使用門檻。

🔗 **來源**
- 標題：Fine-tune video and image models at scale with NVIDIA NeMo Automodel and 🤗 Diffusers
- 作者／機構：HuggingFace（與 NVIDIA 聯合發布；Sayak Paul 參與整合與共同撰寫）
- 連結：https://huggingface.co/blog/nvidia/scale-diffusers-finetuning-nemo-automodel

#DiffusionModels #NeMoAutomodel #Diffusers #HuggingFace #NVIDIA #FineTuning #DistributedTraining #LoRA #TextToVideo #OpenSource
