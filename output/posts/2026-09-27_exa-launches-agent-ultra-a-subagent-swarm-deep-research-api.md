---
title: 'Exa Launches Agent Ultra: A Subagent Swarm Deep Research API Built for Exhaustive
  List Building'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/26/exa-launches-agent-ultra-a-subagent-swarm-deep-research-api-built-for-exhaustive-list-building/
model: claude-code/sonnet
generated_at: '2026-09-27T20:13:46.524944'
score: 87
---

📌 Exa推出Agent Ultra，把研究做到「窮盡」為止

TL;DR：Exa發布Deep Research API最高檔位Agent Ultra，宣稱在4項benchmark上超越Opus 5.5、GPT-6 Astra與Perplexity Agent。

如果一個研究任務要花上30分鐘、甚至3小時才跑完,還得查證上千筆來源,一般agent恐怕早就見好就收了。Exa偏偏把「不查到窮盡不罷休」做成了一個產品檔位。

🤔 為窮盡式清單建構而生

Exa Agent Ultra是Exa Agent API目前效力最高的模式,鎖定的是那些必須「跑到窮盡」的研究任務:大規模清單建構、實體資料補全,以及需要動用上千筆來源才能回答的問題。

🧩 把任務拆給一群子代理去跑

Exa Agent的做法是把一個任務拆解成多個子任務,交給不同子代理同時研究多個領域;在需要的步驟上調度前沿模型,其餘步驟則交給速度較快的模型處理。Ultra是其中花費運算資源最多的檔位,官方文件指出它會比其他效力等級跑得更久,以換取最完整的結果——一般複雜任務約需30分鐘,難度極高的任務則可能耗時到3小時。

目前Agent Ultra已經以託管API形式上線,只要在請求中設定effort: "ultra"即可呼叫,並非開放權重模型,也無法自行部署(self-host)。它沿用標準的Agent run端點,支援outputSchema、input.data與串流輸出;如果手上已經有一份清單,也可以把既有資料傳入,讓Ultra只補上新結果、排除重複項目。使用者可以先在Exa API Playground中試跑。

📊 4項benchmark的比較數字

根據Exa發布的資料,Agent Ultra在WANDR、DeepSearchQA、WideSearch與Company Find-All這4項研究benchmark上,分別對比了同樣以最高效力設定運行的Opus 5.5、GPT-6 Astra與Perplexity Agent。WANDR是Perplexity提出的benchmark,含500個廣度與深度兼具的資料蒐集任務,附有開放的評測框架(harness);DeepSearchQA則是Google DeepMind的900道多步驟搜尋題;WideSearch測試的是廣泛資訊蒐集能力。Exa在WANDR與DeepSearchQA上各評測了最多200個任務,WideSearch與Company Find-All則各評測100個,不同廠商實際被評分的任務數量並不相同。在WANDR上,Ultra與Opus 5.5的絕對分差是9.1分。凡是廠商已在該評測框架上公開過成績,Exa便直接引用;其餘情況則由Exa自行跑測。

⚠️ 以上所有數字均來自Exa自家的發布文章與benchmark說明,屬廠商自報成績,尚未經過獨立第三方覆現驗證,且各家被評測的任務數量本身就不完全一致,比較時需留意這層落差。

🎯 實務啟示

如果團隊本身就有大規模清單建構或實體資料補全的需求,Agent Ultra這種「用運算換完整度」的檔位值得評估,但因為是純託管API、無法自行部署,也要一併考量資料是否適合交給第三方服務處理。面對廠商自報的benchmark數字,建議先用小規模真實任務驗證再決定是否全面導入,尤其是動輒30分鐘到3小時的執行時間,不適合放進對延遲敏感的流程裡。

🔗 來源
- 標題：Exa Launches Agent Ultra: A Subagent Swarm Deep Research API Built for Exhaustive List Building
- 作者／機構：Michal Sutter／MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/26/exa-launches-agent-ultra-a-subagent-swarm-deep-research-api-built-for-exhaustive-list-building/

#Exa #AIAgents #DeepResearch #LLM #AgentSwarm #Benchmark #AISearch #DataEnrichment #API #MachineLearning
