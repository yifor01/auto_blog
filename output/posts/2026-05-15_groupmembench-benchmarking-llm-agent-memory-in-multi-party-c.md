---
title: "GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.14498
score: 121
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:14:45.000090
---

📌 【UCSB & Microsoft】GroupMemBench：多人對話記憶基準測試  
🔗 https://arxiv.org/abs/2605.14498  

你以為 LLM 記憶只需記住單人對話？在真實的群組聊天中，它的表現竟然崩壞到只剩 46% 正確率——連簡單的 BM25 基準都能追上或超過大多數記憶系統。  

🤔 **群組記憶的三個盲點尚未被衡量**  
現有記憶基準大多圍繞單人（dyadic）對話設計，卻忽略了真實部署中常見的多人互動：群組動態不只是單聊的簡單疊加、每位使用者的信念需要獨立追蹤（speaker‑grounded belief tracking），以及根據對象調整用詞的 Theory‑of‑Mind 效應（audience‑adapted language）。這三項特性正是 GroupMemBench 想要捕捉的核心。  

🧪 **圖基合成 + 對抗式查詢產出可控的多人場景**  
研究團隊先以圖為基礎的合成管線生成多方對話，可控回覆結構，並根據每個使用者的人設與目標受眾來條件每條訊息。接著，對抗式查詢管線將每個問題綁定至特定提問者，橫跨六類：多跳推理、知識更新、術語歧義、使用者隱含推理、時間推理與棄答（abstention），並反覆搜尋具挑戰性且真實的查詢，以全面檢測記憶能力。  

📉 **領先記憶系統在 GroupMemBench 上平均僅 46%**  
最強的記憶方法平均正確率為 46.0%；其中知識更新僅 27.1%、術語歧義 37.7%。相比之下，簡單的 BM25 基準在多個指標上不只匹配，甚至超過大多數 agente 記憶系統。這意味著現有的記憶擷取過程抹掉了多人對話所需的結構與詞彙特徵，導致群組記憶遠未解決。  

💡 **記憶系統需要「群組感知」而非只是「單人累加」**  
結果顯示，現有記憶架構在處理群組特有的依賴關係時失效，因為它們將多方對話視為獨立單人對話的拼貼。要提升表現，必須在記憶擷取階段保留對話圖結構、使用者個別狀態以及語用層面的受眾適應，否則只會在單人基準上看似良好，實際部署時卻會崩潰。  

⚠️ **基準仍屬首次嘗試，需注意以下限制**  
- 合成對話雖可控，但未覆盖所有真實群組的語言變體。  
- 評估集中在六類查詢，其他潛在記憶需求（例如跨模態或長期依賴）尚未涉及。  
- 基準規模與多樣性尚待擴充，以確保結果的普遍性。  

🎯 **未來記憶研究應朝群組感知方向發展**  
- 設計能明確建模使用者個別狀態與群組圖結構的記憶模組。  
- 在訓練或檢索階段加入受眾意識（audience‑aware）的詞彙選擇機制。  
- 利用類似 GroupMemBench 的基準持續檢驗新方法在真實多人協作場景中的表現。  

🔗 **論文連結**  
📝 GroupMemBench: Benchmarking LLM Agent Memory in Multi‑Party Conversations  
👤 Jingbo Yang, Kwei‑Herng Lai, Xiaowen Wang, Shiyu Chang, Yaar Harari (UC Santa Barbara; Microsoft)  
🔗 https://arxiv.org/abs/2605.14498  

你在開發或使用 LLM 代理時，是否曾在群組聊天中感到它「忘記」了關鍵資訊？歡迎在留言區分享你的觀察與經驗 👇  

#LLM #記憶系統 #多方對話 #AI基準測試 #UCSB #Microsoft #GroupMemBench #NLP #AgenticAI
