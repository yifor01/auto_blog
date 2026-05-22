---
title: "Spreadsheet-RL: Advancing Large Language Model Agents on Realistic Spreadsheet Tasks via Reinforcement Learning"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.22642
score: 111
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:32:54.586121
---

📌 Spreadsheet‑RL：以強化學習提升 LLM 在真實試算表任務上的表現  

你以為只要用 Prompt 就能讓 AI 輕鬆操作 Excel？實際上，單靠通用大型語言模型的提示在複雜、多步驟的試算表工作流中仍屢屢失誤。  

🤔 **試算表自動化的瓶頂在於缺乏真實環境的訓練**  
現有的試算表代理大多依賴通用 LLM 的專門提示，雖能處理簡單操作，但在財務、供應鏈等領域的多步驟工作流上表現不足。這限制了 AI 在日常資料密集型工作中的實用價值。  

🧪 **Spreadsheet‑RL 框架與自訂 Spreadsheet Gym**  
我們提出一個以強化學習微調的訓練框架 Spreadsheet‑RL，搭配一個設計用於多回合 RL 的 Spreadsheet Gym 環境。該環境透過 Python 沙箱暴露完整的 Excel 功能，並配備精心設計的工具集與工具路由規則，以模擬真實試算表操作。同時，我們建立了一個自動化管線，從線上論壇收集配對的起始‑目標試算表，並根據財務與供應鏈領域編譯出新的 Domain‑Spreadsheet 基準測試集。  

📊 **強化學習顯著提升代理成功率**  
在實驗中，使用 Qwen3‑4B‑Thinking‑2507 作為基礎模型：  
- 在通用 SpreadsheetBench 上，Pass@1 從 12.0% 提升至 23.4%  
- 在我們 curation 的 Domain‑Spreadsheet 資料集上，Pass@1 從 8.4% 提升至 17.2%  
這些結果表明，透過 RL 在真實試算表環境中訓練的專門代理能在一般與領域特定任務上都獲得顯著改善。  

💡 **關鍵在於環境的真實感與獎勵設計**  
性能提升的主要動力來自於 Spreadsheet Gym 提供的完整 Excel 操作空間以及經過細部調整的獎勵機制，使代理學會在多步驟流程中進行長期規劃與錯誤修正，而非僅依賴單次提示的短期映射。  

⚠️ **實驗主要聚焦於特定模型與基準，泛化需進一步驗證**  
目前結果基於 Qwen3‑4B‑Thinking‑2507 在兩個基準測試上的表現；不同模型規模、其他試算表軟體（如 Google Sheets）以及更長時程的任務表現尚未探索。  

🎯 **實務上可先嘗試在受控環境中使用 RL 微調**  
對於希望在內部流程中引入試算表自動化的團隊，可考慮：  
1. 建立或利用類似 Spreadsheet Gym 的沙箱環境  
2. 從真實工作紀錄中收集起始‑目標試算表對  
3. 以強化學習微調開源 LLM，而非僅依賴提示工程  
這樣的做法有望將 AI 從「快速產出」提升至「可靠執行」的層級。  

🔗 **論文連結**  
📝 Spreadsheet-RL: Advancing Large Language Model Agents on Realistic Spreadsheet Tasks via Reinforcement Learning  
👤 Banghao Chi, Yining Xie, Mingyuan Wu, Jingcheng Yang, Jize Jiang (University of Illinois Urbana-Champaign; Meta)  
🔗 https://arxiv.org/abs/2605.22642  

你的團隊是否已在試算表上嘗試過強化學習？歡迎留言分享經驗或疑問 👇  

#AI #ReinforcementLearning #Spreadsheet #LLM Agents #Excel #Automation #UIUC #Meta #MachineLearning #DataWorkflow
