---
title: '[AINews] 10% worse, 100x cheaper, 10000x faster: Why Simulation is taking
  over'
source: Latent Space
url: https://www.latent.space/p/ainews-10-worse-100x-cheaper-10000x
model: claude-code/sonnet
generated_at: '2026-08-23T06:15:48.470519'
score: 84
---

📌 差一成、省百倍、快萬倍：AI 正把整條生產鏈模擬化

TL;DR：從裁判、教材到受試者，AI 生產鏈每年都有一環從真人變成模型模擬。

如果你仔細回想過去幾年 AI 圈的每一次「典範轉移」，會發現一個規律：每年總有一個原本必須靠人力完成的環節，被模型接手。不是漸進發生，而是突然翻轉，而且往往能找到那個「patient zero」——第一篇論文、第一個產品，讓合成版本第一次在前沿實驗室裡變得不可或缺。

🤔 **從裁判到受試者，AI 正在吃掉整條生產鏈**

Latent Space 這篇回顧文章提出一個心智模型：把「合成資料」「合成 rubric」「AI researcher」「端到端 RL 環境」這些看似分散的趨勢串起來看，其實都是同一件事在不同層面發生——越來越有野心的人類模擬，效果差個 10%，但成本便宜 100 倍、速度快 10000 倍。

🧩 **第一步：裁判先變成模型**

InstructGPT 建立了現在的標準套路：收集一次人類偏好，訓練出 reward model，讓 policy 對模型優化而不是對人類優化。Constitutional AI 把這個想法推得更遠，讓 AI 依據一組原則自我批評（RLAIF），Lee 等人後續證明 AI 回饋能以極低成本匹配人類回饋的品質。等到 LLM-as-judge 成為 MT-Bench、AlpacaEval 這類評測方法的預設做法時，整套 reward、批評、評估機制已經是模型評判模型。

**第二步：訓練語料也變成模型寫的**

微軟 Phi 系列的論文標題就是論點本身：《Textbooks Are All You Need》。用 LLM 生成的教科書等級資料訓練小模型，效果遠超參數量預期，phi-1.5 證明這不是僥倖。Apple 的 WRAP 把這個做法推廣到整個網路語料的改寫，讓預訓練效率提升約 3 倍。接著整條管線工業化：NVIDIA Nemotron-4 340B 直接把「合成資料生成管線」當作主打功能開源授權，到了 2025 年，由強推理模型生成的推理鏈語料，已成為預訓練與 mid-training 的標準原料。

**第三步：蒸餾把模仿變成一門訓練學科**

ChatGPT API 開放後沒幾週，史丹佛的 Alpaca 就證明用 600 美元的 fine-tune、搭配 GPT 生成的指令，就能複製前沿模型的大半行為。Vicuna 用共享對話資料做同樣的事，Orca 則用豐富的教師解釋而非單純答案。這個技術逐漸成熟為正式訓練學科——on-policy generalized knowledge distillation 解決了訓練與推論不一致的問題——並在 DeepSeek-R1 隨旗艦模型一起釋出一整個蒸餾模型家族時達到文化高峰，「老師就是一個模型」成為此後每個小模型發布的預設假設。

**第四步：模型開始決定自己要學什麼**

Self-Instruct（模型自己寫指令集）與 STaR（模型自我引導推理鏈）都是 2022 年的產物，但真正的翻轉發生在 Meta 的 Self-Rewarding Language Models 與 SPIN 證明模型能自己生成任務、評判自己的輸出，並突破人類偏好資料的天花板。課程設計，這個過去最仰賴 ML 研究者品味的環節，變成模型對自己做的事。

**第五步：發現本身也自動化了**

DeepMind 的 AlphaEvolve 在 2025 年演化出真正新穎的演算法，Sakana 的 AI Scientist（現已登上 Nature）勾勒出完整的論文撰寫管線。文中提到的關鍵時刻是 Karpathy 在 2026 年 3 月的 autoresearch：一個刻意精簡的 ratchet 迴圈，讓一個 coding agent 修改真實的 LLM 訓練設定、跑一個五分鐘實驗，若驗證損失改善就保留變更，整晚重複。他自己的延伸執行堆疊了 700 個實驗、留下 20 個有效改進，把達到 GPT-2 水準所需時間從 2.02 小時縮短到 1.80 小時——是他睡覺時找到的真實、可轉移的程式碼修改。

**第六步：RL 的環境也合成化**

強化學習的擴展瓶頸已從模型本身移到環境：你需要成千上萬個可執行、可驗證、貼近專業真實的任務世界，人力根本來不及手工打造。Z.ai 在 GLM-5.3 的做法是端到端合成環境——研究型 agent 挖掘真實工作模式並轉換成帶隱藏狀態的長時程環境，judge agent 嘗試每個任務確認可解，驗證器在不看參考解答的情況下被合成出來，再用 oracle、no-op、未解狀態等檢查反覆壓力測試，直到二元獎勵可靠到能直接拿來訓練。同一週發表的 Ornith-1.5 則宣稱做到端到端自我改進——模型自己提出任務、自己生成 RL rollout。

📊 **當受試者本身也開始被模擬**

如果裁判、教師、環境都能是模型，那迴圈裡剩下的人類角色就是「受試者」——偏好、行為、需求的來源。這正是 Simile 想取代的層。從 Joon Sung Park 的 Generative Agents（Smallville，2023）到《Generative Agent Simulations of 1,000 People》，用兩小時傳記式訪談建構的數位分身，重現原始受訪者調查與行為反應的準確度，達到人類自己兩週後重現自身反應準確度的 85%。文章指出的難題在於：前沿模型被訓練成 agent 模型，這反而讓它們模擬真人時表現很差，所以 Simile 特地用訪談、交易資料與 Open Science Framework 上已註冊的 RCT 做 post-training，找回人類的偏誤、不一致與因果紋理，並報告了模擬品質的早期 scaling law。

💡 **實驗束縛與智力束縛的分野**

Poolside 的框架把世界的問題分成兩類：智力束縛的問題（靠擴展認知就能解決，很快會被開源權重商品化），以及實驗束縛的問題——「再多聰明的頭腦也無法取代真實世界的實驗回饋，十萬個天才腦袋若沒有濕實驗室也治不好癌症」。生物領域正從另一端推進同樣的邏輯：CZ Biohub 正把 Human Cell Atlas 影像化為虛擬細胞，因為 in silico 大約比 in vivo 便宜且快上千倍，並延伸朝向虛擬免疫系統邁進，Chai、Xaira 與 Lila 的資料中心式實驗室正在填補這條 AI for science 的堆疊。

⚠️ **物理世界是唯一無法被完全合成的一環**

文章本身也點出局限：物理世界是這條管線裡唯一無法被完全合成的部分，只能被逐格壓縮進模型裡。這篇更接近一篇觀點回顧與心智模型整理，而非提出新方法或新實驗，讀者應把它當作理解趨勢的框架，而非具體可落地的技術方案。

🎯 **實務啟示**

如果你在做模型訓練或 agent 系統，值得盤點一下自己的管線裡，哪些環節還停留在「人力生成」階段——裁判、語料、課程設計、RL 環境、甚至使用者研究——這些往往就是下一個會被合成化、成本結構被打掉重來的地方。

🔗 **來源**
- 標題：[AINews] 10% worse, 100x cheaper, 10000x faster: Why Simulation is taking over
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-10-worse-100x-cheaper-10000x

#AI #SyntheticData #RLAIF #MachineLearning #LLM #AIResearch #SelfImprovement #AgenticAI #FrontierAI #Simulation
