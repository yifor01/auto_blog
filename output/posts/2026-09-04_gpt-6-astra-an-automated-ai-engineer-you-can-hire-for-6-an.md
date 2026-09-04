---
title: 'GPT-6 Astra: an automated AI Engineer you can hire for <$6 an hour'
source: Latent Space
url: https://www.latent.space/p/astra
model: claude-code/sonnet
generated_at: '2026-09-04T19:43:57.328700'
score: 103
---

📌 【OpenAI 發布】GPT-6 Astra:每小時不到6美元的AI工程師

TL;DR:實測GPT-6 Astra後發現,它不只是聊天模型,而是能獨立跑完整套AI工程流程的agent。

當多數人還在看Astra的Pokemon實況與Blender demo時,Latent Space團隊已經燒掉超過20B tokens,得出一個比跑分更值得注意的結論。

🤔 一款「輕度loop化」的超級模型

GPT-6 Astra是OpenAI首個Stargate、"lightly looped"的超級模型,在多項指標上勝過Fable 5.1,包括完全打穿最難版本的FrontierMath(97.6%)與ARC-AGI-3(99.9%,詳見system card)。多數討論會停留在computer use、玩Pokemon、操作Blender,以及科學與資安基準測試這類典型話題,OpenAI總裁Greg稱「AGI已至」,首席科學家Jakub則說這終於是他期待已久的Automated AI Research Intern。

🧩 它不是在秀跑分,而是在當AI工程師

作者實測後認為,GPT-6 Astra代表一類新模型:能自己選擇並訓練模型、標註資料並把標註結果用於active learning(類似SAM的做法)、讓pipeline保持滿載、儀器化系統並讀log、一次到位地部署與除錯整套系統、同時fan out並指揮/評估多個subagent(包含跑其他模型的agent),還能在數十億token長度的單一agent thread裡維持連貫性。

📊 一個月內,從玩票競賽到取代付費SaaS

過去一個月,團隊從一場名為「Kill My SaaS」的競賽出發,做出了十幾個內部或個人用工具,其中4個是原本要另外付費的SaaS服務;重新設計了個人網站;做出一個雖不完整但能運作的GitHub+Vercel替代品;為一款合法棋步比圍棋多一萬倍的策略棋類遊戲訓練了對弈AI;透過清理個人財務省下數萬美元;還把自己的舊書重新出版,同步做出對齊的有聲書音檔與實體印刷版。作者強調,還有更多更有野心的專案即將發布。

💡 33 tokens/秒,算出來的「時薪」

$6一小時這個數字,來自實測中觀察到的33 tokens/秒生成速度,以及最高每百萬token 50美元的計價方式換算而來。由於Astra比Sol與Fable更省token(此點已由Artificial Analysis獨立驗證),它同時也可能是市面上除了Spark 1.3之外最好的「又快又聰明」的模型組合(前提是預覽版的延遲表現能延續到正式發布)。不過若開到Ultra模式,花費會遠高於這個數字——因為Astra的平行化能力太強,實務上團隊常同時開20到50個agent,由一個主Astra agent統一調度,這基本上就是過去要花$200到$1000一天僱一位初階AI工程師盯pipeline、看資料、抓問題、修正、重跑的工作,現在用大約$100、兩天的Astra運算量就能完成。文章也提到,你甚至可以讓Astra順手幫你做出一個自己的Arena.ai平替,用來調prompt、選模型,或訓練自己的偏好模型。

🎯 實務啟示

作者的結論很直接:OpenAI顯然已經訓練出一個能自動化其自家大部分AI工程工作的模型,而且OpenAI內部本來就在用GPT-6做這件事。對工程師來說,現在該做的不是繼續小心翼翼地寫prompt,而是大幅拉高對Astra、Fable這類模型的期待值,並準備好用「一個主agent指揮數十個subagent」的方式重新設計自己的工作流程。作者也提到正在對Grok、Fable等同期frontier模型做類似測試,認為這篇文章討論的agentic coding模式應該能延伸到2026年底其他frontier模型上。

🔗 來源
- 標題:GPT-6 Astra: an automated AI Engineer you can hire for <$6 an hour
- 作者／機構:Latent Space
- 連結:https://www.latent.space/p/astra

#GPT6Astra #OpenAI #AIEngineer #AgenticAI #LLM #Stargate #AIAgents #FrontierMath #ARCAGI #AIProductivity
