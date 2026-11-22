---
title: 87% of the Anthropic power will come from gas and 11% from coal in 2028
source: Hacker News
url: https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/
model: claude-code/sonnet
generated_at: '2026-11-22T22:42:34.262148'
score: 71
---

📌 調查報告:Anthropic 2028年用電,87%靠天然氣、11%靠煤

TL;DR:產業調查指出,Anthropic美國資料中心短期內電力幾乎全靠化石燃料,年排碳量可能超過加州全州電力部門。

Anthropic對外宣稱要「拓展地熱、風電、太陽能等能源組合」,但攤開其美國資料中心目前已簽署的合約,你會發現綠能佔比是——零。

🤔 背景:BYOP 熱潮下,資料中心開始自備電廠

近年資料中心業者不再只靠電網供電,轉而採用「BYOP」(Bring Your Own Power,自備電源)模式,直接在場內建置燃氣發電機。Better Data Center Project 先前的調查已指出,目前規劃中的 BYOP 燃氣容量達 177 GW,足以供應美國 65% 家庭用電;而在這些規劃中,2032 年前renewable(可再生能源)佔比預估不到 20%。除了場內自備電源,另外還有 200 GW 的新建燃氣電廠正因資料中心用電需求而上線。這次報告以 Anthropic 作為個案研究,分析其運算承諾背後的電力來源。

🧩 怎麼算出來的:邊際發電模型

研究團隊彙整 Epoch AI 的追蹤資料、Anthropic 自身公告與申報文件、Amazon 與 SpaceX 的合作揭露,以及 The Information、Semafor 等媒體報導,逐一比對每座資料中心的電力來源。對於有場內燃氣或新建電網燃氣的案場,採用許可文件中的排放係數;對於單純併網、沒有新建發電的案場,則用 EPA 的 AVERT 工具模擬哪些電廠會承接新增負載,估算短期邊際排放率。PUE(電力使用效率)假設落在 1.1 至 1.2,利用率假設 60% 至 80%。

📊 數據:87% 天然氣、11% 煤,排碳上看 3800 萬公噸

截至 2026 年 10 月,Anthropic 已簽約 15 GW 運算容量,其中約 5.9 至 9.6 GW 可對應到具體資料中心案場。9.6 GW 大約相當於 700 萬戶家庭用電,或加州電力尖峰需求的 18%。報告估算:

- 短期內約 87% 的電力來自天然氣、11% 來自煤,幾乎沒有電網綠能被歸因於 Anthropic 的用電,因為新增負載會由可調度的化石燃料邊際機組補上。
- 2028 年這些案場上線後,Anthropic 的用電相關 CO2e 排放估計為每年 1700 萬至 3800 萬公噸,中位估算為 3200 萬公噸,可能超過加州全州電力部門 2024 年的排放量(3110 萬公噸),也可能超過 Meta、Microsoft、Google 三家 2025 年 Scope 2 排放量總和(分別為 590 萬、1200 萬、1500 萬公噸)。
- 這相當於讓美國整個資料中心產業 2024 年排放量(1.05 億公噸)增加 16% 至 36%,或讓美國整體電力部門排放量(2025 年 14.85 億公噸)增加 1.1% 至 2.5%。
- Anthropic 用電的平均碳強度估計為每 MWh 1,033 至 1,076 磅 CO2e,比美國電網平均值(767 磅)高出約 35%。

💡 深入分析:省下的許可成本,轉嫁成的健康代價

報告指出,約 25%(2.5 GW)的 Anthropic 合約電力來自場內燃氣,其中 80% 使用效率較差的simple cycle渦輪機與引擎,單位發電排放的污染物遠高於現代combined cycle電廠。依 EPA 的「每噸效益」估算方法,這些排放每年可能造成 20 億至 30 億美元的健康損害,NOx 排放超過 13,000 噸、PM2.5 超過 2,000 噸。Anthropic 雖公開表示會要求供電廠「使用排放控制技術,包括SCR(選擇性催化還原)」,但報告指出其自 2026 年 5 月起使用 SpaceX Colossus 2 設施的運算容量(年底前最高達 600 MW),該設施多數電力來自臨時、未取得許可的渦輪機,且大多未配備 SCR。Anthropic 另簽約 Nscale 位於西維吉尼亞 Monarch Compute Campus 的 460 MW 電力(洽談中最高 920 MW),該設施以排放甲醛與危害性空氣污染物較高的往復式引擎供電。

⚠️ 數字的不確定性

17 至 3800 萬公噸的排放區間反映了 Anthropic 平均用電量的不確定性,包括冷卻需求與平均利用率等因素,實際數字仍有待更明確的揭露才能收斂。

🎯 實務啟示

對從事 MLOps 或基礎設施規劃的工程師而言,這份報告提醒:算力擴張的碳足跡與供電結構,正在成為選擇雲端供應商、資料中心區域時不可忽視的變數,也可能是未來企業採購AI運算服務時需要納入評估的風險項目。

🔗 來源
- 標題:87% of the Anthropic power will come from gas and 11% from coal in 2028
- 作者／機構:happosai
- 連結:https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/

#AI #DataCenters #Anthropic #ClimateChange #EnergyConsumption #CarbonEmissions #BYOP #AIInfrastructure #Sustainability #TechPolicy
