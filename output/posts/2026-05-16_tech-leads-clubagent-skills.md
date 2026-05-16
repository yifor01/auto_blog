---
title: "tech-leads-club/agent-skills"
source: GitHub Trending
url: https://github.com/tech-leads-club/agent-skills
score: 88
model: tencent/hy3-preview:free
generated_at: 2026-05-16T19:40:18.691933
---

📌 Agent Skills：安全編程外掛庫  

你以為 AI 編程外掛越多越好？實際上，超過 13% 的市場技能藏有致命漏洞，隨便安裝可能讓你的環境暴露在風險中。  

🤔 **市場充斥未經驗證的 AI 技能，安全成隱憂**  
隨著 Cursor、GitHub Copilot、Claude Code 等輔助工具普及，開發者傾向從公開市場下載「Skill」來擴充 AI 能力。然而，這些技能多為社群貢獻，缺乏統一的安全審查，導致惡意程式或漏洞易於混入專案。  

🧪 **開放原始碼、靜態掃描與鎖檔完整性驗證**  
Agent Skills 採取全程開源、無二進位檔的模式：所有技能位於 `packages/skills-catalog/skills/<category>/skill/` 目錄，包含 `SKILL.md`、`templates/` 與 `references/`。在 CI/CD 流程中執行靜態程式碼分析（Snyk Agent Scan），並透過內容雜湊與 lockfile 確保不可變性。每項技能皆經人工審核，才被納入登記冊。  

🔍 **核心發現：100% 開源且經過安全驗證的技能庫**  
- 所有技能皆可公開檢視，無隱藏二進位。  
- 每項技能經過 Snyk 靜態掃描，未發現高危漏洞。  
- 透過內容雜湊與 lockfile，確保安裝時所取得的程式碼與發布時完全一致。  
- 支援 Antigravity、Claude Code、Cursor 等主流 AI 編程代理，可直接透過 CLI 安裝與更新。  

💡 **防禦深度設計：多層防護機制**  
CLI 內建 defence‑in‑depth 機制，包括：  
- 輸入資料清理與路徑隔離，防止惡意路徑遍歷。  
- 符號連結守衛，阻止經由鏈接寫入系統目錄。  
- 原子鎖檔，確保安裝或更新過程不被中斷導致檔案損毀。  
- 完整審計軌跡，紀錄每一次技能的下載、驗證與變更。  

⚠️ **目前僅支援特定代理，生態系統仍在擴充中**  
文件顯示已整合 Antigravity、Claude Code、Cursor，但未列出其他代理的適配狀況。此外，尚未公開針對技能執行效能或實際使用案例的量化數據，長期維護與社群貢獻的激勵機制亦需觀察。  

🎯 **實務啟示：優先使用經驗證的技能庫，降低供應鏈風險**  
- 在專案 CI 中加入 Agent Skills 的完整性檢查（hash 比對），可防止竄改。  
- 開發自有 Skill 時，參照其安全流程：靜態掃描、內容雜湊、人工審核與鎖檔機制。  
- 若需擴充至其他代理，可先檢查現有 CLI 是否提供同等的防禦深度，再進行適配。  

🔗 **資源連結**  
📂 GitHub Repo：https://github.com/tech-leads-club/agent-skills  
🌐 文件站：https://tech-leads-club.github.io/agent-skills/  

#AgentSkills #AI開發 #程式安全 #ClaudeCode #Cursor #開源安全 #供應鏈防護
