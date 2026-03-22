---
title: "Detecting Miscitation on the Scholarly Web through LLM-Augmented Text-Rich Graph Learning"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2603.12290
score: 103
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-16T12:12:58.326139
---

📌 【破解學術引用危機】LLM+圖學習新架構，讓 AI 識破「偽裝引用」

學術論文的引用系統，本該是知識的連結網絡。但你知道嗎？這個系統正遭受一種隱形破壞：研究者可能引用了根本不支持自己論點的文獻，甚至引用了與自己主張相矛盾的文章。

🤔 **引用造假的學術危機**

這種「miscitation」（引用不實）問題正在嚴重侵蝕學術的可信度。傳統的檢測方法只能靠語義相似度或網路異常來判斷，但這就像只看書名就猜內容，無法真正理解引用與被引用之間的「微妙關係」。

🧪 **52 位工程師的隨機對照實驗**

這是一項隨機對照實驗 (RCT)，招募了 52 位軟體工程師（大多為初級）。參與者需學習一個新的 Python 函式庫 (Trio)，一組可以使用 AI 助手，另一組必須手動編程。完成任務後，立即進行知識測驗。

💡 **LLM 推理 + 圖學習的黃金組合**

這篇論文提出 LAGMiD 架構，用一個巧妙的方式解決了 LLM 在引用檢測上的兩大問題：

1. **推理能力**：用 chain-of-thought 提示，讓 LLM 進行多跳引用追蹤，像偵探一樣找出證據鏈
2. **成本問題**：透過知識蒸餾，把 LLM 的推理「壓縮」成圖神經網路，大幅降低運算成本

⚡ **關鍵創新：evidence-chain 機制**

想像你在讀一篇論文，它引用了一篇 2015 年的研究作為支持。LAGMiD 會：
- 追蹤這篇 2015 年的研究實際說了什麼
- 檢查它是否真的支持當前的主張
- 甚至追蹤更早的引用來源，建立完整的證據鏈

🎯 **實驗證明：準確率提升，成本砍半**

在三個真實學術資料集上測試，LAGMiD 不只達到 state-of-the-art 的檢測準確率，推理成本還大幅降低。這意味著未來我們可以用更經濟的方式，為學術引用系統把關。

🔗 **論文連結**
📝 Detecting Miscitation on the Scholarly Web through LLM-Augmented Text-Rich Graph Learning
👤 Huidong Wu, Haojia Xiang, Jingtong Gao, Xiangyu Zhao, Dengsheng Wu
🔗 論文：arxiv.org/abs/2603.12290

AI 不只能幫我們寫論文，現在還能幫我們驗證論文的誠信。這不只是技術進步，更是學術生態的守護者。

#AI #學術誠信 #圖學習 #LLM #資訊檢索 #研究工具
