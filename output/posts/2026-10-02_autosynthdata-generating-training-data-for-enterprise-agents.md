---
title: 'AutoSynthData: Generating Training Data for Enterprise Agents'
source: HuggingFace Blog
url: https://huggingface.co/blog/ServiceNow-AI/autosynthdata
model: claude-code/sonnet
generated_at: '2026-10-02T21:30:54.355259'
score: 94
---

📌 ServiceNow用模型失敗打造企業Agent訓練資料

TL;DR：ServiceNow CoreAI推出AutoSynthData，拿目標模型的失敗和教師模型的成功之間的落差，自動生成可驗證的訓練任務。

企業要的agent不是「什麼都會一點」，而是要在自家系統、自家規則、自家資料狀態下把事情做對。問題是，一個失敗案例只告訴你模型哪裡不會，卻無法直接變成訓練資料——AutoSynthData就是為了解決這個轉換問題而生。

🤔 **一個好的agentic任務要滿足三個條件**

ServiceNow CoreAI團隊先定義了什麼叫「有用的agentic任務」：task = (system specification, user prompt, verifier)。其中user prompt要同時滿足可行性（環境中存在至少一條能完成任務的軌跡）、真實性（像是使用者真的會提出的請求，而不是為了刁難而硬湊的約束）、以及難度（要能曝露目前agent還不穩定解決的能力，已經解得很好的任務就沒有新的訓練訊號）。verifier則要具備一致性（符合user prompt、system specification與任務狀態）、嚴謹性（拒絕不符合任務或違反限制的軌跡）、以及完整性（接受任何有效解法，而不是只認一種標準答案）。

🧩 **從模型失敗到能力規格卡，再到新任務**

AutoSynthData的流程分三步：先讓目標模型與一個更強的教師模型在環境中跑診斷任務，觀察目標模型在哪些任務類型上失敗、教師模型又是怎麼成功的；接著把這些觀察整理成「能力規格卡（capability specification cards）」——值得注意的是，負責生成新任務的模組**不會**拿到原始的評估prompt、實體或verifier細節，只拿到這份經過消毒整理的規格卡，再據此創造出全新的prompt、環境狀態與解法路徑。最後把生成的任務丟進環境中驗證、執行、修補，通過的樣本才拿去做supervised fine-tuning。

資料集建構本身又拆成兩個階段：Target階段由多個worker平行生成核心樣本，每個候選任務都要經過驗證、執行、求解器評估與修補才會被接受；Multiply階段則針對已通過的target樣本做變體擴增，每個變體有自己的使用者請求、環境狀態、實體設定、參考軌跡與verifier，且規定「被multiply出來的樣本不能再拿去衍生下一代」，用這條規則限制跨代漂移。實作上則把生成控制邏輯（品質把關、覆蓋率、資料集組裝）和環境執行邏輯（任務狀態管理、軌跡重播、verifier、求解器執行）拆成controller與adapter兩層，方便套用到不同的企業環境。

💡 **消毒規格卡是避免模型「背答案」的關鍵設計**

這套流程裡最值得留意的設計,是生成器被刻意隔絕於原始評估任務之外，只靠抽象化後的能力規格卡來造題。這樣的分層讓新生成的任務不會變成原始評測集的變形題，而是真正針對「某種能力缺口」在不同情境下重新出題，某種程度上降低了訓練資料汙染評測集的風險。

🎯 **實務啟示**

如果你的團隊也在幫企業agent做post-training，這篇文章提供的task三元組定義（spec／prompt／verifier）與verifier的三個品質要求（consistency、soundness、completeness）值得直接拿來檢視自己手上的訓練資料生成流程：你的verifier是不是太鬆而獎勵了錯誤行為，或是太嚴而扼殺了合理但非標準的解法？

🔗 **來源**
- 標題：AutoSynthData: Generating Training Data for Enterprise Agents
- 作者／機構：Esakkivel Esakkiraja、Shruthan Radhakrishna、Denis Akhiyarov、Sagar Davasam（ServiceNow-AI）
- 連結：https://huggingface.co/blog/ServiceNow-AI/autosynthdata

#AgenticAI #SyntheticData #EnterpriseAI #ServiceNow #SFT #LLMTraining #AIAgents #DataGeneration #MachineLearning #ModelEvaluation
