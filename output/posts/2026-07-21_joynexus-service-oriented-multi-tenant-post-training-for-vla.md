---
title: 'JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.16074
score: 87
model: tencent/hy3:free
generated_at: '2026-07-21T08:32:45.148441'
---

📌 【研究論文】JoyNexus：透過多租戶架構解決 VLA 模型訓練的資源效率問題

TL;DR：JoyNexus 透過解耦服務與 Group Batching 技術，提升多租戶 VLA 訓練的 GPU 利用率。

🤔 **現有服務模式的兩難困境**

在視覺-語言-動作（Vision-Language-Action, VLA）模型領域，由於模擬器、機器人實體與任務目標極具多樣性，模型後訓練（Post-training）變得至關重要。然而，目前的運算服務（無論是直接租用加速器或提交批次工作負載）通常會為單一租戶分配專屬的 GPU 與 CPU 資源。這種模式雖然提供了極高的靈活性，卻將基礎設施適配的負擔丟給了使用者，且固定的卡時計費模式對於短暫或爆發性的工作負載來說，對租戶而言成本過高，對服務提供者而言效率卻不足。

🧩 **JoyNexus：解耦服務與 API 驅動架構**

為了應對這些挑戰，研究提出了 JoyNexus，這是一個針對多租戶 VLA 進行監督式微調（SFT）、強化學習（RL）與評估的統一服務架構。

其核心設計理念在於將服務解耦為三個部分：
1. 訓練模型服務（Training Model Service）
2. 推論模型服務（Inference Model Service）
3. 環境服務（Environment Service）

這些服務皆透過 API 進行存取，並由擁有租戶特定插槽（tenant-specific slots）的共享駐留基礎模型（resident shared base models）提供支援。租戶可以透過高層級的語義 API 直接進行訓練、Rollout（策略執行）與評估，或是利用低層級 API 與指定的端點來組合成自定義演算法。

在多租戶並行作業時，各租戶的動作模組（action modules）、最佳化器（optimizers）、Rollout 紀錄與策略版本都會保持隔離，並由全域的訓練佇列（Training Queue）與推論佇列（Inference Queue）進行排程。

💡 **透過 Group Batching 提升異質資料的訓練效率**

針對多租戶訓練效率，JoyNexus 引入了「群組批次處理」（Group Batching）技術。當不同租戶的異質 VLA 資料具有相容的模型字首（model-facing prefix）時，系統可以將這些樣本分組，讓單次共享骨幹網路（backbone）的前向傳播（forward pass）可以同時處理多個樣本，進而最佳化效能。

📊 **模擬實驗證實能降低 GPU 總耗時**

研究透過工作負載模擬以及在真實具身智慧（embodied）場景下的群組批次管線進行評估。結果顯示，相較於孤立的單租戶執行模式，JoyNexus 透過在共享資源上進行跨租戶排程，成功降低了總體 GPU 耗時並提升了服務利用率。

🎯 **實務啟示**

對於需要頻繁進行 VLA 模型微調與評估的開發者而言，這種解耦且支援多租戶的架構，提供了一種比傳統「獨佔資源」更具成本效益的雲端運算新思路，特別是在處理大量短暫任務時。

🔗 **來源**
- 標題：JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models
- 連結：https://huggingface.co/papers/2607.16074

#VLA #MachineLearning #MultiTenant #Robotics #PostTraining #GPU #ReinforcementLearning #ComputerVision #EmbodiedAI #CloudComputing
