---
title: Amazon releases its own Jev clone as decision models flood the web
source: TechCrunch AI
url: https://techcrunch.com/2026/10/01/amazon-releases-its-own-jev-clone-as-decision-models-flood-the-web/
model: claude-code/sonnet
generated_at: '2026-10-01T22:02:28.280357'
score: 95
---

📌 Amazon 也做了自己的 Jev：決策模型開源潮正式開打

TL;DR：AWS 開源輕量決策模型 Strands Decider 2B，讓 agent 工作流程不用每一步都動用大型 LLM。

當大家還在比拚誰的前沿模型更聰明時，另一條戰線悄悄打開了：不是更聰明的模型，而是更「專精」的模型。Amazon Web Services 這週釋出開源決策模型 Strands Decider 2B，靈感來自新創公司 TypeSafe 的 Jev，而同一週 OpenAI 也宣布了類似的產品。

🤔 **為什麼需要「決策模型」而不是通用 LLM**

AI 開發者愈來愈發現，許多電腦自動化場景其實不需要一個完整的前沿 LLM。Strands Decider 2B 的定位很明確：在預先定義好的選項之間快速做出選擇，並附上一個信心分數，告訴你模型對這個選擇有多確定。它完全開源、現在就能下載使用，而且體積小到可以在本機端執行。

這個專案的起點是 AWS 傑出工程師 Marc Brooker 看到 Jev 之後，自己動手做的一個業餘版本。這個「車庫專案」做得夠好，一度登上同量級模型的 Jevbench 排行榜榜首，後來才被 Amazon 工程團隊整理、以 Strands Labs（AWS 內部開發 AI agent 部署工具與協定的團隊）名義正式釋出。

🧩 **架構：借用 LLM 的「軀幹」，輸出改成校準過的選擇**

Brooker 表示，這類模型的需求是在與 AWS 客戶的對話中浮現的：客戶的 agentic 工作流程並不是每一步都需要完整 LLM 的能力或成本。他形容這類模型「是工作流程中一個步驟的完美決策者——根據我現在所在的位置，下一步該做什麼」，並指出它能提供「一個可以被結構化得更可靠的工作流程步驟，因為有信心分數、因為答案範圍是封閉的，延遲更低、成本也可能更低」。

和其他決策模型一樣，Strands Decider 是建立在 LLM 的「軀幹」之上，這次用的是 Qwen3.5-2B，但輸出的不是生成文字，而是經過校準的選擇結果。TypeSafe 把自家模型取名為 Jev，典故來自經濟學家 William Stanley Jevons，呼應他「某項東西的成本下降反而可能帶動需求上升」的理論——用在這裡，指的就是運算智慧的成本下降。

💡 **這股風潮能走多遠？兩方看法不同**

自 TypeSafe 推出這個概念之後，已經有數十個類似模型由不同研究者做出來，顯示市場興趣濃厚，但也讓人好奇這類模型究竟能創造多少實際價值。Brooker 認為真正的挑戰在於：要在不犧牲模型對不同語言、知識理解能力（也就是它之所以通用、好用的原因）的前提下，把準確率與校準度這類「快速決策」能力推到極致，這中間需要非常謹慎地拿捏平衡。他也不認為前沿實驗室會主導這個市場，理由是這類較小的市場裡，做出一個有意思的東西成本可能只要幾百到幾千美元。

不過 TypeSafe 的執行長暨創辦人 Diogo Almeida 持保留態度。他表示：「我理解大家覺得這是一波淘金熱，但他們可能低估了把模型真正做聰明的難度」，並認為目前還沒有真正的競爭對手出現，形容現在這批跟進者「比較像是 ML 工程師想實作一個酷炫的架構，而不是一個真正致力於讓智慧變得有用的團隊」。

🎯 **實務啟示**

如果你的 agent 工作流程裡有大量「在封閉選項中做下一步決策」的步驟，與其每次都呼叫完整的前沿 LLM，評估像 Strands Decider 這類專精決策模型可能可以同時降低延遲與成本，並透過內建的信心分數讓流程更容易做可靠性把關。但正如 Brooker 所說，這類模型的通用知識與語言理解能力會是取捨重點，導入前值得先確認你的場景是否真的落在「封閉選項決策」這個甜蜜點上。

🔗 **來源**
- 標題：Amazon releases its own Jev clone as decision models flood the web
- 作者／機構：Tim Fernholz, TechCrunch AI
- 連結：https://techcrunch.com/2026/10/01/amazon-releases-its-own-jev-clone-as-decision-models-flood-the-web/

#AWS #StrandsDecider #AIAgents #OpenSourceAI #DecisionModels #Qwen #AgenticWorkflows #EdgeAI #MachineLearning #AICompute
