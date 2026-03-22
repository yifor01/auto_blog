---
title: "AdaMem: Adaptive User-Centric Memory for Long-Horizon Dialogue Agents"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2603.16496
score: 121
model: gpt-4o-free
generated_at: 2026-03-18T20:54:30.419593
---

📌 **AdaMem：適應性記憶提升長對話 Agent**  

長對話中，AI 總是忘記早前說過的事？傳統記憶依賴語義相似度，卻常漏掉關鍵線索。AdaMem 如何用多層記憶圖解這個問題？  

🤔 **記憶系統的三個核心瓶頸**  
現有記憶機制常過度依賴語義相似度，導致重要證據被遺漏；相關經驗被零散存放，削弱時間與因果連貫性；記憶粒度固定，無法依問題需求彈性調整。這三點限制了長對話 Agent 在個人化協助與多步推理上的表現。  

🧪 **AdaMem 的四層結構與動態檢索流程**  
AdaMem 將對話歷史組織為工作記憶、情境記憶、人格記憶與圖譜記憶四個層次，分別保存近期脈絡、結構化長期經驗、穩定使用者特徵以及關係感知的連結。在推理時，系統先確定目標參與者，然後根據問題構建條件化檢索路徑：先進行語義檢索，僅在需要時啟動關係感知的圖譜擴展；最後透過角色專門管道進行證據綜合與回覆生成。  

🔬 **在長對話基準測試上的表現**  
研究團隊在 LoCoMo 與 PERSONAMEM 兩個長對話推理與使用者建模基準上進行評估。實驗結果顯示，AdaMem 在兩個基準上均達到最先進（SOTA）表現，證明其在保存時間因果資訊與使用者個人特徵方面的有效性。  

💡 **關鍵洞察：適應性與使用者中心的設計**  AdaMem 的創新在於：  
- 多層記憶分工，使近期與長期資訊各有專門存放空間；  
- 檢索路徑依問題動態決定是否啟動圖譜擴展，避免不必要的噪聲；  
- 角色專門管道將證據綜合與語言生成分離，提升回覆的相關性與一致性。  
這種設計直接回應了既有系統在語義過度依賴、經驗零散與粒度固定上的不足。  

⚠️ **研究限制**  
- 目前僅在兩個公開基準上驗證，真實世界長對話應用尚需進一步測試；  
- 論文未詳細說明記憶更新頻率與資源消耗的實測數據；  
- 開源程式碼將於論文被接收後發布，暫時無法直接重現實驗。  🎯 **對工程師的實務啟示**  
- 在構建長對話 Agent 時，可考慮將記憶分為工作、情境、人格與關係圖四個模組；  
- 檢索策略可採用「先語義後關係圖」的條件式流程，根據問題複雜度動態調整開銷；  - 角色專門的證據綜合管道有助於分離推理與語言生成的責任，提升系統的可維護性。  

🔗 **論文連結**  
📝 AdaMem: Adaptive User-Centric Memory for Long-Horizon Dialogue Agents  
👤 Shannan Yan, Jingchen Ni, Leqi Zheng, Jiajun Zhang, Peixi Wu (Tsinghua University; WeChat Vision, Tencent Inc.; USTC)  
🔗 https://arxiv.org/abs/2603.16496  
（程式碼將於論文被接收後釋出）  

你認為這種多層、適應性的記憶架構在實際對話系統中有哪些可落地的場景？歡迎在留言區分享你的看法 👇  

#AI #LLM #Agent #Memory #AdaMem #Tsinghua #Tencent #長對話 #使用者建模 #SOTA #arXiv #機器學習 #自然語言處理
