---
title: "Memory-Efficient Looped Transformer: Decoupling Compute from Memory in Looped Language Models"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.07721
score: 101
model: tencent/hy3-preview:free
generated_at: 2026-05-11T20:43:13.530305
---

📌 【Qualcomm AI Research】Memory-Efficient Looped Transformer：解耦計算與記憶體  

你以為讓 AI 多思考幾輪就一定會爆掉記憶體？其實可以「共用」快取，讓推理深度不再耗費線性記憶體。  

🤔 **當迴圈語言模型遇上記憶體瓶頸**  
Ouro 等 looped Transformer 透過在每次迴圈中保留標準 Key‑Value (KV) cache，使記憶體消耗隨推理深度線性增長。這意味著若想讓模型進行更多步驟的推理，所需顯存會快速變得無法承受，限制了類似 Agent 的長 horizon 推理在實際部署中的可行性。  

🧪 **單層共享 KV 快取＋可學習閘門**  
本文提出的 Memory-Efficient Looped Transformer (MELT) 不再為每層、每個迴圈維護獨立的 KV cache，而是每層只保留 **一個** KV cache，該 cache 在所有迴圈間共享。cache 的更新透過一個可學習的 gating mechanism 進行，使得記憶體佔用隨迴圈次數保持 **常數**。為了在這樣的架構下進行穩定訓練，作者採用兩階段的 chunk‑wise 訓練：先做 interpolated transition，再進行 attention‑aligned distillation，將預訓練的 Ouro 模型轉換為 MELT。  

🔥 **在不犧牲效能的前提下達到常數記憶體**  
實驗顯示，從預訓練 Ouro 參數 fine‑tune 得到的 MELT 模型，在各項基準上 **優於** 同等規模的標準 LLM，同時其記憶體足跡與普通 LLM 相近，並 **遠小於** 原始 Ouro 的消耗。這意味著 MELT 能在不增加額外顯存的情況下，保持 looped 模型的推理能力，實現「constant‑memory iterative reasoning」。  

💡 **關鍵在於「共用」而非「複製」**  
MELT 的核心創新在於將 KV cache 從「每層‑每迴圈」的複製模式，轉為「每層‑共享」的設計，並透過可學習的閘門控制資訊的流入與流出。這樣的結構讓模型在進行多步推理時，不需要不斷新增額外的快取空間，因而解決了先前 looped 架構的記憶體瓶頸。  

⚠️ **僅針對 Ouro 起點模型的後續訓練，長期穩定性尚待觀察**  
研究僅在以 Ouro 為起點的模型上進行了兩階段的 chunk‑wise 訓練，未探索從隨機初始化或其他架構直接訓練 MELT 的可行性。此外，實驗主要聚焦於標準語言基準，長 horizon 推理或多模態 Agent 場景的實際表現仍需後續工作驗證。  

🎯 **對工程師的直接啟發：可作為輕量級後訓練步驟**  
- 若你手頭已有 Ouro 系列的預訓練 checkpoint，僅需進行本文提出的兩階段 chunk‑wise 訓練，即可獲得顯著降低記憶體佔用的版本。  
- 此方法不改變模型的參數規模，因此在推理時不需要額外的硬體支援，適合希望在現有設備上提升多步推理能力的場景。  
- 對於希望在資源受限環境部署長 horizon 推理或 Agent 系統的團隊，MELT 提供了一種「不增額外顯存」即可提升推理深度的可行路徑。  

🔗 **論文連結**  
📝 Memory-Efficient Looped Transformer: Decoupling Compute from Memory in Looped Language Models  
👤 Victor Conchello Vendrell, Arnau Padres Masdemont, Niccolò Grillo, Jordi Ros-Giralt, Arash Behboodi (Qualcomm AI Research)  
🔗 https://arxiv.org/abs/2605.07721  

你目前的 looped LLM 是否正為記憶體增長而頭痛？試著看看這種「共用快取」的思路是否能給你的專案帶來新突破！歡迎在留言區分享你的經驗或疑問 👇  

#AI #LLM #Transformer #MemoryEfficient #Qualcomm #Research #機器學習 #深度學習 #Agent #推理 #技術分享
