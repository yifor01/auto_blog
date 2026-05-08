---
title: "vercel-labs/skills"
source: GitHub Trending
url: https://github.com/vercel-labs/skills
score: 101
model: tencent/hy3-preview:free
generated_at: 2026-05-08T20:46:34.158825
---

📌 **vercel-labs/skills：統一 AI Agent 技能安裝的 CLI**

你是否曾為不同的 AI 編程助手（Claude Code、Cursor、Codex…）尋找對應的擴充功能而費神？一個新工具宣稱能一次搞定。

🤔 **AI Agent 生態正快速擴充，但技能分散在各個 repo，缺乏統一安裝方式**  
隨著 OpenCode、Claude Code、Codex 等工具相繼推出，開發者常需要在各個專案中手動搜尋、下載並設定對應的 skill（或稱 plugin、extension）。這種分散的做法不只浪費時間，也增加了版本管理的複雜度。

🧪 **提供一個名為 `skills` 的 CLI，支援多種來源與彈性安裝選項**  
該工具讓你可以透過以下方式安裝 skill：  
- GitHub 縮寫（`owner/repo`）  
- 完整 GitHub URL  
- 指定 repo 中的子路徑（例如 `…/tree/main/skills/web-design-guidelines`）  
- GitLab 或任何 git URL  
- 本地路徑  

安裝時可加入選項：  
- `-g, --global` 安裝至使用者目錄而非專案  
- `-a, --agent <agents...>` 指定目標 agent（如 `claude-code`、`codex`）  
- `-s, --skill <skills...>` 只安裝特定 skill（使用 `'*'` 代表全部）  
- `-l, --list` 僅列出可用技能而不安裝  
- `--copy` 複製檔案而非建立符號連結  
- `-y, --yes` 跳過所有確認提示  
- `--all` 一次將所有 skill 安裝至所有支援的 agent  

🔑 **核心功能：統一發現與安裝，減少重複搜尋**  
透過 `npx skills add vercel-labs/agent-skills --list` 你可以快速檢視某個 repo 中提供的所有 skill；再搭配 `--skill` 參數，只需安裝你真正需要的那些。這種「先列後裝」的流程讓開發者在嘗試新 agent 時能更快上手。

💡 **使用範例（僅根據官方 README 說明）**  
```bash
# 列出 vercel-labs/agent-skills repo 中的所有 skill
npx skills add vercel-labs/agent-skills --list

# 安裝特定兩項 skill
npx skills add vercel-labs/agent-skills --skill frontend-design --skill skill-creator

# 安裝含空格的 skill 名稱（必須加引號）
npx skills add owner/repo --skill "Convex Best Practices"

# 僅針對 Claude Code 安裝
npx skills add vercel-labs/agent-skills --agent claude-code
```

⚠️ **專案剛起步，文件與社群驗證仍在發展中**  
目前的說明主要來自 GitHub README，尚未看到大規模使用案例或第三方審核。支援的 agent 列表（OpenCode、Claude Code、Codex、Cursor 等 51 種以上）可能隨時更新，使用者在生產環境導入前建議先行測試相容性與穩定性。

🎯 **對於同時使用多個 AI 編程工具的開發者，值得嘗試此統一管理方式**  
如果你在不同專案中切換 Claude Code、Cursor、Codex 等工具，透過 `skills` CLI 可以減少重複尋找與手動複製 skill 的步驟，讓專案設定更具一致性。未來隨著社群貢獻增加，這種「技能市集」模式或許會成為 AI Agent 生態的基礎設施之一。

🔗 **專案連結**  
📂 vercel-labs/skills  
🔗 https://github.com/vercel-labs/skills  

#AI #Agent #CLI #Vercel #開發工具 #程式設計 #GitHubTrending
