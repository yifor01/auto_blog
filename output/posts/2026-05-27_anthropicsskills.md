---
title: "anthropics/skills"
source: GitHub Trending
url: https://github.com/anthropics/skills
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-05-27T20:57:52.940151
---

📌 【Anthropic 官方範例】Claude 的「技能」系統到底能做什麼？

你以為 Claude 只能回答問題？它其實可以像員工一樣執行公司流程——只要給它一份技能手冊。

🤔 **從聊天助手到可執行的工作流程**

Anthropic 在 GitHub 公開的 skills 儲存庫展示了 Claude 如何透過「Skill」動態載入指令、腳本與資源，以完成特定任務。這意味著，只要將一套寫好的 SKILL.md 放入對應資料夾，Claude 就能依照該流程產出符合公司品牌指引的文件、依照內部工作流程分析資料，甚至自動化個人日常事務。

🧪 **儲存庫結構與實作範例**

每個技能都是獨立的資料夾，內含 SKILL.md（說明與中繼資料）以及所需的腳本或範本。倉庫中包含：

- 文件建立與編輯技能（docx、pdf、pptx、xlsx），這些正是 Claude 內建文件功能的底層實作。
- 創意應用（藝術、音樂、設計）範例。
- 技術任務（網頁應用測試、MCP 伺服器產生）。
- 企業工作流程（內部溝通、品牌管理等）。

許多技能採用 Apache 2.0 授權，可直接複製或作為自訂技能的起點。

💡 **如何運用這些範例建立自己的技能**

1. 瀏覽對應資料夾，閱讀 SKILL.md 了解所需的輸入、輸出與執行步驟。
2. 依照同樣的結構建立新資料夾，撰寫專屬的指令與腳本。
3. 技能完成後，將其放置於 Claude 能存取的技能目錄，下次對話時 Claude 會自動載入並使用。

這種「插件式」設計讓開發者無需修改 Claude 核心模型，即可針對特定業務場景擴展能力。

⚠️ **目前已知的限制與注意事項**

- 倉庫主要提供範例與參考實作，並未涵蓋所有可能的企業場景。
- 技能的效能依賴於所提供腳本的品質與 Claude 的指令遵循能力。
- 部分技能（例如 docx、pdf）僅為原始碼公開，實際使用時仍需確認相依函式庫的可用性。
- 目前文件未提及效能基準或正式的安全審核報告。

🎯 **給開發者的實務建議**

- 先從倉庫內的文件技能（docx、pdf）入手，觀察 Claude 如何處理格式與樣式。
- 參考「Using skills in Claude」與「How to create custom skills」文件，了解註冊與觸發機制。
- 若團隊有固定的工作流程（例如週報產出、資料清洗），可嘗試將該流程寫成 SKILL.md，讓 Claude 成為流程自動化的夥伴。
- 開源授權允許自由修改與內部重新發布，適合作為內部工具平台的基礎。

🔗 **資源連結**
📂 倉庫：https://github.com/anthropics/skills
📖 Agent Skills 標準說明：https://agentskills.io
📄 相關文件：What are skills?、Using skills in Claude、How to create custom skills、Equipping agents for the real world with Agent Skills

你有想把哪些重複性工作交給 Claude 嗎？歸類你的想法或已經嘗試的技能，歡迎在留言區分享 👇

#Anthropic #Claude #AIskills #GitHub #開源 #自動化 #企業AI
