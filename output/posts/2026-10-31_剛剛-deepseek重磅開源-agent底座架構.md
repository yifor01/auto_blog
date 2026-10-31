---
title: 剛剛，DeepSeek重磅開源：Agent底座架構！
source: 量子位
url: https://www.qbitai.com/2026/10/506904.html
model: claude-code/sonnet
generated_at: '2026-10-31T20:32:28.002073'
score: 104
---

📌 DeepSeek開源Agent底座架構：群裡沒人@，AI自己找到Bug並提交PR

TL;DR：DeepSeek公開Super-agent雙層Router/Worker架構，讓同一個Agent跨平臺持續追蹤任務、主動處理問題。

多數人用Coding Agent的經驗是，開了一個會話討論方案，又開另一個會話改程式碼，最後自己也記不清哪句話該接到哪個上下文。DeepSeek這次要解決的，正是這種「人要追著AI的會話跑」的困境。

🤔 **一個人只能同時跟進3到5個活躍Session**

DeepSeek團隊在文章中提到，日常開發常需要在IM群聊、GitHub、郵件等平臺間來回切換，傳統Coding Agent的操作分散在不同會話裡，使用者得自己記住每個會話進度、再把上下文交代給AI。團隊觀察到，一個人通常只能同時跟進3到5個活躍Session，這意味著模型處理單項任務的能力越強,多工協作的效率反而越容易被人類注意力卡住。

🧩 **Router統籌、Worker執行，加上投機執行**

DeepSeek為Super-agent設計了雙層架構:上層Router負責接收訊息、分配任務與維護全域性上下文,相當於總排程員;下層Worker是一組負責具體執行的Agent會話,可以多任務並行、互不干擾。團隊還設計了訂閱與直通機制,例如某個Worker接手一條GitHub PR後就能直接訂閱後續評論,後續修改意見會直接交給該Worker處理,不需再經過Router層層轉發。

另一項關鍵技術是投機執行(Speculative Execution):AI發現某件事可能需要處理時,會提前在後臺嘗試,例如群裡有人討論Bug,Super-agent便先著手復現、查原因,找到可行方案就交給使用者,沒找到則保持安靜不打擾。這對應DeepSeek為Super-agent提出的四個核心特徵:連續、高效、主動、持久。

為了支撐24小時線上,團隊採用計算、狀態與執行環境分離的思路,Agent計算邏輯可在雲端執行、會話狀態獨立儲存,本地裝置離線也不影響雲端任務狀態;此外還引入獨立的Watchdog機制,專門監督其他Agent,檢測程式故障、判斷任務是否陷入無效迴圈或偏離目標並嘗試介入修復。訊息過濾上則用兩級機制:先用程式規則篩除無關訊息,再由大模型判斷剩餘事件是否需要行動,以減少不必要的Token消耗。

📊 **實測：任務完成時間中位數12.4分鐘，比傳統方案更穩定**

DeepSeek模擬了包含約300條訊息、20項工作請求的協作環境,對比Super-agent與傳統單Session加Subagent方案,每種配置重複測試5次。結果顯示,Super-agent任務完成時間中位數為12.4分鐘,95分位數為15.7分鐘;而傳統單Session方案在中性提示下95分位任務完成時間達到29.5分鐘。不過效率提升也伴隨Token開銷,團隊發現取消事件直通機制後,Router的決策次數增加約30%,讀取快取Token增加約37%。

⚠️ **非同步ReAct Loop尚未預設開啟**

素材提到,支撐Super-agent持續響應新指令的非同步ReAct Loop機制已在DeepSeek Harness中實現,但尚未預設開啟,意味著這套持續性架構的部分能力仍處於可選、未全面啟用的階段。

🎯 **實務啟示**

對正在搭建多Agent系統的團隊,DeepSeek這套Router/Worker分層加訂閱直通的設計,提供了一個具體可參考的工程模式:把「誰接收任務」和「誰執行任務」拆開,並用訂閱機制避免老任務被重新轉發一遍。投機執行的思路也值得借鑑——讓Agent在後臺先嘗試、安靜失敗、成功才現身,是降低對使用者打擾同時保持主動性的折衷方案。專案已開源,有興趣的工程師可以直接參考程式碼落地評估。

🔗 **來源**
- 標題：剛剛，DeepSeek重磅開源：Agent底座架構！
- 作者／機構：夢瑤，量子位
- 連結：https://www.qbitai.com/2026/10/506904.html

#DeepSeek #AIAgent #AgentArchitecture #OpenSource #AutonomousAgent #SoftwareEngineering #LLM #MultiAgent #DevTools #SpeculativeExecution
