---
title: "Yeachan-Heo/oh-my-claudecode"
source: GitHub Trending
url: https://github.com/Yeachan-Heo/oh-my-claudecode
score: 99
model: gpt-4o-free
generated_at: 2026-03-26T20:04:00.205454
---

📌 **oh-my-claudecode：讓 Claude Code 零學習曲線**

你是否覺得 Claude Code 很強，但不知道該怎麼下指令？一個開源專案把多 Agent 工作流包裝成簡單插件，讓你直接說「我想建立任務管理 API」，其餘全自動。

🤔 **工程師需要的不只是更強的模型，而是更簡單的使用方式**

Claude Code 本身提供了強大的程式輔助能力，但對許多開發者來說，學習指令、掌握工作流仍是門檻。當團隊想快速原型或需要分工協作時，如何讓 AI 變得像「團隊成員」一樣可直接指揮，成為實務上的痛點。

🧪 **透過插件與工作流設計降低使用門檻**

oh-my-claudecode 是一套針對 Claude Code 的多 Agent 編排插件。安裝方式僅需兩行指令：

```
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
/plugin install oh-my-claudecode
```

安裝後，透過 `/setup` 與 `/omc-setup` 完成環境初始化。核心功能包括：

- **深度訪談（/deep-interview）**：採用蘇格拉底式提問，幫助使用者在寫 code 前澄清需求、暴露假設，確保明確知道要建什麼。
- **Team 模式（v4.1.7 起為標準 orchestration surface）**：以 `team-plan → team-prd → team-exec → team-verify → team-fix` 的階梯式流程執行，等同於讓多個 Agent 分擔規劃、需求、執行、驗證與修補。
- **原生 Team 支援**：只需在 `~/.claude/settings.json` 加入  
  ```json
  { "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }
  ```  
  即可啟用內建的團隊協作功能。

💡 **核心價值：零學習曲線與結構化協作**

使用者不需要先學 Claude Code 的指令集，只需透過對話式的 `/deep-interview` 表達想法，系統會自動引導進入 Team 流程。整個過程被拆解為可見的階段，使得即使是不熟悉 AI 編程的工程師，也能在明確的步驟中看到進展，降低認知負擔。

🔍 **深入分析：為什麼這種設計對 GenAI 實踐有幫助？**

1. **需求澄清前置**：深度訪談階段強制使用者思考問題本質，避免因模型過度自信而產生的假設錯誤。
2. **流程化執行**：Team 流程把原本可能混雜的指令序列，變成可重複、可審計的階段，適合團隊代碼審查與版本控制。
3. **插件化與零侵入**：透過插件機制，使用者仍可保留原本的 Claude Code 工作流，只在需要時啟用 OMC 的功能，彈性高。

⚠️ **已知限制（基於目前說明）**

- 依賴於 Claude Code 的可用性；若底層模型或 CLI 有變動，可能需要同步更新插件。
- 目前文件著重於安裝與基本使用，尚未見大規模實證數據（如開發時間縮減比率）來量化其效益。
- Team 流程預設為五個階段，對於極簡或極複雜的專案可能需要自行調整腳本。

🎯 **實務啟示：如何在團隊中試用**

- 在個人專案先以 `/deep-interview` 練習需求澄清，熟悉對話流程。
- 當需要跨人協作時，切換至 `/team 3:executor " fix all TypeScript errors "` 觀察階梯式執行是否符合團隊的 SOP。
- 透過 Discord 社群（專案頁面提供連結）取得使用經驗與問題回報，隨時追蹤更新。

🔗 **專案連結**
📂 oh-my-claudecode  
👤 Yeachan-Heo  
🔗 https://github.com/Yeachan-Heo/oh-my-claudecode  如果你已經在使用 Claude Code，或正在評估如何讓 AI 成為團隊的生產力夥伴，歡迎在留言區分享你的體驗或疑問 👇

#AI #ClaudeCode #GenAI #開發工具 #多Agent #工程效率 #oh-my-claudecode
