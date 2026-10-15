---
title: 'CopilotKit Releases CLiF: A Continual Learning Platform That Turns Agent Traces
  and User Actions into Skills, Evals, and Fine-Tuning Data'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/15/copilotkit-releases-clif-a-continual-learning-platform-that-turns-agent-traces-and-user-actions-into-skills-evals-and-fine-tuning-data/
model: claude-code/sonnet
generated_at: '2026-10-15T20:53:31.634669'
score: 81
---

📌 把使用者的真實操作，教回給 Agent

TL;DR：CopilotKit 推出早期產品 CLiF，用 AG-UI 協定同時記錄 agent 與使用者行為，自動生成技能、評測與微調資料。

🎣 多數團隊以為 agent 做不好任務是因為 prompt 寫得不夠細，但真正知道「正確步驟該怎麼走」的人，其實每天都在產品裡操作，只是這些動作從來沒被記錄成 agent 能讀懂的格式。

🤔 **Tracing 看得到 agent，看不到使用者怎麼做對**

目前多數 agent observability 工具聚焦在 agent 本身：prompt、tool call、模型輸出，這能看出 agent 哪裡做錯，卻看不到正確路徑長什麼樣子。另一邊的 product analytics 則記錄點擊、流程轉換與 session replay，但這些資料是為了給人看儀表板，不是為了教 agent 做事或測試 agent。CopilotKit 觀察到，在大部分生產環境裡，這兩種資料從未出現在同一條時間軸上。

🧩 **核心原語：full-stack trajectory**

CLiF 是 CopilotKit Intelligence 的一部分，建立在單一原語之上：full-stack trajectory。它透過 CopilotKit 自家開發的開放協定 AG-UI（Agent-User Interaction Protocol）擷取，因為 AG-UI 本身就架在 agent 與使用者介面之間，所以能同時看到雙方的行為，並把一次使用者 session 整理成一條可以逐步重播的軌跡，點擊、伺服器請求、agent 訊息依照發生順序排列。

CopilotKit 把學習迴圈拆成四個階段：
1. **Capture**：軌跡依照 getTrajectoryLearningContainerIds callback 被分派到不同的 learning container（例如帳務支援、新用戶導覽各自一個），每個 container 只從自己的 session 學習。
2. **Find patterns**：當 container 累積的新 session 數達到門檻，分析會自動排程執行（也能手動觸發），從凍結的 session 快照中找出重複出現的請求與「使用者悄悄繞過的摩擦點」，每一個 Insight 都附上引用的事件與原始軌跡連結。
3. **Review**：若證據支持一個可重複使用的教訓，CLiF 會提議寫成一份 SKILL.md，但分析服務自己不能發布，必須由人在 Intelligence UI 或 CLI 核准或拒絕，已發布的技能有版本號，也能隨時下架。
4. **Deliver & export**：技能發布後 agent 不需重新部署就能取得，也可以把 agent 鎖定在固定的技能版本上；其他 agent 或 MCP server 則能用 copilotkit skills download <container> --output <dir> 把技能下載成純檔案，原始軌跡本身也能從 Intelligence 儀表板匯出成事件資料。

💡 **技能只是其中一個產出**

同一批軌跡在 early access 階段還會產出評測候選案例與微調資料集，四種產出都能匯出接進團隊現有的 eval 與觀測工具，CopilotKit 的立場是：不需要換掉現有工具鏈，CLiF 補的是這些工具一直缺的資料。在 agent 端，CLiF 建立在 CopilotKit Intelligence 既有的 Automatic Learning 能力之上，透過 AG-UI Streams 完整保存每一次對話（訊息、tool call、生成式 UI、state、審批、檔案），開發者用 getLearningContainerId callback 決定哪些對話算數，也能從既有的 LangGraph Server 或 LangSmith Deployment 匯入歷史對話，不必從零開始。技能的傳遞透過 LangGraph（Python / TypeScript）、Mastra、Google ADK、Microsoft Agent Framework 與 CopilotKit 內建 agent 的 adapter 完成，adapter 會加上一個技能目錄與 copilotkit_load_skill、copilotkit_read_skill_file 兩個工具，模型在任務需要時自行載入；開發者預先寫好的指令仍具有最高優先權，技能不能覆寫 agent 的角色、安全規則或工具限制。

⚠️ **目前所有說法都來自 CopilotKit 自己**

素材中並未提供獨立第三方的評測數據或量化效果，CLiF 也仍在 early access 階段，它要解決的問題（agent 與使用者行為資料不在同一時間軸）確實存在，但實際抓取的「摩擦點訊號」品質如何、資料隱私與安全如何處理，都需要團隊自己接進去後驗證。

🎯 **實務啟示**

如果團隊已經在用 CopilotKit 或 AG-UI 架 agent，這套 trajectory capture 的思路值得評估：比起不斷手寫 eval case，從使用者已經在做的事情裡挖出可重複使用的技能，可能是更省力的路徑；但技能不能覆寫安全規則這個設計，也提醒我們：自動學到的知識，終究要有人把關才能上線。

🔗 **來源**
- 標題：CopilotKit Releases CLiF: A Continual Learning Platform That Turns Agent Traces and User Actions into Skills, Evals, and Fine-Tuning Data
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/10/15/copilotkit-releases-clif-a-continual-learning-platform-that-turns-agent-traces-and-user-actions-into-skills-evals-and-fine-tuning-data/

#CopilotKit #AgentObservability #ContinualLearning #AGUI #AIAgents #SkillLearning #FineTuning #LLMEval #OpenSource #AgenticAI
