---
title: 'Google Research Releases ToolGrad: Answer-First Framework Hits 99.8% Pass
  Rate for Tool-Use Data Generation'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/10/google-research-releases-toolgrad-answer-first-framework-hits-99-8-pass-rate-for-tool-use-data-generation/
model: claude-code/sonnet
generated_at: '2026-09-12T19:29:20.402186'
score: 108
---

📌 【Google Research】把工具呼叫資料生成順序整個倒過來

TL;DR：ToolGrad 先造出可執行的工具鏈再回頭寫查詢,生成失敗率僅 0.2%,程式碼與模型全部開放。

過去要教 LLM 學會呼叫工具,得先靠另一個 LLM 瞎猜使用者可能會問什麼,再派一個 agent 用 depth-first search 硬找答案——找不到就整筆資料作廢,浪費的運算就這樣憑空蒸發。ToolGrad 的做法是把這個順序整個倒過來。

🤔 **query-first 的浪費在哪裡**

Google、東京大學、RIKEN AIP 與東北大學的研究團隊指出,先前的資料生成管線如 ToolBench、ToolACE 都是 query-first:從 API pool 抽樣,讓 LLM 想像出一個合理的使用者指令,再派 DFS agent 去找出滿足這個指令的工具呼叫路徑。問題是這個搜尋不保證會成功,一旦搜尋走進死路,前面花掉的算力就白費,樣本也只能丟棄。論文把這個問題形容為「從一個複雜且經常失敗的 agent 探索過程中蒸餾出有價值的軌跡」,本質上就是低效率。

🧩 **先建工具鏈,再回頭標註查詢**

ToolGrad 反過來做:先透過實際呼叫 API,建構出一條經過驗證的 ground-truth 工具鏈,再用一次 LLM 呼叫替這條「已經跑得通」的鏈標註對應的使用者查詢。因為工具鏈本身已經是明確、可執行的事實,遠比憑空想像的查詢來得清楚,所以 chain-to-query 這一步只需要單次 LLM 呼叫就能完成。每一輪迭代跑完固定的模組序列,就能產出一筆完整樣本:一個使用者查詢、一條驗證過的 API 工作流程、以及最終回應。專案預設設定是每個工作流程從 50 個抽樣 API 中跑 10 輪迭代。

📊 **16,000+ API 資料庫上,失敗率只有 0.2%**

研究團隊在包含 16,000 多個真實世界 API 的 ToolBench API 資料庫上進行資料生成,並與 ToolBench 原本 DFS-based 的 query-first 方法做比較。論文指出僅有 0.2% 的案例會失敗,發生在 agent 對 3 個選定的 API,在全部 10 輪迭代中都拿不到成功回應,只能存下一筆空樣本。

團隊用 Gemini 2.5 Flash-Lite 生成了 500 筆樣本的 ToolGrad-500 資料集,拿去對 Gemma-3 的 1B、4B、12B 版本做後訓練,並在 Berkeley Function Calling Leaderboard 上評測——這是一個工具集與 ToolBench 完全不同的 out-of-distribution 測試。文章表示,經過這樣微調的 Gemma-3 表現已能與前沿的 proprietary 模型並列,不過原文並未附上具體分數細項。

🎯 **實務啟示**

程式碼採 Apache-2.0 授權,ToolGrad-500 資料集與 1B/4B/12B 模型都已上架 Hugging Face,也有對應的 PyPI 套件可以直接安裝;複現腳本鎖定 BFCL V1、V2,透過客製化 fork 在 vLLM Docker 映像檔中跑推論,並在單張 NVIDIA A100 40GB 上驗證過。對正在做 tool-use fine-tuning、又苦於資料生成成本太高的團隊來說,這是一條可以直接落地、良率極高的資料管線。

🔗 **來源**
- 標題：Google Research Releases ToolGrad: Answer-First Framework Hits 99.8% Pass Rate for Tool-Use Data Generation
- 作者／機構：Michal Sutter，MarkTechPost（研究團隊來自 Google、東京大學、RIKEN AIP、東北大學）
- 連結：https://www.marktechpost.com/2026/09/10/google-research-releases-toolgrad-answer-first-framework-hits-99-8-pass-rate-for-tool-use-data-generation/

#ToolGrad #ToolUse #LLM #Gemma #FunctionCalling #SyntheticData #GoogleResearch #AIagents #OpenSource #MachineLearning
