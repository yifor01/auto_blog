---
title: Grok 4.7 is now available on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/grok-4-7-is-now-available-on-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-09-28T22:49:17.629174'
score: 80
---

📌 Grok 4.7上架Bedrock，主打耐力而非速度

TL;DR：xAI的Grok 4.7登陸Amazon Bedrock，強項是長時間任務中的自我驗證能力，而非單純比快。

多數frontier model的賣點是「更快」，Grok 4.7反其道而行，它的核心賣點是「肯花更多時間把一件事做對」。這款新模型現在已經進入Amazon Bedrock的模型目錄，鎖定coding、長時間執行的agent與知識工作三大場景。

🤔 **上架Bedrock的定位**

Grok 4.7透過bedrock-runtime端點以跨區域推論設定檔（cross-Region inference profiles）提供服務，支援Responses、Chat Completions與Converse三種API。根據xAI於2026年9月21日發布的Introducing Grok 4.7公告與模型文件，這是xAI目前在coding與知識工作領域最強的模型：它會在困難任務上花更多時間，並在推進下一步之前更仔細地驗證自己的輸出。

🧩 **訓練設計：換取長任務的可靠度**

xAI表示Grok 4.7採用了一個新的、更大的base model，並經過一次更長的強化學習訓練，訓練任務組合刻意偏向需要數小時才能完成的困難問題。這帶來兩個能力上的提升：模型更擅長驗證自己的輸出，也能更有效地利用500K token的長context視窗。xAI還訓練模型原生理解Grok Bot harness，並表示這對對話類任務與一般知識工作有幫助。對於正在打造agent的工程師來說，這種「先自我檢查再繼續」的行為值得留意，因為長軌跡任務中，早期的一個小錯誤往往會隨著每一步逐漸放大，自我驗證能降低這種災難性失敗的機率。

📊 **評測結果與Bedrock整合細節**

xAI公布的評測涵蓋軟體工程（CursorBench、DeepSWE）、多小時的終端機與辦公室任務（Terminal-Bench、AA Briefcase）、電機工程（EEBench）、法律工作（Harvey Legal Agent Benchmark）以及臨床推理（HealthBench Professional），具體數字請見xAI官方公告。另外，Artificial Analysis以自家獨立評測（而非採信廠商公布數字）指出，Grok 4.7在其Intelligence Index綜合評測上有全面提升，最大的進步出現在長時程的agentic知識工作，以及在xAI自家harness中執行的coding agent任務上；評測是在xhigh推理力度下量測的。需要留意的權衡是：這些進步伴隨著大約兩倍的輸出token用量，因此推理力度不該沿用預設值，而應該依任務刻意設定。

💡 **企業級功能與部署選項**

Grok 4.7支援四種可調推理力度：low、medium、high、xhigh。Bedrock提供兩種跨區域推論設定檔：Global設定檔（global.xai.grok-4.7）將請求分散到任一支援的商用AWS區域、定價較低，但對請求實際落地的區域控制較少；US地理設定檔（us.xai.grok-4.7）則將處理侷限在美國境內，適合有資料落地需求或延遲敏感的流量。服務層級也分三種：Standard按token計費無需承諾、Priority提供加價的優先處理、Flex則針對非時間敏感任務提供較低成本選項。企業功能方面，Amazon Bedrock Guardrails可依ID與版本掛載到請求上，套用內容過濾、禁止主題、PII遮蔽等政策；structured outputs可用JSON Schema限制輸出格式方便下游解析；隱式prompt caching會自動套用到重複的prompt前綴，對每輪都重送大型system prompt的agent能省下成本；invocation logging則會把每次呼叫的請求、回應與token數（含推理token）記錄到CloudWatch，作為長時間agent運行的稽核軌跡。

⚠️ **安全性聲稱與限制**

xAI表示Grok 4.7採用全新的safeguard stack，是該公司目前在拒絕有害請求與抵抗jailbreak方面測試過最強的模型，並強調在資安、生物等雙用途（dual-use）領域，目標是同時保持對合法任務有用、又能拒絕危險請求；在資安場景，xAI宣稱模型只會放行極小比例的風險性雙用途提示，同時很少誤擋合法的資安研究工作，並已開始邀請特定資安夥伴使用Grok 4.7的紅隊能力做防禦研究。這些聲稱目前僅來自xAI自身描述，尚待第三方驗證。

🎯 **實務啟示**

若你正在用Bedrock打造agent，移植既有整合可以直接用OpenAI SDK；若想在帳號內所有模型維持一致的訊息格式、並搭配呼叫紀錄與串流回應，則建議用Converse API。無論選哪種路徑，都值得先確認Bedrock控制台中該模型在你要用的區域是否已開通，並依任務難度手動設定reasoning effort，避免預設值帶來不必要的token成本。

🔗 **來源**
- 標題：Grok 4.7 is now available on Amazon Bedrock
- 作者／機構：Suheel Farooq, AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/grok-4-7-is-now-available-on-amazon-bedrock/

#Grok #xAI #AmazonBedrock #AWS #LLM #AgenticAI #CloudAI #ReasoningModels #CodingAgent #MachineLearning
