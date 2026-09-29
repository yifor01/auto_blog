---
title: 'Google Research Open-Sources RRSI: AI Agents That Improve Their Own Harness
  Without Overfitting'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/29/google-research-open-sources-rrsi-ai-agents-that-improve-their-own-harness-without-overfitting/
model: claude-code/sonnet
generated_at: '2026-09-29T21:37:22.594281'
score: 109
---

📌 【Google Research】RRSI 開源:讓 Agent 修改自己的 Harness 卻不作弊

TL;DR：RRSI 讓 LLM agent 自行改寫 prompt、工具與流程,用正規化避免針對單一評測過擬合,程式碼已開源。

讓 AI agent 自己重寫操作手冊,聽起來像是危險的權限開放,因為它很可能只是學會怎麼在考卷上拿高分——RRSI 想解決的正是這個問題。

🤔 自我改良的 Harness,如何避免變成應試教育

Google Cloud AI Research 與 UNC-Chapel Hill、Stanford、Washington University in St. Louis 合作,釋出 RRSI(Regularized Recursive Self-Improvement)。它讓 LLM agent 重寫自己的 harness,包括 prompt、工具、記憶、控制流程與子 agent,而模型權重本身不變。問題在於,harness 演化迴圈的作法是提出修改、在固定的 evolve set 上評分、保留贏家,而同一批任務會被重複使用,迴圈很容易記住這些任務。研究團隊將這類失敗歸納成三種模式:針對特定 benchmark 過度擬合、追逐雜訊,以及複雜度不斷累積,每一種都會拉大 evolve set 分數與實際遷移表現之間的落差。

🧩 不是限制修改內容,而是正規化搜尋過程本身

RRSI 的做法是保持 harness 的每個元件都可編輯,但對搜尋過程本身加上正規化限制。研究團隊把這些機制類比為經典的正規化方法:編輯預算對應 L0,修剪機制對應 Lasso(L1),成本規則對應 Ridge(L2)。

🧩 怎麼用

程式碼採 Apache 2.0 授權,需要 Python 3.10 以上環境,並接受任意 LiteLLM 模型字串,預設假設在 Vertex AI 上使用 Claude Opus 4.8。

📊 六個 held-out 分割全數進步,token 用量也更省

在全部 6 個 held-out 分割上,RRSI 都帶來進步。以 Gemini 3.5 Flash 作為 policy 模型時,Terminal-Bench 2.1 從 64.6 提升到 78.7,SWE-bench Verified 從 76.8 提升到 79.0。產生出來的 harness 也更精簡:在 agentic workspace instance 上,RRSI 每次試驗用掉 2.42M policy token,未加正規化的演化版本則用掉 3.80M。值得注意的是,論文摘要與專案頁面對這項省幅的說法並不一致,分別寫著減少 30% 與 36%。另外,Meta-Harness 在 Harvey LAB 的 evolve split 上表現領先,而 RRSI 雖然在 evolve set 上的進步幅度是所有方法中最小的,卻是唯一一個 OOD 平均分數(JobBench、GDPval、APEX-Agents 三者平均)比 baseline H0 高出超過 1 分的方法。

💡 evolve set 進步最少,遷移表現卻最好

這組結果點出了 RRSI 設計理念的核心:在自我改良迴圈裡,真正決定能否遷移到未見過任務的,不只是「改了什麼」,更是「怎麼搜尋、怎麼保留改動」這個過程本身有沒有被約束。犧牲一部分在固定評測集上的優化空間,換來的是更真實的跨基準遷移能力。

🎯 實務啟示

對正在打造會自我修改的 agent harness(例如自動化 prompt 工程、工具選擇、子 agent 編排)的團隊來說,RRSI 提醒了一個容易被忽略的風險:光靠固定的 evolve set 評分機制去挑選「贏家」修改,很容易讓系統學會討好評測集而非真正變強。程式碼已開源且相容任意 LiteLLM 模型字串,適合作為在自家 agent 系統上實驗正規化式自我改良的起點。

🔗 來源
- 標題:Google Research Open-Sources RRSI: AI Agents That Improve Their Own Harness Without Overfitting
- 作者/機構:Asif Razzaq(MarkTechPost);研究來自 Google Cloud AI Research、UNC-Chapel Hill、Stanford、Washington University in St. Louis
- 連結:https://www.marktechpost.com/2026/09/29/google-research-open-sources-rrsi-ai-agents-that-improve-their-own-harness-without-overfitting/

#GoogleResearch #AIAgents #OpenSource #SelfImprovement #LLM #AgenticAI #MachineLearning #Regularization #SWEBench #TerminalBench
