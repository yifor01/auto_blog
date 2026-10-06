---
title: Introducing Mistral Large 4
source: Mistral AI
url: https://mistral.ai/news/mistral-large-4/
model: claude-code/sonnet
generated_at: '2026-10-06T21:47:55.000184'
pinned: true
---

📌 Mistral Large 4 登場:1 兆參數開放權重模型,挑戰封閉模型的攻防與多模態能力

TL;DR:Mistral 推出 1 兆參數、49 億啟用參數的多模態模型 Large 4,在網路安全與多項 agentic 任務上逼近甚至超越部分頂尖封閉模型。

🎣 當多數頂尖封閉模型在面對漏洞重現測試時選擇直接拒答,一個開放權重模型反而拿下全場最高分。這正是 Mistral 最新發布的 Large 4(暱稱 le Chonk)在網路安全評測中呈現的畫面——Mistral 稱其為目前最大、最強的自研模型。

🤔 開放權重模型追上前沿的下一步

Mistral 表示,ML4 是一個原生多模態(natively multimodal)模型,總參數規模達 1 兆,實際啟用參數為 49 億,是 Mistral 目前最大且最強的模型,且仍在快速迭代改進中。Mistral 強調,ML4 已達到全球最強開源模型的水準,並大幅領先任何美國或歐洲開發的開放權重模型;在網路安全、金融、法律等關鍵企業應用上,更被稱為開放模型中的最先進水準。

🧩 在歐洲自建基礎設施上訓練

ML4 是在 Mistral 位於歐洲自有資料中心的 3,800 張 NVIDIA Grace Blackwell GPU 上從零訓練而成,公開預覽版本也運行於同一套基礎設施上。Mistral 將其定位為「在歐洲打造,為 AI 主權而生」的里程碑,部署將涵蓋多個地區,其中歐洲部署由 Mistral 端到端自行營運,獨立於其他數位服務供應商,並受歐洲法律規範。訓練資料中有相當比例為多語言內容,涵蓋超過 160 種語言,包括歐盟所有官方語言。此外,ML4 使用的訓練、客製化與強化學習環境,與 Mistral Forge 提供給客戶的環境相同。Mistral 表示權重將於本月底釋出,目前正與資安領域人士、受驗證的合作夥伴及國家機構進行實際場景的紅隊測試,這些對象將取得降低審核限制、具更強網路安全能力的同一模型版本。

📊 跨領域的評測成績單

**程式碼與 agentic 能力**

| 評測 | ML4 分數 | 備註 |
|---|---|---|
| DeepSWE v1.1 | 61.7% | |
| SWE-Atlas-QnA | 59.4% | |
| Terminal-Bench 4 | 28.3% | |
| Coding Agent Index(綜合) | 49.8% | 領先 DeepSeek V4 Pro 0813 與 Qwen3.8 Max |

Mistral 另外透過 Surge AI 進行盲測人工評分(1–5 分,模型身分隱藏),ML4 Preview 拿下 3.74 分,在五個模型中排名第二,領先 Kimi K3(3.59)、GLM-5.3(3.60)、GLM-5.2(3.40),僅次於 Claude Opus 5(4.22)。

**網路安全**

在 Artificial Analysis Cyber Index(獨立評估模型找出並修補真實軟體安全漏洞能力的指標)上,ML4 位列全球前五,並大幅領先中國以外開發的開放權重模型。在其中一項「重現真實漏洞並修補」的測試中,ML4 拿下 82% 的分數,為所有模型中最高;在由 40 道資安競賽題組成的 Cybench 測試中,解出 93%,是開放權重模型中最高分之一。Mistral 特別指出,Claude Opus 5.5 與 GPT-6 Astra 在同一測試中得分接近零,原因是這些模型會拒絕執行該任務。

**Agentic workflows**

在涵蓋 Gmail、Google Sheets、Slack、Salesforce 等應用的 657 個商業工作流評測 AutomationBench 上,ML4 拿下 59.9%,領先 Kimi K3、MiMo-V2.6-Pro 與 DeepSeek V4 Pro。在評估長流程知識工作的 AA-Briefcase 上,ML4 達到 1,393 Elo,領先 DeepSeek V4 Pro。

**多模態與視覺定位**

在視覺定位(visual grounding)測試 Dense 200 上,ML4 拿下 42%,略勝 GPT-6-Astra 的 41%。Mistral 表示 ML4 能結合視覺定位與 agentic 能力,應用於檢視工程圖、巨量衛星影像判讀等場景。在 SciCode-Verified 評測上,Mistral 稱 ML4 是開放權重模型中的最先進水準。

💡 安全防護的另一種路線

值得注意的是,Mistral 將 ML4 在網路安全上的高分,直接對照封閉模型因安全防護機制而拒答的現象,並指出威脅行為者正日益透過越獄(jailbreak)手段讓封閉模型執行攻擊性任務,因此防禦者需要能力對等、不受相同拒答限制的系統。ML4 搭配開放權重與自行部署能力,讓組織可在自有政策下運行進階安全工作,這也是 Mistral 強調「主權 AI」路線與多數封閉模型供應商的根本差異所在。

⚠️ 目前仍是預覽階段

目前僅開放 Mistral Studio 上的預覽 API 可試用,完整權重要等到本月底才會釋出;在此之前,模型仍在與資安領域人士及合作夥伴進行紅隊測試。架構細節、更多基準測試與後訓練方法,Mistral 表示會在權重釋出前後陸續公布,目前仍有不少技術細節尚未揭露。

🎯 實務啟示

對需要在地端或私有雲部署、且重視資料主權與稽核能力的資安團隊和企業而言,ML4 展示了開放權重模型在攻防能力上追上甚至超越部分封閉模型的可能性。對一般工程團隊來說,其在 agentic coding 與商業工作流自動化上的分數,也值得在評估開源模型選項時納入對照。

🔗 來源
- 標題:Introducing Mistral Large 4
- 作者/機構:Mistral
- 連結:https://mistral.ai/news/mistral-large-4/

#MistralAI #MistralLarge4 #OpenWeights #LLM #Cybersecurity #AgenticAI #Multimodal #AISovereignty #CodingAgent #OpenSourceAI
