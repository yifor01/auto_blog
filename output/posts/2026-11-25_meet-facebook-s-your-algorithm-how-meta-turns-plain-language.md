---
title: 'Meet Facebook’s Your Algorithm: How Meta Turns Plain-Language Preferences
  Into Ranking'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/24/meta-facebook-your-algorithm-llm-recommendations/
model: claude-code/sonnet
generated_at: '2026-11-25T01:45:12.985034'
score: 82
---

📌 Meta揭露Your Algorithm：LLM如何把文字偏好變成排序

TL;DR：Meta公開Your Algorithm，用LLM把文字偏好接入Feed排序系統。

Feed排序一直靠使用者的按讚、停留時間等隱性訊號堆出來，這類訊號擴展性好，卻反應慢、抓不住細膩的偏好。Meta最新公開的工程部落格，詳細拆解了Facebook在10月13日上線的「Your Algorithm」功能，讓使用者直接用白話文告訴系統自己想看什麼、不想看什麼，再由LLM把這些文字偏好轉成排序訊號。

🤔 **隱性訊號的老問題：擴展性好，但慢且粗**

根據Meta的框架，隱性互動訊號（像是按讚、停留時長）擴展性佳，但調整速度慢，也抓不住使用者偏好中的細微差異。Your Algorithm想補的正是這個缺口：讓使用者用明確陳述的偏好，直接介入排序。

🧩 **三個欄位、四段式偏好生命週期**

Your Algorithm是一個AI驅動的偏好頁面，涵蓋Facebook的Feed與Reels，介面上有三個部分：一句話的「Lately Summary」描述使用者近期觀看內容；「Interested In」清單預先帶入過去的活動紀錄；「Not Interested In」清單則用來存放排除項目。使用者可以輸入興趣、在清單間移動項目，或直接刪除，入口在貼文的三個點選單裡。

Meta把偏好從輸入到生效拆成四個環節：

1. **驗證與儲存**：通過驗證的興趣會補上embedding與搜尋關鍵字，存進Feed與Reels共用的儲存庫，另有獨立元件負責完整性與安全檢查。
2. **檢索**：每個興趣會驅動四種檢索來源，其中兩種直接比對，分別是搜尋與高度相關主題的叢集；另外兩種用來擴大觸及範圍，分別是內容關聯圖譜與項目間的相似度比對。
3. **相關性過濾**：系統比較興趣的語意與每個候選內容，通過的候選內容才能進入後段排序並獲得排序加權。
4. **重排序控制層**：Meta稱這是「每個階段都做分層過濾」，先用embedding比對移除高度相似的重複內容，再用降權規則把近似內容往後排，最後由一個微調過的LLM reranker檢視最終清單。

針對「少一點AI生成內容」或「少一點性暗示內容」這類品質類請求，系統走的是不同路徑，直接對應到專用的降權訊號，而不是主題比對；若使用者指名某位創作者，系統則直接過濾該創作者的內容。在使用端，當使用者新增一個排除項目，client端會先做快取失效，把佇列中符合新排除條件的內容在顯示前先剔除。

💡 **小模型剃刀：reranker只輸出「要刪掉什麼」**

技術上值得注意的一點是，這個微調過的reranker被訓練成只回傳「該移除的項目清單」，而不是逐一替每個候選內容打分。Meta表示，這個小型微調模型的表現勝過逐項評分的通用模型，速度更快也更可靠，原因很直接：輸出一份短短的移除清單，遠比替每個候選內容評分來得便宜。另外，當使用者新增一個興趣，系統會觸發一次正常週期之外的「補充性尾端抓取」（supplementary tail load），但Meta沒有公開這個額外抓取動作的延遲數字。

⚠️ **一個尚待釐清的小矛盾**

原文也提到一處來源衝突：YouTube的說明中心指出同一時間只能啟用一個自訂Feed，而TechCrunch的報導則稱10月起已有多個Feed陸續上線。這兩個說法之間的落差，原文並未進一步解釋，讀者宜留意這屬於第三方報導間的不一致，而非Meta官方的正式說明。

🎯 **實務啟示**

對正在把LLM塞進生產排序系統的工程團隊來說，這篇文章最有參考價值的地方，是它示範了「顯性偏好」如何疊加在既有的隱性訊號排序棧上，而不是整個推翻重做：驗證、檢索、相關性過濾、重排序分成四個獨立環節，各自可以單獨最佳化。reranker只輸出刪除清單而非逐項評分的設計，也是一個值得借鏡的成本最佳化思路，當任務本質是「篩掉不要的」而非「排序全部」時，讓模型只回答前者可以省下大量推論成本。

🔗 **來源**
- 標題：Meet Facebook's Your Algorithm: How Meta Turns Plain-Language Preferences Into Ranking
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/24/meta-facebook-your-algorithm-llm-recommendations/

#Meta #Facebook #RecommenderSystems #LLM #Ranking #Personalization #MachineLearning #AIEngineering #RecSys #ProductAI
