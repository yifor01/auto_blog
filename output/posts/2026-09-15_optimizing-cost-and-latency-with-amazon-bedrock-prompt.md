---
title: Optimizing cost and latency with Amazon Bedrock prompt caching
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/optimizing-cost-and-latency-with-amazon-bedrock-prompt-caching/
model: claude-code/sonnet
generated_at: '2026-09-15T20:39:55.167941'
score: 82
---

📌 同一份文件問 50 次，Bedrock Prompt Caching 省下 90% 成本

TL;DR：把重複的 context 快取起來，輸入 token 成本最高可降 90%。

一份 10,000 token 的合約，配上 50 個使用者問題，等於要付 500,000 個輸入 token 的費用去重複處理模型早就看過的內容。這不是效率問題，是白花錢的問題。

🤔 **重複處理，就是在燒錢**

過去解決這個問題的方式,不外乎縮短 prompt、減少 context window，或是自己在應用層做快取，但每種做法都有取捨。Amazon Bedrock 的 prompt caching 則是在基礎設施層級直接解決：當你把對話 context 中的系統提示、文件或工具定義快取起來，後續請求可以直接讀取快取，而不必重新處理。根據 Amazon Bedrock prompt caching 定價，這能讓命中快取的輸入 token 成本降低最高 90%，同時也能降低首個 token 生成時間（TTFT），完全不需要更換模型或犧牲 prompt 品質。

🧩 **cachePoint 標記怎麼運作**

當請求中包含 cachePoint 標記時，Amazon Bedrock 會檢查標記前的內容是否命中既有快取。命中時（cache hit），模型可以跳過重新處理這些 token，直接從快取狀態開始生成；沒有命中時（cache miss），模型會完整處理內容,並把結果寫入快取供未來請求使用。回應中的 usage 物件會多出兩個欄位，分別對應快取寫入與快取讀取的 token 數。

文章示範了六種由淺入深的快取情境，其中最基礎也最常見的是「文件快取」：在 RAG 應用中反覆針對同一份文件提問，或是 coding assistant 反覆參照同一份大型程式碼庫時，把 cachePoint 放在靜態文件與動態問題之間，Bedrock 會在第一次呼叫時快取文件內容，後續呼叫則重複使用。

在使用 Anthropic Claude Sonnet 4.5 搭配一份超過 1,024 token 的文件測試中，第一次請求的回應顯示為快取寫入；第二次帶著相同文件前綴、但問題不同的請求，則顯示 cacheReadInputTokens 讀取了 1,898 個 token，只有問題本身的 28 個 token 被當作標準輸入處理,整份文件前綴完全沒有被重新處理,並且這些快取讀取的 token 會以較低的快取讀取費率計價（比標準輸入低 90%）。文章也指出，Claude 模型在 Bedrock 上支援簡化的快取管理：只要放一個 cachePoint，Bedrock 會自動檢查該標記前約 20 個內容區塊範圍內是否命中快取，不需要手動放多個檢查點；若要更細緻的控制，也可以在每個段落後各自放置 cachePoint，支援部分命中。

系統提示（system prompt）與工具定義（tool definitions）快取則是另外兩個實用情境：詳細的 persona 與回應準則常常長達數千 token，卻在每次互動中維持不變；agentic 應用中的工具 schema 也常常集體佔用數千 token,且很少變動。把 cachePoint 分別放在 system 參數內的文字之後，或是 toolConfig 底下 tools 陣列的最後一個元素，就能避免每一輪都重新處理這些固定內容。

📊 **省下的是淨成本，不是理論上限**

以一份 10,000 token 的文件配上 10 個不同問題為例：第一次請求會產生快取寫入成本，後續九次請求各自以快取讀取的折扣價（降低 90%）命中,整體換算下來,這份文件 context 的淨成本節省約 75%。前提是所有後續請求都落在 TTL 有效期內，一旦過期就會觸發新的快取寫入，實際節省幅度就會下降。至於延遲改善的幅度，文章提到快取前綴越大，TTFT 的改善越明顯：對於 2,000 到 5,000 token 左右的較小文件，在少量迭代測試中改善可能不具統計顯著性；但超過 10,000 token 的大型快取前綴，TTFT 的降幅就會相當明顯。

🎯 **實務啟示**

如果你的應用有固定的系統提示、參照文件或工具定義,卻在每次呼叫時被當成新內容重新計費，prompt caching 是幾乎零成本就能拿到的最佳化：不用換模型、不用調整 prompt 邏輯，只需要在對的位置插入 cachePoint。特別是 RAG 應用與大量工具定義的 agent 系統，重複處理的 context 佔比通常很高，也就是 prompt caching 帶來效益最明顯的地方。

🔗 **來源**
- 標題：Optimizing cost and latency with Amazon Bedrock prompt caching
- 作者／機構：Daniel Abib（AWS ML）
- 連結：https://aws.amazon.com/blogs/machine-learning/optimizing-cost-and-latency-with-amazon-bedrock-prompt-caching/

#AmazonBedrock #PromptCaching #LLMOps #AWS #ClaudeAPI #CostOptimization #RAG #ConverseAPI #LLMInference #GenerativeAI
