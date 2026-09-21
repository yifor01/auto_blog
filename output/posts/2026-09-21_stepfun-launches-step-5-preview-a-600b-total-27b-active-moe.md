---
title: 'StepFun Launches Step 5 Preview: A 600B-Total, 27B-Active MoE Model With 1M
  Context for Long-Horizon Agentic Work'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/20/stepfun-launches-step-5-preview/
model: claude-code/sonnet
generated_at: '2026-09-21T21:17:58.373105'
score: 88
---

📌 StepFun推出Step 5 Preview:600B MoE主打Agentic任務的成本效益

TL;DR:StepFun新旗艦模型以27B啟用參數對標更貴的競品,但開放權重要等到10月15日。

當一票旗艦模型都在拚「更聰明」時,StepFun這次打出的牌是「同樣聰明但更便宜」。Step 5 Preview鎖定軟體工程、專業知識工作與金融這幾類長程agentic任務,主打的正是所謂「Pareto frontier」的成本效益定位。

🧩 600B總參數,每個token只啟用27B

Step 5 Preview是稀疏Mixture-of-Experts(MoE)模型,總參數約600B,每個token啟用約27B,大約是總權重的4.5%。架構上StepFun沒有選擇加寬網路,而是堆疊了92層Transformer,走「窄而深」的設計路線。據Pandaily報導,研究團隊認為更深的堆疊能為隱式多跳推理提供更長路徑,這在長prefill場景下(agent持續搜尋、跑程式碼、讀取工具回傳結果時)尤其重要。

訓練上採用on-policy、長程強化學習,StepFun提到MoE路由上實現了位元級(bit-wise)的訓練與推理對齊,並搭配MTP-3投機解碼(speculative decoding)、FP8 MoE與KV-cache offload等技術,官方宣稱長程RL的端到端速度提升超過3倍。

📊 跑分表現:落後GPT-6 Astra與Claude Opus 5,但成本更低

在程式碼相關評測上,StepFun報告Step 5 Preview在DeepSWE v1.1拿下67.7分,StepCodeBench(StepFun自家基準)49.0分,ProgramBench 80.5分;GPT-6 Astra與Claude Opus 5在這三項上都領先。值得留意的是,測試時Step 5 Preview以「High」努力等級運行,而對手是以「Max」等級運行。

StepFun另外公佈了兩組各持續24小時的agent實驗:第一組將H100 kernel調校至508 TFLOPS,略高於Claude Opus 5的493 TFLOPS;第二組透過自動化後訓練,把Qwen3-30B-A3B在AIME24上的分數從53.3%提升到60%。

獨立評測機構Artificial Analysis給出的Intelligence Index為44分,高於同價位段推理模型的中位數24分;API輸出速度實測為每秒99.8個token。不過素材也點出一個關鍵落差:在該Index測試中,Step 5 Preview生成了160M個輸出token,遠高於92M的中位數,意味著模型偏向冗長的推理過程,會吃掉一部分按token計價帶來的成本優勢。

⚠️ 開放權重還沒到,自架部署得再等等

目前Step 5 Preview僅提供託管API與StepFun平臺訪問,自建部署要等到開放權重釋出。StepFun表示開放權重將於2026年10月15日上線。以參數量換算,600B參數若以BF16精度儲存,光是權重就需要約1.2 TB空間(尚未計入KV cache),屆時想自架部署得準備多GPU伺服器等級的硬體。

🎯 實務啟示

對正在評估agentic工作負載模型選型的工程師來說,Step 5 Preview值得放進候選清單觀察,尤其是它在成本效益上的定位。但在開放權重正式釋出前,目前只能透過API或StepFun平臺試用,自架方案還需要等待,且要留意冗長輸出可能侵蝕實際的token成本優勢。

🔗 來源
- 標題:StepFun Launches Step 5 Preview: A 600B-Total, 27B-Active MoE Model With 1M Context for Long-Horizon Agentic Work
- 作者/機構:Michal Sutter,MarkTechPost
- 連結:https://www.marktechpost.com/2026/09/20/stepfun-launches-step-5-preview/

#StepFun #MoE #LLM #AgenticAI #OpenWeights #AIBenchmark #SoftwareEngineeringAI #LongContext #CostEfficiency #AIModels
