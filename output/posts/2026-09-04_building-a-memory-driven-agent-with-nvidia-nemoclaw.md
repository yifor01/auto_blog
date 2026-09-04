---
title: Building a Memory-Driven Agent with NVIDIA NemoClaw
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/building-a-memory-driven-agent-with-nvidia-nemoclaw/
model: claude-code/sonnet
generated_at: '2026-09-04T19:52:39.410266'
score: 88
---

📌 【NVIDIA工程實踐】給AI代理裝上「長期記憶」的五個設計教訓

TL;DR：NVIDIA團隊用NemoClaw打造記憶驅動的Chief of Staff代理，記憶架構讓問答準確率提升8.1個百分點。

企業裡的工作往往橫跨數週甚至數月：一則訊息背後可能藏著一個尚未解決的決策，一個專案可能有兩個不同的稱呼。如果每次啟動代理都要從零重建這些脈絡，代理的產出品質注定打折。NVIDIA開發團隊用NemoClaw打造了一個記憶驅動的「幕僚長（Chief of Staff）」代理，試圖解決這個問題。

🧩 **核心設計：self model，一份人類可讀的知識層**

團隊維護一個稱為self model的代理記憶層，以結構化Markdown頁面記錄相關人員、專案、優先順序與工作模式，並定義索引、交叉參照、來源追溯（provenance）與成長上限。排程任務會定期檢視新活動、追蹤未完成的待辦事項，並將使用者的決策持續納入。self model儲存的是「推導出的詮釋」，而非取代原始證據；將兩者分開，開發者才能判斷錯誤答案究竟來自證據本身、記憶維護、檢索過程，還是模型的最終判斷。

📐 **證據、知識、行動三層分離**

架構分為「Evidence → Knowledge → Governed execution」三層。每個任務中，代理會檢索一組有邊界的相關脈絡，再運用於NemoClaw範例中。系統儲存兩類資訊：知識（人員、專案、優先順序、工作模式）與判斷（某項目是否需要關注、排序高低、使用者是否曾忽略它）。Markdown記憶頁儲存知識，SQLite帳本則記錄待辦事項、排序、修正與稽核事件——這樣的設計讓代理的判斷不會被寫回原始訊息，變成已讀標記或資料夾分類。文中特別強調：記憶頁可以告訴代理某位同事偏好用Slack溝通，但真正「發送訊息」這個動作，仍取決於憑證、工具權限、執行環境政策與使用者核准。脈絡可以「告知」一項行動，但無法「授權」它。

⚖️ **意圖優先於表面急迫性，且使用者永遠可以修正代理**

系統設計了一個intent gate（意圖閘門），將最高優先層保留給與使用者既定優先順序相關的待辦事項。在公開的recipe範例中，一則標榜「緊急」的費用政策確認信，排序仍低於一則語氣平和、但與使用者既定優先事項相關的請求——判斷關係由NemoClaw詮釋，但層級大小、溢出行為與排序邏輯由確定性程式碼強制執行。使用者也可以將某項待辦事項移到其他層級或直接忽略，決策會被後續的代理執行保留，並記錄在一份僅追加（append-only）的稽核紀錄中；重複出現的修正模式，還會更新成一份使用者可檢視、編輯或刪除的偏好政策，形成「代理判斷 → 使用者修正 → 稽核事件 → 偏好更新」的可視化回饋迴圈。

📊 **記憶架構讓準確率明顯提升，但也有取捨**

團隊在Agent Memory Benchmark上，比較「多輪檢索的agentic RAG基準」與「self model」，兩者皆使用NVIDIA Nemotron 3 Ultra：

| 指標 | 題數 | Agentic RAG基準 | Self model | 差異 |
|---|---|---|---|---|
| 整體準確率 | 186 | 82.8% | 90.9% | +8.1pp |
| 高難度題目 | 31 | 67.7% | 87.1% | +19.4pp |
| 追蹤隨時間變化的事實 | 5 | 60.0% | 100.0% | +40.0pp |
| 特定時間點推理 | 6 | 33.3% | 66.7% | +33.3pp |
| 實體消歧 | 15 | 66.7% | 86.7% | +20.0pp |
| 多來源綜合 | 73 | 87.7% | 94.5% | +6.8pp |
| 依語料忠實回答 | 13 | 100.0% | 92.3% | -7.7pp |
| 單跳查詢 | 30 | 86.7% | 83.3% | -3.3pp |
| 引用覆蓋率 | 186 | 92.5% | 97.8% | +5.4pp |

值得注意的是，self model在「依語料忠實回答」與「單跳查詢」兩項反而略遜於RAG基準，顯示記憶層雖擅長跨時間、跨來源的推理，卻可能在最簡單直接的查詢上引入些微雜訊。

🔒 **用NVIDIA OpenShell畫出安全邊界**

這套分層設計透過NemoClaw與NVIDIA OpenShell這個安全執行環境來落實：NemoClaw負責整合範例並管理其生命週期，OpenShell則在沙盒中執行代理，並對檔案系統、行程與網路存取提供治理與政策強制執行；用於推論服務與MCP連線的憑證則留在沙盒之外。文中強調，記憶與檢索到的內容只是模型的輸入，並非受信任的安全政策——即便代理誤解脈絡或被惡意指令誘導，仍會被限制在維運者定義的執行環境邊界內。

🎯 **實務啟示**

這套架構釋出為NVIDIA/nemoclaw-community GitHub repo中的開源recipe，內含結構化記憶schema、待辦事項帳本、排序邏輯、修正與稽核路徑、排程記憶維護、範例合成資料、離線走查與單元測試。目前的recipe僅聚焦記憶基礎，不會實際發送訊息或修改來源系統，也就是說要接上真實工作帳號，仍需要另外處理憑證、隱私與資料保留／刪除機制。對正在打造長期執行代理的團隊來說，「把證據、知識與行動分層」以及「讓使用者能修正並留下稽核軌跡」，是兩個可以直接借鏡的設計原則。

🔗 **來源**
- 標題：Building a Memory-Driven Agent with NVIDIA NemoClaw
- 作者／機構：Tanya Lenz, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/building-a-memory-driven-agent-with-nvidia-nemoclaw/

#NVIDIA #NemoClaw #AIAgents #AgentMemory #EnterpriseAI #RAG #OpenShell #Nemotron #LLMOps #AIArchitecture
