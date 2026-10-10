---
title: 'Microsoft AI Releases Microsoft-Decision-1: A Qwen3.5-9B Decision-Scoring
  Model'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/09/microsoft-ai-releases-microsoft-decision-1-a-qwen3-5-9b-decision-scoring-model/
model: claude-code/sonnet
generated_at: '2026-10-10T20:40:53.341254'
score: 95
---

📌 【微軟跟進新賽道】Microsoft-Decision-1：Qwen3.5-9B 打造的決策評分模型

TL;DR：微軟推出「決策模型」新類別產品，標榜低延遲與高準確率，但競品 benchmark 方法論已被對手公開質疑。

就在開源陣營推出決策模型沒多久，微軟也端出自己的版本，而且順手把對手的測試方法拿出來比較，意外掀起一場 benchmark 公平性的爭論。

🤔 **什麼是決策模型**

Microsoft-Decision-1 讀取一個情境、一個問題與固定的答案選項，回傳每個選項的校正機率，而不是生成文字。微軟稱這是一個全新的 AI 類別，目標是產出「軟體可以直接拿來用」的輸出，而不是需要人類再解讀的自然語言。這個模型是以阿里巴巴的 Qwen3.5-9B 為基礎做 post-training 得到的，目前已在 Microsoft Foundry 與 OpenRouter 上架。訓練資料來自微軟 Open Data 流程下的公開資料集，加上合成資料，輸出格式固定為 JSON。微軟表示未來版本計畫改以 MAI 與 OpenAI 的模型作為基底。OpenRouter 上的說明指出，權重會持續更新，但 API 介面會保持不變。

📊 **36 項 benchmark、14 萬題測試，延遲是強打重點**

微軟在 36 項 benchmark、共 147,137 道題目上比較了 9 套系統，且這些 benchmark 在訓練階段是完全隔絕的。Microsoft-Decision-1 的平均準確率以 83.5% 排名第一，p50 延遲為 85 毫秒、p95 為 125 毫秒，比 Quyet-1.0-Large 快 4.5 倍，比 GPT-6 Sol（3.01 秒）快 35 倍。微軟也做了穩健性測試：對每個請求做 8 種擾動（包含改寫句子、選項洗牌），結果平均只有 1.3% 的擾動會讓模型翻轉決策；當擾動方式是改寫、反向排列或洗牌選項時，翻轉率甚至是零。在安全性測試上，微軟針對 11 項涵蓋有害內容、jailbreak 與 prompt injection 的 benchmark 跑了 5,250 次請求，宣稱能正確拒絕危險請求同時保留大部分可用性，但沒有公開具體分數。

💡 **延遲比較方法被對手公開打臉**

這組漂亮的延遲數字有個但書：微軟是透過自家 Foundry 直接量測自己的模型，但圖表上競品的延遲數字，用的是 JevBench v1.6.1 的「調整後中位數」，不是原始量測值。H2O.ai 在自家 model card 上直接點名反駁，指出 JevBession 的調整方式會把實際耗時加倍，再外加 0.15 秒，並宣稱自家模型實際測得的中位數是 29 毫秒，不是圖表上顯示的 210 毫秒。另外值得注意，Microsoft-Decision-1 目前並未出現在 JevBench 官方排行榜上；該榜單的官方綜合分數裡，H2O-Lightning-4B 排名第一，拿下 72.5 分。這代表讀者在看任何決策模型的「比較圖」時，最好先確認延遲與分數是不是用同一套量測方法算出來的。

⚠️ **使用上的限制**

開發者可以在 Microsoft Foundry 以「Direct from Azure」的正式服務呼叫這個模型；但在 OpenRouter 上，它跑在獨立的 Decisions API，而不是一般的 chat completions 端點，意味著既有的 chat SDK 無法直接沿用。計價方面，輸入每百萬 token 收費 0.042 美元，輸出免費；作為對比，OpenAI 的 Luna decisions 端點輸入每百萬 token 收費 0.10 美元。

🎯 **實務啟示**

如果你的系統需要高頻率、低延遲的分類／路由／驗證任務，Microsoft-Decision-1 的輸入定價與延遲數字確實有吸引力；但在下決定前，建議自己用相同的量測方式重跑一次 benchmark，而不是完全依賴官方對比圖表。

🔗 **來源**
- 標題：Microsoft AI Releases Microsoft-Decision-1: A Qwen3.5-9B Decision-Scoring Model
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/09/microsoft-ai-releases-microsoft-decision-1-a-qwen3-5-9b-decision-scoring-model/

#DecisionModel #Microsoft #Qwen #MicrosoftFoundry #OpenRouter #LLM #Benchmark #AIInfrastructure #MachineLearning #AgentTools
