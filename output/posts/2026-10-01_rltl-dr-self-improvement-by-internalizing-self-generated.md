---
title: 'RLTL;DR: Self-Improvement by Internalizing Self-Generated Feedback'
source: Apple ML
url: https://machinelearning.apple.com/research/rltl-dr-self-improvement
model: claude-code/sonnet
generated_at: '2026-10-01T21:59:51.306590'
score: 106
---

📌 Apple新作RLTL;DR：自產回饋如何打破RLVR瓶頸

TL;DR：Apple提出RLTL;DR，讓模型內化自己寫的失敗筆記，在Pass@128=0的難題上從0%衝到14-31%。

強化學習與可驗證獎勵（RLVR）的標準做法，是讓 agent 對一項任務多次嘗試，再把訓練訊號集中在成功的那幾次上。問題是，當任務難到 agent 幾乎不可能成功、又沒有教師模型或範例解答可以蒸餾時，這套機制根本無從啟動。Apple 的研究團隊在 NeurIPS 發表的 RLTL;DR，試圖解決這個自我提升（self-improvement）的死結。

🤔 **當任務難到連 128 次嘗試都全軍覆沒**

論文鎖定的場景很極端：在困難的 tool-calling 與程式設計資料集上，先篩選出 Pass@128 = 0 的題目，也就是模型嘗試 128 次都無法答對的任務。在這種情境下，標準 GRPO 訓練 Qwen 3.5 9B Thinking 策略模型，Pass@1 一直停滯在 0% 到 1%，完全學不動——因為沒有任何一次成功的 rollout 可以作為正向訊號。

🧩 **讓模型自己寫一句 TL;DR，再把它寫進權重裡**

RLTL;DR 的做法是：每次嘗試失敗後，把驗證器（verifier）的輸出展示給策略模型看，讓它自己寫一條 TL;DR 式的洞見（insight）作為回饋；下一次 rollout 會以所有先前累積的洞見為條件（conditioned），依序取樣 rollout 直到找到解答為止。更關鍵的一步，是對這些「上下文中的洞見」做反向傳播（backpropagation），讓模型把「任務 → 洞見」這個映射直接內化進參數裡，而不只是停留在 prompt 層面的提示。

為了進一步拆解這個效果從何而來，團隊還做了一個簡化版 SFTL;DR：完全不展示也不對任何 rollout 做反向傳播，只用（任務, 洞見）這種配對資料做監督微調。

📊 **內化之後，不用提示也能維持 12-13% Pass@1**

結果顯示，RLTL;DR 突破了標準 GRPO 卡住的學習障礙：在訓練時上下文中帶著洞見，Pass@1 達到 14% 到 31%；更重要的是，到了評估階段，即使上下文中完全不放洞見，Pass@1 仍能維持在 12% 到 13%——證明模型確實把「任務 → 洞見」的映射學進了自己的權重，而不是單純依賴提示工程。

團隊進一步確認，關鍵就在這個內化過程本身：簡化版的 SFTL;DR 只用 4,000 筆（任務, 洞見）配對資料訓練，完全不碰任何 rollout，就幾乎追平了 RLTL;DR 以及在完整 rollout 上做傳統 SFT 的效果。

💡 **一種更精簡的訓練範式**

這個結果指出一種值得延伸的訓練思路：與其蒐集大量完整 rollout 軌跡去蒸餾，不如蒐集「這類任務該記住這種重點」式的精簡洞見配對，就能達到接近的效果。對計算成本敏感的自我提升訓練場景而言，這代表一條更經濟的路徑。

🎯 **實務啟示**

如果你正在為難度極高、幾乎沒有成功範例可蒸餾的任務設計 RL 訓練流程，這篇論文提示了一個可嘗試的方向：先讓模型對自己的失敗寫洞見、把洞見放進下一輪的上下文，再對這些洞見做反向傳播以求內化；若計算資源有限，甚至可以跳過完整 rollout，只蒐集（任務, 洞見）配對做監督微調，用更低成本逼近類似效果。

🔗 **來源**
- 標題：RLTL;DR: Self-Improvement by Internalizing Self-Generated Feedback
- 作者／機構：Michael Kirchhof, Eleonora Gualdoni, Andrew Szot, Khashayar Gatmiry, Aryo Lotfi, Abbas Kazerouni, Omar Attia, Sanjoy Chowdhury, Alexander Toshev／Apple
- 連結：https://machinelearning.apple.com/research/rltl-dr-self-improvement

#ReinforcementLearning #RLVR #SelfImprovement #Apple #NeurIPS #LLM #GRPO #SelfSupervised #AIResearch #MachineLearning
