---
title: '[AINews] High Taste Testers Ep. 1'
source: Latent Space
url: https://www.latent.space/p/ainews-high-taste-testers-ep-1
model: claude-code/sonnet
generated_at: '2026-10-17T19:41:49.301135'
score: 63
---

📌 開源模型三消大戰開打:Meta Muse Spark Open 對決 Reflection Beam,「決策模型」新賽道登場

TL;DR:一週內看懂美系開源MoE模型打擂臺、新興決策模型分類,以及TPUv7、Vera Rubin的推理晶片戰報。

🎣 這期Latent Space的AI新聞彙整涵蓋範圍很大,從Meta、Reflection、StepFun、騰訊的開源權重大戰,到Gemini、Anthropic、OpenAI的前沿模型更新,再到一個新詞「決策模型(decision model)」正式登場。以下整理工程師最該留意的幾條線。

🧩 美系開源權重對決:Muse Spark Open vs Reflection Beam

Meta Muse Spark Open是816B總參數、42B啟用的MoE模型,開源權重。根據Artificial Analysis(AA),其Intelligence Index為39分,是目前美系開源模型最高分,比NVIDIA Nemotron 3.5 Super VL的26分高出13分。架構為62層、GQA 16個KV head、每個token啟用8/256個專家,搭配18億參數的Perception Encoder與100萬token上下文,支援文字、圖片、影片、音訊輸入,輸出為文字。BF16權重約1.6TB,Meta另外提供僅量化專家層的NVFP4版本,壓縮至約530GB,官方稱可塞進4張Blackwell Ultra GPU、8張H200,或兩臺512GB記憶體的M5 Ultra Mac Studio。

Reflection Beam 1.0則是501B總參數、23B啟用的MoE模型,100萬token上下文,採Apache 2.0授權開源,同時釋出BF16、FP8、NVFP4三種權重格式,附帶DFlash2 drafter、訓練所用的開源Mirror CLI框架,以及一份安全報告。AA給它30分,是美系開源模型第二高分,平均每個任務用掉約2.6萬個token。

| 模型 | 總參數/啟用參數 | AA Intelligence Index | 平均輸出token/任務 | 弱點 |
|---|---|---|---|---|
| Muse Spark Open | 816B/42B | 39 | 約4萬 | AA四項agentic評測中墊底,Vals榜上開源模型排第12、整體排第38 |
| Reflection Beam 1.0 | 501B/23B | 30 | 約2.6萬 | Terminal-Bench 4.0僅3.0%,AA-Omniscience雖答對33%但幻覺率達47% |

費用上,Together、Fireworks、Baseten對Muse Spark Open的報價為每百萬輸入/輸出token 1.25美元/4.25美元,快取輸入0.15美元;AA換算每個index任務成本0.84美元,比GLM-5.3的2.01美元便宜,但仍高於DeepSeek V4.1 Flash的0.27美元,平均每個任務用掉的輸出token數(約4萬)也是前九大開源模型中最少的。生態系支援方面,mlx-lm首日即支援Muse Spark Open並含視覺能力,Apple也發文介紹如何用RDMA跨多臺Mac Studio做分散式推理;vLLM在Muse訓練階段就負責跑RL rollout,發布當天同步支援推理;SemiAnalysis則在其InferenceX服務中加入B200設定。在Arena的Code WebDev榜單上,Muse Spark Open以1511分成為美系開源模型最高分,整體排名開源模型第13。授權上,Muse Spark Open採用客製化的Muse Model License,要求標註「Built with Muse Spark Open」,年營收超過2000萬美元的Model-as-a-Service業者需另外與Meta簽約。評論聲音(屬個人意見,非官方定論):有評論者@teortaxesTex認為Muse Spark Open面對更小、採MIT授權的V4.1 Flash時已經出局,並推測(未附證據)Meta是顧慮被認定抄襲蒸餾自OpenAI的模型才按住了Spark 1.3沒發;另一邊,@alexandr_wang則形容Meta打造出了一臺「能持續生產新模型的機器」。

Reflection Beam同樣由vLLM首日支援,在4張B300、NVFP4、TP4設定下,併發16時量得每秒1,769個輸出token;SkyRL提供首日LoRA、全量微調與MXFP8強化學習支援,並稱LoRA的decode輸出量提升62%(每GPU每秒276提升到447個token,但這是decode階段的數字,不是端到端訓練速度的提升);Ollama限時免費提供Reflection Beam,主機設在美國且不保留使用者資料。在Arena榜單上,Reflection Beam於Agent Arena排名開源模型第12(誤差±3.84%),也是唯一進入Code WebDev開源前25名的非中系模型。同期其他開源釋出:StepFun發布Step 5 Preview開源權重;騰訊推出Hy Memory 2.0,並宣稱Hy-Memory-30B-A3B在記憶體框架評測上超越Opus 5;Datalab釋出僅100萬參數的OCR模型Indra,宣稱在CPU上執行速度比Tesseract快15倍。

📊 前沿模型更新與「決策模型」新賽道

Gemini 4 Argon已向Pro訂閱用戶與AI Studio Build開放,正式版把輸出上限從6.4萬token拉高到100萬token(與輸入共用同一個視窗),早鳥定價為每百萬輸入/輸出token 2美元/10美元,將持續到11月30日。Perplexity表示Argon在其WANDR研究基準上刷新紀錄,在Agent Arena排名第5、提升13.2%;也有使用者對其數學能力給出初步好評,但提醒需要調高推理力度(reasoning effort)才能發揮。

Anthropic這邊,Haiku 5.5對10萬token以內的提示收費每百萬token 0.10美元(輸入)/0.50美元(輸出),比Haiku 4.5便宜約九成,在最大推理力度下Terminal-Bench 4.0拿下39.2%,相較GPT-6 Luna的16.4%;另有報告指出Opus 5.5出現了2.5倍速的快速模式;Claude Code也更新為每一輪對話都對傳輸內容做gzip壓縮以降低延遲。OpenAI這邊,ChatGPT中的GPT-6 Astra Pro現在能把任務拆成多個部分、並行跑多個agent,換來更快回應與更好的工具使用;GPT Live 1.1改善多語言語音,新錄了九組由真人配音員演繹的語音預設;另有未經證實的傳言(屬推測)指出Codex可能有一到兩款新模型即將推出。

值得一提的是Elorian Glimpse,一款「視覺思考」VLM,改用對潛在視覺狀態做循環運算,取代純文字的chain-of-thought。Elorian自稱在12項基準中有5項打平或超越Astra,token價格卻低17倍,訓練僅用了「數百張GPU」;也有使用者做了非正式測試,在一組棋盤題上Elorian答對8/10題,Gemini 3.8 Flash答對5/10題。

新興的「決策模型(calibrated one-pass classifiers)」類別也在這期出現:

| 模型 | AA Decision Index | 非幻覺率 | 準確率 | 延遲 | 價格 |
|---|---|---|---|---|---|
| Liquid d1-ultra | 65 | 85%(前代d1為2%) | 32%(前代d1為41%) | 92毫秒/任務 | 每百萬輸入token 0.042美元,輸出免費 |
| Jev 1.14 | 57 | 未提供 | 未提供 | 未提供 | 未提供 |

Perplexity也推出pplx-decider v1.2,開源權重分為27B模型(每百萬token 2美分)與4B Flash模型(每百萬token 1美分)兩個版本,新增reranking、單次推理可處理多問題(最高快5倍)與-latest版本代號。應用面上,OpenAI的Live API新增了Decisions API,用於快速的工具委派;有使用者實驗把Jev模型換進Recursive Language Model的子呼叫中,在OOLONG基準、100萬token長度的情境下,成本減半、速度快6倍,優於Haiku 5.5。

💡 推理硬體戰報:TPUv7、Vera Rubin與MI355X互相叫陣

SemiAnalysis報告指出,在AgentX上,TPUv7每美元效能比GB300 NVL72(FP4)高1.42倍(採用非Google的外部成本基準計算),比MI355X高2.5倍;在中高互動性情境下,TPUv7比拆分式(disaggregated)GB200最高快3.16倍,但GB200的FP4在低互動性情境仍保有1.2倍優勢,該測試以vLLM搭配TorchTPU進行。NVIDIA自行送測的結果顯示,Vera Rubin NVL72在AA-AgentPerf上,處理DeepSeek V4 Pro時每MW吞吐量最高達GB300的5.7倍,處理Kimi K3時降到2.8倍,在高單使用者速度情境下增益最明顯;峰值吞吐量的差距則縮小到1.14至1.45倍;Vera Rubin在V4.1 Flash上也創下每使用者每秒906個token的紀錄。AMD方面,8張MI355X在Kimi K3、每使用者每秒50 token的設定下,吞吐量比HGX B300高24.4%,每美元token數則高87.4%;Inferact也宣布與AMD合作,公開agentic推理的開源配方。

🎯 這期資訊量很大,對工程師最實用的兩個訊號是:一是開源MoE模型的競爭正從「智慧分數」延伸到「每個任務的實際成本與agentic能力」,挑模型前務必對照AA等基準的agentic分項,不能只看綜合分數;二是「決策模型」正成為獨立產品類別,專門處理需要快速、低成本、高確定性判斷的子任務,未來設計multi-agent系統時,可以考慮把部分子任務從大模型卸載給這類校準過的一次性分類器,換取延遲與成本的大幅下降。

🔗 來源
- 標題:[AINews] High Taste Testers Ep. 1
- 作者/機構:Latent Space
- 連結:https://www.latent.space/p/ainews-high-taste-testers-ep-1

#OpenSourceAI #LLM #MoE #Gemini #Anthropic #OpenAI #AIInference #DecisionModels #GPU #AIHardware
