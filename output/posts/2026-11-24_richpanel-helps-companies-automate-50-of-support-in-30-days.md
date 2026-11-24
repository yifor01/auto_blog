---
title: Richpanel helps companies automate 50% of support in 30 days
source: OpenAI Blog
url: https://openai.com/business/customer-stories/richpanel-ai-customer-support
model: claude-code/sonnet
generated_at: '2026-11-24T03:25:14.645696'
pinned: true
---

📌 Richpanel 打造「AI 主管」，30 天內讓客服自動化率衝到 50%

TL;DR：Richpanel 用多顆 GPT-6 系列模型分工,讓 AI 客服 30 天內自動化率達 50%,未達標就退費。

人類客服要熟練運用 20、30 種工具才能完成一次服務,而這些操作流程往往從來沒有人寫下來過。當你想讓 AI 接手這份工作,第一個卡關的問題往往不是「AI 夠聰明嗎」,而是「誰來把這些工具和流程教給它」。

🤔 **把「設定 agent」這件事也交給 AI**

Richpanel CEO Amit RG 觀察到,部署一個客服 agent 通常需要有 forward-deployed engineer 去串接客戶系統並定義運作方式,但很多公司根本沒有多餘的工程師可以做這件事。於是他反過來思考:如果這個 forward-deployed engineer 本身就是一個 AI agent 呢?Richpanel 因此打造出一個 AI 管理者,被客戶稱為「Boss AI」,專門負責撰寫程序並定義前線客服 agent、copilot 以及品質把關 agent 該如何呼叫各自需要的工具。

🧩 **分層用模型:準備階段重準確,執行階段重成本**

Richpanel 在打造 Boss AI 時使用 GPT‑6 Astra 和 GPT‑6.1 Sol,優先考量準確度,因為這一層決定了後續所有 agent 要怎麼做事。而真正面對客戶、數量動輒數十萬筆的對話,則交給 GPT‑6 Luna 等模型處理,copilot 與品質把關 agent 也採取相同邏輯。Amit 表示:「重點是在成本與智慧之間取得平衡。」畢竟很多客戶原本就在使用低成本的外包客服,自動化方案必須在財務上站得住腳才有意義。

📊 **300 個部署案,全部達標的 50% 自動化承諾**

截至 2026 年 10 月受訪時,Amit 表示 Richpanel 在過去六個月內已完成約 300 個 AI 客服部署案。公司對客戶的承諾是:30 天內自動化率達到 50%,否則退費;Amit 表示所有這些部署案都達成了這個目標,而且在每一個案例中,AI 的客戶滿意度都勝過人類客服。

💡 **長上下文、長任務,同時維持成本效益**

Amit 將這套分層架構的可行性歸功於 OpenAI 的模型,他提到這些模型能同時處理長上下文、較長時間跨度的任務,又能維持成本效益,讓 Richpanel 可以用推理能力較強的模型去「準備」agent 該怎麼做事,再用較經濟的模型去「執行」實際對話。

🎯 **實務啟示**

Richpanel 的案例示範了一種值得參考的 agent 系統分工思路:用相對昂貴、準確度優先的模型去產生工具定義與操作流程,再用成本效益更高的模型去跑實際的高流量對話。對正在設計多 agent 系統的工程師來說,「設定階段」與「執行階段」用不同層級的模型,可能比單一模型打天下更務實。

🔗 **來源**
- 標題：Richpanel helps companies automate 50% of support in 30 days
- 作者／機構：OpenAI
- 連結：https://openai.com/business/customer-stories/richpanel-ai-customer-support

#OpenAI #Richpanel #AICustomerSupport #GPT6 #AIAgents #CustomerExperience #Startup #APAC #LLMOps #AIAutomation
