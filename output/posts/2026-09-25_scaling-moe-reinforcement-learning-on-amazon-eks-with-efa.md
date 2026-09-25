---
title: Scaling MoE reinforcement learning on Amazon EKS with EFA and DeepEP with 40%
  more throughput
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/scaling-moe-reinforcement-learning-on-amazon-eks-with-efa-and-deepep-with-40-more-throughput/
model: claude-code/sonnet
generated_at: '2026-09-25T20:43:48.816355'
score: 101
---

📌 【AWS實戰】用EKS、EFA與DeepEP幫MoE強化學習訓練提速40%

TL;DR：AWS用EKS、EFA與DeepEP優化MoE強化學習訓練，官方稱吞吐量提升40%。

訓練一個Mixture-of-Experts模型看似靠稀疏化省下了推理成本，但一旦進入強化學習後訓練階段，真正卡住效能的往往不是運算力，而是通訊。

🤔 **MoE的RL後訓練同時撞上三個難題**

對Mixture-of-Experts(MoE)模型做RLHF或GRPO這類大規模強化學習後訓練時，會同時出現三個挑戰：協調rollout生成與policy訓練這兩種異質運算負載、在數百個加速器之間維持高吞吐量的通訊、以及動態協調每個子系統讓彼此保持平衡。

MoE架構已成為把LLM規模擴展到數千億甚至上兆參數、同時靠稀疏性維持推理效率的標準做法，但稀疏性並不會消除訓練端的基礎設施複雜度。標準訓練流程包含pre-training、mid-training、監督式微調(SFT)、以及強化學習(RL)，其中大規模RL訓練對基礎設施的要求特別不尋常，因為它同時混合了彈性的推理工作，與需要高頻寬通訊、緊密耦合的模型訓練。

相較於稠密模型，MoE後訓練多了一個新麻煩：隨著新一代MoE架構為了降低推理成本而變得更稀疏，訓練反而愈來愈被通訊、而非運算力所侷限。這個通訊開銷的主要來源是Expert Parallelism(EP)，它會在裝置之間引入動態的all-to-all token路由，疊加在Tensor Parallelism(TP)、Data Parallelism(DP)、Pipeline Parallelism(PP)原本結構化的通訊模式之上。

在緊密耦合的非同步RL工作負載中，MoE訓練的異質運算與通訊需求，必須和以推理為主的生成端保持平衡：訓練步驟太慢會讓推理worker停滯，推理吞吐量不足又會讓訓練用的加速器閒置。這個挑戰不只出現在GRPO，也出現在以PPO為基礎的RLHF流程裡。PPO通常需要一個critic model來估計價值，GRPO則靠群組相對獎勵(group-based relative rewards)避開額外的critic model，但兩者在基礎設施上的要求其實很類似：大規模rollout生成、緊密耦合的policy訓練、以及高頻寬的跨節點通訊。

🧩 **架構設計：EKS、EFA、S3三層各自獨立擴展**

AWS的做法是把Amazon EKS、EFA(Elastic Fabric Adapter)與Amazon S3組合起來，讓編排(orchestration)、高效能通訊、與持久儲存可以各自獨立擴展。

Rollout生成階段執行的是大規模分散式推理，目標是最大化總吞吐量，而不是把first token時間(TTFT)或token間延遲壓到最低；相對地，policy訓練需要worker以近乎同步(lockstep)的方式推進，就像pre-training或SFT那樣，任何一個延遲高峰或落後的worker都可能讓整個任務卡住，甚至觸發NVIDIA Collective Communications Library(NCCL)逾時。RL系統必須讓這兩種節奏互相匹配，速率一旦不對稱，硬體就會閒置，或是訓練變得不穩定。

需要一起平衡的資源包括加速器運算力、記憶體、以及網路頻寬。Policy訓練是運算密集型，必須跟上rollout生成的節奏；同時分散式推理要管理KV cache容量與token生成，而MoE層又會在token跨裝置路由時加入稀疏、動態的all-to-all通訊，讓記憶體頻寬與運算力的平衡變得更關鍵；reward model在訓練過程中提供回饋，資料搬移又是額外壓力，所有這些子系統都得一起被納入平衡，否則任何一個都可能變成瓶頸。

當RL訓練規模超過單一機器，模型的切分與parallelism群組就會跨越多臺節點，通訊也從高頻寬的機內NVLink fabric轉移到頻寬較低的機間連結；MoE模型會放大這個轉移，因為Expert Parallelism會透過稀疏、細粒度的all-to-all通訊動態路由token，隨著EP的程度提高，這些流量會愈來愈走向機間通訊。AWS的P5、P6加速運算執行個體有兩個主要通訊網域：透過NVSwitch連接的機內NVLink fabric，以及機間的EFA網路。在支援的配置下，EFA搭配NVIDIA GPUDirect RDMA與OS bypass技術，可以讓資料直接在跨執行個體的GPU記憶體緩衝區之間傳輸，減少CPU與作業系統在通訊路徑上的介入。要最佳化RL工作負載的頻寬使用率，關鍵就在於判斷哪些運算適合走EFA、哪些必須留在NVLink fabric內。

具體的叢集拓樸上，Amazon EKS叢集內針對RL流程的每個階段各自劃分獨立的node group：GPU加速執行個體負責rollout生成、reward model推理與policy訓練；CPU執行個體負責environment與前處理任務；記憶體最佳化執行個體則負責承載experience buffer與checkpoint cache，讓生產者與消費者交換資料時不需要把持久儲存直接放進關鍵路徑上。在rollout階段，模型透過與CPU-based environment pod互動來生成樣本，產出的experience會流入記憶體最佳化的buffer中。文章標題也點出，這套架構搭配DeepEP最佳化EP在EFA上的通訊後，達到了40%的吞吐量提升。

💡 **EP打破了原本結構化通訊的假設**

TP、DP、PP的通訊模式相對結構化、可預測；EP不同，它是依照token內容動態決定路由目的地，通訊模式本質上是稀疏且細粒度的，這也是為什麼EFA搭配GPUDirect RDMA的重要性格外突出，把通訊直接留在GPU記憶體之間，減少CPU/OS介入的開銷，對這種動態、大量小封包的通訊型態特別關鍵。而把node group依rollout、policy training、environment、buffer的角色切開，也呼應了前面提到的核心矛盾：rollout要衝吞吐量，policy training要衝同步穩定性，兩者對硬體的要求完全不同，硬綁在同一批node上反而互相拖累。

🎯 **實務啟示**

對正在規模化MoE RL訓練(不論是RLHF/PPO還是GRPO)的團隊來說，這篇文章給出一個可直接參考的分層思路：用EKS依工作角色(rollout推理、policy訓練、環境前處理、experience buffer)切分node group，用EFA加GPUDirect RDMA解決EP帶來的跨節點all-to-all瓶頸，用S3承接資料集、checkpoint與訓練產出，讓編排、通訊、儲存三層可以各自獨立擴展，而不是被綁死在同一種執行個體規格上。

🔗 **來源**
- 標題：Scaling MoE reinforcement learning on Amazon EKS with EFA and DeepEP with 40% more throughput
- 作者／機構：Ashvin Nihalani, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/scaling-moe-reinforcement-learning-on-amazon-eks-with-efa-and-deepep-with-40-more-throughput/

#MoE #ReinforcementLearning #AmazonEKS #EFA #DeepEP #GRPO #RLHF #ExpertParallelism #AWSMachineLearning #DistributedTraining
