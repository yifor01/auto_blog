---
title: 'MiniMax Just Launched M3.1 Flash: 428B MoE Agentic Model at $0.15/M Input'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/19/minimax-m3-1-flash-release/
model: claude-code/sonnet
generated_at: '2026-10-19T21:38:29.312969'
score: 106
---

📌 MiniMax M3.1 Flash：428B MoE 模型，輸入只要 $0.15/M

TL;DR：MiniMax 用 Flash 等級價格打出接近頂尖 Agent 的分數，附完整 benchmark 對照表。

一個停工模型悄悄跑了超過 200T tokens，結果揭露後發現它根本就是正式版的前身——這就是 MiniMax M3.1 Flash 上線前的「Space Bunny」。

🤔 **從神秘模型到正式發布**

MiniMax 已在自家 API 上線 MiniMax M3.1 Flash,輸入定價每 100 萬 tokens 只要 $0.15。官方同時證實,先前流傳的神秘模型 Space Bunny,其實就是 M3.1 Flash 的早期版本,累計處理超過 200T tokens。模型權重預計 2026 年 10 月下旬公開,目前尚未公布授權條款。

🧩 **428B 總參數、23B 啟用的多模態 MoE**

M3.1 Flash 是一個多模態 mixture-of-experts 模型,主打程式設計、辦公室 Agent 任務與視覺推理。官方產品頁列出 428B 總參數、約 23B 啟用參數,搭配 sparse attention 與原生視覺編碼器,可接受文字、圖片、影片輸入,輸出文字,context window 達 100 萬 tokens。這組參數與 MiniMax M3（約 428B 總參數、23B 啟用）相符,但官方並未發布技術報告說明 Flash 版本具體改動了什麼。

值得留意的是推理模式永遠開啟、無法關閉,開發者可從 Low、Medium、High、Xhigh、Max 五個 effort 等級中選擇,官方建議預設用 Max。若請求中傳入 thinking.type=disabled 或 effort=none 會直接回傳錯誤;推理內容會放在獨立的 reasoning_content 欄位中（可能為空),過去會解析 M3 內嵌 <think> 標籤的整合方案需要相應更新。

📊 **Benchmark 一覽（以下皆為 MiniMax 自行公布數據,尚無第三方複現）**

| 測試項目 | M3.1 Flash | 對照模型 |
|---|---|---|
| Automation-Bench v1.0.6（CoWork） | 62.2 | Opus 5：50.3；GPT-5.6 Sol：45.8 |
| BankerToolBench | 76.2 | 與 Opus 5 同分 |
| LOCA-Bench 256K | 60.3 | 居冠 |
| Agents' Last Exam | 29.6 | — |
| DeepSWE v1.1 | 73.7 | GPT-5.6 Sol：73.0；DeepSeek-V4.1-Flash-1017：77.0（更高) |
| Terminal Bench 4.0 | 38.1（最弱項) | Opus 5 領先 13.7 分 |
| SWE Refactor Bench | 23.0 | Opus 5：31.0 |
| BabyVision（with tools） | 91.0 | — |
| CharXiv RQ | 82.5 | — |
| HLE（without tools） | 43.4 | — |

交叉比對方面,Kimi K3 的 model card 報告 DeepSWE 67.5、BabyVision 85.7,與 MiniMax 表格中列出的對照數字一致;但也出現一處內部矛盾——MiniMax 成本圖上 Automation-Bench max effort 標示 62.8,表格卻寫 62.2。另外 Kimi K3 自家 card 在 600-task 公開子集上報告 Automation-Bench 為 30.8,而 MiniMax 列出的卻是 46.7,說明不同 harness 選擇會讓同名 benchmark 數字無法直接比較。

💡 **用「每任務成本」取代「每 token 成本」**

MiniMax 強調的是每個任務的成本,而非單純每 token 價格。在 Automation-Bench 的成本圖上,五個 effort 等級全部落在每任務 $0.05 以下,分數從低 effort 的 52.8 一路到 max effort 的 62.8。一次完整 152 題的 Agents' Last Exam 跑完約花費 $111,對應分數 29.6。不過在 DeepSWE 上,DeepSeek V4.1 Flash-1017 在 max effort 時同時比 M3.1 Flash 分數更高、成本更低。

定價方面,M3.1 Flash 為 $0.15 輸入 / $0.60 輸出（每 100 萬 tokens),快取讀取 $0.015/M,無長 context 加價。相較之下,MiniMax M3 在 512K 以下輸入收費 $0.30/$1.20,超過後價格加倍——換算下來 Flash 每 token 價格是 M3 標準費率的一半,官方宣稱整體成本是 M3 的三分之一,但未說明具體計算方式。速度上官方列出約每秒 150 tokens,宣稱是 M3 的三倍速。M3 的 MXFP8 版本模型大小約 440 GB,可作為權重規模的參考。

⚠️ **常駐推理與未知的自架細節**

永遠開啟的推理模式意味著即使是簡單呼叫,也會有固定的 token 與延遲下限。模型目前可透過 platform.minimax.io、M Plan 及 MiniMax Code 桌面應用使用,支援 Anthropic 相容與 OpenAI 相容介面（Chat Completions 與 Responses）,但自架（self-hosting）所需的細節要等 10 月 23 日權重公開後才會明朗。

🎯 **給工程師的參考點**

如果你的場景是高頻 Agent 任務、重視每任務成本而非單純 token 單價,M3.1 Flash 的定價結構值得放進評估清單;但由於所有分數均為廠商自報、且 Automation-Bench 等指標在不同報告間數字不一致,導入前建議自行用目標任務跑一輪實測,而非直接採信官方對照表。

🔗 **來源**
- 標題：MiniMax Just Launched M3.1 Flash: 428B MoE Agentic Model at $0.15/M Input
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/19/minimax-m3-1-flash-release/

#MiniMax #MoE #LLM #AIAgents #OpenWeights #Benchmark #AgenticAI #LLMPricing #AICoding #MultimodalAI
