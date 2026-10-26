---
title: 'Groundhog Day for AI agents: Prompt caching patterns for using OpenAI models
  on Amazon Bedrock'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/groundhog-day-for-ai-agents-prompt-caching-patterns-for-using-openai-models-on-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-10-26T21:49:49.662445'
score: 86
---

📌 Agent 也有記憶：Bedrock上的Prompt Caching實戰

TL;DR：AWS 說明如何用 prompt caching 讓 Bedrock 上的 OpenAI 模型不必每輪都重讀整段對話歷史，實測省下六成以上輸入成本。

想像一個 agent 每執行一步，就要把自己從頭到尾的人生故事重新讀一遍,這聽起來很荒謬,但這正是多數 AI agent 的真實處境:模型沒有內部記憶,每次呼叫都得把系統提示、工具定義、對話歷史整包重新餵進去,到第 20 輪時,前 19 輪的內容又被重新讀了一次,而這些 token 費用全由你買單。

🤔 **Agent 的 Groundhog Day 困境**

當模型讀取 prompt 時,會先執行一個叫 prefill 的運算步驟:處理每一個輸入 token,建立 key-value（KV）向量,這是模型開始輸出第一個字之前必經的過程。沒有快取機制時,這整段運算每輪都要重做一次。

🧩 **Implicit 與 Explicit 兩種快取模式**

Prompt caching 的做法是把這段 prefill 狀態存起來,下次請求若開頭 token 完全相同,就直接載入已存的狀態,只處理新增的部分。Amazon Bedrock 提供兩種模式:

- Implicit（隱式）：由 Bedrock 自動判斷可重複使用的前綴邊界,適合隨對話成長、內容多變的場景。
- Explicit（顯式）：開發者用 `prompt_cache_breakpoint` 自行標記邊界,適合標記工具清單、系統指令這類跨 session 共用的靜態內容。

兩者可以搭配使用:explicit 負責固定不變的工具與指令區塊,implicit 則讓 Bedrock 自動處理持續增長的對話歷史。文章也提醒,要快取的前綴需要（在一次測試案例中）達到 1,024 token 才符合資格,而且快取只在輸入文字「完全相同」時才會命中,所以工具清單的序列化方式、MCP 伺服器的索引順序都必須保持一致;會變動的日期、使用者名稱、request ID 則要放在被快取的指令之後。

📊 **實測省下六成輸入成本**

在一次 explicit caching 測試中，約 4,000 token 的工具與指令前綴，第一次請求寫入了 4,120 token 到快取，之後的請求則直接讀取這 4,120 token。在一段六輪對話的工作流程測試裡，GPT-6 Astra 模型用 implicit 快取相比完全不快取，輸入成本降低約 62%；用 explicit 的 rolling breakpoint 方式則降低約 61%。文章也強調，這些是特定工作負載下的結果，實際效益需要依自己的 agent 場景實測。

⚠️ **工具清單一變動，快取就可能失效**

文章特別提醒：新增、移除或重新排序工具定義，都可能讓已快取的前綴失效，因此如果 agent 的工具集會隨時間擴充，需要仔細選擇讓新工具加入的方式，避免破壞既有的快取命中率。

🎯 **實務啟示**

如果你的 agent 架構裡，每輪呼叫都要重送完整的系統提示和工具定義，這是最直接能省錢又能降低延遲的切入點。先用 explicit breakpoint 固定住工具與指令這類不變內容，再讓 implicit 模式接手處理持續增長的對話歷史，是文章建議的組合做法；同時留意工具清單的序列化穩定性，這是快取命中率的隱形殺手。

🔗 **來源**
- 標題：Groundhog Day for AI agents: Prompt caching patterns for using OpenAI models on Amazon Bedrock
- 作者／機構：Claudio Mazzoni（AWS ML Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/groundhog-day-for-ai-agents-prompt-caching-patterns-for-using-openai-models-on-amazon-bedrock/

#AmazonBedrock #PromptCaching #AIAgent #OpenAI #LLMOps #CostOptimization #AWS #AgenticAI #MachineLearning #CloudComputing
