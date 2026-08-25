---
title: Build an End-to-End Data Science Project with Grok Build and Grok 4.6
source: KDnuggets
url: https://www.kdnuggets.com/build-an-end-to-end-data-science-project-with-grok-build-and-grok-4-6
model: claude-code/sonnet
generated_at: '2026-08-25T06:31:54.982759'
score: 80
---

📌 用四句 Prompt，讓 Grok Build 端到端做完一個資料科學專案

TL;DR：實測 xAI 新款終端機代理 Grok Build，四個 prompt 走完 EDA、建模、API 化到雲端部署全流程。

如果一個資料科學專案從探索性分析到上線部署，只需要打四句話，會發生什麼事？作者用 xAI 最新的 Grok 4.6 搭配終端機代理工具 Grok Build，實際跑了一遍「預測咖啡店顧客等待時間」的完整專案，記錄下每個環節的實際輸出。

🤔 **Grok Build 是什麼**

Grok Build 是 xAI 自家開發的終端機 coding agent 與 TUI（terminal user interface），設計理念是讓開發者直接在終端機中使用 xAI 的模型，而非依賴第三方介面。它能理解專案結構、建立與編輯檔案、執行指令、搜尋網路，並處理較長時間的任務；同時支援互動式全螢幕操作，也能以無介面（headless）模式跑腳本與自動化。目前 Grok Build 提供 Windows、macOS、Linux、WSL 的預編譯版本，安裝方式為在終端機執行 `curl -fsSL https://x.ai/cli/install.sh | bash`（Windows PowerShell 則用對應的 install.ps1 指令）。根據 xAI 的評測，Grok 4.6 在 Artificial Analysis Intelligence Index 上達到與 GPT-5.6 Sol 相當的水準，且該模型直接驅動 Grok Build 本身。

🧩 **四句 Prompt 走完整條流程**

作者建立空白資料夾 `coffee-wait-time-project` 後啟動 `grok`，依序下達四個指令：

1. 產生 3,000 筆模擬咖啡店訂單資料，存成 CSV，執行資料清理與探索性分析，並輸出視覺化圖表。
2. 用 scikit-learn 建立可重複使用的前處理 pipeline，訓練 Linear Regression、Random Forest、Gradient Boosting 三種模型，比較 MAE、RMSE、R²，並將最佳 pipeline 存成 joblib 檔。
3. 用 FastAPI 建立包含根目錄、健康檢查、預測三個端點的應用程式，以 Pydantic 驗證輸入，回傳預測等待時間與簡短說明。
4. 準備部署到 FastAPI Cloud，確認本地開發模式可運作、執行 `fastapi deploy`，並測試上線後的各個端點。

📊 **結果：Gradient Boosting 勝出，MAE 降到 1.1 分鐘**

清理後的資料集剩下 2,986 筆（移除遺失值與 14 筆極端離群值）。初步分析顯示平均等待時間約 10.5 分鐘，尖峰時段會多出約 3.3 分鐘，而店員人力負載與等待時間的相關係數高達 0.68，是最強的關聯因子。第一版 baseline 用 Random Forest 建模，MAE 為 1.63 分鐘、R² 為 0.85。

進入正式訓練階段後，在 598 筆保留測試集上比較三個模型，Gradient Boosting 表現最佳：MAE 1.101、RMSE 1.408、R² 0.934；Linear Regression 次之，Random Forest 排第三。作者提到在訓練過程中一度用完免費額度，升級方案後輸入「continue」，Grok Build 便從中斷處接續完成。

最終部署到 FastAPI Cloud 後，作者用 curl 測試線上 `/predict` 端點，傳入含 8 點、Latte、中杯、排隊 5 人、2 位店員、雨天等條件的訂單，API 回傳：

```
{
  "predicted_wait_time_minutes": 13.06,
  "explanation": "Estimated wait time is about 13.1 minutes, mainly due to a moderate queue (5 people), rush-hour timing.",
  "model_name": "Gradient Boosting",
  "model_metrics": {"MAE": 1.101, "RMSE": 1.408, "R2": 0.934}
}
```

確認整條從資料清理、模型訓練、pipeline 序列化到線上推論的流程都正確運作。

⚠️ **值得留意的限制**

整個過程中，作者需要在關鍵節點親自檢查與介入，例如中途升級付費方案、確認 API 測試結果、以及部署時的瀏覽器登入驗證。這仍是一個由人主導方向、AI 執行細節的協作流程，而非完全自動化的黑箱。

🎯 **實務啟示**

對工程師而言，這個案例展示了終端機代理型工具在資料科學工作流中的可行性：從 EDA 到雲端部署的重複性工作，可以透過清楚分階段的 prompt 交給代理處理，人力則專注在審查中間產出（如模型指標、API 回應格式）與關鍵決策點。這種模式特別適合原型驗證與教學示範場景。

🔗 **來源**
- 標題：Build an End-to-End Data Science Project with Grok Build and Grok 4.6
- 作者／機構：Abid Ali Awan, KDnuggets
- 連結：https://www.kdnuggets.com/build-an-end-to-end-data-science-project-with-grok-build-and-grok-4-6

#GrokBuild #xAI #Grok4 #DataScience #MachineLearning #FastAPI #ScikitLearn #MLOps #AIAgent #CodingAgent
