---
title: "CLEF: EEG Foundation Model for Learning Clinical Semantics"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.10817
score: 113
model: tencent/hy3-preview:free
generated_at: 2026-05-12T20:42:22.223887
---

📌 【MIT CSAIL】CLEF：長序列EEG基礎模型  

腦波（EEG）診斷需要觀察完整的錄製時段，並將訊號模式與病人臨床背景結合。現有的EEG基礎模多半專注於短視窗解碼，難以納入完整的臨床資訊。  

🤔 **你以為 AI 只能看短片段腦波？CLEF 卻能讀取整段 EEG，並將其與病歷報告對齊**  

隨著臨床對腦波解讀需求的增加，單靠短窗模型可能遺漏跨時段的關鍵特徵。這促使研究團隊探索能夠處理完整會話並與神經科報告、電子健康紀錄（EHR）產生語義對齊的模型。  

🧪 **234項多任務基準、超過26萬段EEG會話**  

研究團隊構建了一個涵蓋疾病表型、藥物暴露與EEG發現的234任務基準，資料來自超過108萬位患者的260k+ EEG 會話。CLEF 將完整會話表示為3D多週頻譜圖(token)，使得Transformer能在會話規模上進行建模。透過對比學習，CLEF 同時將這些token與神經科報告以及結構化EHR資料對齊。  

🚀 **CLEF 在 229/234 項任務上優於既有模型，平均 AUROC 從 0.65 提升至 0.74**  

- 在所有基準任務中，CLEF 有 229 項表現優於先前的EEG基礎模型。  
- 整體平均 AUROC 由 0.65 提升至 0.74。  
- 僅使用重建目標的預訓練已經超過既有模型；加入報告與EHR的對比對齊進一步提升效能。  
- 持離概念及外部隊伍實驗顯示，這些表示具備超越訓練對齊目標的泛化能力。  

💡 **長會話建模與臨床語義對齊是關鍵**  

CLEF 的設計讓模型能夠捕捉跨時段的腦波動態，而對齊步驟則將純粹的訊號特徵映射到臨床概念（如疾病標籤、藥物使用）。這種「訊號＋語義」的雙重約束，使得表示在下游任務上更具解釋力與預測力。  

⚠️ **資料來源單一、基準多為相關任務、長期泛化尚待驗證**  

- 所有EEG資料來自特定醫療系統，可能限制對其他機構或不同採集設備的直接適用性。  
- 基準任務雖多，但仍主要圍繞疾病、藥物與波形特徵，對於極端罕見或新興臨床場景的表現仍需進一步驗證。  
- 論文僅報告了持離概念與外部隊伍的初步結果，長期臨床部署的穩定性與實用性尚未在實際工作流程中完整驗證。  

🎯 **對研究與臨床的啟示**  

- 若模型與程式碼公開，研究者可在此基礎上探索更細粒度的腦波‑臨床對應工作。  
- 臨床團隊在評估EEG時，可考慮將長會話表示作為輔助工具，特別是在需要結合病史與藥物資訊的情況下。  
- 未來工作可著重於跨機構資料的領域適應，以及探索模型在即時監控或ICU情境中的應用潛力。  

🔗 **論文連結**  
📝 CLEF: EEG Foundation Model for Learning Clinical Semantics  
👤 Peng Cao, Ali Mirzazadeh, Jong Woo Lee, Aleksandar Videnovic, Dina Katabi (MIT CSAIL; Brigham and Women’s Hospital; Harvard Medical School; Massachusetts General Hospital)  
🔗 https://arxiv.org/abs/2605.10817  

你認為這種「長會話＋臨床語義」的方向，會在未來的腦波診斷中扮演什麼角色？歡迎在留言區分享你的看法 👇  

#AI #EEG #機器學習 #臨床醫學 #MIT #哈佛醫學院 #麻省總醫院 #Brigham and Women’s #神經科技 #基礎模型 #深度學習 #醫療AI
