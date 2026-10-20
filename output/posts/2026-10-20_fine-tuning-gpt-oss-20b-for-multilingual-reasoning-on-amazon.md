---
title: Fine-tuning GPT-OSS-20B for multilingual reasoning on Amazon SageMaker HyperPod
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/fine-tuning-gpt-oss-20b-for-multilingual-reasoning-on-amazon-sagemaker-hyperpod/
model: claude-code/sonnet
generated_at: '2026-10-20T20:47:10.841357'
score: 98
---

📌 推理模型滿腦子英文,SFT 與 GRPO 各修對半邊

TL;DR:AWS 實測顯示,開源推理模型 GPT-OSS-20B 即使被要求用法文思考,內心仍會切回英文;SFT 補上能力,GRPO 才做精修。

叫一個推理模型用法文、德文思考,它會先答應,然後默默用英文寫完整段 chain-of-thought。AWS 團隊在 50 題多語推理測試中量化了這個現象:GPT-OSS-20B 只有 22% 的題目用對了目標語言思考,而這 22% 幾乎全來自英文題目本身(英文 100%、法文 0%、德文 10%、西班牙文 0%、義大利文 0%)。對要服務非英語使用者的團隊來說,這不是小問題。

🤔 **模型會答應指令,但思考還是切回英文**

這篇文章要回答一個每個客製化開源模型的團隊都會遇到的問題:監督式微調(SFT)、強化學習的 GRPO,還是兩者都要?作者在 Amazon SageMaker HyperPod 上微調 GPT-OSS-20B 做多語推理,說明何時 SFT 就夠、何時 GRPO 能再加值,並額外用 Qwen2.5-7B 做了一組對照實驗,觀察在不同能力落差的任務上 GRPO 的效果(該對照實驗的細節本文並未提供具體分數)。

🧩 **資料集、訓練棧與兩階段設計**

使用的資料集是 HuggingFaceH4/Multilingual-Thinking,把一份 chain-of-thought 推理資料翻譯成法文、西班牙文、德文、義大利文(加上英文),約 949 筆訓練、50 筆驗證樣本。模型會收到一個「目標推理語言」的 system prompt 指令,要求推理與作答都用該語言完成,藉此覆寫它原本強烈的英文偏好。評測用 50 筆測試案例:5 種語言(EN/FR/DE/ES/IT)各 10 題數學/邏輯題。

訓練基礎設施是 Amazon SageMaker HyperPod 搭配 Amazon EKS 編排:初期的 SFT 與 GRPO 用 PyTorch TRL 函式庫,Qwen 對照實驗則換成 veRL 搭配 Ray、KubeRay 做分散式編排,並用 vLLM 加速 rollout 生成。checkpoint 與資料集放在 Amazon FSx for Lustre,節點間通訊用 Elastic Fabric Adapter(EFA)。所有微調都採用 LoRA,兼顧參數效率與 SFT、GRPO 兩種訓練方式。

作者對兩種技術的核心判斷很簡潔:SFT 教模型一個它原本不會的行為,GRPO 則是在模型「偶爾能做對」的行為上做強化 — 如果目標行為在 base 模型的機率分佈裡根本是零,GRPO 幾乎沒有東西可以強化。

📊 **22% → 100%,再靠 GRPO 補答案語言的 8 分**

SFT 設定為 LoRA r=8、α=16,訓練 1,000 步,用 4 臺 ml.g6e.12xlarge(16 張 L40S 48GB)、FSDP full-shard、bf16 精度加上梯度檢查點,整個任務以 HyperPodPyTorchJob 的形式由 Kueue 管理、透過 hyperpodrun 啟動。SFT 完成後,推理語言正確率從 22%(11/50)衝到 100%(50/50),涵蓋全部五種語言。但「答案語言」(最終答案本身所用的語言)仍只有 62% 正確 — 這是較難啃的部分,因為最終答案通常很短,英文偏好在這裡最強。

由於 SFT 之後推理語言已經 100% 正確,且模型有時候已經能答對答案語言,這代表「有訊號可以強化」,因此作者接著用 GRPO 針對答案語言做強化。做法是從 SFT checkpoint 出發,merge_and_unload 後再疊加一個新的 LoRA(r=8、α=16,約佔 20B 參數中的 13.6M、0.068%),每個 prompt 取樣 K=8 組生成,學習率 1e-6,訓練 10 個 epoch。獎勵函數同時評分答案語言(±5.0)、推理語言(±1.5)與簡潔度(+0.5 或 -1.0),總分落在 -7.5 到 +7.0 之間。結果是 GRPO 在答案語言指標上再拉高 8 分,同時維持推理語言 100% 正確。

💡 **用對工具,取決於能力落差在哪裡**

這篇文章最有價值的結論其實是一個通則:當模型完全不會某個行為時,先做 SFT 把機率分佈從零搬到有;等模型已經「偶爾做對」、只是不穩定時,再用 GRPO 針對那個殘餘的落差做精修。兩者不是二選一,而是接力:SFT 負責打地基,GRPO 負責收尾。

⚠️ **答案語言依然是最難的一塊**

即使 SFT 把推理語言徹底解決,GRPO 加持後答案語言也只提升 8 分,顯示「最終輸出短、英文先驗最強」的部分,比起長篇的 chain-of-thought,更難被微調完全扳正。

🎯 **給正在客製化開源模型團隊的啟示**

遇到「模型完全不會」的行為落差,先做 SFT;遇到「模型偶爾會、但不穩定」的落差,再上 GRPO 做強化,與其一開始就上重型的 RL pipeline,不如先判斷清楚能力落差屬於哪一種,再對症下藥。

🔗 **來源**
- 標題:Fine-tuning GPT-OSS-20B for multilingual reasoning on Amazon SageMaker HyperPod
- 作者/機構:Mijanur Palash,AWS ML
- 連結:https://aws.amazon.com/blogs/machine-learning/fine-tuning-gpt-oss-20b-for-multilingual-reasoning-on-amazon-sagemaker-hyperpod/

#GPTOSS #FineTuning #GRPO #SFT #MultilingualNLP #AmazonSageMaker #LoRA #ReinforcementLearning #LLM #AWSMachineLearning
