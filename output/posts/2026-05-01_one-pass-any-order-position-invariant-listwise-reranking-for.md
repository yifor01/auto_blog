---
title: "One Pass, Any Order: Position-Invariant Listwise Reranking for LLM-Based Recommendation"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2604.27599
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-01T20:10:45.067580
---

📌 【RMIT 研究】LLM推薦重排實現排列不變性

你用 LLM 做推薦重排時，有沒有遇過同一組候選集，僅調整輸入順序就讓排名大變的狀況？
這不是模型出錯，而是 decoder-only LLM 的序列計算特性，和推薦的集合本質天生衝突。

🤔 **LLM 重排的順序敏感性，讓推薦結果不可靠**
大型語言模型（LLM）近年越來越多被用於推薦系統的重排任務，但既有的列表級預測結果會受候選項目呈現順序影響。推薦任務本質是集合導向，同一組候選集的排名應反映用戶真實偏好，但 decoder-only 架構的 LLM 是序列式計算，即便候選集完全相同，僅調整輸入順序就可能改變項目評分與最終排名。這種順序敏感性會導致排名結果反映的是 prompt 序列化邏輯，而非用戶偏好，讓 LLM 重排器的可靠性大打折扣。

🧪 **InvariRank 兩核心設計，架構級解決順序依賴**
RMIT 團隊提出 InvariRank，這是一個排列不變的列表級重排框架，直接從架構層面解決順序依賴問題，核心設計包含兩點：第一，使用結構化注意力掩碼阻斷跨候選項目的注意力交互；第二，在旋轉位置編碼（RoPE）機制下採用共享位置框架，抵消位置信息導致的評分偏差。框架結合列表級學習排序目標，
