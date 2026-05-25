---
title: "Human-in-the-Loop Multi-Agent Ventilator Decision Support with Contextual Bandit Preference Learning"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.23320
score: 100
model: tencent/hy3-preview:free
generated_at: 2026-05-25T21:00:33.884946
---

📌 【上海工程科技大學等機構聯手】人類回圈多代理框架如何變換呼吸機決策支援？

隨著重症監護病房（ICU）對呼吸機參數的即時調整需求日益增加，既要追蹤不斷變化的生理狀態，又必須遵守安全邊界與醫師個人的調校風格。傳統規則型方法難以實現個人化，而端到端強化學習或單一大型語言模型則在控制與可審計性上面臨挑戰。

🎣 **你以為 AI 能直接取代醫師決策？這篇研究指出，真正的進步可能在於「人在回圈」的協同。**

🤔 **ICU 呼吸機決策需要兼顧即時生理追蹤與安全個人化**

研究指出，現有的規則型決策支援難以泛用於不同醫師的調校習慣；純粹的強化學習或大語言模型則因缺乏可追蹤的證據與安全保證，難以在高風險的 ICU 環境中落地。因此，團隊尋求一種能同時提供模組化決策、可審證過程以及個人偏好適應的架構。

🧪 **以契約驅動介面串聯多代理，並透過情境強化 bandit 學習醫師偏好**

論文提出 **Ventilator Decision Support System (VDSS)**，採用人類在回圈（human‑in‑the‑loop）的多代理框架。系統透過「契約驅動結構化介面」將各決策模組（例如氣體交換、壓力限制、患者舒適度等）解耦，使其能以可追蹤的方式交換資訊。每次調整週期結束後，系統採用 **contextual bandit** 從最終被醫師接受的決策中學習該醫師的偏好，並將這些偏好作為後續建議的引導。當醫師提供結構化的拒絕回饋時，系統會觸發有針對性的重新規劃，以減少無效的互動輪次並提升互動穩定性。

🔍 **專家回顧顯示建議可接受度提升、互動輪次減少**

經由對歷史 ICU 軌跡的回放與專家複審，研究團隊觀察到：VDSS 的建議在專家眼中具有更高的可接受度，且達到可接受方案所需的互動輪次較少。這些結果顯示，在保留人類最終決策權的同時，系統能提供更具個人化且易於追蹤的支援。

💡 **關鍵在於「結構化介面」與「偏好即時適應」的結合**

VDSS 的創新點不僅在於引入多代理架構，更在於：
- **契約驅動介面**：確保各模組間的資訊交換有明確規範，便於審計與除錯。
- **情境 bandit 偏好學習**：從真實臨床決策中即時更新醫師個人偏好，使後續建議更貼近其風格。
- **結構化拒絕回饋導向重新規劃**：將醫師的否定意見轉換為具體的規劃目標，減少無意義的來回迭代。

這種設計讓系統在提供決策支援時，既能保持醫師的最終決策權，又能透過可追蹤的證據鏈降低風險。

⚠️ **僅以歷史軌跡回放驗證、實際臨床部署尚需進一步驗證**

目前的評估主要基於回顧性 ICU 軌跡與專家複審，未涉及前瞻性臨床試驗。因此，長期使用對患者結果的影響、系統在不同 ICU 設備與工作流程中的適應性，以及真實環境中的安全與可用性，仍需後續實證研究進一步確認。

🎯 **對 AI 醫療協作的啟示：人在回圈 + 模組化契約 + 偏好適應**

此研究表明，在高風險醫療決策中，單纯追求全自動化可能不是最佳路徑。相反，結合以下三種機制更能促進安全且可接受的人機協作：
1. **人在回圈**：保留臨床專家的最終決策權。
2. **模組化契約介面**：確保系統內部元件可獨立開發、測試與審計。
3. **即時偏好適應**：透過輕量級的強化學習（contextual bandit）捕捉並尊重個人醫師的決策風格。

未來若能在真實 ICU 環境中進行前瞻性驗證，並與電子健康紀錄（EHR）系統深度整合，此框架有望成為更廣泛的臨床決策支援平台的基礎。

🔗 **論文連結**
📝 Human-in-the-Loop Multi-Agent Ventilator Decision Support with Contextual Bandit Preference Learning  
👤 Sijia Li, Xiaoyu Tan, Qixing Wang, Weiyi Zhao, Chen Zhan  
🏫 Shanghai University of Engineering Science; Tencent Youtu Lab; Tongji University School of Medicine; Songjiang Hospital Affiliated to Shanghai Jiao Tong University School of Medicine; Max Planck Institute for Heart and Lung Research; Fudan University; BIH at Charité – Universitätsmedizin Berlin  
🔗 https://arxiv.org/abs/2605.23320

你認為在 ICU 這類高風險場景中，「人在回圈」的 AI 設計是否能平衡安全與效率？歡迎留言討論 👇

#AI #醫療AI #呼吸機 #人機協作 #多代理系統 #ContextualBandit #ICU #ShanghaiUniversity #TencentYoutu #醫學創新
