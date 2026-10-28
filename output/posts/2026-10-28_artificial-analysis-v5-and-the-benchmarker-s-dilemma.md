---
title: Artificial Analysis v5 and the benchmarker's dilemma
source: Interconnects
url: https://www.interconnects.ai/p/artificial-analysis-v5-and-the-benchmarkers
model: claude-code/sonnet
generated_at: '2026-10-28T21:57:09.799583'
score: 91
---

📌 GPT 6.1 Terra 贏過 Claude Fable 5.1?拆解 Artificial Analysis v5 的評測難題

TL;DR：AA 智慧指數大改權重後開閉源差距再度拉大,但這揭露的是評測方法本身的取捨難題。

把一個模型的能力壓縮成一個數字,聽起來像是把複雜問題簡化,實際上卻是整個 AI 產業裡壓力最大的工作之一。Artificial Analysis 最新一版智慧指數 v5 上線後,出現了一個讓人意外的排名:GPT 6.1 Terra 贏過 Claude Fable 5.1。Interconnects 作者 Nathan Lambert 藉此談了一個更根本的問題:獨立評測機構到底在解決一個多難的題目。

🤔 **每個評測機構都要面對同一個兩難**

Lambert 指出,獨立評測不是單純對現有模型「認證分數」這麼簡單。當 AI 進步速度這麼快,把能力壓縮成一個能反映 vibe check、社群觀感與科學分析,卻又不會三個月後就過時的單一數字,本身就是一場高難度任務。而每一種把多項分數彙整成一個數字的方法,都必然帶著取捨。考慮到今天 AI 生態系裡的資金規模,這類指數某種程度上在決定一個數兆美元市場的勝負,甚至影響模型本身演進的方向。

🧩 **AA v5 的權重配置**

| 類別 | 權重 | 子項目 |
|---|---|---|
| Knowledge Work | 25% | AA-Briefcase(15%)、AutomationBench-AA(5%)、GDP.pdf(5%) |
| Coding | 25% | FrontierCode 2.0(15%)、Terminal-Bench 4.0(10%) |
| Science | 25% | Terminal-Bench-Science(15%)、CritPt v2 hard subset(10%) |
| General | 25% | AA-Omniscience v1.1(15%,含 10% 準確率+5% 非幻覺率)、HLE-Diamond(10%) |

官方說法是這套權重「反映真實世界今日的使用情況」,但 Lambert 認為真實世界的使用狀況本身就極度參差不齊,就像模型能力一樣。目前驗證最充分的場景是程式開發,開源模型在這塊確實有競爭力,但在知識工作領域,他對開源模型的表現就沒那麼有信心。

📊 **開源模型落後的焦點:科學類評測**

引發這篇文章的那張圖,顯示 8 個閉源模型的分數贏過目前最好的開放權重模型 Kimi K3.1 Pro(圖中甚至沒有標示為藍色,代表它不在"領先"之列)。Lambert 認為,這代表 AA 這次的指數更偏向衡量「前沿模型正在往哪個方向移動」,而這會拉大與開源模型的差距。開源模型目前落後最明顯的,是像 terminal-bench-science 與 CritPt v2 這類「科學」評測,但他也提到開源模型本來的價值主張就不是要在絕對前沿上競爭。

💡 **「私有基準」的取捨:防 benchmaxxing,但犧牲透明度**

這次更新另一個值得留意的變化是轉向「私有基準」,也就是不公開 prompt 內容,用來當作防範開源實驗室過度針對基準做訓練(benchmaxxing)的訊號。Lambert 的分析框架是:最好的開源模型確實會做一點 benchmax,最差的開源模型做得更多(但通常也沒什麼人關注);最好的開源模型能力覆蓋範圍相對較窄,科學領域的差距就是例子。他認為這背後更細緻的解釋,是訓練成績的提升很多來自於 RL 環境的資料分布與評測本身夠接近,而不是所有開源實驗室都具備足夠成熟的 RL 技術堆疊去跟上多個領域同時進步的節奏,有些實驗室甚至仰賴採購資料,交付週期本身就有延遲。不過他也坦言,私有基準意味著要完全信任基準建造者,少了社群公開挑錯、推動基準自我改進的機制,而這種機制過去其實發生過很多次。考慮到這個領域牽涉的資金規模,他個人更傾向透明、讓更多人能挑出基準本身的問題。

🎯 **對工程師的實務啟示:別被單一數字綁架選型**

Lambert 最後提到一個值得工程師記住的觀察:Anthropic 與 OpenAI 這類頭部實驗室,其實早就不太在意這類公開指數了,他們的重心大多放在內部用途(例如 AI R&D 自動化)與願意付費的大型客戶需求上。對於要選型的工程師而言,這篇分析提醒的是:單一智慧指數適合快速排名,但真正該看的是跟自己使用場景(coding、知識工作、科學推理)最接近的子項分數,而不是只看總分。他也預期下一個主要開源模型週期(例如 2 到 3 個月後的 GLM 6 或 Kimi 3.5)很可能在這個指數上明顯拉近差距,這是過去幾年反覆出現的模式。

🔗 **來源**
- 標題：Artificial Analysis v5 and the benchmarker's dilemma
- 作者／機構：Nathan Lambert, Interconnects
- 連結：https://www.interconnects.ai/p/artificial-analysis-v5-and-the-benchmarkers

#AIBenchmarks #ArtificialAnalysis #LLMEvaluation #OpenSourceAI #FrontierModels #AIIndustry #ModelEvaluation #Benchmaxxing #AIResearch #Interconnects
