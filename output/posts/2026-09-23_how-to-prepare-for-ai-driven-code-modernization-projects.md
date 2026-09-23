---
title: How to prepare for AI-driven code modernization projects
source: Claude Blog
url: https://claude.com/blog/how-to-prepare-for-ai-driven-code-modernization-projects
model: claude-code/sonnet
generated_at: '2026-09-23T20:38:46.607612'
score: 87
---

📌 【Anthropic】導入 AI 程式碼現代化前，先想清楚這 6 件事

TL;DR：Anthropic 分享企業導入 AI 驅動程式碼現代化時，該如何先做好組織與流程準備。

過去動輒數年、全員投入的程式碼現代化專案，現在用 agent 可能幾個月甚至幾週就能完成。但 Anthropic 的 forward deployed engineers 在「Notes from the Field」系列中指出一個容易被忽略的事實：技術瓶頸消失了，組織瓶頸卻沒有跟著消失。銀行等關鍵系統的每一次變更，仍然要經過完整的變更管理、審查與核准流程——這套流程原本就是建立在「人寫每一個變更、人審每一個 diff」的假設上。一旦 agent 加速了變更的產出速度，瓶頸就從「怎麼寫出變更」轉移到「怎麼動員整個組織去消化變更」。

🤔 **在動手之前，組織要先做完的功課**

文章把這件事拆成六個步驟：定義目標（target）、建立驗收憑證（certificate）、設定推廣到正式環境的政策（promotion policy）、備妥前置條件（環境、CI/CD、審查量能、核准機制）、打造並優化 agentic workflow（用 Claude Code 打造能拆成多條平行 subagent 工作流的客製流程），最後才是實際執行：先在一小部分程式碼上端到端驗證，再逐步擴大規模。

🧩 **第一步：決定你要做的是哪一種現代化**

Anthropic 把現代化分成三種類型。Uplift（提升）是同技術堆疊的版本升級，例如 C++11 → C++20，適用於堆疊本身沒問題、只是版本落後（生命週期已終止的執行環境、未修補的安全漏洞、升不動的相依套件），目標就是明確的執行環境版本與套件集合。Transform（轉換）是跨堆疊但保持行為不變的重寫，例如 COBOL → Java，適用於堆疊本身才是問題、而現有行為是可信的，除了 Uplift 的所有需求外，還要定義新的語言、框架與架構慣例。Reimagine（重構想）則是在新架構上進行的全新重建，同時修改行為，適用於行為本身也需要改變的情況，除了 Transform 的需求外，還要寫出完整的新系統行為規格。

文章特別提醒，選哪一種類型在組織內部常常有爭議：越靠近正式環境的人傾向希望「只換堆疊、行為完全不變」以控制風險（也就是 Transform）；而長期背負這套舊系統的工程師和部分業務關係人，則往往希望趁機清償技術債、甚至提出新需求（也就是 Reimagine）。兩種立場都合理，但如果這個問題沒有先解決，之後每一個變更「算不算正確」都會變成爭論焦點。先花時間建立共識，看似增加前期摩擦，實際上會讓整個專案跑得更順。

💡 **先盤點現有系統，再決定要不要動它**

定義目標之前，理解現有系統往往是必要的第一步。把舊程式碼實際在做的事情整理成行為清單，才能判斷哪些部分該改、哪些該留，也才能真正決定這是 Transform 還是 Reimagine——這個過程也經常會挖出沒人記得存在的業務邏輯與邊界案例。Claude 可以承擔大部分的探索工作，例如程式碼現代化外掛（code modernization plugin）裡的 assess、map、extract-rules 指令，能挖出附帶原始碼引用的業務規則，供工程師審閱。不過文章也坦言，光靠 Claude 的探索未必能完整捕捉一套舊系統的實際行為，還是需要搭配對商業使用者與開發者的訪談，以及內部文件補齊缺口。這段前期的脈絡收集可能要花不少時間，但它的品質會決定後續整個 workflow 每一個決策的品質。如果是做 Reimagine，還需要額外把行為規格寫下來並與使用者群體取得共識。

⚠️ **為什麼要做這件事，往往比怎麼做更難達成共識**

文章指出，現代化能降低維運與營運成本，但在他們的經驗裡，成本削減其實很少是這類專案真正的驅動力，風險降低才是。帶著未修補漏洞的系統，可能意味著資安入侵或足以危及整個事業的嚴重停機；不再受支援的執行環境、加上懂這套系統的工程師越來越少，只會讓風險持續放大。像 Claude Code 這樣的 agentic coding 工具雖然縮短了現代化的時程，但預算依然難以精準估算，這也是專案容易陷入慣性、遲遲不啟動的原因之一。啟動這類專案最大的挑戰，通常不是技術，而是在擁有系統的團隊與依賴系統的團隊之間建立內部共識與承諾——在領導層把商業論證與專案目標訂清楚，會讓後面的過程順利很多。

🎯 **給準備導入的團隊**

如果你的組織正在評估類似專案，這篇文章給出的順序值得參考：先在領導層釐清「為什麼要做」與「做到什麼程度」，把 Uplift／Transform／Reimagine 的選擇攤開來討論，再用 Claude 的探索能力搭配人工訪談把現有行為盤點清楚。當利害關係人對「一個變更能承受多少風險」意見分歧時，把「不做現代化的風險」拿出來當作對照的砝碼，往往比單純談成本更容易凝聚共識。

🔗 **來源**
- 標題：How to prepare for AI-driven code modernization projects
- 作者／機構：Jonah Ezekiel、Lexie Tonelli／Anthropic（Claude Blog）
- 連結：https://claude.com/blog/how-to-prepare-for-ai-driven-code-modernization-projects

#Anthropic #ClaudeCode #CodeModernization #EnterpriseAI #LegacySystems #AgenticWorkflow #ChangeManagement #SoftwareEngineering #DigitalTransformation #AICoding
