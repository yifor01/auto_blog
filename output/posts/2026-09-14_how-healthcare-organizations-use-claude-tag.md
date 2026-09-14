---
title: How healthcare organizations use Claude Tag
source: Claude Blog
url: https://claude.com/blog/how-healthcare-organizations-use-claude-tag
model: claude-code/sonnet
generated_at: '2026-09-14T21:03:18.658874'
pinned: true
---

📌 醫療團隊怎麼讓 Claude 加入 Slack，卻完全碰不到病患資料

TL;DR：Insight Health、Tennr 用 Claude Tag 在 Slack 頻道裡處理告警與內部工具，全程不接觸 PHI。

醫療產業導入 AI 助理最大的顧慮，向來是病患隱私資料（PHI）會不會外洩。Insight Health 和 Tennr 給出的答案是：讓 Claude 以「Slack 隊友」身份加入團隊，但透過頻道與連接器層級的隔離，讓它根本碰不到敏感資料。

🤔 **Claude Tag 是什麼，為何醫療業能用**

Claude Tag（beta）讓使用者在 Slack 頻道中 @Claude，它會讀取討論串、使用已連接的工具完成工作並回報結果，也能記住頻道歷史，讓長期任務不必重複說明背景。目前 Claude Tag 尚未被 Anthropic 的 Business Associate Agreement（BAA）涵蓋，因此還不能用於接觸 PHI 的場景，但多家醫療機構已經在「不碰 PHI」的頻道與連接器中啟用它。

🧩 **權限怎麼切：頻道範圍 + 連接器隔離**

管理員可以決定 Claude Tag 在哪些頻道生效、能存取什麼：預設關閉、只在核准頻道開啟，DM 可停用，連接器也是逐頻道授權。它只看得到一般工作區成員看得到的公開頻道內容，無法讀取未被邀請的私人頻道。透過「access bundles」，團隊可以在同一頻道連上程式碼庫與 issue tracker，同時讓 EHR、臨床系統、病患通訊完全不可觸及。

📊 **Insight Health：97% 告警不需工程師介入**

Insight Health 打造的 MagicDocs 是專科醫療診所用的 AI 轉診協調工具，服務超過 1,100 間診所、涵蓋 56 個專科。過去三個月，該公司在不含 PHI 的工程與客服頻道中讓 Claude Tag 調查告警、開票與去重、審查 PR，並在討論串間延續脈絡。在高頻告警頻道，他們讓 Claude Tag 與自行用 Claude Agent SDK 打造的第二個 agent「Zeus」搭配：Claude Tag 能看程式碼庫與 Linear，Zeus 則跑在有 BAA 保護的 Claude API 組織上，能查詢正式環境資料並在資料進入 Slack 前遮蔽 PHI。兩者分工調查根因、開草稿 PR、監控測試，最後由工程師審核合併。啟用 Claude Tag 後，關鍵告警頻道中 97% 的告警不需工程師出手即可結案。

**Tennr：一個月內出貨 15 張以上內部工具票**

患者轉診平臺 Tennr 則讓 Claude Tag 成為內部工具的主要維護者。今年 7 月上線的招募門戶 recruiting.tennr.com 由 Claude Code 建置，並在專屬 Slack 頻道中交由 Claude Tag 持續維護。招募人員、People 團隊、用人主管等非技術同仁直接用白話英文 @Claude 提需求，Claude 完成程式修改、部署並回報。約一個月內團隊透過這種方式出貨了 15 張以上工單，包含修補一個被公開曝露的 copy API（發現當天就鎖住）、修正 Ashby 匯入導致權益重置的 bug，以及在一次薪酬顯示錯誤後主動發出全頻道通知說明受影響範圍與補救方式。

💡 **人機協作的關鍵：頻道分權而非全域授權**

Tennr 業務營運暨策略副總 Abe Griffiths 表示，因為可以逐頻道劃定 Claude 的行為尺度，例如在內部工具頻道讓 Claude 自主修 bug、改程式碼、略過 PR 審查直接出貨，但在 Product 或 Eng 頻道只做資訊蒐集與整理，讓團隊能在低風險場景給予真正的自主權，而不必在所有地方都放權。

⚠️ **仍有限制**

Claude Tag 目前不受 BAA 涵蓋，因此無法用於處理 PHI 的系統；企業組織若啟用並串接 GitHub 可獲得的 25,000 美元額度（Team 方案 10 席以上為 2,500 美元）也將於 2026 年 10 月 1 日到期。

🎯 **實務啟示**

對受監管產業而言，導入 AI 團隊成員的關鍵不在於「等全面合規」，而是先用頻道與連接器的細粒度權限，把 AI 限制在不碰敏感資料的工作範圍內，逐步累積信任與使用經驗。

🔗 **來源**
- 標題：How healthcare organizations use Claude Tag
- 作者／機構：Camy Pearson、Maria Howe、Araba Koomson／Anthropic
- 連結：https://claude.com/blog/how-healthcare-organizations-use-claude-tag

#Anthropic #ClaudeTag #Healthcare #AIAgents #Slack #HealthTech #PHI #EnterpriseAI #HumanAgentTeam #IncidentResponse
