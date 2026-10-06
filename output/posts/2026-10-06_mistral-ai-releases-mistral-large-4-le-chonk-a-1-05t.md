---
title: 'Mistral AI Releases Mistral Large 4 (Le Chonk): A 1.05T Parameter Multimodal
  MoE Model'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/06/mistral-ai-releases-mistral-large-4-le-chonk-a-1-05t-parameter-open-weight-multimodal-moe/
model: claude-code/sonnet
generated_at: '2026-10-06T21:51:00.654537'
score: 106
---

📌 Mistral Large 4：1.05 兆參數,資安評測碾壓對手

TL;DR：Mistral 發表 1.05T 參數 MoE 模型 Le Chonk,資安 benchmark 大幅領先,但權重要等到月底才釋出。

多個閉源前沿模型在 CyberGym-E2E 上幾乎拿零分,原因不是能力不足,而是直接拒絕任務。Mistral Large 4 反而在同一個 benchmark 上拿下 82%——這個對比,正是 Mistral 這次發表想凸顯的重點。

🤔 **公開預覽上線,權重月底才到**

Mistral AI 於 2026 年 10 月 6 日公開發表 Mistral Large 4(內部代號 Le Chonk)的 public preview。根據官方模型文件,這是一個 granular Mixture-of-Experts 模型,總參數量 1.05 兆,每個 token 僅啟用 490 億參數,搭配 16 億參數的視覺編碼器,支援 1M token 的上下文視窗。模型從零開始訓練,使用 Mistral 自家歐洲資料中心內的 3,800 張 NVIDIA Grace Blackwell GPU。API 目前已上線,輸入 $1.36/1M token、輸出 $4.18/1M token,但權重要到 10 月底才會釋出,目前還無法自行架設。

🧩 **只有 4.7% 參數被啟用,但記憶體還是要吃滿 1.05T**

ML4 是一個混合指令遵循與推理能力的 MoE 模型,原生支援影像輸入。每個 token 僅啟用約 4.7% 的權重,這是一個兆級參數模型能以中階價位提供服務的關鍵;但完整的 1.05T 參數仍需全部載入記憶體,啟用比例只決定運算量,不代表硬體需求會變低。Mistral 目前尚未公布專家數量、top-k 路由機制或層數配置等細節,官方表示這些會在權重釋出時一併公開。訓練資料涵蓋超過 160 種語言,包括所有歐盟官方語言。

📊 **資安評測亮眼,agentic coding 數據尚待獨立驗證**

| 項目 | 指標 | 分數 |
|---|---|---|
| 資安 | Cybench | 93% |
| 資安 | CyberGym-E2E | 82% |
| Agentic Coding | DeepSWE v1.1 | 61.7% |
| Agentic Coding | SWE-Atlas-QnA | 59.4% |
| Agentic Coding | Terminal-Bench 4.0 | 28.3% |
| Agentic Coding | Artificial Analysis Coding Agent Index(綜合) | 49.8% |
| 安全性 | Lakera B3(抵禦攻擊比例) | 93.3% |
| 安全性 | KORABench(滿分 2.0) | 1.691 |

在資安項目上,Mistral 表示 ML4 在 Artificial Analysis Cyber Index 上排進全球前五,更值得注意的是官方指出:好幾個閉源前沿模型在 CyberGym-E2E 上幾乎零分,原因是直接拒絕這類任務——而重現漏洞以證明其真實存在,本就是防禦性資安工作的標準流程,供應商層級的拒答反而會卡住這類工作。Agentic coding 的數據方面,Mistral 說明這些是在官方測試框架(harness)公開前私下評測的結果,因此目前還無法獨立重現。

比較實在的訊號來自與 Surge AI 合作進行的盲測人工評分:專業標註員給 ML4 Preview 打了 5 分中的 3.74 分,在受測的 5 個模型中排第二,領先 GLM-5.3(3.60 分)與 Kimi K3(3.59 分),但落後 Claude Opus 5 的 4.22 分。

⚠️ **權重未發、架構未公開、部分數據待驗證**

目前權重尚未釋出,自行架設仍要等到 10 月底;expert 數量、路由機制等架構細節也要等權重釋出才會公開;agentic coding 的評測結果是私下跑的,尚無法被第三方獨立重現。

🎯 **對工程師的啟示**

如果你的場景涉及長上下文的 agent loop,$0.14/1M token 的快取輸入價格值得注意,會明顯改變多輪 agentic 呼叫的成本結構。而如果你的應用場景是防禦性資安研究(如重現漏洞驗證),ML4 不會因為任務敏感就直接拒答,這點與部分閉源模型形成明顯差異,值得實際測試看看是否符合需求。至於想自架的團隊,目前還得再等權重正式釋出。

🔗 **來源**
- 標題：Mistral AI Releases Mistral Large 4 (Le Chonk): A 1.05T Parameter Multimodal MoE Model
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/06/mistral-ai-releases-mistral-large-4-le-chonk-a-1-05t-parameter-open-weight-multimodal-moe/

#MistralAI #MistralLarge4 #MoE #LLM #Cybersecurity #AgenticCoding #OpenWeightAI #AIBenchmark #EuropeanAI #MultimodalLLM
