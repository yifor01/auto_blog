---
title: "Mixture-of-Depths Attention"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2603.15619
score: 116
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-17T18:37:07.327941
---

# 📌 【深度擴展新突破】MoDA：讓 Transformer 真正深入思考

隨著大語言模型越來越深，一個關鍵問題浮現：為什麼越深的模型表現不一定越好？

🤔 **深度擴展的隱藏瓶頸**

當我們讓 Transformer 變得更深時，會發生什麼事？研究發現，淺層學習到的有價值特徵，會在後續的殘差連接中逐漸被稀釋，這就是所謂的**訊號退化**問題。簡單說，模型越深，就越難記住一開始學到的好東西。

🧪 **MoDA 的巧妙設計**

來自華中科技大學與字節跳動的研究團隊提出**Mixture-of-Depths Attention (MoDA)**，讓每個 attention head 不只看當前層的輸入，還能「回頭看」前面層的特徵。這就像讓模型在思考時，能同時參考當前的觀察和過去的經驗。

💡 **關鍵創新：跨層特徵融合**

MoDA 的核心是讓 attention head 能同時 attend to：
- 當前層的 sequence KV pairs（當下的觀察）
- 前面層的 depth KV pairs（過去的記憶）

這種設計讓模型能更好地保留淺層學到的資訊，避免隨著深度增加而遺失重要特徵。

⚡ **高效能實作**

MoDA 的一大挑戰是非連續的記憶體存取模式，但研究團隊設計了一套硬體高效能演算法，在 64K 序列長度下仍能達到 **97.3% 的 FlashAttention-2 效率**。這意味著你幾乎不需要為了 MoDA 付出額外的計算成本。

📊 **實驗結果**

在 1.5B 參數模型上的測試顯示：
- 在 10 個驗證集上平均困惑度降低 **0.2**
- 在 10 個下游任務上平均表現提升 **2.11%**
- 計算開銷僅增加 **3.7% 的 FLOPs**

值得注意的是，MoDA 與 post-norm 的組合表現優於 pre-norm，這為模型架構設計提供了新的參考。

🎯 **為什麼這很重要**

MoDA 解決了深度擴展的核心瓶頸，讓我們能更有效率地讓模型變深，而不會犧牲表現。這對於追求極致效能的大型語言模型研究尤其重要。

🔗 **論文連結**
📝 Mixture-of-Depths Attention
👤 Lianghui Zhu, Yuxin Fang, Bencheng Liao, Shijie Wang, Tianheng Cheng
🏢 Huazhong University of Science & Technology; ByteDance Seed
🔗 論文：arxiv.org/abs/2603.15619
🔗 程式碼：github.com/hustvl/MoDA

你對深度擴展有什麼看法？歡迎分享你的觀點 👇

#AI #Transformer #深度學習 #MoDA #大語言模型 #LLM #AttentionMechanism #技術突破
