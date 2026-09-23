---
title: How to Use NVIDIA Warp and MjWarp to Accelerate Robotics Simulation and Learning
  Workflows
source: HuggingFace Blog
url: https://huggingface.co/blog/nvidia/how-to-use-nvidia-warp-and-mjwarp
model: claude-code/sonnet
generated_at: '2026-09-23T20:38:46.607507'
score: 88
---

📌 【NVIDIA】把 MuJoCo 機器人模擬推向 GPU 規模：一次跑 2,048 個平行世界

TL;DR：NVIDIA Warp 與 MJWarp 讓相容的 MuJoCo 模型從單一 CPU 世界擴展到上千個 GPU 平行環境。

傳統 MuJoCo 在 CPU 上跑一個機器人世界已經夠快，甚至能把取樣工作平行分散到多個 CPU 核心。但當學習任務的規模持續擴大，問題不再是「一個世界能跑多快」，而是「同時能跑多少個世界」。這正是 NVIDIA Warp 與建立在其上的 MuJoCo Warp（MJWarp）要解決的問題。

🤔 **從「一個世界跑得快」到「上千個世界一起跑」**

強化學習與大規模取樣最在意的不是單一環境的延遲（latency），而是每秒完成的世界步數總量，也就是聚合吞吐量（aggregate throughput）。MJWarp 的價值不必然是讓單一世界的一步算得更快，而是能把數百甚至上千個世界一起推進，讓 GPU 有足夠的平行工作量把吞吐量真正拉起來。這篇文章是 NVIDIA「State of Simulation for Physical AI」系列的第二篇，重點是準備並擴展模擬環境本身，並不涉及訓練策略；後續的 Newton 與 Isaac Lab 文章才會處理更上層的整合。

🧩 **三層架構：Warp、MJWarp、你的場景**

整個技術棧可以拆成三層：NVIDIA Warp 是 Python kernel 語言，提供 SIMT（single instruction, multiple threads）平行執行、自動微分（autodiff）以及與 PyTorch／JAX 的互通性；MJWarp 則是在 Warp 上實作的 MuJoCo 物理引擎，使用同一份 MJCF 模型檔案，但把批次化的 GPU 吞吐量做出來；再上層就是你的場景，例如文中示範的 SO-101 follower arm，沿用熟悉的 Menagerie／Robot Studio 資產與任務幾何。

Warp 的核心賣點有三個：效能上透過 JIT 編譯、kernel 融合與 CUDA Graphs 達到接近原生 CUDA 的速度；易用性上維持純 Python 撰寫，並內建向量、矩陣、四元數、BVH、hash grid、稀疏矩陣等結構；能力上則支援可微分 kernel 與類似 DLPack 的互通格式，讓模擬能直接嵌入 ML 訓練迴圈。一個最小範例是這樣的 kernel：透過 `wp.tid()` 取得目前執行緒對應的點索引，套用重力更新速度，再更新位置——同一段程式碼可以從兩個點無痛擴展到數百萬個點，控制流程完全不必寫進 GPU 相關術語。

從 MuJoCo 遷移到 MJWarp 的 API 對應也很直接：`mujoco.MjModel` 對應 `mjw.put_model(mjm)`，`mujoco.MjData` 對應 `mjw.put_data(mjm, mjd, ...)`，`mujoco.mj_step(mjm, mjd)` 對應 `mjw.step(m, d)`，而原本 `mjd.ctrl` 這類 host 端陣列，會變成形狀為 `(nworld, nu)` 的批次化裝置陣列。文章也指出一個實務細節：想要保留初始化後的精確 MuJoCo 狀態，要用 `mjw.put_data()`；只需要預設或全新狀態時，用 `mjw.make_data()` 就夠了。

💡 **可微分與確定性：兩個目前用不到、但值得知道的能力**

Warp kernel 本身是可微分的：`wp.Tape` 會記錄 context 內的前向 kernel 呼叫，呼叫 `backward()` 時再反向重播其伴隨運算，這也是為什麼團隊會用 Warp 打造可微分幾何、CFD 甚至客製物理引擎，應用在 CAE 的模擬與設計最佳化上。另外，Warp 1.15 引入了確定性執行模式：GPU atomics 預設依排程而定，重複執行同一個 kernel 可能有微小差異，開啟確定性模式可以用一些效能換取可重現的執行順序，適合驗證與回歸測試。但要注意，這是 Warp 本身的能力，並不代表整條 MJWarp rollout 都自動具備可微分性或確定性保證。

⚠️ **這篇文章沒有涵蓋的範圍**

文中明確指出，solver 調校、Jacobian 表示方式，以及多 GPU 或確定性的進階主題，並不是這次遷移的必要條件，會留到之後另外說明。這篇也只走到「驗證單一世界、遷移到 MJWarp、組成批次、驗證、正確測量」為止，並未實際訓練策略。

🎯 **該用哪一個工具？**

文章給了一個很實用的決策捷徑：只需要單機器人 MPC 或遙操作，用 MuJoCo CPU 就好；要在原生 MuJoCo 物理上榨出最大吞吐量，選 MJWarp（或 mjlab）；需要 JAX 訓練流程，用 MuJoCo Playground／MJX（`impl='warp'`）；要多 solver API 加上 Isaac Lab 整合，就等系列下一篇的 Newton。想試試 Warp，可以直接 `pip install warp-lang`（GPU 確定性需求要 1.15 以上），再跑 `python -m warp.examples.browse` 或官方 tutorial notebooks。

🔗 **來源**
- 標題：How to Use NVIDIA Warp and MjWarp to Accelerate Robotics Simulation and Learning Workflows
- 作者／機構：Johnny Nuñez Cano、Asier Arranz、Rishabh Chadha、Ben Oliveri（NVIDIA）／HuggingFace Blog
- 連結：https://huggingface.co/blog/nvidia/how-to-use-nvidia-warp-and-mjwarp

#NVIDIA #Warp #MuJoCo #MJWarp #RoboticsSimulation #ReinforcementLearning #GPUComputing #PhysicalAI #SO101 #CUDA
