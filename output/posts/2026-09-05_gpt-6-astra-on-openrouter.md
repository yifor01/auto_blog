---
title: GPT-6 Astra on OpenRouter
source: Hacker News
url: https://openrouter.ai/openai/gpt-6-astra
model: claude-code/sonnet
generated_at: '2026-09-05T19:21:39.118474'
score: 58
---

📌 GPT-6 Astra 規格出爐：105 萬 token context，output 單價衝上 $50/M

TL;DR：OpenAI 旗艦模型 GPT-6 Astra 登上 OpenRouter，主打長程 agentic 任務，但定價結構明顯瞄準高價值工作場景。

當一個模型的 context window 衝到 105 萬 token，output 定價來到每百萬 token 50 美元，這代表 OpenAI 對它的定位是什麼？

🤔 **主打長程 agentic 任務的旗艦模型**

根據 OpenRouter 的模型頁面，GPT-6 Astra 是 OpenAI 針對「demanding end-to-end work」設計的旗艦模型，適合進階分析、軟體工程、深度研究、科學工作與文件產生，特別強調在長程 agentic 任務中涉及電腦與瀏覽器操作的能力。該模型於 2026 年 9 月 4 日發布。

🧩 **規格與定價一次看**

- Context window：1,050,000 tokens；最多支援 128,000 completion tokens
- 定價：input $10.00/M tokens、output $50.00/M tokens；cache read $1.00/M tokens、cache write $12.50/M tokens、web search $10.00/1K calls
- 支援 tools 與 tool_choice 的 function calling，也支援透過 response_format 以 JSON schema 產生 structured output
- 可接受 PDF、圖片、文字作為輸入，輸出為文字
- 由 OpenAI 與 Azure（US）兩家 provider 在 OpenRouter 上提供服務，支援自動 failover

📊 **OpenRouter 的路由機制**

OpenRouter 提供 Balanced（價格與速度平衡）、Nitro（最快）、Exacto（最高 tool-calling 準確度）三種路由模式，讓同一個模型的請求依照不同優先順序被導向不同的 host provider，並透過 Endpoints API 提供各 provider 的即時可用性資料。

💡 **定價結構透露的產品定位**

Output token 價格是 input token 的五倍，加上單次 $10/1K calls 的高額 web search 費用，這樣的成本結構清楚指向「長任務、高價值 agentic 工作」，而非一般聊天場景，這與素材中反覆強調的 long-horizon agentic tasks 定位相互呼應。這篇上架資訊也在 Hacker News 上引發 283 點讚、209 則討論，顯示社群對這次發布高度關注。

⚠️ 這份素材本質上是 OpenRouter 的模型規格與定價頁面，並未包含實際 benchmark 成績、真實使用案例或與其他模型的效能比較，僅呈現規格與計費資訊。

🎯 **實務啟示**

評估是否導入 GPT-6 Astra 時，除了關注百萬級 context window 帶來的新可能性，也務必把 output token 與 web search 的高單價算進整體 TCO，尤其是在會頻繁呼叫工具與網頁搜尋的 agentic pipeline 中，成本可能遠高於單看 input 定價的直覺印象。

🔗 **來源**
- 標題：GPT-6 Astra on OpenRouter
- 作者／機構：Topfi（Hacker News）
- 連結：https://openrouter.ai/openai/gpt-6-astra

#GPT6Astra #OpenAI #OpenRouter #LLMPricing #AgenticAI #LongContext #FunctionCalling #AIInfrastructure #ModelRouting #FrontierModel
