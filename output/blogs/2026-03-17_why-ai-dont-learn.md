---
title: "LeCun 最新論文：為什麼你的 AI 部署之後就不再學習了"
date: "2026-03-17"
paper_url: "https://arxiv.org/abs/2603.15381"
paper_title: "Why AI systems don't learn and what to do about it: Lessons on autonomous learning from cognitive science"
tags: [Autonomous-Learning, Cognitive-Science, LeCun, META-FAIR]
tldr: "AI 部署後就停止學習，認知科學告訴我們怎麼修"
---

Yann LeCun、Jitendra Malik、Emmanuel Dupoux，分別來自 META FAIR、NYU、UC Berkeley 和 EHESS，三個人聯名出了一篇 position paper，標題直接問：為什麼 AI 系統不會學習？

聽起來很矛盾。Machine「learning」不就是在學嗎？

但他們指的是另一件事。你花了幾個月訓練好一個模型，部署上線之後，它就再也不學任何新東西了。它的世界在訓練結束那一刻凍結了。一個三歲小孩不是這樣運作的。

🧒 小孩會的，AI 不會

這篇論文最核心的觀察其實很直覺。六個月大的嬰兒會自動把注意力放在人臉上，沒有人標註說「這是人臉，請注意」。到了十二個月，他們從能分辨所有語言的語音差異，收斂到只對母語的音位敏感。這是自發性的 curriculum learning，沒有人在旁邊幫他們排 training schedule。

再看直覺物理。嬰兒看到「不可能事件」會多看幾眼。一個球穿過固體牆壁？他們盯著看更久。代表他們已經建了某種 world model，而且知道什麼時候預測出錯了，然後把注意力分配給出錯的地方。

現在的 AI 呢？你餵什麼它就吃什麼，你不餵它就什麼都不吃。部署後的 LLM 不會自己決定「我對量子計算理解不夠，我應該去多讀一些」。

它甚至不知道自己不知道什麼。

🧩 三個系統

論文提出了一個認知科學啟發的框架，把學習拆成三個子系統：

System A「觀察學習」。從被動資料中學表徵，self-supervised learning 就是典型的例子。優點是能大規模 scale，缺點也很明顯：需要人類幫忙整理資料、無法自己選擇要看什麼、分不清因果和相關性。想像成一個很會讀書但從不出門的學生。

System B「行動學習」。就是 RL，透過跟環境互動來學。它是 grounded 的，能建立因果關係。但樣本效率極差，而且需要有人定義好獎勵函數。在自然環境中，哪有人幫你寫 reward function？

System M「元控制」。這是整篇論文最關鍵的提案。它監控低維度的 telemetry（預測誤差、不確定性、獎勵趨勢），然後決定現在應該讓 A 學、讓 B 學、還是把東西存進記憶體。它不直接處理高維原始資料，只看「儀表板」上的指標。

用白話講：System M 就是那個決定「現在該讀書、該練習、還是該睡覺」的東西。

論文把它類比成「演化上硬編碼的狀態轉移表」。嬰兒天生就會注意人臉和語音，這是硬編碼的。Critical period 就是演化幫我們設定好的 learning rate schedule，語音學習窗口大概在六到十二個月，錯過就很難再到母語水準。睡眠鞏固記憶、好奇心驅動探索，這些都是 System M 的生物學版本。

🧬 怎麼建？演化的雙層優化

這裡有個我覺得很漂亮的想法。System M 不是靠個體學習來的，而是靠演化。

→ 內層迴圈：一個 agent 的一生，System M 根據硬編碼規則調度 A 和 B 的學習
→ 外層迴圈：演化，根據 fitness 優化 System M 本身的參數

用 AI 的術語講就是 bilevel optimization。內層是 agent 的 lifetime learning，外層是 architecture search。

🤖 對 LLM 的批評

論文對當前 LLM 的批評很直接，列了三個結構性問題：

→ 資料牆。高品質文本是有限的，你不可能靠讀更多書來超越人類知識的邊界。要發現新知識，你需要跟環境互動。

→ 太偏重語言。人類智能有很大一部分是空間的、身體的、直覺物理的。LLM 對「重力」的理解來自讀過的句子，不是來自東西掉下來的經驗。

→ 部署後靜態。沒有 System M 來判斷「我在這個領域一直預測錯，應該多花時間在這裡」。用戶的唯一選擇是 prompting 或 fine-tuning，但這些都是人類主動介入，不是模型自主學習。

然後論文指出三個阻擋進展的路障：ML 子領域太碎片化（做 SSL 的不跟做 RL 的對話）、學習被外包給人類工程師、沒有有效方法 scale 三者耦合的系統。

🤔 我怎麼看

先說清楚，這是 vision paper，不是實驗論文。沒有新 benchmark、沒有 ablation study。它的價值在於把一個大家隱約知道但很少系統性討論的問題整理成清晰的框架。

System M 是最有啟發性的部分。現在很多人在做 agent，但大部分 agent 的決策都在 task level，決定下一步用哪個工具。System M 談的是 learning level 的決策，決定現在應該學什麼、怎麼學、學多久。完全不同的層次。

不過我也有疑慮。把 System M 設定成「演化硬編碼」其實是繞過了最難的問題：怎麼學到好的 meta-control policy？在生物學裡這靠幾十億年的演化，在 AI 裡我們有什麼等價物？論文提了 bilevel optimization，但實際怎麼做、規模能不能上去，都還沒有答案。

另一個想法。也許 LLM 的下一步不是「部署後持續學習」，而是「部署後持續收集需要學習的東西，然後定期重訓」。工程上可行得多，雖然不如論文的願景那麼優雅。

如果你做 agent 或 continual learning，這篇框架值得花 30 分鐘讀。它不會告訴你明天該寫什麼 code，但可能改變你思考「學習」這件事的方式。

📄 論文：https://arxiv.org/abs/2603.15381

<!-- fb -->

Yann LeCun、Jitendra Malik、Emmanuel Dupoux（META FAIR / NYU / UC Berkeley / EHESS）聯名問了一個問題：為什麼 AI 系統不會學習？

你花幾個月訓練好模型，部署上線後它就再也不學新東西了。一個三歲小孩不是這樣的。

🧩 三個系統
→ System A「觀察學習」：SSL，能 scale 但需要人整理資料，分不清因果
→ System B「行動學習」：RL，能建因果但樣本效率極差
→ System M「元控制」：監控預測誤差和不確定性，決定現在該讓 A 學、B 學、還是存記憶體

用白話講：System M 就是那個決定「現在該讀書、該練習、還是該睡覺」的東西。

🤖 對 LLM 的三個批評
→ 資料牆：高品質文本有限，靠讀更多書無法超越人類知識邊界
→ 太偏重語言：人類智能有大量空間和身體直覺
→ 部署後靜態：沒有機制判斷「我哪裡不足」

🤔 這是 vision paper，沒有實驗。但 System M 的概念很有啟發性。現在的 agent 在 task level 做決策，System M 談的是 learning level 的決策。完全不同的層次。

#GenAI #LeCun #METAFAIR #AutonomousLearning #CognitiveScience #LLM
