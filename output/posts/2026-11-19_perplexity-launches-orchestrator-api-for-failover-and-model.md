---
title: Perplexity Launches Orchestrator API for Failover and Model Routing
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/19/perplexity-orchestrator-api-failover-model-routing/
model: claude-code/sonnet
generated_at: '2026-11-19T23:52:26.067756'
score: 84
---

📌 Perplexity Orchestrator API：一個端點串起85個以上模型

TL;DR：Perplexity推出單一端點的Orchestrator API，自動做provider failover與模型路由，統一一張帳單結算。

🎣 **半夜provider掛掉，誰來接手？**

多模型整合最麻煩的不是挑模型，而是每個provider各自一套金鑰、各自一套SLA，一旦其中一家半夜出事，整條pipeline就跟著斷線。Perplexity這次把「選模型」和「選誰來serve」拆成兩件事，交給同一個API處理。

🤔 **一個base URL，背後是85個以上模型**

Perplexity Orchestrator API是一個託管的推理gateway，用同一個base URL serving多個模型：涵蓋OpenAI、Anthropic、Google、xAI的前沿模型，也serving像GLM、Kimi、DeepSeek這類開源權重模型，由Perplexity自己或推理夥伴代管。它接受OpenAI Chat Completions、OpenAI Responses、Anthropic Messages三種請求格式，多數團隊只需要換掉API金鑰與base URL：OpenAI SDK對應`https://api.perplexity.ai/orchestrator/v1`，Anthropic SDK則對應`https://api.perplexity.ai/orchestrator`（沒有`/v1`）。Perplexity內部本身就是用這一層，橫跨85個以上模型與十幾家provider在跑。

🧩 **Failover換的是部署，不是模型**

Failover機制會固定模型本身，只換掉背後的部署來源：例如一個打到Anthropic失敗的Claude請求，可以轉由AWS Bedrock接手serve。文件寫明開發者不能自己指定要用哪個部署，這個決策完全交給Orchestrator。

路由功能目前是preview階段：把model設為`perplexity/auto`，再傳入一個routing物件，裡面有一個default_model與1到5條route（各自有name、description、model）。負責判斷的decision model只會讀取對話內容與route描述，看不到route名稱或模型ID；如果沒有任何route符合，或decision model失敗、逾時，就會由default model回答，帶有媒體輸入的請求也一樣走default model。回應header會回報`x-perplexity-autoroute-outcome`、`-route`、`-confidence`三個欄位。預設路由策略會把流量送到GPT-6.1 Sol，簡單請求則送往GPT-6 Luna；另外還有內建的Lower cost、Balanced、Higher quality三種設定檔，以及一個preview階段的Auto effort模式。

📊 **成功率沒給百分比，速度數字倒是給了**

Perplexity量測了2026年10月4日到11月2日的生產流量，結論是：透過Perplexity打出去的Claude與GPT請求，成功率比直接打任何單一provider都更高；在provider發生事故期間，每日成功率的波動也更小。文章沒有公開具體百分比。

速度方面則因provider而異：以Claude Opus 5.5為例，30天裡Anthropic自家最快的天數有15天，AWS Bedrock最快的天數同樣是15天；而GPT-5.6 Sol在Azure上的中位數輸出速度比OpenAI自家高27%。文件也承認，依速度動態路由的功能還在開發中。

路由功能的一個測試案例：在Claude Code中跑Terminal-Bench 4.1的63個任務子集，搭配security、biology、after_refusal三條route。由於Anthropic文件指出Claude Fable 5.2的安全機制有時會擋下無害的安全研究或生命科學任務，用路由分流後多完成了3個任務，但單任務估計成本也更高。Perplexity自己稱這是「調整後的比較」，結果會依工作負載不同而變化。

💡 **計費邏輯：failover不加價**

每個請求都按照實際回答的那個模型公開的每token費率計費，failover到別的部署不會改變費率；Perplexity強調在credit之上沒有額外的平臺費用。舉例來說，`perplexity/glm-5.3`的費率是每百萬token輸入1.4美元、輸出4.4美元、cache讀取0.26美元。用量從預付的Perplexity API credit扣款，這些credit也可以透過AWS Marketplace購買，存取權限則依累積購買的credit量分級。

⚠️ **幾個還在打磨中的部分**

速度感知路由還在進行中；成功率提升沒有具體百分比可供驗證；decision model本身也可能失敗或逾時；Terminal-Bench的比較結果被官方自己標註為「調整後」，不代表所有工作負載都能複製。

🎯 **實務啟示**

對已經在多個模型provider間切換的團隊，這類orchestrator型API能省掉維護多套SDK、多張帳單的成本，但failover的部署選擇權不在開發者手上，遇到延遲或行為敏感的場景（如文中的security/biology案例），可能還是需要自訂route來避免誤判或非預期的拒答。

🔗 **來源**
- 標題：Perplexity Launches Orchestrator API for Failover and Model Routing
- 作者／機構：Michal Sutter，MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/19/perplexity-orchestrator-api-failover-model-routing/

#Perplexity #LLMRouting #APIGateway #Failover #MultiModel #LLMOps #Anthropic #OpenAI #InferenceInfra #AIEngineering
