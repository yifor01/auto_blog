---
title: Google Open-Sources Harness2, a Recursive Agent Harnessing Framework
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/18/google-harness2-recursive-agent-harnessing-framework/
model: claude-code/sonnet
generated_at: '2026-10-18T19:31:10.849957'
score: 98
---

📌 Google 開源 Harness²：模型凍結不動，進步靠「周邊」優化

TL;DR：Harness² 在部署階段遞迴優化 agent 的 prompt、工具與記憶等「harness」，不需要標籤或測試案例就能自我改進。

如果你的 agent 表現不如預期，直覺反應通常是換一個更強的模型。Google Cloud AI Research 開源的 Harness² 提出另一種思路：模型權重完全不動，改進圍繞在模型周圍的程式碼與檔案，一樣能把分數拉上去。

🤔 **沒有標準答案的開放世界，怎麼自我改進？**

Harness² 鎖定的場景是「開放世界」：任務事先沒看過，也沒有驗證器能判斷答案對不對。研究團隊指出，多數自我改進方法都假設存在標籤或測試案例，Harness² 則是設計成在完全沒有這些條件下運作。這裡的「harness」指的是模型以外的一切，包含 prompt、工具、記憶、skill 與 orchestration；「harnessing」則是持續優化這套系統的過程。

🧩 **8 個可編輯元件，兩層遞迴搜尋**

Harness² 把 agent 的 harness 拆成 8 個可編輯元件，每個都掛載為獨立檔案，涵蓋 context 建構、工具介面、delegation 以及 tool loop 內的行為，比先前 Agentic Harness Engineering 的 7 檔拆分多了一個元件。

框架執行兩層互相串接的遞迴搜尋，由一個預算參數 k 控制搜尋規模：
- 平行模式（parallel）：先探測 k 個「不變」候選與 k 個「領域相關」候選，再組合出 k 種版本。
- 序列模式（sequential）：串接 k 個精煉步驟，一步步改良。

📊 **弱模型受益更明顯**

研究團隊在 3 個專業 benchmark（WorkBuddy-Bench、JobBench、Harvey 的 LAB）上測試，executor 為 Gemini 3.5 Flash 與 GLM-5，分別跑在 OpenCode 與 Codex 之上，預設編輯模型為 Claude Opus 4.8，結果為 3 次執行的平均值。

| 項目 | 數據 |
|---|---|
| GLM-5 經 1 次優化後 | 在 WorkBuddy-Bench 上超越未經優化的 Gemini 3.5 Flash |
| Gemini + OpenCode，平行遞迴 k=5 | WorkBuddy-Bench 分數提升至 80.8 |
| Gemini + OpenCode 每任務步驟數 | 從 25.4 降至 21.9，4 組設定中有 3 組步驟數同步下降 |

💡 **較弱的 executor 進步空間更大**

數據顯示，起始能力較弱的 executor（如 GLM-5）從 harness 優化中獲益更明顯，WorkBuddy-Bench 上不少設定在優化後不只分數提高，完成任務所需的步驟也變少，代表優化不只是「做對」，也讓流程更有效率。

🎯 **怎麼跑起來**

README 鎖定 Linux、Python 3.12 與 uv，本地 demo 不需要模型金鑰就能跑兩種遞迴模式體驗流程；要接真實模型則需要 Node.js 20+、Google Cloud CLI 與 Vertex AI 專案。LAB 這個 benchmark 另外需要 Pandoc 與 Poppler，WorkBuddy-Bench 需要 Docker。Executor 預設走 OpenCode，也可以加上 `--substrate cx` 改用 Codex。對於正在維運 agent 系統的工程師，這提供了一個不用重新訓練模型、也能持續迭代效果的開源起點。

🔗 **來源**
- 標題：Google Open-Sources Harness2, a Recursive Agent Harnessing Framework
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/18/google-harness2-recursive-agent-harnessing-framework/

#AIAgents #GoogleResearch #OpenSource #AgentEngineering #PromptEngineering #LLMOps #RecursiveOptimization #Gemini #AIFramework #MachineLearning
