---
title: 'Supabase Releases Evals: an Open Source Benchmark That Scores Claude Code,
  Codex and OpenCode on Real Supabase Tasks'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/01/supabase-releases-evals-an-open-source-benchmark-that-scores-claude-code-codex-and-opencode-on-real-supabase-tasks/
model: tencent/hy3:free
generated_at: '2026-08-02T07:59:00.023609'
score: 107
---

📌 【Supabase 開源新進展】Supabase Evals 登場：針對 AI Agent 在真實開發任務中的表現進行評測

TL;DR：Supabase 開源了 Evals 框架，透過真實開發情境評估 Claude Code 等 AI Agent 的開發能力。

隨著 AI Agent 逐漸介入軟體開發流程，如何量化這些 Agent 在處理複雜、真實開發任務時的效能，成為了工程師關注的核心議題。Supabase 正式推出了 Supabase Evals，這是一個開源的基準測試（benchmark）與框架，專門用於測試 AI Agent 使用 Supabase 進行開發的表現。

🧩 **模擬真實開發流程的評測框架**

Supabase Evals 並非僅僅測試簡單的程式碼生成，而是將測試情境建立在真實的開發維度上：

- **產品維度**：涵蓋 Database、Auth、Storage、Edge Functions、Realtime、Cron、Queues、Vectors 以及 Data-API。
- **主題維度**：包含 RLS（Row Level Security）、安全性、Migrations、SQL、SDK、可觀測性（Observability）、自我託管（Self-hosting）、測試以及宣告式 Schema（Declarative Schema）。
- **階段維度**：分為 Build（建置）、Deploy（部署）、Investigate（調查）與 Resolve（解決）。

為了確保測試的真實性，測試場景是根據實際的支援票證（Support tickets）、錯誤報告（Bug reports）與 GitHub Issues 所選定，並在容器化的真實環境中執行，讓 Agent 能直接呼叫實際的 MCP Server 與 CLI。

📊 **評估結果：部分模型在建置階段表現完美**

該框架將測試分為「基準測試（Benchmark）」與「回歸測試（Regression）」兩大套件。在基準測試中，研究人員觀察到以下數據：

- **建置階段（Build Stage）**：Opus 5 與 Kimi K3 在無額外技能輔助下，皆取得了 100% 的高分。
- **技能輔助（Skills）的影響**：
  - Sonnet 5：從 78% 提升至 100%。
  - GPT-5.6 Sol：從 89% 提升至 100%。
  - GPT-5.4 mini：從 78% 提升至 89%。

⚠️ **三大技術弱點：AI Agent 的開發習慣仍有進步空間**

儘管部分模型表現優異，但研究也發現了目前 AI Agent 在處理 Supabase 任務時的常見問題：

1. **Schema 管理方式**：Agent 傾向於手寫 Migrations，而非使用更具效率的宣告式 Schema（Declarative schemas）。
2. **驗證方式**：Agent 傾向於手動驗證 Auth，而不是直接呼叫 `@supabase/server` 套件。
3. **文件閱讀習慣**：不同 Agent 對文件的使用率差異極大。例如 Codex 與 GPT-5.6 在每個場景中會閱讀約 8 頁文件，而 Claude Code 僅在不到 40% 的場景中會主動檢查文件。

🎯 **實務啟示**

對於開發者而言，Supabase Evals 提供了一個標準化的工具，可以用於評估與優化專屬的 AI Agent。透過觀察 Agent 在 RLS 或 Edge Functions 等真實任務中的錯誤模式，開發者可以更精準地進行 Prompt Engineering 或提供更完善的開發技能（Skills）包。

🔗 **來源**
- 標題：Supabase Releases Evals: an Open Source Benchmark That Scores Claude Code, Codex and OpenCode on Real Supabase Tasks
- 作者／機構：Michal Sutter @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/01/supabase-releases-evals-an-open-source-benchmark-that-scores-claude-code-codex-and-opencode-on-real-supabase-tasks/

#Supabase #AIAgents #OpenSource #Benchmark #SoftwareEngineering #ClaudeCode #LLM #DeveloperTools #MachineLearning #CodingAssistant
