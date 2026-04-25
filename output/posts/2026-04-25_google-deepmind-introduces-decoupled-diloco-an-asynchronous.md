---
title: "Google DeepMind Introduces Decoupled DiLoCo: An Asynchronous Training Architecture Achieving 88% Goodput Under High Hardware Failure Rates"
source: MarkTechPost
url: https://www.marktechpost.com/2026/04/23/google-deepmind-introduces-decoupled-diloco-an-asynchronous-training-architecture-achieving-88-goodput-under-high-hardware-failure-rates/
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-04-25T19:07:19.843502
---

📌 【Google DeepMind】異步訓練抗故障，Goodput 達 88%

當你調度數千顆晶片進行 LLM 訓練時，最怕的不是算力不夠，而是「一顆故障，全軍覆沒」。在跨地域的分散式訓練中，傳統的同步機制往往讓效率在頻寬與等待中消磨殆盡。

🤔 **同步訓練的擴展噩夢：一顆慢，全體等**

目前的標準 Data-Parallel 訓練依賴 AllReduce 機制，每次梯度更新後，所有加速器（GPU/TPU）必須同步。這代表最快的設備必須等待最慢的那一個。當規模擴大到跨數個資料中心時，這種緊耦合（Tight Synchronization）讓訓練變得極度脆弱，且 198 Gbps 的跨資料中心頻寬需求也遠超一般 WAN 的負載能力。

🧪 **解耦式島嶼架構：借鏡 Pathways 的異步思維**

Google DeepMind 提出的 **Decoupled DiLoCo (Distributed Low-Communication)**，核心概念是將計算解耦為異步、故障隔離的「島嶼（Islands）」。這項架構建立在 Google 先前的 Pathways 系統之上，利用異步數據流讓不同計算資源能以自己的步調工作，不再因為單點故障或延遲而阻塞整個訓練流程。

 **高故障率下仍維持 88% Goodput**

Goodput（有效吞吐量）是衡量實際有用工作的關鍵指標。Decoupled DiLoCo 的設計目標是讓 LLM 預訓練能在地理距離遙遠的資料中心進行，且不依賴傳統的高頻寬同步。實驗顯示，即便在硬體故障率極高的環境下，該架構仍能維持 88% 的 Goodput，這對於降低大規模訓練的維運風險至關重要。

💡 **從「緊耦合」轉向「低通訊」的範式轉移**

這項研究的關鍵在於重新定義了分散式訓練的邊界。透過降低對跨資料中心頻寬的依賴（從 198 Gbps 的需求中解放），Decoupled DiLoCo 讓企業能更靈活地利用全球各地的閒置算力，而不必將所有資源集中在同一個擁有超高頻寬的機房內。

⚠️ **技術細節尚待完整揭露**

由於目前資訊基於 MarkTechPost 的報導摘要，論文中關於具體的梯度壓縮技術、島嶼間的具體通訊協議，以及與其他低通訊訓練方法（如 DiLoCo 原始版本）的詳細對比數據，仍有待進一步閱讀完整論文。

🎯 **超大規模訓練的容錯新路徑**

對於致力於訓練百億甚至千億參數級別模型的團隊來說，這是一個重要的技術訊號。異步與故障隔離將成為下一代分散式架構的標配，這能顯著降低因硬體老化或網路波動帶來的巨額成本損失。

🔗 **相關連結**
📝 Google DeepMind Introduces Decoupled DiLoCo: An Asynchronous Training Architecture Achieving 88% Goodput Under High Hardware Failure Rates
👤 Asif Razzaq @ MarkTechPost
🔗 詳細報導：https://www.marktechpost.com/2026/04/23/google-deepmind-introduces-decoupled-diloco-an-asynchronous-training-architecture-achieving-88-goodput-under-high-hardware-failure-rates/

你們在進行分散式訓練時，遇過最崩潰的硬體故障經驗是什麼？歡迎在留言區交流避坑心得 👇

#GoogleDeepMind #AI #LLM #DistributedTraining #MachineLearning #DiLoCo #系統架構 #AI基礎設施
