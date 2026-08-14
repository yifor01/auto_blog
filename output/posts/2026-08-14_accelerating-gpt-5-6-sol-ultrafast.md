---
title: Accelerating GPT-5.6 Sol Ultrafast
source: Hacker News
url: https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai
model: claude-code/sonnet
generated_at: '2026-08-14T07:32:27.863170'
score: 83
---

📌 750 tokens/秒：Cerebras 讓 GPT-5.6 Sol 快到「等不到你分心」

TL;DR：Cerebras 晶片跑 GPT-5.6 Sol，同精度下比對手快 5 到 11 倍。

以往用 AI，速度和智慧只能二選一：模型越強、算得越久，你越常盯著轉圈圈的 loading 圖示發呆。Cerebras 與 OpenAI 這次聯手推出 Ultrafast Mode，宣稱把這個取捨直接打破。

🤔 **背景：智慧與速度的老矛盾**

隨著模型規模擴大，運算與資料搬移成本跟著提高，回應時間也跟著變慢，使用者往往得在「等久一點拿到高品質結果」和「快一點但品質打折」之間二選一。Ultrafast Mode 是 OpenAI API 新推出的服務層級，率先開放給部分客戶，由 Cerebras 提供算力，目標是讓前沿智慧也能用在時間敏感、任務關鍵的工作上。

🧩 **硬體解法：把權重留在晶片上**

Cerebras 指出，快速的前沿推理本質上是一個資料搬移問題。在 GPU 上，大型模型推理常受限於記憶體頻寬，因為權重必須在晶片內外的記憶體之間反覆搬移才能生成下一個 token。Cerebras 的做法是反其道而行：在每片晶圓級晶片上封裝 44 GB 的 SRAM，讓權重常駐晶片上，token 得以在跨晶圓、pipeline 化的模型層之間不中斷地流動。這套架構理論上能隨模型規模成長平順地擴展，為未來更大的前沿模型延續速度優勢。

📊 **實測數字：11 小時做完 78 小時的題目**

依 Artificial Analysis 回報的輸出速度換算，GPT-5.6 Sol 在 Ultrafast 模式下可達每秒 750 個輸出 token，比 Fable 5 快 11 倍，比 Opus 4.8 的 Fast 模式快 5 倍。Cerebras 也拿 Humanity's Last Exam（HLE，2500 題橫跨化學、經濟、文學等領域、通常只有博士能答的難題）做對照：GPT-5.6 Sol Ultrafast（搭配 Codex、xhigh reasoning，測試於 7 月 10 日）11 小時 11 分鐘答完全部 2500 題；Claude Fable 5（搭配 Claude Code、xhigh reasoning，測試於 7 月 13 至 15 日）則花了 78 小時 27 分鐘，超過三天不間斷運算，兩者準確度相近，但 Ultrafast 快了近 7 倍。另外在 GDP-Val（一個評估「經濟價值知識工作」任務的 benchmark，測試於 7 月 31 日，於 Codex 內以 medium reasoning 比較 GPT-5.6 Sol 與其 Ultrafast 版本）上，Ultrafast 端到端提速 5.6 倍且沒有品質下滑。

💡 **快到讓你來不及分心**

OpenAI 產品端的 Rohan Varma 表示，Ultrafast 讓 AI 能跟上使用者思考、寫程式、協作的速度；OpenAI 研究員 Jeffrey Wang 則提到，以往可能要等好幾分鐘才能看到任務完成，現在往往在他還沒來得及切換到別的視窗前就已經跑完，直接提升了生產力。文章也點出幾個高風險應用場景：處理正式環境故障排除、對抗性資安攻擊下的即時偵測與應變，這類每一秒都攸關損失規模的工作。

⚠️ **現況：限量開放中**

GPT-5.6 Sol 的 Ultrafast 模式目前僅以有限預覽（limited preview）形式開放給少數客戶，隨算力擴增才會逐步開放更多使用者。

🎯 **實務啟示**

如果你的應用場景本身就對延遲敏感（例如即時故障排除、資安應變、或需要頻繁往返確認的 Agent 工作流），Ultrafast 這類「不犧牲品質換取速度」的服務層級值得關注；至於一般可以平行處理、不急著等結果的任務，仍可以留在標準處理層級，把高速資源留給真正卡在關鍵路徑上的工作。

🔗 **來源**
- 標題：Accelerating GPT-5.6 Sol Ultrafast
- 作者／機構：Cerebras（經 Hacker News 轉載，原始投稿者 pr337h4m）
- 連結：https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai

#Cerebras #OpenAI #GPT5 #UltrafastMode #WaferScaleEngine #LLMInference #AIInfrastructure #HumanitysLastExam #LowLatencyAI #FrontierModels
