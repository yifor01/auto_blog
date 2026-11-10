---
title: 'Google Unveils TPU 8i Max and TPU 8tx: A Dual-Chip TPU and a Confidential
  TPU'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/09/google-tpu-8i-max-tpu-8tx/
model: claude-code/sonnet
generated_at: '2026-11-10T01:01:31.979659'
score: 86
---

📌 TPU 8i Max 規格拆解：單晶片推算 20.2 PFLOPS，KV 傳輸延遲降到 230ms

TL;DR：MarkTechPost 根據 Google 公開數據反推 TPU 8i Max 的效能規模，並揭露 TPU Sync 在 Qwen3 測試中的延遲改善幅度。

Google 這次沒有公布 TPU 8i Max 的絕對效能數字，但從既有 TPU 8i 單晶片規格乘以二，可以大致估算出這款雙晶片封裝的真實威力——以及它和機密運算版本 TPU 8tx 之間的分工關係。

🤔 **新增的是系統配置，不是新晶片**

Google 在第八代 TPU 陣容中新增兩款系統：TPU 8i Max 針對超長 context window 與機架運算密度，TPU 8tx 針對安全、機密推理。兩者都與四月發布的 TPU 8t、TPU 8i 並列，但關鍵是：Google 重複使用既有的第八代矽晶圓，只是改變封裝、主機、記憶體與網路的組合方式。

🧩 **雙晶封裝攻記憶體牆，機密版沿用訓練晶片**

TPU 8i Max 把兩顆低延遲的 TPU 8i 晶片封裝進同一個模組，直接針對「記憶體牆」——當數十個 AI agent 同時處理整個程式碼庫或數小時影片時，記憶體頻寬往往比算力更早成為瓶頸。TPU 8tx 則沿用與 TPU 8t 相同的晶片，搭配第五代 AMD EPYC CPU 主機，並採用原本為 TPU 8i 打造的 Boardfly 低延遲網路，讓資料與模型權重在「使用中」也維持加密與隔離。

📊 **從官方數字反推出的規模**

MarkTechPost 指出，Google 官方公布的單顆 TPU 8i 規格為：10.1 PFLOPS（FP4）、288GB HBM、8,601 GB/s 頻寬、384MB 晶片內 SRAM。把這些數字乘以二，可推算 TPU 8i Max 約為 20.2 PFLOPS（FP4）、768MB SRAM、約 17.2 TB/s 頻寬——但 Google 並未公布這些絕對數字，也未揭露 TPU 8i Max 的 HBM 容量。

另外，文章引用了一組獨立於新硬體之外的延遲數據：在 Qwen3 235B 模型上，TPU Sync 把 median KV 傳輸延遲從數秒降至約 230ms；在低並發情境下，235B 模型的 TTFT（首個 token 延遲）平均下降 60%，480B 模型下降 90%。這些測試是在 Ironwood（TPU v7x）上進行，並非 TPU 8i Max 或 TPU 8tx 本身的實測結果。

⚠️ **數字的來源要分清楚**

兩點需要留意：一是 TPU 8i Max 的效能數字是媒體依據「公開單晶片規格 ×2」推算出的衍生值，並非 Google 官方公布的絕對數字；二是 TPU Sync 的延遲改善數據測試對象是現有的 Ironwood（TPU v7x），而不是這次新發布的系統，兩者不能直接混為一談。

🎯 **對工程團隊的實務意義**

兩個訊號值得留意：第一，新系統是封裝與配置層面的創新，而非全新矽晶圓，意味著既有軟體棧（如 PyTorch）的相容性風險相對較低，遷移成本可能不如想像中高；第二，TPU Sync 展示的 KV cache 傳輸延遲改善，提醒我們長 context、高並發推理場景下，傳輸層最佳化和算力堆疊同樣重要，不能只看 PFLOPS 數字。

🔗 **來源**
- 標題：Google Unveils TPU 8i Max and TPU 8tx: A Dual-Chip TPU and a Confidential TPU
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/09/google-tpu-8i-max-tpu-8tx/

#TPU #GoogleCloud #AIHardware #ConfidentialComputing #Inference #Qwen3 #AIInfrastructure #MachineLearning #LLMServing #PFLOPS
