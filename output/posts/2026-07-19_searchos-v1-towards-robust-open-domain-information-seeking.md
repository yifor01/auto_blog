---
title: 'SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.15257
score: 87
model: tencent/hy3:free
generated_at: '2026-07-19T08:05:14.817741'
---

📌 【HuggingFace Daily Papers】SearchOS-V1：把搜尋進度變成共享狀態，解決代理卡死迴圈

TL;DR：SearchOS 用顯式共享狀態與排程機制，讓開放領域搜尋代理不再陷入重複搜尋迴圈。

當搜尋代理的對話歷史越長，它們越容易忘記「任務做到哪了」。一旦搜尋失敗，單一或多代理系統常常在原地打轉，把搜尋預算燒光，最後產出殘缺不全的結果。

🤔 **搜尋歷史變長，代理反而跟不上進度**

近期 tool-integrated LLM 讓網頁搜尋成為資訊搜尋代理的核心能力。但論文指出，隨著互動歷史增長，代理越來越難追蹤任務進度；當搜尋嘗試無法產出有用證據時，現有單一與多代理系統會被困在重複迴圈中，浪費搜尋預算並犧牲最終輸出的品質與完整性。

🧩 **把隱含進度變成顯式、持久、共享的狀態**

作者提出 SearchOS，一個系統層級的多代理框架，將脆弱且隱含的搜尋進度轉為顯式、持久且共享的狀態。具體做法分為兩層：

- 任務形式化：將開放領域資訊搜尋定義為「帶依據引用的關聯式 schema 補全」（relational schema completion with grounded citations）。代理負責發現實體、在連結表格中填補屬性，並將每個數值錨定到來源證據。
- Search-Oriented Context Management（SOCM）：把演進中的狀態外部化為四個元件——FrontierTask、EvidenceGraph、CoverageMap 與 FailureMemory。

🧩 **用平行排程與中介層填補覆蓋缺口**

建立在 SOCM 之上，SearchOS 設計了數個關鍵機制：

- Pipeline-parallel 排程：重疊子代理的執行，並持續把空出來的 slot 填入針對未解決覆蓋缺口的任務，提升利用率與吞吐量。
- SearchTool Middleware Harness：攔截模型與工具互動，記錄具來源依據的證據，並對停滯或預算耗盡做出反應；同時提供可重複使用的階層式技能系統（含 strategy 與 access skills），強化搜尋流程並避免跨執行重複失敗模式。

📊 **在兩個基準上全面領先 baseline**

在 WideSearch 與 GISA 兩個評測集上，SearchOS 在受評的單一與多代理 baseline 中，於所有指標均取得領先，顯示其在穩健資訊搜尋協作上的潛力。

🎯 **把「進度」當成一等公民來設計**

對工程師而言，與其讓代理靠隱含上下文追進度，不如把任務狀態、證據圖與失敗記憶外部化；搭配中介層攔截與技能重用，能有效避免多代理搜尋系統在實際部署中空轉燒錢。

🔗 **來源**
- 標題：SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration
- 連結：https://huggingface.co/papers/2607.15257

#MultiAgent #InformationSeeking #LLM #SearchAgent #ToolIntegrated #SearchOS #SOCM #PipelineParallel #EvidenceGraph #OpenDomain
