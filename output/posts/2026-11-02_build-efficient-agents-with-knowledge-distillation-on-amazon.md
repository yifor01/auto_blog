---
title: Build efficient agents with knowledge distillation on Amazon SageMaker AI
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-efficient-agents-with-knowledge-distillation-on-amazon-sagemaker-ai/
model: claude-code/sonnet
generated_at: '2026-11-03T00:01:04.902328'
score: 96
---

📌 把前沿模型的購物 Agent 能力蒸餾進小模型：AWS SageMaker 實戰

TL;DR：用 SeqKD 把 GLM-5.3 教師模型的 Agent 行為蒸餾進 Qwen3.5-4B 學生模型，兼顧品質與成本。

一個購物助理 agent 聽到「兩美元以下、評分4.5星以上店家的黑色腰包」,背後跑的不是一次模型呼叫,而是一整個迴圈:搜尋、檢視結果、修正、驗證、決策。每完成一次任務,可能就是對前沿模型的多次付費呼叫,規模一旦擴大,成本就會侵蝕專案的 ROI。

🤔 **換小模型便宜,但品質掉了怎麼辦**

讓 agent 改用更小的模型,回應更快、主機成本更低,問題是小模型通常達不到任務要求的品質,這也是當初選用大模型的原因。知識蒸餾（knowledge distillation）的作法,是把大型「教師」模型的行為轉移給小型「學生」模型,讓學生在維持多數品質的前提下,享有小模型的速度與成本。

🧩 **SeqKD：只需要教師的文字輸出**

文章聚焦 sequence-level knowledge distillation（SeqKD）:教師模型生成高品質回應,學生模型再用 supervised fine-tuning 在這些回應上訓練。SeqKD 只需要教師的文字輸出,不需要存取教師的 logits,也不需要強化學習基礎設施,因此即使教師是封閉或僅提供 API 的模型也能使用。

對 agent 而言,教師產出的「序列」不是一段散文,而是一條 trajectory:推理、工具呼叫與其回傳結果交織而成的有序過程,每一步都依賴前面所有步驟。讓學生在整條 trajectory 上訓練,學到的是導向每個動作的推理過程與整套多步驟行動,而不只是單段答案文字。文章指出 SeqKD 適用的情境包括:手上有輸入但缺高品質目標輸出、教師只能透過 API 存取、或是想要一個低成本但有效的推理遷移起點（DeepSeek-R1 的蒸餾模型就是用教師推理軌跡做 SFT 的知名案例)。

**案例管線**:前沿教師模型 GLM-5.3（部署在 Amazon Bedrock,開啟 reasoning,temperature 1.0)扮演 ShoppingBench 的 agent 角色,在訓練題目上生成 trajectory;ShoppingBench 自帶的評分器（scorer)只保留真正解出任務的 trajectory（即 rejection sampling);每條通過篩選的 trajectory 逐步編碼後,用於以 Amazon SageMaker AI model customization 進行 serverless 的 supervised fine-tuning,訓練出 Qwen3.5-4B 學生模型;最後在保留的 ShoppingBench 測試集上評估,並透過 SageMaker AI Inference 的 real-time endpoint 跑完整的工具呼叫迴圈。

📊 **資料怎麼來的**

ShoppingBench 提供 750 個合成購物問題,分成 product、shop、voucher 三種意圖各 250 題,每題都有隱藏的標準答案與成功條件;文章將題目依固定索引切成 426 題訓練集與 324 題保留評測集（product 103、shop 105、voucher 116),確保兩邊不重疊。教師在約 270 萬件商品的目錄中搜尋、檢視候選商品、確認是否符合條件,針對每個訓練題目取樣兩次,合計產生 850 條 trajectory,再用 ShoppingBench 的評分器篩掉失敗的執行。採用 temperature 1.0 而非貪婪解碼（greedy decoding)是刻意設計,目的是讓兩次取樣探索不同的查詢與推理路徑,提高至少有一條成功 trajectory 的題目比例,也讓學習素材更多樣。

⚠️ **這一步只是資料生成,不是完美複製**

SeqKD 本質上是用教師實際產生的樣本去逼近其完整輸出分佈,而非精確匹配,因為可能的序列空間太大,窮舉不可行。文章也坦言,這個 rejection sampling 步驟能成立的前提是教師「不需要每次都對,只要對的次數夠多,值得被模仿即可」。

🎯 **實務啟示**

如果你的任務有程式化的評分器（programmatic scorer),就可以用前沿模型當教師,大量生成候選 trajectory 並只保留解出任務的部分,不必依賴既有的高品質標註,也適用於只能透過 API 存取、無法拿到 logits 或權重的教師模型。這讓 SeqKD 成為把 agent 行為從昂貴的前沿模型搬進可負擔的小模型時,最具可攜性的切入點。

🔗 **來源**
- 標題：Build efficient agents with knowledge distillation on Amazon SageMaker AI
- 作者／機構：Giuseppe Zappia，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/build-efficient-agents-with-knowledge-distillation-on-amazon-sagemaker-ai/

#KnowledgeDistillation #SeqKD #AmazonSageMaker #AIAgents #LLMFineTuning #ModelCompression #AWSMachineLearning #AgenticAI #Qwen #ShoppingBench
