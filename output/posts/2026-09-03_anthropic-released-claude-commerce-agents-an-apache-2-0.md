---
title: 'Anthropic Released Claude Commerce Agents: An Apache-2.0 Blueprint for Shopping
  and Merchant Agents Across Retail, Travel, Telecom and Entertainment'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/03/anthropic-released-claude-commerce-agents-an-apache-2-0-blueprint-for-shopping-and-merchant-agents-across-retail-travel-telecom-and-entertainment/
model: claude-code/sonnet
generated_at: '2026-09-03T20:18:25.347504'
score: 94
---

📌 【Anthropic 開源】商務代理不用重造輪子，一套藍圖橫跨零售、旅遊、電信、娛樂

TL;DR：Anthropic 開源 Apache-2.0 商務代理藍圖，含購物與商家兩種 agent，四個垂直領域可直接跑。

每個團隊想做購物助手，幾乎都要重新搭一次同樣的地基：agent loop、包住商品目錄的工具層、審核關卡、評測套件。這次 Anthropic 直接把這套地基公開成程式碼，而且不是概念驗證，是可以直接部署的版本。

🤔 **同樣的腳手架，大家都在重複蓋**

Anthropic 這週釋出 `anthropics/commerce-agents`，一個包含購物代理（shopping agent）與商家代理（merchant agent）的參考藍圖，並附上零售、旅遊、電信、娛樂四個可執行的垂直領域範例。搭配釋出的還有兩篇文件：一篇產品公告，一篇工程深度剖析《A guide to the anatomy of effective commerce agents》。

🧩 **架構主張：一個 agent 配技能，而非一堆 subagent**

這份藍圖最值得參考的地方是它的架構立場：Anthropic 反對用意圖路由（intent router），也反對「每個領域配一個 subagent」的設計。理由是一次商務對話是高度耦合的，任何一次 handoff 都會遺失狀態，因為 orchestrator 掌握著購物車、偏好與歷史紀錄，切換一次就可能多花數倍 token 並增加數秒延遲；而且領域彼此重疊，例如退貨流程同時需要訂單歷史、購物車與商品目錄。Agent skills 能提供相同的模組化效果卻沒有這個代價，因為技能指示是載入到已經掌握完整歷史的同一個 agent 裡。Anthropic 表示，在多個企業部署案例中，「單一 agent 配技能」在品質上打贏了「一大包 prompt」與「多 subagent」兩種設計，而且往往成本與延遲更低。不過 subagent 並非全無用處，對於像深度研究這種範圍狹窄、自成一體的工作，subagent 仍有其位置。

購物代理內建於商家自己的 App 中，能搜尋目錄、處理多品項需求、比較選項、組建購物車，並在同一段對話裡回答訂單與退貨問題，其五項技能為 search-discovery、purchase-research、planning-goals、customer-care、memory-personalization，部署時需要實作一個對接目錄／購物車／訂單／政策系統的 StorefrontBackend。商家代理則服務店家員工，處理銷售表現查詢、庫存警示、定價與促銷建議、行銷文案草稿，技能為 performance-insights、catalog-listings、inventory-operations、pricing-promotions、marketing-campaigns，對接 MerchantBackend。

💡 **元件當工具用，串流輸出降低感知延遲**

多數商務回應其實是元件而非純文字，藍圖的做法不是提示模型生成自訂標籤，而是把每個呈現元件都做成工具，例如 present_products、present_itinerary、present_plan_comparison，並用型別化參數讓伺服端在渲染前驗證。因為這些呼叫本來就存在於 messages 陣列裡，重新載入歷史不需要自訂解析器，agent 也能直接解析「第一間飯店」這類指代。搭配 `eager_input_streaming: true` 跳過伺服端緩衝與 schema 保證，一則約 500 到 700 output token 的回應如果不做串流，等於五秒的轉圈圈；Anthropic 把端到端延遲與「感知延遲」分開處理，一邊串流元件成形、一邊顯示白話進度提示。搭配 Agent SDK 預設的 eager tool dispatch（工具參數一串流完就立刻執行），據稱能把數秒的等待縮短到幾百毫秒。

Prompt caching 則是主要的成本槓桿，請求依照 global → session → volatile 的順序排列，因為快取是以前綴為基礎，若把時間戳記放在 system prompt 最上方，每次請求都會打破快取。快取讀取的成本只有新鮮 token 的十分之一，快取寫入則有約 1.25 倍的溢價，最佳部署案例的快取命中率可達 90% 到 99%。至於記憶抽取，藍圖選擇在獨立的非同步流程中執行，而非對話當下即時儲存，Anthropic 測得這種做法讓事實回憶率提升了 13%。

🧩 **怎麼用：三種執行方式、一個 Claude Code 外掛**

購物代理與商家代理都能以三種方式執行：Messages API、Claude Agent SDK，以及 Claude Managed Agents（beta），三者共用同一份 prompt、技能、工具合約與審核關卡的定義。repo 採 Apache 2.0 授權，可在本機以 Python 3.11+ 與 Node 22 執行，只需設定 `ANTHROPIC_API_KEY`；由於執行環境接受任何 anthropic client，同一份程式碼能部署到 Claude API、Amazon Bedrock、Microsoft Foundry 或 Google Cloud Vertex AI。另外還附上一個 Claude Code 外掛 `commerce-builder`，可用 `/scaffold-commerce-agent` 生成新的商務代理，或用 `/review-commerce-agent` 檢視既有代理的實作。

prompt 與技能之間的分工則以使用頻率決定：大致三分之一以上的流量走 system prompt，其餘放進技能；安全規則、品牌限制與關鍵使用者事實則一律固定放在 prompt 裡。

🎯 **實務啟示**

如果你正在評估「多 subagent」架構來拆分商務場景的不同領域，這份藍圖給了一個值得思考的反例：先確認你的場景是否真的需要跨領域切換上下文，如果答案是否定的，單一 agent 加技能可能是更省 token、更低延遲的選擇；而元件即工具、快取排序、非同步記憶抽取這幾個做法，即使不採用整個藍圖，也能直接搬進既有的 agent 系統裡。

🔗 **來源**
- 標題：Anthropic Released Claude Commerce Agents: An Apache-2.0 Blueprint for Shopping and Merchant Agents Across Retail, Travel, Telecom and Entertainment
- 作者／機構：Asif Razzaq（MarkTechPost）／Anthropic
- 連結：https://www.marktechpost.com/2026/09/03/anthropic-released-claude-commerce-agents-an-apache-2-0-blueprint-for-shopping-and-merchant-agents-across-retail-travel-telecom-and-entertainment/

#Anthropic #Claude #AgentSDK #CommerceAI #OpenSource #PromptCaching #AgentArchitecture #Apache2 #LLMAgents #ConversationalCommerce
