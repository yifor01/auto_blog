---
title: 'Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security
  Agents'
source: arXiv
url: http://arxiv.org/abs/2607.15263v1
score: 87
model: tencent/hy3:free
generated_at: '2026-07-18T07:37:00.301658'
---

📌 【arXiv 研究】安全代理評估不能只看成功率，還要算成本

TL;DR：以固定推論成本比較紅藍隊安全代理，揭示兩者不同的擴充套件特性與實用門檻。

大多數安全代理評測都在「預算管夠」的前提下測峰值攻擊能力，但真實營運環境裡，每一次推理步驟、工具呼叫、遙測查詢都在燒錢。這篇論文主張：不看成本的成功率，只是半套評估。

🤔 **現有評測忽略營運成本**

常見的安全代理評估聚焦於漏洞發現、 exploit 開發、滲透測試與 CTF 完成率，並在寬鬆的 inference budget 下測量最佳攻擊能力。作者指出，這類測量有用但不完整，因為在實際安全場景中，每個 reasoning step、tool call、telemetry query 與 enrichment request 都會消耗預算。

🧩 **用成本—成功率視角評估紅藍隊任務**

研究以 cost-success lens 評估語言模型安全代理，涵蓋：
- 攻擊面：Cybench 挑戰（offensive）
- 防禦面：Splunk BOTS v1 調查挑戰（defensive）

方法上不僅回報最佳情況成功率，而是在固定成本層級下比較不同模型，並將效能依 inference spend 與 tool spend 拆解分析。

📊 **紅隊與藍隊呈現不同擴充套件特性**

- 攻擊型 CTF 表現隨 test-time compute 增加而提升；擴充套件後的開放權重（open-weight）模型可逼近前沿專有系統，且保持成本競爭力。
- 防禦型 SOC 調查則不以此方式擴充套件：成功更依賴紀律化的工具使用、telemetry 導航與選擇性 enrichment，而非單純堆疊推理預算。

⚠️ **基準應納入經濟效率與實務適配**

作者主張安全代理基準應同時測量經濟效率（economic efficiency）與 operational fit，而非僅看任務成功率。成本導向、SOC-native 的評估能更清楚呈現哪些模型當下真正實用、以及防禦代理還需在何處改進。

💡 **互動式結果網站已公開**

論文提供一個互動網站（https://evals.frontier.security）展示其評測結果，供讀者實際瀏覽不同模型在成本與成功率上的表現。

🎯 **評測框架應轉向成本意識**

對開發或採購安全代理的團隊而言，這篇提醒我們：在固定預算下比較模型，比「最佳案例成功率」更有參考價值；特別是防禦場景，應優先考察工具使用紀律與遙測導航能力，而非盲目加大推理預算。

🔗 **來源**
- 標題：Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents
- 作者／機構：Paul Kassianik, Blaine Nelson, Yaron Singer
- 連結：http://arxiv.org/abs/2607.15263v1

#SecurityAgents #CostAwareEvaluation #RedTeam #BlueTeam #LLM #Cybench #SOC #Benchmark #OffensiveSecurity #DefensiveSecurity
