---
title: Z.ai Launches GLM-5.2 With a Usable 1M-Token Context, Two Thinking-Effort Levels,
  and No Benchmarks at Launch
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/14/z-ai-launches-glm-5-2-with-a-usable-1m-token-context-two-thinking-effort-levels-and-no-benchmarks-at-launch/
score: 96
model: google/gemma-4-31b-it:free
generated_at: '2026-06-15T21:15:46.233015'
---

📌 【Z.ai 最新發佈】GLM-5.2 帶來 1M 超長上下文，Coding Agent 的記憶力大躍進

在 AI 編程工具的競爭中，上下文視窗（Context Window）的大小決定了 AI 能「一次讀多少程式碼」。Z.ai 最近快速迭代，在四個月內接連推出四款旗艦級模型，最新發佈的 GLM-5.2 直接將上下文視窗推升至 100 萬個 Token。

這意味著 AI 不再需要頻繁地對程式碼進行摘要（Summarization），而是能將中型專案的整個 Repository 直接放入工作記憶中。

🤔 **擺脫頻繁摘要，讓 AI 真正「讀懂」整個專案**

目前的 Coding Agent 常面臨一個痛點：當專案規模較大時，受限於上下文長度，AI 必須不斷地對檔案進行截斷或摘要，這往往導致關鍵的邏輯細節在傳遞過程中遺失。

GLM-5.2 提供的 1M-token 視窗，讓 Agent 可以同時持有原始碼、測試案例、設定檔以及完整的對話歷史。這種從「碎片化閱讀」到「全域閱讀」的轉變，將大幅改變 AI 處理複雜專案的實作方式。

🧪 **快速迭代的產品線與模型規格**

Z.ai 的發佈速度極快，從 2 月的 GLM-5 到 4 月的 GLM-5.1，再到現在的 GLM-5.2，幾乎每個月都有重大更新。

雖然官方未詳細說明 GLM-5.2 的具體架構，但根據社群資訊，其基底為一個 7,440 億參數的混合專家模型 (MoE)，每次 Token 生成僅激活 400 億個參數。GLM-5.1 則是在相同骨幹上透過重新調整後訓練 (Post-training) 完成的。

💡 **新增「思考強度」設定：High 與 Max 模式**

除了記憶力提升，GLM-5.2 引入了兩種思考努力程度（Thinking-effort levels）：**High** 與 **Max**。

- **Max 模式**：Z.ai 建議在處理複雜、多步驟的編程任務時使用。
- **實作對接**：在 Claude Code 中，`/effort` 指令可控制此設定，其中 `xhigh`、`max` 與 `ultracode` 等選項均對應到 GLM-5.2 的 Max 模式。

⚠️ **缺乏基準測試數據，效能仍需實測驗證**

這篇發佈最令人意外的一點是：Z.ai 在發表 GLM-5.2 時，**完全沒有提供任何基準測試 (Benchmarks) 分數**。

目前沒有 SWE-bench、Terminal-Bench 或 Code Arena 的數據。這次發佈的重點完全放在「可用性」、「上下文長度」以及「開源路線圖」上。對於追求量化指標的工程師來說，目前的效能表現仍是一個未知數，需要實際部署後才能確認 1M 視窗的實際召回率（Recall）表現。

🎯 **工程實踐：如何在 Claude Code 中配置 GLM-5.2**

對於想要嘗試 1M 上下文的開發者，可以透過以下方式配置：

1. **修改設定檔**：編輯 `~/.claude/settings.json`，將 Sonnet 與 Opus 的槽位指向 GLM-5.2 的 1M 變體。
2. **調整視窗**：調高 `auto-compact window` 數值，確保 Agent 能充分利用完整的上下文。
3. **端點切換**：使用相容於 Anthropic 的端點進行 base-URL 替換。
4. **啟動最高效能**：在 Session 中執行 `/effort` 並選擇 `max`。

🔗 **相關資訊**
📝 Z.ai Launches GLM-5.2 With a Usable 1M-Token Context, Two Thinking-Effort Levels, and No Benchmarks at Launch
👤 Michal Sutter @ MarkTechPost
🔗 來源：https://www.marktechpost.com/2026/06/14/z-ai-launches-glm-5-2-with-a-usable-1m-token-context-two-thinking-effort-levels-and-no-benchmarks-at-launch/

你認為 1M 的上下文長度會讓 RAG (檢索增強生成) 變得不再重要嗎？歡迎在評論區分享你的看法 👇

#GenAI #LLM #CodingAgent #GLM5 #Zai #SoftwareEngineering #AIProgramming
