---
title: 'Introducing preemptible compute: the same compute, half the price'
source: Together AI
url: https://www.together.ai/blog/introducing-preemptible-compute-the-same-compute-half-the-price
model: claude-code/sonnet
generated_at: '2026-11-25T01:52:58.175100'
score: 69
---

📌 Together AI 推出 Preemptible Compute：同款 GPU 砍半價

TL;DR：同款 GPU 算力打五折，用未使用容量跑可中斷工作，但 5 分鐘內要存檔退場。

如果你的訓練或推理工作能忍受「隨時被請下線」，Together AI 現在願意用一半的價格把同一顆 GPU 租給你——條件是你要在五分鐘內學會優雅退場。

🤔 哪些工作適合丟進折扣區

Preemptible compute 已在 Together GPU Clusters 全面 GA，支援 Kubernetes 與 Slurm，所有地區皆可用。Together 把它定位成跑「可中斷容忍」工作的低成本選項：短實驗、推理尖峰、batch job。Standard node 一律同步配置、絕不會被搶佔；preemptible node 用的是同一款 NVIDIA 加速運算，但吃的是「未使用容量」，容量被別處需要時就會被收回。

🧩 怎麼運作：固定五折費率 + 五分鐘硬退場

計費方式是 sub-hourly，每 1 到 2 分鐘計量一次，跑 12 分鐘就只算約 12 分鐘的費用；費率固定在 on-demand 的 50%，不像 spot market 那樣隨行情浮動。被搶佔時的時序很明確：T+0 node 被 cordon、觸發 TogetherPreemptionNotified 的 Kubernetes 事件、pod 收到 SIGTERM；T+0 到 T+5:00 之間（由 terminationGracePeriodSeconds 控制）有最多五分鐘可以 checkpoint 並退出；T+5:00 node 被移除。Cluster 會記住你設定的 preemptible 目標值，容量恢復時自動補滿，不需要自己重新申請。Preemptible node 不是獨立的 cluster 類型，而是用 together.ai/compute-class=preemptible 標籤加入既有 cluster，讓 coordinator、login pod、serving replica 這些關鍵元件留在 standard node 上。

📊 一個具體的時間參考點

Together 舉的候選工作包括 ablation、config sweep、快速 fine-tune、eval、distillation、batch inference，前提是能從 checkpoint 恢復或直接 retry。Ray Train、PyTorch Lightning 這類框架可以自動從最新 checkpoint 接著跑，不需要人工介入。作為參考，GLM5.3 Flash（321B 參數）的全權重 checkpoint 大約 3.5TB，就算效能降級，寫入 parallel filesystem 也只要 22 秒到 4 分鐘，落在五分鐘的 drain window 之內還有餘裕。另一個情境是臨時尖峰：batch 或內部推理需求突然暴增時，用便宜的 preemptible node 吸收尖峰和非關鍵工作，而不必把 standard 容量撐到峰值大小；被中斷的 request 會 requeue，使用者端的 replica 則一律留在 standard node。不適合的情況很明確：沒有 checkpoint 機制的多日訓練，以及沒有 fallback 的嚴格 SLO serving。Together 表示自家內部的研究、dev/test、非關鍵 production 工作也大量跑在 preemptible cluster 上，讓不同產品團隊共用剩餘容量。

💡 上線前的三個提醒

把 preemptible node 當成隨時會消失的資源：沒有最短存活時間保證，要頻繁 checkpoint；關鍵元件用 compute-class 標籤強制留在 standard node；terminationGracePeriodSeconds 可以設到 300 秒，收到 SIGTERM 就立刻 checkpoint 再退出。一個 cluster 可以完全跑在 preemptible 上，但如果需要隨時能存取共享儲存，至少要留一個 standard node；node 一旦建立就無法原地轉換類型。

🎯 實際操作方式

新建 cluster 時可以直接加 --num-preemptible-gpus 參數（tg beta clusters create），既有 cluster 也能用 tg beta clusters update 調整目標值，cluster 不用重啟。API 會同時回報 desired_preemptible_gpus（你設的目標）與 allocated_preemptible_gpus（實際拿到的容量），容量緊張時兩者可能不一致。排程時用 nodeSelector: together.ai/compute-class: preemptible 明確指定要跑在折扣節點上；搶佔通知會透過 SIGTERM、Kubernetes 事件（reason=TogetherPreemptionNotified）、console 的 Event Timeline，以及 API 的 node_lifecycle_events 四個管道同步送達。

⚠️ 本質上這是「用未使用容量換折扣」，recovery 行為決定一切——沒有 checkpoint 或 retry 機制的工作完全不該丟上去。

🔗 來源
- 標題：Introducing preemptible compute: the same compute, half the price
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/introducing-preemptible-compute-the-same-compute-half-the-price

#TogetherAI #GPU #CloudComputing #MachineLearning #MLOps #Kubernetes #Slurm #SpotInstances #AIInfrastructure #CostOptimization
