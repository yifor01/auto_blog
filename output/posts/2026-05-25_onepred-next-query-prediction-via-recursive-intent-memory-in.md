---
title: "OnePred: Next-Query Prediction via Recursive Intent Memory in Multi-Turn Conversations"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.23668
score: 111
model: tencent/hy3-preview:free
generated_at: 2026-05-25T20:50:31.049152
---

📌 **【清華大學 & 阿里巴巴 Qwen】OnePred：用「遞歸意圖記憶」實現多輪對話下一查詢預測**  

你有沒有想過，AI 能否在你還沒打完下一句話時就知道你要問什麼？讓對話系統從「被動回覆」變成「主動預測」是提升使用體驗的關鍵一步。  

🤔 **多輪對話的效率‑品質兩難**  
現有大型語言模型在處理多輪對話時，要麼把完整歷史全部塞進模型（token 成本隨對話長度線性增長），要麼只保留最近幾輪（卻可能丟失關鍵的跨輪意圖）。這種兩難使得「下一查詢預測」（Next‑Query Prediction）在實務上難以同時達成高品質與低成本。  

🧪 **OnePred：遞歸意圖記憶 + 兩階段強化學習**  
論文提出 OnePred，其核心是一個**遞歸更新的意圖記憶體**（recursive intent memory），僅維護一個摘要狀態，作為所有跨輪上下文的唯一來源。這樣，每輪的 token 消耗與對話長度無關。  
訓練採用兩階段強化學習管線：  
1. 首先教模型「要預測什麼」（預測目標）；  
2. 再教模型「要壓縮什麼」（如何把歷史資訊編輯成利於預測的意圖鏈）。  
為了嚴格評估，作者構建了 **NQP‑Bench**，涵蓋三個多樣化子集，並開放原始碼（https://github.com/ZBWpro/OnePred）。  

📈 **核心發現：長對話中 token 省逾 20 倍，品質更勝基線**  
- 與直接輸入完整歷史相比，OnePred 能將 **單輪 token 消耗降低最高 22×**。  
- 在所有基線模型上，**預測品質持續優越**，且在對話長度越長時優勢越顯著。  
- 這些結果表明，透過追蹤使用者隨話題演變、未滿足需求與興趣轉移的「意圖軌跡」，可以在不犧牲品質的前提下大幅節省計算資源。  

💡 **深入分析：意圖鏈取代原始歷史**  
OnePred 的記憶體並不是簡單的歷史截斷，而是透過遞歸更新捕捉使用者意圖的演變軌跡。兩階段 RL 使得這條記憶被塑造成「預測導向」的意圖鏈——即記憶中的每個更新都被引導向提升下一查詢預測的準確度。這種設計讓模型能在固定成本下保持對長距離依賴的敏感度。  

⚠️ **目前僅在 NQP‑Bench 上驗證，實際場景表現尚待觀察**  
實驗僅在作者自行提出的基準測試上進行，模型在真實產品環境中的延遲、穩定性與泛化能力仍需進一步驗證。  

🎯 **給工程師的啟示：建構主動式對話代理的可行路徑**  
- 若你正在開發需要低延遲、高互動性的對話系統（如客服、個人助理），OnePred 提供了一種「不隨對話長度增長」的上下文壓縮方案。  
- 開放原始碼與基準測試讓你能直接在自己的管線上複現或改進。  
- 未來可考慮將此意圖記憶體與其他主動策略（如建議生成、任務規劃）結合，進一步提升使用者體驗。  

🔗 **論文連結**  
📝 OnePred: Next-Query Prediction via Recursive Intent Memory in Multi-Turn Conversations  
👤 Jiangwang Chen, Bowen Zhang, Zixin Song, Jiazheng Kang, Xiao Yang @ Tsinghua University; Qwen Applications Business Group of Alibaba  
🔗 https://arxiv.org/abs/2605.23668  
💻 程式碼：https://github.com/ZBWpro/OnePred  

你認為這種「預測下一查詢」的技術會在哪些場景帶來最大改變？歡迎在留言區分享你的想法 👇  

#AI #對話系統 #NextQueryPrediction #OnePred #Tsinghua #Alibaba #NLP #強化學習 #開源代碼 #機器學習 #Chatbot #主動式AI
