---
title: 'Smart Routing in Unity AI Gateway: Match frontier quality with 30%+ lower
  cost per task'
source: Databricks
url: https://www.databricks.com/blog/smart-routing-unity-ai-gateway-match-frontier-quality-30-lower-cost-task
model: claude-code/sonnet
generated_at: '2026-08-14T07:32:27.863075'
score: 86
---

📌 別再手動挑模型：Unity AI Gateway 用 Smart Routing 省下大筆程式碼開銷

TL;DR：任務自動配對最適模型，內部省 35%、公開基準省 56% 成本。

2026 年才過一半，已經有 33 個新模型問世。多到讓人選擇困難，於是很多工程師乾脆放棄挑選，直接把最貴、效果最強的模型開到最高推理力度，一路用到底。Databricks 認為這是浪費，因為他們先前benchmark 自家程式碼庫時發現，模型能力其實會分群成不同層級，而修 flag、單檔編輯、範圍明確的 bug fix 這類日常工作，根本用不到最頂級的模型。

🤔 **問題：選擇太多，大家乾脆都用最貴的**

只是換用便宜模型就能省下超過 50% 成本，但要工程師自己判斷「這個任務該用哪個模型」既耗時又容易出錯。Databricks 因此在 Unity AI Gateway 推出新的成本控制機制 Smart Routing（Beta），直接在 Claude Code 與 Codex 裡運作，把「選模型」這件事從使用者手上拿掉。

🧩 **怎麼判斷任務難度：先分類，再決定升降級**

路由決策的關鍵時機點是「什麼時候該做路由判斷」。Databricks 選擇了 task-aware routing，也就是在任務開始時一次性決定，藉此保留 cache 效率，同時把每個 coding 任務配對到合適的模型與 harness。具體流程是：先用一個便宜、低延遲的模型讀取任務描述，標記出幾項語意欄位，包括系統哪個部分要改、prompt 帶有什麼程式碼證據（片段、traceback，還是完全沒有）、失敗模式為何、修復範圍有多局部、屬於哪種專案類型；再從這些標籤推導出任務類型家族與語言家族。路由器預設使用中等規模模型，再依標籤決定要往上升級到更貴的前沿模型，還是往下降級到更便宜的模型。這套單一策略目前套用在所有任務上，尚未做個人化。

📊 **成效：內部省 35%，公開基準省 56%**

在 Databricks 自家內部 coding workload 上，Smart Routing 的整體表現超越任何單一模型，成本僅為 Opus 5 每個任務成本的 65%；在公開 benchmark 上，Smart Routing 在效能上打平 Opus 5，成本卻不到一半。內部基準測到 35% 的成本節省，公開 coding benchmark 則達到 56%，顯示成果具有一定的泛化能力。

💡 **Omnigent：路由不只選模型，也選 harness**

Databricks 同時推出 Omnigent，一個 coding agent 的 meta-harness，讓 Smart Routing 不只決定模型，也決定要用哪套 coding harness。開發者可以直接選用 Smart Routing 取代手動指定 harness，Omnigent 會自動同時選好 harness 與模型。這個設計也延伸到 sub-agent：所有 sub-agent 的啟動都會經過 Smart Routing API，因此同一個任務裡，規劃階段與平行的 sub-agent 工作可以各自拿到不同的路由決策，例如把大型程式碼庫的摘要工作路由到便宜模型，架構設計則交給更貴的模型。

⚠️ **早期挑戰：Benchmark 資料跟真實使用行為對不上**

Databricks 坦言，目前最大的挑戰是 benchmark 資料不可靠。Benchmark 任務通常是自成一體、描述清楚的工作陳述，路由器在這類任務上表現良好，但真實的 coding session 往往雜亂得多。他們也強調，路由不能只優化成本，必須同時兼顧開發者體驗，因此把所有 coding session 的追蹤紀錄記入 Unity Catalog（並施以嚴格的存取政策與標籤治理），用 AI 模型加上人工審查來評估路由器的改動效果。

🎯 **實務啟示**

如果你的團隊也在用 coding agent，與其手動幫每個任務挑模型，不如思考「任務分類 → 路由決策」這套機制能不能套進既有工作流程。Databricks 的經驗也提醒一個容易被忽略的方向：路由不是只用來省錢，同樣的機制也能在任務真的需要時，果斷升級到更貴、更強的模型，把稀缺的前沿算力留給真正需要的工作。

🔗 **來源**
- 標題：Smart Routing in Unity AI Gateway: Match frontier quality with 30%+ lower cost per task
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/smart-routing-unity-ai-gateway-match-frontier-quality-30-lower-cost-task

#Databricks #UnityAIGateway #SmartRouting #LLM #CodingAgents #ClaudeCode #Codex #CostOptimization #Omnigent #AIInfrastructure
