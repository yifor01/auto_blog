---
title: anthropics/skills
source: GitHub Trending
url: https://github.com/anthropics/skills
score: 129
model: google/gemma-4-31b-it:free
generated_at: '2026-06-12T20:32:17.555716'
---

📌 【Anthropic 開源】Claude 可插拔「Skills」讓 LLM 變身專業助理

Claude 的功能不再只能靠提示詞，而是可以動態載入 **Skills** ——一套可重用、可自訂的任務模組。Anthropic 把這套系統完整開源在 GitHub，讓工程師直接拿來改造自己的工作流。

🤔 **LLM 只靠提示，怎麼保證執行力？**  
在實務中，我們常需要讓模型遵守公司品牌、套用既有資料流程，甚至自動產出文件。僅靠文字提示往往不夠穩定、難以重複。Anthropic 的 **Skills** 把「說明書、腳本、資源」打包成獨立資料夾，Claude 執行時會即時載入，像安裝插件一樣把專業能力注入模型。

🧪 **開源示例：從藝術到企業全覆蓋**  
這個 GitHub repo（anthropics/skills）提供了多樣化的範例：

- 🎨 **創意類**：藝術、音樂、設計生成  
- 🛠 **技術類**：Web 應用測試、MCP 伺服器產生  
- 📊 **企業類**：品牌文件生成、內部流程自動化  

每個 Skill 都有獨立資料夾，內含 `SKILL.md`（指令與 metadata）以及執行腳本，結構清晰、即插即用。

 **文件處理 Skill 已內建**  
repo 中還包含了支援 **docx、pdf、pptx、xlsx** 的文件創建與編輯模組，這些正是 Claude 在產品介面背後使用的核心能力。所有模組皆採 Apache 2.0 授權，可自由商業使用或二次開發。

⚠️ **限制與注意事項**  
- 目前僅提供 **Claude** 專屬的 Skills 格式，其他模型需自行適配。  
- 部分技能依賴外部服務或特定環境（例如測試 Web App 需要可執行的測試框架），使用前需確認相依套件。  
- 雖然多數範例已開源，但完整的商業級部署仍需自行完成安全與資源管理。

🎯 **實務建議：如何把 Skills 融入你的產品**  
1. **先定義重複任務**：列出你團隊每天需要的「可標準化」工作，例如客製化報告、資料清理。  
2. **參考現成 Skill**：在 repo 中找到相似功能的資料夾，直接 copy 並調整 `SKILL.md` 內的指令與參數。  
3. **測試與迭代**：使用 Claude 的 API 載入自訂 Skill，觀察回傳結果，根據錯誤訊息微調腳本或說明文。  
4. **版本管理**：將每個 Skill 放在獨立 Git 子模組，方便團隊協作與 CI/CD 部署。  

🔗 **原始碼 & 文件**  
📝 Repository: **anthropics/skills**  
👤 作者：Anthropic（anthropics）  
🔗 GitHub：<https://github.com/anthropics/skills>  
📚 了解 Agent Skills 標準：<https://agentskills.io>  

💬 你有在自己的工作流中使用 LLM 代理人嗎？哪個 Skill 最符合你的需求？歡迎在下方留言分享你的實作心得 👇

#AI #LLM #Claude #Anthropic #OpenSource #AgentSkills #Automation #DevOps #MachineLearning #GitHubTrending
