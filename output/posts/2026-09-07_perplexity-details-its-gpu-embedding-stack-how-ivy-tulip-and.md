---
title: 'Perplexity Details Its GPU Embedding Stack: How Ivy, Tulip and ROSE Serve
  pplx-embed'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/05/perplexity-details-its-gpu-embedding-stack-how-ivy-tulip-and-rose-serve-pplx-embed/
model: claude-code/sonnet
generated_at: '2026-09-07T20:46:03.370849'
score: 90
---

📌 Perplexity公開GPU嵌入引擎：Ivy、Tulip與ROSE怎麼分工

TL;DR：Perplexity詳解pplx-embed背後的GPU serving架構，重點不是換模型，而是重用LLM推論的runtime。

多數人以為embedding serving只是把一個小模型丟上GPU跑，Perplexity工程團隊這週發布的Fast Embeddings on GPUs卻指出，真正的效能差距早就不在模型本身——在成熟的Hopper與Blackwell硬體上，各家推論引擎的embedding推論早已收斂，勝負關鍵反而在模型外圍的runtime與harness。

🤔 兩種完全不同的工作負載

Perplexity把embedding serving拆成兩種情境：batch embedding發生在建立或重新索引向量資料庫時，目標是最大化throughput、把成本壓到最低；online embedding發生在查詢當下，一句短查詢必須被快速嵌入。介於兩者之間的是scoring：向量搜尋完成後，要對大批候選文件重新排序，同時兼顧吞吐與延遲。

🧩 不重造引擎，直接借用LLM stack的kernel

最關鍵的架構決策是：Perplexity沒有另外打造一套獨立的embedding引擎。因為embedding模型本質上是小型Transformer，batch embedding的運算特性很像LLM推論裡運算密集的prefill階段，online embedding(常常只有幾個token)則很像記憶體頻寬密集的decode階段。於是團隊直接重用LLM stack裡既有的prefill與decode kernel。

負責處理一個請求的是三個服務：Tulip以先進先出的方式挑選要處理的序列，這個看似簡單的策略背後有實測依據——在Perplexity服務的序列長度下，對這類小型embedding模型而言，dense layer的線性成本主導了attention的平方成本，延遲因此近似正比於token數而非序列數。一旦batch讓GPU吃飽(對次十億參數的模型大約是512個token)，再塞更多序列進去也不會提升效率。文中另外提到，高並發benchmark會計入Ivy的tokenization與網路開銷，顯示Ivy承擔請求路徑上的前處理工作；ROSE則負責CUDA graph管理與attention backend的選擇。

在小batch情境下，CPU端啟動kernel的開銷甚至可能超過GPU本身的執行時間。Perplexity為所有embedding模型建立「全模型」CUDA graph，把每一次kernel launch都包進單一次driver呼叫。因為模型夠小，GPU工作量超過launch開銷的臨界點要到數千token、數十個序列的batch規模才會出現。部分attention實作依賴動態的host端輸入，會擋住全模型graph的擷取，Perplexity團隊為此把相關修改回饋upstream到FlashInfer專案。由於graph必須依每種設定分別擷取，token數會被padding到64或256的倍數桶位，這樣算下來仍會產生數千個graph、每個模型光擷取就要花上數分鐘。解法是lazy capture：每種設定先跑一次eager warmup，直到第二次命中才觸發真正的擷取與replay，代價是啟動階段的p99延遲會變差，換來的是把原本集中的數分鐘eager工作分攤到數小時的服務時間裡。

第二個關鍵元件是LazyTensor，它追蹤一塊page-locked的host buffer，搭配cudaMemcpyAsync與CUDA event。原本呼叫step()必須阻塞等裝置端運算完成，改用LazyTensor後可以直接回傳，讓Rust寫的非同步任務在等待第N個batch結果的同時，讓CPU端繼續排入第N+1個batch，藉此把GPU計算與CPU排程重疊起來。

ROSE本身支援多種處理ragged輸入的attention backend，包括FlashInfer 2、FlashInfer 3與FlashAttention 4。Perplexity表示FlashAttention 4整體較快，但在Qwen系模型的極長序列上，FlashInfer 3反而表現更好，因此backend的選擇是逐案決定，而非固定寫死。值得一提的是，在服務embedding模型時，ROSE完全不建立KV cache，而是直接派發到ragged attention變體，藉此避免padding造成的浪費。

📊 Benchmark設計

Perplexity以vLLM v0.22.0作為對照，統一使用BF16精度、真實模型權重與從評測資料衍生的輸入，並在warmup後驗證輸出的cosine similarity差異落在0.1%以內。整套benchmark分成四組：低延遲embedding(batch為1，測試128／512／4096 token)、低延遲scoring(512 token下測試batch 5／25／50)、高吞吐embedding(batch 100、四個並行行程)，以及高並發embedding(1到16個並行請求，並計入Ivy的tokenization與網路開銷)。文中著重描述了benchmark的設計方式，並未附上具體的對比效能數字。

💡 深入分析：省下一個引擎，換來更聚焦的最佳化

不另建embedding引擎、直接重用LLM stack的決定，本質上是用工程複雜度的取捨換來效能——團隊把心力集中在CUDA graph管理、非同步結果追蹤與Rust請求路徑這幾個真正影響延遲與吞吐的環節，而不是重新發明一套推論框架。

🎯 實務啟示

如果你的團隊也在自建或最佳化embedding serving，這篇文章裡的幾個手法都值得借鏡：用whole-model CUDA graph搭配lazy capture降低啟動成本、用類似LazyTensor的機制把CPU排程與GPU執行重疊、以及依模型與序列長度動態切換attention backend，而不是一套設定打天下。

🔗 來源
- 標題：Perplexity Details Its GPU Embedding Stack: How Ivy, Tulip and ROSE Serve pplx-embed
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/05/perplexity-details-its-gpu-embedding-stack-how-ivy-tulip-and-rose-serve-pplx-embed/

#Perplexity #GPUInference #Embeddings #MLInfra #CUDA #LLMServing #InferenceOptimization #FlashAttention #SystemsEngineering #AIInfrastructure
