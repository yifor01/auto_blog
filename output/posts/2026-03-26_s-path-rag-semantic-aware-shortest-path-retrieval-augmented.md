---
title: "S-Path-RAG: Semantic-Aware Shortest-Path Retrieval Augmented Generation for Multi-Hop Knowledge Graph Question Answering"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2603.23512
score: 103
model: gpt-4o-free
generated_at: 2026-03-26T19:51:54.927917
---

📌 S-Path-RAG：語意感知最短路徑檢索增強生成  

現有的 Retrieval‑Augmented Generation 在大型知識圖上做多跳問答時，常常靠一次性、文字堆砌的檢索：token 消耗大、路徑難以追蹤，且缺乏對圖結構的敏感度。當模型不確定時，缺乏機制去動態調整檢索範圍，導致答題品質與證據完整性受限。  🤔 **多跳知識圖問答需要同時顧及語意與拓樸，傳統檢索耗 token 且難解釋**  

🧪 **結合 k‑shortest、beam 與受限隨機遊走，學習可微分路徑評分器與對比編碼器**  
S-Path‑RAG 首先在知識圖上枚舉有限長度的候選路徑，使用混合的加權 k‑shortest、beam 與受限隨機走訪策略。同時訓練一個可微分的路徑評分器、一個對比式路徑編碼器以及一個輕量驗證器，將所選路徑的潛在表示以 soft mixture 形式經由 cross‑attention 注入語言模型。  

💡 **在標準多-hop KGQA 基準上，答題正確率、證據覆蓋與端到端效率均優於圖與 LLM 基線**  
實驗顯示，該框架在常見的多跳知識圖問答基準上持續提升答案準確度、證據檢索覆蓋率以及整體推論效率，優於現有的圖基礎與純 LLM 檢索方法。  

🔍 **語意加權、驗證過濾與迭代更新的 trade‑off 提供了在有限計算與 token 預算下的部署建議**  
進一步消融分析指出，語意加權能提升路徑相關性，驗證器可濾掉噪聲路徑，而 Neural‑Socratic 圖對話循環（模型產出簡診斷訊息，對應圖編輯或種子擴展）則在模型不確定時啟動自適應檢索。這三者的平衡決定了在不同資源限制下的最佳配置。  

⚠️ **實現複雜度高、依賴自訂圖感知模組，非即插即用**  
該方法需要自行實作路徑枚舉、可微分評分器、對比編碼器以及圖對話迴圈，對於希望快速接入現有 RAG pipeline 的團隊而言，整合成本較高。  

🎯 **在 token 預算緊湊的場景下，可優先使用語意加權的最短路徑枚舉與輕量驗證器**  
若計算資源受限，建議先採用語意加權的 k‑shortest/beam 路徑生成，搭配簡單的驗證器進行過濾；在資源允許時再加入對比編碼器與迭代對話機制，以獲得更佳的準確率與證據追溯性。  

🔗 **論文連結**  📝 S-Path-RAG: Semantic-Aware Shortest-Path Retrieval Augmented Generation for Multi-Hop Knowledge Graph Question Answering  
👤 Rong Fu, Yemin Wang, Tianxiang Xu, Yongtai Liu, Weizhi Tang (University of Macau; Xiamen University; Peking University; Hanyang University; University of Liverpool; Zhejiang University)  
🔗 https://arxiv.org/abs/2603.23512  

你在處理圖檢索時，是否也曾在「找路徑」與「省 token」之間掙扎？歡迎在留言區分享你的經驗或對此方法的看法 👇  

#AI #KnowledgeGraph #RAG #MultiHopQA #SemanticRetrieval #LLM #GraphNeuralNetworks #ResearchPaper #UniversityOfMacao #PekingUniversity #ZhejiangUniversity
