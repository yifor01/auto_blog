---
title: "Errors in AI-Assisted Retrieval of Medical Literature: A Comparative Study"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2603.22344
score: 103
model: gpt-4o-free
generated_at: 2026-03-25T19:49:31.356792
---

📌 AI 輔助文獻檢索錯誤率 48%  

你以為 AI 能幫你快速找到正確論文？實際上近半數參考文獻全錯，連基本的 DOI、PubMed ID 都可能對不起來。  

🤔 **LLM 輔助檢索在醫學文獻上的可靠度有多低？**  
隨著研究人員越來越依賴 GPT、Gemini 等模型快速蒐集文獻，錯誤參考文獻的後果可能影響實驗設計與臨床決策。然而，這類錯誤在實際應用中到底有多普遍？  

🧪 **2,000 筆參考文獻 × 5 大免費版 LLM 的對照測試**  
研究團隊從《British Medical Journal》、《Journal of the American Medical Association》與《The New England Journal of Medicine》中隨機挑選 40 篇 2024 年 1 月至 2025 年 7 月發表的原創論文（每期 10 篇），共計 2,000 筆參考文獻。分別讓 Grok‑2、ChatGPT GPT‑4.1、Google Gemini Flash 2.5、Perplexity AI 與 DeepSeek GPT‑4 進行文獻檢索，並以 DOI、PubMed ID、Google‑Scholar 連結以及主題相關性四項指標組成的分數比率（score ratio）與完全失敗率（complete miss rate）作為評估標準。  

📊 **平均得分僅 0.29，近半數檢索完全失敗**  
- 五個 LLM 平台的平均 score ratio 為 0.29（標準差 0.35，範圍 0‑1.25），分數越高代表檢索越正確。  
- Grok‑2 表現最佳，score ratio 達到 0.57；Google Gemini Flash 2.5 最低，僅 0.11。  
- 完整失敗率（即四項指標皆不符合）高達 47.8%，也就是平均每兩筆參考文獻就有一筆完全錯誤。  - 同樣的 2,000 筆檢索中，《New England Journal of Medicine》的論文在 score ratio 上較《British Medical Journal》低，且完整失敗率較高，顯示期刊來源也會影響 LLM 的檢索表現。  
- 多變量迴歸分析顯示，LLM 平台與期刊分別對 score ratio 與完整失敗率具有獨立關聯。  

💡 **錯誤主要來自哪裡？**  
雖然研究未逐項分解每種錯誤類型，但分數比率的低值表明，LLM 在返回的參考文獻中經常出現 DOI 或 PubMed ID 不對應、連結導向錯誤頁面，或主題與原文不相關的情況。這意味著在依賴 AI 進行文獻蒐集時，僅看標題或摘要仍可能誤植錯誤資訊。  

⚠️ **研究限制：僅測試免費版模型、三種高影響力期刊、特定時間窗**  - 實驗僅使用了各平台的免費版本，付費或企業版的表現未被涵蓋。  
- 文獻來源限於三個頂尖醫學期刊，其他領域或期刊的表現尚未知。  
- 評估期間為 2024 年 1 月至 2025 年 7 月，隨著模型更新，後續錯誤率可能會變化。  

🎯 **實務啟示：使用 LLM 輔助文獻時必須人工複核**  
- 在寫作、寫稿或設計實驗前，務必手動檢查 AI 返回的參考文獻的 DOI、PubMed ID 是否正確，並點開連結確認內容相關性。  
- 若時間允許，可交叉使用兩個不同的 LLM 平台進行互驗，降低單一模式失誤的風險。  
- 此研究提醒我們：AI 能提升效率，但在需要精確引用的科學寫作中，仍不可完全取代傳統的文獻核對步驟。  

🔗 **論文連結**  
📝 Errors in AI-Assisted Retrieval of Medical Literature: A Comparative Study  
👤 Jenny Gao, Yongfeng Zhang, Mary L Disis, Lanjing Zhang (New York University; Rutgers University; University of Washington; Department of Pathology, Princeton Medical Center; Rutgers Cancer Institute)  
🔗 https://arxiv.org/abs/2603.22344  你在使用 AI 搜尋文獻時，有曾經發現參考文獻錯誤的經驗嗎？歡迎在留言區分享你的檢核技巧 👇  

#AI #文獻檢索 #醫學研究 #LLM #Grok #Gemini #ChatGPT #Perplexity #DeepSeek #NYU #Rutgers #科學誠實
