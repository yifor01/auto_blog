---
title: 'Meet Factory Droid 1.0: A Model-Independent Coding Agent Harness Built on
  Script Mode'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/31/factory-droid-1-0-frontier-harness/
model: claude-code/sonnet
generated_at: '2026-10-31T20:32:28.002160'
score: 100
---

📌 Factory Droid 1.0：讓模型寫程式驅動工具呼叫，成本直降15%

TL;DR：Factory Droid 1.0預設開啟Script Mode，模型用程式碼批量驅動工具呼叫，在Claude Opus 5.5上成本降15%。

一般Coding Agent迴圈裡，每一次工具呼叫的結果都要塞進模型的context，呼叫一多，context就被塞滿。Droid 1.0的解法很直接:別讓工具結果直接進context,讓模型自己寫程式去跑。

🤔 **一次模型請求，驅動數百次工具呼叫**

Factory把harness定義為圍繞模型的一切:提示詞、工具、工具結果如何回傳,以及整個迴圈。Droid 1.0是這套harness的最大更新,核心變化是程式化工具呼叫(Programmatic Tool Calling, PTC)現在預設開啟。使用者可以自選模型,或讓Factory Router挑選成本效益較佳的模型組合。

🧩 **Script工具:模型寫JavaScript,在沙箱裡跑**

在標準迴圈中,每一次工具輸出都會落進模型的context;而PTC讓模型改寫一段程式,Droid把這套做法實作成一個Script工具——模型寫的JavaScript在沙箱中執行,沙箱本身沒有檔案、網路或系統存取權限,原始檔案、搜尋結果與日誌都留在程式內部,只有列印出來的輸出才回傳給模型,獨立的呼叫還能並行執行。這個思路建立在CodeAct(Wang et al., 2024)之上。

📊 **Claude Opus 5.5上省15%，10個模型預設開啟**

Factory報告稱,在Claude Opus 5.5上,Script Mode相較直接工具呼叫可將Droid的成本降低15%,目前已在10個模型上預設開啟,包括GPT-6.1 Sol與Kimi K3。測試方法上,Factory讓每個harness在同一模型上對跑,每個任務跑3輪,時間為2026年10月23日至28日,只有兩種harness都在全部3輪中通過的任務才計入成本與時間比較(Terminal-Bench 4的數據為Factory自家依其方法論跑出的結果)。

💡 **內部Agent Factory迴圈,自己找Bug自己改**

素材提到,這次更新大多數改動來自一個內部的Agent Factory迴圈:Agent讀取失敗案例並提出修改,在每個受影響的模型家族上測試,再由工程師審核並合併。

⚠️ **數據來自Factory自身測試,非第三方獨立基準**

需要注意的是,15%成本下降與Terminal-Bench 4的對比結果都是Factory自己執行、自己報告的數據,文中並未提及第三方獨立複現。

Droid 1.0以桌面應用與終端UI的形式提供,Droid SDK可從Node執行同一套harness,支援會話、串流與MCP工具,付費方案每月20美元起。

🎯 **實務啟示**

如果你的Agent任務經常觸發大量工具呼叫(比如批量檢索、多檔案操作),把工具結果留在沙箱、只讓模型看列印輸出,是一個能直接降低context消耗與成本的工程模式,值得在自建harness時參考。Script工具加CodeAct的做法,也提示了一個方向:把「模型決策」與「大量機械性工具呼叫」拆開,是壓低多工成本的通用思路。

🔗 **來源**
- 標題：Meet Factory Droid 1.0: A Model-Independent Coding Agent Harness Built on Script Mode
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/31/factory-droid-1-0-frontier-harness/

#AIAgent #CodingAgent #ProgrammaticToolCalling #CodeAct #FactoryDroid #DeveloperTools #LLM #AgentHarness #OpenSource #SoftwareEngineering
