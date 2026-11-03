---
title: Keep Distributed Training Running with Automated Workload Recovery
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/keep-distributed-training-running-with-automated-workload-recovery/
model: claude-code/sonnet
generated_at: '2026-11-03T00:09:09.726005'
score: 82
---

📌 【NVIDIA 開源】10000張GPU的訓練任務，為什麼永遠「跑不完一天」

TL;DR：NVIDIA開源Recovery服務，自動偵測、歸因並重啟故障的分散式訓練工作。

就算每張GPU單日故障機率低到只有0.1%，一個橫跨10,000張GPU的訓練任務，當天完全不中斷的機率也只剩下約0.005%。規模一拉大，稀有的故障就變成了日常。

🤔 每個中斷都能處理,但累積起來就是災難

分散式AI訓練規模擴大後，硬體與軟體依賴鏈上的故障會越來越頻繁地打斷訓練進度：一個停滯的rank可能觸發NCCL timeout，一個GPU節點可能對scheduler失去回應，一個straggler可能拖慢整個任務。單獨來看,每種中斷都能處理，但累積的影響與恢復overhead，才是決定系統能把多少wall-clock時間轉換成實際訓練進度（goodput）的關鍵。當這類恢復必須覆蓋叢集上的每一個訓練任務、全天候進行時,人工處理就不可能跟上：每次中斷都要分析log、定位故障、從checkpoint重啟,而受影響的GPU在恢復期間只能閒置。

🧩 四階段恢復迴圈，疊加在既有的健康監控之上

NVIDIA Recovery是NVIDIA DSX OS模組化軟體組合中的一個開源、workload層級服務，定位是整個健康與韌性堆疊中一個獨立的協調層：break-fix自動化負責找出故障節點、移出服務並安排硬體維修;NVRx這類framework層級的函式庫在單個訓練任務內提供恢復、hang偵測與straggler緩解，但需要使用者自行為自己的workload設定；Slurm這類cluster workload manager負責資源分配、排隊與container執行。NVIDIA Recovery要解決的是另一個協調問題：把故障歸因到真正原因、決定受影響任務是否要重啟、在哪裡重啟，並對共用基礎設施的多個workload採取一致的行動。

恢復迴圈分四個階段：
1. Detect：Anomaly Detector結合application log與scheduler訊號，辨識crash、hang與straggler，能辨認PyTorch與NCCL錯誤、CUDA錯誤與interconnect故障模式；進度訊號消失或出現已知的通訊hang模式代表可能hang住，相對近期基線持續的throughput下降則代表可能有straggler。
2. Attribute：利用偵測階段收集到的scheduler訊號與application log對中斷分類，並指引恢復動作；若整合NVIDIA Attribution,可進一步區分硬體故障、系統軟體問題與應用程式bug，這些證據會用來決定節點排除範圍，也會豐富稽核紀錄。團隊也可以接自己的歸因服務，或獨立採用NVIDIA Recovery。
3. Isolate：Anomaly Remediator執行恢復建議，把涉事節點排除在後續重啟嘗試之外，或在重試已無意義時直接停止workload，並持續追蹤涉事節點避免故障重演；另外有一個watchdog安全網，當恢復決策耗時過長或失敗時，允許正常排程繼續進行，避免workload無限期等待。
4. Restart or Stop：scheduler整合透過Advisor API執行NVIDIA Recovery的建議,重啟workload或停止沒有意義的重試；重啟時，應用程式會依其既有的重啟邏輯從最後一次儲存的checkpoint繼續。

📊 Meta 24,000張A100的11個月觀察,與NVIDIA自家叢集的實測數據

文中引用一項針對Meta 24,000張A100 GPU、長達11個月的研究：硬體故障只打斷了不到1%的任務，但這些任務卻佔了19%的GPU執行時間——代表規模最大、跑最久的任務反而最容易受影響。NVIDIA自己的生產觀察顯示，7月9日到10月9日間，Recovery在一個訓練叢集上監控將近200個任務／天，記錄約8,550次異常偵測，平均偵測延遲69秒、平均恢復動作延遲94秒，整套流程不依賴個別工程師或各使用者自訂的恢復安排。

💡 模組化設計，可以單獨採用也可以互相搭配

這套健康與韌性堆疊的各層彼此獨立運作，沒有硬依賴：Kubernetes環境可以用NVSentinel監控GPU健康指標與XID事件並自動cordon、drain故障節點；Slurm站點多半用自訂的prolog／epilog script檢查節點健康，Slinky專案的slurm-operator則在Kubernetes上執行Slurm時原生支援並注入同樣的script。對已經在用NVSentinel或NVIDIA Health Validation的叢集，NVIDIA Recovery幾乎不需要改動既有健康流程就能整合；對已經在用NVRx的環境，NVIDIA Recovery補上的是in-job重啟碰不到的那一塊：跨workload的生命週期管理與節點排除。搭配NVIDIA Attribution時，還能取得更豐富的跨層診斷verdict,強化稽核紀錄。

⚠️ 恢復動作的延遲,不等於訓練恢復生產力的時間

文中特別提醒，恢復動作延遲（recovery-action latency）在自動化動作完成時就算結束，但訓練真正恢復到有生產力的狀態，還要看後續的排程與checkpoint還原需要多久——這部分不包含在前述的69秒／94秒數字裡。

🎯 實務啟示

對同時跑大量小型與大型分散式訓練任務的叢集來說，NVIDIA Recovery處理的是兩種不同的痛點：小任務數量多，中斷累積起來會拉高維運負擔；大任務一旦中斷，影響的GPU數量更多，恢復成本也被放大。對已經在用Slurm、NVSentinel或NVRx的團隊，這套服務設計成可以用既有的health workflow與Advisor API整合，而不是要求整套換掉。

🔗 來源
- 標題：Keep Distributed Training Running with Automated Workload Recovery
- 作者／機構：Elizabeth Goodman，NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/keep-distributed-training-running-with-automated-workload-recovery/

#NVIDIA #DistributedTraining #MLOps #GPU #OpenSource #Slurm #AIInfrastructure #FaultTolerance #Goodput #ClusterComputing
