---
title: 'MiniMax Sparse Attention (MSA): a Two-Branch Block-Sparse Attention Trained
  on a 109B-Parameter MoE With a 3T-Token Budget'
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/17/minimax-sparse-attention-msa-a-two-branch-block-sparse-attention-trained-on-a-109b-parameter-moe-with-a-3t-token-budget/
score: 107
model: google/gemma-4-31b-it:free
generated_at: '2026-06-17T20:29:22.507242'
---

📌 【MiniMax 最新研究】解決長文本計算瓶頸：用兩路分支稀疏注意力 (MSA) 實現常數級複雜度

當 LLM 的上下文視窗（Context Window）越來越長，記憶體與計算成本的平方級增長（Quadratic Cost）成了最大的痛點。即便有了 GQA (Grouped Query Attention)，在面對超長文本時，計算開銷依然隨長度線性增加。

MiniMax 團隊提出了一種新的方案：MiniMax Sparse Attention (MSA)。它不嘗試在所有 Token 中找答案，而是先用一個「索引分支」篩選出關鍵區塊，讓計算開銷不再隨文本長度增加而成長。

🤔 **長文本的死穴：Softmax Attention 的平方級開銷**

在標準的注意力機制中，每個 Query 都需要對所有 Key-Value 進行比對，這導致計算複雜度與序列長度 $N$ 成正比 $O(N)$。當 context 增加到數萬甚至數十萬 token 時，推理速度會劇烈下降。即使是 GQA 雖然減少了 KV 緩存的空間，但計算量的基本結構依然沒變。

🧪 **設計核心：將注意力拆分為「索引」與「主路徑」兩路分支**

MiniMax 將注意力機制重新設計為兩階段流程，將粒度從單個 Token 提升到「區塊 (Block)」等級：

1. **Index Branch（索引分支）**：負責決定「哪些 KV 區塊值得讀取」。它透過一組輕量級的投影矩陣，對 KV 區塊進行評分並透過 Max-pooling 轉化為區塊級得分，最後用 Top-k 算子選出得分最高的前 $k$ 個區塊。
2. **Main Branch（主路徑）**：僅針對索引分支選出的關鍵區塊執行精確的 Softmax Attention。

值得注意的是，為了確保局部資訊不丟失，查詢所在的當前局部區塊會被強制納入選取範圍，避免 AI 忘記剛剛才說過的話。

🚀 **從 $O(N)$ 降至 $O(kB_k)$：計算成本不再隨長度增長**

這項設計帶來了顯著的工程優勢：
- **固定計算預算**：預設區塊大小 $B_k = 128$，每組選取 $k = 16$ 個區塊。這意味著每個 Query 的處理預算被固定在 $kB_k = 2,048$ 個 KV tokens。
- **複雜度脫鉤**：傳統 GQA 的複雜度是 $O(N)$（隨長度 $N$ 增加），而 MSA 的複雜度是 $O(kB_k)$。這意味著隨著上下文長度增加，MSA 與傳統方法的計算差距會越來越大，推理效率提升極其顯著。
- **分組獨立性**：在 GQA 組內共享區塊選擇，但不同組別可以關注長文本中不同的遠端區域，保留了模型捕捉多樣化資訊的能力。

💡 **109B MoE 大模型實測，並直接部署於 MiniMax-M3**

這不是一個僅存在於論文中的理論。MiniMax 將 MSA 部署在一個擁有 109B 參數的 MoE（混合專家）模型中，並使用 3T tokens 的原生多模態數據進行訓練。目前該技術已正式應用於其生產級模型 MiniMax-M3 中，並開源了推理內核（Inference Kernel），讓工程師可以直接實作。

⚠️ **區塊化選擇的取捨 (Trade-off)**

雖然 MSA 大幅降低了計算量，但其核心是在「精度」與「速度」之間做權衡。將注意力限制在 Top-k 個區塊中，意味著模型放棄了對所有 token 的全域掃描。雖然這在實務上能大幅加速，但對於極其細碎、且分佈在文本各處的資訊檢索能力是否會受影響，仍需在實際應用中進一步評估。

🎯 **工程實踐啟示：從 Token 粒度轉向 Block 粒度**

對於開發長文本 LLM 的工程師來說，MSA 提供了一個重要的思考方向：**「並非所有 Token 都同等重要」**。透過引入輕量級的索引機制（Index Branch），可以在幾乎不增加參數量（僅增加兩個投影矩陣）的情況下，將計算成本從線性降至常數級。這對於需要處理超長文檔、多模態輸入的生產環境具有極高價值。

🔗 **相關資訊**
📝 MiniMax Sparse Attention (MSA): a Two-Branch Block-Sparse Attention Trained on a 109B-Parameter MoE With a 3T-Token Budget
👤 Asif Razzaq / MiniMax Research Team
🔗 詳情請參閱 MarkTechPost 報導：https://www.marktechpost.com/2026/06/17/minimax-sparse-attention-msa-a-two-branch-block-sparse-attention-trained-on-a-109b-parameter-moe-with-a-3t-token-budget/

你認為「稀疏注意力」會是解決 LLM 長文本成本問題的最終方案嗎？歡迎在下方討論 👇

#AI #LLM #MiniMax #SparseAttention #MoE #長文本 #深度學習 #AI工程
