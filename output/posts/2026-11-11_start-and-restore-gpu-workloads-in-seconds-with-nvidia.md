---
title: Start and Restore GPU Workloads in Seconds with NVIDIA Snapshot
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/start-and-restore-gpu-workloads-in-seconds-with-nvidia-snapshot/
model: claude-code/sonnet
generated_at: '2026-11-11T23:46:32.595437'
score: 101
---

📌 NVIDIA Snapshot：讓 GPU 推理服務幾秒內復活

TL;DR：開源 checkpoint/restore 技術，讓 GPU 推理 replica 從分鐘級冷啟動降到秒級復活。

🎣 推理流量突然暴增，或是一個 replica 掛掉，手上明明有空的 GPU，卻幫不上忙，因為重新初始化一個 LLM 服務要花上好幾分鐘——這段落差正是 NVIDIA Snapshot 想解決的問題。

**🤔 冷啟動為什麼這麼慢**

一次完整的冷啟動流程要經過：機器 provisioning、載入容器映像檔、啟動推理引擎、把模型權重載入 GPU 記憶體、用 torch.compile 編譯、再進行 CUDA graph capture。每一步都要花時間，也因此延遲了擴容與故障復原的速度。

**🧩 Kubernetes 上的 checkpoint/restore 系統**

Snapshot 捕捉一個已完全初始化的 workload（包含 CPU 與 GPU 記憶體狀態），再把這個狀態還原到相容的硬體上，讓推理容量在幾秒內上線，而不是幾分鐘。它最初是為 NVIDIA Dynamo inference worker 開發的，現在開放給其他推理引擎、排程器、controller 與平臺整合。

核心是兩個操作：Checkpoint（workload 初始化完成後，把 CPU 與 GPU 記憶體狀態捕捉成一個可攜的 artifact）與 Restore（在 GPU 型號與 driver 相同的任意節點上，從 artifact 啟動新 Pod，直接從 checkpoint 當下繼續，跳過 weight loading、compile、graph capture）。兩者都透過 Kubernetes 自訂資源操作：對已在跑的 Pod 建立 `PodSnapshot` 做 checkpoint；要用範本啟動並在 ready 後立刻 checkpoint，就建立 `SnapshotJob`；restore 時只要在新 Pod 加上 `nvidia.com/restore-from` annotation，指名要還原的 `PodSnapshot`。workload 端只需要一個小型 handshake，在 checkpoint 前暫停、restore 後恢復。官方 repo 已提供 vLLM、SGLang、TensorRT-LLM 的範例設定，對於跨多 GPU 的 workload（例如用 tensor parallelism、data/expert parallelism、decode context parallelism 的 MoE 大模型），Snapshot 可以把所有 rank 的狀態一起捕捉成單一 checkpoint artifact。

**📊 restore 時間全數在 43 秒內**

測試環境：GPU 為 NVIDIA B200，driver 615.71.09，儲存後端為 VAST（NFS），測試引擎為 vLLM 0.31.0、SGLang 0.5.21、TensorRT LLM 1.3.0。cold start 量測分四階段（startup、model load、initialization、compile/autotune/graph capture）；Snapshot restore 則分四階段（agent setup、CRIU restore、CUDA restore、wake/remap）。

重點結果：
- 跨所有測試設定，Snapshot 在 3.6 秒到 42.7 秒內讓 replica 重新上線，比 cold start 快 8 倍到 36 倍。
- 最大的 MoE 模型（checkpoint 約 600GB 到 1TB、橫跨 8 張 GPU）在 43 秒內完成 restore，相較 cold start 要 6 到 19 分鐘。
- checkpoint 建立一次要 15 秒到 5.5 分鐘，但即使加上這個一次性成本，checkpoint+restore 的總時間仍比單次 cold start 短。
- 在 8 GPU 的 MoE 設定中，搬運 GPU 狀態最花時間，佔 18 到 29 秒；用 CRIU 還原 CPU process 狀態只要 4.2 到 10.8 秒。

部分完整數據（原文表格節錄）：

| 模型 | 推理引擎 | Parallelism | Checkpoint 大小(GB) | Checkpoint 時間(s) | Cold start(s) | Snapshot restore(s) | 加速倍數 |
|---|---|---|---|---|---|---|---|
| Qwen3-0.6B | vLLM | TP1 | 8.13 | 15.30 | 104.43 | 4.66 | 22.40x |
| Qwen3-0.6B | SGLang | TP1 | 9.42 | 20.71 | 87.08 | 3.59 | 24.26x |
| Qwen3-0.6B | TRT-LLM | TP1 | 8.04 | 20.07 | 121.26 | 8.15 | 14.88x |
| Qwen3-14B | vLLM | TP1 | 37.71 | 19.98 | 122.76 | 5.72 | 21.45x |

設計夥伴的實測也印證效果：Crusoe 在 NVIDIA HGX B300 上，把 GLM-5.3 的 Pod 就緒時間從約 8 分鐘縮短到 31 秒；token factory 平臺 Saturn Cloud 針對 scale-from-zero 推理場景，在 HGX B300 上把 vLLM 啟動時間從 2 到 8.5 分鐘壓到 6 到 34 秒。

**💡 把「每次都要重算一次」變成「算一次、之後搬狀態」**

cold start 不只是 load weights，還包含 compile、autotune、capture CUDA graphs 這些重複性工作。Snapshot 的價值在 replica 數量越多、擴縮容越頻繁的場景越明顯，因為 checkpoint 的一次性成本可以被後續多次 restore 分攤掉。

**⚠️ 限制**

restore 只能在 GPU 型號與 driver 版本相容的節點上進行，workload 也必須符合 Snapshot 列出的 checkpoint/restore 與 runtime 相容性要求，並非任意推理服務都能直接套用；量測結果也不包含容器映像檔拉取與容器 runtime 設置的時間，實際上線的總延遲會比文中數字再多一些。

**🎯 實務啟示**

如果推理平臺常態面對流量尖峰或 replica 故障復原，Snapshot 提供了一條現成路徑：針對穩定版本的模型設定先做一次 checkpoint，之後所有新 replica 都能用秒級 restore 頂上。對於用 vLLM、SGLang、TensorRT-LLM 且已經在 Kubernetes 上跑推理的團隊，官方範例設定是最直接的起點。

🔗 來源
- 標題：Start and Restore GPU Workloads in Seconds with NVIDIA Snapshot
- 作者／機構：Ron Kahn, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/start-and-restore-gpu-workloads-in-seconds-with-nvidia-snapshot/

#NVIDIA #GPU #Kubernetes #LLMInference #vLLM #SGLang #TensorRTLLM #MLOps #ColdStart #AIInfrastructure
