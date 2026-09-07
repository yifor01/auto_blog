---
title: 'Meta FAIR Introduces AI Research Preference Models (RPMs): Ranking ML Experiments
  Before Spending GPU Hours'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/06/meta-fair-introduces-ai-research-preference-models-rpms-ranking-ml-experiments-before-spending-gpu-hours/
model: claude-code/sonnet
generated_at: '2026-09-07T20:46:03.370733'
score: 95
---

📌 【Meta FAIR研究】別急著算分數，先讓實驗互相PK再花GPU

TL;DR：Meta FAIR用成對排名取代絕對分數預測，篩選出值得執行的ML實驗，同一算力下更快逼近甚至超越基線效能。

AI研究agent現在已經能自己提出、實作並評分自己的機器學習實驗。問題是，提出想法很便宜，驗證想法卻很貴——訓練一個候選方案動輒要花上數小時到數天的GPU時間，agent能提出的候選數量永遠遠多於它負擔得起執行的數量。真正決定研究進度的，其實是「該執行哪一個」這個選擇動作。

🤔 核心問題：選誰執行，比想出什麼點子更關鍵

來自Meta FAIR、牛津大學與倫敦大學學院(UCL)的研究團隊把這個「選擇」正式定義為research preference，並提出AI Research Preference Models(RPM)。關鍵設計是：RPM只負責替尚未執行的候選排名並挑出一個，它不去預測某個候選最終會拿到多少分數。研究團隊發現，語言模型在預測metric數值或執行結果這件事上並不可靠，所以乾脆放棄絕對分數預測，改用相對比較。

🧩 方法與架構：15個候選打知識淘汰賽，只有贏家能上場

RPM架在開源的evolutionary tree search框架AIRA-dojo之上：greedy parent selection挑父節點、用Draft／Improve／Debug三種operator產生子代、最終回傳驗證分數最高的節點。RPM只介入「產生子代」這一步——原本一次只生成一個子代並執行，現在agent平行套用operator15次，產生15個尚未執行的候選，接著用knockout tournament成對比較，只有贏家會被真正拿去執行。每次比較的依據，是對已探索樹做BFS走訪蒐集到的context node，每個node都附上它當時取得的驗證分數。

團隊實作了兩種RPM：
- Inference-only RPM：純粹是一個LLM-as-a-judge，對候選的計畫、程式碼與搜尋歷史打分。它的prompt經過DSPy的MIPROv2最佳化，收斂出一套「首席研究員」風格的評分準則：容忍可修復的bug、獎勵可延伸性、懲罰重複方向，離線準確率落在57.7%到59.0%之間。
- Agentic RPM：除了同一個judge，還多了一個複製agent環境的沙盒(含一張H200)，工具是python、bash與submit_solution。它會先跑小規模的pilot實驗，再由一個feedback model決定要不要提出下一個最有資訊量的pilot、或是結束比較。這裡有兩個值得注意的設計：一是刻意誇大剩餘預算(回報2,700秒，實際只有300秒)，避免agent過早喊停；二是pilot次數上限30次、單次60秒門檻。因為pilot時間會跟agent自己的時鐘搶額度，agentic selector只在Draft與Improve步驟啟用，Debug步驟仍退回隨機選擇。

📊 實驗設定與結果：效率提升比絕對勝率更實際

實驗涵蓋20個公開的文字與表格任務，每個任務在單張H200上跑24小時、10個隨機種子，operator與RPM都用同一個Qwen3.6-27B當backbone——這代表任何提升都是來自選擇層本身，而不是換了一個更強的judge。

相對No-RPM基線的改善機率，inference-only為0.5923(95%信賴區間下界0.5066)，agentic為0.5913(下界0.5018)。更具實務意義的是效率數字：inference-only在14.88小時(相當於1.61倍加速)就達到基線最終跑滿時間才拿到的0.684分；agentic版本則在15.50小時(1.55倍)達到同樣水準。若把自架inference額外增加的0.660小時算進去，調整後在23.34小時可以拿到0.708分。

論文也報告了兩項新的SOTA：WinoGrande上agentic RPM拿到94.1%，超過先前agentic SOTA(AIRA2的90.4%)；SVAMP上inference-only RPM拿到95.7%，超過先前人類SOTA的94.2%。

💡 深入分析：可部署性只到「部分」

RPM本身用的是凍結、未經微調的pretrained LLM，scaffold AIRA-dojo與benchmark AIRS-Bench都已開源，backbone Qwen3.6-27B也是開放權重模型。換句話說，這套選擇層不需要額外訓練成本，理論上可以直接套用在其他基於tree search的研究agent框架上。

⚠️ 限制

Agentic RPM的pilot實驗會佔用agent自己可用的執行時間，所以只能用在Draft／Improve兩種operator，Debug步驟仍得依賴隨機選擇，代表這套機制目前還沒有完全覆蓋整個搜尋流程。

🎯 實務啟示

如果你的agent pipeline也面臨「候選太多、算力太貴」的困境，這篇論文給出的思路值得參考：與其硬要模型猜出一個準確分數，不如讓它做它更擅長的事——兩兩比較誰更好。另外，agentic RPM裡「刻意誇大剩餘預算」這個小技巧，本質上是一種prompt層面的行為引導，或許也能用在其他容易「過早收斂」的agent設計上。

🔗 來源
- 標題：Meta FAIR Introduces AI Research Preference Models (RPMs): Ranking ML Experiments Before Spending GPU Hours
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/06/meta-fair-introduces-ai-research-preference-models-rpms-ranking-ml-experiments-before-spending-gpu-hours/

#AI #MachineLearning #MetaFAIR #ResearchAutomation #LLM #AIAgents #GPUEfficiency #AutoML #Qwen #ExperimentDesign
