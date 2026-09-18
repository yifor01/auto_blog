---
title: Introducing Kimi K3 on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/introducing-kimi-k3-on-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-09-18T19:52:25.439539'
score: 91
---

📌 2.8兆參數開源模型上線，Kimi K3進駐Amazon Bedrock

TL;DR：Moonshot AI的2.8T參數開源模型Kimi K3登陸Bedrock，支援百萬token與明確prompt快取。

當開源模型的參數規模開始逼近甚至超越部分閉源旗艦模型時,「要不要用開源」已經不再是能力問題,而是部署信任問題。Amazon Bedrock這次把Moonshot AI的Kimi K3納入平臺，某種程度上正是在回應這個問題。

🤔 **開源權重模型正在改變AI部署的成本結構**

隨著開源模型的智慧與效率快速提升,企業能依工作負載挑選最適合的能力、速度與成本組合。AWS這次上線Kimi K3，延續的是自2025年以來持續在Bedrock擴充開源模型陣容的策略——目前已涵蓋DeepSeek、Google、MiniMax、Mistral AI、Moonshot AI、NVIDIA、OpenAI、Qwen等多家提供者的數十款模型，而Bedrock在2026年陸續補上的tool calling、structured output、reasoning、串流回應,以及Responses與Chat Completions API,都是平臺層級的能力,新加入的開源模型可以直接沿用,不必個別重新對接。

🧩 **原生視覺、百萬token context，以及首個支援明確prompt快取的開源模型**

根據Moonshot AI的說法，Kimi K3是其目前最強大的模型,也是首個突破2.8兆參數的開源模型。它結合原生視覺（vision）能力與100萬token的context window，並宣稱相較於前代Kimi K2，在scaling效率上有約2.5倍的提升。這些特性讓它適合需要在大型程式碼庫、長文件與圖片間維持長期上下文的長時間coding與知識工作流程。值得一提的是，Kimi K3是Bedrock上第一個支援explicit prompt caching的開源權重模型——當你在多次呼叫間重複使用同一段上下文（例如repository說明、工具定義或參考文件）時，明確標記可重用的prompt前綴，能讓後續請求命中快取，降低回應延遲與輸入token成本。

在資料安全方面，Bedrock上所有開源權重模型都遵循相同原則：資料處理在AWS資料邊界內完成、不會與模型提供者共享、也不會用於訓練底層模型；推論請求永遠啟用zero data retention，zero operator access則確保連AWS自己的維運人員都無法在推論過程中存取你的prompt與回應內容。

🧩 **兩種跨區域推論設定檔，以及與OpenCode、Hermes Agent的整合**

要試用Kimi K3，最快的方式是打開Bedrock console，進入Test > Playground選擇模型；程式化呼叫則透過bedrock-runtime端點，同時支援OpenAI相容的Responses/Chat Completions API,以及Bedrock自己的Invoke與Converse API。呼叫時需透過跨區域推論設定檔：沒有地區限制需求的話，建議使用global.moonshotai.kimi-k3，它會把每個請求路由到任何支援的商用AWS區域，成本比地理性設定檔低約10%；若有資料落地需求，us.moonshotai.kimi-k3會把處理限定在美國地理範圍內。文中也示範了用OpenAI Python SDK搭配aws-bedrock-token-generator函式庫產生短期bearer token進行驗證，並展示了如何在OpenAI Python API中設定explicit caching。

除了直接呼叫API，Kimi K3也能透過支援Bedrock或OpenAI相容供應商的各類coding agent與框架使用。文中以開源、model-agnostic的coding agent OpenCode為例，說明如何在opencode.json設定檔中配置amazon-bedrock供應商（底層走Converse API），設定完成後用/models指令切換到global.moonshotai.kimi-k3即可開始開發；另一個例子是通用生產力助手Hermes Agent，它可透過桌面應用、常見通訊軟體或終端機使用，原生支援Bedrock上的模型，適合deep research與任務自動化等場景。

⚠️ **細節仍有待補齊之處**

文中提到Hermes目前若要在多組AWS憑證環境下運作，需要設定AWS_PROFILE環境變數或使用預設profile，尚未支援在設定檔中直接指定AWS profile，這點還有一個開放中的issue在追蹤後續支援進度。至於Kimi K3實際效能表現，除了Moonshot AI自身宣稱的2.5倍scaling效率提升外，本文並未提供具體的benchmark分數，讀者評估時仍需自行測試驗證。

🎯 **實務啟示**

對已經在使用Bedrock、又想嘗試超大規模開源模型的團隊來說，Kimi K3的吸引力在於「用開源模型的成本彈性，配上受管服務的資料邊界保證」——不需要自己承擔模型權重的部署與維運，也不用因為使用開源模型就放寬資料安全的要求。若你的工作流程本身就需要長文本與圖片混合輸入，或已經在跨多次呼叫重用相同上下文，explicit prompt caching能直接反映在成本與延遲上，值得優先評估。

🔗 **來源**
- 標題：Introducing Kimi K3 on Amazon Bedrock
- 作者／機構：Alex Thewsey
- 連結：https://aws.amazon.com/blogs/machine-learning/introducing-kimi-k3-on-amazon-bedrock/

#AmazonBedrock #KimiK3 #MoonshotAI #OpenWeightModels #LLM #AWS #PromptCaching #AICoding #CloudAI #GenerativeAI
