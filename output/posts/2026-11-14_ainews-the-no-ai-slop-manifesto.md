---
title: '[AINews] The No AI Slop Manifesto'
source: Latent Space
url: https://latent.space/p/ainews-the-no-ai-slop-manifesto/
model: claude-code/sonnet
generated_at: '2026-11-14T21:38:29.540431'
score: 70
---

📌 拒絕AI Slop：llama.cpp喊出1.0，SGLang也跟進

TL;DR：開發者社群發起「No AI Slop」宣言，同週llama.cpp與SGLang雙雙邁入1.0。

同一週，開源推理引擎llama.cpp宣布1.0、SGLang在自己的summit上跟進宣布1.0，但真正衝上Hacker News首頁的，卻是一份呼籲大家別再產出「AI垃圾內容」的宣言。

🤔 AI Slop manifesto從哪裡來

根據Latent Space的AINews彙整，「No AI Slop」宣言源自AIE CODE大會上的討論，由Dex在閉幕主題演講中正式提出，並獲得多位與會講者連署。這份宣言的全文、連署名單與編輯討論都公開在slopmanifesto.com，Latent Space提到Hacker News社群也把它投票推上了首頁。

🧩 同一週的基礎設施新聞：llama.cpp邁入1.0，SGLang緊接宣布1.0

llama.cpp與ggml同時宣布達到1.0，代表的是「宣告穩定」，具體做法是把llama.cpp公開標頭檔裡35個已棄用（deprecated）的函式移除。報導中也提到，現在使用超過GPU記憶體容量的Mixture-of-Experts模型的使用者，可以設定一塊快取空間留給常用的experts，這項1.0里程碑由Georgi Gerganov主責，Daniel Han Chen則提供了範例。同一篇彙整也提到，SGLang在近期的SGLang Summit上同樣宣布了自己的1.0版本，與llama.cpp的穩定化動作前後呼應。

💡 穩定版號與拒絕Slop，其實是同一種對品質的承諾

把這幾件事放在一起看，其實有共同的脈絡：llama.cpp移除35個已棄用函式、SGLang宣告自己的1.0，都是在對外承諾「介面不會再隨意變動」；而No AI Slop manifesto則是另一種形式的品質承諾，希望團隊內部能有一份共同語言，討論怎麼避免讓AI產出未經把關、品質堪憂的內容或程式碼進入正式產出。兩者的共同精神，都是在AI工具與開源基礎設施快速演進的當下，為「穩定」與「品質」畫一條線。

🎯 實務啟示

Latent Space提到，發起這份manifesto的初衷是「提供一個在工作場合討論AI Slop問題時好用的工具」，而不是要變成強制規範。對工程團隊來說，與其等AI生成的低品質程式碼或文件堆積成技術債，不如趁現在把這份宣言或類似的原則，拿來當作團隊review流程的討論起點；同時，像llama.cpp、SGLang這類基礎設施邁入1.0，也代表依賴它們的下游專案現在可以更放心地對齊穩定API，減少跟著上游deprecated函式變動而反覆修改的成本。

🔗 來源
- 標題：[AINews] The No AI Slop Manifesto
- 作者／機構：Latent Space
- 連結：https://latent.space/p/ainews-the-no-ai-slop-manifesto/

#AISlop #OpenSource #llamacpp #SGLang #LLM #DeveloperTools #MachineLearning #Inference #SoftwareQuality #AIAgents
