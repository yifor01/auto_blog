---
title: How SWE-Serve Exposes the Gap Between Local Tests and Live Serving
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/how-swe-serve-exposes-the-gap-between-local-tests-and-live-serving/
model: claude-code/sonnet
generated_at: '2026-09-23T20:34:24.372306'
score: 101
---

📌 通過單元測試不代表能上線：SWE-Serve 揪出的 serving 落差

TL;DR：NVIDIA 與 SGLang 團隊推出的 SWE-Serve benchmark 顯示，近三分之一通過一般測試的 patch，在真實 serving 下會失敗。

你的 coding agent 寫的 patch，單元測試全綠，結果一接上真正的推理伺服器就掛了——這不是個案，而是 SWE-Serve 想量化的系統性落差。

🤔 **背景：沒人測過「serving 本身」改對了沒**

既有的 repo-level benchmark 評估一般軟體工程任務，inference benchmark 又多聚焦在 kernel 生成或效能最佳化，兩者都沒有測試「inference-serving stack 本身的變更」是否真的能跑起來、回傳正確結果。SWE-Serve 想補上這一塊：評估模型啟用、decoding、caching、scheduling、serving API 與 runtime 效能等真實 serving 路徑上的正確性。

🧩 **方法：83 個 merged PR，變成 53 個可執行任務**

SWE-Serve 是與 SGLang 團隊合作開發，把 83 個 merged 到 SGLang（一套開源 LLM serving 系統）的 pull request，轉成 53 個可執行任務，分成六大 inference-engineering 家族：

| 工程家族 | 任務數 |
|---|---|
| Speculative 與進階 decoding | 14 |
| 模型與 backend 啟用 | 12 |
| Kernel、量化與效能 | 8 |
| Serving API 與 runtime 正確性 | 8 |
| Caching 與 runtime 狀態 | 7 |
| 分散式執行與 scheduling | 4 |

12 個任務跑在 CPU，41 個用單張 H100；這一版尚不評估其他 inference engine、多 GPU 或多節點 serving。每個任務給 agent 一段指令，以及一份目標變更之前的 containerized SGLang checkout，agent 的 patch 只要通過該任務的 hidden verifier 就算過，不會與 reference implementation 直接比對。中位數的 reference solution 修改 553 行、涉及 7 個檔案；典型 verifier 有 7 個新行為測試加 10 個 regression 測試。19 個任務會啟動真正的 server，3 個在 H100 上設有校準過的效能門檻。

舉例來說，其中一個任務要求 agent 為 Qwen3.5 的 dense 與 mixture-of-experts（MoE）版本加上 serving 支援：要讓 0.8B dense 模型與 35B-A3B MoE 模型都能在單張 H100 上，透過 SGLang 標準介面載入與 serving。verifier 會檢查 model registration、設定與權重載入、圖片與影片輸入、OpenAI 相容請求、native batched generation、log probabilities，以及 MoE 路由的執行正確性。

📊 **數據：拿掉 live serving 測試，通過率從 45.9% 跳到 69.4%**

在 19 個含 live-serving 檢查的任務中，同一批 627 個 patch，若拿掉 live serving 測試，通過率是 69.4%；套用完整 verifier 後只剩 45.9%，等於 147 個 patch 從「過」變成「沒過」。這 19 個任務共有 276 個 live serving 測試，其中 242 個來自或改自 SGLang 本身，其餘 34 個是為對應變更新寫的。

以 Gemma 4 MoE 任務為例，33 個 patch 裡有 16 個通過了所有其他檢查，卻至少在一項 live serving 測試上失敗，這些測試涵蓋 model loading、expert routing、文字與圖片 serving，以及有正確順序與 log probabilities 的 batched generation。

文章把 request-to-output 路徑拆成四個 runtime domain：request handling 與 I/O、scheduling 與請求生命週期、model execution、KV-cache 與 runtime 資源管理。只涉及單一 domain 的 26 個任務通過率是 69.0%，跨多個 domain 的 27 個任務只有 47.7%，差距 21.3 個百分點，而且每一種模型設定都呈現同樣方向的落差。

評測涵蓋 11 個模型、31 種 model-effort 組合，用只靠 Bash 的 mini-swe-agent，在 closed-book 條件下跑完整 53 題 benchmark 三次，每個 session 上限 210 分鐘、350 步：

| 模型 | Reasoning 設定 | pass@1 | 平均成本／任務 | 平均耗時 |
|---|---|---|---|---|
| Claude Opus 5 | max | 75% ± 3% | $17.40 | 57.5 分 |
| GPT-5.6 Sol | max | 75% ± 6% | $12.26 | 29.5 分 |
| Claude Sonnet 5 | xhigh | 64% ± 3% | $6.61 | 40.6 分 |
| Kimi K3 | max | 64% ± 5% | $7.24 | 99.9 分 |
| GPT-5.6 Luna | max | 64% ± 4% | $0.95 | 28.9 分 |
| DeepSeek V4 Flash (0731) | max | 55% ± 4% | $0.69 | 36.4 分 |

用原生 harness（Codex、Claude Code）並沒有讓兩個領先者表現更好：GPT-5.6 Sol 在 Codex 裡拿 73.6%、Claude Opus 5 在 Claude Code 裡拿 69.8%，都低於用 mini-swe-agent 跑出的 75.5%。成本與表現也沒有明確對應關係：四個並列 64% 的模型裡，平均成本從 $0.95 到 $7.24 都有，耗時從 25.5 分到 99.9 分不等，且沒有一個模型在六大工程家族裡全部領先。

⚠️ **限制**

SWE-Serve 的「通過」只代表滿足 benchmark 的 verifier，並不等於 SGLang 真正的 upstream review 流程，也不代表某個 patch 或 reference solution 可以合併、已獲 SGLang maintainer 認可。目前這一版也不涵蓋其他 inference engine、多 GPU 或多節點 serving。

🎯 **實務啟示**

若你在維護或評估與 inference-serving 相關的 coding agent，別只看單元測試綠燈——SWE-Serve 的資料顯示，大約三分之一「看起來過關」的 patch，會在真正啟動 server 之後才暴露問題，尤其是同時動到多個 runtime domain（例如同時碰 scheduling 又動 KV-cache）的變更，值得額外補上 live-serving 層級的驗證，不能只靠既有的單元測試與 regression 測試判定安全。

🔗 **來源**
- 標題：How SWE-Serve Exposes the Gap Between Local Tests and Live Serving
- 作者／機構：Elizabeth Goodman／NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/how-swe-serve-exposes-the-gap-between-local-tests-and-live-serving/

#SWEServe #NVIDIA #SGLang #LLMServing #CodingAgents #Benchmark #InferenceEngineering #AIAgents #MachineLearning #SoftwareEngineering
