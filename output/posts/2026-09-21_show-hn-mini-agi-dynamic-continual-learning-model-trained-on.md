---
title: 'Show HN: Mini-AGI – Dynamic continual learning model trained on 8GB VRAM'
source: Hacker News
url: https://github.com/volotat/mini-AGI/
model: claude-code/sonnet
generated_at: '2026-09-21T21:19:53.745923'
score: 85
---

📌 一人打造的持續學習 MoE，8GB VRAM 也能訓練

TL;DR：獨立開發者在消費級顯卡上實作動態增減專家的 MoE，探索小顯存訓練大模型的可能性。

當大家都在討論千億參數模型需要多少張 H100 時，Hacker News 上一則 Show HN 貼文丟出了另一個問題：如果我連 1B 參數的模型都無法在自己的硬體上訓練，那「擁有一個完全由自己掌控、而非被某家公司對齊過的模型」這件事，還有可能嗎？

🤔 **消費級硬體訓不動大模型的不滿**

作者 volotat 在專案 README 中坦言，這個專案源自於他對現況的「深度不滿」：我們可以在消費級硬體上做大模型的推論（inference）與微調（fine-tuning），但幾乎不可能真正從頭訓練一個中等規模（1B 以上）的模型。他想要的，是能完全掌控訓練過程中模型看到什麼資料，而不是依賴某家公司預先訓練好、對齊好的權重。

🧩 **兩個構想：可增減的 MoE 專家，加上 batch 1 的連續資料流**

為了解決這個問題，作者提出兩個構想，並與 Claude 一起腦力激盪後找到了可行的實作方向：

- 第一個構想是讓 MoE（Mixture of Experts）架構中的專家（expert）在訓練過程中動態新增與剪除，且任何時刻只有一小部分專家真正被啟用。作者認為，這樣一來模型規模理論上只受限於硬碟空間，因為專家可以依需要載入與卸載。
- 第二個構想是採用 batch size 為 1 的訓練方式，讓模型讀取單一、連續的資料流，而不是需要儲存大量隨機打亂的 batch 及其對應梯度。如果這個想法真的可行，就能大幅降低對 VRAM 容量的需求。

專案目前的訓練方式，就是把模型設定成連續讀取交錯排列的文字段落，每段長度為 32,000 個字元，當成單一資料流輸入，如同人類閱讀一樣。

📊 **目前的進度：Scaling Law 曲線看起來很有希望**

作者在專案中放出了一張 scaling law 圖表，並表示結果「看起來非常有希望」。目前模型仍在跑訓練語料庫（共 7.8B 字元）的第一輪，權重尚未釋出，依照目前的讀取速度，還需要大約兩週才能訓練完成。README 中也附上了整個訓練過程中的取樣輸出連結，讓外界可以觀察模型的學習狀況。

⚠️ **仍在早期階段，權重未公開**

作者明確說明，這個專案還在進行中，模型的正式權重要等訓練跑完才會釋出。他也坦承整個開發過程大量使用了 AI 協助，並認為若沒有 AI 的幫助，這個專案對他來說「完全不可能」完成。

🎯 **實務啟示**

對於想在有限硬體資源下探索訓練基礎設施的工程師來說，這個專案示範了一種思路：與其一味追求更大規模，不如重新設計架構（動態專家增減）與訓練流程（batch 1 連續資料流），讓「用得起」的硬體也能參與訓練實驗。作者也強調整個設定相當簡單，git clone 後即可直接執行並觀察訓練過程，適合對持續學習（continual learning）與 MoE 架構感興趣的人親自動手驗證構想。

🔗 **來源**
- 標題：Show HN: Mini-AGI – Dynamic continual learning model trained on 8GB VRAM
- 作者／機構：volotat
- 連結：https://github.com/volotat/mini-AGI/

#MixtureOfExperts #ContinualLearning #OpenSource #MachineLearning #AGI #ConsumerGPU #DeepLearning #ModelTraining #AIResearch #MoE
