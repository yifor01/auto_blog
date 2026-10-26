---
title: Tsinghua AI Open-Sources AKV, a Cache Engineering Server for LLM Agents on
  SGLang
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/26/tsinghua-akv-kv-cache-engineering-llm-agents/
model: claude-code/sonnet
generated_at: '2026-10-26T21:48:01.279916'
score: 106
---

📌 清華開源 AKV：讓 Agent 自己丟棄 KV Cache，省下 27.7% 成本

TL;DR：清華大學與中文大學團隊開源 AKV，讓 LLM agent 選擇性捨棄 KV cache 而非重新計算，推理成本平均降 27.7%，任務分數還提升 1.7 分。

多輪對話的 agent 跑久了，context 會越疊越長，多數框架的做法是「摘要舊歷史」。但這篇研究指出一個常被忽略的代價：摘要會改動前綴文字，而前綴一變，後面所有的 KV cache 全部失效，得重新 prefill。清華大學與 CUHK（中文大學）團隊於是提出另一條路：不動文字歷史，只動 KV cache 本身要不要被看見。

🤔 **摘要為何昂貴：KV cache 讀取佔了 82.4% 的 API 成本**

Context engineering（文字層級的壓縮或摘要）會編輯 prompt 的前綴，一旦前綴改變，保留下來的 suffix 就必須重新計算。這逼得 agent harness 傾向「晚一點才摘要、摘要得更激進」，結果反而容易丟掉中間回合的細節。研究團隊在成本分析中發現，KV cache 的讀取就佔了總 API 成本的 82.4%，這也是 AKV 想直接處理的目標：既然讀取 KV cache 才是大頭，那就讓這些 cache 可以被安全地「捨棄」與「搬動」，而不是整段重算。

🧩 **三個 cache 操作：Append、Drop、Repos**

AKV 定義了三種操作：

- **Append**：新 token 進來時的標準更新。
- **Drop**：把選定的 cache 項目從未來的 attention 中移除，但不改變其他項目的位置。
- **Repos**：用 RoPE（旋轉位置編碼）旋轉，把保留下來的 key 重新寫到 0 到 r-1 的新位置；value 維持不變，所以不需要重新計算任何隱藏狀態。

消融實驗顯示，光是加上 Repos，就讓 GPT-OSS-120B 在 BrowseComp-Plus 上的 pass rate 從 55% 拉高到 62%，說明「重新壓縮位置」本身就有實際效益，不只是省記憶體。

🧩 **服務端的難題：同樣的 token，可能有不同的 cache 狀態**

技術上最棘手的地方在於服務層：同一段文字 token，在不同的操作歷史下會對應到不同的 cache 狀態，單純的前綴比對可能誤用錯誤的 cache。AKV 的做法是擴充 SGLang 的 radix tree，加入 drop 與 reposition 節點，只有在沒有任何進行中的請求還需要某段 KV 時才釋放它；並透過「segment-batch attention」在一次 prefill 內就恢復被驅逐的狀態。

對外介面則維持無狀態、OpenAI 相容：客戶端照樣送完整的訊息歷史，外加兩個可選欄位 ——`drop_message`（把某個觸發訊息的索引對應到要丟棄的訊息）與 `reposition`（列出需要壓縮位置的索引點）。上層還有 `CachePolicy` 把「觸發條件、選擇器、重新定位規則」封裝起來，內建 turn-based、token-based、model-based 三種策略；也可以用 `CacheTool` 讓模型自己呼叫 `drop_context`。論文中主要採用的策略是「工具回應滾動丟棄」，固定只保留最近 12 筆工具回應。

📊 **長上下文越久，差距越明顯**

評測涵蓋 BrowseComp-Plus、GAIA-Text、SWE-bench Verified 與 xbench-DeepSearch-2510，baseline 分別是在 96K tokens（MiroThinker 為 192K）才摘要的 Standard，以及在 48K tokens 就摘要的 Text Engineering。

| 測試情境 | Standard | Text Engineering | AKV |
|---|---|---|---|
| BrowseComp-Plus（96K tokens 以上，GPT-OSS-120B） | 24% | 32% | 37% |
| SWE-bench Verified（100 任務，固定 GPU 預算） | 40.7% | 32.3% | ~47% |

整體而言 AKV 比 Standard 平均成本降 27.7%、分數升 1.7 分，比 Text Engineering 再省 21.9% 成本。服務端的壓力測試也很直接：在 80 個長上下文 SWE-bench Verified 任務、並發數 16 的情況下，Standard 的 P95 延遲飆到 229.90 秒，AKV 只要 30.63 秒；每個 decode step 的 full-attention 時間則從 7.082 毫秒降到 2.849 毫秒 —— Standard 因為 KV 壓力被迫反覆重新 prefill，AKV 則避開了這個惡性循環。

另外，讓 MiniMax-M2.7 自己在 20 個 BrowseComp-Plus 任務上迭代 cache 策略，第六輪策略在同等準確率下比 Standard 省下 17.8% 成本，比人工設計的策略再省 7.1%；把丟棄 cache 的動作直接暴露成工具給模型呼叫，GPT-OSS-120B 的分數也從 52.1 分升到 61.0 分（但 MiniMax-M2.7 的成本也從 5.4 分升到 5.9 分，取捨因模型而異）。

⚠️ **數字來自不同論文、不同設定**

文中各項對比數字分別來自各自論文的設定，彼此並非直接可比，解讀時需留意這一點。

🎯 **實務啟示**

AKV 以 Apache-2.0 授權開源，直接建構在 SGLang 之上，介面維持 OpenAI 相容，等於是可以直接插進現有 agent harness：無論是用內建 `CachePolicy` 設定規則，或是讓模型自己學會呼叫 `drop_context`，都不需要重寫 prompt 管線，是對長任務、工具密集型 agent 相對低成本的最佳化切入點。

🔗 **來源**
- 標題：Tsinghua AI Open-Sources AKV, a Cache Engineering Server for LLM Agents on SGLang
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/26/tsinghua-akv-kv-cache-engineering-llm-agents/

#LLM #AIAgents #KVCache #SGLang #Tsinghua #InferenceOptimization #OpenSource #LLMOps #AgenticAI #MachineLearning
