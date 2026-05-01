---
title: "Synthetic Computers at Scale for Long-Horizon Productivity Simulation"
source: ChatPaper/AI
url: https://arxiv.org/abs/2604.28181
score: 126
model: tencent/hy3-preview:free
generated_at: 2026-05-01T19:28:06.944102
---

📌 【Microsoft 研究】千台合成電腦，讓 AI Agent 練習一個月工作

當大家還在測試 AI Agent 能不能訂餐、回郵件時，Microsoft 團隊已經把戰場拉到了「一個月工作量」的長期生產力模擬。這不只是測試，而是一套用於 Agent 自我進化的基礎設施。

🤔 **長期任務卡關，缺的不是模型而是環境**

目前的 AI Agent 訓練多受限於短任務與靜態 Benchmark。但真實的生產力工作高度依賴於特定的電腦環境，包含複雜的目錄結構與豐富的內容工件（如文件、試算表）。過去缺乏大規模生成這類「動態環境」的方法，導致 Agent 難以學習跨越數千個步驟的長期決策。

🧪 **1,000 台合成電腦，模擬 8 小時的馬拉松**

Microsoft 提出「Synthetic Computers at Scale」方法論，核心在於可擴展地構建具備真實資料夾結構與內容的合成電腦環境。

研究設計採用雙 Agent 模擬機制：
1. **目標設定者**：根據電腦環境的使用者畫像，生成需耗費「約一個月人類工時」的專業目標（如製作多份交付物）。
2. **執行者**：扮演該使用者，在電腦中進行真實操作（導航檔案系統、與模擬協作者溝通、產出工件），直到目標完成。

在初步實驗中，團隊構建了 1,000 台合成電腦。每個模擬平均跨越 **2,000 個回合**，Agent 運行時間超過 **8 小時**。

 **跨越 2,000 回合，效能顯著提升**

這些長期模擬產生了豐富的「體驗式學習信號」。數據顯示，基於這些信號訓練的 Agent，在**領域內（In-domain）與跨領域（Out-of-domain）的生產力評估中，效能均獲得顯著提升**。這證明了該方法能有效解決長期任務中的上下文依賴與連續決策問題。

💡 **從百萬到十億級的擴展潛力**

論文指出，由於使用者畫像（Personas）在理論上可達十億級規模，只要算力允許，這套方法論可擴展至數百萬甚至數十億個合成世界。這意味著可以覆蓋極其多樣的職業、角色與工作情境，為 Agent 提供近乎無限的訓練素材。

⚠️ **初步實驗階段，落地仍需驗證**

目前公開資訊顯示該研究尚處於「初步實驗（Preliminary experiments）」階段。雖然理論擴展性強，但合成環境與真實企業環境的擬合度、以及大規模訓練的實際成本效益比，仍需進一步的工業級驗證。

🎯 **長期推理的基礎設施，而不只是數據**

對於致力於長週期 Agent 系統、企業級自動化與強化學習（RL）訓練的工程師而言，這項研究的啟示在於：**數據的「質」與「環境的真實性」比單純的「量」更重要**。這套框架提供了一個可擴展的基礎設施（Substrate），讓 Agent 能透過模擬體驗進行自我改進（Self-improvement）與強化學習。

🔗 **論文連結**
📝 Synthetic Computers at Scale for Long-Horizon Productivity Simulation
👤 Tao Ge, Baolin Peng, Hao Cheng, Jianfeng Gao @ Microsoft
🔗 論文：https://arxiv.org/abs/2604.28181

你認為 AI Agent 要達到人類一個月的工作產出，目前最大的技術瓶頸是記憶力、規劃能力還是工具使用？歡迎討論 👇

#Microsoft #AI #Agent #ReinforcementLearning #Productivity #人工智慧 #深度學習 #自動化
