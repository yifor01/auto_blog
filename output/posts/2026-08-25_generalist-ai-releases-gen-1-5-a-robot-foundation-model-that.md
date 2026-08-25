---
title: 'Generalist AI Releases GEN-1.5: A Robot Foundation Model That Learns New Tasks
  From One 3–12 Second Demo'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/24/generalist-ai-releases-gen-1-5-a-robot-foundation-model-that-learns-new-tasks-from-one-3-12-second-demo/
model: claude-code/sonnet
generated_at: '2026-08-25T06:23:14.516446'
score: 93
---

📌 【機器人基礎模型】看一次示範就會做，GEN-1.5 的物理版「一次性學習」

TL;DR：GEN-1.5 靠單次 3–12 秒示範，就能在情境中學會新的機械操作任務，無需微調。

想像教機器人一個新動作，不用寫程式、不用微調權重，只要「示範一次」，它就照著做——這聽起來像是科幻情節，但 Generalist AI 宣稱已經在自家機器人模型上實現。

🤔 **核心問題：機器人能不能像 GPT-3 一樣一次看懂**

Generalist AI 推出的 GEN-1.5，要解決的問題是：機器人基礎模型能否僅靠單一示範，在不做梯度更新、不微調、不寫任務專屬程式的情況下，直接學會新的物理操作任務。作法是把一段 3–12 秒的 sensorimotor（感測運動）資料，拖放進模型 30 秒的 context window 中，剩餘的視窗空間放置即時觀測資料，模型隨即執行任務。

🧩 **物理提示（physical prompting）如何運作**

GEN-1.5 是一個大型多模態模型，輸入包含影片、感測器訊號、語言與本體感覺（proprioceptive）資料，並以 100 Hz 輸出動作軌跡。它已在住家、倉庫、工廠採集的物理互動資料上，經過超過八個月的持續預訓練。Generalist 表示，這個一次性學習能力（physical prompting）並非刻意設計出來的：模型沒有為此做任何架構改動，沒有 meta-learning loop，也沒有鼓勵即興發揮的輔助目標函式。這項能力是從預訓練規模中「湧現」出來的，作者將其類比為 GPT-3 湧現出的一次性提示（one-shot prompting）能力。

📊 **10 個任務、59% 到 83% 的成功率**

在 10 個多樣化的操作任務上，未經任何訓練、純粹靠一次性 in-context 提示的預訓練模型平均成功率為 59%（標準差 ±10%）。若額外用每個任務 5 分鐘的資料（約 50 筆示範）做 10 次梯度更新，成功率提升至 83%（±9%）。在極端案例中，僅用 1 分鐘資料做 1 次梯度更新，就在一個 held-out 任務上達到 66.5% 的成功率，且未做任何針對性的超參數調整。

值得注意的是，這 10 次梯度更新對模型權重的改動幅度小於 0.15%，Generalist 認為這顯示微調更像是在重新調度模型既有的知識，而不是建構全新的表徵，並將此現象定位為「極低資料量的 test-time training」。

在輕度微調後，模型也展現出泛化能力：訓練資料是「用刷子把方塊刷進碗裡」的 5 分鐘示範，模型卻能改用香蕉充當刷子完成任務，或改用畚箕鏟起再倒出方塊——這是完全不同的接觸序列；它還會自行移除蓋在碗上的一張紙，並在示範只用單手的情況下，展現雙手操作的能力。

⚠️ **只是研究釋出，任務仍偏簡單**

Generalist 自己也坦言，這些任務規模簡單、時間跨度短。目前 GEN-1.5 沒有公開權重、沒有 API、沒有定價頁面，也沒有自助服務產品，全部運算都跑在 Generalist AI 自家的機隊與資料引擎上，外部若想使用，只能透過直接合作的方式。

🎯 **實務啟示**

這份成果的重點不在任務本身有多複雜，而在於「10 次梯度更新」對比機器人策略適應通常需要的數萬次梯度更新，代表了一種完全不同的資料與運算效率量級。對關注機器人 few-shot 學習或基礎模型遷移的工程師來說，physical prompting 這種「以 context window 取代微調」的機制值得持續追蹤，但目前受限於封閉存取，短期內仍難以在自己的專案中直接驗證。

🔗 **來源**
- 標題：Generalist AI Releases GEN-1.5: A Robot Foundation Model That Learns New Tasks From One 3–12 Second Demo
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/08/24/generalist-ai-releases-gen-1-5-a-robot-foundation-model-that-learns-new-tasks-from-one-3-12-second-demo/

#RobotFoundationModel #InContextLearning #GeneralistAI #Robotics #FewShotLearning #PhysicalAI #TestTimeTraining #EmbodiedAI #Manipulation #FoundationModel
