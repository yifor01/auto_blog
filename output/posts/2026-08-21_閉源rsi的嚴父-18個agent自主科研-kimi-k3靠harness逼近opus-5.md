---
title: 閉源RSI的嚴父：18個Agent自主科研，Kimi K3靠Harness逼近Opus 5
source: 量子位
url: https://www.qbitai.com/2026/08/476199.html
model: claude-code/sonnet
generated_at: '2026-08-21T06:37:04.472520'
score: 80
---

📌 【Prime Intellect最新實驗】開源Kimi K3配Harness,逼近Opus 5

TL;DR：Prime Intellect讓18個前沿模型速通nanoGPT訓練最佳化,開源的Kimi K3搭配自家Harness跑出2930步,只差Opus 5十步。

過去大家想像的RSI(遞迴自我改進)劇本,是某個最強的閉源模型率先跨過「AI開發AI」的臨界點,然後把所有對手越甩越遠,贏家通吃。但Prime Intellect最新公布的實驗結果,讓一個開源權重模型逼近了本該遙遙領先的閉源旗艦,這個經典劇本開始動搖。

🤔 能不能讓「AI開發AI」變得更便宜?

Prime Intellect想驗證的問題是:藉助多智能體Harness,把監控與具體實作交給更小、更便宜的開源模型,是否能讓AI自主科研變得又便宜又有效,而不必每一步都動用最強大也最貴的閉源模型。

🧩 讓18個模型速通nanoGPT最佳化

實驗任務是速通Karpathy著名的nanoGPT訓練最佳化。Agent一開始拿到一份含baseline超參數的訓練指令碼,只被告知「現在這套方案還不夠好」,至於該換更好的預條件方法、給權重與更新幅度設上下限、調整學習率schedule,還是在訓練後期加入權重平均,完全靠agent自己嘗試。評分只看一個指標:用盡可能少的training steps,把一個1.24億參數GPT的驗證集loss降到3.28以下。Baseline設在3290步,目前公開的人類最佳紀錄是2600步。每次啟動,agent會拿到程式碼倉庫、規則手冊與目標指令,實驗統一在8張H200上執行,全程鎖進斷網sandbox,防止agent直接上網抄現成答案。在Kimi K3的測試中,Prime Intellect自家的Prime Agent Harness提供了一個持久執行的IPython核心,讓模型能圍繞研究任務自行搭建與迭代工作流,也讓K3能主動推翻自己先前的假設。

📊 153次全自主實驗,Kimi K3逼近Opus 5

參與測試的共有18個前沿模型,包括Fable 5、Opus 5、GPT-5.6 Sol、Kimi K3、Grok 4.5、GLM 5.2、Muse Spark 1.1、DeepSeek V4 Pro、Grok 4.6、Muse Spark 1.2、Qwen 3.8等。整體共跑了153次全自主實驗,單次最長持續超過8天。

| 模型 | 最終成績(training steps) | 備註 |
|---|---|---|
| Fable 5 | 2726步 | 本次實驗最佳成績,已吃掉baseline與人類紀錄之間690步差距中的564步,約82% |
| Opus 5 | 2920步 | Anthropic旗艦閉源模型 |
| Kimi K3(搭配Prime Agent Harness) | 2930步 | 開源權重模型,僅比Opus 5多10步,超過GPT-5.6 Sol |
| GPT-5.6 Sol | 3042步 | — |
| Baseline | 3290步 | 實驗起點 |
| 人類公開最佳紀錄 | 2600步 | 尚未被任何模型追上 |

💡 拉開差距的不是idea,是試錯的方式

一個多少有點掃興的結論是:153次實驗裡,沒有任何一次提出真正全新的方法,最終有效的normalization、學習率調整、權重平均、optimizer技巧,大致都能在既有研究裡找到類似思路。但正因為大家最後想到的idea差不多,另一個現象反而更明顯:真正拉開模型差距的,不是想到了什麼,而是怎麼把它試出來。強模型不會輕易判死一個idea,會換seed、重新消融,甚至在recipe改變後把舊方案撿回來重測,例如Opus 5重新調整β2後刷出新紀錄,Fable 5重新探測舊方案又省下31步。強模型也更擅長分辨一個提升究竟是真實改進還是隨機噪聲,甚至有模型發現同一個seed重複跑,loss也會因GPU的非確定性而變化,並圍繞這個現象重做實驗流程。強模型還會自己造工具:Kimi K3會自己寫實驗函式、比較loss曲線、恢復baseline,甚至搭建一個小型數值實驗室先驗證Newton-Schulz,再把結論帶回真實訓練。這讓「科研能力」開始更像一個試錯吞吐量問題,而不只是單純比誰的模型更聰明。

⚠️ 沒有新方法,結果也尚待第三方驗證

153次全自主實驗裡,沒有出現真正原創的新方法,找到的招數多是既有研究思路的重新組合。這份結果目前是Prime Intellect自行發布的部落格內容,尚未經過同行評審或第三方復現。

🎯 便宜開源模型+Harness,可能是更划算的AI科研槓桿

對於想壓低AI4Research或AutoML成本的團隊,這個實驗提示了一個可行方向:把「該不該繼續某個方向」這類需要判斷力的環節留給強模型,把寫程式碼、跑實驗、盯結果這類重複勞動交給便宜的開源模型加Harness,用同樣預算跑更多輪試錯。這也代表未來提升AI科研能力的槓桿,可能不只在模型本身的智力,也在圍繞模型打造的agent編排基礎設施,例如Prime Agent Harness提供的持久IPython核心。Prime Intellect下一步計畫把這套speedrun擴展到訓練棧的更多環節,並繼續放大實驗規模。

🔗 來源
- 標題：閉源RSI的嚴父：18個Agent自主科研，Kimi K3靠Harness逼近Opus 5
- 作者／機構：henry, 量子位
- 連結：https://www.qbitai.com/2026/08/476199.html

#RSI #AIResearch #PrimeIntellect #MultiAgentHarness #OpenSourceAI #nanoGPT #AutoML #LLMAgents #KimiK3 #AIInfrastructure
