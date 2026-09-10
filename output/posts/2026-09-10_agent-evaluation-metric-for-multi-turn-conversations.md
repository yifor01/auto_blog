---
title: Agent Evaluation Metric for multi-turn conversations
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/agent-evaluation-metric-for-multi-turn-conversations/
model: claude-code/sonnet
generated_at: '2026-09-10T19:58:02.898776'
score: 97
---

📌 多輪 Agent 出錯,問題到底出在哪一輪?

TL;DR:AWS 提出 AEM,把多輪 agent 正確性拆到逐輪可溯源。

🎣 想像一個五輪對話,使用者請企業助理產出一份銷售報表,再逐步微調。第二輪,agent 選對了動作,卻把參數填成「profit」而不是「revenue」。這個錯誤沒有立刻爆炸,而是安靜地滲透進後續每一輪。如果你只看最終結果,你只會看到「這次對話失敗了」,卻完全看不出問題其實只出在其中一輪。

🤔 背景:整體評分為什麼抓不到級聯錯誤

多輪 agent 的失敗模式,是單輪評估看不到的:一個早期的小錯誤會悄悄污染後面每一輪。任務層級的評估只檢查最終結果,把整段互動標記為失敗,卻沒揭露其實只有一輪需要修正。這正是核心問題所在:多輪 agentic 對話裡的錯誤會級聯,而任務結果層級的評估分不出根因與其下游效應。目前多數 agent 評估工具採整體式評分,提供目標達成度評分與 LLM-as-judge 品質評估,部分工具還加上 trace 層級的根因分析,這些都有價值,但共享同一個框架:把 agent 品質當成單一訊號,而不是拆解成可獨立追蹤的組成部分。知道 agent「目標達成率 70%」,並不能告訴你失敗是事實錯誤、資訊缺漏,還是工具選錯,單一分數也無法隨著需求成長,乾淨地擴充到新的評估維度。

🧩 方法:把正確性拆成兩個可獨立量測的子指標

AWS 提出的 Agent Evaluation Metric(AEM)把 agent 品質定義為由具名、可獨立量測的子指標組成的複合指標。這篇文章先聚焦第一個維度:正確性(correctness),用逐輪(turn-level)的方式評估。一輪對話要嘛是 response turn(agent 回覆使用者),要嘛是 action turn(agent 呼叫工具),兩者共用同一套評估層級。

正確性由兩個子指標組成:completeness(完整性)與 truthfulness(真實性)。對 response turn 而言,completeness 問「回覆是否涵蓋了完整的查詢」,truthfulness 問「內容是否符合事實」。同一套組合套用在 action turn 上:completeness 檢查參數 key 是否齊全(structural check),truthfulness 檢查參數 value 是否語意正確。兩者都建立在一個結構性檢查之上:agent 是否選對了工具與動作。

在這篇文章中,每一輪的正確性以二元(pass/fail)方式判定,並附上具體的失敗原因,指出是哪個子指標、哪個欄位出錯;同一套拆解方式也能延伸成更細緻、對個別 claim 或欄位做連續分數評分。把整段對話組合起來,AEM 分數就是通過的輪次比例。因為分數是依子指標拆解的,一旦分數下滑,你能立刻看出是 truthfulness 還是 completeness 拖累了整體,而不只是「正確性下降了」這種模糊訊息。

兩個子指標都依賴語意比對,而非精確字串比對:「New York City」與「NYC」語意相同,「Q3 2024 revenue」與「third quarter revenue figures for 2024」傳達同樣的資訊,精確比對在這裡太脆弱。語意相似度評分器可以是基於 embedding 的相似度檢查(快、便宜),也可以是 LLM-as-judge(更細膩但評分過程不透明)。門檻值決定判定的嚴格程度:門檻設高能抓到真正的錯誤,但也可能誤判語意相同的內容;門檻設低則較寬鬆。文章中的 0.5 是一個中性的起始預設值,而非調校過的最終值,實際數值取決於應用場景對偽陽性與偽陰性的容忍度。

Completeness 對 response turn 採語意檢查(回覆有沒有涵蓋完整問題),對 action turn 則採結構性檢查(必要參數 key 是否齊全)。回傳的 missing 與 extra 參數集合會直接餵進失敗分類:非空的 missing 集合產生 missing_parameters 失敗,非空的 extra 集合產生 extra_parameters 失敗,精準指出是哪個參數出了問題。

組合分數的規則本身也是可替換的設計選擇。這篇文章預設用「通過輪次的無加權平均」,但也提到其他同樣合理的規則:加權平均可以給成本較高的輪次更高權重;gating 規則可以讓單一關鍵輪次的失敗直接封頂整體分數;每個子指標也可以設定各自獨立的門檻。整個組合函式被設計成可插拔的。當一輪失敗時,系統會給出具體的失敗原因,精準指出出錯的地方;這套失敗分類同時涵蓋 response turn 與 action turn 的失敗類型,結構性檢查(工具與動作選擇)只適用於有呼叫工具的輪次。

⚠️ 限制:門檻值仍需依場景調整

文章明白指出,語意相似度門檻的 0.5 只是一個中性的起始值,不是調校過的定論,不同領域對「偽陽性」與「偽陰性」的容忍度不同,實際部署前仍需要依自己的資料調整這個門檻。

🎯 實務啟示:別再用整段對話的成敗做監控

如果你的團隊正在維運多輪 agent,而目前只靠「整段對話成功/失敗」這種粗粒度指標做監控,AEM 的拆解方式提供了一個更可操作的除錯路徑:與其在 dashboard 上看著一個模糊下滑的成功率乾著急,不如把正確性拆成 completeness 與 truthfulness,逐輪追蹤,直接定位是哪一輪、哪個欄位出的錯。這套「拆解-評估-組合」的模式,文章也提到可以延伸到安全性、指令保留度、推理深度等新維度,值得作為 agent 評估框架的設計參考。

🔗 來源
- 標題:Agent Evaluation Metric for multi-turn conversations
- 作者/機構:Surafel Lakew, AWS ML Blog
- 連結:https://aws.amazon.com/blogs/machine-learning/agent-evaluation-metric-for-multi-turn-conversations/

#AgentEvaluation #MultiTurnAgents #LLMEval #AIAgents #AWS #EvaluationMetrics #ToolCalling #AgenticAI #MachineLearning #LLMOps
