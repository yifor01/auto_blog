---
title: "DeepWeb-Bench: A Deep Research Benchmark Demanding Massive Cross-Source Evidence and Long-Horizon Derivation"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.21482
score: 122
model: tencent/hy3-preview:free
generated_at: 2026-05-21T20:32:24.396793
---

📌 **DeepWeb‑Bench：深度研究新基準**  

現有的深度研究基準已被頂尖模型拿到近乎滿分，卻很難真正區分它們的實際能力。  
當模型能在秒內找到資料時，錯誤究竟來自哪裡？這正是我們想釐清的問題。  

🤔 **即使檢索快速，錯誤仍主要出現在推理與校準上**  
我們設計了 DeepWeb‑Bench，讓每個任務都需要大規模證據蒐集、跨來源對齊以及長距離多步推導。在九種前景模型上的評測顯示，僅 12‑14% 的錯誤來自檢索失敗，而推導與校準失敗則佔了超過 70%。這意味著，提升檢索速度並不是突破瓶頸的關鍵。  

🧪 **以證據蒐集、跨來源對齊與長程推導為核心的任務設計**  
基準將任務難度分為四個能力家族：Retrieval（檢索）、Derivation（推導）、Reasoning（推理）與 Calibration（校準）。每個參考答案都附帶來源溯源紀錄，分為四個披露層級，並在此有的情況下進行交叉來源檢核，方便審計模型的答案是否真的建立在證據之上。  

🔍 **強弱模式的錯誤類型截然不同**  
進一步分析發現，強模式的錯誤主要是「推導不完整」——即能找到資料但在多步推導中斷鏈；弱模式則以「 hallucinated precision 」為主，也就是在缺乏足夠證據時仍給出過於確定的答案。這兩種失誤機制完全不同，說明模型在能力提升上的路徑並不單一。  

💡 **模型在不同領域上呈現真正的專長，互相間的共識度僅為 0.61**  
跨模型的平均相關係數 (rho) 只有 0.61，且在單個案例上，模型間的分數差異最高可達 18.8 個百分點。這表示即使是前景模型，也在特定領域上有明顯的強弱分化，單一基準無法全面反映其表現。  

⚠️ **基準規模仍屬探索階段，長期效能觀測尚未進行**  
目前的公開版本提供了資料、評分規則與評估程式碼，但僅涵蓋了現有的任務集合，尚未針對長 horizon（例如數週或數月的研究流程）做延伸測試，亦未探討不同網路來源的偏差對最終答案的系統性影響。  

🎯 **評估時應關注推導與校準，而不只是檢索速度**  
- 在模型迭代過程中，加入明確的推導完整度檢查與校準不確定度報告，能更直接針對主要錯誤來源。  
- 針對不同領域建立子基準或領域特化的評估，可更清楚看出模型的專長與不足。  
- 開發團隊可參考公開的評分規則與程式碼，快速在自有模型上進行同類測試。  

🔗 **論文連結**  
📝 DeepWeb‑Bench: A Deep Research Benchmark Demanding Massive Cross‑Source Evidence and Long‑Horizon Derivation  
👤 Sixiong Xie, Zhuofan Shi, Haiyang Shen, Jiuzheng Wang, Siqi Zhong @ Peking University  
🔗 https://arxiv.org/abs/2605.21482  

你在使用 AI 進行深度研究時，是否更常卡在「找不到資料」還是「推導斷鏈／過度確定」？歡迎在留言區分享你的經驗 👇  

#AI #DeepResearch #Benchmark #LanguageModel #PekingU #LLM評估 #機器學習 #科技趨勢
