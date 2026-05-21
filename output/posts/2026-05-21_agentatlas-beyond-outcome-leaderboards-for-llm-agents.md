---
title: "AgentAtlas: Beyond Outcome Leaderboards for LLM Agents"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.20530
score: 98
model: tencent/hy3-preview:free
generated_at: 2026-05-21T21:08:41.785504
---

📌 **【UC Santa Cruz & MIT】單一成功率不再足以評估 LLM 代理，AgentAtlas 提供更細膩的診斷框架**

你以為領先的 LLM 代理只要看任務成功率就夠了？新研究顯示，這種單一指標可能掩蓋了模型在決策與失敗上的關鍵差異。

🤔 **單一成功率無法衡量可部署代理的真實能力**  
現有代理基準各自強調不同度量（任務成功、工具呼叫有效性、軌跡一致性、安全性或攻擊韌性），無法全面反映代理在真實環境中的行為。因此，研究團隊認為需要一套更細緻的分類與評估方法。

🧪 **六狀態控制決策分類與九類失敗標註**  
AgentAtlas 提出兩個分類系統：  
1. 六種控制決策狀態（Act / Ask / Refuse / Stop / Confirm / Recover），用以描述代理在每一步的行為選擇。  
2. 九種軌跡失敗類別，並以兩個正交層級標記（primary_error_source、impact）來指出錯誤來源與影響程度。

🔑 **移除提示選單後，所有模型準確度驟降 14‑40 個百分點**  
在以八個模型（四個 frontier 閉源、四個開源權重）為基礎的合成實驗中，研究團隊比較了「taxonomy‑aware」（提供明確選單）與「taxonomy‑blank」（未提供選單）兩種提示方式。結果顯示，去除選單後每個模型的軌跡準確度均下降 14‑40 個百分點，落在 0.54‑0.62 的狹窄區間，且沒有任何單一模型同時在控制準確度、軌跡診斷與工具情境實用保留三項指標上皆稱雄。

💡 **能力來源可被分辨：提示監督 vs. 內在泛化**  
透過 taxonomy‑aware 與 taxonomy‑blank 的對比分析，該方法能量測模型表現中有多少來自提示中的顯著監督，有多少來自模型自身的泛化能力。這有助於區分「真正學會」與「只是跟隨提示」的行為。

⚠️ **實驗規模有限、僅為方法論示範**  
該研究使用固定的八模型集合（共 1,342 個生成項目）進行合成測試，並未發放程式碼或將結果視為正式基準發布。因此，數據主要用於展示評估流程的可行性，長期效果及更廣泛模型的表現仍需後續工作驗證。

🎯 **工程師可直接套用的評估視角**  
- 在設計代理測試時，除了最終成功率外，可記錄代理在每一步的六種決策狀態。  
- 失敗時記錄 primary_error_source 與 impact，以便定位是工具呼叫錯誤、規劃失敗還是安全問題。  
- 透過比較有無決策選單的提示，檢查模型能力有多少仰賴外部監督，從而調整訓練或提示策略。  
- 此框架可適用於現有十五個代理基準的六個行為軸審計，協助團隊選擇或設計更全面的評估集。

🔗 **論文連結**  
📝 AgentAtlas: Beyond Outcome Leaderboards for LLM Agents  
👤 Parsa Mazaheri, Kasra Mazaheri (University of California, Santa Cruz; Massachusetts Institute of Technology)  
🔗 https://arxiv.org/abs/2605.20530

你在評估 LLM 代理時，是否只看最終成功率？歡迎在留言區分享你的經驗與做法 👇

#LLM #AgentEvaluation #AIResearch #UCSC #MIT #AgentAtlas #MachineLearning #AIEngineering
