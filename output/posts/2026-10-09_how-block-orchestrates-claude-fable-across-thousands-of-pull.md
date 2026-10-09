---
title: How Block orchestrates Claude Fable across thousands of pull requests
source: Claude Blog
url: https://claude.com/resources/articles/how-block-orchestrates-claude-fable-across-thousands-of-pull-requests
model: claude-code/sonnet
generated_at: '2026-10-09T21:48:31.128097'
pinned: true
---

📌 Block 用 Claude Fable 指揮上千個 PR 的遷移戰

TL;DR：Block 讓 Claude Fable 5 當程式碼遷移的總指揮，自己做架構決策、再分派給數十個 Opus／Sonnet 執行細節，一次遷移能處理上千個 PR。

一次大型程式碼遷移,動輒橫跨多個 repo、數百萬行程式碼、數千個 pull request。過去這種規模的工作,只能靠人類工程師一個個盯著改,模型頂多同時啃一兩個 PR。Block 的 AI 能力負責人 Bradley Axen 在接受 Anthropic 採訪時說,這件事在 2026 年終於發生了轉變:人類負責掌舵,Claude Fable 負責指揮全局。

🤔 **從「寫程式碼」到「設計遷移本身」**

Block 打造 Square、Cash App 等協助企業與個人參與經濟活動的工具。Bradley Axen 帶領的團隊除了打造端對端 AI 產品,也開發了 Buzz,一套開源的人類與 agent 協作工作空間,並與 Square、Cash App 團隊合作建置面向客戶的 AI 功能。

Axen 指出,2025 年像 Claude Code 這類工具雖然已經出現,但仍需要大量人工介入,問題必須被切得很小、很規整,模型才能真正發揮。隨著模型愈來愈聰明,工程師的工作重心也跟著轉移:從實際動手改程式碼,變成設計遷移本身、檢視 agent 的行為、以及打造更多面向客戶的功能。

🧩 **一個 Fable 指揮,數十個小模型動手**

Block 描述的 orchestration 模式是這樣運作的:人類工程師先把方向定下來,Claude Fable 負責高層級的設計工作,包括資料模型、API 規格、演算法;接著 Fable 會指揮多達數十個更划算的小模型(像是 Opus 或 Sonnet),去完成實際的檔案編輯與測試執行等個別任務。

Axen 特別提到經濟效益:早期結果顯示,orchestrator 會把 frontier 等級的 token 用在複雜的前期規劃上,之後再把更高比例的 token 導向較小的 worker 模型,品質卻沒有因此下滑。這整套流程跑在 Buzz 上,讓人類與 AI agent 在共用的頻道與討論串裡並肩工作,團隊也因此對遷移進度有很好的可見度。

📊 **一次遷移,合併上千個 PR**

Axen 舉例,在某次遷移中,團隊可能會合併一千個由 Fable 協調完成的 pull request。他認為這是 Fable 推出後帶來的「階段性跳躍」:在那之前,你得把問題切得非常規整,frontier 模型才能真正發揮;Fable 出現後,團隊能一次處理的問題規模直接跳了一個等級。

另一個被他視為最難問題的場景,是維護一個規模在百萬行程式碼左右的既有系統。由於團隊出貨的 PR 比以前多,技術債累積的速度也比以前快,Block 現在讓 agent 每天或每週對整個 codebase 做一次巡檢,問「這裡現在狀況如何?有什麼該清理或整合的?」

💡 **模型選擇不再只有一個答案**

Axen 說,這是他記得第一次,「用最 frontier 的模型 100% 的時間」不再是正確答案。現在團隊更多在討論模型效率:Fable 的 frontier 智能最適合用在處理大問題上,細節則交給較小的模型補完。他甚至把 effort 等級也納入同一張決策表裡:同一個模型在 low 跟 xhigh 效果可能差很大,Fable 在 low 效果上甚至可能優於另一個模型在 xhigh。因此團隊會針對每個使用案例,逐一 benchmark 每個模型搭配每個 effort 等級的表現,目標是得出清楚的建議,例如「這類任務預設用某模型搭配 high effort」,並盡量把這個判斷自動化成工具,也就是他們正在打造的 auto-selector。

Block 讓所有技術職位的員工都能完整存取最前沿的模型,因為公司策略就是始終站在能力邊界上工作。但 Axen 也坦言,用 Fable 去修一個 README 的拼字錯誤是很浪費資源的用法,所以才需要更好的系統來建議「什麼任務該用什麼模型」。

⚠️ **合併主幹與上線部署,永遠留給人類**

即便 agent 的自主性已經走得很遠,Block 仍劃出一條清楚的紅線:合併到 main 分支、以及部署到生產環境,一律由人決定,相關的 feature flag 變更也不例外。Agent 可以修改程式碼,但那些變更必須通過安全檢查,接著還要有兩名人類批准才能部署。Axen 強調,這道雙重審核機制讓 LLM 不可能獨自把這類變更推上線。

🎯 **實務啟示**

Block 的經驗呈現出一個清晰的分工模式:frontier 模型做規劃與架構決策,較小、較便宜的模型做執行細節,人類保留對關鍵路徑(合併主幹、生產部署)的最終否決權。對正在導入 agentic 工作流的團隊來說,值得借鏡的不只是「用更強的模型」,而是建立一套能評估「哪個任務該配哪個模型、哪個 effort 等級」的機制,並把關鍵的人工審核節點明確地留在流程裡。

🔗 **來源**
- 標題:How Block orchestrates Claude Fable across thousands of pull requests
- 作者／機構:Anthropic(Claude Blog)
- 連結:https://claude.com/resources/articles/how-block-orchestrates-claude-fable-across-thousands-of-pull-requests

#ClaudeFable #Anthropic #AIOrchestration #CodeMigration #AgenticAI #Block #SquareCashApp #LLMEngineering #ModelSelection #AIatScale
