---
title: The Enterprise Case for Open-Weight Models on Databricks
source: Databricks
url: https://www.databricks.com/blog/enterprise-case-open-weight-models-databricks
model: claude-code/sonnet
generated_at: '2026-11-04T22:58:29.294009'
score: 82
---

📌 標題：企業模型組合從 4.2 檔增至 7.1 檔，為何開始擁抱開源權重模型

TL;DR：Databricks 揭露企業為何從單一前沿模型供應商轉向開源權重模型組合，兼顧成本與治理彈性。

過去兩年,企業普遍把 AI 架構押在單一前沿模型供應商身上，但 Databricks 內部資料顯示，光是今年一月到七月，客戶平均使用的模型數量就從 4.2 檔跳升到 7.1 檔，其中近四成是開源權重模型。這背後,是七個讓企業重新評估策略的壓力點。

🤔 **為何單一供應商策略開始鬆動**

Databricks 的現場工程師團隊觀察到,企業重新評估單一前沿模型策略，原因包括:AI 支出的投資回報率不如預期;自 2023 年以來，模型效能排名已經換手超過 20 次，綁定單一供應商的架構難以隨時切換到效能更好的模型;前沿模型的安全防護機制有時會擋下合法工作，例如 Hugging Face 事件中，回應團隊想分析真實的攻擊紀錄與攻擊 payload，前沿模型拒絕處理，最後改用開源權重模型 GLM 5.2 完成分析;部分供應商的資料保留政策也在改變，例如 Anthropic 前沿層級引入 30 天最低保留期，這對原本以「prompt 與 completion 絕不留存」為合規基礎的企業而言，可能需要調整系統;企業也越來越要求對模型治理有完整的可視性與控制權，包括可查詢的輸入輸出紀錄與錯誤紀錄;harness（提示詞、工具、控制流程的整套 scaffolding）本身也會改變效能表現，Databricks 的內部基準測試顯示，同一個模型在不同 harness 下分別拿到 61.7%、48.1%，裸跑則只有 38.4%，代表評測必須同時測試模型與 harness 的組合;最後，也是最關鍵的轉折，頂尖開源權重模型的效能已經追上頂尖前沿模型，但成本更低，這在十八個月前還做不到。

🧩 **Unity Gateway：讓模型可以換，但治理不能鬆**

面對這些壓力，企業想做到三件事:在不犧牲生產力的前提下控制成本、保留操作自由度、確保能快速導入新模型。Databricks 的做法是透過 Unity Gateway，用統一 API 同時服務開源權重與前沿模型，並提供集中式治理控制，讓團隊能透過設定或智慧路由切換模型，而不必改程式碼或額外包一層抽象層。Omnigent 則把這種彈性延伸到 harness 層，讓團隊換模型或換 agent 執行環境時，不必重建整個工作流程。

📊 **GLM 5.2 上線一個月，就吃下近四成開源 token 用量**

GLM 5.2 在七月中上線後,Unity Gateway 上的開源權重模型用量明顯上升，而既有客戶的整體 AI 流量成長幅度大致持平，意味著這些成長主要來自既有客戶把更多流量轉向開源權重模型。上線僅一個月，GLM 5.2 已佔 Unity Gateway 開源 token 用量的約四成，且多為新增流量。獨立評測機構 Artificial Analysis 的數據顯示，GLM 5.3（max）在 Databricks 上的端到端回應時間（含輸入處理、推理與生成）為 9.1 秒，與一線代管端點相比具競爭力。GLM 5.3 與 Kimi K3 的基準表現，也讓客戶在 GLM 5.2 之外多了可評估的開源選項。

💡 **三十億美元募資背後的 GPU 算盤**

為了支撐這股需求，Databricks 七月宣布完成 30 億美元募資。CEO Ali Ghodsi 向 CNBC 表示，這筆資金有一部分正是為了確保 GPU 產能，用於代管開源模型:「我們在日本、韓國、美國、印度到處都缺 GPU…所以我們需要募到足夠的資金拿到更多 GPU」。

⚠️ **前沿模型沒有被取代，只是不再是唯一選項**

文中也強調，沒有單一模型或供應商能在品質、成本與政策適配性上同時領先所有工作負載，前沿模型在某些場景仍有優勢。企業需要的不是「換掉前沿模型」，而是一套能讓模型組合隨時調整、同時維持治理一致性的架構。

🎯 **實務啟示**

如果你的團隊目前把整套 agent 或應用綁在單一模型供應商的 API 上，這篇文章提醒的重點是:評測時務必連 harness 一起測，而不是只比較模型裸跑分數;同時，透過閘道層（像 Unity Gateway 這類設計）統一管理路由、權限與稽核，才能在模型排名持續變動的情況下，低成本地把流量導向當下 ROI 最高的模型，而不必每次都重寫程式碼。

🔗 **來源**
- 標題：The Enterprise Case for Open-Weight Models on Databricks
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/enterprise-case-open-weight-models-databricks

#OpenWeightModels #Databricks #LLM #AIInfrastructure #ModelGovernance #GLM #EnterpriseAI #UnityCatalog #AICost #MachineLearning
