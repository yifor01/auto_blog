---
title: Optimizing agent system prompts with Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/optimizing-agent-system-prompts-with-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-09-16T20:24:33.398430'
score: 87
---

📌 用 AI Agent 修 AI Agent：AWS AgentCore 用「反思式」設計自動優化 System Prompt

TL;DR：AWS Bedrock AgentCore 用 agent 讀取自家的執行紀錄自動改寫 system prompt，效能打平甚至超越 GEPA、MIPROv2，且優化耗時縮短逾十倍。

過去要救一個表現不佳的 agent，工程師得一行一行翻執行紀錄（trace），猜哪裡出錯，手動調整 prompt 與工具描述，再重新跑一次評估。AWS 這次做的事情，是讓另一個 agent 來做這件苦工。

🤔 從人工除錯到自動化迴圈

Amazon Bedrock AgentCore 的 Observability 功能會記錄 agent 的行為軌跡，Evaluation 則提供品質訊號。AgentCore optimization 把兩者串起來：用 production traces 提出配置變更建議，先透過離線批次評估驗證，再上線做 A/B 測試，最後才把表現較好的版本推廣出去。整個流程的核心，是一個被稱為「reflector」的推理元件，負責審視已評分的 agent 行為、找出成功與失敗案例之間的規律，並提出針對性的配置修改建議。

🧩 用檔案系統餵資料，而非硬塞進 context window

Agent trace 通常很長，就算只有幾十筆，也很容易塞爆模型的 context window。AWS 的做法不是截斷或預先摘要，而是把完整的 trace 語料庫放進一個目錄，交給 reflector agent 用 shell 工具自行探索：可以用 `ls` 列檔案、`grep` 搜尋、`cat` 讀取單筆 trace、`diff` 比較輸出，自由挑選要細看的成功與失敗案例。整個過程沒有固定的訊號萃取或摘要流程，由 reflector 自己判斷哪些證據重要、該做什麼比較，再把結論轉譯成配置修改建議。

任何提案在被採用前，都必須先通過平臺層級的 guardrails，防止優化過程中常見的「跑偏」現象：prompt 越改越長、直接把 trace 裡的用詞當成範例寫進 prompt、或是為了衝高評分分數而放寬安全限制。

目前實際驅動 AgentCore optimization 的是 Single Agent Reflector：單一 agent 一次看完整組 trace，先掃過分數分布，再深入檢視最有資訊量的片段，對比成功與失敗案例，輸出一組連貫的配置修改。每個 optimization epoch 都重複「評分 → 反思 → 套用通過 guardrail 的修改」這個循環，可以多跑幾個 epoch 換取更好的品質。

另一個是實驗性的 Sub-Agent Reflector，已在 Strands 開源 GitHub repo 中釋出初步版本。它用一群 sub-agent 分頭處理，每個 sub-agent 只負責分析單一 trace（素材未列出具體的三層分析內容），各自回傳精簡的發現與一條修正規則。因為每個 sub-agent 都在自己獨立的 context window 中運作，不會被其他 trace 干擾，最後由 orchestrator 彙整發現、歸納重複模式、去除冗餘，濃縮成一組配置修改。單一 reflector 一次掃過大量 trace 時，容易只聚焦在最先看到的五到十筆案例上，漏掉只出現在少數案例中的失敗模式，Sub-Agent Reflector 正是為了補這個缺口而設計。

📊 AppWorld 與 WebShop 上的表現

AWS 在兩個公開 benchmark 上，把 Single Agent Reflector、Sub-Agent Reflector 與 GEPA、MIPROv2 兩個既有方法放在一起比較，每個方法都掃過設定空間、回報最佳結果連同所需 turn 數與實際耗時。

| 方法 | AppWorld 分數 | AppWorld 耗時 | WebShop 分數 | WebShop 耗時 |
|---|---|---|---|---|
| Single Agent Reflector | 81.55% | 6 分鐘、20 turns | 78.31% | 1 分鐘、5 turns |
| Sub-Agent Reflector | 95.83% | 較長（未列具體數字） | 79.15% | 較長（未列具體數字） |
| GEPA / MIPROv2（最佳基準） | 對照組 | 慢 18～36 倍 | 對照組 | — |

Single Agent Reflector 在 AppWorld 上比 GEPA 快 18 倍、比 MIPROv2 快 36 倍，分數仍相當甚至更好；Sub-Agent Reflector 則拿下兩個 benchmark 的最高分，在 AppWorld 上比基準線高出 23 分、比次佳方法再高 16 分，在 WebShop 上也比基準線高 4 分。逐 trace 拆解分析的效果在 AppWorld 上最明顯，因為那裡的失敗模式較分散，單一 reflector 一次通讀容易漏掉少數模式。

💡 兩種設計各自的取捨

整體反思讓 Single Agent Reflector 用遠少於迭代式方法的 turn 數與時間就能拿到有競爭力的分數，適合追求快速迭代週期的場景；而 sub-agent 分工讓 Sub-Agent Reflector 有更高的品質天花板，代價是需要更多算力與時間。

⚠️ 仍是輔助工具，不是自動駕駛

AWS 特別強調，Responsible AI 的考量是這個流程的一部分：推薦結果應該被審查與測試後才使用，guardrails 只是在候選更新被採用前先做篩選，並不代表可以完全跳過人工把關。

🎯 實務啟示

如果你正在維運一套會累積大量 production trace 的 agent 系統，這個做法提供了一個可參考的迭代模型：與其手動翻 log 調 prompt，不如把「評分 + 反思 + guardrail + A/B 測試」變成常態化流程，同時視情境在效率（Single Agent Reflector）與品質天花板（Sub-Agent Reflector）之間取捨。

🔗 來源
- 標題：Optimizing agent system prompts with Amazon Bedrock AgentCore
- 作者／機構：Han Ding, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/optimizing-agent-system-prompts-with-amazon-bedrock-agentcore/

#AWS #BedrockAgentCore #AIAgents #PromptEngineering #LLMOps #AgentEvaluation #AutoPromptOptimization #GEPA #MIPROv2 #ObservabilityAI
