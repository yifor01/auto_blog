---
title: Building an Adaptive Agentic Cybersecurity System with NVIDIA Nemotron
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/building-an-adaptive-agentic-cybersecurity-system-with-nvidia-nemotron/
model: claude-code/sonnet
generated_at: '2026-09-02T10:05:06.523213'
score: 96
---

📌 NVIDIA Nemotron 撐起紅藍對抗的資安 agent 迴圈

TL;DR:NVIDIA 與 CrowdStrike 用 Nemotron 打造持續攻防迴圈,防禦模型準確度勝過頂尖 proprietary 模型且省 99% 成本。

多數企業導入資安 agent,仍然綁定在既有警報、預先定義的工作流程與已知的攻擊行為上,真正困難的問題是找出防禦系統看不到的死角,並把這些死角變成可靠的偵測覆蓋率。NVIDIA 與 CrowdStrike 想測試的問題是:紅隊與藍隊 agent 能不能靠開放模型與專用 harness,把這個迴圈以機器速度持續跑下去。

🤔 **手動交接,限制了攻防迭代的次數**

傳統紅藍隊演練仰賴人工交接:紅隊執行攻擊,藍隊檢視產生的遙測資料,偵測工程師開發或更新偵測規則,紅隊再重新測試。每一次交接都要花時間,限制了團隊能評估的迭代次數與攻擊變化。NVIDIA 與 CrowdStrike 在一個模擬 NVIDIA 加速運算基礎設施的隔離環境中,評估了一套 agentic 攻防系統:防禦端由客製化的 NVIDIA Nemotron 模型在 CrowdStrike 的 agentic 資安系統 SafeMind 中運作。根據 CrowdStrike 內部評估,其 Blue Solano 防禦模型比測試中最領先的 proprietary frontier 模型更準確,成本卻低了 99%。這次評估採用的最佳化開放模型組合,是用 NVIDIA Nemotron 3 Ultra 負責防禦端的協調(orchestration),搭配微調過的 Nemotron 3 Super 負責產生偵測規則。

🧩 **四階段閉環:執行、重建、產生驗證、重測**

這套系統把攻防串成一個可重複的閉環,分成四個階段。第一階段「執行與擷取」:從一個以威脅情資為基礎的目標出發,紅隊 agent harness 在代表性環境中選擇並執行攻擊路徑,每一步都記錄成行動軌跡,同時 CrowdStrike Falcon 端點感測器擷取對應的遙測資料。第二階段「處理與重建」:藍隊 agent harness 接收行動軌跡、感測器遙測與更廣的攻擊情境,以可用的資料來源與 CrowdStrike 的偵測工程經驗作為依據,判斷事件序列中哪些部分可以重建、哪些既有偵測有觸發、哪裡還有可視性或偵測缺口。第三階段「產生與驗證」:藍隊 agent harness 依此產生候選偵測規則,驗證 harness 對每個候選規則做技術檢查,並用擷取到的遙測資料回測,失敗的規則會被退回修正,通過的才送進偵測引擎。第四階段「重測、調整、重複」:偵測規則部署後,由一次獨立產生的攻擊重新測試同一個目標,偵測與告警的結果回饋給紅隊 agent harness,讓它調整並嘗試其他攻擊或規避路徑,產生新的軌跡與遙測資料,直到在這個模擬環境中找不到其他可行路徑為止。

為了讓測試安全又真實,NVIDIA 提供了一份代表自家加速運算基礎設施的、經過消毒處理的自然語言規格,再透過 agent 輔助的流程把這份規格轉換成一個裝有 Falcon 平臺感測器的隔離目標環境。評估過程用攻擊路徑與可觀察的里程碑,從行動軌跡與感測器遙測資料衡量進度,而不是依賴 agent 自己的宣稱;NVIDIA 的資安專家審查過這個環境與威脅路徑的真實性,同一套環境支援所有攻擊回合、偵測測試與評估指標,確保各種設定之間可以一致比較。

藍隊 harness 結合了六道機制:Schema 知識庫讓 agent 能列舉 Falcon 感測器支援的 schema、欄位與查詢語法,避免捏造欄位或無效查詢;遙測落地(telemetry grounding)用紅隊軌跡、Falcon 遙測與更廣的攻擊情境把整個流程錨定在實際觀察到的事件與關係上,減少沒有根據或幻覺出來的關聯;專門的偵測撰寫由客製化的 Nemotron 3 Super 擔任有界限的專家,專責產生與修復偵測規則,把這個專門任務從較長的協調上下文中分離出來;產物檢查(artifact linting)自動拒絕語法錯誤、不支援的欄位,以及綁定特定 IP、主機、使用者或子網路的偵測規則,失敗時會回傳指引,要求改寫成基於行為訊號的版本;偵測回放(detection replay)把每個候選規則對擷取到的攻擊遙測資料重放一次,沒有命中的候選規則會被拒絕並退回修正;獨立審查則由另一個帶著全新上下文的裁判模型,評估每個偵測規則在行為對齊、健壯性與是否恰當運用多重訊號上的表現,補上 linting 與回放沒抓到的品質缺口,審查未過的會把結構化回饋送回藍隊工作流程重新嘗試。這六道機制合在一起,把原本靠人工偵測工程審查才能落實的作法,變成有依據、可測試、可修正的流程,而不只是看起來合理而已。

📊 **協調與撰寫分工:Nemotron 3 Ultra 配 Nemotron 3 Super**

在評估的開放模型組合中,Nemotron 3 Ultra 負責重建攻擊序列、規劃偵測工程步驟並呼叫工具;當需要撰寫或修復偵測規則時,則交給客製化的 Nemotron 3 Super 擔任有界限的專家。這樣的分工讓工作流程的協調與專門的偵測撰寫任務彼此分離。NVIDIA 也提到,Open Secure AI Alliance 正在協助擴展開放模型、harness 與工具在資安領域的生態系。

🎯 **實務啟示**

這套架構示範了一個可以參考的分工模式:用一個較大的模型做長上下文的協調與規劃,另一個較小、經過微調的模型當作有界限的專家處理特定子任務(這裡是偵測規則撰寫),再靠 schema 限制、遙測落地、產物檢查、回放與獨立審查等機制把「聽起來合理」的輸出,逼成「經過驗證」的輸出。對於想把 agent 導入資安偵測工程的團隊,這種以遙測資料為準、而非以 agent 自述為準的驗證方式,值得作為設計依據。

🔗 **來源**
- 標題:Building an Adaptive Agentic Cybersecurity System with NVIDIA Nemotron
- 作者／機構:Michelle Horton, NVIDIA Developer(與 CrowdStrike 合作)
- 連結:https://developer.nvidia.com/blog/building-an-adaptive-agentic-cybersecurity-system-with-nvidia-nemotron/

#NVIDIA #Nemotron #CyberSecurity #AIAgents #CrowdStrike #ThreatDetection #RedTeamBlueTeam #AgenticAI #SecurityOperations #OpenModels
