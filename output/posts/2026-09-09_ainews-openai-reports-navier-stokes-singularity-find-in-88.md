---
title: '[AINews] OpenAI reports Navier-Stokes singularity find in 88 hours using Astra-next,
  roughly 10,000 agents and 130B tokens (>$40M), a contender for second ever Millennium
  Prize awarded'
source: Latent Space
url: https://www.latent.space/p/ainews-openai-reports-navier-stokes
model: claude-code/sonnet
generated_at: '2026-09-09T20:01:24.913158'
score: 97
---

📌 OpenAI稱萬人代理88小時「攻克」Navier-Stokes,但證據只有推文

TL;DR：OpenAI相關人士稱以萬人規模agent協作解出Navier-Stokes問題,但論文、證明稿與驗證細節全數缺席。

如果有人告訴你,一個困擾數學界超過一世紀的千禧年大獎難題,被一萬個AI agent在幾天內「順手」解決了,你會先鼓掌還是先皺眉?過去這兩天,AI圈就在這兩種反應之間反覆拉扯。

🤔 **一場只有推文、沒有論文的「重大突破」**

事件的起點,是OpenAI員工Ethan Knight在推文中表示,「Navier-Stokes的解答,是約一萬個agent協同合作的結果」,並補充OpenAI過去一年都在訓練模型透過「multiagent RL(多代理強化學習)」進行協作,認為困難問題有機會靠「大量非結構化的平行測試時運算(test-time compute)」來解決,讓模型自行決定如何組織分工。多位觀察者將此解讀為OpenAI宣稱針對Navier-Stokes千禧年問題中的「有限時間奇異點(finite-time singularity)/blow-up」給出了結果,其中一則帶有諷刺意味的轉述提到「一萬個agent」與「88小時」等細節,但同時也承認數學界的正式承認仍只是「minor formality」。

需要特別指出的是,根據素材本身的分析,「88小時」這個廣為流傳的數字,只出現在諷刺性的貼文中,並未見於較直接的OpenAI相關陳述,因此不應被當作已證實的事實。

🧩 **揭露的其實是系統架構,而非數學證明**

從公開推文能確認的技術輪廓,其實更偏向研究系統設計,而非流體力學本身:
- 規模：約一萬個agent協同運作
- 訓練方式：透過multiagent RL訓練約一年
- 推論哲學：大量非結構化的平行測試時運算,讓agent自行決定分工與協作方式,而非完全依人工腳本編排

素材分析指出,這種「讓模型自己決定如何合作」的描述,暗示的是一種部分湧現(emergent)的協調策略,而不是全手動編排的流程。如果這項工作確實觸及了困難的數學問題,真正的創新可能不在於「LLM寫出一篇證明」,而在於帶有學習型協作策略的分散式定理搜尋。

📊 **公開推文「確定」與「未確定」的界線**

素材明確區分了兩類資訊:

已經浮上檯面的說法:
- 約一萬個agent參與其中
- OpenAI花了約一年時間訓練協作型agent
- 系統使用大量平行測試時運算
- 這項結果被公開討論為與Navier-Stokes解答/證明有關的主張

尚未被證實的部分:
- 沒有任何理論陳述、預印本、證明草稿、形式化驗證產物、基準報告或獨立審稿意見出現在這批推文中
- 「解答」一詞本身模糊不清,可能是完整證明、證明策略、候選反例、形式化推導,或只是一條研究線索,推文並未釐清
- 是否針對標準的3D不可壓縮Navier-Stokes全域正則性問題(在R^3或環面上)給出答案,完全沒有揭露
- 人類與模型的實際分工比例未知,「一萬個agent協作」並未說明是人類拆解搜尋空間、篩選引理、驗證步驟,還是模型幾乎全自動完成

💡 **為何這類「AI解出X」的說法特別容易失真**

素材點出一個關鍵觀察:在前沿模型的討論中,「AI解決了X」這句話經常壓縮了多個不同層次——生成猜想、搜尋、草擬證明、驗證證明、社群審查認可,而這批推文只提供了系統層級的描述,並未觸及數學本身的認識論狀態(epistemic status)。若Navier-Stokes全域正則性真的被證明不成立(即存在有限時間奇異點),這將是極具爆炸性的結論,需要極度精確的陳述與審查,而目前顯然還沒有走到那一步。

⚠️ **連「ChatGPT變慢」都被牽拖成證據**

事件也衍生出不少缺乏根據的猜測,例如有人將ChatGPT出現延遲警告,聯想成OpenAI可能把大規模運算資源轉去跑這次的Navier-Stokes實驗,但素材明確指出這純屬臆測,並無證據支持。另外也有評論者將此事框定為「AI真的不會寫程式」論調的崩潰時刻,或視為業界進入「高運算規模」時代的訊號,但這些都屬於社群心理與產業敘事層面的評論,而非可驗證的技術評估。

🎯 **實務啟示**

對工程師而言,這起事件真正值得關注的,不是「Navier-Stokes被解開了嗎」,而是背後透露的研發方向:用海量平行agent搭配自組織協調策略,在推論階段砸大量運算去啃困難問題,可能正在成為與「把單一模型做大」同等重要的路線。但在看到論文、證明稿與獨立驗證之前,任何「已解決」的說法都該先當作待驗證的強主張,而不是既定事實。

🔗 **來源**
- 標題：[AINews] OpenAI reports Navier-Stokes singularity find in 88 hours using Astra-next, roughly 10,000 agents and 130B tokens (>$40M), a contender for second ever Millennium Prize awarded
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-openai-reports-navier-stokes

#OpenAI #NavierStokes #MillenniumPrize #MultiAgentRL #TestTimeCompute #AIResearch #AIagents #MathAI #AIskepticism #FrontierModels
