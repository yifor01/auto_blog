---
title: "Paraphrase-Induced Output-Mode Collapse: When LLMs Break Character Under Semantically Equivalent Inputs"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.04665
score: 110
model: tencent/hy3-preview:free
generated_at: 2026-05-07T20:27:15.718532
---

📌 【Peking University & University of Chicago】LLM 在同義改寫下失格  

你以為只要語義不變，AI 的回答就會穩定嗎？實際上，即使溫度設為零，同義改寫的提示也能讓模型從簡單標籤突然變成冗長對話，導致評估系統誤判。  

🤔 **當語義保持不變，輸出格式卻可能崩解**  
傳統的 prompt‑robustness 研究多聚焦於答案是否正確，卻鮮少檢查模型是否仍維持原本要求的輸出形式（例如單一標籤或選項 token）。當這種形式被破壞時，即使答案內容正確，評估管線也會因無法精準匹配而判定失敗。  

🧪 **PARACONSIST 基準與多維度評分**  
研究團隊構建了 PARACONSIST 基準：150 個基礎查詢，每個查詢配五種詞彙、句法與語義擴充的變體，共 900 個 prompt。他們在五個 2025 年時代的緊湊 LLMs 與四種任務類型上進行 150 查詢的評估，並提出 Semantic Consistency Score，將 prompt‑variant 魯棒性分解為答案一致性、Sentence‑BERT 語義相似度與長度穩定度三個維度。  

📊 **只有約 22% 的回覆保持正確標籤，約 78% 完全偏離答案空間**  
在全詞匹配的評估下，僅有 ~22% 的閉形式變體回覆仍將事實標籤嵌入輸出；其餘 ~78% 的回覆完全跳出預期的答案空間，轉而產出冗長的對話式文字。這種失誤在不同模型間並不均一，主要由任務結構驅動；模型間的差異則由答案一致性與長度穩定度共同決定。  

💡 **輸出模式的穩定性應成為可靠性評估的第一指標**  
結果顯示，僅關注答案正確性不足以捕捉此類失效。工程師在審核 prompt 魯棒性時，應將「回覆模式是否保持」列為與答案準確性同等重要的目標，並可直接使用 PARACONSIST 基準與 Semantic Consistency Score 進行診斷與改進。  

⚠️ **研究限制**  
評估僅涵蓋五個緊湊的 2025‑era LLMs 與四種任務類型；未探討更大規模模型或開放式生成場景。因此，所觀察到的 output‑mode collapse 是否在更廣泛的設定下仍然顯著，尚需後續工作驗證。  

🔗 **論文連結**  
📝 Paraphrase-Induced Output-Mode Collapse: When LLMs Break Character Under Semantically Equivalent Inputs  
👤 Aofan Liu, Jingxiang Meng (Peking University; University of Chicago)  
🔗 https://arxiv.org/abs/2605.04665  

你在使用 AI 時，是否曾注意到同樣問題的不同說法會導致答案格式大幅變化？歡迎在留言區分享你的經驗與觀察 👇  

#AI #LLM #PromptRobustness #PARACONSIST #PekingUniversity #UniversityofChicago #機器學習 #自然語言處理
