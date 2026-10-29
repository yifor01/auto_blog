---
title: 'Grace Blackwell needs a new scheduler: 27% more usable GPUs from the same
  racks'
source: Hacker News
url: https://skypilot.ai/blog/grace-blackwell-needs-a-new-scheduler
model: claude-code/sonnet
generated_at: '2026-10-29T22:11:05.307105'
score: 87
---

📌 NVIDIA NVL72機架：排程不對,27%算力就蒸發

TL;DR：NVLink擴展到整機架後,多節點訓練/推論效能幾乎全看排程器能否守住機架局部性。

把本該走NVLink的分散式訓練任務改成跑InfiniBand,效能直接掉43%。這不是極端案例,而是機架排程沒做好時的常態代價——而這正是SkyPilot這篇文章想解決的問題。

🤔 大規模訓練,本質上是個通訊問題

要在數千張GPU上訓練模型,必須回答兩個問題：如何切分模型讓它能跑起來(Tensor Parallelism切權重矩陣、Expert Parallelism把MoE的專家分散到不同GPU、Pipeline Parallelism按層切分),以及在既定運算預算下能跑多少份平行副本(Data Parallelism)。其中Tensor Parallelism每個transformer層的前向傳播都需要兩次all-reduce,這兩次同步卡在關鍵路徑上無法被運算重疊掩蓋,因此通常必須留在NVLink——Hugging Face實測改走InfiniBand後,訓練吞吐量掉了43%。Expert Parallelism則在每個MoE層需要兩次all-to-all通訊(dispatch與combine),當模型加入更多MoE層、每個token路由到更多專家時,未最佳化的通訊甚至能吃掉高達60%的訓練時間。

推論端也面對同樣問題：把模型權重切得更細,能釋放更多記憶體給KV cache。文中引用的vLLM基準顯示,Llama-3.1-70B從單張H100切到兩張H100做Tensor Parallelism,KV cache容量增加13.9倍,吞吐量提升3.9倍。而WideEP(跨節點的Expert Parallelism)雖然能大幅降低每張GPU要存的專家數,代價是all-to-all通訊範圍變大——在標準8-GPU伺服器上,Expert Parallelism群組最多只能擴到8張GPU,一旦超過就得走InfiniBand,單GPU頻寬直接掉18倍。

🧩 機架變成新的伺服器

NVIDIA的NVL72系統把NVLink的範圍從單一節點擴展到整個機架：每張GPU有18個NVLink埠,每埠雙向100GB/s,加總單GPU頻寬達1.8TB/s;機架內18個NVSwitch晶片各自接入全部72張GPU的NVLink線路,讓機架內部總頻寬達到130TB/s。這個拓撲是完全非阻塞的(fully non-blocking),代表機架內任何一張GPU都能以相同頻寬、相同延遲跟其他任何一張GPU通訊。

效果立竿見影：在Expert Parallelism場景下,64-way的專家並行若放在標準8-GPU伺服器上,all-to-all流量得跨越多臺InfiniBand互連;但在NVL72上,全部64張GPU都留在同一個NVLink域內,通訊瓶頸基本消失。在推論端,服務DeepSeek-R1這類模型時,GB200 NVL72用32-way Expert Parallelism能跑出比8-GPU B200伺服器(受限於只能做8-way)高出4.4倍的單GPU吞吐量。

⚠️ 機架全開未必是最佳解

文章也指出一個反直覺的張力：把整個18節點的機架都塞滿工作負載雖然能最大化利用率,但隨著硬體故障讓節點離線、不同時間結束的任務把空閒容量打散到各個機架,維持「機架局部性」(rack-locality)反而變得更困難——用更少節點反而可能提升可靠性。這部分的具體取捨文章沒有給出完整結論,只點出了這個矛盾存在。

🎯 實務啟示

對正在規劃多節點訓練或推論叢集的工程團隊,關鍵是排程器要能感知拓撲：把Tensor Parallelism和Expert Parallelism的通訊路徑釘死在NVLink域內,Data Parallelism則可以放寬到跨機架用InfiniBand。SkyPilot這篇文章提到自家平臺透過拓撲感知的放置策略、硬體故障時的原地復原,以及共用叢集的自動碎片整理來維持這種局部性,這也是文章想強調的設計方向:排程不再只是分配GPU數量,而是要分配「正確拓撲位置」的GPU。

🔗 來源
- 標題：Grace Blackwell needs a new scheduler: 27% more usable GPUs from the same racks
- 作者／機構：wondersky（Hacker News）
- 連結：https://skypilot.ai/blog/grace-blackwell-needs-a-new-scheduler

#NVIDIA #NVL72 #GPUScheduling #DistributedTraining #MixtureOfExperts #TensorParallelism #ExpertParallelism #AIInfrastructure #NVLink #MLOps
