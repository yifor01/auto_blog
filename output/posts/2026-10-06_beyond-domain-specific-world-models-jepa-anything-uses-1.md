---
title: 'Beyond Domain-Specific World Models: JEPA-Anything Uses 1 Recipe for 7 Fields'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/05/beyond-domain-specific-world-models-jepa-anything-uses-1-recipe-for-7-fields/
model: claude-code/sonnet
generated_at: '2026-10-06T21:53:51.611773'
score: 100
---

📌 一套配方跑七個領域，JEPA-Anything 想終結「每個領域各建一個世界模型」

TL;DR：PhAI Labs 等六機構用正交分解法讓同一套 JEPA 配方同時適用視覺、生物、臨床、控制、分子、物理場與氣象。

世界模型通常是「一個領域一個客製架構」：視覺有自己的 JEPA，分子動力學有自己的模擬器，氣象預測又是另一套管線。來自 PhAI Labs、CUHK、Fudan、Stanford、Oxford 與 Princeton 的研究團隊提出 JEPA-Anything，主張這些差異很大的系統其實可以共用同一套學習配方。

🤔 **問題所在：預測器的「容量分配」困境**

標準的 joint-embedding predictive architecture（JEPA），例如 I-JEPA 或 V-JEPA 2，由 context encoder、EMA target encoder 和一個 predictor 組成，predictor 輸出單一、整塊的目標 embedding。研究團隊將此稱為 capacity-allocation problem：高變異的結構會主導學習過程，變異較弱的模式則會收到互相衝突的梯度，難以被好好學到。

🧩 **方法：正交預測分解（Orthogonal Predictive Factorization, OPF）**

JEPA-Anything 把寬度為 d 的 latent target 拆成 K 個學習到的子空間，每個寬度 r，d = K × r（多數實驗用 K=4），每個子空間（factor）各自配一個獨立的 predictor。這些 factor 的預測結果最後透過投影矩陣的 Moore-Penrose 偽逆（pseudoinverse）重新組合，還原成一個完整的 latent state，供後續 decoding、planning 或 rollout 使用。訓練時會加上三個 regularizer 來維持各 factor 的有效性，OPF loss 直接疊加在每個領域原本的訓練損失上。工程實作上，domain adapter 負責處理各領域的 tokenization 與 encoder，核心函式庫則把共用的核心邏輯封裝成 `OrthogonalFactorProjection`。

正交性對穩定重組至關重要：在 CITRIS Interventional Pong 上，一個參數量相當但沒有正交約束的多頭模型，condition number 高達 438.52；加上正交約束後降到 1.00005，各 factor 之間的重疊幾乎為零。

📊 **七個領域的實驗結果**

| 任務群組 | 指標 | JEPA-Anything | 對照 |
|---|---|---|---|
| 單細胞 PBMC 聚類（AvgBIO） | 分數 | 0.7752 | Cell-JEPA 0.7194 |
| Norman 擾動 | Pearson 相關 | 0.814 | 標準 JEPA 0.787 |
| UK Biobank 臨床事件預測 | 平均 PRAUC | 0.718 | 標準 JEPA 0.711 |
| Interventional Pong 單一干預 | MSE | 下降 34.83% | — |
| 未見過的組合干預 | 誤差改善 | 12.90% | — |
| 6-step 自由 rollout | 誤差改善 | 8.58% | — |
| APEBench Burgers 6-step rollout | 誤差下降 | 約 44.7%（每個 seed 皆改善） | — |

在 CausalWorld、DeepMind Control、PDEBench 與 WeatherBench2 等基準上，JEPA-Anything 在全部 10 個對照的動力學任務上都改善了回報的指標；在以 TrajCast 式骨幹進行的 100-step 分子 rollout 中，於 water、quartz、paracetamol、benzene 四種材料上都拿到最低的 MAE 與 RMSD。

比較特別的是科學分析場景：factor 分析提名了 IL-18 加 CD73 阻斷作為一種癌症干預方案，並在濕實驗室測試（co-culture、患者衍生類器官、腫瘤切片、小鼠模型）中得到支持；在物理場景下，latent 的軌道模式甚至重現了克卜勒定律，擬合斜率為 −1.4991，與理論值 −1.5 相當接近。

⚠️ **並非全面勝出**

在 planning 任務上結果並不一致：在參數量差異控制在 0.3% 以內的條件下，JEPA-Anything 在 Walker2d 與 HalfCheetah 上提升了 CEM return，但在 Hopper 上標準 JEPA 反而表現更好。

🎯 **實務啟示**

如果你的團隊正為不同模態或領域各自維護一套 world model，JEPA-Anything 展示的是另一種思路：把「哪個子空間該學什麼」這件事交給正交分解去解決，而不是手動設計領域專屬架構。但 Hopper 上的反例也提醒,這類通用配方不會在所有控制任務上都穩贏，上線前仍需按任務逐一驗證。

🔗 **來源**
- 標題：Beyond Domain-Specific World Models: JEPA-Anything Uses 1 Recipe for 7 Fields
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/10/05/beyond-domain-specific-world-models-jepa-anything-uses-1-recipe-for-7-fields/

#JEPA #WorldModels #SelfSupervisedLearning #MachineLearning #AIResearch #RepresentationLearning #DeepLearning #ScientificML #RoboticsAI #Stanford
