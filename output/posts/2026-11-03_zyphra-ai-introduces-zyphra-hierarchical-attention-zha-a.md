---
title: 'Zyphra AI Introduces Zyphra Hierarchical Attention (ZHA): A Path to True Subquadratic
  Attention'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/02/zyphra-hierarchical-attention-zha-sparse-attention/
model: claude-code/sonnet
generated_at: '2026-11-03T22:31:22.598053'
score: 101
---

📌 Zyphra 用樹狀索引解稀疏注意力瓶頸

TL;DR：ZHA 用樹狀索引器壓縮搜尋，讓稀疏注意力的索引開銷不再隨上下文線性增長。

稀疏注意力本該省運算，但當上下文衝到 1M tokens，替每個 query 挑選相關 key 的「索引器」本身卻可能吃掉 60% 到 90% 的層運算時間，稀疏反而變成另一種昂貴。

🤔 索引器本身沒有真的變稀疏

像 DeepSeek Sparse Attention 這類細粒度稀疏注意力方法，最終選出的 attention 確實是稀疏的，但做選擇用的索引器仍要幫每個 query 把過去所有 token 都打分一遍，索引器本身的運算量還是跟著完整上下文線性成長。SSM、sliding window 這類固定狀態方法則在長上下文時效能會飽和。Zyphra Hierarchical Attention（ZHA）要解的，正是「索引器本身也要變稀疏」這個問題。

🧩 把 key 壓成摘要，再用學出來的 query 逐層篩選

ZHA 保留完整的 KV cache，只是用一棵樹來決定每個 query 該讀哪些被快取的 key。做法是把 key 切成連續的區塊（chunk），把每個區塊壓縮成一個摘要 key，再把這些摘要逐層分組、再次壓縮；以 chunk size 4 為例，6 層就能讓最頂層一個節點覆蓋 4,096 個 token。摘要的生成仰賴一小組「學出來的參考 query」（learned reference queries），每個參考 query 對一個區塊的 log attention mass 給出一個切平面估計值，取這些估計值的最大值，近似任何未來 query 會給這個區塊多少注意力。解碼時，query 先替最頂層節點打分，只保留能涵蓋估計注意力總量中 p 比例的最小節點集合，然後只展開這些節點的子節點，重複此過程直到抵達真正的 KV 項目。這個 top-p 機制讓運算預算隨查詢內容自動調整：只需要查一個事實的 query 只展開少數分支，需要大範圍比對資訊的 query 才會展開更多分支。第一個 token 永遠被保留做為 attention sink。

📊 深樹保留度勝過 MSA，壓縮比不犧牲準確率

Zyphra 把 Qwen3.6-35B-A3B 轉換成兩種樹結構：深樹（chunk 4、6 層）和寬樹（chunk 256、1 層），都使用 16 個參考 query、p = 0.95，整個轉換只用約 3.98B tokens、1,900 個訓練步驟、32K 上下文，且只訓練參考 query，底層模型全程凍結，訓練訊號是用 KL loss 讓每層每個區塊的注意力分布貼近原始 dense attention。作為對照，團隊也用 10 倍資料量（40B tokens）訓練了一個 MiniMax Sparse Attention（MSA）索引器。

| 評測 | ZHA 深樹 | MSA |
|---|---|---|
| RULER-13 | 93% 以上 | 77.1% |
| LongBench v2（讀取 key 比例相近，約 1%） | 比 MSA 高 14.1 分 | 基準 |

在 28 種樹狀幾何設定中，只要讀取 10% 到 30% 的 key，RULER 準確率都能維持穩定，樹愈深、在相同壓縮比下能撐住的稀疏程度愈高；團隊用一個只有 4 個參數的模型就能從樹狀幾何預測 RULER 準確率，RMSE 僅 1.44 分。延遲方面，Zyphra 沒有公開核心運算的 kernel 實作，而是用 roofline 模型估算單層、batch size 1 的解碼延遲。在輕量設定下（1 個參考 query、chunk 8、p = 0.75），模型估算 ZHA 在上下文達到約 48K tokens 時開始超越 dense attention，約 0.48M tokens 時超越 MSA；推算到 1B tokens，預期加速可達 dense attention 的 373 到 417 倍、MSA 的 52 到 58 倍，部落格文章也補充 10M tokens 時的加速為 32 到 35 倍（對 dense）與 4.7 到 5.1 倍（對 MSA）。在 256K 這種較實際的長度下，增益溫和許多：Pareto 前緣的設定只能拿到 1.93 到 2.28 倍加速，對應 RULER-13 準確率 92.7% 到 96.4%。

⚠️ 仍是模型化估算，小模型轉換效果不佳

文中所有延遲數字都來自 roofline 模型推算，而非實際跑出來的 kernel benchmark，真實部署時的加速可能與估算有落差。Zyphra 也坦承參數量低於 1B 的模型在轉換成 ZHA 時表現不佳，要到 4B 參數以上效果才明顯改善。

🎯 實務啟示

對需要處理長上下文（例如 256K 以上）的團隊，ZHA 的樹狀索引器提供了一個可以在凍結的 pretrained 模型上，只用相對小量 token（約 4B）完成轉換的稀疏注意力選項，不必重新訓練整個模型。但在導入前，應留意目前公開的加速數字多數來自理論模型而非已發布的 kernel，實際落地效果仍需等待官方釋出可執行的運算核心後再驗證。

🔗 來源
- 標題：Zyphra AI Introduces Zyphra Hierarchical Attention (ZHA): A Path to True Subquadratic Attention
- 作者／機構：Asif Razzaq／MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/02/zyphra-hierarchical-attention-zha-sparse-attention/

#ZyphraHierarchicalAttention #SparseAttention #LongContext #LLM #TransformerArchitecture #AttentionMechanism #Qwen #EfficientAI #MachineLearning #ModelOptimization
