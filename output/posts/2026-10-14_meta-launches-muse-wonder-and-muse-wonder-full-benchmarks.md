---
title: 'Meta Launches Muse Wonder and Muse Wonder Full: Benchmarks, Pricing and How
  to Use It'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/13/meta-muse-wonder-muse-wonder-full-release/
model: claude-code/sonnet
generated_at: '2026-10-14T20:56:31.587080'
score: 96
---

📌 Meta 發布 Agent 旗艦模型 Muse Wonder，定價與操作流程一次看懂

TL;DR：Meta 推出新一代 agent 模型 Muse Wonder／Muse Wonder Full，可規劃長任務並操作瀏覽器、桌面與手機 App，API 已開放申請。

多數人對「AI agent」的想像還停在「幫你寫一段程式」，但 Meta 這次推出的 Muse Wonder，直接把目標設定在「長時間自主作業」：寫程式、處理法務與財務任務，甚至操作電腦。

🤔 **接續 Muse Spark 的 scaling ladder**

Muse Wonder 是 Meta Muse 系列在 scaling ladder 上接續 Muse Spark 的下一步。Meta 團隊表示模型在自家的 Prometheus 資料中心訓練，pretraining 與 reinforcement learning 兩端都有提升，並將表現進步歸功於更大的 base model，使模型在陌生任務上的泛化能力更好。

🧩 **核心能力：長任務規劃＋操作電腦**

對開發者而言，Muse Wonder 的重點能力是規劃長任務並把子任務委派給 sub-agent，同時具備操作瀏覽器、桌面應用程式與手機 App 的能力，目標是讓 agent 能完成需要多步驟、跨工具的實際工作，而不只是單輪問答。Muse Wonder 已在 Meta Model API 與 Muse Code 上線；能力更完整的 Muse Wonder Full 則限定付費 Muse Code 方案才能使用。

📊 **Benchmark 數字揭露有限，比較方式也不完全公平**

Meta 官方表格中列出的分數多半引用第三方來源，例如 Artificial Analysis、Vals AI 與 Datacurve，而 PSI、MemoryBench、FocusBench 則是 Meta 內部評測項目。值得注意的是，model card 本身就說明競品的跑分是「best-effort」，不保證對手模型有被妥善調校；SWE-Marathon 項目中，對手使用的是 Codex 與 Claude Code 跑出的結果，並非同一套測試環境下的比較。由於素材並未提供實際分數，這裡不列出具體數字，但這個揭露限制本身就值得工程師在解讀官方 benchmark 時多留一分警覺。

🧩 **怎麼開始用**

1. 打開 dev.meta.ai，點選 Start building 登入；Muse Code 的安裝指令也在同一頁。
2. 選模型：Muse Wonder 定價為每百萬 token 輸入 $4、cached $0.20、輸出 $20；Muse Wonder Full 需要 Muse Code 的 Power（$50/月）或 Maximum（$200/月）方案。
3. 用 Meta 帳號登入，確認名稱並接受 Model API 條款。
4. 加入付款方式後，在 API keys 頁面建立 API key，並依 quickstart 指示匯出為 `MODEL_API_KEY`。
5. 在 Playground 的 Chat 頁面選擇 `muse-wonder-1.0`，可調整 temperature、max tokens 與 reasoning effort。
6. 點 Get code 取得 curl 或 Python 範例，呼叫的是 Responses endpoint `https://api.meta.ai/v1/responses`；此 API 與 OpenAI 相容，換個 base URL 就能直接用 OpenAI SDK。
7. 也可以在終端機用 Muse Code：Mac 上執行 `curl -fsSL https://dev.meta.ai/install.sh | bash`，Windows 用 `irm https://dev.meta.ai/install.ps1 | iex`，在專案資料夾執行 `muse` 並登入。預設模型是 `muse-spark-1.2`，可用 `/models` 切換，或直接 `muse --model muse-wonder-1.0` 啟動。

⚠️ **解讀 benchmark 時要留意比較基準不同**

由於競品跑分未必經過調校、且部分比較（如 SWE-Marathon）用的是不同 harness，建議工程師自行用實際任務測試，而非只看官方發布的排行榜。

🎯 **實務啟示**

對已經在用 OpenAI SDK 的團隊，Muse Wonder 的相容 API 讓遷移成本很低，可以先用 Muse Wonder（較低成本）驗證 agent 工作流，再視需求評估是否要升級到需要付費方案的 Muse Wonder Full。

🔗 **來源**
- 標題：Meta Launches Muse Wonder and Muse Wonder Full: Benchmarks, Pricing and How to Use It
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/13/meta-muse-wonder-muse-wonder-full-release/

#Meta #MuseWonder #AIAgent #LLM #AgenticAI #ComputerUse #MetaAI #DeveloperTools #APIIntegration #AIModels
