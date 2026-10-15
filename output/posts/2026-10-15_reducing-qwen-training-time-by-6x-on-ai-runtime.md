---
title: Reducing Qwen training time by 6x on AI Runtime
source: Databricks
url: https://www.databricks.com/blog/reducing-qwen-training-time-6x-ai-runtime
model: claude-code/sonnet
generated_at: '2026-10-15T20:37:52.405000'
score: 103
---

📌 Databricks實測:微調Qwen 27B速度提升6倍,從7.7小時到77分鐘

TL;DR:Databricks靠kernel融合與資料封裝,把Qwen微調時間砍成六分之一。

如果有人跟你說他的GPU使用率長期維持在98%,你可能會以為訓練已經把硬體用到極致了。但Databricks工程團隊發現,這個數字其實會騙人。

🤔 GPU使用率98%,為什麼還有最佳化空間
GPU使用率這個指標只計算GPU「有沒有在做事」的時間比例,不代表GPU活動時做得有多好。Databricks團隊在AI Runtime(AIR)上微調Qwen 3.8 27B模型,搭配transformers函式庫與HuggingFaceH4/ultrachat_200k這個SFT資料集,baseline跑完整資料集需要7小時44分,訓練速度為9,396 tok/s,期間GPU平均使用率98%。

為了搞清楚使用率背後真正發生了什麼,團隊用torch的trace機制做更深入的剖析(並限制step數以快速取樣)。單一step的結果顯示:CPU耗時14.4秒,呼叫次數高達1,714,382次;GPU耗時10.3秒,包含269,448個operations。其中batch matrix multiplication這個kernel在一個step內就被呼叫超過30,000次,同時批次中還存在大量為了湊成矩形張量而產生的padding浪費。

🧩 融合kernel與重新設計batch,兩個關鍵最佳化
第一個最佳化是kernel融合。所謂fused kernel,是把多個小的GPU kernel合併成一個單位,藉此避免GPU高頻寬記憶體與晶片上更高頻寬記憶體之間的昂貴搬運,同時也讓GPU核心的排程更有效率。團隊觀察到Qwen模型裡大量的小operation其實來自非標準的gated delta network層,而這類層剛好有causal-conv1d與flash-linear-attention這兩個套件可以把許多逐層的operation融合起來。要知道哪些kernel可用,其實transformers函式庫對Qwen的實作本身就會告訴你支援哪些kernel。

取得這些kernel有兩種方式:一是在建置容器時就把所有kernel安裝好(團隊推薦這個作法,尤其是搭配docker容器一起使用,可以減少job啟動時間);二是使用kernelhub,雖然方便,但由於kernel常常與特定版本的torch、CUDA綁定,你的環境未必有對應版本可用,此時transformers模型會悄悄退回未最佳化的kernel,效能大打折扣卻不會有任何警示。安裝flash-linear-attention與causal-conv1d這兩個Python套件後,端到端時間改善了3.7倍,降到2小時5分。新的profiling結果顯示,原本的elementwise運算已經被對應的融合kernel取代,總operation數量也減少了15倍(CPU耗時降到3.9秒、118,316次呼叫;GPU耗時降到3.9秒、18,060次呼叫)。需要留意的是,訓練時forward與backward兩個方向都需要對應kernel,但部分kernel只為了加速推理而實作,訓練時未必能直接套用。

第二個最佳化是重新設計batch的組織方式。預設的batching使用2D矩形張量,把每個batch填到8,192 token(這是記憶體允許的最大值),但這種做法會把大量空間浪費在padding上。如果Qwen只用標準attention機制,torch的NestedTensor已經能很好地支援、藉由完全移除padding來省下這筆成本,但flash-linear-attention只支援較傳統的1D packed張量。問題是不能直接把1D張量丟進模型——這種做法在預訓練階段或許可以接受,但微調時必須確保同一個樣本中的token只會互相關注,不能跨樣本attend。解法是把正確的樣本position_ids傳入模型,模型會把這些資訊傳給融合過的attention kernel,讓它套用正確的attention mask。

📊 這個改動,把訓練時間再砍36%
做完這個看似簡單的改動,訓練時間從2小時5分降到1小時17分。這裡有個明確的trade-off:輸入pipeline會變得更複雜,出錯的風險也會提高,一旦出錯可能影響模型品質;但在這個案例裡,36%的時間節省被認為值得冒這個風險。團隊也提到另一種減少padding的做法——維持原本的batching機制,但把所有輸入依長度排序以縮小padding,只是這麼做可能讓相鄰樣本之間產生意外的相關性,帶來訓練上的偏誤。整體而言,這個資料封裝(packing)的改動帶來1.6倍的訓練速度提升。

💡 六倍加速背後的三件事
把整個過程串起來看,6倍加速(從7小時44分到1小時17分)來自三件事:先衡量真正重要的指標,而不是只看GPU使用率,找出模型實際把時間花在哪裡;用像Flash Linear Attention這類已知函式庫做kernel融合;以及重新設計batch的資料餵入方式。

🎯 實務啟示
Databricks表示,AI Runtime已經內建了許多這類最佳化:基礎環境預先綁好最新版CUDA與flash attention,自動追蹤GPU使用率、溫度與健康狀態等核心指標,並確保torch版本與profiler保持在最新狀態;內部agent「Genie Code」也會主動尋找類似的最佳化機會,而透過UCVolumeDataset讀取Databricks上的資料也經過最佳化。對正在微調大型語言模型的工程師來說,這個案例提醒:GPU使用率高不代表沒有最佳化空間,真正該做的是用profiling工具找出kernel層級的浪費,再評估kernel融合與資料封裝這類改動是否值得承擔額外的複雜度與風險。

🔗 來源
- 標題:Reducing Qwen training time by 6x on AI Runtime
- 作者/機構:Databricks
- 連結:https://www.databricks.com/blog/reducing-qwen-training-time-6x-ai-runtime

#Qwen #LLM #FineTuning #Databricks #GPUOptimization #FlashAttention #MachineLearning #DeepLearning #MLOps #PerformanceEngineering
