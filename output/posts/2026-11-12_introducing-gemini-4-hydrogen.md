---
title: Introducing Gemini 4 Hydrogen
source: Google DeepMind
url: https://deepmind.google/blog/introducing-gemini-4-hydrogen/
model: claude-code/sonnet
generated_at: '2026-11-12T22:56:07.871468'
score: 137
---

📌 【Google DeepMind】Gemini 4 Hydrogen 上線：主打速度的日常工作模型

TL;DR：Hydrogen 主打速度與效率，定位為日常 coding 與 agent 工作流的執行引擎。

當大家都在比較哪家模型推理能力最強時，Google 這次反而先推出一個「不追求最聰明，但要最快」的模型。Gemini 4 Hydrogen 的定位很清楚：讓 Carbon 與 Argon 負責深度架構判斷與疑難除錯，自己專心把日常的寫程式、跑測試、驗證改動做得又快又準。

🤔 為什麼需要一個「專門做執行」的模型

在真實的軟體開發情境中，團隊固然需要 Carbon、Argon 這類前沿模型處理系統設計或棘手的 bug，但更多時候需要的是反應快、紀律嚴謹的執行模型，負責寫程式碼、跑測試、驗證改動。Hydrogen 就是為此而生，可以獨立使用，也可以和 Carbon、Argon 搭配成多模型工作流中的高效執行引擎。

🧩 Orchestrator：讓模型自動換人上場

Google Antigravity 新推出的 Orchestrator 功能，會在同一個 session 裡動態切換 Carbon 與 Hydrogen 等模型，不必整段工作流都用同一個模型跑到底。根據官方公布的 Terminal-Bench 4.0 數據，Orchestrator 能達到接近 Carbon 的任務成功率，同時平均少耗 24% 的 quota、快 19% 完成任務。在需要平行 agent 的場景，Carbon 可以當協調者，Hydrogen 則同時在多個隔離工作區裡擔任 worker 與 verifier，一邊寫程式一邊測試。

📊 跟上一代比，到底快多少、便宜多少

Hydrogen 在 Artificial Analysis Intelligence Index 預設高思考等級下拿到 51 分，超過 Argon 的 50 分；拉到最高的 xhigh 等級則來到 54 分。價格方面，整個 100 萬 token 的 context window 統一收費，輸入每百萬 token 1.5 美元、輸出 7.5 美元。

與前代 Gemini 3.8 Flash 相比：

| 指標 | Gemini 3.8 Flash | Gemini 4 Hydrogen |
|---|---|---|
| 高思考等級任務速度 | 基準 | 快 2.5 倍 |
| Terminal-Bench 4.1 | 18.2% | 57% |
| 捏造內容（fabricated claims） | 基準 | 降低超過 5 倍 |

在其他基準上，Hydrogen 在 HLE-Diamond 拿到 58.8% 的同級最佳成績，於 Vals Tax Agent Bench 排名第一（52.3%），Vals Legal Research Bench 並列第一（55.8%），並在新推出的 Multimodal Knowledge Agent（MKA）基準拿下 53.4%，Agents' Last Exam v1.1 則是 71.6%，在 Agent Arena 上排名第 5。官方也提到，在複雜圖、SQL 與資料密集的企業工作流中，合作夥伴的早期測試顯示 Hydrogen 比 3.8 Flash 快 2 到 2.8 倍，同時減少 12% 到 23% 的 token 用量。

💡 從即時 3D 建模到試算表動畫

幾個官方展示的應用場景頗能看出 Hydrogen 的速度優勢：在 Geminisland 中，使用者只要輸入一句提示，就能即時生成 3D voxel 結構讓玩家走進去探索；搭配 Google Antigravity 新推出的 Gemini 前端設計技能，Hydrogen 一次生成了包含 WebGL2 地形 shader、四階段 scrollytelling、3D wireframe 規格卡的電商網站；在 Google Sheets 裡，它甚至能用 Python 配合原生 =LET(...) 公式與條件式格式，把上千個儲存格變成會動的像素畫布。在 Google Slides，它能從一段 YouTube 影片與範本自動生成多頁投影片，再跑一輪自我檢查修正排版重疊的問題。

🎯 實務啟示

如果團隊已經在用前沿模型處理困難的架構決策，Hydrogen 這類「快但夠用」的執行引擎值得納入多模型工作流，把高成本模型留給真正需要深度判斷的環節，日常的寫程式、測試、資料整理則交給更便宜更快的模型處理，對控制 token 成本與縮短迭代週期會有直接幫助。

🔗 來源
- 標題：Introducing Gemini 4 Hydrogen
- 作者／機構：Google DeepMind
- 連結：https://deepmind.google/blog/introducing-gemini-4-hydrogen/

#Gemini4 #GoogleDeepMind #LLM #AgenticAI #AIcoding #MultiModel #GoogleAntigravity #AIbenchmark #DeveloperTools #GenerativeAI
