---
title: 'Jev: System One models for Prod, not God — with Diogo Almeida, CEO, TypeSafe
  AI'
source: Latent Space
url: https://www.latent.space/p/jev
model: nvidia/nemotron-3-ultra-550b-a55b:free
generated_at: '2026-09-22T20:36:25.553205'
score: 85
---

📌 InstructGPT 共同作者推 Jev：拋棄 RLHF、轉向 RLCD，為讓 AI 真正能在 Production 跑起來

TL;DR：TypeSafe AI 推出 System One 模型 Jev，用 RLCD 取代 RLHF，針對「校準決策」而非「人類偏好」最佳化，要讓 AI 像 regex 一樣消失在軟體背景裡。

Diogo Almeida 在發布影片 4,000 萬觀看、佔據 AI timeline 的那週，對 Latent Space 說：「情緒上從未這麼糟，像具殘軀；但理智上覺得整個 AI 領域終於有人看清現實了。」這位 InstructGPT (Ouyang et al., 2022) 共同作者、前 OpenAI 後訓練團隊成員，花了 2023–2024 年試圖修正他眼中的核心缺陷——**可靠性**，最後決定另起爐灶，創立 TypeSafe AI 並推出 Jev。

🎣 **聊天模型贏了世界，卻輸了自動化**

ChatGPT 的壓倒性成功，讓業界把所有資源壓在「自迴歸、聊天調教、序列到序列」這條單一路徑上。Diogo 指出：從 Function Calling、Structured Outputs 到 Reasoning，全都是在字串預測典範上打補釘的 hack。結果是：模型能解決納維-斯托克斯方程，卻無法可靠地自動化最基礎的軟體工作——幻覺、阿諛奉承、拒答、校準失效，一旦把模型埋進軟體依賴鏈裡，這些問題就會被放大成系統性風險。

🤔 **RLHF 的三條支流與「校準危機」**

Diogo 追溯 RLHF 三大源頭：Christiano et al. 2017（機械手臂後空翻）、Stiennon et al. 2020（學習摘要）、Ouyang et al. 2022（InstructGPT，他的作品）。他認為：為了訓練「討人類喜歡的助手」，我們犧牲了「可組合、可程式化、可自動化」的特質。RLHF 最佳化的是人類偏好評分，導致模型學會迎合評分者而非輸出認識論上誠實的機率；RLVR（以程式驗證獎勵）雖能解數學難題，卻加劇「鋸齒智能」，且難與其他軟體整合。

🧩 **RLCD：為 System One 任務學「認識論誠實的機率」**

Jev 的核心創新是 **RLCD（Reinforcement Learning for Calibrated Decisions）**，一種未公開的新技術。目標很單純：在 System One（快速、直覺、可組合）任務上，輸出「校準過的決策」與「認識論誠實的機率」。
- 不追求人類偏好分數 → 避免幻覺與阿諛奉承。
- 不追求程式可驗證的正確性 → 避免鋸齒智能與整合困境。
- 追求 **Calibration（校準）**：模型輸出的信心度＝實際正確率，讓下游程式能直接信任並分支。

Diogo 在 AIE 講座中詳細說明：為何一代訓練「有用助手」的過程，反而損害了模型作為自動化元件的能力。

📊 **拒絕公開 Benchmark，只看「智能 per Dollar」**

TypeSafe 公開拒絕建立 JevBench，也拒絕參與通用排行榜。Diogo 的理由：「You get what you optimize for.」若為了榜單分數調整資料與目標，就會偏離 Production 需求的北極星。他們自稱 **Data Lab 而非 Model Lab**——挑選正確任務、正確資料，比堆算力更重要（這就是他稱之為「最苦澀的教訓」）。甚至宣稱：「給我 10 億美元我也不會拿去預訓練。」

產品面上，Jev 提供：
- **長期支援（LTS）版本控管**，不搞滾動更新驚嚇下游。
- **Programming Primitives**：Guided Responses、Structured State、Computer Use、Structured Output——用結構化狀態取代巨大 System Prompt。
- **Intelligence per Dollar** 作為核心 KPI，追求速度與成本效益。

💡 **深入分析：從「巨大 Prompt」到「微小、可測決策」**

Diogo 主張開發者應將 AI 工作流拆解為 **小而可測量的決策單元**，再串接成控制流。Jev 的設計哲學是「消失在背景裡」——像 regex 一樣平淡無奇、極度可靠、不需時刻監控。
- **Coding Agents**：官方指南展示如何用 Jev 重構單一模型架構的 Coding Agent，引入共享狀態、子代理、多代理協作，跳出 KV Cache 瓶頸。
- **Dark Data & Computer Use**：真實世界的非結構化操作紀錄（Dark Data）是下一波資料金礦，Jev 的 Computer Use 能力正是針對此場景。
- **Inverse SaaS-pocalypse**：AI 不會取代 SaaS，而是超級充電既有軟體，讓現有應用獲得可程式化的智能層。

⚠️ **限制與現狀**

- RLCD 技術細節尚未公開發表，外部無法驗證理論優勢。
- Jev 目前以 API 形式提供，模型權重不開放，生態系仍在早期建構階段（Cookbook、Patterns 剛釋出）。
- 「拒絕 Benchmark」雖有哲學一致性，但也讓外部難以橫向比較基礎能力。

🎯 **實務啟示：給工程師的三個行動重點**

1. **重新審視評估指標**：若你的系統把 LLM 埋在關鍵路徑，請測量 **Calibration Error（ECE）** 而非單看 Accuracy/F1。模型敢不敢說「我不確定」，比答對多少題更重要。
2. **拆解 Prompt，建立 State Machine**：別再寫 2,000 token 的 System Prompt。把任務拆成「分類 → 擷取 → 決策 → 行動」的微小步驟，每步用 Jev 這類 System One 模型處理，並用 Structured State 傳遞上下文。
3. **把「拒答」當作 Bug 處理**：在自動化流程裡，模型拒答等於拋出未處理例外。選擇支援「零拒答、可控制輸出分布」的模型，或在上游加上 Guardrail 而非仰賴模型內建對齊。

🔗 **來源**
- 標題：Jev: System One models for Prod, not God — with Diogo Almeida, CEO, TypeSafe AI
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/jev

#Jev #TypeSafeAI #RLCD #SystemOne #LLM #AIEngineering #Calibration #InstructGPT #DiogoAlmeida #LatentSpace
