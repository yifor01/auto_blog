---
title: 5 production challenges in multi-agent systems and how Deep Insight solved
  them
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/5-production-challenges-in-multi-agent-systems-and-how-deep-insight-solved-them/
model: claude-code/sonnet
generated_at: '2026-10-22T20:46:46.098762'
score: 97
---

📌 Multi-agent demo 做得出來,production 卻卡關:AWS 怎麼拆解

TL;DR：AWS 用 Deep Insight 示範如何把多代理系統從 pilot 推進生產環境,關鍵是 Context Engineering 而非更多 prompt。

一個 agent 跑起來看起來很厲害,幾行 prompt、幾個 tool call 就能做出 demo。但真正要上線時,團隊常會發現同一個問題反覆出現:agent 不照業務邏輯走、跳過驗證步驟、漏掉邊界情況。調整 prompt、加範例、換模型,問題還是會回來。

🤔 **Agent 不是照腳本走的程式,是會自己判斷的系統**

這正是 AWS Solutions Architecture 團隊想點出的核心問題。Agent 不遵循固定指令序列,而是根據 context 自行判斷下一步,光靠寫更好的 prompt 不足以解決。團隊因此打造了 Deep Insight,一套生產級多代理系統,並透過三篇系列文章分享過程中應用 Anthropic 提出的 Context Engineering 技巧(多代理架構、結構化筆記、human-in-the-loop 等)的實務經驗,這篇是系列的第一篇,定義多代理系統上生產環境必須解決的五個核心挑戰,並說明技術堆疊的每一層如何應對,包括 Strands Agents SDK、Amazon Bedrock、Amazon Bedrock AgentCore、Application Load Balancer 與 AWS Fargate。

🧩 **八個 agent 分工,一份報告**

Deep Insight 的任務是把複雜的資料分析自動化成洞察報告。使用者上傳一份 CSV 檔與一句自然語言指令,一群各司其職的 agent——Coordinator、Planner、Plan Reviewer、Supervisor、Coder、Validator、Reporter、Tracker——協同完成載入資料、執行分析、產生圖表、驗證計算,最後輸出一份附帶引用來源的 .docx 報告。文中以一個虛構食品公司 Yummy Food 的廣告資料為例,給定資料檔與欄位定義檔,加上「從銷售與行銷角度分析,產生圖表與洞察,並產出 docx 報告」的指令,Deep Insight 會先生成分析計畫,交由使用者核准(human-in-the-loop)後才執行。

每個 agent 都在獨立的 context 中運作,只做自己專精的任務,並只把「壓縮後的結果」往下傳遞,而不是把整段對話歷史往下丟。Coordinator 負責路由使用者請求,遇到簡單問候直接回覆,遇到需要工具或多步推理的任務則交給 Planner。這裡有個值得注意的工程決策:Coordinator 只負責分類判斷,因此刻意選用輕量的 Claude Haiku,避免在簡單問候上也燒 Opus 等級的運算成本,同時換來更快的回應速度。Planner 接手後,把大任務拆成一步步的小任務,再交給各專職 agent 依序執行,讓每個 agent 的 context 維持在小範圍內。

架構上結合了 Strands Agents SDK 的兩種模式:Graph pattern 把執行順序定義成有方向性的圖,流程依序是 Coordinator → Planner → Plan Reviewer → Supervisor,並在使用者要求修改時,透過條件分支繞回 Planner,讓 HITL 與錯誤處理的複雜流程變得清晰可控;Agents-as-Tools pattern 則讓 Supervisor 只在需要時,把 Coder、Validator、Reporter、Tracker 當作工具呼叫,各自在獨立 context 中工作,只回傳結果,同時把 context 用量降到最低,又保留各自的專業分工。

🎯 **三種部署方式,同一套架構直接搬上生產**

Deep Insight 已在 GitHub 開源,附完整的架設指南,提供三種部署選項:Self-Hosted 版本透過 CLI 在本機執行,約 10 分鐘可設好,適合快速迭代與對每個 agent、prompt、流程的完整程式碼存取;Web 版本提供瀏覽器 UI,讓非開發者也能上傳資料、審核分析計畫、下載報告,不需寫程式;Managed AgentCore 版本則是生產部署選項,架構在 Amazon Bedrock AgentCore 之上,整套系統跑在私有 VPC 內,搭配獨立架設在 AWS Fargate 上的自訂 Code Interpreter,各使用者的 agent 在隔離環境中並行執行,適合需要 session 隔離與私有 VPC 部署的場景。三種部署方式共用同一套多代理架構,代表在開發環境驗證過的 agent,可以原樣部署到生產環境,不需要重新設計。

對正在把 multi-agent 系統推向生產的團隊,這篇文章的參考價值在於它把「prompt 工程」和「系統架構設計」拆開來看——當 agent 行為不穩定時,該檢視的往往是執行流程的圖結構與 context 分配方式,而不只是繼續調 prompt。

🔗 **來源**
- 標題：5 production challenges in multi-agent systems and how Deep Insight solved them
- 作者／機構：Yoonseo Kim，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/5-production-challenges-in-multi-agent-systems-and-how-deep-insight-solved-them/

#MultiAgent #ContextEngineering #AWS #BedrockAgentCore #AgentOps #LLMOps #ProductionAI #HumanInTheLoop #StrandsAgents #AIArchitecture
