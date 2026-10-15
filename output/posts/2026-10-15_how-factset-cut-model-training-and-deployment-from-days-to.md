---
title: How FactSet cut model training and deployment from days to hours with Databricks
  AI Runtime
source: Databricks
url: https://www.databricks.com/blog/how-factset-cut-model-training-and-deployment-days-hours-databricks-ai-runtime
model: claude-code/sonnet
generated_at: '2026-10-15T20:41:33.850233'
score: 99
---

📌 FactSet 用 Databricks AI Runtime，把模型微調從天縮到小時

TL;DR：FactSet 自然語言轉公式系統導入 serverless GPU 微調，訓練部署週期從天縮短到小時。

當使用者的查詢愈來愈複雜，純粹靠檢索硬撐的 RAG 系統終究會撞牆——這正是 FactSet Text-to-Formula（TTF）團隊走到的十字路口。

🤔 當 RAG 撞上複雜度天花板

FactSet 的 TTF 系統要解決的問題很具體：把投資專業人士的自然語言請求，轉換成正確的 FactSet Query Language（FQL）公式。團隊最初以 retrieval-augmented generation（RAG）打底，靠檢索找出相關範例與資訊來生成答案。但隨著使用量成長，查詢愈趨專業化、公式也愈複雜，單靠檢索的做法開始遇到品質天花板。

🧩 把微調納入 Compound AI 架構，再交給 serverless GPU

FactSet 於是把 fine-tuned 開源模型納入 Compound AI 架構，讓模型直接學習 FQL 的結構與模式，而不只是在推論時依賴檢索。團隊在 TTF 早期導入微調模型後，發現端到端延遲降低了約 60%。

隨著訓練資料持續累積，微調不再是偶一為之的實驗，而是每兩到三週就要重跑一次的常態工作。這對基礎設施是另一種考驗：每次有新資料或新模型要測試，重新準備環境、設定 GPU 運算資源的工作都會直接疊加到開發週期裡；而不同模型、不同 prompt 長度與輸出特性，所需的運算配置也不一樣，若把訓練環境綁死在固定的 GPU 設定上，反而會讓實驗更難進行。

FactSet 選擇用 Databricks AI Runtime 在 serverless GPU 基礎設施上執行這些微調工作。工程師可以依照特定訓練任務的需求挑選運算資源，不需要事先佈建與設定底層 GPU 環境。TTF 的訓練流程同時銜接著既有的資料、實驗、模型管理與治理體系：團隊用 MLflow 追蹤模型開發與實驗過程，底層資料則維持在既有的 Lakehouse 環境中受到治理。把 GPU 訓練留在這套工作流程裡，工程師就能在受治理的資料上訓練新模型、追蹤產出的 artifacts，並往部署推進，不必為微調維護一套獨立的 GPU 堆疊。

📊 從天到小時，效果如何疊加

對 FactSet 而言，這把建置、訓練、部署一個客製化 TTF 模型所需的時間，從過去的「天」級別縮短到「小時」級別。對一個每兩到三週就要重新訓練的系統來說，這個差距會不斷累積：新資料能更快進入新模型，工程師也能把更多時間花在改善 TTF 本身，而不是準備訓練所需的基礎設施。

團隊目前持續採用與評估 Llama 系列等開源模型，模型選擇一直是 TTF 演進的核心環節之一；未來也打算針對查詢拆解（query decomposition）、元件抽取（component extraction）與函式庫識別（library identification）等子任務，探索更多專用的微調模型。微調管線本身則建立在 Databricks Lakeflow Jobs 與 Pipelines 之上，做成一套可重複使用的框架，方便其他團隊以低設定成本導入。

🎯 實務啟示

當一個系統需要頻繁重新訓練時，真正決定迭代速度的往往不是模型本身，而是「換一個模型需不需要重建訓練環境」。把 GPU 訓練整合進既有的資料治理與實驗追蹤流程，能讓工程團隊把精力放在該用哪個模型、怎麼訓練、新版本有沒有變好這些真正影響產品的問題上。

🔗 來源
- 標題：How FactSet cut model training and deployment from days to hours with Databricks AI Runtime
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/how-factset-cut-model-training-and-deployment-days-hours-databricks-ai-runtime

#Databricks #FactSet #FineTuning #MLOps #LLM #ServerlessGPU #MLflow #CompoundAI #RAG #FinTech
