---
title: 1小時真機RL微調成功率破95%！HIL-ResRL：即插即用的VLA“外掛”神器
source: 量子位
url: https://www.qbitai.com/2026/06/438166.html
score: 92
model: google/gemma-4-31b-it:free
generated_at: '2026-06-24T20:05:37.020150'
---

📌 【華為雲研究】1 小時真機微調成功率破 95%：HIL-ResRL 讓 VLA 模型擺脫分佈偏移

TL;DR：透過「基礎模型打底 + 殘差策略糾偏」的設計，讓 VLA 模型在 1 小時內快速適應新場景且成功率突破 95%。

在具身智慧（Embodied AI）的應用中，視覺-語言-動作（VLA）模型雖然泛化能力強，但一旦部署到真實工業產線，常因目標物位置微偏移而導致誤差累積，使機器人出現「胡亂抖動」或軌跡發散的現象。

🤔 **模仿學習的硬傷：分佈偏移與誤差累積**

目前的 VLA 模型高度依賴模仿學習（Imitation Learning），尤其是行為克隆（BC）。這種方式的致命缺陷在於：一旦真實環境與演示資料的分佈不一致（Out-of-Distribution, OOD），模型會因缺乏自我糾錯能力而失效。雖然使用真實世界強化學習（Real-world RL）可以解決，但計算成本高昂且與特定模型架構深度綁定，缺乏部署靈活性。

🧩 **HIL-ResRL：將基礎模型視為黑盒的「外掛」設計**

華為雲 CloudRobo 團隊提出的 HIL-ResRL 採取了一種輕量化的殘差策略（Residual Policy），將其設計為一個模型無關（Model-agnostic）的介面卡，其運作邏輯如下：

1. **基礎動作打底（Base Policy）**：凍結預訓練的 VLA 模型（如 Diffusion Policy 或 $\pi 0.5$），將其視為黑盒，負責輸出基礎動作 $a_{base}$。
2. **殘差動作糾偏（Residual Action）**：訓練一個極輕量的殘差網路來輸出修正動作 $a_{res}$。
3. **動作合成**：機器人最終執行的動作為兩者之和：$a_t = a_{base} + a_{res}$。

這種設計讓 HIL-ResRL 變成一個「即插即用」的元件，無論基礎模型是基於 Diffusion 還是 Flow Matching，無需獲取內部權重即可無縫整合。

🛡️ **人機協同（HIL）確保安全探索與極速收斂**

為了避免隨機探索損壞昂貴硬體，HIL-ResRL 將「人類在環」（Human-in-the-loop, HIL）機制融入訓練迴圈：

- **精準幹預**：操作員使用 3D SpaceMouse 隨時待命。當模型進入 OOD 狀態開始抖動時，人類給出微小幹預訊號 $a_{int}$，將機器人「拽」回正確的分佈中。
- **降低工作量**：人類不需要重新演示完整軌跡，僅需在危急時刻進行微調。
- **快速學習**：殘差網路僅需學習「特定時刻如何糾偏」而非重新學習所有動作，因此透過離策略強化學習（SAC）能實現極速收斂。

📊 **訓練成效：1 小時內成功率突破 95%**

根據論文指出，這種方法能讓機器人在僅 1 小時的真機線上訓練後，任務成功率突破 95%。

🎯 **實務啟示**

對於追求快速部署的柔性製造業，這種「基礎模型 + 殘差修正」的架構提供了極高的工程價值：
- **降低部署門檻**：無需對龐大的 VLA 模型進行全參數微調，大幅降低計算成本。
- **提升部署安全性**：透過 HIL 機製取代隨機探索，解決了真機 RL 訓練中對硬體損耗的擔憂。
- **提升環境適應力**：將人類的經驗轉化為局部動力學修正，使模型能快速適應微小的環境變動。

🔗 **來源**
- 標題：HIL-ResRL: Human-in-the-Loop Residual Reinforcement Learning for Model-Agnostic Fine-Tuning of VLAs
- 連結：https://arxiv.org/abs/2606.22860

#VLA #EmbodiedAI #ReinforcementLearning #HIL #ResidualLearning #Robotics #HuaweiCloud #SAC #ImitationLearning #HumanInTheLoop
