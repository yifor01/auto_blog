---
title: "Claude Code as a Daily Driver: Claude.md, Skills, Subagents, Plugins, and MCPs"
source: Hacker News
url: https://arps18.github.io/posts/claude-code-mastery/
score: 104
model: tencent/hy3-preview:free
generated_at: 2026-05-27T20:54:33.767521
---

📌 **Claude Code 進階使用指南**  

你以為 Claude Code 只是聊天機器人？進階用戶已把它變成可編程的 AI 助手，記憶、自訂指令與平行會話都成為日常工作的一部分。  

🤔 **為何需要超越基礎使用？**  
隨著 Claude Code 在終端機中的普及，許多開發者仍停留在「提示‑等待」的階段，將其視為較聰明的自動補全。然而，當你開始把它當作需要防護導軌的自主代理人時，工作流程會產生質的飛躍——這正是 Boris Cherny 與 Anthropic 團隊所強調的核心原則。  

🧪 **指南的結構與重點**  
這份由 arps18 撰寫的 Hacker News 熱文（306 點、210 則留言）以目錄式方式逐層深入：  
1. **Claude Code Beyond the Basics** – 認識從聊天機器人到可編程代理人的概念轉移。  
2. **.claude 目錄的正確理解** – 專案層級的設定檔與資源如何組織。  
3. **CLAUDE.md 的撰寫方式** – 包含官方範例與社群值得參考的檔案。  
4. **CLAUDE.local.md 作為日常駐檔** – 如何在不影響共享設定的情況下客製化個人工作流。  
5. **Skills 的深入探討** – 什麼是 Skill、如何撰寫真實範例（如 Go API 規範）以及值得安裝的熱門 Skill。  
6. **自訂 Subagents 的建構** – 以 /pr-review 為例走過完整流程，並列出社群熱門 Subagents。  
7. **Plugins 與 Marketplace** – 擴充功能的安裝與使用方式。  
8. **較少被使用的 Claude Code 指令** – 例如 /goal 與內建的 Ralph Loop。  
9. **MCPs 作為力量工具** – 真實的 Obsidian 工作流示範。  
10. **優化日常工作流程** – 如何讓上述元素隨時間複利增效。  
11. **來自 Anthropic 團隊的建議**  
12. **資源與結語**  

💡 **核心收穫：從工具到夥伴的心態轉變**  
指南反覆強調，真正的進階使用不只是學會更多指令，而是建立一套「防護導軌 + 記憶 + 自訂」的系統：  
- 透過 .claude 目錄與 CLAUDE.md 為專案設定明確的規則與預設。  
- 以 Skills 封裝可重複使用的邏輯（例如程式碼風格檢查），減少重複輸入。  
- 以 Subagents 實現特定任務的自主代理人（如程式審查），達到「一次設定、多次復用」的效果。  
- 透過 Plugins 與 MCPs（Model Context Protocol）擴充外部工具整合，例如直接在 Obsidian 中編輯與檢索筆記。  
這些元素組合起來，讓 Claude Code 不再是被動回應的聊天機器人，而是能記住上下文、執行預先定義工作流並且隨專案成長而演進的夥伴。  

⚠️ **指南的適用範圍與限制**  
- 內容假設讀者已具備基本的 Claude Code 終端機使用經驗。  
- 重點在於設定檔案、Skills、Subagents 等客製化層面，未涉及模型本身的訓練或推論細節。  
- 所有範例與建議來自作者個人經驗與社群分享，未附帶正式的效能基準測試或控制實驗結果。  
- 某些進階功能（如 MCPs）仍屬較新的實驗性特性，未來可能有 API 調整。  

🎯 **實務建議：從小處開始，逐步累積**  
1. 先閱讀官方 CLAUDE.md 範例，了解其結構與變數用法。  
2. 在 .claude 目錄中加入一個簡單的 Skill（例如自訂的 lint 指令），驗證載入與執行。  
3. 嘗試撰寫一個專屬的 Subagents，先從 /pr-review 這類常見工作流入手。  
4. 依需求瀏覽 Plugin Marketplace，選擇與你編輯器或版控系統相容的擴充。  
5. 定期檢視 CLAUDE.local.md，將有價值的個人客製化遷移至專案共享設定，以利團隊協同。  

🔗 **原始參考**  
📝 Claude Code as a Daily Driver: Claude.md, Skills, Subagents, Plugins, and MCPs  
👤 作者：arps18  
🔗 連結：https://arps18.github.io/posts/claude-code-mastery/  

你目前的 Claude Code 工作流是哪一種？歡迎在留言區分享你正在使用的 Skills、Subagents 或是自訂技巧 👇  

#AI #ClaudeCode #開發工具 #程式設計 #Anthropic #技巧分享 #工作流程優化
