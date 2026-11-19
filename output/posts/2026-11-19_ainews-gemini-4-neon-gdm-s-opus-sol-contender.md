---
title: '[AINews] Gemini 4 Neon: GDM''s Opus/Sol Contender'
source: Latent Space
url: https://latent.space/p/ainews-gemini-4-neon-gdm-s-opus-sol-contender/
model: claude-code/sonnet
generated_at: '2026-11-19T23:59:54.294993'
score: 76
---

📌 Gemini 4 Neon 上線：Google DeepMind 七週內的第四個 Gemini 4 模型

TL;DR：Google DeepMind 推出中階新模型 Neon，定位比上一代更快更便宜，多項基準測試緊追旗艦模型 Carbon 與對手 Fable 5.2。

七週內發布四個模型，命名邏輯還跟元素週期表的原子序「反著走」——中階模型 Neon（原子序 10）速度比旗艦模型 Carbon（原子序 6）更快更便宜，連社群都搞不清楚這套命名規則。

🤔 命名混亂背後，是飛快的發布節奏

根據 Latent Space 整理的 AI News，Google DeepMind 近期上線 Gemini 4 Neon，是 Gemini 4 系列約七週內推出的第四個模型。推出僅一個半月的 Argon 已經退役，Gemini 1-3 時代的 Pro 與 Flash 也已停用。文中指出，由於 distillation、RL 與 benchmark 設計的運作方式，體型較小的 Neon 在某些指標上反而能超越體型更大的 Carbon。發布節奏也在明顯加速：Argon 到 Carbon 間隔 28 天，Carbon 到 Hydrogen 間隔 15 天，Hydrogen 到 Neon 只間隔 6 天。

🧩 定價、規格與上線管道

Neon 的定價為每百萬 token 輸入 3 美元、快取輸入 0.15 美元、輸出 15 美元，具備 1M token 的 context window 與四個 effort 等級；Vals 的報告指出其最大輸出上限為 1M token。上線管道包括 AI Studio 與 Android Studio 中的付費 Gemini API、Gemini for business，以及 Antigravity 的 Pro／Ultra 訂閱用戶；在 Gemini app 中，Pro／Ultra 用戶可將它選為「Deeper analysis」模式，Tasks 功能也支援。首日整合的工具包括 Cursor、GitHub Copilot（App、CLI、VS Code）與 LangChain Managed Deep Agents。

📊 基準測試：追著 Carbon 與 Fable 5.2 跑

| 測試 | Neon 表現 | 對照 |
|---|---|---|
| Intelligence Index（high effort） | 60 分，每題成本 $3.74 | 與 Carbon 同分 |
| GDP.pdf | high 效果 33.4%，xhigh 效果 28.0% | high 反而優於 xhigh |
| Agent Arena | 第二名，1,336 分，約 4,200 場次，median task cost $2.82，steerability 第二 | Carbon 仍領先另一項 Text Arena |
| Vals Index | 70.9%，第二名 | 落後 Fable 5.2 約 0.4 分，但成本不到對手一半 |
| Code Migration | 平均 160 輪 | 少於 Carbon 的 234 輪、Hydrogen 的 574 輪，但分數低於兩者 |
| CursorBench 4.1（預設 effort） | 63.7% | 高於 Hydrogen 的 57.3% |

💡 用量觀察：工具呼叫多，但有時不聽指揮

文中引用 Kimmonismus 在 13 個早期 Antigravity session 中的記錄：Neon 共發出 762 次工具呼叫，input cache 命中率達 93%；當被要求避免使用終端機時，這些測試中 Neon 完全沒有執行任何 shell 指令。同一批記錄也顯示 57 次容量錯誤與 4 次卡住的執行。在實際用法上，Theo 表示自己用 Neon 寫文案、用 Fable 實作變更、用 Astra 進行 playtest；Jeremy Howard 則稱讚 Neon，但同時把 Solveit 裡的 Astra 與 Sol 選項退回 6.2 版之前的設定。

同一批 Gemini 4 家族模型中，Astra 與 Sol 在 MathArena 拿下前兩名，Astra 解出 ArXivLean 53 題中的 42 題；Vals 另外指出這可能是 Smoktunowicz's Gap Theorem 在 Lean 中的首次正式化證明，並經獨立 kernel replay 驗證。Agent Arena 上 Astra 排名第六，Sol 第十一但 median task cost 僅 $0.90；在另一個 Code Arena 的 WebDev 榜單上，Astra 排名第三，median cost 比前代低 42%。

⚠️ 仍有雜訊：容量錯誤與早期評測落差

除了前述的 57 次容量錯誤與 4 次卡住執行外，OpenAI 的 Tibo Sottiaux 提到同期有評論者測試的其實是最終版定稿前幾天的 build；Artificial Analysis 的行為評測也發現，另一個家族模型 Astra 的回覆變短，且比之前更不願意承認不確定性。

🎯 實務啟示

挑選模型時，Neon 的 GDP.pdf 測試出現「high 效果優於 xhigh」的反直覺結果，提醒工程師在導入新 effort 等級前，應該針對自己的任務實測，而不是假設效果等級越高分數必然越好；同時 median task cost 與輪數（turns）這類效率指標，往往比單一準確度分數更能反映實際部署的性價比。日內的工具整合（Cursor、Copilot、LangChain）與 agent 測試中出現的容量錯誤、指令被忽略等問題,也值得在導入 agentic workflow 前先行驗證。

🔗 來源
- 標題：[AINews] Gemini 4 Neon: GDM's Opus/Sol Contender
- 作者／機構：Latent Space
- 連結：https://latent.space/p/ainews-gemini-4-neon-gdm-s-opus-sol-contender/

#GeminiAPI #GoogleDeepMind #LLM #AIBenchmark #AgentArena #CursorBench #ModelRelease #AIAgents #PromptEngineering #LLMPricing
