---
title: 'JetBrains Releases Mellum2.1: A 12B MoE Open Model for Coding Agents'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/08/jetbrains-releases-mellum2-1-a-12b-moe-open-model-for-coding-agents/
model: claude-code/sonnet
generated_at: '2026-10-08T22:18:08.593469'
score: 98
---

📌 【JetBrains 開源】12B MoE 模型 Mellum2.1，SWE-bench Verified 從 2 分衝到 47 分

TL;DR：JetBrains 以大規模 RL 重訓 Mellum2，打造出可自架的 Apache 2.0 編碼 agent 模型。

同一套 12B 架構，只靠大規模強化學習（RL）重新訓練，SWE-bench Verified 分數就從 2.0 分跳到 47.0 分，成長超過 20 倍。這不是換了新架構，而是 JetBrains 用真實軟體環境訓練出來的成果。

🤔 **從 Mellum2 到 Mellum2.1，架構沒變，練法全變**

Mellum2.1 是 JetBrains 今年 6 月開源的 Mellum2 Thinking 的下一版，釋出的檢查點名為 Mellum2.1-12B-A2.5B-Thinking，以 Apache 2.0 授權上架 Hugging Face。這是一個會先輸出思考鏈（chain of thought）才回答的推理模型，JetBrains 將其定位在三種用途：agent worker、通用推理助手，以及可自架的私有部署。模型架構與 Mellum2 完全相同，所有升級都來自後訓練階段的強化學習。

🧩 **28 層、64 個 expert，每 token 只動用 8 個**

Mellum2.1 採用 MoE（mixture-of-experts）架構，共 28 層、64 個 expert，由路由器為每個 token 挑選 8 個 expert 啟動，實際啟動參數量約 2.5B。Attention 使用 grouped-query attention，配置 32 個 query head、4 個 KV head；每 4 層中有 3 層採用 1,024 token 的滑動視窗（sliding window）。Context 長度達 131,072 tokens，詞彙表（vocabulary）有 98,304 個 token，權重以 bfloat16 格式釋出。

JetBrains 表示，過去 RL 只是訓練流程最後的短暫收尾步驟，這次則把 RL 變成訓練的主體。新增的 RL 任務涵蓋數學、競技程式設計、科學、工具呼叫（tool use）與軟體工程，並對開源 RL 資料集做了篩選，排除測試壞掉、答案無法驗證，以及太簡單或根本做不到的任務。在軟體工程任務上，模型於真實 repository 中訓練，配備 shell 與檔案編輯工具，測試通過才會得到獎勵。JetBrains 透露，訓練過程啟動了數百萬個沙盒（sandbox），橫跨數千種環境。

📊 **Agentic coding 分數暴增，但不是每項都贏**

JetBrains 用同一套流程（thinking mode）評測了 Mellum2.1、Mellum2、Qwen3.5-9B 與 Gemma 4 E4B，以下數據皆為 JetBrains 自行回報：

| 項目 | Mellum2 | Mellum2.1 |
|---|---|---|
| SWE-bench Verified | 2.0 | 47.0 |
| SWE-bench Pro | 0.0 | 28.0 |
| Terminal-Bench 2.1 | 0.6 | 17.4 |
| HarmBench（越低越好） | 21.5 | 8.5 |

Agentic 測試採用開源的 Pi v0.73.1 harness，context 設為 114K tokens。Mellum2.1 在 LiveCodeBench v6（82.0）、HumanEval+（91.5）、MBPP+（79.4）與 BFCL v4（62.3）上領先同組模型，但 Qwen3.5-9B 在 SWE-bench Verified（50.0）、SWE-bench Pro（38.0）、AIME 25/26（86.7）與 GPQA Diamond（77.8）上仍佔優勢。

值得留意評測管線（pipeline）差異：Qwen 官方模型卡自報 LiveCodeBench v6 為 65.6、GPQA Diamond 為 81.7，但 JetBrains 用自己的流程測出來分別是 75.4 與 77.8，顯示跨團隊比較基準模型時要留意評測方法本身的差異。

💡 **架構沒變，所以速度沒退步**

因為後訓練完全沒動架構，Mellum2.1 的推理速度與 Mellum2 一致。JetBrains 表示，在單張 H200 高負載情境下，Mellum2.1 的 token 吞吐量接近 Qwen3.5-9B 的兩倍；單一請求情境下，透過 multi-token prediction（MTP）可再加速約 1.6 倍。供 vLLM 推測解碼（speculative decoding）使用的 MTP head 則標示「即將推出」。

🎯 **怎麼跑起來**

完整模型可透過 vLLM 部署，加上 `--reasoning-parser qwen3` 參數；若要支援工具呼叫，再加上 `--enable-auto-tool-choice --tool-call-parser hermes`。JetBrains 建議的取樣參數是 temperature 0.6、top_p 0.95、top_k 20。GGUF 版本仍在製作中，官方的 GGUF repository 目前已列出 5 個檔案。對於想要自架、又需要 agent 在 repo 裡自己動手編輯檔案並驗證改動的團隊，Mellum2.1 提供了一個開放授權、架構透明的選項，值得納入自架方案的評估清單。

🔗 **來源**
- 標題：JetBrains Releases Mellum2.1: A 12B MoE Open Model for Coding Agents
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/08/jetbrains-releases-mellum2-1-a-12b-moe-open-model-for-coding-agents/

#JetBrains #Mellum #OpenSource #MoE #CodingAgent #LLM #ReinforcementLearning #SWEBench #vLLM #ApacheLicense
