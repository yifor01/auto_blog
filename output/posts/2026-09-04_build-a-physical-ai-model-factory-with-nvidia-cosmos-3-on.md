---
title: Build a Physical AI model factory with NVIDIA Cosmos 3 on SageMaker HyperPod
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-a-physical-ai-model-factory-with-nvidia-cosmos-3-on-sagemaker-hyperpod/
model: claude-code/sonnet
generated_at: '2026-09-04T19:46:50.340194'
score: 96
---

📌 NVIDIA Cosmos 3打造具身AI的模型工廠

TL;DR：AWS展示如何用單一模型家族Cosmos 3，在SageMaker HyperPod上跑完具身AI的整條資料到部署迴圈。

一臺機器人或自駕車要「能理解環境並行動」，靠一次訓練job是做不到的，需要的是一條持續運轉的pipeline。AWS這篇文章示範了如何用NVIDIA Cosmos 3，在SageMaker HyperPod上打造這樣的Physical AI model factory。

🤔 **具身AI需要的是一個不會停的迴圈**

打造機器人或自駕車（AV）系統的團隊，跑的從來不是單一次微調工作，而是一個迴圈：擷取真實資料、整理、用合成資料擴增、post-train、在閉環模擬中評估、部署policy、收集更多資料，再重新開始。文章將這個迴圈畫成四階段飛輪：(1) 將真實世界的具身AI資料（DROID、BridgeData2、AV感測器紀錄）擷取並整理進Amazon S3與Amazon FSx for Lustre上的共用語料庫；(2) 由Cosmos3-Super擔任teacher產生合成資料以擴增語料庫；(3) 結合合成與真實資料，post-train出可部署的Cosmos3-Nano policy，並在Nano與Super兩個tier上都套用視覺微調；(4) 在閉環模擬中評估policy，失敗案例回頭成為下一輪合成資料生成的目標，重新進入語料庫。

🧩 **一個transformer trunk，三種模式**

傳統做法常常是為每個階段各自準備一套GPU容量：一批節點生成合成資料、一批post-train、一批評估，各自有自己的建立與拆除生命週期。Cosmos 3的設計讓這變得不必要。它是一個開源的omnimodal world foundation model，把影片、影像、動作、聲音當成單一token串流處理，同一個transformer trunk可以用三種模式運行：作為forward-dynamics world model做合成影片生成、作為inverse-dynamics動作標註器，以及作為可部署的動作policy。

架構上有兩個關鍵設計：AR（autoregressive）子序列負責處理文字與模型要「讀懂」的視覺token，維持causal特性、看不到diffusion token；DM（diffusion-model）子序列負責生成的影片、聲音與動作token，DM的query會對AR與DM的key做full attention。兩者共用Reasoner與Generator塔，透過逐層attention銜接。中間訓練出的base checkpoint可以透過改變「哪些token從noise開始」，切換forward dynamics、inverse dynamics、policy三種模式；post-training再把checkpoint特化到單一模式與控制頻率。

模型家族分兩個tier：Cosmos3-Nano（16B參數，架構於8B的Qwen3-VL dense backbone之上）與Cosmos3-Super（64B參數，架構於32B的Qwen3-VL dense backbone之上），任務變體如Cosmos3-Nano-Policy-DROID即建構於這些tier之上。NVIDIA另外釋出了Cosmos3-Edge，一個4B的精簡版本，鎖定裝置端部署（在Jetson Thor與Orin上有benchmark）。Edge與Nano、Super共享相同的physical-world預訓練資料，但架構於一個從頭訓練、約2B參數的dense backbone之上，並非由Qwen3-VL初始化，屬於不同的權重系譜，也就是說要針對目標硬體直接post-train Edge，而不是把Nano checkpoint壓縮進去。

💡 **成本看的是GPU goodput，不是尖峰吞吐量**

因為整條迴圈要持續運轉，等於是一種容量承諾（capacity commitment）：不管pipeline有沒有在推進進度，你都要為預留的容量付費。這也是為什麼真正該關注的指標不是任何單一job的尖峰吞吐量，而是GPU goodput——每個預留GPU小時內，pipeline實際完成的有效進度。當生成、post-train、評估三個階段全部跑在同一個模型家族、同一套儲存層之上，就能time-share同一個已承諾的容量池，而不是把容量按階段切碎，這正是Cosmos 3單一模型涵蓋生成、post-training、評估三種角色所帶來的效益。

要支撐這種飛輪，底層叢集也要對應這個形狀：一個持久化的資源池、一個控制平面，而不是每個job各自一套環境。Amazon SageMaker HyperPod on Amazon EKS提供的正是這種形狀，文章指出Cosmos 3的架構選擇（如單一token串流、64B的MoT結構帶來的長序列多節點訓練需求、生成與推論的不對稱性）分別對應到SageMaker HyperPod的特性，讓叢集能滿足這些需求。

⚠️ **不是所有workload都需要HyperPod**

文章也提醒，是否選擇SageMaker HyperPod取決於工作單位的性質：一次性的微調workload不一定需要HyperPod等級的韌性與持久性，短時間運行的job較少遇到節點故障，這種情況下用像Amazon SageMaker AI training job這樣的ephemeral managed training job就已足夠。

🎯 **實務啟示**

若你的團隊正在建構機器人或AV相關的資料到部署pipeline，這篇文章提供的awsome-distributed-ai GitHub repository附有各階段的manifest與設定檔，可以作為把這套四階段飛輪落地成實際叢集的起點，而不用重新設計整套基礎設施。

🔗 **來源**
- 標題：Build a Physical AI model factory with NVIDIA Cosmos 3 on SageMaker HyperPod
- 作者／機構：Nathan Arnold, AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/build-a-physical-ai-model-factory-with-nvidia-cosmos-3-on-sagemaker-hyperpod/

#PhysicalAI #NVIDIACosmos #SageMakerHyperPod #RoboticsAI #WorldModel #AWS #AIInfrastructure #SyntheticData #AutonomousVehicles #GPUCluster
