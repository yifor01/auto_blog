---
title: GPT-6-Astra Can Do Ambitious Things
source: Don't Worry About the Vase
url: https://thezvi.wordpress.com/2026/09/12/gpt-6-astra-can-do-ambitious-things/
model: claude-code/sonnet
generated_at: '2026-09-12T19:34:52.879761'
score: 75
---

📌 【OpenAI】GPT-6 Astra 上線，官方喊出「AGI 時代」

TL;DR：OpenAI 發布 GPT-6 Astra，主打 3D／電腦操作／科學任務，官方宣稱多項頂級 benchmark 成績。

當一家公司的總裁在發布文案裡直接寫下「歡迎來到 AGI 時代」，工程師該興奮還是該冷靜看待數字？GPT-6 Astra 的發布，把這個問題又推上了檯面。

🤔 **這次到底發生了什麼**

OpenAI 正式推出 GPT-6 Astra，評論者 TheZvi 在部落格中形容，Sol 到 Astra 的進步幅度，比 Fable 5 到 Fable 5.1 的進步還要大。他認為 Astra 在「野心勃勃的專案」上是目前最強，尤其在 3D 相關任務、遊戲、電腦操作（computer use）與 subagent 協調方面表現突出，多項 benchmark 都出現明顯躍進。但他也提醒，Astra 並非在所有面向都全面領先：一般程式撰寫上進步有限，多輪來回討論場景中，他個人仍偏好 Fable 5.1，並持續把 Fable 系列當作主要編輯工具。

值得注意的是，OpenAI 研究員 roon 在發布數天後又公開表示「內部已經有比 Astra 高一個級別的模型」，暗示 Astra 的領先視窗可能相當短暫。

🧩 **官方宣稱的能力與數字**

OpenAI 總裁 Greg Brockman 以「歡迎來到 AGI 時代」作為定調，執行長 Sam Altman 則表示 Astra 在 FrontierMath Tier 4 拿下 98%、ARC-AGI 3 拿下 99.9%、ExploitBench 拿下 100%（這些均為 OpenAI 官方公布的數字，尚缺乏第三方比較基準）。官方展示的具體案例包括：用 KiCad 排版印刷電路板、在 Unity 搭建 3D 城市場景、用 FreeCAD 與 Blender 製作動畫版汽車變速箱模型、根據 W-2 表單填寫報稅草稿等。在科學任務上，OpenAI 研究員 Noam Brown 提到 Astra 協助改進了「相鄰質數間距」相關的數學結果，把已知上界從 212 縮小到 186（先前的 212 同樣是 OpenAI 團隊得出），不過報導也提到對於這項結果具體證明了什麼，外界仍有爭議。

💡 **工程師實際會摸到的東西：價格與快取**

Astra 的定價為每百萬 token 輸入 10 美元、輸出 50 美元，快取寫入 12.5 美元，快取命中的輸入只要 1 美元；若單次提示超過 27.2 萬 token，輸入價格會翻倍、輸出價格上調 50%。作為對照，Fable 5.1 的標價同樣是每百萬 token 10/50 美元，但快取命中的輸入只要 0.25 美元，比 Astra 便宜不少，這對重度依賴長上下文快取的應用來說是實際會影響選型的差異。

⚠️ **要留意的地方**

多數展示案例目前缺乏獨立第三方的對照組，例如「4 倍人類速度操作試算表」「PCB 排版」這類 demo 令人印象深刻，但報導本身也承認「我們缺乏比較基準」。是否構成 AGI 本身也仍有爭論，Zvi 明確表示他不認為這已經是 AGI，也提醒外界不要過早使用這個標籤。

🎯 **實務啟示**

對工程師而言，比較務實的做法是把 Astra 和 Fable 5.1 都放進手邊最困難的任務中實測，依任務類型（3D／電腦操作／科學計算 vs. 一般程式撰寫與多輪討論）決定用哪一個；若應用大量依賴 prompt caching，Fable 5.1 目前的快取讀取成本明顯更低，值得在成本估算時納入考量。

🔗 **來源**
- 標題：GPT-6-Astra Can Do Ambitious Things
- 作者／機構：TheZvi, Don't Worry About the Vase
- 連結：https://thezvi.wordpress.com/2026/09/12/gpt-6-astra-can-do-ambitious-things/

#GPT6Astra #OpenAI #AGI #LLM #AIAgents #ComputerUse #Benchmark #AIIndustry #ModelComparison #TokenPricing
