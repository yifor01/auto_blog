---
title: Full Fine-Tuning (FFT) on SageMaker AI Serverless Model Customization
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/full-fine-tuning-fft-on-sagemaker-ai-serverless-model-customization/
model: claude-code/sonnet
generated_at: '2026-11-19T23:55:34.680091'
score: 79
---

📌 SageMaker Serverless全量微調上線:資料衝破10萬筆,LoRA天花板在哪裡?

TL;DR:AWS SageMaker AI Serverless Model Customization 新增全量微調(FFT),資料量達10萬+筆時語義正確率衝到90%,且免GPU維運。

LoRA 長期被當作微調 LLM 的預設答案,省 GPU、省時間。但如果你的任務夠複雜、資料集夠大,增加 LoRA 的 rank 真的能追上完整微調的準確率嗎?AWS 的實驗給出了否定的答案。

🤔 **LoRA 撞上的不是參數量天花板,是秩本身的限制**

LoRA 這類模型客製化方法,透過凍結預訓練權重、注入小型低秩矩陣對(low-rank matrices)來減少可訓練參數量,這對簡單的調整很有效。但隨著任務複雜度上升、資料集規模擴大到數萬筆以上,LoRA 會碰到一個準確率天花板:即使提高 rank(也就是增加可訓練參數量),也無法縮小與標準完整微調之間的差距。這揭示了差距的根源並非參數量不足,而是低秩結構本身就無法捕捉深度任務調適所需的完整權重變化複雜度。

🧩 **FFT 同時更新所有參數,而且切換只需改一行程式碼**

Full Fine-Tuning(FFT)同時更新模型全部參數,克服低秩限制,讓 LLM 能完整吸收複雜的領域知識。它均勻修改模型的權重矩陣,運用權重矩陣的完整表達能力,而不是把更新侵入限制在一個小子空間裡,也不會出現低秩方法那種侵入式、局部化的失真。結果是更強的收斂、跨層更好的 activation 對齊,以及一個既能忠實反映目標任務分佈、又保留預訓練知識豐富度的模型。

SageMaker AI Serverless Model Customization 現在支援 FFT,不需要 GPU 佈建、叢集設定或分散式訓練配置,指定基礎模型、資料集與超參數即可,服務會以 serverless 方式自動處理運算配置與 checkpoint 管理。程式碼層面上,從 FFT 切換到 LoRA 只需把 `TrainingType.FULL` 改成 `TrainingType.LORA`,其他程式碼完全不變。

實驗設定上,AWS 在 Qwen3-4B 基礎模型上,使用 Magicoder-Evol-Instruct-110K 資料集(11萬筆涵蓋演算法設計、除錯、資料結構與系統程式設計的程式碼 instruction-response 配對)進行 SFT(Supervised Fine-Tuning),以 90/5/5 比例切分:9.9萬筆訓練、5,500筆驗證用於監控收斂與訓練 loss、5,500筆保留作為無偏見的最終評估測試集。LoRA 與 FFT 兩個方法在實驗中使用相同的 prompt、目標與評估程式碼。

📊 **資料量衝破10萬筆,FFT 語義正確率達90%**

當訓練資料擴展到10萬+筆時,FFT 在以 LLM-as-Judge 衡量的語義正確率上達到90%。評估採用三種互補方法:
- LLM-as-Judge:用 Amazon Nova Pro 當自動評審模型,讀取生成的程式碼與原始 prompt,判斷解法是否邏輯正確
- PRIMECODE:用 BLEU(n-gram 精確度)、ROUGE-1/2/L(召回導向的重疊度)、F1(精確度與召回率平衡)等決定性文字相似度指標,衡量生成程式碼與參考解答的吻合度,具備高度可重現性,適合做控制變因的消融研究
- MMLU:檢驗一般知識保留程度

雷達圖比較顯示,base model 在各維度分數都偏低,LoRA 呈現均衡的明顯提升,而 FFT 在每個維度都更進一步,在 BLEU 與 ROUGE-2 上的領先尤其明顯。

💡 **這不是單一指標的偏差,是全秩最佳化的根本優勢**

FFT 的品質優勢隨資料規模擴大而擴大,而且在 LLM-as-Judge、PRIMECODE、MMLU 三種完全不同性質的評估方法上都一致領先,說明這是全秩最佳化本身帶來的根本優勢,不是某個指標的巧合。

⚠️ **限制**

素材並未提供 FFT 在小型資料集或簡單任務上的表現數據,官方強調的優勢場景聚焦於「複雜任務且資料量充足」的情境;素材也沒有給出 FFT 相對 LoRA 的具體訓練時間或成本對比數字。

🎯 **實務啟示**

如果你的微調資料集已經超過10萬筆、任務本身也足夠複雜(例如程式碼生成),這份實驗結果值得作為選擇 FFT 而非 LoRA 的參考依據。更重要的是,Serverless 架構把切換訓練方法的成本壓到一行程式碼,團隊可以直接拿自己的資料集,用 LLM-as-Judge、PRIMECODE、MMLU 三種評估方法跑一輪 A/B 比較,再決定是否值得多花的運算成本。

🔗 **來源**
- 標題:Full Fine-Tuning (FFT) on SageMaker AI Serverless Model Customization
- 作者/機構:Sandeep Raveesh-Babu @ AWS
- 連結:https://aws.amazon.com/blogs/machine-learning/full-fine-tuning-fft-on-sagemaker-ai-serverless-model-customization/

#AWS #SageMaker #FineTuning #LoRA #LLM #MachineLearning #Qwen #ModelCustomization #MLOps #DeepLearning
