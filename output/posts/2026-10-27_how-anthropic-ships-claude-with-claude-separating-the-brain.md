---
title: 'How Anthropic ships Claude with Claude: Separating the Brain from the Hands'
source: Latent Space
url: https://latent.space/p/opus55/
model: claude-code/sonnet
generated_at: '2026-10-27T21:34:15.808281'
score: 93
---

📌 Anthropic工程內幕:用Claude打造Claude的大腦與雙手

TL;DR:Anthropic揭露Opus 5.5背後的沙盒隔離、憑證保護與Rust重寫,安全考量正逐漸凌駕於功能堆疊之上。

當一家公司的模型本身就是公司最重要的工程工具時,「怎麼部署」會和「怎麼訓練」一樣複雜。Latent Space訪問了Anthropic工程與產品負責人Katelyn Lesse與Angela Jiang,談Opus 5.5的發布過程,也談到一個更底層的問題:Anthropic是如何用Claude來打造並保護Claude的。

🤔 **兩種壓力同時夾擊**

訪談指出,Anthropic團隊同時承受兩種壓力:模型能力愈強,安全部署與存取權限的判斷就愈困難;同時用量成長快到讓CPU消耗這類原本屬於基礎設施的選擇,變成了策略層級的決策。這兩股壓力最終都匯聚到了面向開發者的產品設計上。

🧩 **把「大腦」和「雙手」拆開**

訪談中最值得記下的心智模型,是把一個agent拆成「大腦」(session log與harness)和「雙手」(實際執行程式碼的sandbox)。Anthropic的Managed Agents架構讓harness可以持續存在,而執行環境則是按需建立;即使sandbox執行失敗,也不會連帶把整個agent session一起搞垮。

這個拆分同時帶來一個安全上的好處:如果生成的程式碼是在一個從未拿到服務憑證的sandbox裡執行,那麼這段程式碼就沒有憑證可以讀取。訪談描述Anthropic把憑證另外保管,透過proxy附加使用,並對sandbox的對外流量加上管控。

這個設計也解決了效能問題。團隊提到早期做法是把整個coding agent都放進一個包在API後面的sandbox裡,啟動環境與agent本身都要花時間,一旦sandbox消失,連帶執行中的agent也會跟著消失。拆開大腦與雙手之後,才有辦法同時追求更低延遲與更高可靠性,又保持執行環境的隔離。

💡 **保護模型思考,也可能弄壞客戶的程式**

另一個細節是關於防止模型推理過程被蒸餾(distillation)。保留跨輪對話的thinking blocks有助於防止這點,但訪談也坦承,這類新規定有可能弄壞客戶既有的harness整合。早期存取計畫的實際運作,是讓客戶在自己的harness裡跑評測、回報意外行為,有時候只是傳來不太正式的觀察心得——真正有價值的部分,不只是一個benchmark分數,而是看到模型在Anthropic自家產品沒有涵蓋到的環境與任務裡的表現。

訪談也提到團隊用Rust重寫了Messages API,以及記憶功能中所謂的「dreaming」——其實就是讓一個agent去檢視另一個agent先前的工作紀錄,再把結果寫回記憶裡,是在同一套Managed Agents原語之上組合出的更高層行為。

⚠️ **路線圖不是承諾**

團隊坦言,隨著模型發布愈來愈難,記憶與學習功能雖然重要,但目前更多注意力已轉移到安全上。他們也傾向讓底層harness保持精簡,把verifiers、平行agent等策略交給開發者自行在上層實驗。訪談中提到的平臺未來功能,應視為規劃方向而非已出貨的承諾。

🎯 **給agent runtime設計者的提問清單**

這套大腦與雙手的分離思維,值得任何設計agent runtime的工程師借鏡:哪些部分需要在失敗後存活下來?哪些部分在執行不受信任的程式碼?真正需要出現在程式碼執行現場的機密,到底有哪些?具體實作會因產品而異,但這些問題本身是通用的。

🔗 **來源**
- 標題:How Anthropic ships Claude with Claude: Separating the Brain from the Hands
- 作者/機構:Latent Space
- 連結:https://latent.space/p/opus55/

#Anthropic #ClaudeAI #AgentArchitecture #AIInfrastructure #ModelSecurity #Sandboxing #LLMOps #Distillation #RustLang #AISafety
