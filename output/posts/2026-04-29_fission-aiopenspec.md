---
title: "Fission-AI/OpenSpec"
source: GitHub Trending
url: https://github.com/Fission-AI/OpenSpec
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-04-29T20:17:21.276649
---

📌 【Fission-AI 新工具】自然語言驅動，AI 幫你寫規格又實作

還在複製貼上 AI 生成的程式碼片段，然後手動整理需求文件嗎？Fission-AI 團隊推出的 OpenSpec 正在 GitHub Trending 上飆升（單日 325 stars），它試圖解決 AI 開發中最混亂的一環：如何將「想法」結構化地轉化為「可執行的工程任務」。

🤔 **從「寫 Code」轉向「管流程」，AI 開發的新解法**

目前的 AI 輔助工具多著重於單一程式碼的生成，但往往忽略了需求規格（Spec）與實作細節的同步。OpenSpec 的核心理念是「流動而非僵化、迭代而非瀑布」，它將 AI Agent 深度整合進開發流程，讓開發者用自然語言指令，就能自動產生從提案到實作的所有工程文件。

🧪 **Artifact-Guided Workflow：用指令定義開發週期**

OpenSpec 重新設計了開發工作流，核心在於生成結構化的 Artifacts（交付物）。你可以直接對 AI 下達指令，例如 `/opsx:propose "add-dark-mode"`，系統會自動生成以下架構：

*   **proposal.md**：描述動機與變更範圍
*   **specs/**：定義需求與場景
*   **design.md**：技術實作方案
*   **tasks.md**：實作清單（Checklist）

 **從想法到歸檔，一條龍自動化**

最令人驚豔的是其指令集的連貫性。在生成規格後，你只需輸入 `/opsx:apply`，AI 就會根據 tasks.md 自動執行實作（如新增 Theme Provider、設定 CSS Variables 等）。完成後透過 `/opsx:archive`，系統會將此次變更歸檔至歷史紀錄，並更新全域規格。這讓專案無論是個人 Side Project 還是大型企業級應用（Brownfield 與 Greenfield 皆宜），都能保持高度的可維護性。

💡 **不只生成程式碼，而是建立「工程共識」**

OpenSpec 的價值在於它強迫 AI 產出的內容具備結構。它不僅僅是寫 Code，而是透過 `proposal` 到 `archive` 的閉環，確保每一次的 AI 輔助都有跡可循。對於 GenAI 工程團隊來說，這解決了「AI 生成的東西很難管理」的痛點。

⚠️ **環境限制與學習曲線**

目前 OpenSpec 需要 Node.js 20.19.0 或更高版本，且主要依賴特定的 CLI 指令（如 `/opsx:new`, `/opsx:verify` 等）。對於習慣傳統 Git Flow 的團隊，可能需要時間適應這種「指令驅動」的新模式。此外，其擴充指令（如 `/opsx:bulk-archive`）的具體行為尚待社群進一步驗證。

🎯 **想試試看？三步驟上手**

如果你對這種新型態的開發模式感興趣，現在就可以在終端機嘗試：
1. 安裝：`npm install -g @fission-ai/openspec@latest`
2. 初始化：`openspec init`
3. 開始提案：`/opsx:propose "你的功能想法"`

🔗 **專案連結**
📝 Fission-AI/OpenSpec
🔗 GitHub：https://github.com/Fission-AI/OpenSpec
💬 Discord：加入 OpenSpec Discord 獲取支援
🐦 X：追蹤 @0xTab 獲取最新更新

你覺得這種「Spec as Code」的模式，會是 AI 開發的主流嗎？歡迎留言討論 👇

#AI #OpenSpec #FissionAI #DevTools #GitHubTrending #軟體工程 #LLM #自動化開發
