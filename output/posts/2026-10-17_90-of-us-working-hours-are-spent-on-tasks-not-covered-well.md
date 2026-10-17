---
title: 90% of US working hours are spent on tasks not covered well by AI benchmarks
source: Hacker News
url: https://www.mercor.com/research/labor-index/benchmark-map/
model: claude-code/sonnet
generated_at: '2026-10-17T19:31:27.826097'
score: 93
---

📌 AI benchmark 測不到的 90% 工時：Mercor 的覆蓋率地圖揭露了什麼

TL;DR：Mercor 分析 923 個美國職業後發現，九成工時對應的任務幾乎沒有 AI benchmark 覆蓋。

市面上的 AI benchmark 數量這幾年暴增，但當 Mercor 把這些 benchmark 一個個對應到真實的美國職業任務後，得出一個刺眼的結論：九成的美國工時，落在幾乎沒有任何 benchmark 測過的任務上。

🤔 **我們測的到底是「AI 能力」還是「AI 最想被測的那部分」**

Mercor 想回答一個基本問題：現有的 AI benchmark 到底覆蓋了多少「真正有經濟價值」的工作？為此，他們建立了一張 Benchmark Map，把美國勞動力依照 O*NET 職業分類拆成 923 個職業、歸入 22 個職業家族，再看每個職業有多少任務被現有 benchmark 實際測過。

🧩 **方法：O*NET 任務分類 + LLM 判定 + 人工驗證**

O*NET 這套美國勞動部的分類體系，把 923 個職業細分成總計 18,797 項任務。Mercor 挑選了 29 個以品質與經濟相關性為標準的 benchmark，接著用 LLM 當裁判，把每一條 benchmark 的 prompt 標記對應到一個或多個 O*NET 任務；這套標記方式有在 Mercor 自家的 APEX benchmark 子集上與人類專家標記做過比對驗證。一項任務只要被對應到至少 5 條 benchmark prompt，就被判定為「有覆蓋」。最後，再結合 Hatgis-Kessell 等人對每項任務佔工時比例的估算,換算出整體工時的覆蓋率。

📊 **208／923 個職業有像樣的覆蓋，6 個職業家族完全空白**

結果顯示，923 個職業裡只有 208 個至少有一項任務達到 5 條 prompt 以上的覆蓋門檻，22 個職業家族裡有 6 個完全沒有任何職業達標。覆蓋的分布也不是隨機的：被 Eloundou 等人（2023）標記為「AI 曝險」（AI-exposed）的任務，被 benchmark 覆蓋的機率大約是「非曝險」任務的 6 倍；在控制曝險程度後，薪資規模（wage bill）越大的職業，任務被覆蓋的機率也顯著更高；而 O*NET 自己對任務重要性打的 1 到 5 分裡，最重要那一級的任務被覆蓋的機率，是最不重要那一級的 6 到 10 倍。一個具體對照：同樣被標記為高度 AI 曝險的律師任務被大量覆蓋，但同樣曝險的法務助理（legal secretaries）與法院書記官（court clerks）任務卻幾乎無人問津。

💡 **Benchmark 設計者在追著「大市場、容易自動化」跑**

這個偏斜的分布說明了一件事：benchmark 社群在選題時,傾向優先測試那些「AI 曝險程度高」又「薪資規模大」的任務,這解釋了為什麼軟體工程與財務分析類 benchmark 密集,而卡車駕駛、天然氣廠操作這類職業幾乎沒有對應題目。換句話說,現有 benchmark 分數高,反映的可能只是「AI 在最容易被測、最被重視測的那一小塊工作」表現好,而不是它在整體勞動市場裡真正能取代多少工作。

⚠️ **作者自己承認：這份地圖是「暫時的」**

Mercor 在方法論裡明確指出幾個限制：這 29 個 benchmark 並非完整或具代表性的樣本，任何不完整的清單都會讓經濟覆蓋率的估計偏低，但難以界定偏誤的範圍；為了讓整體覆蓋率的估計更準確，他們對每個職業家族設了 benchmark 數量上限，這會讓軟體工程這類已經被大量測試的領域的覆蓋率被低估；此外，「經濟真實性」這類選題標準本身帶有主觀性。他們也坦言，納入已經飽和（saturated）的 benchmark 可能會高估覆蓋率，因為飽和往往反映題目設計不夠貼近真實場景,而不是 AI 真的在該任務上表現優異。

🎯 **對做 agent 產品和做 benchmark 的人都是一個提醒**

如果你在用 SWE-bench、法律考試題或財務分析分數來推斷 AI「已經能取代某個職業」，這份地圖提醒了一件事：那些分數覆蓋的往往只是曝險程度高、薪資規模大、任務重要性高的一小塊，中段的知識工作（像法務助理、行政支援）幾乎是空白地帶。對正在評估 AI 能否自動化某項業務流程的工程團隊來說，自己去對照實際任務清單，可能比看公開 benchmark 排行榜更可靠。

🔗 **來源**
- 標題：90% of US working hours are spent on tasks not covered well by AI benchmarks
- 作者／機構：Mercor（Labor Index Research）
- 連結：https://www.mercor.com/research/labor-index/benchmark-map/

#AIBenchmarks #LaborEconomics #ONET #AIEvaluation #FutureOfWork #Mercor #AIExposure #JobAutomation #LLMEvaluation #EconomicResearch
