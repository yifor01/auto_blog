---
title: Write your own training loop — without managing GPUs — with Amazon SageMaker
  training session APIs
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/write-your-own-training-loop-without-managing-gpus-with-amazon-sagemaker-training-sessions/
model: claude-code/sonnet
generated_at: '2026-10-22T20:52:29.218016'
score: 92
---

📌 不用管 GPU，照樣寫自己的 LLM 訓練迴圈：SageMaker Training Session API

TL;DR：SageMaker 新 API 讓你自寫訓練迴圈，無需自管 GPU 叢集。

微調LLM常常得在「訓練迴圈的控制權」和「維運的簡單程度」之間二選一:標準recipe夠用,就交給全託管服務處理;一旦需要自訂loss、自己的data curriculum、RL reward function,或是上週才發表的對齊演算法,就得自己扛起基礎設施工作來換演算法自由。AWS這次把抽象邊界挪低了一層。

🤔 標準 recipe 不夠用的時候

全託管服務的運作方式是:選base model,給資料跟超參數,其餘全部交給服務處理,適合標準recipe能解決的問題。較不受管理的服務給你更多控制權,代價是自己要管底層infra和訓練框架。只要需要自訂訓練程序,就得承擔那部分infra工作。

🧩 把 forward_backward、optim_step、sample 變成 API 呼叫

Amazon SageMaker AI的serverless model customization現在多了training session API,它抽掉的是運算資源,不是演算法。forward_backward()、optim_step()、sample()這些操作變成SageMaker API呼叫,可以自由組合成SFT、preference optimization、RL,或任何新技術。這些呼叫的對象是一個live、stateful的session,模型持續載入在GPU上、跨step存在,你可以對它打任意多次呼叫。服務負責runtime設定、分散式執行、gradient同步、容錯復原、tenant隔離,以及大規模GPU維運的所有細節。AWS同時發布了SageMaker training sessions cookbook,內含現成的SFT與RL recipe可以直接當訓練迴圈的範本。

API由三個SDK client組成,依序建立:ServiceClient持有平臺層設定(execution role、model package group、S3輸出位置,選填KMS key與VPC設定),負責啟動session;它會建立TrainingClient,負責forward、forward_backward、optim_step、save_weights_for_sampler等訓練與checkpoint操作;TrainingClient再建立SamplingClient,負責sample與compute_logprobs,用於rollout生成與評分。一個active session還會額外提供OpenAI相容的chat completions endpoint,現有的OpenAI client程式碼可以直接拿來取樣。

以GSM8K(約8,500道有單一數字答案的國小數學題)為例,一個最小RL迴圈的單個training step是這樣運作的:先對目前模型呼叫sample,在GPU上生成一批prompt的回應;接著你的Python程式碼對這些輸出打分,可以是verifier、reward model呼叫,或test harness,任何能寫成程式碼的評分方式都行;然後forward_backward與optim_step把分數轉成GPU上的gradient update;最後呼叫save_weights_and_get_sampling_client()刷新sampler,讓下一個step從更新後的模型取樣。sampling、gradient、checkpoint這些操作跑在service管理的GPU上,loop控制與reward邏輯則跑在你自己的機器上。做SFT的話,拿掉sampling和reward步驟,改成對labeled example呼叫forward_backward搭配cross_entropy loss即可,同一組原語就能覆蓋。

💡 按 token 計費，不是按 GPU 時數計費

用量是依處理的token數計費,只有呼叫GPU-bound操作時才算錢。如果reward function在自己機器上跑10秒才打完一批分,那段時間不會計入GPU費用。相比GPU按小時計費,這帶來兩個實務優點:第一,沒有閒置GPU成本,reward計算、資料載入、記錄、debug都發生在計費之外;第二,花費隨資料集和生成量成長,而非隨wall-clock時間或叢集規模成長,讓預算更容易預估、實驗更容易互相比較。對於本地運算量大的工作負載,例如複雜reward model、多工具agentic rollout,或人工在環評估,比起整段session都保留GPU,這樣省下的成本可能相當可觀。

🎯 適用場景與定位

Training session API支援SFT(cross_entropy loss)、RL(ppo、importance_sampling、cispo,也就是GRPO、PPO等group-relative方法),以及preference optimization、distillation等自訂目標,因為這些都是用同一組原語拼出來的。在SageMaker AI的模型客製化選項裡,它的定位介於兩端之間:比全託管的Serverless Model Customization多出許多演算法控制權,又比直接使用SageMaker Training Jobs或SageMaker HyperPod少掉許多維運負擔。文件中示範的真實案例,是用GRPO對GPT-OSS 20B訓練一個LoRA adapter:針對每一題模型生成多個回應,各自打分正確性,表現優於該組平均的回應會被強化;更進一步的真實工作負載,則是對競程題目做RL,生成的程式碼會被拿去跑unit test評分。

🎯 實務啟示：如果訓練流程已經超出「選base model加丟資料」能解決的範疇,又不想自己維運GPU叢集,training session API提供了一個中間選項:自己寫loop、讓SageMaker跑GPU運算,並用token計費取代GPU計費來控制成本,cookbook裡現成的SFT/RL recipe可以直接當起點。

🔗 來源
- 標題：Write your own training loop — without managing GPUs — with Amazon SageMaker training session APIs
- 作者／機構：Nicolas Jourdan, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/write-your-own-training-loop-without-managing-gpus-with-amazon-sagemaker-training-sessions/

#AWS #SageMaker #LLMTraining #ReinforcementLearning #GRPO #FineTuning #MachineLearning #MLOps #GPU #LoRA
