---
title: AI開始改進“改進自己的方法”，RSI進入平方時代丨MetaRSI
source: 量子位
url: https://www.qbitai.com/2026/09/488832.html
model: claude-code/sonnet
generated_at: '2026-09-14T21:06:26.049337'
score: 105
---

📌 當AI開始改進「改進自己的方法」，RSI進入平方時代

TL;DR：CosmosMind聯合多所高校推出MetaRSI-v1，首次統一Model、Data、Harness三種遞迴自我改進機制。

如果一套AI系統已經能自己生成訓練資料、自己改寫提示詞、自己修復程式碼，那麼再往上一層，讓「改進的方法本身」也被改進，會發生什麼事？這正是MetaRSI-v1想回答的問題。

🤔 現有RSI系統的共同侷限

遞迴自我改進（Recursive Self-Improvement，RSI）指的是模型反覆對自己進行改進的路線。但文章指出，幾乎所有現有RSI系統都共用同一種結構：一套固定不變的改進程序，反覆作用在模型上，而且往往只從Harness、Data或Model其中一個視角切入，彼此互不統一。CosmosMind聯合史丹佛、柏克萊、MIT、清華、北大等十餘家海內外高校，針對這個問題提出MetaRSI-v1，宣稱是全球首個統一Model-RSI、Data-RSI、Harness-RSI的元遞迴架構，能夠進一步「改進自我改進的過程」本身。

🧩 統一底層：Loop Kernel與三個運算元

MetaRSI-v1的核心是首次提出的Loop Kernel範式：把「進步如何發生」抽象成一條與物件無關的閉環——消費反饋得到學習訊號，在Data、Harness、Model上提出改動，交由驗證器裁決，再把結果迴流成下一輪的訊號。Data、Harness、Model從此可以被視為同一個Kernel底下不同的運算元實例，能夠彼此組合、統一排程。

三個運算元各自承擔不同工作：
- Data-RSI：從模型自身的執行軌跡中提取學習訊號，經校驗後合成資料供下游消費，同時標定並放大模型能力的正、負邊界。
- Harness-RSI：利用學習反饋訊號，在Harness拆分出的System Prompt、Skill、MCP、Tools、Memory五個可插拔槽位上做加法與減法，動態調整。
- Model-RSI：更新模型自身的參數與結構，把反覆驗證有效的行為直接內化進模型。

在運算元之上，MetaRSI設計了橫、縱兩條編排軸：橫軸（horizontal orchestration）由RSI²Agent在每個決策點依訊號反饋決定下一個要用哪個運算元；縱軸（vertical optimization）則由RSI²Agent向該運算元專屬的RSI²Sub-Agent下發指令，改寫運算元內部的RSI規則，等於最佳化「RSI系統本身」。整套架構由四個Agent協調：MetaRSI²Agent學習如何做合適的縱橫最佳化，RSI²Agent負責每個決策點的橫縱選擇，RSI²Sub-Agent執行縱向策略改寫，Transition Agent銜接上游運算元的產物與下一個運算元的輸入。四個Agent對應三層RSI最佳化：運算元改進目標系統、雙軸編排改進運算元用法、元層改進雙軸編排策略本身。

📊 小模型與旗艦模型都測出自我提升

實驗沿兩條路線展開。小模型路線以Qwen3.5-35B-A3B（35B總參數、3B啟用參數）為目標模型，Data、Harness、Model三個運算元全部開啟，在Terminal-Bench 2.1、SWE-bench Pro、GPQA-Diamond高難度子集、AIME四項基準上評測，結果MetaRSI-v1帶來平均10.9分的提升，其中SWE-bench Pro的解決率接近翻倍。

前沿模型路線面向GPT-5.6、Claude Opus 5、Kimi K3等六款頂級模型，由於這些模型參數巨大或本身為閉源，僅啟用Data與Harness兩個運算元，在Terminal-Bench 2.1上依然測得平均7.3分的提升。整個過程沒有任何外部教師模型參與。

💡 加法與減法並行：能力留下，成本退場

文章特別指出，Harness-RSI不只做加法，也會做減法：當Data-RSI放大暴露出的問題經Model-RSI內化進模型參數後，原本靠Harness補強的那部分知識就變得冗餘，Harness-RSI會在回放校驗下把它刪除，結果是能力保留、但推理成本下降。Data-RSI的產物同時供給Harness-RSI與Model-RSI消費，兩條路線的改動又會迴流回Data-RSI，重新標定能力邊界，驅動下一輪改進，形成逐輪累積的閉環。團隊也提煉出五條定律，其中一條值得工程師留意：可信度由不可寫面度量，也就是說在閉環內部，「真正能力變強」與「單純放寬成功標準」會得到完全相同的分數，這種偏差從系統內部無法察覺，也無法靠統計方式糾正。

⚠️ 自我改進系統的內生風險

上述「可信度不可寫面度量」的定律，某種程度上點出了這類自我改進閉環共同的隱憂：驗證器本身如果被鑽漏洞或標準被悄悄放寬，系統無法從內部分辨出來。文章也承認，能不能形成自改進閉環，前提是該領域任務要有合適的verifier可用，這意味著MetaRSI的方法論並非對所有任務都同樣適用。

🎯 實務啟示

對正在做agent或RSI相關研究的工程師而言，Loop Kernel這套「訊號→改動→驗證→迴流」的統一骨架，值得拿來對照、盤點自己系統目前偏重Data、Harness還是Model中的哪一環。團隊同步開源的RSI-Harness，作為一個能自我學習迭代的Harness框架，也是值得關注的實作起點。

🔗 來源
- 標題：AI開始改進「改進自己的方法」，RSI進入平方時代丨MetaRSI
- 作者／機構：思邈，量子位
- 連結：https://www.qbitai.com/2026/09/488832.html

#RSI #RecursiveSelfImprovement #AIAgents #MetaRSI #LLM #MachineLearning #AIResearch #SelfImprovingAI #Qwen #AIArchitecture
