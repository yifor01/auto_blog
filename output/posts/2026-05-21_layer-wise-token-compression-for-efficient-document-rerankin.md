---
title: "Layer-wise Token Compression for Efficient Document Reranking"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.20683
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-05-21T20:43:13.598682
---

📌 【Amazon AGI】Layer‑wise Token Compression 加速 Reranker  

你以為讓 Transformer 更快只能犧牲準確度？這篇論文證明，在中間層做 token 壓縮，既能提升吞吐，又不損失排名品質。  

🤔 **現有 reranker 在長序列上計算成本高**  
現代資訊檢索系統依賴 Transformer‑based cross‑encoder 進行 query‑document 重新排序。雖然表現優秀，但模型在推論時必須處理完整的長序列，導致計算開銷大、吞吐量低。現有的 token compression 多僅作用於初始嵌入層，對 bi‑encoder 有效，但對 cross‑encoder 的效果卻不明顯。  

🧪 **在中間 transformer 層進行自適應 token 池化**  
作者提出 Layer‑wise Token Compression (LTC)：在 transformer 的中間層依序進行自適應的 token 池化，將相鄰的 token 合併，從而減少後續層需要處理的 token 數量。透過在 MS MARCO passage 與 document 排名任務上的大量消融實驗，他們比較了不同層級的壓縮策略，驗證哪一層的壓縮能保持排名品質同時提升效率。  

 **壓縮中間層可提升 QPS 高達 116%，排名品質不受影響**  
實驗結果顯示：在 passage 排名任務上，LTC 使 inference QPS 提升最高 25%；在 document 排名任務上，提升最高達 116%。同時，排名指標（如 MRR、NDCG）與未壓縮的基準模型無顯著差異。此外，將 LTC 擴展至 listwise LLM reranker 時，同樣的做法可直接適用於長上下文的 listwise 重新排序，吞吐量提升更為顯著。  

💡 **壓縮可能充當正則化器，促進長短文件表示的一致性**  
更有趣的是，當使用在短通路上訓練的 reranker 被應用於長文件排名任務時，經過 LTC 訓練的模型反而優於未壓縮的對手。作者認為，中間層的 token 池化迫使模型學習更具長度不變性的表示，這種效應類似於正則化，有助於模型在不同長度的文件上保持一致的排名能力。  

⚠️ **實驗主要集中在 MS MARCO，長期效果與其他架構尚待驗證**  
研究僅在 MS MARCO passage 與 document 集合上進行 ablation，未涵蓋其他基準資料集。樣本主要為短至中等長度的 query‑document 對，長文件行為的普遍性仍需進一步驗證。此外，LTC 目前僅在標準 transformer encoder 上驗證，是否適用於其他變體（如稀疏或混合專家模型）尚未探討。  

🎯 **工程師可在現有 reranker 流程中插入 LTC 以獲得顯著吞吐提升**  
對於需要高 QPS 的線上排序服務，可在訓練階段加入中間層的自適應 token 池化，推論時不需額外修改架構。這種做法既能降低計算成本，又不犧牲排序品質；而在訓練短文件模型時，同樣的壓縮策略或許能間接提升模型對長文件的泛化能力。  

🔗 **論文連結**  
📝 Layer-wise Token Compression for Efficient Document Reranking  
👤 Shengyao Zhuang, zhichao Xu, Ivano Lauriola @ Amazon AGI; Amazon AWS  
🔗 https://arxiv.org/abs/2605.20683  

你的 reranker 系統是否正在尋找「不犧牲品質」的加速方案？歡迎在留言區分享你的想法或實作經驗 👇  

#AmazonAGI #InformationRetrieval #Reranking #TokenCompression #MachineLearning #AIEngineering #MSMARCO #LLM #SearchTech
