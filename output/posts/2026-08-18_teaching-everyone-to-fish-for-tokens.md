---
title: Teaching Everyone to Fish for Tokens
source: Interconnects
url: https://www.interconnects.ai/p/teaching-everyone-to-fish-for-tokens
model: claude-code/sonnet
generated_at: '2026-08-18T06:37:24.847777'
score: 68
---

📌 Nvidia 砸 260 億美元,賭開源模型能撐起晶片需求

TL;DR:Nvidia 重金扶植開源模型生態,盼藉此撐住晶片需求,但這場賭注尚未見分曉。

如果開源大型語言模型（LLM）真的是下一個 Linux,為什麼願意投入完整訓練食譜（recipe）的公司越來越少?Interconnects 作者 Nathan Lambert（曾參與 Ai2 的 Olmo 模型開發）在這篇文章裡,拆解了「開源模型」與「開權重模型」的差異,並指出這條生態鏈背後真正的金主是誰。

🤔 開源模型不是 Linux,而是 Linux 的兩種不同零件

Lambert 認為,把開源 AI 直接類比成開源作業系統太粗糙。真正對應 Linux 原始碼的,是附帶完整訓練食譜、資料與程式碼的「開源模型」,例如 Ai2 的 Olmo 系列,以及更早的 EleutherAI Pythia。而我們平常使用、只拿到權重與推論程式碼的「開權重模型」,比較像是安裝在專案裡的特定版本軟體,權重本身汰換很快,但實務上壽命可以很長,就像許多公司至今仍用 Llama 3 建構的工作流程,即便 agentic 能力早已迭代好幾輪。

🧩 Nvidia 想教全世界釣代幣,Meta 則直接把代幣灑滿地

文章指出,Nvidia 正投入約 260 億美元推動近開源（near-open-source）模型,例如 Nemotron 系列,盡可能釋出資料與訓練程式碼。邏輯很直接：如果越多公司能自己動手訓練模型,對推論算力的需求就會越大,而這些需求最終都要靠 Nvidia 的晶片來滿足。這是一場「教全世界釣代幣」的策略,目標是讓整個生態系統自我維持,不被少數幾家壟斷智慧供給。

相對地,像 Meta 這類坐擁龐大資產負債表、透過其他業務間接變現的公司,則選擇直接把強力模型（文中提到 Muse Spark 1.2）以開權重釋出。這麼做能有效削弱 Anthropic、OpenAI 這類靠賣 token 賺錢的對手的營收成長。兩者都是在「商品化競爭對手的互補品」,只是路徑不同：一個是灌溉生態系,一個是直接把水淹過去。

💡 訓練食譜正在變得跟當年的 pretraining 一樣不透明

Lambert 觀察到一個更根本的趨勢：後訓練（post-training）過去泛指把 base model 變成可用智慧體的整個流程,但現在「把 base model 訓練成通用 agentic 推理器」這一步,正逐漸變得像幾年前的大規模 pretraining 一樣不透明、難以複製。他甚至預測業界用語可能會從 pretraining／post-training 的二分法,演變成 pretraining、reasoning training、post-training 三段式。當越少人關心「怎麼練出一個 base model」,自然也就越少人願意投資完整的開源訓練生態,這也解釋了為什麼釋出 base model 的開源團隊持續減少,轉而出現分潤授權（revenue share license）這類新的變現實驗。

🎯 實務啟示

對正在用 Tinker 之類工具微調 DeepSeek V4 Flash、Inkling Small、GLM 5.X 這類開放模型的工程師來說,這篇文章提醒了一件事：你現在受益的開源生態,建立在 Nvidia 的資本支出能否轉換成長期利潤的假設之上。如果這個假設不成立,開源模型很可能不會消失,而是分流到一個更偏效率、可修改性與特定場景（例如地端部署、企業內部 agent）的長尾生態,而非繼續追趕前沿閉源模型的通用能力。規劃長期技術路線時,值得把這個分岔情境納入考量。

🔗 來源
- 標題：Teaching Everyone to Fish for Tokens
- 作者／機構：Nathan Lambert, Interconnects
- 連結：https://www.interconnects.ai/p/teaching-everyone-to-fish-for-tokens

#OpenSource #LLM #Nvidia #AIInfrastructure #OpenWeights #Olmo #Nemotron #AIEconomics #MachineLearning #TechStrategy
