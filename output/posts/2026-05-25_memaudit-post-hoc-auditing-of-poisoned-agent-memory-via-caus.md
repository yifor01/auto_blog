---
title: "MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.23723
score: 120
model: tencent/hy3-preview:free
generated_at: 2026-05-25T20:27:37.956531
---

📌 【Chinese Academy of Sciences 最新研究】MemAudit：事後追查記憶中毒的因果圖譜  

你以為記憶中毒只能靠即時過濾擋下？當有害行為已經發生，卻沒有辦法追溯是哪條記憶惹的禍？  

🤔 **記憶增強帶來長程表現，也開啟了隱形後門**  
大型語言模型代理越來越依賴持久記憶來存放過往互動、檢索示範並提升長距離任務表現。這同樣為惡意使用者提供了可乘之機：透過普通對話將惡意紀錄注入代理記憶，之後再被檢索出來操縱代理的推理與行動。現有防禦多著眼於線上介入（如過濾提示詞或阻斷輸出），卻缺乏事後審計的方法來指出具體哪些記憶導致了問題。  

🧪 **基於反事實影響與結構異常的雙重信號設計**  
我們提出 MemAudit，一個事後因果記憶審計框架。它結合兩種互補訊號：  
1. 反事實記憶影響分數，量測每條記憶對有害輸出的因果貢獻；  
2. 記憶一致性圖，在整個記憶庫中尋找結構上異常的紀錄。  
這兩個訊號一起被用來標記可疑的中毒記憶。  

 **QA 攻擊成功率從 70% 降至 0%， reasoning-agent 從 83.3% 降至 0%**  
我們以 MINJA（僅透過查詢注入的記憶中毒攻擊）作為基準，在問答（QA）與推理代理（reasoning-agent）兩個設置上進行事後審計實驗。結果顯示，使用 MemAudit 後，QA 攻擊成功率從原本的 70% 降至 0%；而推理代理的攻擊成功率從 83.3% 同樣降至 0%。  

💡 **因果貢獻分數與記憶一致性圖共同指向中毒痕跡**  
高影響分數表明某條記憶在產生有害輸出上具有顯著的因果作用；同時，結構異常圖能夠發現那些與正常記憶模式顯著脫節的節點。當兩者同時指向同一條記憶時，誤判率大幅下降，使得審計既精準又可靠。  

⚠️ **僅針對特定注入方式驗證，泛化性尚待進一步探討**  
本研究僅評估了 MINJA 這種透過普通互動生成並存儲惡意紀錄的攻擊方式；對其他類型的記憶中毒（例如直接修改記憶庫）的適用性尚未驗證。此外，實驗主要聚焦於單輪事後審計，長期或重複攻擊的穩定性需要後續工作檢驗。  

🎯 **事後審計可成為記憶增強 Agent 的標準防線**  
對於已經部署記憶增強的 LLM 代理，MemAudit 提供了一種可在觀測到問題後立即定位毒源的工具。工程團隊可將其作為日常安全檢查的一部分，快速隔離並清理可疑記憶，從而減少因記憶中毒導致的風險。  

🔗 **論文連結**  
📝 MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection  
👤 Zhewen Tan, Yilun Yao, Huiyan Jin, Wenhan Yu, Guoan Wang (Chinese Academy of Sciences; Qiyuan Tech; Peking University; University of Chinese Academy of Sciences)  
🔗 https://arxiv.org/abs/2605.23723  

你的代理是否已啟用持久記憶？現在是時候檢查它的「記憶衛生」了 👇  

#AI #LLM #AgentSecurity #MemAudit #TrustworthyAI #ChineseAcademyofSciences #QiyuanTech #PekingUniversity #UCAS #ArXiv #機器學習 #資安
