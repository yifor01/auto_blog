---
title: Rewriting Prime Agent in Rust
source: Hacker News
url: https://www.primeintellect.ai/blog/prime-agent-rust
model: claude-code/sonnet
generated_at: '2026-10-10T20:44:14.729306'
score: 83
---

📌 兩千個AI Agent花兩週，把自己的程式碼庫從TypeScript搬到Rust

TL;DR：Prime Agent用2000+個agent組成的群體，自己重寫了自己的核心架構，人類只負責搭建驗證機制。

如果一個coding agent工具要「重寫自己」，誰來寫Code、誰來審查、誰來把關品質？Prime Intellect給出的答案是：全部交給agent群體，人類只搭驗證框架。Prime Agent自八月推出以來，下載量超過30萬次，處理超過8兆個token，而這次團隊選擇把整個產品從TypeScript改寫成Rust，並讓這次重寫本身成為一場多agent協作的壓力測試。

🤔 為什麼要從TypeScript換成Rust

團隊坦言TypeScript幫助Prime Agent快速上線，但它的型別是選用的，執行期就會消失；錯誤以未檢查的例外形式傳遞；CPU密集工作（如渲染、解析大型session）會跟鍵盤輸入搶同一個event loop；而且每個process都要負擔JavaScript runtime與垃圾回收的成本。Rust能提供效能（原生程式碼、無GC、worker process per session）、並行安全（Send/Sync trait讓編譯器檢查哪些資料能在執行緒間移動或共享）以及編譯期保證（exhaustive enum、ownership與lifetime排除整類bug，加上Clippy的pedantic lint規則）——這些特性在「程式碼大多由agent寫」的情境下特別重要。

🧩 四個agent角色，一套平行驗證的FSM流程

整個重寫由一個root agent主導，負責把工作拆成拓樸排序的任務清單。這個root agent本身不寫任何產品程式碼，專心監控每項任務、合併完成的工作，並與人類團隊討論優先順序。每個任務會依序經過四個agent角色：

- Planner：撰寫整體規格，包含功能設計、TypeScript版的ground-truth行為，以及對應的驗證邏輯（parity check）。
- Implementer：在獨立的worktree中寫Rust程式碼，讓功能能平行開發。
- Reviewer：用不同模型、在獨立context中「對抗式」審查PR，專門找出這段改動錯在哪裡。
- Verifier：在全新的Prime Sandbox中編譯並執行該功能的parity check與測試。

只要Review或Verify任一關卡失敗，任務就退回給Implementer重做，兩關都過才會合併。團隊設計了四種parity檢查：TUI parity（差分測試比對TS與Rust版的終端機畫面輸出，涵蓋啟動、slash選單、工具呼叫、compaction、agent視圖、session resume、subagent與crash recovery）、Harness parity（比對session transcript與送往模型供應商的請求）、Protocol parity（比對daemon protocol中的訊息型別）、Feature parity（agent逐一審查TS介面的每個元件，分類為matching/partial/missing）。

基礎設施上，所有orchestrator與其agent跑在兩臺8核心的on-demand CPU節點上，每臺可支援100多個並行的subagent與各自的CPython kernel；編譯、型別檢查與diff這類吃資源的工作則外包給Prime Sandbox，讓整個重寫可以高度平行化。

📊 兩週、兩千多個agent、超過2000億token

根據進度圖表，Rust Implementation階段動用了1,981個agent，耗用192.99B token；接著的Performance Hillclimb階段（跑真實benchmark與trace調效能、抓bug）用了228個agent，耗用35.70B token。到10月1日15:59為止，累計共2,209個agent、16,758則agent對agent訊息，總計228.70B token。

💡 重寫順帶換來的架構紅利

這次重寫也是重新設計架構的機會：程式碼拆成9個crate，依Cargo強制的單向依賴圖排列，TUI唯一的內部依賴是共享的types crate；最大的原始碼檔案從TypeScript版的約15,000行降到約2,500行，且沒有任何檔案超過5,000行（TS版有四個檔案超過這個門檔）。每個session跑在獨立的worker process底下，由一個小型supervisor管理，單一session的失敗不會波及其他session，session狀態也會落地到磁碟供重連後復原。transport、process control、file locking都被抽象成平臺特定介面，讓Windows支援只需要實作對應的trait即可，而不用重寫整個daemon。模型與MCP清單也改成執行期抓取的catalog，可以不用發新版本就上架新模型或plugin。等到主要RLM迴圈達成parity後，團隊更把重寫用的agent群自己也換到Rust版上跑,等於讓Rust版Prime Agent遞迴地改進自己。

⚠️ 差分測試只驗證「有跑到」的行為

團隊也坦言，自動化的parity check只能驗證它實際涵蓋到的行為路徑，真正剩下的bug與行為差異，大多是等到內部團隊把Rust版拿來日常使用後才被發現，這也指引了後續在可靠性與介面細節上的補完工作。

🎯 實務啟示

這套「Planner-Implementer-Reviewer-Verifier」的四角色FSM流程，本質上是把「生成」與「驗證」刻意拆成不同agent、不同context，降低agent審查自己程式碼的偏誤。對任何想用多agent做大規模程式碼重構或遷移的團隊而言，這組模式（加上可重複使用的parity check）或許比單純堆agent數量更值得借鏡。

🔗 來源
- 標題：Rewriting Prime Agent in Rust
- 作者／機構：Prime Intellect
- 連結：https://www.primeintellect.ai/blog/prime-agent-rust

#PrimeAgent #Rust #MultiAgent #CodingAgent #AgentOrchestration #SoftwareRewrite #AIEngineering #FiniteStateMachine #PrimeIntellect #AgentSwarm
