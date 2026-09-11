---
title: Together AI expands fine-tuning service with more models, live metrics, and
  finer controls
source: Together AI
url: https://www.together.ai/blog/together-ai-expands-fine-tuning-service-with-more-models-live-metrics-and-finer-controls
model: claude-code/sonnet
generated_at: '2026-09-11T19:53:51.552006'
score: 79
---

📌 Together AI 微調平臺升級：MoE 專家層也能 LoRA 了

TL;DR：Together Fine-Tuning 新增 GLM-5.3、Kimi K2.7 等最新模型、即時訓練曲線，以及能訓練 MoE 專家層的 Expert LoRA。

如果你用 LoRA 微調一個 Mixture-of-Experts（MoE）模型，卻發現模型死活學不會新知識，問題可能不在資料，而在於 LoRA adapter 根本沒碰到模型真正「懂事」的那部分參數。Together AI 這次更新，正是針對這個容易被忽略的細節下手。

🧩 **新模型支援：從旗艦到端側一次到位**

Together Fine-Tuning 這次擴大支援一批最新的開放權重模型，包括追求極致效能的 GLM-5.3、GLM-5.2、GLM-5.1、Kimi K2.7-Code、Kimi K2.6，兼顧效能與成本的 Qwen 3.8-27B、Qwen 3.6 系列、Gemma 4 系列，以及適合本機／端側部署的 Qwen 3.5 系列（參數量從 0.8B 到 9B 不等）。文中提到 GLM-5.3 在 Terminal-Bench 2.1 上拿下 88.2 分，與頂尖的專有模型只差一分。使用者只需送出訓練任務，架構相關的複雜度由平臺在背後處理。

📊 **即時追蹤訓練曲線，不用再開一堆分頁**

微調任務現在會在每個訓練與評估步驟記錄指標，並透過 Together API、CLI 與 UI dashboard 直接暴露出來。每個 job 都有一個會即時更新曲線的 Metrics 分頁，可以同時勾選多個 job 疊圖比較，讓一整組 sweep 實驗變成一張圖，而不是十幾個瀏覽器分頁。核心訓練訊號（loss、gradient norm、learning rate）每次都會記錄；有設定 validation set 的話，evaluation loss 與相關指標也會一併追蹤。透過 Python SDK，也能直接在終端機拉曲線，不需要切換介面。

💡 **Expert LoRA：把 adapter 放到真正儲存知識的地方**

在 MoE 模型中，超過 90% 的參數、也是模型大部分知識所在，都落在專家層（expert layers）。標準 LoRA 微調只把 adapter 接在 attention 上，專家層維持凍結，等於完全沒訓練到知識最集中的地方。這次更新讓使用者可以直接把 LoRA adapter 加到專家層本身。

Together 團隊做了一個對照實驗：教模型 200 個捏造的新事實（確保 base model 完全不知道），結果如下：

| 設定 | 新知識回想率 | MMLU-Pro |
|---|---|---|
| 僅 attention 的 LoRA adapter | 最高 15% | 71.5% |
| 涵蓋專家層的 LoRA adapter | 最高 89% | 75.3% |

團隊解釋，用僅 attention 的 adapter 訓練時，會有越來越多路由到的專家在微調過程中逐漸「閒置」，而涵蓋專家層的 adapter 能讓整個 MoE 混合結構保持活躍。啟用方式也很簡單，只要把 expert modules 加進 `lora_trainable_modules` 即可，其餘流程與一般 LoRA job 相同。

🧩 **Early stopping 與任意 batch size**

新增的 early stopping 功能會在設定 validation set 後，於每次評估監控 validation loss；一旦曲線出現平原（plateau），系統會自動停止訓練、保留 validation loss 最佳的 checkpoint 作為最終模型，並退回未使用的訓練步驟費用。patience、對小幅改善的敏感度、warmup 都可調整。

針對顯存放不下的大 batch 需求（長序列、大模型，或需要調大 global batch 的訓練配方），現在可以透過設定 `gradient_accumulation_steps`，讓梯度先在多個 micro-batch 間累積再更新，effective batch size 等於 `batch_size × gradient_accumulation_steps`，不再受單次前向傳遞顯存上限限制。

📊 **價格調降 30% 到 70%**

Together 同步調降多數模型的訓練費用，部分模型（如 gpt-oss 系列）降幅達 70%。以每百萬 token 訓練 LoRA adapter 的費用為例：

| 模型 | 舊 SFT | 新 SFT | 舊 DPO | 新 DPO |
|---|---|---|---|---|
| Qwen/Qwen3.5-9B | 0.48 | 0.34 | 1.20 | 0.84 |
| Qwen/Qwen3.8-27B | 1.50 | 1.05 | 3.75 | 2.62 |
| google/gemma-4-31B-it | 1.50 | 1.05 | 3.75 | 2.62 |
| openai/gpt-oss-120b | 5.00 | 2.50 | 12.50 | 6.25 |
| openai/gpt-oss-20b | 1.50 | 0.40 | 3.75 | 1.00 |

文中也分享了 Adaption 公司的案例：其 AutoScientist 系統用一個閉環流程自動搜尋訓練配方、最佳化資料、訓練與評估，支援 LoRA 與全參數微調，模型規模最高達 1 兆參數，訓練由 Together 平臺承載，評估則跑在 Together 的專屬 endpoint 上。

🎯 **實務啟示**

如果你的微調任務是要讓模型「學會新知識」而不只是「調整語氣風格」，而底層模型剛好是 MoE 架構，Expert LoRA 這個選項值得優先評估——對照實驗顯示 attention-only 的 adapter 可能根本學不進新事實。另外，early stopping 加上即時 metrics 追蹤，等於把「盯著 loss 曲線手動判斷何時該停」這件事自動化，對頻繁跑 sweep 實驗的團隊能省下不少人力與算力成本。

🔗 **來源**
- 標題：Together AI expands fine-tuning service with more models, live metrics, and finer controls
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/together-ai-expands-fine-tuning-service-with-more-models-live-metrics-and-finer-controls

#TogetherAI #FineTuning #LoRA #MoE #OpenWeightModels #GLM #Qwen #MachineLearningOps #LLMTraining #ModelDeployment
