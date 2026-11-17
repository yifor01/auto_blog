---
title: 'Introducing the Databricks AI Index: The state of enterprise AI tokenomics'
source: Databricks
url: https://www.databricks.com/blog/introducing-databricks-ai-index-state-enterprise-ai-tokenomics
model: claude-code/sonnet
generated_at: '2026-11-17T01:06:07.331426'
score: 87
---

📌 Databricks AI Index：企業的AI帳單,正在往開放權重模型傾斜

TL;DR：Databricks 公開企業AI用量與成本數據,開放權重模型佔比四個月內翻三倍以上。

模型推陳出新的速度已經快到「每週就有一個新旗艦模型上市」,若把地區性實驗室也算進去,平均每 3.7 天就有一個新模型推出。在這種速度下,企業到底該選哪個模型、什麼時候該換,變得越來越難判斷。Databricks 選擇把自己內部的評測資料公開出來。

🤔 **一個彙整企業真實用量的公開資源**

Databricks 推出的 AI Index 結合兩種資料來源:一是來自 Unity Gateway 上超過 10,000 家企業(涵蓋數位原生公司、Fortune 500、Global 2000)的匿名用量與花費資料,包含流向 Anthropic、OpenAI 等外部供應商的流量;二是以 Databricks 內部 12,000 多名員工的真實 coding agent 工作流程(建立與審查 PR、調查問題、處理複雜開發任務)所持續更新的評測,並使用私有程式碼庫與保留的測試集來降低 benchmark 污染風險。

📊 **供應商版圖正在被打散**

文章提供的數字顯示出明顯的碎片化趨勢:
- 今年年中,多數企業主要仰賴少數幾個 Anthropic 模型;如今採用已分散到更多模型版本與供應商。
- OpenAI 的企業 token 流量份額曾因 6 系列的 Sol、Astra 模型成長明顯,但 Claude Opus 5.5 上市後,動能在六週內轉回 Anthropic——Opus 5.5 從佔 Anthropic 專有模型 token 的 7.2% 衝到 37.9%,帶動 Anthropic 整體份額從 57.6% 提升到 68.8%。
- 7 月時約 64% 使用 Unity Gateway 的企業只依賴單一模型供應商,到 11 月 2 日這個比例降到 28%,更多組織開始採用 2 家以上供應商的模型。
- 開放權重模型的企業 token 流量份額從 7 月的 7.3% 成長到 11 月的 30.9%,不到四個月翻了超過四倍。在 Databricks 的 coding 品質 benchmark 中,三個開放權重模型進入前十,其中 DeepSeek V4.1 與 GLM 5.3 並列第三,通過率皆為 93.1%。

💡 **同樣的分數,成本可能差 32 倍**

Databricks 內部導入新模型有一套「Day 1 rollout」流程,能在數天內評測新模型。文章提到,評估 Opus 5.5 時發現它比前代成本降低 29%(每個 session),這也是團隊決定把它設為 Claude Code 預設模型的依據。但評估 Opus 4.8 升級到 Opus 5 時,Databricks 比對 cost-quality Pareto frontier 並重播自家工作流程的記錄,結論是「這次升級的額外成本不值得」,因此選擇留在 Opus 4.8。

benchmark 本身也揭露了「分數相近、成本天差地別」的現象:GPT-6 Luna 與 Claude Opus 5.5 在 coding benchmark 都拿下 89.1% 的任務成功率,但 Luna 平均每個任務只要 0.05 美元,Opus 5.5 要 1.62 美元,相差約 32 倍。Gemini 3.8 Flash 的 token 單價雖低,卻因為平均每個任務要跑 140 個對話輪次,最終每個任務成本高達 11.97 美元,成為 benchmark 中最貴的模型之一——這說明低 token 單價不等於低總成本,模型完成任務所需的「工作量」同樣關鍵。

在成本與品質的頂端也有取捨:Claude Fable 5.1 以 96.0% 任務成功率排名第一,每任務成本 7.47 美元;Muse Wonder 以 94.9% 成功率、每任務僅 1.53 美元緊追在後。多出的 1.1 個百分點,代價是近五倍的成本——企業似乎也這麼判斷,Fable 5.1 的專有模型 token 份額在上市六週內從 5.5% 滑落到 0.6%。在成本效益前緣(cost-quality frontier)上,九個 AI 實驗室中共有五個模型、分別來自 OpenAI、DeepSeek、Meta、Anthropic 四個實驗室,被評為最佳的成功率與成本平衡點。

📊 **一小群重度用戶撐起大半帳單**

用戶層級的花費差異同樣懸殊:中位數用戶的 AI 花費僅 2.49 美元,第 99 百分位用戶卻高達 699.74 美元,相差約 281 倍。六週內中位數週花費從 1.10 美元翻倍以上,而第 90、99 百分位的花費則相對平穩,顯示一般用戶的 AI 使用量正在成長,但帳單主力仍集中在少數重度使用者身上。

🎯 **實務啟示**

模型排名本身不足以做決策,企業該評估的是「模型加 harness」的組合,並用自己真實的使用資料與追蹤記錄(trace)重播,去衡量效能與成本的取捨——這正是 Databricks 內部決定是否升級模型的方法。對於例行任務,便宜模型可能已經足夠;只有在高複雜度、高風險的工作上,才值得為額外的品質付出高成本。像 Unity Gateway 的 Smart Routing 這類智慧路由機制,可以依任務品質與成本需求自動配對模型。

🔗 **來源**
- 標題：Introducing the Databricks AI Index: The state of enterprise AI tokenomics
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/introducing-databricks-ai-index-state-enterprise-ai-tokenomics

#Databricks #AIIndex #EnterpriseAI #LLMCost #OpenWeightModels #CodingAgent #UnityGateway #AIAdoption #ModelBenchmark #Tokenomics
