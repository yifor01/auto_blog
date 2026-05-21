---
title: "Beyond Text-to-SQL: An Agentic LLM System for Governed Enterprise Analytics APIs"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.21027
score: 99
model: tencent/hy3-preview:free
generated_at: 2026-05-21T21:01:32.588294
---

📌 【Dialpad 最新研究】Beyond Text-to-SQL：Agentic LLM 打造受管控的企業分析 API  

你以為只要讓 LLM 直接產出 SQL，就能讓每位員工輕鬆取得數據嗎？在真實的企業環境裡，隨意呼叫資料庫可能違反資料管控、審計與安全政策，反而帶來合規風險。  

🤔 **企業分析需求亟需兼顧易用與管控**  
傳統 BI 工具或純 Text-to-SQL 方案雖能提供自然語言介面，但卻無法確保每一次查詢都經過既定的業務邏輯與權限管控。當數據存取必須透過已治理的 API 時，把數學或彙總計算交給 LLM 會帶來不可預測的誤差與合規問題。  

🧪 **基於 90 真實企業使用案例的評估設計**  
研究團隊針對由領域專家構建的 90 個實際企業分析場景進行測試。這些場景涵蓋不同的業務意圖、權限需求與視覺化需求，目的是檢驗系統是否能正確理解使用者目標、驗證權限、執行受管控的查詢，並產出符合規範的圖表。  

🔍 **Analytic Agent 能透過多步驟推理與政策感知 orchestration 將自然語意轉為安全 API 呼叫**  
提出的 Analytic Agent 是一個以 LLM 為核心的代理系統。它不直接產生 SQL，而是先解讀使用者的自然語意，然後依照預先定義的政策（權限、審計、安全規則）決定哪些受管控的 API 該被呼叫、何時進行彙總或過濾，最後依 API 回覆生成符合規範的視覺化輸出。整個過程依賴多步驟推理，確保每一步都受到政策的約束。  

💡 **關鍵在於不把數學邏輯交給 LLM，而是交給已管控的 API**  
與傳統 Text-to-SQL 不同，Analytic Agent 將所有涉及業務規則、彙總或變換的邏輯留存在企業已治理的 API 內部。LLM 只負責意圖理解與政策感知的決策，從而在保持自然語言便利性的同時，降低了因模型幻想或計算錯誤導致的合規風險。  

⚠️ **未公開原始碼與實作細節限制即時落地**  
雖然概念與實驗結果顯示潛力，但論文未提供開源實作或詳細的系統架構。這意味著想要立刻在自家環境中試用的團隊仍需自行實作或等待後續公開資源，限制了概念的快速驗證與擴散。  

🎯 **建議先評估現有 API 政策，再考慮 LLM 代理層的引入**  
對於希望透過 LLM 降低數據使用門檻的企業，首步應該審視現有的 analytics API 是否已經完整封裝了業務邏輯與權限控制。在此基礎上，可以嘗試引入類似 Analytic Agent 的政策感知代理層，以自然語言方式呼叫既治理的服務，同時保持審計與安全不受影響。  

🔗 **論文連結**  
📝 Beyond Text-to-SQL: An Agentic LLM System for Governed Enterprise Analytics APIs  
👤 Gundeep Singh, Parsa Kavehzadeh, Jing Xia, Xue-Yong Fu, Julien Bouvier Tremblay @ Dialpad Inc.  
🔗 論文：https://arxiv.org/abs/2605.21027  

你的企業目前是否已經將關鍵數據流程封裝在受管控的 API 中？歡迎在留言區分享你的看法與經驗 👇  

#AI #LLM #AgenticAI #DataGovernance #EnterpriseAnalytics #Dialpad #TextToSQL #APISecurity #機器學習 #科技趨勢
