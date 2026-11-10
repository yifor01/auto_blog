---
title: 'Our Smallest, Most Efficient Model: Muse Ember'
source: Hacker News
url: https://research.meta.ai/blog/muse-ember
model: claude-code/sonnet
generated_at: '2026-11-10T00:51:05.012237'
score: 103
---

📌 【Meta Superintelligence Labs】Muse Ember：比 Haiku 便宜三倍的 Agent 執行模型

TL;DR：Meta 新推最小模型 Muse Ember，主打 agent 高頻雜務，成本效益打贏 Haiku 與 Luna。

當一個 agent 系統一天要跑上萬次工具呼叫、路由判斷、文件擷取，真正決定成本的往往不是「哪個模型最聰明」，而是「哪個模型每次任務花最少錢還夠用」。Meta 這次直接把 Muse Ember 定位在這個戰場上。

🤔 **Agent 的日常雜務，需要的是便宜又穩的執行者**

Muse Ember 被 Meta 定義為「專為複雜推理執行與 agent 整天重複的工作設計」：工具呼叫、程式碼子任務、路由、資訊擷取、長文件解析。這類任務數量龐大但單次複雜度不高，傳統上會用大模型硬扛，造成成本失控，Ember 瞄準的正是這個缺口。

📊 **在 Artificial Analysis 的成本/智能效率前緣上無人能及**

依官方公布的 Artificial Analysis 測試，在不同 reasoning effort 設定下比較成本與智能分數：Muse Ember 在花費約 0.136 美元／任務時可拿到 35.8 分，而 Claude Haiku 5.5 要花到 0.411 美元才拿到最高的 36.2 分，相當於 Ember 用約三分之一成本打到對手的天花板分數；同時 Ember 最低分的 33.9 分也已經超過 GPT-6 Luna 在任何設定下的最高分 27.8。官方稱其「在整個 Artificial Analysis 排行榜上，沒有模型用更低成本做到更高分」。

在 max reasoning 設定下的幾項關鍵評測（Muse Ember／Claude Haiku 5.5／GPT-6 Luna）：

| 評測項目 | Muse Ember | Claude Haiku 5.5 | GPT-6 Luna |
|---|---|---|---|
| AutomationBench-AA（端到端商業流程） | 37.8% | 13.9% | 20.2% |
| Agents' Last Exam（端到端 agent 任務） | 61.6% | 57.0% | 57.1% |
| Personal Superintelligence Index | 46.8% | 36.1% | 37.0% |
| Terminal-Bench 4.0（終端機 agent 編程） | 40.9 | 39.2 | 16.4 |
| Coding Agent Index-AA | 46 | 37 | 31 |
| PerceptionBench（含工具的視覺感知） | 80.6 | 78.6 | 62.8 |

在 OSWorld 2.1（跨桌面應用的電腦操作任務）中，Ember 的 partial 分數為 69.5（binary 33.8），同樣領先 Haiku 的 68.9（binary 27.8）與 Luna 的 50.5（binary 17.0）。

💡 **早期合作夥伴的回饋聚焦在速度與吞吐量**

Box 的 VP of AI Products Yashodha Bhavnani 提到，Ember 能逐條款比對合約與公司談判準則並給出整體風險評級；Cline 創辦人 Saoud Rizwan 表示 Ember 是團隊用來做 subagent 編程與文件分析、同時壓低成本的理想選擇；Cloudflare CTO Dane Knecht 指出 Ember 在尾端延遲比對照模型快up up to 30%，適合多 repo 調查類的高吞吐 agent 工作；You.com Inference Lead Chak Pothina 則表示 Ember 完成了所有測試的 coding quest，p95 延遲僅 2.2 秒，比領先的開放權重模型快 4 到 13 倍，輸出 token 數也少了 36% 到 48%。

🎯 **實務啟示**

Muse Ember 目前已上線 Meta Model API，定價為每百萬輸入 token 0.10 美元、每百萬輸出 token 0.50 美元，並支援 1M token 上下文與最高 512K 輸出 token，可一次吃進整個程式碼庫或文件集。對正在設計 agent harness 的工程團隊而言，這類「便宜但夠用」的執行層模型，值得納入作為大模型之下的子任務執行節點，用來壓低大量重複性呼叫的總成本。

🔗 **來源**
- 標題：Our Smallest, Most Efficient Model: Muse Ember
- 機構：Meta Superintelligence Labs
- 連結：https://research.meta.ai/blog/muse-ember

#AI #LLM #Meta #MuseEmber #AIAgents #AgenticAI #ModelEfficiency #Benchmarking #ArtificialAnalysis #MachineLearning
