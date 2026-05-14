---
title: "LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.13137
score: 110
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:38:52.407461
---

📌 【LeanSearch v2】兩階段檢索提升 Lean 4 定理證明  

你以現有的程式輔助工具，能否一次找出證明一個定理所需的所有補充定理？實際上，現有工具往往只能匹配零散的單一宣告，難以覆蓋完整的前提集合。  

🤔 **定理證明的瓶頸在於「全域前提」的缺失**  

在 Lean 4 中，證明一個定理通常需要從函式庫中撿選零散的多個引理，這些引理的聯合使用才能形成簡潔的證明。現有的語義搜尋引擎或逐步前提選擇系統，只能處理單一查詢或單步驟的預測，無法一次性恢復整個定理所需的完整前提集。  

🧪 **標準模式與推理模式的兩階段檢索架構**  

LeanSearch v2 包含兩種模式：  
- **標準模式**：利用階層資訊非正式化的 Mathlib 語料，搭配 embedding‑reranker 管線，在無需領域特定微調的情況下達成單一查詢檢索的 state‑of‑the‑art（nDCG@10 為 0.62，次佳系統為 0.53）。  
- **推理模式**：以標準模式作為檢索基底，透過迭代的「草圖‑檢索‑反思」循環，針對全域前提擷取進行多輪優化。  

📊 **標準模式 nDCG@10 達 0.62，推理模式在 69 個研究級定理上找回 46.1% 前提群**  

在包含 69 個研究級 Mathlib 定理的基準測試中：  
- 推理模式在前 10 個候選項中恢復了 46.1% 的事實前提群組，顯著優於強度相近的推理檢索系統（38.0%）與前提選擇基線（9.3%）。  
- 標準模式的單一查詢檢索表現亦優於現有最佳方案。  

💡 **迭代草圖‑檢索‑反思循環讓檢索從單一查詢擴展為全域前提**  

推理模式的核心在於：先根據當前證明草圖生成查詢，檢索相關引理，然後根據檢索結果反思並修正草圖，重複此過程。這種循環使系統能逐步補充缺失的前提，最終在有限的候選數內覆蓋較完整的前提集合。  

⚠️ **僅在 Mathlib 上評估，長期穩定性與其他形式系統尚未驗證**  

實驗僅基於 Mathlib 函式庫與 69 個研究級定理進行，未涉及其他形式語言或長期使用情境的測試，因此對於更廣泛的適用性仍需進一步驗證。  

🎯 **開放原始碼與公開 API 讓形式驗證研究者直接 plug‑in 提升證明成功率**  

作者已將所有程式碼、資料與基準開源，並提供公開 API（https://leansearch.net/）。在固定證明迴路的下游評估中，使用 LeanSearch v2 取代其他檢索器可將證明成功率提升至 20%（次佳系統為 16%，無檢索則為 4%），證明檢索品質的提升能直接傳遞至證明生成。  

🔗 **論文連結**  
📝 LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving  
👤 Guoxiong Gao, Zeming Sun, Jiedong Jiang, Yutong Wang, Jingda Xu (Peking University; IQuest Research; Kyoto University; Westlake University; Great Bay University; Zhongguancun Academy)  
🔗 https://arxiv.org/abs/2605.13137  
💻 程式碼與資料：https://github.com/frenzymath/LeanSearch-v2  
🌐 公共 API：https://leansearch.net/  

你有使用過 Lean 或其他形式驗證工具嗎？歡迎在留言區分享你的經驗與對檢索輔助的看法 👇  

#Lean4 #TheoremProving #InformationRetrieval #FormalMethods #AI4Math #OpenSource #PekingU #IQuest #KyotoU #WestlakeU #GreatBayU #GuoxiongGao
