---
title: Building Legal Agents When You Can't See the Data - Jacob Lauritzen, CTO of
  Legora
source: Latent Space
url: https://latent.space/p/building_legal_agents_when_you_can_t_see_the_data_-_jacob_lauritzen_cto_of_legora/
model: claude-code/sonnet
generated_at: '2026-11-03T00:14:20.794893'
score: 74
---

📌 看不到一行紀錄，Legora 如何把法律 Agent 的引用準確率做到 99%

TL;DR：法律 Agent 公司 Legora 無法讀取客戶資料，靠模擬測試環境把引用正確率推到 99%。

一間公司要怎麼改善自己 AI 產品的表現，卻完全看不到使用者在產品裡做了什麼？這正是 Legora 每天面對的處境：律師事務所的客戶資料歸屬客戶，Legora 連一條完整的執行紀錄都看不到。

🤔 **從 Stockholm 地下室的 ChatGPT 外掛到法律 Agent**

Legora CTO Jacob Lauritzen 在 Latent Space 的訪談中回顧，團隊最初是在 Stockholm 的地下室，用 ChatGPT 搭配瑞典法律資料與搜尋工具起步。如今律師能用 Legora 在 Word 文件裡起草與編輯合約、在單一表格中審閱一萬份合約、執行併購盡職調查，Agent 也會協調律師、客戶與其他 Agent 之間的工作。Legora 自己進行公司併購時，也是用自家產品做盡職調查。

🧩 **看不到紀錄，就建一個「世界」來測試**

這是整篇訪談最具體的工程做法：由三位工程師與三位律師組成的團隊，依照客戶實際工作型態建立模擬測試環境，概念上類似強化學習裡用來訓練 Agent 的「world」。因為無法直接檢視正式環境的 trace，Legora 轉而對 trace 做改寫（paraphrasing），把失敗模式歸納成十到二十種類型，藉此在不觸碰客戶資料的前提下定位問題。

Jacob 提到一個具體案例：引用（citation）正確率原本停留在 70%，團隊原本沒打算針對這點做任何改動，結果單次模型更新後，準確率直接跳到 99%，Legora 自己什麼都沒改。這也呼應他對現有模型能力的判斷：模型已經能把約六成的法律工作做得不錯，剩下的部分則需要更聰明的模型才能補上。

💡 **從拒絕做模型選擇器，到擁抱模型套利**

Legora 曾經多年拒絕在產品裡加入模型選擇器，後來還是加上了；Jacob 也坦言不同模型各有脾性,他覺得某些模型在起草文件時話太多，偏好另一款模型更精簡的寫法——這也呼應他的另一個觀察：起草一份長合約，本質上是一個搜尋問題，而不只是生成問題。公司出於資料隱私考量，所有服務都跑在 Azure 上，也因此沒有採用 ElevenLabs 的語音轉錄服務。

產品面上，Tabular Review（百萬儲存格的審閱表格）已經被業界原封不動抄到連名稱都一樣；法務情報入口則是透過 Slack 上的 intake bot 運作，Agent 可以建立清單，而一張清單本身又能啟動另一個 Agent，形成一套可疊加的工作流程。團隊內部也區分「legal engineer」與「forward-deployed engineer」兩種角色，分工處理客戶導入與產品落地。

⚠️ **二十人工程團隊的極限**

Jacob 曾用「三百壯士」那張投影片論證二十名工程師就足以撐起整個產品的未來發展，如今團隊已擴編到一百人，他仍覺得人手不足——這反映出法律 Agent 系統的複雜度,遠超早期團隊的預期。

🎯 **對工程團隊的啟發**

當產品無法直接存取使用者資料時，用模擬環境還原客戶真實工作場景、並對 trace 做改寫後再分析失敗模式，是一條可行的替代路徑。同時,模型更新帶來的準確率躍升（如本例從 70% 到 99%）提醒團隊：定期重新評測既有 pipeline，有時比自己動手修補更有效。

🔗 **來源**
- 標題：Building Legal Agents When You Can't See the Data - Jacob Lauritzen, CTO of Legora
- 作者／機構：Latent Space（主持人 Basil Chatha；來賓 Jacob Lauritzen, CTO of Legora）
- 連結：https://latent.space/p/building_legal_agents_when_you_can_t_see_the_data_-_jacob_lauritzen_cto_of_legora/

#LegalTech #AIAgents #Legora #Evals #LLMOps #Citations #DataPrivacy #ProductEngineering #ReinforcementLearning #AIforLaw
