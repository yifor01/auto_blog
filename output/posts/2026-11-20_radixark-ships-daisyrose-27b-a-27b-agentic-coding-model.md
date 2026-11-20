---
title: RadixArk Ships DaisyRose-27B, a 27B Agentic Coding Model Trained With Reinforcement
  Learning Only
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/20/radixark-daisyrose-27b-agentic-model/
model: claude-code/sonnet
generated_at: '2026-11-20T23:20:07.259287'
score: 96
---

📌 RadixArk推出DaisyRose-27B：全程RL打造的開源Agentic Coding模型

TL;DR：27B模型完全跳過SFT與蒸餾，純靠強化學習後訓練，Terminal Bench分數翻倍。

近來開源模型的後訓練幾乎離不開SFT加蒸餾這套組合拳，但RadixArk這次反其道而行：他們的第一個開放權重模型DaisyRose-27B，宣稱完全只用強化學習（RL）後訓練，連SFT都沒有。這在工程細節齊全的模型卡與技術部落格裡，是個值得拆開來看的案例。

🤔 從Qwen3.8-27B出發，架構原封不動

DaisyRose-27B是從Qwen3.8-27B post-trained而來，模型卡明確寫出訓練只用了RL，沒有SFT也沒有distillation，並以Apache 2.0授權發布，可直接作為base模型的drop-in replacement。底層架構維持Qwen3.8-27B不變：64層decoder，採3:1排列，即3層Gated DeltaNet linear-attention搭配1層full-attention交替出現；hidden size為5,120；另外有一個27層的vision encoder處理影像輸入，以及一層multi-token-prediction（MTP）layer用於支援推測性解碼（speculative decoding）。輸入支援文字與影像，輸出為文字，且是一個thinking model。

🧩 1,200道任務、144張H200跑18天

RadixArk與Eigent AI合作，從數千個候選任務中篩選出約1,200道精心設計的任務，每一道都針對base模型的特定失敗模式。每個sandbox嘗試允許最長1.5小時、100次以上的tool call、256k以上的輸出token，agent session甚至可以拉到1M token。

訓練框架是RadixArk自家開源的RL框架Miles，採全異步（fully asynchronous）模式運行，使用144張H200 GPU跑了18天，其中128張負責agent推理、16張負責訓練，總計63,000 GPU小時。RadixArk表示其內部backend達到37% MFU，而一個以Megatron為基礎的開源trainer只有16%；端到端吞吐量是16.8k tokens/s，對比8.3k tokens/s，提速2.0倍，換算下來GPU時間減少57%。

Sandbox環境則跑在AgentENV上：從9月中到11月中，RadixArk報告共產生約944,000個sandbox，尖峰並發數達1,566，9週內的建立成功率為99%，成本比主流雲端sandbox供應商低約80%。

📊 Terminal Bench翻倍，但對上更大模型互有勝負

所有分數皆為RadixArk自行報告（取BF16與FP8兩種跑法中較高者）。最亮眼的是Terminal Bench 4.1，pass@1從5.6分跳到12.0分，翻了一倍以上。程式碼相關的進步較為穩定：DeepSWE v1.1提升4.0分，SWE Bench Pro v2提升3.4分（該數據可追溯至arXiv 2611.16289）。知識類任務的提升則較小，HLE僅+0.4、GPQA Diamond+1.5。

和更大的模型相比，結果並非全面領先：總參數309B的MiMo V2.6 Flash在Terminal Bench 4.1上以16.1分領先；總參數594B的Inkling 2 Small則在DeepSWE拿下72.1分、HLE拿下44.1分。在RadixArk自己列出的9模型比較表中，DaisyRose-27B只在IFBench這一項排名第一。

⚠️ 侷限

知識型任務的提升幅度不大，且面對規模大得多的模型時表現並非全面佔優；所有數據均為廠商自行提供，尚未見第三方復現。

🎯 實務啟示

模型權重已上傳Hugging Face，提供BF16、FP8、NVFP4與GGUF格式，其中NVFP4需要Blackwell GPU才能跑。官方建議搭配SGLang並啟用DSpark推測性解碼（draft model為Qwen3.8-27B-DSpark），也可以用`vllm serve "RadixArk/DaisyRose-27B"`跑vLLM。thinking mode建議的取樣參數是temperature 1.0、top_p 0.95、top_k 20。對於想在agentic coding場景做RL後訓練實驗的團隊，Miles這套開源非同步RL框架與其異步推理/訓練比例的設計,值得作為參考案例研究。

🔗 來源
- 標題：RadixArk Ships DaisyRose-27B, a 27B Agentic Coding Model Trained With Reinforcement Learning Only
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/20/radixark-daisyrose-27b-agentic-model/

#RadixArk #DaisyRose27B #ReinforcementLearning #AgenticCoding #OpenWeights #Qwen #LLM #SGLang #SpeculativeDecoding #MachineLearning
