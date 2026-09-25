---
title: Accelerate multimodal RL training with SkyRL on Amazon SageMaker HyperPod
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/accelerate-multimodal-rl-training-with-skyrl-on-amazon-sagemaker-hyperpod/
model: claude-code/sonnet
generated_at: '2026-09-25T20:51:30.986773'
score: 88
---

📌 用GRPO訓練視覺agent走迷宮，解題率衝上95%

TL;DR：AWS示範如何用SkyRL在SageMaker HyperPod上跑多模態強化學習，讓視覺語言模型的迷宮解題率大幅提升。

強化學習（RL）post-training正在成為打造具行動能力的語言模型agent的標準流程，但要在多節點、上百GPU小時的rollout規模下穩定跑完一次訓練，考驗的其實是底層基礎設施，而不只是演算法本身。

🤔 RL post-training需要什麼樣的基礎設施

模型要透過生成軌跡（trajectory）、取得獎勵、更新策略來學會跨步驟推理與行動。要在多節點、單次訓練動輒上百GPU小時rollout的規模下執行，需要能撐住長時間任務、在硬體故障時不中斷進度、並提供訓練動態即時可視性的持久化叢集基礎設施。Amazon SageMaker HyperPod正是為此設計，建構在Amazon EKS之上，透過叢集韌性（cluster resiliency）功能持續監控節點健康狀況並自動替換故障節點，搭配checkpoint機制讓訓練工作能從上次儲存的步驟接續，而不必從頭開始，這對長時間的多節點RL任務特別重要，因為單一硬體故障原本可能讓數小時的rollout進度付諸東流。HyperPod上的Ray能力讓使用者能從SageMaker Studio建立Ray叢集、以安全連線遠端提交工作，並透過HyperPod Observability EKS外掛程式提供的Amazon Managed Grafana儀表板監控訓練過程。

🧩 用GRPO訓練視覺語言模型走迷宮

文章示範用開源RL框架SkyRL，在SageMaker HyperPod上以Group Relative Policy Optimization（GRPO）訓練Qwen3-VL-8B視覺語言模型解迷宮任務。標準單回合RL只針對單一模型輸出給予獎勵，而多回合（multi-turn）RL讓agent在一整個步驟序列中學習：觀察狀態、採取行動、取得回饋、進入下一個狀態，策略是根據整個episode累積的獎勵學習，而非任何單一步驟。以2D迷宮為例，一個episode就是走一次迷宮，每個turn是一步移動：模型看著目前的迷宮畫面選擇方向或決定停止，環境再回傳更新後的畫面。獎勵是稀疏的，只有在限定步數內真正走到終點才會得到1.0分，否則什麼都沒有；由於某一步是否正確取決於前後步驟，沒有逐步的標準答案可供訓練。這正是GRPO發揮作用的地方：對每個起始位置，agent在目前策略下把迷宮跑好幾次，GRPO再把這些結果拿來互相比較，強化表現優於群體平均的軌跡，壓低落後的軌跡。這種組內比較就是全部的訓練訊號，讓GRPO不需要額外的critic或value model。

🧩 叢集架構與訓練流程

文章中的方案在HyperPod的Ray叢集上運行，配置一個CPU head節點與三個GPU worker節點。SkyRL把推論與訓練共置在同一批GPU上：vLLM引擎負責產生rollout（完整的迷宮episode），同時以Fully Sharded Data Parallel（FSDP）分片的policy模型負責梯度更新；每次optimizer step後，更新後的LoRA adapter權重會透過Amazon FSx for Lustre共用儲存，從訓練節點同步到推論引擎。

實作步驟包含：用預先安裝好SkyRL與VisGym（並釘選特定commit SHA以確保可重現）的Dockerfile建置映像檔並推送到Amazon ECR；在SageMaker Studio的HyperPod Tasks頁籤建立名為skyrl-visgym的Ray叢集，head節點使用ml.r5d.16xlarge（因為head節點在每次儲存checkpoint時，需要把GPU worker的LoRA adapter分片彙整起來，短暫將完整的adapter權重載入CPU記憶體，因此需要512GB的大記憶體），三個worker節點使用ml.g7e.12xlarge；透過原始YAML manifest編輯器把Amazon FSx檔案系統掛載到每個節點的/shared路徑，供checkpoint、LoRA權重與評估輸出讀寫；開啟Remote endpoints功能，讓工作提交與儀表板存取可透過IAM授權的URL遠端進行，不需要本機kubectl port-forward。

訓練工作腳本會在首次執行時下載VisGym SFT checkpoint並產生資料集（皆存放於FSx以便跨次訓練保留），再啟動GRPO訓練。這個SFT checkpoint讓GRPO有一個穩健的起點：預先在VisGym示範資料上訓練過的Qwen3-VL-8B，已經懂得解析迷宮圖片並輸出結構化的移動動作，GRPO只需要進一步微調哪些動作序列真正能走到終點。設定trainer.placement.colocate_all=true後，vLLM rollout引擎與FSDP policy worker共用同一批GPU：rollout階段GPU平行執行推論，policy更新階段則集體執行FSDP訓練；lora_sync_path指向FSx，讓每次optimizer step後更新的adapter權重能立即被節點上的推論引擎看到。

📊 從43.75%到超過95%

從VisGym SFT checkpoint出發，在SageMaker HyperPod上執行GRPO post-training後，模型在固定的64個迷宮評測集上的解題率，從43.75%提升到超過95%。

🎯 實務啟示

這篇文章示範的重點其實不是GRPO演算法本身，而是「如何把multi-turn RL訓練的rollout與訓練共置、checkpoint與故障復原、以及可觀測性整合進同一套叢集基礎設施」。對想把RL post-training導入自家agent訓練流程的工程團隊來說，vLLM rollout與FSDP policy訓練共置在同一批GPU、並用共用檔案系統同步LoRA權重的作法，是一個值得參考、可直接落地的工程模式。

🔗 來源
- 標題：Accelerate multimodal RL training with SkyRL on Amazon SageMaker HyperPod
- 作者／機構：Nilesh PS，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/accelerate-multimodal-rl-training-with-skyrl-on-amazon-sagemaker-hyperpod/

#ReinforcementLearning #GRPO #SkyRL #AWS #SageMaker #MultimodalAI #VisionLanguageModel #MLOps #DistributedTraining #AIInfrastructure
