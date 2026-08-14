---
title: Writer introduces new AI model and upgraded harness to contain token costs
source: TechCrunch AI
url: https://techcrunch.com/2026/08/13/writer-introduces-new-ai-model-and-upgraded-harness-to-contain-token-costs/
model: claude-code/sonnet
generated_at: '2026-08-14T07:34:30.483418'
score: 71
---

📌 Writer 押注「調 Harness」比「換模型」更能省 token 錢

TL;DR：Writer 發表 Palmyra X6 與新版 harness，宣稱基本任務成本最高可降 50%。

當多數 AI 廠商還在比拚榜單分數時，Writer 選擇正面回答企業最在意的問題：帳單為什麼這麼貴。

🤔 **企業不想再追榜單，只想要成本別再漲**

Writer 是一家提供 AI 工具與 agent 給行銷團隊使用的公司，週四推出新旗艦模型 Palmyra X6，這是在 Z.ai 開源模型 GLM-5.2 基礎上做後訓練（post-training）調整而成的版本。Writer 執行長 May Habib 向 TechCrunch 表示：「企業已經受夠了追逐下一個榜單分數，他們要的是成本能被壓平，而現在似乎沒有人能做到。」

🧩 **兩件事一起做：換模型底座，也重寫 harness**

Writer 宣稱，將 Palmyra X6 與公司自家 harness 基礎架構的調整結合後，能為客戶的基本任務省下最高 50% 的成本。這次除了新模型，公司也同步發布標準 agentic harness 的重大升級，兩者皆自週四起提供給客戶使用。新方法特別著重複雜、多步驟任務，目標是用更少的 token、更快的速度完成執行，Writer 將 harness 最佳化視為達成這個目標的關鍵槓桿。

📊 **內部研究：調 harness 平均省 40% 成本**

Writer 研究人員的一篇論文測試了在多個不同模型上做小幅 harness 效率調整的效果，發現在許多情況下，調整 harness 比選擇模型本身更能穩定降低成本，測試中成本平均下降 40%。研究人員在論文中寫道：「harness 是唯一一個效率能夠乘數放大到組織現在及未來所使用的每一個模型上的元件。」對 Writer 的客戶而言，體驗仍是模型無關（model-agnostic）的：Palmyra X6 可以與 Writer 其他模型並存，也能搭配透過 Azure 或 Amazon Bedrock 導入的外部模型一起使用。

⚠️ **成本數字目前只有廠商自己的說法**

無論是「最高降 50%」或「平均降 40%」，目前都是 Writer 自身的估算與內部研究成果，文中並未提及獨立第三方的驗證。Habib 也把這波降本訴求，連結到企業對大型 AI 實驗室愈來愈不信任的氛圍，她表示：「這裡的成本爆炸對客戶來說是前所未有的，CIO 們對這些實驗室死心的程度也是。」並認為這些實驗室「並不真正理解如何幫助企業從 AI 中獲益」，背後隱含大型實驗室在 token 用量上存在財務誘因的說法，這同樣是 Writer 一方的觀點，尚待市場檢驗。

🎯 **實務啟示**

Writer 這次釋出的訊號值得注意的地方，不在於 Palmyra X6 本身的能力，而在於它把「harness 效率」明確列為與「模型選擇」同等重要的成本槓桿。對正在管理多模型部署的工程團隊而言，與其只盯著換更便宜的底層模型，也可以回頭檢視自己的 agent harness（呼叫次數、prompt 結構、多步驟流程設計）是否還有壓縮 token 用量的空間。

🔗 **來源**
- 標題：Writer introduces new AI model and upgraded harness to contain token costs
- 作者／機構：Russell Brandom，TechCrunch
- 連結：https://techcrunch.com/2026/08/13/writer-introduces-new-ai-model-and-upgraded-harness-to-contain-token-costs/

#Writer #PalmyraX6 #AgentHarness #LLMCost #OpenSourceAI #GLM #EnterpriseAI #TokenEfficiency #AIAgents #ZAI
