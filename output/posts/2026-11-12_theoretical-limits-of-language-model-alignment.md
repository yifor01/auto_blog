---
title: Theoretical Limits of Language Model Alignment
source: Apple ML
url: https://machinelearning.apple.com/research/theoretical-limits-alignment
model: claude-code/sonnet
generated_at: '2026-11-12T23:04:19.020564'
score: 86
---

📌 【Apple ML 研究】對齊模型到底能做到多好?KL 預算給出了理論上限

TL;DR:這篇 NeurIPS 論文用資訊理論算出 KL 約束下對齊能帶來的最大 reward 提升,並發現 PPO、GRPO 離這個上限還很遠。

RLHF、best-of-N 這些對齊技巧已經是訓練語言模型的標準配備,但一個基本問題始終沒有乾淨的答案:在固定的 KL-divergence 預算下,reward 到底能提升多少才算「到頂」?Apple ML 這篇論文(Lucas Monteiro Paes、Natalie Mackraz、Barry-John Theobald、Federico Danieli,將發表於 NeurIPS)試圖把這個問題講清楚。

🤔 **核心問題:對齊的「天花板」在哪裡**

語言模型對齊的兩種主流做法,一種是在 KL-divergence 約束下最大化期望 reward 的強化學習,另一種是從 N 個獨立樣本中挑出 reward 最高者的 best-of-N。這兩種方法用得非常廣,但論文指出,在固定 KL 預算下「reward 最多能提升多少」這個基本的理論限制,過去一直沒有被說清楚。

🧩 **用 Jeffreys divergence 取代舊有的 √KL 估計**

論文的第一個結果是推導出一個封閉形式(closed-form)的表達式,描述在固定 KL 預算下最佳可達成的 reward 提升量。關鍵差異在於:這個表達式是由 Jeffreys divergence 項主導,而不是過去分析中常用的 √KL。作者進一步把這個表達式重新表示為「base model 底下的共變異數(covariance)」,由此得到一個實用的估計器,可以只用 base model 的採樣結果來預測可達成的對齊增益,不需要真的跑完整個對齊流程。

論文還把分析延伸到 proxy reward 的情境:當實際使用的 reward model 只是真實偏好的代理(proxy)時,理想對齊與 proxy 對齊之間的落差(也就是 reward hacking)會隨著 reward 誤差的幅度擴大,也會在 KL penalty 係數變小時擴大。作者接著證明了 reward ensembling(多個 reward model 集成)能緩解 reward hacking,為這個業界已經在用的技巧提供了理論上的解釋。

📊 **best-of-N 貼著理論上限,PPO 與 GRPO 明顯跑輸**

實驗部分,作者針對兩個任務(safety 與 summarization)計算出 KL–reward 的 Pareto frontier,結果顯示 best-of-N 非常接近理論上限,而 PPO 和 GRPO 則明顯落後,離最優解還有相當差距。

⚠️ **限制:最優解的代價是推論成本**

作者坦言,理論上的最優對齊策略目前主要靠 best-of-N 這種需要大量採樣的方法才能接近,這意味著要達到理論上限,勢必要付出高昂的推論成本。論文的結論是,現有的強化學習式對齊演算法(PPO、GRPO)還需要進一步的演算法改進,才能在不犧牲推論效率的前提下逼近這個理論上限。

🎯 **實務啟示**

對做 RLHF 或 DPO 的工程團隊來說,這篇論文提供了一個可操作的訊號:如果你的 reward 提升已經接近用 base model 樣本估計出的理論上限,那麼繼續加大 KL 預算或換更複雜的 RL 演算法可能邊際效益有限;反之,如果 PPO/GRPO 的結果離上限還很遠,問題可能出在演算法本身的效率,而不是 reward model 或資料品質。

🔗 **來源**
- 標題:Theoretical Limits of Language Model Alignment
- 作者／機構:Lucas Monteiro Paes、Natalie Mackraz、Barry-John Theobald、Federico Danieli(Apple ML,NeurIPS 2026)
- 連結:https://machinelearning.apple.com/research/theoretical-limits-alignment

#LanguageModelAlignment #RLHF #AppleML #NeurIPS #RewardHacking #PPO #GRPO #BestOfN #KLDivergence #AIAlignment
