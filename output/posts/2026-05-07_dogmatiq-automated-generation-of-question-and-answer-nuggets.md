---
title: "DoGMaTiQ: Automated Generation of Question-and-Answer Nuggets for Report Evaluation"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.04458
score: 98
model: tencent/hy3-preview:free
generated_at: 2026-05-07T20:47:06.885612
---

📌 【多校聯手+Google】自動產生問答式金粒，讓長報告評估不再靠人工標註  

隨著檢索增強生成（RAG）系統廣泛使用，評估長篇、帶引用的報告變成迫切需求。傳統做法必須人工編製「金粒」（nuggets）來衡量報告是否涵蓋查詢相關資訊，這個過程耗時且難以擴展，特別是跨語言場景。  

🤔 **人工金粒產成評估的瓶頸**  

現有評估框架依賴人類針對每個主題手動挑選問答對，這不僅費力，也限制了新興資訊需求的快速評估。當來源文件為多語言時，問題更為顯著。  

🧪 **三階段自動化管線：文件依託生成→改寫聚類→品質篩選**  

DoGMaTiQ 由三個步驟組成：  
1. **文件依託金粒生成** – 利用 LLM 在來源文件基礎上產出初步問答對。  
2. **改寫聚類** – 把語意相近的問答對群組，減少冗餘。  
3. **品質子選擇** – 基於設計好的準則（例如答案的可識別性與問題的覆蓋度）挑選最終金粒集合。  

此管線產出的金粒接續近期的 AutoArgue 框架，使得報告評估能完全自動化。  

📊 **在 NeuCLIR 與 RAGTIME 兩項跨語言 TREC 任務上，與人工判斷具強烈排名相關**  

實驗顯示，使用 DoGMaTiQ 產出的金粒進行自動評估，所得到的系統排序與：  
- 人類在迴圈中的判斷（human‑in‑the‑loop）  
- 完全人工標註的金粒判斷  
之間具有顯著的排名相關性。此外，分析指出：  
- 強大的 LLM 金粒產生器是管線表現的關鍵因子。  
- 所得的系統排名對異常系統具備穩定性（robust to outlier systems）。  

🔍 **品質篩選的設計決定最終金粒的實用性**  

管線的第三階段不只是簡單過濾；它根據「問題能否獨立表達資訊需求」以及「答案集合是否足以驗證問題」等原則來選金粒。這使得最終金粒集既保持細粒度（問題與答案分離），又避免因過度聚類而遺失重要變體。  

⚠️ **依賴強大 LLM、實驗限於兩項共享任務**  

- 金粒品質高度依賴底層 LLM 的生成能力；較弱的模型可能導致召回率下降。  
- 實驗僅在 NeuCLIR 與 RAGTIME 兩個跨語言 TREC 集合上進行，其他領域或單語言場景的表現尚需進一步驗證。  
- 目前未報告人工標註金粒的具體數量或標註成本，因此無法量化自動化帶來的省力比例。  

🎯 **研究者與工程師可直接採用的開源工具**  

- 完整程式碼與實驗遺物已於 GitHub 公開：https://github.com/manestay/dogmatiq  
- 將 DoGMaTiQ 金粒 plug into AutoArgue 或其他基於金粒的評估框架，即可獲得無需人工標註的自動評估分數。  
- 對於正在建置跨語言 RAG 長文生成系統的團隊，這提供了一種可擴展、與人類判斷一致的評估基線。  

🔗 **論文連結**  
📝 DoGMaTiQ: Automated Generation of Question-and-Answer Nuggets for Report Evaluation  
👤 Bryan Li, William Walden, Yu Hou, Gabrielle Kaili-May Liu, Dawn Lawrie  
🏫 University of Pennsylvania; Johns Hopkins University; University of Maryland; Yale University; University of New Hampshire; Google Inc.  
🔗 https://arxiv.org/abs/2605.04458  

你是否也在為長報告評估而手動標註金粒感到頭痛？DoGMaTiQ 的自動化管線或許能省下大量人力，同時保持與人工判斷的一致性。歡迎在留言區分享你的看法或使用經驗！  

#InformationRetrieval #RAG #ReportEvaluation #DoGMaTiQ #TREC #Nuggets #LLM #OpenSource #UPenn #JHU #UMD #Yale #UNH #GoogleAI
