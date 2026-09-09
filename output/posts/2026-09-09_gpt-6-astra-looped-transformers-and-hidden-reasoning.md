---
title: GPT-6 Astra, Looped Transformers, and Hidden Reasoning
source: Sebastian Raschka
url: https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and
model: claude-code/sonnet
generated_at: '2026-09-09T19:58:46.909580'
score: 107
---

📌 GPT-6 Astra 評測：真正的突破在於學會操作電腦

TL;DR：GPT-6 Astra 刷新多項基準，但其電腦操作能力與 Mac 叢集訓練法才是工程師該關注的重點。

如果一個模型在邏輯推理基準上從 7.8% 一口氣衝到 99.9%，你會覺得它進步的是「思考」；但 Sebastian Raschka 在實測後發現，OpenAI GPT-6 Astra 真正讓人驚豔的地方，其實是它用滑鼠操作 MS Paint 畫圖的樣子。

🤔 **上週發布，作者用了幾天就給出「目前用過最好」的評價**

Raschka 表示，GPT-6 Astra 上週發布時聲勢浩大，他實際使用幾天後認為這是他目前用過最好的模型。相較前代 GPT-5.6，Astra 在寫作、數學、程式碼等幾乎所有類別都有躍進，但最明顯的進步集中在圖形類任務與 3D 渲染、動畫相關的展示上。

📊 **ARC-AGI-3 從 7.8% 衝到 99.9%，但編碼代理指標領先幅度有限**

在基準測試上，GPT-6 Astra 於數學與程式碼表現亮眼，其中 ARC-AGI-3（測量邏輯解謎與泛化能力的基準）拿下 99.9%，相較之下 GPT-5.6 Sol 僅有 7.8%。不過作者也提醒，更貼近真實使用情境的 Artificial Analysis Coding Agent Index v1.4 與綜合性的 Intelligence Index v4.2 顯示，Astra 雖處於前沿，但並未大幅拋開對手。

值得注意的是，這些獨立基準測試使用的評測工具（harness）並不統一：GDPval-AA 與 AA-Briefcase 用的是開源、精簡的 Stirrup harness，Terminal-Bench v2.1 用 Terminus 2，τ³-Banking 用 τ-Bench harness。作者指出，模型訓練時通常只針對一種主要 harness 最佳化，因此這些跨 harness 的代理型評測，可能低估了 Astra 在自家主力 harness 下的真實表現。

💡 **AGENTS.md、SKILL.md 是不是該重寫了？**

Raschka 提到一個實務側記：一位同事(以及 Claude Code 團隊的建議)認為,既然新一代 LLM 對 prompt 的理解力更強、解題能力更好，不妨考慮刪除或封存既有的 AGENTS.md、SKILL.md 內容,因為過度的手把手說明反而可能限制模型發揮，導出較差的解法。這不代表要完全捨棄 SKILL.md（重複性工作流程仍能因為重用而提升效率），而是提醒工程師：舊的指令描述未必仍是最佳解，該考慮更新或重新生成。

🧩 **用 Mac Mini 叢集訓練模型「操作電腦」**

Astra 在圖像與渲染任務上格外突出，涉及圖形介面操作時，也展現出電腦操作（computer use）能力，也就是透過 Codex/ChatGPT App 直接操作本機軟體。作者示範用 Astra Medium 與 High 兩種等級，讓模型用滑鼠在瀏覽器版 MS Paint 中重繪一張他的照片(為了省 token，沒有用 Extra High 或 Max)，展示出模型不只會畫圖，還能透過遊標實際操作介面。

這與近期報導的 OpenAI 採購數萬臺 Mac Mini 與 Mac Studio 用於強化學習相呼應。這些 Mac 並非用來做模型本身的訓練運算(GPU 更適合這件事)，而是作為讓模型在訓練過程中「見識」macOS 環境的介面。其基本流程如下：

1. 給模型一個任務提示，例如「打開某 App 並完成某操作」
2. 由 harness 提供 macOS 介面的螢幕截圖
3. LLM 預測滑鼠、鍵盤動作(點擊、按鍵、捲動等)
4. harness 在 Mac 上執行這些動作
5. 提供動作後的最新螢幕截圖
6. 重複 2 到 5，直到任務成功或失敗
7. 用成功／失敗訊號與驗證器(grader)作為訓練回饋，這與可驗證獎勵的強化學習(RLVR)概念類似

作者認為，這類電腦操作能力可類比人形機器人：不是效率最高的解法(組裝線上專用機械仍更有效率)，卻具備高度泛用性。因為現實中大量軟體並沒有暴露 CLI 介面，與其等所有工具都補上 API，不如讓模型直接學會操作圖形介面。

🎯 **實務啟示**

對工程師而言，這意味著未來一段時間，電腦操作能力會同時在模型層與 harness 層持續打磨,不只用於編碼與圖形任務，也可能延伸到日常辦公自動化。同時，若你的 Agent 專案仍仰賴大量 AGENTS.md／SKILL.md 說明文件，這篇分析提醒了一個值得驗證的假設：這些文件是否仍在幫模型，還是已經開始限制它。

🔗 **來源**
- 標題：GPT-6 Astra, Looped Transformers, and Hidden Reasoning
- 作者／機構：Sebastian Raschka
- 連結：https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and

#GPT6Astra #OpenAI #LLM #ComputerUse #AIAgents #ReinforcementLearning #RLVR #Benchmarking #AIEngineering #MachineLearning
