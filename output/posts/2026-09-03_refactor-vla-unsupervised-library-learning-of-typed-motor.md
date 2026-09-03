---
title: 'REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs'
source: Apple ML
url: https://machinelearning.apple.com/research/refactor-vla-motor-programs
model: claude-code/sonnet
generated_at: '2026-09-03T20:12:21.196989'
score: 104
---

📌 【Apple ML 研究】VLA 模型別再「一根腸子通到底」：REFACTOR-VLA 讓機器人自己整理出可重用技能庫

TL;DR：Apple 提出 wake/sleep 架構的 REFACTOR-VLA，讓機器人策略自動聚類出可重用的「有型別」動作技能。

多數現行的視覺-語言-動作（VLA）模型，包括 OpenVLA、π0、RT-2、RDT-1B，本質上都是「單體式」的：它們直接生成原始動作指令或極短的動作序列，沒有把行為組織成可重用、定義清楚的抽象。這導致這些模型在長時程（多步驟）任務上表現不佳，而且很難解讀模型到底學到了什麼。

🤔 現有技能發現方法迴避了一個核心問題

Apple ML 團隊指出，既有的技能發現方法大多迴避了「如何判斷兩段動作序列在行為上是否等價」這個核心問題。像 AtomicVLA、AtomSkill 是靠對比嵌入（contrastive embeddings）做聚類來分組動作序列；BLADE、LRLL 則交給大型語言模型判斷兩段序列是否等價，但這些 LLM 並未針對機器人自身的動力學特性做校準。

🧩 wake/sleep 架構：讓世界模型自己判斷「行為等價」

REFACTOR-VLA 引入一套 wake/sleep 架構來學習可重用技能。在 sleep 階段，系統利用一個學習到的潛在世界模型 Mφ 進行動作 rollout，並以此為基礎的「行為等價核」（Behavioral-Equivalence Kernel, BEK）對動作程式片段進行聚類。在 wake 階段，系統依照受 Hindley-Milner 型別系統啟發的詞彙表，生成有型別的 lambda 項（結構化的簡單程式），再交由一個以技能庫為條件的整流流（rectified-flow）動作解碼器產生實際動作。只有同時通過最小描述長度（MDL）準則與「回報保留」門檻（return-preservation gate）的抽象，才會被接受為正式技能。

🧩 三階段訓練排程

訓練分三個階段進行：Phase A（世界模型暖身）訓練潛在世界模型 Mφ；Phase B（wake 階段策略最佳化）最佳化使用技能庫的策略；Phase C（sleep 階段技能發現）將動作片段聚類成可重用技能。

📊 LIBERO 基準測試：世界模型不是越大越好

團隊在完整的 LIBERO 基準測試套件上評估 REFACTOR-VLA，得出兩項主要發現。第一，單純把潛在世界模型從 1.88 億參數放大到 4.3 億參數，反而在全部 4 個基準測試套件上都拖累了表現，推翻了「世界模型越大越好」的直覺假設。第二，訓練目標的選擇影響巨大：在 Phase A 世界模型暖身階段加入輔助的監督式對比損失（具體為 InfoNCE loss），大幅提升了 Phase C sleep 階段技能聚類的品質。團隊以 n=3 多重隨機種子測得的正規化互資訊（Normalized Mutual Information, NMI）如下：

| 測試套件 | NMI（n=3） |
|---|---|
| Object suite | 0.462 ± 0.021 |
| Spatial suite | 0.867 ± 0.025 |
| Goal suite | 0.915 ± 0.013 |
| LIBERO-10 suite | 0.754 ± 0.010 |

💡 這對機器人策略設計的意義

這項結果暗示，比起一味擴大世界模型規模，訓練目標的設計（例如加入對比式輔助損失）對技能聚類品質的影響更為關鍵，這與近期不少「規模至上」的直覺相左，值得後續在其他機器人基準上驗證是否具有普適性。

🎯 實務啟示

如果你正在開發長時程機器人操作任務的 VLA 系統，REFACTOR-VLA 的結果提示了一個值得參考的方向：與其單純堆大世界模型的參數量，不如優先檢視表徵學習的訓練目標是否有助於下游的技能聚類品質；同時，將動作抽象成有型別、可組合的技能單元，也是提升長時程任務可解讀性的一條可行路徑。

🔗 來源
- 標題：REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs
- 作者／機構：Riyaaz Shaik, Chandru Venkataraman @ Apple Machine Learning
- 連結：https://machinelearning.apple.com/research/refactor-vla-motor-programs

#VLA #RobotLearning #ApplyML #SkillDiscovery #WorldModel #EmbodiedAI #LIBERO #RoboticsResearch #RepresentationLearning #ComputerVision
