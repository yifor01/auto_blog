---
title: 'Reducing the noise: How Atlassian built an OCSF security lakehouse on Databricks'
source: Databricks
url: https://www.databricks.com/blog/reducing-noise-how-atlassian-built-ocsf-security-lakehouse-databricks
model: claude-code/sonnet
generated_at: '2026-10-16T20:19:04.376119'
score: 64
---

📌 每天 440 億筆事件,Atlassian 如何讓資安資料講同一種語言

TL;DR:Atlassian 用開放的 OCSF schema 搭配 Databricks 打造資安湖倉,把雜亂的日誌格式統一,查詢速度明顯提升。

一間經歷 20 年成長與多次併購的 SaaS 公司,光是資安日誌就累積出每天 440 億筆事件,而且每個收購進來的系統都帶著自己的時間戳格式與專有 schema。Atlassian 的資安日誌工程負責人 Zachary Schmerber 形容,這對任何想把資料組織起來的人來說都是「維運上的消耗」。他們沒有選擇再加一層轉接層,而是從根本換了一套共同語言。

🤔 **分析師在正式開始調查前,先得花時間「翻譯」資料**

Atlassian 的問題不只是資料量大,而是資料「形狀」不一致:不同時間戳、不同的專有 schema,導致分析師要先手動正規化資料才能分析,跨平臺的關聯分析因此受限,SIEM 管線的處理速度也追不上資料成長的速度。團隊需要的是一個能把分散的遙測資料收攏到同一處、同時保持彈性又不被單一廠商綁死的方法。

🧩 **選 OCSF 的理由:夠開放、夠嚴謹,而且被 Linux Foundation 撐著**

團隊最終把所有資料標準化到 Open Cybersecurity Schema Framework(OCSF),並在 Databricks 上建立湖倉。根據文章說明,團隊考量過 ECS、UDM 等替代方案,但只有 OCSF 被視為真正全開放的選項:它有強型別的 schema 與完整驗證機制,能在轉換後把歧異降到最低,同時具備不錯的壓縮效率、延展性,背後有 Linux Foundation 支持,並朝向成為國際標準邁進。OCSF 大約有四萬個欄位,乍看嚇人,但這種「囉嗦」反而是最大資產,因為語意脈絡會跟著資料一起保留下來——有五套弱點掃描器時,得到的是一份資料集,而不是五份互不相通的資料。

選擇 Databricks 作為平臺的理由則是原生 ACID 交易,讓團隊能在不打斷下游使用者的情況下跨 schema 版本遷移;auto-scaling 的 Spark 叢集能處理跨團隊的高流量共用工作負載;平臺本身也能吸收大型多團隊組織的基礎設施管理負擔。團隊刻意選擇 ETL 而非 ELT,在資料流動過程中就完成轉換,目的是支援即時偵測、維持廠商中立性,並在搬動資料時順便做壓縮。

一個關鍵的工程決策是把整個 OCSF schema 直接嵌進 Go 的 struct,團隊稱之為「TypeGo」:因為 schema 活在型別系統裡,正確性在編譯期就能保證。Schmerber 說,「每次產生新的 OCSF 日誌,它都已經先被驗證過,因為它不可能是別的東西,只能是 OCSF。」這個型別安全也「馴服」了 AI:當團隊用 agentic workflow 自動化轉換流程時,嚴謹的 schema 大幅降低了幻覺,也因為 agent 無法產出無效映射而少走許多錯誤迴圈,進而降低 token 消耗。

📊 **查詢快 20 倍,人力地圖化時間從一年縮到兩個月**

結構化的 OCSF 資料配合 partitioning 與 Z-ORDER,讓一個具代表性的查詢從約 45 秒降到 2 到 3 秒,改善幅度約 95%,較大型查詢也有類似的提升幅度。啟用搭配 Photon 的 Graviton 叢集後,查詢成本與執行時間都砍掉約三分之二。

更顯著的是維運面的轉變。資安資料工程團隊原本要走一套六階段的手動流程:收集日誌、轉成 TypeGo、路由、測試、設定、透過 PR 上線。隨著自動化程度提高,這套流程最終被交還給使用者,變成自助式平臺:分析師只要指出想要的日誌並提供一份標準化資料集,經過一個把關確認步驟後,workflow 會自動掃描 Go struct 裡的 schema、產生映射與 DAG、在本機測試、以 canary 設定透過 PR 部署、在 canary 環境大規模驗證,經過一段觀察期後才推上生產環境,並在出錯時通知使用者;正式上線前還有迴歸測試把關。Schmerber 提到,「我花了一年才映射出大約三分之一的資料,但接下來兩個月就把剩下三分之二做完。」

💡 **從一對一告警,走向以訊號為基礎的偵測**

Atlassian 偵測與回應團隊的 Jordan 表示,導入 OCSF schema 讓團隊能把偵測管線從「一個偵測對一則告警」,轉換成以訊號與風險為基礎的方法,把多個訊號發現聚合成單一告警。團隊透過名為 Alert Explorer 的自製工具,讓發現結果圍繞標準化的 OCSF 欄位值聚類,例如同一個 actor.user 值,無論出現在身分驗證事件還是網路事件裡都是一致的。這種一致性讓團隊能標準化聚類、資料豐富化與分級處理的做法:不必針對每個偵測各自寫豐富化邏輯,而是對一個標準化的使用者名稱欄位呼叫同一套豐富化 API。Jordan 說,這讓分析師「不論資料來自哪裡,都能深入分析、取得更有意義、可行動的告警。」

⚠️ **這是單一公司的案例,規模與適用性仍有保留**

文章呈現的是 Atlassian 自身的實作經驗與效益數字,並未討論在資料量或團隊規模不同的組織中是否能複製相同成果,也沒有提及導入過程中遇到的具體阻力或失敗嘗試。

🎯 **實務啟示**

如果你正在打造或整理資安資料管線,這個案例給出的參考是:越早採用一套開放且強型別的 schema,後期做跨來源關聯分析時省下的映射工時就越多;把 schema 嵌進程式語言的型別系統(如 Go struct)能讓驗證左移,順便讓 agentic 自動化流程的幻覺與 token 消耗都降下來;而 ETL-in-flight 的設計選擇,則是在即時偵測需求與廠商中立性之間取得平衡的具體做法。

🔗 **來源**
- 標題:Reducing the noise: How Atlassian built an OCSF security lakehouse on Databricks
- 作者／機構:Databricks
- 連結:https://www.databricks.com/blog/reducing-noise-how-atlassian-built-ocsf-security-lakehouse-databricks

#OCSF #Databricks #Lakehouse #SecurityEngineering #DataEngineering #SOC #ThreatDetection #CyberSecurity #Atlassian #AIAgents
