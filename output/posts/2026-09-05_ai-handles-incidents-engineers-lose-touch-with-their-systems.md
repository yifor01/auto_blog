---
title: AI handles incidents, engineers lose touch with their systems
source: Hacker News
url: https://www.sylvainkalache.com/blog/ai-handles-incidents-engineers-lose-touch-with-their-systems
model: claude-code/sonnet
generated_at: '2026-09-05T19:17:00.422716'
score: 75
---

📌 AI包辦事故排除，工程師卻愈來愈不懂自己的系統

TL;DR：AI SRE把例行事故處理得又快又好，卻可能讓工程師在真正棘手的事故面前失去判斷力。

半夜三點，一個容量問題被AI自動排查、自動修復，你完全不用起床。這聽起來像是夢寐以求的場景，但作者提出一個尖銳的疑問：如果例行事故都交給AI處理，工程師從哪裡累積判斷系統故障的直覺？

🤔 **從LinkedIn的自癒系統原型到今日的AI SRE**

作者2012年在LinkedIn擔任SRE時，就曾設計過一套能自我修復、從過往事故學習的系統，當時AI能力遠不及今日，那套系統終究只是原型。如今，這類被稱為「AI SRE」的工具已經能檢視告警、形成假設、查詢遙測資料、比對近期部署，甚至直接動手修復問題。作者認為這些工具確實令人驚豔，但也點出核心隱憂：我們正在與自己的系統漸行漸遠。

🧩 **Bainbridge的「自動化的反諷」**

人因研究學者Lisanne Bainbridge在1983年的經典論文《The Ironies of Automation》中指出，自動化會減少操作者練習例行工作的機會，卻仍要求他們在新奇、異常的狀況下負起責任，因此操作者反而需要比自動化之前更熟練、接受更多訓練。作者據此預測，未來大多數事故的平均修復時間（MTTR）會因AI輔助而下降，但複雜事故的排除時間將會大幅拉長，因為應變的工程師早已與系統失去連結，難以進行有效調查。

📊 **航空業如何為罕見故障做準備**

作者以航空業作為對照：現代渦輪引擎的空中熄火機率低於每十萬飛行小時一次，罕見到一名商用機師可能終其職涯都不會在模擬器外遇到一次。但故障一旦發生，機師必須迅速正確反應。復興航空235號班機起飛後右側引擎螺旋槳自動順槳，機組人員誤判狀況，飛機在第一個警告出現後僅117秒就失速墜毀。正因如此，美國聯邦航空總署（FAA）規定機長每六個月就必須完成複訓或適任性檢定，其中包含起飛引擎故障等情境演練。

💡 **軟體業需要事故模擬器**

作者任職的事故管理公司Rootly與Uptime Labs合作，透過模擬真實電商停機事故來實踐這個理念：工程師在模擬情境中擔任事件指揮官，一邊使用觀測工具排查問題，一邊在Slack上與LLM扮演的關係人（如執行長、客服）協調溝通。作者過去也曾創辦一所以「做中學」為核心的軟體工程學校，當時Dropbox反映錄用的畢業生排錯能力仍不足，他因此設計出讓學生面對「故障基礎設施」、自行診斷修復的專案。

⚠️ **看AI示範，不等於自己動手練習**

作者也提到可以讓AI代理人解釋它排查時採取的步驟與依據的訊號，藉此保留部分學習效果，但強調「解釋與觀察無法取代實作」，就像看小威廉絲打球能學到一些東西，但網球終究要親自上場才學得會。

🎯 **實務啟示**

隨著LLM承擔愈來愈多例行維運工作，團隊很可能累積「理解負債」：系統實際如何運作，與應變工程師對系統的理解程度之間的落差會愈拉愈大。作者建議把事故模擬納入on-call準備的常態流程，讓工程師定期親手處理不熟悉的故障、在壓力下練習協調與溝通，而不是把這些能力的維持完全寄託在AI身上。

🔗 **來源**
- 標題：AI handles incidents, engineers lose touch with their systems
- 作者／機構：sylvainkalache（Rootly）
- 連結：https://www.sylvainkalache.com/blog/ai-handles-incidents-engineers-lose-touch-with-their-systems

#SRE #IncidentResponse #AIops #Observability #ChaosEngineering #DevOps #AutomationRisk #OnCall #ReliabilityEngineering #AIinOps
