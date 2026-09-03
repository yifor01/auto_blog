---
title: Fine-tuning a 350M Model for Better Structured Outputs in 100 GRPO Steps
source: HuggingFace Blog
url: https://huggingface.co/blog/grpo-with-trl-ifstruct
model: claude-code/sonnet
generated_at: '2026-09-03T20:18:25.347346'
score: 94
---

📌 500 筆資料、100 步 GRPO，把 3.5 億參數模型的結構化輸出準確率拉高 7 個百分點

TL;DR：HuggingFace 示範用 GRPO 微調 LFM2.5-350M，IFStruct 基準分數從 22.6% 提升到 29.7%，免費 GPU 就能跑完整流程。

LLM 能不能穩定吐出「可被下游系統直接解析」的 JSON 或 YAML，往往比模型推理能力更關鍵，因為只要格式錯一個欄位，整條 pipeline 就會斷掉。但這項能力常被埋進更大範圍的推理或抽取分數裡，很少被單獨拿出來優化。HuggingFace 這篇教學就專門針對「結構化輸出合規率」做微調，而且全程可在免費層 GPU 上重現。

🤔 **結構化輸出為何是被低估的痛點**

多數 benchmark 把 schema 合規度（模型是否回傳可解析、符合要求格式與形狀的輸出）併入更廣的推理分數，導致這項能力常被忽略。但實務上，這正是模型能否被接進真實系統的決定性因素。文章選用 IFStruct 這個專門測試輸出有效性與 schema 遵循度的基準，並在 LiquidAI/LFM2.5-350M 這顆 350M 參數的小模型上驗證：透過針對性的輕量微調，能否讓小模型逼近更大模型的表現。

🧩 **用 LoRA + GRPO，只練 6M 參數**

微調流程使用 TRL 函式庫的 GRPO（Group Relative Policy Optimization）。因為 LFM2.5 採用 hybrid attention/convolution 架構，LoRA 的 target_modules 特別針對 LFM 專屬的模組名稱設定：`q_proj`、`k_proj`、`v_proj`、`out_proj`、`in_proj`、`w1`、`w2`、`w3`，LoRA rank 設為 16、alpha 32，總共只訓練約 600 萬參數，佔整體模型的 1.66%。

獎勵設計是這次微調的核心，共有三個獎勵函式，每個都落在 0 到 1 分區間：
- `json_format_reward`：輸出是否可解析、且符合要求的格式（fenced code block 或原始輸出）。完全符合給 1.0 分，格式錯但可解析給 0.2 分，無法解析則 0 分。
- `field_count_reward`：頂層欄位數量是否與預期相符，完全吻合給滿分，偏差則依差距線性遞減。
- `schema_validation_reward`：輸出是否符合該筆資料對應的 JSON Schema，會計算違反的限制數量，並以必填欄位覆蓋率作為部分分數的門檻。

三項獎勵以加權方式合併，權重為 `reward_weights=[1.0, 0.5, 2.0]`，最重視 schema 驗證是否通過。

📊 **訓練資料與規模：500 筆、100 步搞定**

訓練資料使用 `nvidia/Nemotron-RL-instruction_following-structured_outputs`，每筆 prompt 都配對一個目標 JSON Schema 與預期欄位數。作者只取約 500 筆樣本，並額外做了兩項資料增強，用來補齊 Nemotron 資料分布與 IFStruct 評測情境間的落差：40% 的樣本被加上「請把輸出包在 fenced code block 內」的指令，讓模型學會依照格式指示而非永遠輸出原始 JSON；另外獨立的 20% 樣本被轉換成「頂層陣列」任務（schema 被包在陣列裡並要求特定筆數），用來訓練 bare-list 輸出與筆數合規。整個訓練只跑 100 步、每個 prompt 群組取 8 個生成樣本，刻意控制在 16GB 顯示卡即可負荷的規模。

📊 **基準分數：22.6% → 29.7%**

微調前，作者先在本地用 llama.cpp 部署 LFM2.5-350M（BF16 GGUF）重現基準分數：在 2000 筆 IFStruct 測試樣本上，整體通過率為 452/2000（22.6%），與 IFStruct 官方部落格公布的 21.1% 相近。細看分類數據，JSON 格式通過率僅 18.0%，YAML 則有 27.2%；頂層結構方面，wrapper key 形式通過率 28.5%，bare list 只有 16.6%。最常見的錯誤是「必填欄位缺失」（7228 次）與「筆數錯誤」（738 次）。

經過 100 步 GRPO 微調後，IFStruct 分數從 22.6% 提升到 29.7%，也就是用極小的訓練成本，換來約 7 個百分點的絕對提升。

⚠️ **這不是要重現 IFStruct 官方 RL 模型**

作者特別澄清，這裡示範的訓練管線並非 IFStruct 部落格中用來訓練其 RL 模型的那套流程，目的也不是重現該基準分數，而是展示「針對性微調小模型」這件事本身能帶來多大的效能提升，並藉此逼近更大模型的表現。

🎯 **實務啟示**

如果你的應用嚴重依賴 LLM 吐出可解析的結構化資料，與其等待更大的模型，不如針對你自己的 schema 分布，用少量標註資料（甚至 500 筆等級）搭配 GRPO 做輕量微調，往往比換更大模型更划算，而且整個流程可以在免費層 GPU 上完成驗證。

🔗 **來源**
- 標題：Fine-tuning a 350M Model for Better Structured Outputs in 100 GRPO Steps
- 作者／機構：Leonie Monigatti, Ben Burtenshaw, Sergio Paniego @ HuggingFace / Liquid AI
- 連結：https://huggingface.co/blog/grpo-with-trl-ifstruct

#GRPO #TRL #LoRA #StructuredOutput #LLMFineTuning #ReinforcementLearning #IFStruct #HuggingFace #SmallLanguageModels #ReproducibleAI
