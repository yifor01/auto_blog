---
title: Introducing GLM 5.3 on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/introducing-glm-5-3-on-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-10-06T22:03:44.810979'
score: 78
---

📌 GLM 5.3 登上 Amazon Bedrock,原廠主打 cyber security 能力

TL;DR:Z.ai 的 753B MoE 模型 GLM 5.3 現已在 Amazon Bedrock 全託管提供,AWS 也示範拿它跑開源滲透測試 agent Strix。

重構整個 repo、撐過數小時不中斷的 agentic workflow、在每一步工具呼叫中維持推理正確,這些對模型的要求已經不是「答得對」就夠了。過去想用開源權重模型做到這些,代表你得自己採購與維運推論基礎設施。現在,Z.ai(Zhipu AI)的 GLM 5.3 可以直接在 Amazon Bedrock 上用,不用管任何底層基礎設施。

🧩 模型規格與存取方式

GLM 5.3 在 Hugging Face Hub 上公開發布,是一個 753B 參數的 mixture-of-experts 模型,針對 coding 與長時間 agentic 任務最佳化。Z.ai 宣稱這個模型展現出不錯的 cyber security 能力。在 Bedrock 上,GLM 5.3 支援跨 Region 推論、prompt caching、service tiers,目前開放給符合資格的企業客戶使用。呼叫方式支援 OpenAI 相容的 Responses API 與 Chat Completions API,也支援 Bedrock 原生的 Invoke 與 Converse API;AWS 建議新專案優先用 OpenAI 相容 API,因為支援的功能較完整,並建議用短效憑證(例如透過 aws-bedrock-token-generator 從 AWS CLI 憑證產生短期 token)取代長效的 API key。

📊 Prompt caching:省掉重複上下文的成本

長時間的 coding 與知識型 workflow 常常在多輪對話間重送固定內容,例如 system prompt、工具定義或 repo 檔案。GLM 5.3 在 Bedrock 上預設支援隱性(implicit)prompt caching,降低重複呼叫的延遲與輸入 token 成本;若用顯性(explicit)模式明確標出可重用的 prompt 前綴,還能進一步提高 cache 命中率。

🧩 實戰演練:用 GLM 5.3 跑 Strix 做滲透測試

文章示範的應用場景是自動化安全測試:Strix 是一套開源 AI 滲透測試 agent,會動態執行你的程式碼、找出漏洞,並用 proof-of-concept 驗證。截至發文當下,Strix 官方文件把 GLM 5.3 設為預設模型,你可以改設定讓 Strix 改用 Bedrock 上的 GLM 5.3,讓模型推論跑在自己 AWS 帳戶的控管範圍內。範例的測試目標是 OWASP Juice Shop,一個刻意留有漏洞的練習用應用程式,在本機執行。AWS 特別提醒:只能測試自己擁有或已取得書面授權的系統,未經授權的安全測試在多數司法管轄區屬違法行為,也違反 AWS 可接受使用政策。Strix 會啟動一組子 agent 分頭繪製攻擊面、探索各類潛在漏洞,並嘗試用實際可行的 PoC 驗證每個發現,藉此減少人工篩掉偽陽性的時間;測試完成後會產出報告,列出每個發現的嚴重程度、證據與修復建議。對於想要更大規模、持續性安全測試的團隊,AWS 另外提供 AWS Continuum 這個隨選的滲透測試託管服務,兩者可以互補:開源 agent 讓開發者能在本機建置版本上做深度客製化測試,AWS Continuum 則負責規模化的託管評估。

💡 延續 GLM 5 的脈絡

GLM 5 今年早些時候就已上架 Bedrock,GLM 5.3 延續同一系列,文中提到帶來「一系列重要進展」,但具體細節未在本文展開。

🎯 實務啟示

如果你的團隊已經在用開源權重模型做 coding agent,GLM 5.3 上 Bedrock 的意義在於拿掉自架推論的維運成本,同時保留模型選擇的彈性;pay-per-token、沒有常駐資源的計價方式,很適合拿來做像 Strix 這種偶發性但運算密集的安全測試工作。但這仍是「現有模型搬上雲端」的整合型公告,評估時應該聚焦在你實際工作負載下的延遲、cache 命中率與費用,而不是把它當成全新的模型能力突破。

🔗 來源
- 標題:Introducing GLM 5.3 on Amazon Bedrock
- 作者/機構:Alex Thewsey(AWS ML Blog)
- 連結:https://aws.amazon.com/blogs/machine-learning/introducing-glm-5-3-on-amazon-bedrock/

#AmazonBedrock #GLM53 #ZhipuAI #AWS #OpenWeightModel #AIAgent #PenetrationTesting #Cybersecurity #PromptCaching #MoE
