---
title: 'Claude Fable 5.1 and Mythos 5.1: The System Card'
source: Don't Worry About the Vase
url: https://thezvi.wordpress.com/2026/09/04/claude-fable-5-1-and-mythos-5-1-the-system-card/
model: claude-code/sonnet
generated_at: '2026-09-04T19:56:00.186292'
score: 83
---

📌 Claude Fable 5.1 系統卡解讀：連 Anthropic 都不敢肯定資安門檻沒被跨過

TL;DR：Anthropic 系統卡顯示能力小幅提升，但作者質疑資安評級被低估。

一份 200 多頁的系統卡，理論上該讓人放心地知道「這個模型有多危險、危險到哪裡」。但部落格作者 TheZvi 逐項拆解 Anthropic 最新公布的 Claude Fable 5.1 與 Mythos 5.1 系統卡後，得出一個微妙的結論：連 Anthropic 自己在資安（cyber）能力評估上，可能都低估了模型的真實水準。

🤔 一個模型，兩個名字

Mythos 5.1 與 Fable 5.1 其實是同一個底層模型，差別只在於 Fable 疊加了額外的分類器（classifiers）做安全防護。文章指出，發布當下 Fable 5.1 明顯是全球最強的公開可用 AI 模型，多數使用者也認為它比 Fable 5 更好互動，同時 Anthropic 調降了快取讀取（cache read）的價格，讓它變得更便宜。不過隨著 GPT-6-Astra 稍後登場，作者表示目前尚無足夠資料比較兩者高下，暫不下結論。

🧩 生醫能力：卡在「還不算專家」這條線上

依 Anthropic 的責任擴展政策（Responsible Scaling Policy），只要新模型不遜於前代，就要視同具備 CB-1（可協助已具備基礎知識者取得化學或生物武器）能力，因此 Mythos 5.1 自動被歸類為 CB-1。真正的爭議在 CB-2：模型是否已能取代頂尖人類專家、協助製造新型生化武器。Anthropic 的結論是「還沒有」，理由是模型仍會犯下一些難以察覺的錯誤，但信心並不算高，因此仍部署了高規格的生醫安全防護。多數審查者認為 Mythos 5.1 的生醫程度落在「能完成大部分步驟，但仍有明顯缺口」，少數人認為已達「有素養的專家」，但沒有人認為它已是「世界頂尖專家」。系統卡第 8 節列出的相關基準測試也顯示有進步，但幅度不足以觸發 CB-2 門檻。

至於自主性（Autonomy），Mythos 5.1 同樣毫無懸念達到 Autonomy-1，但 Autonomy-2（自動化 AI 研發）Anthropic 認為還早，作者也認同這個判斷。值得注意的是，CB-2 與 Autonomy-2 的評估方式已逐漸從正式測試轉向「氛圍判斷」（vibe checks），原因是模型在正式測試上不斷刷滿分，測試本身的鑑別度反而不夠了。

📊 METR 的初步評估：加速，但還沒到質變

METR 針對 Mythos 5.1 做了幾項初步能力測試（Sunlight、Budget NanoGPT Speedrun、Language Model Conceptual Argumentation），結論是它在有明確、連續指標與客觀回饋的任務上表現優於公開模型，尤其在 Budget NanoGPT 上表現亮眼。整體而言確實有加速研發的跡象，但還沒有到專家等級全面覆蓋，也可能未達 Anthropic 定義的「2 倍生產力乘數」門檻。

⚠️ 資安：作者不相信 Anthropic 的自我評估

文章特別點出一個長期存在的怪異之處：資安能力至今仍未被納入 RSP 的正式評估項目。Anthropic 表示 Mythos 5.1「正在接近」Tier 2 資安門檻（能完全自主執行網路攻擊行動、開發新型攻擊能力並具備適應性持續存在能力），但「尚未看到」真正的新型能力出現。TheZvi 明確表示不採信這個判斷，認為 Mythos 5.1 很可能已經是 Tier 2，與 GPT-6-Astra 相近。所幸 Anthropic 無論如何都已按 Tier 2 標準部署防護措施，因此這個爭論在實務上影響有限。作者也觀察到一個一貫模式：頂尖實驗室在說法上傾向低估風險，但實際部署時往往還是採取了對應的安全措施。

🎯 對工程師而言的實務意義

如果你透過 API 使用 Fable 5.1 或 Mythos 5.1，代表你正在使用一個已被部署高規格生醫與資安防護的模型，這些分類器可能會影響特定敏感任務的回應方式。同時，快取讀取降價也是值得留意的成本變化。更廣義地說，這篇分析提醒工程師：官方系統卡的「未達門檻」結論，不必然等於「風險可忽略」，尤其在資安這類尚未有正式評估框架的領域，實務部署的防護規格可能才是更誠實的風險訊號。

🔗 來源
- 標題：Claude Fable 5.1 and Mythos 5.1: The System Card
- 作者／機構：TheZvi（Don't Worry About the Vase）
- 連結：https://thezvi.wordpress.com/2026/09/04/claude-fable-5-1-and-mythos-5-1-the-system-card/

#Anthropic #ClaudeAI #AISafety #SystemCard #ResponsibleScalingPolicy #AIAlignment #Cybersecurity #Biosecurity #METR #FrontierAI
