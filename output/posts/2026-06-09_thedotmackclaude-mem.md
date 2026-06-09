---
title: thedotmack/claude-mem
source: GitHub Trending
url: https://github.com/thedotmack/claude-mem
score: 97
model: google/gemma-4-31b-it:free
generated_at: '2026-06-09T20:34:23.446362'
---

📌 **【GitHub Trending】讓 Claude Code 擁有「長期記憶」：claude-mem 持久化記憶壓縮系統**

在使用 Claude Code 或 Gemini CLI 進行開發時，最令人沮喪的莫過於每次開啟新 Session，AI 就像失憶一樣，必須重新讀取專案背景或重複相同的指令。雖然 Context Window 越來越大，但「記憶的持久化」與「高效能檢索」依然是開發者的痛點。

🤔 **Context Window 很大，但為什麼我們仍需要記憶系統？**

即便模型能處理大量 Token，但每次將所有歷史紀錄塞進 Prompt 不僅浪費 Token，更會導致模型在冗長的上下文中遺失焦點（Lost in the Middle）。真正的解決方案不是單純增加容量，而是如何將「有價值的經驗」壓縮並持久化，讓 AI 在新會話中能立即找回之前的進度。

🧪 **自動化捕捉與語義摘要的設計邏輯**

`claude-mem` 提出了一套持久化記憶壓縮系統，其核心運作流程如下：
1. **自動捕捉 (Automatic Capture)**：系統會自動記錄 AI 在執行過程中的工具使用觀察（tool usage observations）。
2. **語義摘要 (Semantic Summaries)**：將捕捉到的碎片化資訊轉換為結構化的語義摘要，而非簡單的文字紀錄。
3. **跨會話可用 (Cross-session Availability)**：將這些摘要儲存並在未來的新 Session 中重新提供給 AI。

這意味著 Claude 不再只是在單次對話中運作，而是能維持對專案知識的連續性，即便 Session 結束或重新連接，之前的開發脈絡依然存在。

💡 **從「碎片資訊」到「結構化知識」的轉化**

這項工具的核心價值在於它將「過程」轉化為「知識」。它捕捉的不是對話紀錄，而是「工具使用的結果」。例如，如果 AI 之前透過 `ls` 或 `grep` 探索過專案結構，`claude-mem` 會將這些探索結果壓縮成摘要，讓 AI 在下次啟動時直接知道「專案結構是什麼」，而不需要重新執行一遍指令。

⚠️ **安裝路徑的關鍵細節：請勿僅使用 npm install**

開發者在安裝時需要特別注意：雖然該專案發佈在 npm 上，但執行 `npm install -g claude-mem` 僅會安裝 SDK/函式庫，**並不會**註冊插件鉤子 (plugin hooks) 或設定 Worker 服務。

若要完整啟用記憶功能，必須使用專用的安裝指令來完成環境配置。

🎯 **快速上手：三秒鐘讓你的 AI 助手不再失憶**

如果你正在使用 Claude Code 或 Gemini CLI，可以根據環境選擇以下安裝方式：

- **Claude Code (最快方式)**：
  直接在 Claude Code 內執行：`/plugin marketplace add thedotmack/claude-mem`
  或使用指令：`npx claude-mem install`

- **Gemini CLI (自動偵測 ~/.gemini)**：
  `npx claude-mem install --ide gemini-cli`

- **OpenCode**：
  `npx claude-mem install --ide opencode`

安裝完成後重啟 CLI，之前的會話上下文將會自動出現在新會話中。

🔗 **專案連結**
📝 claude-mem: Persistent memory compression system built for Claude Code
👤 作者：thedotmack
🔗 GitHub：https://github.com/thedotmack/claude-mem

對於經常在大型專案中切換 Session 的工程師來說，這種「記憶壓縮」機制能顯著提升開發效率。你目前是如何管理 AI 的長短期記憶的？歡迎在下方分享你的 Workflow 👇

#AI #ClaudeCode #GeminiCLI #GitHubTrending #LLM #ContextManagement #開發工具 #生產力
