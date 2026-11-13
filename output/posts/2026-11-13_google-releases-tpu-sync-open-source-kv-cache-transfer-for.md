---
title: 'Google Releases TPU Sync: Open-Source KV Cache Transfer for TPUs'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/13/google-tpu-sync-kv-cache-transfer-library/
model: claude-code/sonnet
generated_at: '2026-11-13T22:44:52.288403'
score: 104
---

📌 Google 開源 TPU Sync：把 KV cache 搬運效能瓹辛，瓶頸不在算，而在搬

TL;DR：Google 開源 C++ 函式庫 TPU Sync，將 KV cache 跨記憶體層傳輸延遲降低逾九成。

推理大型 MoE 模型時，真正拖後腿的往往不是矩陣運算，而是把 KV cache 和模型權重從一個地方搬到另一個地方。Google Cloud 這次開源的 TPU Sync，就是衝著這個「搬運」瓶頸而來。

🤔 **把 TPU HBM、主機記憶體、儲存和網路當成一個記憶體層級**

TPU Sync 是一個開源 C++ 函式庫（Apache-2.0 授權），用非同步 DMA 在 TPU 之間搬動已經 tile 過的張量。它要解決兩個任務：推理時的 KV cache 狀態搬運，以及強化學習（RL）訓練中 trainer 到 sampler 的權重廣播。這個函式庫橫跨 TPU HBM、pinned host DRAM、共享儲存與多主機的資料中心網路（DCN），儲存層則透過實驗性的 POSIX 後端支援本地 SSD 與 Google Cloud Managed Lustre。

🧩 **P/D 分離式服務下的搬運路徑**

在 prefill/decode 分離（P/D disaggregated serving）架構裡，TPU Sync 的角色分工如下：

- Prefill 節點先透過非同步 DMA，把 KV 區塊卸載到 pinned host RAM。
- 傳輸控制器（transfer controller）再把這些區塊以 host-to-host 的方式串流給指定的 decode 節點。
- 抵達的區塊被搬進 decode 節點的 HBM，同時 decode 運算繼續進行,不必等待傳輸完成。

這套流程之上還有一個全域 KV store 負責前綴（prefix）查找，加上傳輸控制器與 KV cache manager 共同協調整個搬運過程。

📊 **90% 以上的延遲降幅是怎麼測出來的**

Google 回報，在 235B 到 480B 參數規模的 MoE 模型上，KV 傳輸延遲降低超過 90%。這項內部測試在 2026 年 7 月於 TPU v7x（2x2x1）上進行，軟體版本為 tpu-inference v0.24.0、JAX 0.10.2 與 libtpu 0.0.42.1。Google 團隊也主動表示，實際結果會因環境而有差異。

值得留意的是，TPU Sync 公布的頻寬數字量測的是 host PCIe DMA 路徑，而業界常被拿來比較的 Mooncake 則是量測 RoCE 網路傳輸,兩者路徑不同,不能直接等號比較。

🧩 **生態系整合：vLLM、SGLang、GKE 都已經接上**

TPU Sync 同時支援 PyTorch（透過 TorchTPU）與原生 JAX。在 vLLM-TorchTPU 中，它是實作 vLLM KVConnector 介面的 TPU KV connector；在 SGLang-TorchTPU 中，它是 P/D 傳輸後端與分層快取 I/O 後端。在 GKE 上，llm-d 1.0 用它來做前綴快取親和性（prefix-cache-affinity）路由，並支援實驗性的 spill to Managed Lustre。Inferact 和 RadixArk 共同參與了 vLLM 與 SGLang 的整合工程，Google 表示 Meta 與 Wayfair 正在評估這套架構。

⚠️ **工程紮實，但不是範式轉移**

TPU Sync 解決的是一個具體、已知的系統瓶頸,而非提出新的模型架構或演算法。它的價值在於把原本分散、各家自行土炮的 KV 搬運邏輯,收斂成一套開源、跨框架可用的標準件。

🎯 **實務啟示**

如果你在用 TPU 跑大型 MoE 模型的 P/D 分離推理，或正在自己手刻 KV cache 跨主機搬運邏輯，TPU Sync 值得拿來替換掉自製方案；若你用的是 GPU 推理堆疊，也可以把這套三層記憶體（HBM／主機 DRAM／共享儲存）的設計思路當作系統設計參考。

🔗 **來源**
- 標題：Google Releases TPU Sync: Open-Source KV Cache Transfer for TPUs
- 作者／機構：Michal Sutter（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/11/13/google-tpu-sync-kv-cache-transfer-library/

#TPU #KVCache #GoogleCloud #LLMInference #OpenSource #vLLM #SGLang #MoE #DistributedSystems #MachineLearning
