---
title: 'NVIDIA Introduces SoL-Pi: Auto-Research Loops That Cut Coding Agent Token
  Traffic by Up to 49%'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/21/nvidia-researchers-have-released-sol-pi/
model: claude-code/sonnet
generated_at: '2026-09-22T20:23:47.867008'
score: 98
---

📌 【NVIDIA】讓 AI 自己優化 Coding Agent，Token 流量砍近半

TL;DR：NVIDIA、NTU、MIT 團隊用自動研究迴圈找出 harness 優化技巧，讓開源 Pi coding agent 省下最多 49% token 流量。

多數省 token 的招數都在降低「每個 token 的成本」：更快的 kernel、量化、換用更便宜的模型。NVIDIA 團隊這次反過來問：能不能直接減少任務要用掉的 token 數量？答案是讓另一個 AI 去自動搜尋 coding agent harness 的優化空間。

🤔 **Coding agent 越跑越久，context 越塞越滿**

Coding agent 現在一跑就是好幾個小時，每一次編輯、測試執行、log 讀取都會回寫進模型的 context。Harness 是負責處理 tool call、context、observation 與委派（delegation）的那一層，手動調校速度慢，而且各部分彼此耦合，改一處可能把成本推到後面的步驟。Meta-Harness 之類的系統嘗試自動化這件事，但先前有研究指出，演化出來的 harness 容易過度擬合搜尋時用的任務，換到沒看過的任務只有邊際效益。

🧩 **怎麼搜：一個 AI 觀察另一個 AI 的執行軌跡**

NVIDIA、NTU、MIT 團隊釋出的 SoL-Pi，是給開源 Pi coding agent 用的 4 個效率機制，全部由一個「研究 AI」透過在 harness 層跑自動研究迴圈找出來。流程是：研究 AI 觀察一個跑基礎版 Pi 的獨立 agent 產生的執行軌跡，據此提出 harness 改動並實際測試。每一次搜尋都是一個獨立、可拋棄的迴圈，遵循 autoresearch cycle，並額外加上 Ralph Loop 實作步驟與一位獨立審查員。

驗收規則在搜尋開始前就固定下來，優化器本身不能修改規則：每一項能力指標都必須落在預先宣告的容忍範圍內，候選方案還必須至少改善一項效率指標。EdgeBench 的 51 個公開任務中，11 個用來對凍結後的候選方案做單向驗收，40 個用於最終評估；held-out 的結果不會回饋進搜尋過程，避免自我強化的過擬合。

📊 **實測：token 少了近一半，分數幾乎沒掉**

整套機制先在 GPT-5.6 Sol 上搭建完成，再直接搬到 Opus 5 上使用，中間沒有針對 Opus 5 再做搜尋：

| 模型 | 保留分數比例 | Token 流量減少 | API 成本減少 |
|---|---|---|---|
| Opus 5 | 94.3% | 44.7% | 33.5% |
| GPT-5.6 Sol | 93.7% | 49.0% | 33.2% |

另外還有一個「Performance point」設定，只挑各後端表現最好的單一機制（GPT-5.6 Sol 用 ObservationPack、Opus 5 用 Action Fusion），能讓分數比原版 Pi 分別高出 5.3% 與 12.8%。

💡 **省下來的錢，是拿 cache-write 換的**

在 GPT-5.6 Sol 上，完整堆疊反而讓 cache-write 流量從 0.0141B 增加到 0.0316B token，但總成本仍然下降，從 1,339 美元降到 894 美元。論文估算，相較原生 Codex 與 Claude Code harness，每小時可省下 8.75 到 13.50 美元；相較原版 Pi，則是 4.36 到 5.71 美元。

⚠️ **跨模型遷移還只是初步結果**

研究團隊自己也強調，跨模型遷移的結果屬於初步（preliminary）——這些機制在 Opus 5 上觸發的頻率較低，可能是因為搜尋過程只用了 GPT-5.6 Sol 的執行軌跡，尚未針對 Opus 5 重新搜尋。

🎯 **實務啟示**

SoL-Pi 已經以 MIT 授權在 NVlabs 的 GitHub 上開源，可以直接套用在未經修改的 Pi 版本上，官方測試環境是 Pi 0.85.1 搭配 Node.js 22.19 以上。對正在跑長時間 agent 任務、被 context 堆積吃掉成本的團隊來說，這提供了一條不用換模型、不用改 prompt，只從 harness 層面省錢的路徑，而且驗收機制的設計（固定規則、held-out 評估）也值得參考，用來避免自己手動調校 harness 時掉入過擬合的陷阱。

🔗 **來源**
- 標題：NVIDIA Introduces SoL-Pi: Auto-Research Loops That Cut Coding Agent Token Traffic by Up to 49%
- 作者／機構：Asif Razzaq @ MarkTechPost；研究團隊來自 NVIDIA、NTU、MIT
- 連結：https://www.marktechpost.com/2026/09/21/nvidia-researchers-have-released-sol-pi/

#NVIDIA #CodingAgent #LLMAgents #TokenEfficiency #OpenSource #AIResearch #HarnessOptimization #AgenticAI #MachineLearning #EdgeBench
