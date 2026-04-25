---
title: "alvinunreal/oh-my-opencode-slim"
source: GitHub Trending
url: https://github.com/alvinunreal/oh-my-opencode-slim
score: 86
model: tencent/hy3-preview:free
generated_at: 2026-04-25T19:18:47.809707
---

📌 【GitHub Trending】OpenCode 多智能體調度插件

還在讓單一 AI 模型包辦所有開發任務？
你可能正在浪費預算、拖慢效率，還犧牲程式碼品質。
這款開源插件給出了務實的解法。

🤔 **單一模型包辦開發任務，質效成本難兼顧**
當前 Cursor、Claude Code 等 GenAI 輔助開發工具普及，多數團隊直接使用單一大模型處理從架構設計、文件查詢到 UI 實作的全流程任務。但實際落地常面臨兩難：採用高能力模型成本高、回應速度慢，採用小模型則難以保障架構合理性與程式碼品質，三者很難同時兼顧。oh-my-opencode-slim 正是針對此痛點設計的 OpenCode 生態插件。

🧪 **內建 7 位專職 Agent，按任務類型自動路由**
這款插件由 Boring Dystopia Development 維護，屬於 Open Multi Agent Suite 的一員，核心設計邏輯是避免用單一模型處理所有工作，而是將任務路由給最適配的專職 Agent，同時支援混合任意模型、自動委托任務，平衡產出質量、執行速度與使用成本。
內建 7 位專職 Agent（團隊名為 Pantheon），分別負責：
- 偵查程式碼庫
- 查詢最新技術文件
- 審查系統架構
- 處理 UI 相關工作
- 執行小範圍實作任務
所有任務由統一編排器統籌調度。

安裝門檻極低，可選兩種方式：
1. 直接將指定提示貼到 Claude Code、AmpCode、Cursor 等 LLM Agent 中自動完成配置
2. 手動執行指令：`bunx oh-my-opencode-slim@latest install`

預設安裝會生成 OpenAI 預設配置：
- 高判斷型 Agent 使用 `openai/gpt-5.5`
- 快速執行型 Agent 使用 `openai/gpt-5.4-mini`
使用者也可自行登入其他模型供應商，透過以下指令管理可用模型：
- 登入供應商：`opencode auth login`
- 刷新模型列表：`opencode models --refresh`

💡 **分工路由可同時優化質量、速度、成本**
這款插件的核心價值在於將「多智能體分工」與「成本控制」兩個 GenAI 工程化熱門議題落地為開箱即用的工具。透過明確的角色分工設計，工程團隊無需從零搭建 Agent 編排架構，可直接基於 OpenCode 生態快速驗證多智能體開發流程的實際效果，思路清晰且實用性強。

💡 **多智能體分工是落地 GenAI 開發的務實路徑**
需要明確的是，這款插件並非基礎模型或全新架構的技術突破，而是工程側的務實工具創新。它沒有嘗試解決底層模型的技術問題，而是聚焦於現有模型能力的調度優化，大幅降低了多智能體協作開發的門檻，這也是它能快速登上 GitHub Trending、引發 GenAI 工程師與技術管理者關注的核心原因。

⚠️ **公開資訊未明確標註專案限制**
目前基於可取得的專案公開說明內容，未提及明確的功能邊界、適用場景限制或已知問題。建議有進階使用需求的團隊，可參考 GitHub 倉庫內的「Meet the Pantheon」Agent 說明與「Features & Workflows」章節，確認是否符合自身需求。

🎯 **工程團隊可快速試用驗證多智能體流程**
對於正在導入 GenAI 輔助開發的團隊，這款開源
