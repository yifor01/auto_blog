---
title: Mistral releases weights for its trillion-parameter AI model, targeting cybersecurity
source: TechCrunch AI
url: https://techcrunch.com/2026/10/29/mistral-releases-weights-for-its-trillion-parameter-ai-model-targeting-cybersecurity/
model: claude-code/sonnet
generated_at: '2026-10-29T22:00:06.356357'
score: 95
---

📌 Mistral 公開兆參數模型「Le Chonk」權重，主打主權資安防禦

TL;DR：Mistral 開源兆參數模型 Mistral Large 4 的權重，讓企業與政府能自行部署資安防禦 AI。

當 OpenAI、Anthropic 等公司把最強模型鎖在自家 API 背後時，法國 AI 公司 Mistral 選擇把一個兆參數模型的權重直接公開下載，而且第一個主打場景就是資安防禦。

🤔 開源與封閉模型陣營的角力，在資安領域格外有說服力

Mistral 這週正式釋出本月初發布的 Mistral Large 4（暱稱「Le Chonk」）模型權重，讓企業與政府可以自行下載並部署這套系統。這是開源陣營與 OpenAI、Anthropic 等封閉模型供應商競爭加劇下的一步，Mistral 的立場是企業與政府不該被迫依賴外部 AI 公司才能取得先進能力。Mistral CEO Arthur Mensch 的說法是，AI 應該「成為賦能的工具,而非支配的工具」。而這個論點在資安場景格外有份量，因為組織本來就更在意對自身資料與系統的控制權。

📊 效能可比 GLM-5.3，但 token 用量少 47%

Mistral 表示 ML4 的效能與中國開源競品 GLM-5.3（此前被視為全球最佳開源模型之一，尤其在資安工作上）相當，但每個任務使用的 token 數量少了 47%，經濟性明顯更好。公司也宣稱，在 Artificial Analysis 的 Coding Agent Index 代理式程式設計任務評測上，ML4 的排名超過所有其他開源模型。模型權重已上架 Hugging Face，並同時提供 API 存取方式。

💡 開源權重的意義：防禦能力「無法被切斷」

Mistral 科學副總裁 Pierre Stock 向 TechCrunch 表示,權重公開意味著企業與政府能擁有「無法被切斷」的前沿智慧存取權，因為模型本身就是開放權重的。他進一步說明，這能讓組織即時識別、協調並應對重大安全事件,而開源也代表企業可以把模型部署在自己的地端生態系統中。對於為什麼要把這種能力開放給所有人,Stock 的解釋是：鑒於部分惡意行為者可能會利用自己的技術發動攻擊，盡快把同等能力提供給所有人,有助於強化整個防禦生態系統。針對近期出現的失控 AI 代理事件,Stock 也坦言這是真實存在的風險，但認為是「可解決的難題」，並呼籲不要過度恐慌。

⚠️ 公開資訊止於定性比較，缺乏完整基準測試數據

這次公告提供的多是相對性說明（與 GLM-5.3 比較、token 用量減少 47%、在特定評測站排名第一），並未附上完整的基準測試分數細節；而開源一個兆參數規模的強力模型本身,也意味著同樣的能力可能被惡意行為者用於攻擊，這點 Stock 自己也承認是需要持續面對的課題。

🎯 想要地端部署資安 AI 的團隊,現在多了一個選項

對於需要在地端環境中運行安全防禦 AI、不想受制於單一雲端 API 供應商的企業與政府機構，ML4 的開源權重提供了另一條路；但在導入前，建議實際驗證其在自身場景下相對於 GLM-5.3 等既有開源模型的效能與 token 成本差異。

🔗 來源
- 標題：Mistral releases weights for its trillion-parameter AI model, targeting cybersecurity
- 作者／機構：Lucas Ropek，TechCrunch AI
- 連結：https://techcrunch.com/2026/10/29/mistral-releases-weights-for-its-trillion-parameter-ai-model-targeting-cybersecurity/

#Mistral #OpenWeightAI #Cybersecurity #LLM #OpenSourceAI #TrillionParameter #AIInfrastructure #OnPremAI #AgenticCoding #SovereignAI
