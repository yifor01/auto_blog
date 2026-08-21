---
title: Broadening access to Skala creates a faster path to predictive DFT
source: Microsoft Research
url: https://www.microsoft.com/en-us/research/blog/broadening-access-to-skala-creates-a-faster-path-to-predictive-dft/
model: claude-code/sonnet
generated_at: '2026-08-21T06:28:32.363565'
score: 121
---

📌 【Microsoft Research】Skala-1.1 免費升級，DFT 準確度再進化

TL;DR：Skala-1.1 用 2.5 倍訓練資料換來更準的 DFT 計算，並開始進駐五套主流計算化學軟體。

如果你做過密度泛函理論（DFT）計算，大概對「functional zoo」不陌生：新的交換相關泛函一個接一個推出，卻沒有一個真正取代前一個，工程師只能憑經驗東拼西湊。Microsoft Research 想打破這個循環。

🤔 **不是新增泛函，而是取代舊泛函**

Skala 是 Microsoft Research 推出的深度學習交換相關泛函（exchange-correlation functional），設計哲學與傳統做法完全不同：每一代新版本的目標是直接取代前一代，而不是疊加在「泛函動物園」裡供人挑選。隨著新資料、新模型架構與訓練策略到位，模型持續變準，但運算成本維持不變。

🧩 **靠更大、更多元的訓練資料集持續進化**

Skala-1.1 是這套「持續改進」哲學的第一次實際示範，訓練資料量是第一個公開版 Skala 的 2.5 倍。這些資料來自 Microsoft Research Accurate Chemistry Collection（MSR-ACC），一個以高成本波函數方法（wavefunction methods）生成的高精度量子化學參考資料庫。這次擴充新增了電子親和力（electron affinities）與非共價分子團簇（noncovalent clusters）等類別，同時提高了資料的規模與多樣性。

📊 **GMTKN55 上的加權平均誤差來到 2.8 kcal/mol**

在涵蓋熱化學、反應能障、非共價交互作用等 55 個化學類別的 GMTKN55 基準測試中，Skala-1.1 的加權平均誤差為 2.8 kcal/mol，超越目前主流的全域（range-separated）混成泛函，同時保有半局域泛函（semi-local functional）等級的運算效率。除了能量之外，Skala-1.1 在電子密度、偶極矩與分子幾何結構的預測上也相當準確。在效能上，Skala 於 CPU 與 GPU 上都能達到與半局域 meta-GGA 相當的速度，而在原子數超過 20 到 30 個的分子上，額外開銷更會逐漸消失。

🧩 **從一個套件，擴散到整個生態系**

Skala 最早透過開源社群版釋出，建構在（GPU4）PySCF 之上並整合 ASE，讓研究者能以最小成本評估與使用。但沒有任何單一套件能滿足所有應用場景，因此 Microsoft Research 過去一年的重心之一，就是把 Skala 帶進更廣的電子結構軟體生態系。目前 Skala 已成功整合進開源套件 CP2K（與 Center for Advanced Systems Understanding／CASUS 的 Thomas D. Kühne 教授團隊合作），CP2K 擁有超過 25 年開發歷史，特別擅長大型系統與長時間尺度的分子動力學模擬。同時，Skala 正在整合進開源的 Psi4，以及 FHI-aims、ORCA、VASP 等業界廣泛使用的套件。團隊也與 CASUS 團隊共同開發了完整的整合測試套件，確保 Skala 在不同程式碼與運算設定下都能產出數值正確、可靠的結果，相關細節記錄在雙方合著的論文《Molecular Implementation of the Machine-Learned Skala Exchange-Correlation Functional in CP2K through GauXC》中。

💡 **用「活基準」追蹤效能演進**

由於效能並非固定不變的屬性,新版 Skala、GauXC 等函式庫的改進、以及硬體專屬最佳化都會持續影響運算效率,團隊因此建立了一套持續更新的活基準（living benchmark），追蹤不同軟體套件與硬體平臺上、連續多個 Skala 版本的運算效能，讓社群能透明地量測與加速朝更高準確度與效率邁進的過程。

🎯 **實務啟示**

對計算化學與材料科學工程師而言,這代表未來不需要在「準確」與「能跑得動」之間妥協。如果你的工作流程已經使用 CP2K,現在就能直接用上 Skala；若使用 Psi4、FHI-aims、ORCA 或 VASP，也可以留意近期的整合進度，評估導入下一代 DFT 準確度的時機。

🔗 **來源**
- 標題：Broadening access to Skala creates a faster path to predictive DFT
- 作者／機構：Microsoft Research — Sebastian Ehlert, Stefano Battaglia, Thijs Vogels, Jan Hermann 等
- 連結：https://www.microsoft.com/en-us/research/blog/broadening-access-to-skala-creates-a-faster-path-to-predictive-dft/

#DFT #ComputationalChemistry #MachineLearning #Skala #MicrosoftResearch #DeepLearning #QuantumChemistry #MaterialsScience #DrugDiscovery #AIforScience
