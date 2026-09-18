---
title: A new kind of AI model from a ChatGPT inventor is thrilling developers
source: TechCrunch AI
url: https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/
model: claude-code/sonnet
generated_at: '2026-09-18T19:45:27.818381'
score: 102
---

📌 發明 RLHF 的人說:LLM 不是自動化該用的語言

TL;DR：TypeSafe AI 推出非 LLM 的 Jev,輸出校準機率而非文字,開發者實測比 LLM 分類器快 5 到 20 倍。

Diogo Almeida 參與打造了 ChatGPT,也發明了 RLHF——這個讓當代 AI 得以誕生的關鍵訓練技術。但他心碎了。「我們手握閃電,它卻不實用,」他告訴 TechCrunch。這句話,成了他離開 OpenAI 創辦新公司的起點。

🤔 **問題不在模型,在於「語言」本身**

Almeida 的診斷是:「我們花了四年把人類語言做得非常好,但這對自動化沒用,因為電腦說的是另一種語言。」兩年前他離開 OpenAI,創立 TypeSafe AI,試圖解決這個落差。這週,公司發表了新模型 Jev——一個基於 transformer,但刻意不輸出文字的模型。它輸出的是機率,公司稱之為「校準決策(calibrated decisions)」。

🧩 **不說話的模型,為什麼反而更有用**

放棄語言輸出帶來幾個直接效果:模型變得極其便宜且快速;因為輸出範圍由使用者預先定義,它不會產生幻覺(hallucinate)。計費方式也不同於一般 LLM——輸出 token 免費,輸入 token 以「十億」為單位計價,而非「百萬」。文章提到,需求一度高到公司短暫無法透過 API 服務所有使用者。

📊 **開發者實測:快 5 到 20 倍,而且給出真實機率**

Vercel 的軟體工程師 Pranit Sharma 原本用 OpenAI 的 ChatGPT Luna 5.6 跑一個分類器,審查指令是否安全;換成 Jev 後,結果快了 5 到 18 倍,準確度也更高。另一位開發者,Bryo AI 的 CTO Nikhil Mudholkar,拿 Jev 與 Gemini 比較商業郵件分類:Gemini 略準一些,但成本貴了 10 到 20 倍。真正打動他的是 Jev 會回傳「真實的機率」,他認為這對自動化工作流是關鍵能力。

Jev 也能反過來輔助 LLM:用它監控 agent 的行為軌跡、攔截越獄(jailbreak)嘗試,成本遠低於用另一個 agent 去監控 agent。開源模型 harness Pi 的作者、Earendil CTO Armin Ronacher 解釋這種設計的哲學:「這等於把幻覺問題的一部分交還給使用者——如果它只回傳 50% 機率,那可能就是丟硬幣,你可以選擇忽略;但如果是 95%,你就可以放心採取行動。」Ronacher 也提到另一個潛在用途:model routing,用 Jev 即時判斷一項工作該交給哪個模型處理,而不必動用昂貴的 LLM 來做這個判斷。

💡 **模型取名自 Jevons 悖論**

Jev 這個名字來自 19 世紀經濟學家 William Stanley Jevons,他提出的悖論描述:一項商品成本下降,反而會導致它被更廣泛地使用。Almeida 的賭注正是如此——智慧的成本下降,會讓它散布到軟體的每個角落。「我們認為未來會有大量智慧型軟體,以一種湧現、分散的方式存在,更像早期的網際網路,而不是現在大家在建的那些巨型 app。」

⚠️ **架構不透明,靠合成資料訓練**

Almeida 對模型架構相當保密,外界觀察者推測它建立在某個開源權重 LLM 之上。公司把 Jev 稱為「System One 模型」,強調直覺而非推理,且針對特定任務優化。Almeida 表示 Jev 完全以合成資料訓練,採用他稱為「reinforcement learning from calibrated decisions」的技術。他形容這是自己「做過最好的賭注之一,比公司上線本身還好,甚至比 RLHF 還好」。Ronacher 認為,既然 Jev 的實用性已經顯現,競爭者很快就會出現。TypeSafe 本身也計畫在其他模態推出更多版本的模型。

🎯 **實務啟示**

如果你的系統裡有大量「分類、審查、路由」這類任務,目前用 LLM 硬解,Jev 這類「輸出機率而非文字」的模型提供了一個值得評估的方向:用機率閾值取代文字解析,天生規避幻覺問題,而且可能大幅降低延遲與成本。它與 LLM 並非取代關係,更像是分工——LLM 負責生成與推理,校準機率模型負責判斷與把關。

🔗 **來源**
- 標題:A new kind of AI model from a ChatGPT inventor is thrilling developers
- 作者/機構:Tim Fernholz, TechCrunch AI
- 連結:https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/

#TypeSafeAI #RLHF #AIAgents #CalibratedProbability #ModelRouting #Hallucination #AIStartup #SoftwareAutomation #Transformer #AIInfrastructure
