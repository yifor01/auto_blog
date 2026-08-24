---
title: 'Harvey Introduces Harvey Tenet: A Kimi K3 Base Post-Trained with Fireworks
  for Long-Horizon Legal Agent Work'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/23/harvey-tenet-post-trained-kimi-k3-legal-agent-model/
model: claude-code/sonnet
generated_at: '2026-08-24T06:32:03.357796'
score: 84
---

📌 Harvey Tenet：用強化學習後訓練Kimi K3打造法律agent

TL;DR：Harvey以Fireworks的非同步RL後訓練Kimi K3，推出研究預覽版法律agent模型Tenet，任務完成率翻倍但尚未開放權重。

法律事務所想要的從來不只是一個聊天機器人，而是能跑完上千輪對話、處理真實案件文件的agent。Harvey這次交出的答案，是一套訓練方法，而不是一個現成產品。

🤔 法律事務所想要「自己的」前沿模型

素材指出，Harvey這次發布的目標有兩個：在開放權重模型上建立前沿等級的法律智慧，並且讓法律事務所有機會擁有自己的專屬模型，而不是完全依賴閉源API。Harvey Tenet正是這個方向下的第一個後訓練模型，以Kimi K3為基礎，透過Fireworks執行非同步強化學習，鎖定長流程（long-horizon）的法律agent工作，於8月20日以研究預覽形式發布。訓練語料混合了合成資料、公開法律資料與人類專家資料，Harvey表示訓練過程未使用任何客戶資料。

🧩 用「模擬法律案件」的沙盒環境做RL

訓練環境仿照Harvey自家的Legal Agent Benchmark（LAB）任務設計：每個任務由一段約50字、類似合夥律師風格的指示開場，搭配一份包含關鍵文件與周邊文件的案件資料，再對照一份由專家撰寫的評分細則（rubric），細則由多項atomic pass/fail準則組成，一般任務約50項，極端情況可達數百項；單一rollout的對話輪數甚至可以超過1000輪。Rollout由LLM-as-a-judge評分，經過消融實驗後，Harvey選定Kimi 2.6作為評分模型。獎勵訊號結合三部分：rubric準則的滿足比例、整體解決的法律議題數量，以及全數通過的額外加成。

策略最佳化採用GSPO演算法，在完整的K3網路上疊加rank-64的LoRA，每次最佳化步驟使用八組、每組八次rollout，訓練規模涵蓋約1,750個環境、單一epoch超過10,000次rollout。Fireworks則負責在kernel層級共同打造訓練與推理部署，透過token-in-token-out與router replay機制，確保這個大型MoE模型在訓練與推理之間維持數值一致。素材也提到，Harvey團隊另外後訓練了一批專家模型，供Tenet以工具或子agent的形式呼叫，但具體是哪些專家模型，素材並未進一步說明。

📊 任務完成率翻倍，且能力有遷移

對比基礎K3模型，Tenet在Harvey自家的Legal Agent Benchmark（LAB）上完成的held-out任務數量幾乎翻倍，在LAB: Contracts子集上則多完成20%，全數通過率（all-pass rate）分別提升9個與2個百分點。Harvey表示，依據Vals提供的基礎模型分數，Tenet在LAB: Contracts上取得業界最佳成績，在LAB整體排名第二。

更值得注意的是遷移效果：這些進步同樣出現在訓練過程中從未見過的Mercor's APEX Agents（公司法場景）與Crosby's Redline Bench上，同時Tenet在LegalBench、CUAD、MAUD與Scale's PRBench等知識型基準上維持原有表現，代表這次的agentic訓練並未犧牲基礎的法律知識推理能力。在成本方面，Harvey表示這是「品質與成本共同最佳化」：開放權重模型本身降低了單位token的價格，加上獎勵設計偏好等品質下更短的執行路徑，進一步壓低了實際消耗的token數，最終在維持穩定成本的前提下取得明顯的品質提升。

⚠️ 目前只是研究預覽，權重未公開

Harvey Tenet目前僅是研究預覽，Harvey尚未公開權重、model card或API端點；基礎模型K3本身是開放權重，但Tenet這個checkpoint屬於Harvey自有。素材指出，公司表示未來會把這套方法「從研究推進到量產」，逐步整合進Harvey自家產品，但就目前而言，公開的是訓練方法本身，還不是可以直接取用的模型。

🎯 實務啟示

對於想要參考這套方法的團隊，Harvey Tenet展示的重點不在模型本身，而在RL訓練配方：用貼近真實工作型態的沙盒任務（partner-style指示＋案件文件＋專家rubric）取代通用對話資料，搭配偏好短路徑的獎勵設計，可能是提升長流程agent任務表現、同時控制推理成本的可行方向；但在Harvey正式開放產品或API之前，這套方法目前仍停留在可參考的技術路線，而非可以直接整合的現成工具。

🔗 來源
- 標題：Harvey Introduces Harvey Tenet: A Kimi K3 Base Post-Trained with Fireworks for Long-Horizon Legal Agent Work
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/23/harvey-tenet-post-trained-kimi-k3-legal-agent-model/

#LegalAI #ReinforcementLearning #LLM #KimiK3 #Harvey #AgenticAI #Fireworks #LegalTech #PostTraining #GSPO
