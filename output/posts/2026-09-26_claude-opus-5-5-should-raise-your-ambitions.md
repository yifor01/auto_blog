---
title: Claude Opus 5.5 Should Raise Your Ambitions
source: Don't Worry About the Vase
url: https://thezvi.wordpress.com/2026/09/26/claude-opus-5-5-should-raise-your-ambitions/
model: claude-code/sonnet
generated_at: '2026-09-26T20:00:26.070973'
score: 76
---

📌 Anthropic 發布 Opus 5.5：效能打平 Fable，價格砍四成

TL;DR：Opus 5.5 號稱效能看齊 Fable 5.1，跑起來卻比舊版 Opus 便宜四成。

作者在文章開頭就說「基準測試很漂亮，但忽略它」，這句話本身就很反直覺，畢竟大家平常最愛拿分數說話。

🤔 **這次到底發布了什麼**

Anthropic 推出 Claude Opus 5.5，是新的 Claude 5.5 家族首發模型。官方定位是「在多數工作上達到 Claude Fable 5.1 的水準，但執行成本比 Opus 5 低 40%」。作者認為這其實是保守說法，Opus 5.5 在不少場景已經超越 Fable 5.1，只是 Anthropic 一貫傾向低調行銷。官方特別強調三個重點：agentic coding（自主寫程式）、資安能力，以及溝通表達的改善，並提到模型能更可靠地長時間獨立運作。

Opus 5.5 提供零資料保留（ZDR）選項，但作者質疑這點不一致：既然 Opus 5.5 至少和 Fable 5.1 一樣強，甚至在網路資安任務上被形容為「極強」，卻只有 Fable 5.1 能用 ZDR，邏輯上說不通，官方雖給出技術解釋但作者並不買帳。

📊 **基準測試怎麼看**

Artificial Analysis 的智慧指數把 Opus 5.5 排到全場最高的 58 分，在多數追蹤的基準上贏過除 Astra 以外的所有模型，且往往還領先 Astra，包括 AA-Briefcase、GDPval-AA SciCode、AA-Omniscience Index 與 HLE。Astra 最大的優勢落在 GDP.pdf 這一項。新加入的 Terminal-Bench-Science 0.1 上，Astra 拿下 63%，Opus 5.5（xhigh 設定）緊追在 62%，其餘模型都不到 50%。

在 Omniscience 測驗中，Opus 5.5 拿到 46 分，略高於 Fable 5.1 與 Astra 的 43 分，原因不是答對題數更多，而是它猜測與幻覺更少、更願意承認「不知道」。WeirdML v3 上 Astra 仍以 42.2% 領先，Opus 5.5 以 31.2% 排第二，Fable 5.1 為 26%，非 OpenAI、非 Anthropic 陣營最好的是 Kimi K3，僅 7.3%。

有意思的是 Opus 5.5 落後 Fable 5.1 的項目有規律可循：包括七項 Vals 專業任務、MedCode、SAGE 以及兩項 MLCR，作者引用自家 Opus 5.5 的分析指出，這批任務多半是「純粹以正確性評分」的領域問答，一旦文字表達品質不列入評分，Fable 5.1 的優勢就會顯現；反過來說，只要輸出的呈現方式也算數，人類與 AI 評審都更偏好 Opus 5.5。像 ProgramBench（完全解決）這項，Astra 只拿 5.5%、Fable 7%，Opus 5.5 卻跳到 18.5%。

💡 **寫作、防護機制都有感**

Anthropic 員工 Sholto Douglas 提到模型在理解與建模 3D 空間上有進步；Tom Brown 開玩笑說「順便把口音也修好了」；Claude 官方說法則是 Opus 5.5 溝通更自然，會把重要資訊放在最前面，也更會遵守使用者給的寫作規則，讓長時間對話更容易跟上。多位早期測試者反覆提到 Opus 5.5 好聊、好合作，且比 Opus 5 便宜約四成。

防護分類器（classifier）行為與 Fable 5.1 相近，有測試者表示它在阻擋「非資安相關」任務時的誤判明顯減少，也有人形容連續上百次對話都沒被拒答過，但也有零星回報遇到莫名其妙的拒絕牆。整體而言分類器觸發頻率差不多，但作者認為觸發得更「合理」，且觸發後恢復正常對話的能力也更好。

價格方面，Opus 5.5 定價 $4/$20，比 Opus 5 低 20%，快取價格 $0.20，低了 60%，官方估計整體成本平均下降 40%，速度提升 30%。訂閱方案的用量上限也提高了。另有 Fast 模式，定價 $8/$40，速度最多可達 2.5 倍。同時間 OpenAI 也把 GPT-6 Sol 價格砍半到 $2/$10，Luna 更只要 $0.10/$0.50，主打依任務等級混搭不同模型；相較之下 Anthropic 這次幾乎是喊出「大部分任務都直接用 Opus 5.5 就好」。

⚠️ **仍有落差與不確定**

Opus 5.5 並非全面領先，在 GDP.pdf、WeirdML v3 等項目仍輸給 Astra；ZDR 政策的不一致也還沒有讓人信服的解釋；分類器行為雖整體改善，個別使用者仍回報過偶發的異常拒答。

🎯 **實務啟示**

如果你原本因為預算考量而在 Fable 級模型與較便宜的 Opus 之間妥協，Opus 5.5 值得重新評估：它把「Fable 級效能、Opus 級價格」做成了現實選項，尤其在 agentic coding 與需要長時間自主運作的任務上。價格與速度都有明顯改善，適合拿來重新跑一次你手上任務的模型選型測試。

🔗 **來源**
- 標題：Claude Opus 5.5 Should Raise Your Ambitions
- 作者／機構：TheZvi（Don't Worry About the Vase）
- 連結：https://thezvi.wordpress.com/2026/09/26/claude-opus-5-5-should-raise-your-ambitions/

#ClaudeOpus55 #Anthropic #LLM #AgenticCoding #AIBenchmarks #ArtificialAnalysis #ZeroDataRetention #GPT6 #AIPricing #FrontierModels
