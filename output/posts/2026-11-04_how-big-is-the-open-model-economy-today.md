---
title: How big is the open model economy today?
source: Interconnects
url: https://www.interconnects.ai/p/how-well-can-we-measure-open-model
model: claude-code/sonnet
generated_at: '2026-11-04T22:54:31.647903'
score: 85
---

📌 開源模型是雜訊,還是真正在長大的市場?

TL;DR：Interconnects 用推理平臺的 token 量拼湊數據,顯示開源模型的 inference 市場正呈近指數成長。

如果你問「開源模型的推理市場到底是不是相對 OpenAI、Anthropic 的一個誤差範圍內的數字」,Nathan Lambert 給出的答案是:目前所有能拿到的數據都不精確,但方向很清楚——這個市場在快速長大。

🤔 **衡量開源模型市場的難處**

Interconnects Dashboard 是 Lambert 長期維護的 agent 測試場,彙整網路上關於開源模型採用與效能的最佳數據。但他坦言,現有的指標大多是「吵雜的平臺指標、帶行銷意味的創業公司數字,以及不完美的公開評測」,需要有經驗的判斷才能看出趨勢方向。他想回答的核心問題是:開源模型的推理市場有在成長嗎?還是相對 OpenAI/Anthropic 根本是個誤差範圍內的數字?

🧩 **用誰當指標:Baseten、Fireworks、Together AI**

他選擇把 Baseten、Fireworks、Together AI 這三家專做開源模型推理的創業公司,以及 OpenRouter API 回報的開源模型 token 佔比,當作市場的風向球,理由是這些公司的命運與「開源模型推理」這個品類的成敗直接綁定。超大規模雲端業者(例如 Amazon Bedrock、Azure 的 model garden)可能也佔有相當份量,但目前沒有看到他們依模型類別拆分使用量的揭露。為了找到對照基準,他進一步拿 Google 在財報中揭露的整體平臺與 API token 量,疊加到這些開源推理平臺的數字上做比較。

📊 **單一垂直就有每天 40 兆 token**

從公開揭露的 token 量(對數尺度)來看,開源模型推理呈現近指數成長,而這波成長在 GLM 5.2 帶動開源 agent 的質變後還出現了進一步的提升。最新的具體數字來自 Fireworks:他們在自家第一次公司大會上宣布,為客戶客製化的模型每天服務超過 40 兆(40T)個 token。這還只是其整體推理業務的「一個垂直」,而且這個垂直從今年夏天以來成長超過兩倍,Lambert 據此推估,Fireworks 今年秋天的總體數字應該會遠超過每天 100 兆 token。

💡 **數據粗糙,但方向重要**

Lambert 自己強調這些是「比較粗糙的研究筆記」,是他正在思考、但尚未有完整證據的內容,而不是成熟的結論。這種坦白本身也提醒讀者:平臺公開的 token 量多半服務於行銷敘事,拿來做精確的市場規模估計要謹慎,但拿來判斷「成長方向」仍然有參考價值。

🎯 **實務啟示**

對於正在評估是否要把工作負載放到開源模型推理平臺上的團隊,這份分析給出的訊號是:這不是一個邊緣市場的小賭注,而是一個有真實規模、且持續在加速成長的基礎設施層。Interconnects Dashboard 本身對所有人免費開放,值得作為追蹤開源模型採用度的長期參考工具。

🔗 **來源**
- 標題：How big is the open model economy today?
- 作者／機構：Nathan Lambert, Interconnects
- 連結：https://www.interconnects.ai/p/how-well-can-we-measure-open-model

#OpenSourceAI #AIInfrastructure #LLMInference #AIEconomy #ModelServing #Fireworks #TogetherAI #Baseten #OpenRouter #AIMarketAnalysis
