---
title: "RAG-Enhanced Large Language Models for Dynamic Content Expiration Prediction in Web Search"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.13052
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:34:47.289303
---

📌 **LLM 查詢感知過期預測**  

你有沒有遇過搜尋結果顯示很新，但其實內容早已過時？傳統的時間窗過濾無法因查詢而異，常導致「chronologically recent but semantically expired」的問題。Baidu 最新研究提出用 LLM 為每個查詢算出「有效期限」，把時效性轉成語意推論任務。

🤔 **傳統時間窗無法捕捉語意過期**  
在商業網頁搜尋中，資訊的生命週期高度不一樣。固定時間窗過濾會把所有內容套用同一個新鮮度標準，無法根據使用者意圖判斷什麼時候資訊在語意上已經失效。

🧪 **離線與線上 A/B 測試驗證框架**  
作者設計了一個 Query‑Aware Dynamic Content Expiration Prediction Framework：先從文件中擷取細緻的時間脈絡，再利用大型語言模型推導出查詢專屬的「validity horizon」（語意上的過期邊界）。為確保可靠性，框架內建了強力的幻覺緩解策略。該方法在離線實驗與線上真實流量的 A/B 測試中進行驗證。

📌 **LLM 推斷查詢專屬有效期限顯著提升新鮮度與體驗**  
實驗結果顯示，該框架在搜尋新鮮度與使用者體驗指標上都有可觀的提升，證明以 LLM 進行語意過期推論在工業規模的搜尋系統中是可行且有效的。

💡 **查詢感知的語意過期推論機制**  
核心思想是把「內容何時過期」視為一個依賴查詢的語意推論問題：LLM 不僅看時間戳，更會結合查詢意圖與文件內容的語義，判斷資訊在特定查詢下仍然有效的時間界限。這種動態、查詢感知的方式克服了靜態時間窗的一刀切限制。

⚠️ **公開程式碼有限，外部復現仍具挑戰**  
雖然方法在 Baidu 生產環境中驗證有效，但論文未提供完整的程式碼或開源實作，外部研究者想要完全復現仍需自行實作 LLM 推論與幻覺緩解模塊。

🎯 **結合 LLM 推論與幻覺緩解，可適用於大規模搜尋系統**  
對於搜尋引擎或其他需要時效性過濾的應用，可考慮將 LLM 作為查詢感知的過期判斷模組，並搭配適當的幻覺抑制機制，以提升結果的語意新鮮度而不犧牲系統可靠性。

🔗 **論文連結**  
📝 RAG-Enhanced Large Language Models for Dynamic Content Expiration Prediction in Web Search  
👤 Tingyu Chen, Wenkai Zhang, Li Gao, Lixin Su, Ge Chen @ Baidu Inc.  
🔗 https://arxiv.org/abs/2605.13052  

#LLM #搜尋引擎 #資訊檢索 #Baidu #AI #網頁內容過期 #動態時效性 #檢索優化
