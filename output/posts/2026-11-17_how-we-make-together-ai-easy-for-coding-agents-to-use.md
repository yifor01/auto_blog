---
title: How we make Together AI easy for coding agents to use
source: Together AI
url: https://www.together.ai/blog/how-we-do-agent-evals-at-together-ai
model: claude-code/sonnet
generated_at: '2026-11-17T01:06:07.331553'
score: 84
---

📌 Together AI 怎麼確保 Coding Agent 真的會用自家平臺

TL;DR：Together AI 打造 agent evals 框架,量化 agent 使用其平臺時的成功率與踩雷點。

一個開發者手動串接 Together AI 上的正式環境推理,可能要花上好幾天甚至幾週;理論上,一個用 SDK 和 CLI 的 agent 只要幾分鐘就能完成同樣的事——但「理論上」是個危險的詞。Together AI 發現,他們根本不知道真正指向自家平臺的 agent,到底是順利完成任務,還是卡在某個環節、鑽進死胡同、甚至直接失敗並浪費大量 token。

🤔 **當開發者體驗變成「Agent體驗」**

文章指出一個越來越明顯的趨勢:隨著開發者把更多工作交給 agent,開發者體驗(DX)正逐漸等同於 agent 體驗(AX)——軟體對 agent 越友善,開發者就越容易把它整合進自己的產品與工作流程。GitHub 被文章拿來當作 AX 的典範案例:過去一年平臺活動成長三倍,2026 年約 40% 的 PR 由 agent 開出,背後靠的是 GitHub 出色的 API、CLI 與文件,讓 agent 極易上手。為了衡量自家平臺的 AX 到底如何,Together AI 建立了一套 agent evals 流程。

🧩 **先列出任務清單,再分三種設定測試**

Together AI 先整理出開發者在平臺上常做的任務清單,把每個任務寫成一句可以直接交給 agent 的 prompt。文章舉的例子是:「列出可用的 GPU 叢集地區與機型,印出最便宜的選項,並顯示你會用來預留一小時隨需執行的確切指令,但不要真的去預留它。」要通過這個測試,agent 必須找到最新的定價資訊、呼叫 regions API 列出可用地區、把兩者結合算出最便宜選項,並產出一條有效的 CLI 指令——這個 prompt 故意沒說「地區」和「價格」資訊放在兩個不同地方,因為一般使用者本來就不會預先知道,這正是容易讓人類與 agent 一起卡關的真實情境。

每個任務都會用三種設定各跑一次:
- Baseline:agent 只拿到 prompt,沒有任何特殊設定,模擬一般開發者的預設工作流程,可以使用預設工具(如上網抓文件),但不給任何特定的 MCP connector 或 skill。
- MCP:agent 透過 Together 的 MCP server 直接取得文件存取權,踩到障礙時能準確知道該去哪裡查。
- Skills:agent 拿到 Together skill package,裡面是專門寫給 agent 看的操作說明與範例。

完整的一輪評測,會讓每個任務在每種設定下,搭配三個模型各跑兩次,等於每個設定六次嘗試。文章提到 9 月 30 日那輪測試中,agent 在 215 次有評分的測試中通過了 192 次;其中 GPU 叢集任務在 baseline 設定下全部失敗,在 skills 設定下則全部通過。

🧩 **把流程自動化,並用LLM裁判打分**

一開始,Together AI 是手動開終端機、貼 prompt 進 Claude Code、觀察結果再重複,相當繁瑣。確定好系統架構後,他們把整套流程自動化:每個 agent 都在 Together sandbox 中執行,避免互相干擾或影響本機環境;GitHub Actions 負責啟動、設定、收尾與存結果;一個 proxy 負責攔截並記錄 agent 對 Together API 的每一次呼叫與回應。

每輪結束後,由一個 LLM 裁判審閱任務 prompt 與完整對話紀錄,給出三種判定之一:Pass(完全符合任務要求)、Incomplete(嘗試了但部分步驟未完成或未驗證)、Fail(agent 提早放棄、違反明確限制,或產出錯誤結果)。文中特別強調,失敗或不完整的判定本身不會告訴你問題出在 agent、API 還是缺乏證據,只會告訴你該從哪裡開始查;即使是通過的測試也值得檢視,因為 agent 有時能繞過令人困惑的回應硬撐完成任務,這類「硬撐成功」的案例正好能指出該優化哪些地方來提升 token 使用效率。為了讓審查更實際可行,他們還做了一個結果檢視工具,能並排比較不同模型與設定下的 prompt、使用的工具、拿到的回應,以及完整的 API 呼叫記錄。

📊 **案例:GPU叢集定價任務踩的兩個坑**

早期測試時,即使啟用 skills,Sonnet 4.6 在這個 GPU 叢集任務上 15 次嘗試只通過 4 次。事後分析發現,失敗的案例都出現同一個模式:Sonnet 把 CLI 文件裡的範例輸出(只列了一個地區和兩種 GPU 機型)誤當成即時庫存,還跳過了 regions 查詢,直接猜測它認為最便宜的選項,完全沒去查定價頁面。

問題其實出在 Together 自己身上:一是那份範例輸出沒有被標記清楚,沒有任何提示告訴 agent 需要去執行指令取得即時資料;二是他們的 skill 檔案連結到 GPU 叢集的行銷頁面,而不是定價表,導致 Sonnet 打開行銷頁面卻看不到真實價格,只能憑猜測給答案。同一段時期,能力更強的 Opus 4.8 在相同設定下 14 次嘗試通過 13 次——根據對話記錄,它注意到 list_regions 的回應裡沒有價格,於是持續搜尋直到在文件中找到定價資訊。文章特別點出,這正是為什麼一定要用能力較弱的模型測試:如果只用 Opus 測,團隊可能要花更久才會發現這個缺口。

為了修正問題,團隊把 GPU 叢集的 skill 從完整 skill package 中抽出來,寫一個更窄的 prompt 專門重現這個問題——用舊版 skill 測試時每次都會失敗,等於拿到了可靠的重現步驟,之後每次改版都能快速驗證。幾輪迭代後,他們只加了兩句話到 skill 檔案裡:指向即時 regions API(GET /v1/compute/regions 或 tg clusters list-regions --json)取得即時地區庫存與相容機型資訊,並連結到 GPU 叢集定價表取得目前的隨需與預留費率。

💡 **深入分析**

這個案例最值得注意的,不是「agent 犯了什麼錯」,而是錯誤的根源始終在文件與 skill 的設計上——範例輸出沒標示清楚、連結指向錯誤頁面。對平臺方而言,agent 的失敗其實是產品文件與 AX 設計缺陷的放大鏡,而用較弱的模型測試,正好能把這些缺陷暴露得更明顯。

🎯 **實務啟示**

如果你的平臺或 API 預期會被 agent 大量使用,值得仿照這套方法:列出真實使用場景的任務清單,用「無特殊設定 / 給文件存取 / 給專用 skill」三種配置做對照測試,刻意納入能力較弱的模型,並用自動化與 LLM 裁判讓評測可以重複執行、持續追蹤。AX 正在成為繼 DX 之後,API 與開發者工具必須認真對待的新維度。

🔗 **來源**
- 標題：How we make Together AI easy for coding agents to use
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/how-we-do-agent-evals-at-together-ai

#TogetherAI #AgentExperience #CodingAgent #DeveloperExperience #LLMEval #AIAgents #MCP #APIDesign #AgentTesting #GenerativeAI
