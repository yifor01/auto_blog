---
title: Cut self-hosted LLM cost and latency with the distributed KV caching agent
  skill
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/cut-self-hosted-llm-cost-and-latency-with-the-distributed-kv-caching-agent-skill/
model: claude-code/sonnet
generated_at: '2026-11-21T22:15:45.478282'
score: 100
---

📌 用一個 Agent Skill，把自架 LLM 的首字延遲砍掉八成

TL;DR：AWS 推出分散式 KV 快取 Agent Skill，讓 coding agent 直接診斷、估算並部署共享快取，號稱可省四成推論成本。

律師中午休息回來，回到同一個對話串，結果 LLM 整整花了 13 秒才吐出第一個字。問題不是模型變笨了，而是 GPU 把幾十萬 token 的歷史對話全部重算了一遍。這種「冷 prefill」的痛點，在自架 LLM 的世界裡幾乎是常態，而 AWS 這次把解法包成了一個可以直接對話操作的 Agent Skill。

🤔 **自架 LLM 省下的錢，都拿去重算 KV 了**

客戶自己架 LLM 到 GPU 上，圖的是成本、準確度與延遲的控制權。但自架常常意味著要為重複的 GPU 運算付錢：每臺伺服器各自維護一份小型、彼此不共享的快取，撐不住 AI agent 與聊天應用程式不斷重送的、愈長愈長的上下文。文中舉的例子是一個會累積數十萬 token 案件歷史的法律 AI 助理，請求落到某臺 GPU 伺服器時，那臺伺服器的記憶體裡完全沒有這段歷史，於是必須重新計算所有 token 的 key-value（KV）attention 狀態，也就是 prefill，才能開始回答。同樣的模式也會拖慢重新接續的 coding agent、agentic AI 助理與文件問答系統。AWS 表示，用 Amazon ElastiCache 做分散式 KV 快取，最多可以把自架 LLM 推論成本降低 40%，把首字時間（TTFT）降低 80%。

🧩 **讓 coding agent 自己診斷、估算、動手部署**

這個分散式 KV 快取技能被收進 AWS 的 Agent Toolkit，支援 Kiro、Claude Code、OpenAI Codex 等支援 Agent Skills 的 coding agent。文中示範了四段對話:

- **診斷慢首字**：在 vLLM 的 p5 機群上跑 64K-token 上下文的法律助理，回頭對話首字要 13 秒。Agent 先排除不需要新架構的修法，例如確認是否關掉了 prefix caching，或 GPU prefix cache 命中率是否已經超過 90%（若已經很高，可能根本不需要共享快取）；接著指出法律場景的特殊限制:共享 KV 快取可能讓一個租戶從回應時間推測另一個租戶是否送過相同文字，所以必須隔離的案件要分開建快取，共享快取的租戶則要在 KV hash 中加入自己的 ID；最後它不會憑空猜容量,而是反問模型與 TP size、KV 資料型別、副本數與路由方式、使用者輪次間隔等資訊。
- **估算規模與價格**：針對一組 8 臺 p5、處理 64,000-token 提示的多輪 RAG 助理，agent 查詢 GPU 與快取節點價格,推算出 prefill 速率與 KV 大小,最終建議兩個 `cache.i8ge.48xlarge` 節點。由於沒有提供快取命中率（即能被快取服務、省下重算的 token 比例），agent 改為列出情境並建議先跑 KVTrace 來實測。KVTrace 會記錄 vLLM 或 SGLang 的 KV cache 事件,離線重播到不同容量的共享 KV 快取上做模擬；記錄器不會寫入 token ID 或提示文字,只保留區塊雜湊與 token 數量,若提示內容敏感可加上 `--anonymize-key-file`。報告會建議能拿到九成節省效果的最小容量。
- **從零開始部署**：agent 會先請求確認可用區、建議的節點數與估算價格,獲準後才建立含 EFA 權限的安全群組,以及使用自訂參數群組（含快取逐出策略）的 Valkey 9.1 叢集。LMCache 取得獨立的快取使用者帳號,密碼存進 AWS Secrets Manager,接著在每臺 GPU 伺服器上啟動一個 LMCache 伺服器,並用小型測試物件確認重複的提示能透過 RDMA 從快取載入 KV 狀態。
- **排錯**：當 LMCache 連上 ElastiCache、`BLOB.RDMA_HELLO` 成功，但實際資料傳輸卻失敗，`rdma_write_errors` 持續攀升時,agent 依照技能內建的排錯指引推斷出可能是安全群組擋掉了自身成員之間的 EFA 流量,並給出檢查與修正指令。

📊 **效益取決於工作負載，而非固定值**

文中強調,實際效益跟所使用的 LLM 模型、使用者流量模式與提示路由方式密切相關,很難單憑經驗估算,這也是 KVTrace 存在的原因:在不部署任何基礎設施、不額外收費的前提下,先用自己的模型與流量跑出接近真實的估算值。文章也提醒,省下的 GPU 時間要真正轉換成成本節省,前提是因此跑更少臺伺服器,或在同樣的伺服器上服務更多流量。

🎯 **實務啟示**

如果你的自架 LLM 服務有長對話、多輪 agent 或重複造訪同一上下文的場景，這類分散式 KV 快取值得納入評估清單；更值得注意的是，AWS 把「診斷 → 估算 → 部署 → 排錯」整個流程包裝成 coding agent 可直接操作的技能，這代表基礎設施層的最佳化工作，正在逐步變成可以對話驅動、而不必從頭查文件的流程。

🔗 **來源**
- 標題：Cut self-hosted LLM cost and latency with the distributed KV caching agent skill
- 作者／機構：Ravi Yadav（AWS Machine Learning Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/cut-self-hosted-llm-cost-and-latency-with-the-distributed-kv-caching-agent-skill/

#LLMInference #KVCache #AWS #ElastiCache #SelfHostedLLM #AgentSkills #vLLM #InferenceOptimization #GPUCost #RAG
