---
title: Adaptive agentic intelligence framework using Strands Agents
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/adaptive-agentic-intelligence-framework-using-strands-agents/
model: claude-code/sonnet
generated_at: '2026-10-22T20:52:29.218090'
score: 91
---

📌 不是每個請求都該丟給大模型：Strands Agents 打造的分層 Agent 架構

TL;DR：AAIF 用小模型分流，複雜請求才轉交雲端大模型處理。

查個裝置狀態也要跨網路打一次雲端大型LLM,這是許多agent系統的現狀。AAIF反過來想:先讓本地的小模型判斷這個請求到底需不需要大模型。

🤔 一個模型打天下的代價

許多組織在打造AI agent時,不管是常規狀態查詢還是複雜分析,所有請求通常都被丟給同一個大型、昂貴的模型處理。這種一視同仁的做法會拉高API成本、帶來不可預期的延遲,也讓offline運作變得不可能:就連本來可以在地端解決的常規查詢,最後也得完整跑一趟網路往返雲端LLM。

🧩 三層架構,建立在一個明確的研究立場上

Adaptive Agentic Intelligence Framework(AAIF)建立在Strands Agents之上,不把所有請求丟給單一大模型,而是用small language model(SLM)在地端處理常規任務,較複雜的請求才透過Amazon Bedrock轉交雲端模型。這個做法承接NVIDIA Belcak等人的研究立場:他們主張SLM對agentic系統裡的許多呼叫來說,已經足夠強大、本質上更合適,而且必然更經濟。

AAIF把AI處理分成三層:智慧分流、本地處理、雲端處理。架構核心是一個Strands agent,連接一個Ollama runtime,裡面同時跑著1B參數的orchestrator模型和一個vision模型。agent對外暴露三個工具:get_device_telemetry讀取本地感測器資料,analyze_camera_feed用llama3.2-vision做裝置端視覺分析,get_expert_insights透過boto3呼叫Amazon Bedrock做複雜分析。使用者請求先流經SLM orchestrator,由它判斷任務複雜度,再分派到本地工具或雲端endpoint。

Strands Agents用@tool裝飾器定義agent能呼叫的能力。llama3.2-vision完全在本地硬體上執行,意味著敏感的攝影機畫面不會離開裝置;get_expert_insights只有在orchestrator判定本地模型處理不了時才會被呼叫;整個routing是透過模型對請求的理解完成的,沒有寫死的關鍵字比對規則。

這個架構會依部署限制調整,不需要重構整套infra:可以跑在像Raspberry Pi(8GB記憶體)這樣的邊緣裝置上,可以是全雲端部署(所有推論都打Amazon Bedrock),也可以是混合設定。彈性來自把routing邏輯(SLM orchestrator)和處理工具分開,兩者能依硬體與網路條件各自替換。

💡 三種部署設定可以怎麼調

全雲端設定把Ollama換成Amazon Bedrock處理所有請求,拿到自動擴展但不需要本地GPU資源,適合有穩定低延遲連線、沒有資料落地限制的團隊。混合設定是本文示範的預設組態,保留本地SLM orchestrator,同時加上雲端模型處理超出本地能力的請求,適合大多數請求夠常規可以在地端解決、但少數需要大模型更深推理的環境;文章指出成本節省來自大約80%不會打到付費API endpoint的流量。全氣隔或嚴格資料主權的場景,則把雲端工具換成更大的本地模型,全部在裝置上處理:一個3B參數模型在記憶體足夠的硬體上,可以處理原本1B orchestrator會升級轉交的中等複雜任務,代價是最難問題的推理深度會打折,好處是資料完全不離開場內。

🧩 走向正式環境:用 MCP 把工具分散出去

本文的實作把工具直接定義在agent程式碼裡。正式環境若有多個agent要共享工具,可以把這些工具包成Model Context Protocol(MCP) server,提供標準化的工具發現與呼叫介面,集中管理並跨agent、跨環境重複使用。範例的分散式架構是:Device 1作為orchestrating hub,跑著Strands agent的SLM router和本地telemetry工具;透過MCP連到Device 2,它跑著搭載llama3.2-vision的edge vision處理伺服器;Device 3則連到Amazon Bedrock,擔任雲端分析閘道。從orchestrator的角度看,所有遠端工具都像本地function call一樣,因為MCP傳輸層會透明處理序列化和網路通訊。

⚠️ 限制

走到production前要補上責任AI控制機制,因為雲端推論路徑會帶著tool輸出、檢索到的資料和使用者輸入。可以把Amazon Bedrock Guardrails用guardrail ID和版本掛到Strands的BedrockModel上,套用有害內容過濾、prompt injection過濾,以及不受來源資料支撐就擋下回應的contextual grounding檢查;要在本地SLM層套用同樣政策,得另外呼叫獨立的ApplyGuardrail API。

🎯 實務啟示

如果agent系統裡大部分請求其實都很常規,先用小模型做分流判斷,再決定要不要升級到雲端大模型,可能是比全部打大模型更務實的成本結構。這個模式特別適合IoT、邊緣場景,也適合逐步從單機demo演化成多裝置透過MCP分工的正式架構。

🔗 來源
- 標題：Adaptive agentic intelligence framework using Strands Agents
- 作者／機構：Nitin Eusebius, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/adaptive-agentic-intelligence-framework-using-strands-agents/

#StrandsAgents #AIAgents #SmallLanguageModels #AmazonBedrock #EdgeAI #MultiAgent #AWS #Ollama #MCP #AgenticAI
