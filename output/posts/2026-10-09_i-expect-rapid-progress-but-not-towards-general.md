---
title: I expect rapid progress but not towards general superintelligence
source: Interconnects
url: https://www.interconnects.ai/p/i-expect-rapid-progress-but-not-towards
model: claude-code/sonnet
generated_at: '2026-10-09T21:58:09.593210'
score: 89
---

📌 模型會超越研究者，但不等於走向超級智慧

TL;DR：Nathan Lambert認為AI研究將因工程自動化急速加速，但這不代表模型本質會出現質變。

頂尖研究者常說「AI 再過幾年就會比我更會做這份工作」，Nathan Lambert 一開始對這句話感到懷疑，最後他把答案收斂成一句話：研究者看到的其實是基礎設施與工程能力的爆發式進步,而不是模型本質正在變得不同。

🤔 **研究與工程的鐘擺，又一次擺回來了**

Lambert 指出，這不是 AI 領域第一次在「研究導向」與「工程導向」之間擺動。深度學習興起之前，AI 本質上更偏研究;之後，最優秀的研究者逐漸被要求要能把想法落地到複雜的基礎設施上並規模化執行。現在,隨著 coding agent 讓實驗與調參變得容易，鐘擺又開始往研究端擺回去,他認為 Ilya 提出「AI 進入研究時代」的說法其實說得早了一點，但方向是對的。這個轉變讓好的點子（idea）可能比好的執行力（execution）更有價值，而這個階段才剛剛開始。

💡 **先看得到效率的提升，再看不到的是模型本質**

Lambert 把近期可預期的進展拆成可驗證（verifiable）與不可驗證兩塊。訓練端的指標像是每張 GPU 每秒的 token 數,推論端的指標像是每個 prompt 的 token 數、每個 token 的 FLOPs，或直接算每個答案的成本,這些指標都高度可最佳化，而且已經有明確的子問題與架構取捨可以優化。他預期未來幾年 AI agent 能把這整條訓練與推論的 stack 端到端最佳化,讓推論效率逼近加速器（像 GPU）本身的理論算力上限。過去幾年,各家公司光是在推論效率上的優化,就已經能在公開定價之後再省下一成到三成的服務成本,他認為這整條 stack 會持續複利疊加,模型智慧的有效成本會以接近指數的速度下降,甚至可能比最近的趨勢更快。他給出一個具體的時間預測:預訓練研究,至少在架構與資料選擇這兩塊,在未來 2 到 3 年內被自動化是合理的預期。

這一波工程效率提升會觸發 agentic 模型版本的 Jevons paradox:成本降低不會讓需求減少,反而會讓需求增加,因為產業目前的瓶頸更多是在「如何更好地引導與交付 agent」，而不是模型能力本身。Meta 的 Muse agent 被他視為這個方向的早期訊號,價值來自理解 agent 如何被使用，而不是單純推高前沿效能分數。

另一個他點出的低垂果實是 RL 環境的品質問題。市場上已經有不只一家 RL 資料公司營收跨過一億甚至十億美元門檻,數量比他預期得多，但這個產業產出的平均品質其實相當低,不少研究者私下都承認自己買到的訓練資料很多是劣質品。即便如此,頂尖實驗室仍然看得到買這些資料帶來的明確回報，這意味著 RL 環境品質是一塊可以被直接修正、而不是需要架構突破的低垂果實。

⚠️ **工程加速解決不了的事**

Lambert 清楚劃出界線:他同意模型在幾年內會成為超人類等級的分散式 GPU 工程師,這會讓調整模型形態、做實驗變得容易很多,但這不會讓模型的本質出現戲劇性的不同。換句話說,這一波進展更多是把現有工具的推論時間運算（inference-time compute）規模化,而不是模型研究能力本身出現突破性的質變。他也點出科學文獻（像生物、化學）的對應情境:AI 擅長爬過大量文獻並在過去由彼此很少互動的小型社群各自把守的稀疏知識網路之間建立連結,這會不會帶出像攻克多數癌症那樣的新發現時代,還是只是讓科學原本的發展軌跡加速,目前是一條很細的分界線,還不明朗。

🎯 **給工程師的意義**

如果你的團隊正在做模型訓練或推論的基礎設施，這篇觀點等於是一個訊號:接下來幾年,效率最佳化（訓練速度、推論成本、RL 環境品質）會是最確定能拿到回報的方向,因為指標可驗證、問題有既定框架可以攻。但如果期待的是模型「研究判斷力」本身出現質變，Lambert 的態度是保留的,他押注的是「平行化、AI 輔助的語言建模」在工程面大幅提速，而不是通向某種泛用超級智慧。

🔗 **來源**
- 標題：I expect rapid progress but not towards general superintelligence
- 作者／機構：Nathan Lambert, Interconnects
- 連結：https://www.interconnects.ai/p/i-expect-rapid-progress-but-not-towards

#AIResearch #Superintelligence #MachineLearning #AIInfrastructure #RLHF #AIAgents #InferenceOptimization #AIAlignment #FutureOfAI #TechCommentary
