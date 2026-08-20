---
title: Evaluating AI Agent Skill Performance with NVIDIA SkillEvaluator
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/evaluating-ai-agent-skill-performance-with-nvidia-skillevaluator/
model: claude-code/sonnet
generated_at: '2026-08-20T06:25:32.016361'
score: 109
---

📌 【NVIDIA 開源】300 多個驗證技能，Agent 表現平均多 31 分

TL;DR：NVIDIA SkillEvaluator 用「裝與不裝 skill」的對照實驗，量化 agent skill 到底值不值得裝。

🎣 就算模型能力強、文件寫得再完整，agent 還是可能在找工具的路上迷路，浪費好幾輪 token 才摸到正確做法。NVIDIA 這次沒有只靠感覺說「skill 有幫助」，而是直接做了一套評測層，把答案量化出來。

🤔 skill 有沒有用，過去只能憑感覺
NVIDIA 的 Skills 是打包過的能力描述檔，告訴 agent 某個 NVIDIA 產品能做什麼、什麼時候該呼叫它、怎麼呼叫。但「打包好」不等於「有效」，團隊因此開發 SkillEvaluator，一套開源評測工具，透過靜態檢查與真實任務執行，量測有無 skill 對 agent 行為軌跡與輸出品質的實際影響。這篇文章公布了超過 300 個經過驗證的 skill、涵蓋 30 多項 NVIDIA 產品的首批基準測試結果。

🧩 三層驗證，Tier 3 才是重頭戲
每個 skill 上架前要通過三層評測，各自獨立可單獨執行：
- Tier 1（安全與結構）：schema 與 frontmatter 驗證、品質評分、prompt injection 與資料外洩的安全掃描、secret／PII 偵測、授權條款檢查、腳本 lint。
- Tier 2（差異性）：用 embedding 相似度找出單一 skill 內部的重複指引，以及跨目錄的重疊涵蓋範圍。
- Tier 3（實測）：在隔離沙箱中，讓 agent 針對自動產生的任務跑兩次，一次裝 skill、一次不裝，量測差異。

Tier 3 建立在開源的 Harbor 框架上，SkillEvaluator 負責把評測案例轉成 Harbor 任務、在沙箱中執行 agent、蒐集結果並計算影響力。每個評測案例都在同一組 prompt、模型、任務輸入與評分標準下執行兩次，唯一變數就是是否安裝該 skill；同樣的比較會在兩套 agent harness（Claude Code、Codex）上各跑一次。裝與不裝之間的分數差，就是所謂的 Skill Lift。

實際操作上，流程相當精簡。先產生評測資料集：

skillevaluator create-eval-dataset ./my-skill --full

這會建立 evals/evals.json，每個案例包含 ID、prompt、預期輸出，以及可選的斷言；加上 --full 後，資料集會涵蓋明確、隱含、情境與否定等多種案例類型。確認案例沒問題後，執行對照評測：

skillevaluator tier3 evaluate ./my-skill --agents codex --env-mode docker

SkillEvaluator 會把案例轉成 Harbor 任務包、分別跑有無 skill 的兩輪、評分，再算出 Skill Lift，底層的執行與隔離則交給 Harbor 處理。

📊 沒裝 skill 時，agent 表現普遍偏低

以下數據取自 2026 年 8 月 12 日的 benchmarks.json 快照（commit 738d79e），分數是跨 skill／harness 配對的巨觀平均。

| 維度 | 說明 | 無 skill 分數（滿分 100） |
|---|---|---|
| Correctness | 最終答案是否正確 | 46 |
| Discoverability | 相關時能不能載入 skill、不相關時能不能保持不載入 | 42 |
| Effectiveness | agent 是否達成使用者目標、遵循預期流程 | 39 |
| Efficiency | 有沒有浪費步驟或重複呼叫工具 | 43 |
| Security | 是否避免不安全操作、secret 外洩、未授權存取 | 97 |

裝上驗證過的 skill 之後，各維度全面提升，尤其 Correctness、Discoverability、Effectiveness、Efficiency 增幅最大：

| 維度 | 無 skill | 有 skill | Skill Lift |
|---|---|---|---|
| Correctness | 46 | 87 | +41 |
| Discoverability | 42 | 82 | +40 |
| Effectiveness | 39 | 78 | +39 |
| Efficiency | 43 | 78 | +35 |
| Security | 97 | 98 | +1 |
| 全部維度平均 | — | — | +31 |
| 排除 Security 平均 | — | — | +39 |

Correctness 與 Effectiveness 是兩個在有無 skill 情境下都一致量測的維度，分數分別從 46 升到 87、從 39 升到 78。文章特別提醒，這些分數不是通過機率的估計值，而是在被評測的特定任務上的平均表現；Discoverability 與 Efficiency 則是針對 skill 本身的評分，應解讀為「agent 裝上後有沒有正確啟用並使用它」，而非未輔助情境下的 agent 行為指標。

⚠️ 讀數據前要注意的細節
Correctness、Effectiveness、Security 量測的是執行結果，所以無 skill 基準線反映的是 agent 沒有相關 skill 時能做到什麼程度；但 Discoverability 與 Efficiency 同時也在衡量「怎麼用」skill，沒裝 skill 時這些行為根本無從發生。文章解釋，agent 仍可能因為工具使用得宜、執行乾淨、或正確地在不相關任務中保持 skill 不載入而拿到部分分數，這也是為什麼基準線落在 42、43 附近而非 0。另外，多數 skill 僅跑一次評測（已公布結果中 85% 只跑一次、15% 跑兩次），實測結果本身存在跑次間的變異，文章也未提供信賴區間。

🎯 對開發者的實務啟示
NVIDIA 已經釋出 Claude Code、Codex、Cursor 的外掛，同樣的 skill 也可透過 Skills.sh、ClawHub、Hermes Hub 取得。如果你在建構自己的 agent 工具或 skill，SkillEvaluator 提供了一套可重複、可拆分執行的三層驗證框架，值得在發布前拿來檢驗：光是「有沒有 skill」的差異，就可能決定 agent 是流暢完成任務，還是在死路裡打轉。

🔗 來源
- 標題：Evaluating AI Agent Skill Performance with NVIDIA SkillEvaluator
- 作者／機構：Michelle Horton, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/evaluating-ai-agent-skill-performance-with-nvidia-skillevaluator/

#AIAgents #NVIDIA #SkillEvaluator #OpenSource #AgentEvaluation #LLM #Benchmarking #ClaudeCode #Codex #AgentTooling
