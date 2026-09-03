---
title: A guide to the anatomy of effective commerce agents
source: Claude Blog
url: https://claude.com/blog/the-anatomy-of-effective-commerce-agents
model: claude-code/sonnet
generated_at: '2026-09-03T20:05:08.984585'
pinned: true
---

📌 商務 Agent 該用 Subagent 拆分域，還是一個 Agent 扛全部？

TL;DR：Anthropic 工程團隊實測發現，用 skills 取代 subagent 架構，商務 Agent 的品質、成本、延遲全面勝出。

多數團隊設計複雜 Agent 時，直覺會想「每個領域配一個 subagent」，看似乾淨俐落。但 Anthropic 在替零售、市集、旅遊、娛樂、電信客戶打造商務 Agent 的過程中，得到的結論恰恰相反。

🤔 **什麼是商務 Agent？**

Anthropic 把商務 Agent 定義為「讓線上目錄的買賣變簡單」的 Agent。面向消費者的一類負責搜尋、比較、替代方案與組單，可能是零售購物車、旅遊行程、行動門號方案變更，或是演唱會的留位；面向商家的一類則回答銷售相關問題、執行促銷與行銷活動、管理庫存與定價。這篇指南分三部分：架構怎麼決定（一次性決策）、如何兼顧延遲與成本，以及如何在正式環境中運作（記憶、安全、評估、跨組織擴展）。Anthropic 也一併公開了對應的參考實作 repository：anthropics/commerce-agents。

🧩 **核心架構：一個模型、標準 Agent 迴圈、外掛 skills**

Anthropic 觀察到，這些正式上線的商務 Agent 共用同一種簡單架構：Claude 跑在一個標準的 Agent 迴圈裡，搭配一組 skills 與工具，外加一套完整的 eval 體系。這個迴圈的運作方式是：針對目標進行推理、探索上下文、透過工具採取行動、透過 skills 學習流程、視需要提出釐清問題，並持續觀察結果直到目標達成。架構中沒有前置的 intent router 把對話切段，後面也沒有一群按領域劃分的專用 subagent。

💡 **為什麼不用「一個領域配一個 Subagent」？**

Anthropic 指出，商務對話往往是一個緊密耦合的 session，橫跨多個意圖與多輪對話，需要大量共享上下文。在 subagent 架構下，orchestrator（主控 Agent）持有購物車、暫存變更、使用者偏好與對話歷史，而每一次交給 subagent 的 handoff 都是「有損狀態」的操作，往往拖累 subagent 回應的品質，進而影響整體回應。更現實的問題是，每次 handoff 可能消耗多倍的 token，並額外增加數秒延遲。再加上商務領域彼此很難乾淨切分：一個退貨流程可能同時需要訂單歷史、目前購物車與商品目錄，這讓「每領域一個 subagent」的做法，要嘛在各處重複存取邏輯，要嘛得在任務執行到一半時中途 handoff。

Anthropic 也提到，隨著模型能力提升，能處理更長的上下文、更多 skills 與工具，過去限制架構選擇的種種限制正逐代放寬。相對地，agent skills 能提供類似 subagent 的「按領域模組化」與上下文控制，卻不必付出 handoff 的代價，因為 skill 指令是直接載入已經持有完整歷史的主 Agent 裡。在多個企業部署的比較中，「單一 Agent ＋ skills」的設計，在品質上持續勝過「單一大 prompt 打天下」與「subagent 分工」兩種設計，而且成本與延遲往往更低。

🧩 **Subagent 什麼時候才值得用？**

文中指出兩種例外情況。第一種是 orchestrator 把 subagent 當成工具呼叫，處理一個範圍狹窄、自成一體、適合擁有獨立上下文視窗的任務，常見案例是 deep-research 型 subagent：它自己搜尋、閱讀文件、寫並執行程式碼、走訪資料模型、碰壁再重來，所有過程都發生在一個或多個 subagent 內部，回傳給 orchestrator 的只有一份精簡答案。第二種例外，是該領域本身已經有一套專用的 Agent，例如藥局或金融服務體驗本來就跑著具備自己合規邏輯的專屬 Agent，這時正確做法是「hand-off」，讓該 Agent 直接接手，透過自己的迴圈與使用者互動到任務完成。文中強調兩者的關鍵差異在於「誰擁有這段對話」：hand-off 讓領域 Agent 成為使用者真正的對話對象；delegation 則讓 orchestrator 保有主導權，只是把領域 Agent 在單一回合內叫進叫出，而每次交手都會讓品質打折扣。

🧩 **系統提示詞還是 Skill？用「出現頻率」決定**

決定一組指令該放進系統提示詞（system prompt）還是 skill，主要看 Agent 多常需要用到它。載入一個 skill 要多花一個模型回合（model turn），所以 Agent 在大多數回合都會用到的東西，通常直接放進系統提示詞。這也取決於實際流量分布與 eval 觀察到的 Agent 行為，一個可用的起始經驗法則是：不論是上線前預期、還是上線後在正式流量中觀察到，只要相關性涵蓋三分之一以上的流量，就放進系統提示詞，其餘放進 skills。如果某個 skill 可以從已知的訊號預先判斷（例如使用者是從哪個頁面進來的），建議在第一次呼叫模型之前就由 harness 直接注入，省下額外載入 skill 的那一個回合。至於安全與法規規則、品牌限制、以及像過敏這類關鍵使用者資訊，則永遠放進系統提示詞。

在 Anthropic 的參考實作中，購物 Agent 的系統提示詞裡放的是 grounding、購物車與結帳語意、呈現規則，以及商品搜尋（因為幾乎每個 session 都會用到），其餘則拆成 search-discovery、purchase-research、planning-goals、customer-care、memory-personalization 等 skills。商家 Agent 則依 performance-insights、catalog-listings、inventory-operations、pricing-promotions、marketing-campaigns 等營運領域各自拆成一個 skill。

⚠️ **本篇涵蓋的只是架構這一層**

素材明確表示這是一份分三部分的完整指南，本文取材的部分主要對應「架構」這一部分，關於延遲最佳化、prompt caching、模型選型、正式環境中的記憶機制、安全設計與 eval 實務等後續內容，素材中僅列出章節名稱、未展開細節，因此本文不予展開，避免臆測。

🎯 **實務啟示**

如果你正在評估要不要幫 Agent 拆 subagent，先問自己一個問題：這個任務是不是真的需要獨立的上下文視窗，且不太需要跟主對話共享狀態？如果答案是否定的，Anthropic 的實務經驗建議先試著用 skill 取代 subagent，尤其是在使用者體驗高度依賴「同一段對話記得住購物車、偏好與歷史」的商務場景中。

🔗 **來源**
- 標題：A guide to the anatomy of effective commerce agents
- 作者／機構：Ali Shazal, Matthew Koen（Anthropic）
- 連結：https://claude.com/blog/the-anatomy-of-effective-commerce-agents

#Anthropic #Claude #AIAgent #AgentArchitecture #CommerceAgent #LLMEngineering #AgenticAI #SoftwareArchitecture #PromptEngineering #AIagentdesign
