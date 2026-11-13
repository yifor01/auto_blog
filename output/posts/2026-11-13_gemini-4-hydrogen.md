---
title: Gemini 4 Hydrogen
source: Hacker News
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/
model: claude-code/sonnet
generated_at: '2026-11-13T22:47:57.183392'
score: 94
---

📌 Google發布Gemini 4 Hydrogen，主打速度與Agentic執行力

TL;DR：Google推出Gemini 4家族新成員Hydrogen，定位為高速、低成本的日常編碼與agentic執行模型，並導入多模型協作機制Orchestrator。

當深度推理模型Carbon與Argon負責啃最難的架構決策,日常寫程式、跑測試、驗證改動這種高頻但重複的工作,其實更需要一個跑得快、不囉嗦的執行模型。這正是Google這次發布Gemini 4 Hydrogen要補上的位置。

🤔 **Gemini 4家族的分工：深度推理交給Carbon/Argon，快速執行交給Hydrogen**

Google DeepMind SVP暨首席AI架構師Koray Kavukcuoglu在發布文中說明，Hydrogen的定位是「把尖端智慧帶給每個人」,強調速度與效率，而非像Carbon、Argon那樣主攻長時程深度推理。Hydrogen已開放至Google AI Studio各層級、Gemini API、Gemini for business、Gemini app、Google搜尋,以及付費Google AI Pro/Ultra用戶的Google Antigravity。

📊 **跑分與定價：Artificial Analysis Intelligence Index小勝Argon,價格全文全context窗口統一計費**

在Artificial Analysis Intelligence Index上，Hydrogen以預設high thinking等級拿下51分，超過Argon的50分；拉到最高xhigh思考等級則達54分。定價在完整100萬token context窗口內統一為每百萬輸入token 1.50美元、每百萬輸出token 7.50美元。相較前代Gemini 3.8 Flash，Hydrogen在高速設定下任務完成速度快2.5倍，Terminal-Bench 4.1分數從18.2%跳升到57%（超過三倍），並將「捏造內容」的比例降低超過5倍。

在多模型協作情境下，Antigravity新推出的Orchestrator功能會在同一個session裡動態切換Carbon與Hydrogen：在Terminal-Bench 4.0上，Orchestrator達到接近Carbon的任務成功率，同時平均少耗24%配額、快19%完成。在其他基準上，Hydrogen在HLE-Diamond拿下同級別最高的58.8%，在Vals Tax Agent Bench排名第一（52.3%），在Vals Legal Research Bench並列第一（55.8%），在Agent Arena排名第5，在新發布的Multimodal Knowledge Agent基準拿下53.4%，在Agents' Last Exam v1.1達71.6%。部分合作夥伴在複雜圖形、SQL與資料密集型企業工作流測試中，觀察到Hydrogen比3.8 Flash快2到2.8倍、token用量減少12%到23%。

💡 **多模型協作與四段式思考等級，是這次發布的設計重點**

除了Orchestrator這種「Carbon當架構師、Hydrogen當執行者/驗證者」的分工模式，Hydrogen本身也提供low、medium、high（預設）、xhigh四個思考等級，讓使用者依任務難度選擇品質、延遲與成本的平衡點。Google也強調Hydrogen擅長原生平行批次處理檔案讀取與搜尋呼叫，而非逐一檢視檔案，這是它在大型程式庫導覽上比前代更快的原因之一。

🎯 **實務啟示**

對正在設計multi-agent工作流的工程團隊，Hydrogen與Orchestrator示範了一種務實的成本結構：架構判斷與疑難排錯留給Carbon等深度推理模型，大量重複的程式碼撰寫、測試執行、worker/verifier角色交給更便宜更快的Hydrogen，再靠Orchestrator自動切換,而不必整個pipeline都綁死在單一模型上。需提醒的是，以上效能數據均為Google官方自行公布的benchmark結果，尚待第三方獨立覆核。

🔗 **來源**
- 標題：Gemini 4 Hydrogen
- 作者／機構：Koray Kavukcuoglu，Google DeepMind
- 連結：https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/

#Gemini4 #GoogleDeepMind #LLM #AgenticAI #Orchestrator #GoogleAntigravity #AIBenchmark #DeveloperTools #MultiModel #AICoding
