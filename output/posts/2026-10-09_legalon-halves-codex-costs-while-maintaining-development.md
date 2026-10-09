---
title: LegalOn halves Codex costs while maintaining development speed
source: OpenAI Blog
url: https://openai.com/index/legalon-halves-codex-costs
model: claude-code/sonnet
generated_at: '2026-10-09T21:47:16.116816'
pinned: true
---

📌 【OpenAI 官方案例】LegalOn 靠模型配對砍 Codex 成本 65%

TL;DR：LegalOn 依任務指派 Astra、Sol、Luna 三款模型並策略性管理預算，在不拖慢開發速度下砍掉估計每日 Codex 花費的 65%。

同一套編碼代理工具，換個「派工」方式就能省下超過六成的運算花費，這是 LegalOn 的做法。

🤔 **開發速度與運算成本的拉扯**

法律科技公司 LegalOn 在用 OpenAI Codex 進行軟體開發時，面臨運算成本隨團隊用量上升的壓力，但又不想因此犧牲開發速度。

🧩 **依任務配對模型，而非一招打天下**

根據 OpenAI 公布的案例，LegalOn 採取兩個策略：一是「依任務配對模型」，將 Astra、Sol、Luna 三款模型分別對應到不同類型的開發任務；二是「策略性管理預算」，而不是讓所有任務統一使用同一個（通常也最貴）模型。

📊 **每日估計成本降 65%，開發速度不變**

這個做法讓 LegalOn 估算每日 Codex 花費下降 65%，同時維持原有的開發速度。

💡 **多模型調度正在成為 agentic coding 的常見手段**

把這個案例與 Asana 的案例放在一起看，會發現 OpenAI 目前釋出的 Codex 相關客戶故事，共同指向同一個工程實務：多模型組合調度（model routing）正在取代單一模型打天下的用法。把便宜、快速的模型留給高頻率、低風險的任務，把更強的模型留給關鍵決策，是控制 agentic coding 成本的核心手段之一。

⚠️ **素材未提供的細節**

素材並未說明 LegalOn 具體如何判斷任務該配對哪個模型，也沒有提供預算管理的實際工具或數字細節，這部分仍待更多公開資訊。

🎯 **實務啟示**

對使用 Codex 或類似編碼代理的團隊，值得評估是否能依任務複雜度與風險程度拆分不同模型，而不是讓所有 agent 呼叫都走向同一套模型設定。

🔗 **來源**
- 標題：LegalOn halves Codex costs while maintaining development speed
- 作者／機構：OpenAI
- 連結：https://openai.com/index/legalon-halves-codex-costs

#OpenAI #Codex #LegalOn #AIAgents #CostOptimization #ModelRouting #LegalTech #AgenticCoding #EnterpriseAI #DeveloperProductivity
