---
title: 'Meta Superintelligence Labs Releases Muse Spark 1.1: A Multimodal Reasoning
  Model for Agentic Tasks on Meta Model API'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/09/meta-superintelligence-labs-releases-muse-spark-1-1/
score: 96
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T08:09:37.642819'
---

📌 Muse Spark 1.1 閉源推理模型  
TL;DR：Meta 釋出閉源多模態推理模型 Muse Spark 1.1，開發者需依 token 付費使用，消費者可免費體驗。

🎣 開場鉤子  
當開源模型仍是大多數團隊的首選時，Meta 卻將最新的多模態推理模型關起來，只能透過付費 API 呼叫。這種轉向對已經習慣開放權重的開發者意味著什麼？

🤔 背景或問題  
Meta Superintelligence Labs 今日發布 Muse Spark 1.1，並同時開放 Meta Model API 的公開預覽。過去 Meta 的模型主要以開放權重形式提供給開發者，而這次模型改為閉源、託管並按 token 計費。Meta 將其定位為「多模態推理模型」，專門設計用於代理（agentic）任務。

🧩 方法或架構  
- 模型型別：多模態推理模型（輸入可為文字、圖片、影片、檔案；輸出為文字）。  
- 推理機制：屬於推理模型，會在回答前進行思考，且推理力度可依每個請求自行調整。  
- 上下文視窗：1,000,000 token（Meta Model API 檔案列出 1,048,576 token）。  
- API 功能：結構化輸出、平行工具呼叫、Files API、提示快取；在 Responses API 中加入 web_search 工具即可得到帶來源的回答。  
- 定位：根據 Meta 發布的啟動表格，Muse Spark 1.1 在工具使用與工具增強推理方面領先對手，在編碼與多模態理解上排名第三，因而被描述為「 orchestration 模型」，而非編碼精準度的領導者。

📊 資料或結果  
- 報告提示：相較於第一代 Muse Spark，工具使用、電腦使用、編碼與多模態理解均有提升（具體數值未在摘要中給出）。  
- 定價：開發者付費 $1.25 每百萬輸入 token，$4.25 每百萬輸出 token；新帳號獲得 $20 免費額度。  
- 存取方式：消費者可在 Meta AI App 與 meta.ai 上免費使用「Thinking」模式；開發者需透過 Meta Model API 付費呼叫。  
- 地區限制：目前公開預覽僅限美國地區，尚未開放歐盟存取。

💡 深入分析  
Muse Spark 1.1 的核心價值不在於單一任務的最高分數，而在於其「orchestration」能力——模型能主動管理巨大的上下文視窗，記住先前的行動、從較早的工作中檢索資訊，並進行內容壓縮。這種行為解釋了它在工具使用與工具增強推理上的領先表現。同時，因為模型是閉源且按使用量計費，團隊在評估成本效益時需要考慮 token 使用量與所獲得的推理深度之間的權衡。

⚠️ 限制  
- 模型為閉源，無法直接取得權重進行本地微調或離線實驗。  
- 服務目前僅在美國提供預覽，歐盟開發者暫時無法使用。  
- 費用結構依賴 token 計數，長時間或高頻率的代理任務可能導致成本上升。  
- 文章未提供詳細基準分數或具體競爭對手名字，因此無法進行精準的效能比較。

🎯 實務啟示  
對於需要結合多種媒體（文字、圖片、影片、檔案）並且希望模型能自行規劃工具使用、資料檢索與任務分割的場景，Muse Spark 1.1 提供了一個可訂閱的「思考型」API。開發者可以先利用免費額度測試其在代理工作流程中的表現，再根據實際 token 消耗與效能來決定是否將其納入生產管線。同時，注意到其在純編碼精準度上僅排名第三，若主要目標是生成高品質程式碼，可能仍需考慮其他專門的編碼模型。

🔗 來源  
- 標題：Meta Superintelligence Labs Releases Muse Spark 1.1: A Multimodal Reasoning Model for Agentic Tasks on Meta Model API  
- 作者／機構：Asif Razzaq @ MarkTechPost  
- 連結：https://www.marktechpost.com/2026/07/09/meta-superintelligence-labs-releases-muse-spark-1-1/  

#AI #Meta #MuseSpark #MultimodalReasoning #AgenticTasks #ModelAPI #LLM #APIPricing #ToolUse #OrchestrationModel
