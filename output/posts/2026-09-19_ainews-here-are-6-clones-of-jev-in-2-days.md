---
title: '[AINews] Here are 6 Clones of Jev in 2 days'
source: Latent Space
url: https://www.latent.space/p/ainews-here-are-6-clones-of-jev-in
model: claude-code/sonnet
generated_at: '2026-09-19T19:26:48.731194'
score: 100
---

📌 Jev爆紅48小時,冒出六個複製架構

TL;DR:Jev兩天狂攬3600萬觀看,六個開源或半開源的複製架構隨即湧現。

一支發表於週三的launch影片,兩天內衝出3600萬觀看數,對照組是什麼概念?OpenAI的Navier-Stokes研究成果影片是7400萬觀看,Anthropic的Fable 5是5700萬觀看。這支影片主角不是新模型的聊天能力,而是一種不生成文字、只吐機率的「決策模型」Jev。

🤔 沒開源反而燒得更旺

Jev並未開源,這個空白反而招來大量揣測、精彩demo與範例,也少不了對「這概念其實不新」忿忿不平的聲音,以及各種過度解讀,而這一切又進一步餵養了熱度。Latent Space的AINews統整了兩天內冒出的六個複製品,推測其中最接近的路線是ModernBERT系與Diffusion系。

🧩 兩天內的六個複製品長什麼樣

- Laya:421M參數,ModernBERT-large編碼器外加兩層新增的transformer來為使用者提供的選項評分,用PPO在sequence embedding上訓練,輸出逐輪轉換軌跡(0.0到1.0的機率)。Latent Space的鋭評是:作者對沒得到應有肯定感到不滿;宣稱自己用了RLCD卻沒有給出佐證;其信心分數是以entropy計算而非真正校準過的機率。
- DiffusionGemmaJev:改用diffusion model路線,基準測試表現相當接近Jev。
- Bespoke Nimble:對Qwen3.5-9B做LoRA微調,搭配對比式(contrastive)資料整理,基準測試略低於Jev。在其自建評測集上,原始Qwen從66%進步到90%,Jev則是93%,在H100上約100毫秒,可在本地跑。
- SemIf(前身為OpenJev):以4B與35B的Qwen3.5 causal backbone,外接一個在最後一個token上運作的三分類NLI分類器。
- Jevlike:一個4萬byte embedding的輕量option-attention模型,每個候選選項都變成一個query去讀取共享的context representation,再據此評分。
- Kev-0.5B:在Qwen2.5-0.5B上加LoRA adapter與一個小型讀出層(readout head),可以在MacBook Pro上跑。

值得注意的是,鮮少人談論資料面,而這波複製品的訓練資料被公認為100%合成產生。

📊 一場還沒有標準基準的軍備賽

Bespoke Nimble在其自建評測上的數字提供了少見的量化對照:base Qwen3.5-9B原本66%,微調後拉到90%,而Jev是93%,推論延遲約100毫秒(H100)。但正如評論者@abacaj指出的核心疑慮:多數demo強調的是速度而非品質,這個新興類別目前還沒有一套公認的標準基準測試。

💡 這不是聊天機器人故事,是workflow控制平面的故事

Braintrust已經把Jev接入自家的eval流程,評分成本據稱降到過去的約1/400。也有人從應用場景切入:校準過的機率適合用在routing、citation selection、escalation、法務流程等決策;更具架構企圖心的觀點認為,Jev這類判別式(discriminative)模型有機會把tool calling、routing、MCP式的決策,從小型生成式LM手中搶回來,甚至進一步被視為一種近乎零邊際成本、可以放在裝置端的判斷層,用在notification、UI調整、感測器驅動的決策上。使用者反應也出現世代分歧:經歷過ChatGPT洗禮的人視其為revelation,而GPT之前就在做傳統ML的人則相對困惑於這波熱度。目前最具說服力的落地場景集中在瀏覽器與電腦操作workflow:有人用它把Box的事件回報分類到對應的escalation路徑,有人用LangChain搭配Jev做browser use,在Wikipedia game和摺衣服式的結構化工作流上表現不錯,Cline也已經替它接上瀏覽器外掛,並被稱為目前看過最好的Jev應用案例。

🎯 實務啟示

如果你的agent系統裡有大量「該不該呼叫工具」「該路由到哪」這類判斷,值得關注這波判別式決策模型的發展,它有機會用遠低於生成式LLM的延遲與成本接手這類任務。但在導入前也要記住,目前這個類別還沒有公認的標準基準,多數demo強調的是速度而非嚴謹的品質評估,選型時不能只看展示影片。

🔗 來源
- 標題:[AINews] Here are 6 Clones of Jev in 2 days
- 作者/機構:Latent Space
- 連結:https://www.latent.space/p/ainews-here-are-6-clones-of-jev-in

#Jev #DiscriminativeModels #LLMRouting #OpenSource #AgentTooling #ModernBERT #LoRA #AIBenchmark #BrowserUse #MachineLearning
