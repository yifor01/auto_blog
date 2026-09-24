---
title: How to train your own Jev for $17
source: Together AI
url: https://www.together.ai/blog/how-to-train-your-own-jev
model: claude-code/sonnet
generated_at: '2026-09-24T20:44:52.846757'
score: 89
---

📌 訓練一個屬於自己的分類模型，只要 17 美元

TL;DR：Together AI 公開教學，教你用 Qwen3.5 4B 微調出 Jev 風格分類模型，訓練成本約 17 美元且可全程復現。

Jev 最近在 AI 圈引起不少討論——一個又快又便宜的分類模型，丟給它一段狀態加上預先定義的問題，它就能回傳分數、布林值或選擇題答案。Together AI 這篇文章沒有停在討論熱度上，而是直接示範怎麼自己動手做一個，並附上完整的指令與成本明細。

🤔 解決什麼問題

文章指出，這類「輸入狀態 + 問題 → 結構化答案」的分類模型有大量實際用途：電商平臺評估自動退貨申請、將 ML 論文分類、或是為一段文字打情感分數。Together AI 以此為出發點，在自家 serverless 平臺上發布了 together/Tev1-4B-experimental，並以此篇文章示範如何從頭微調出等效模型。

🧩 核心架構：用 Qwen3.5 4B 打底

模型底座是 Qwen3.5 4B，訓練資料則從 Hugging Face 上取樣了約 37,840 筆範例，涵蓋八個不同任務類型：

| 資料來源 | 任務類型 | 訓練筆數 |
|---|---|---|
| MultiNLI | 支持／反駁／中立 | 5,000 |
| BoolQ | 依段落回答是／否 | 3,000 |
| Banking77 | 選擇銀行業務意圖 | 3,000 |
| AG News | 新聞分類 | 1,500 |
| SST-5 | 情感等級 | 2,000 |
| Programmatic policies | 套用規則 | 13,500 |
| Routing | 路由決策 | 6,000 |
| Research taxonomy | 論文分類 | 3,840 |

文章特別強調，把資料量控制在這個規模，是為了讓整個微調成本壓在 17 美元左右；用更大的資料集雖然可能更準，但成本與訓練時間都會明顯上升。

🛠️ 怎麼用：從 clone 到部署

整個流程分成幾個步驟，Together AI 把每一步都寫成了可直接執行的指令：

1. Clone 專案並安裝依賴：`git clone https://github.com/togethercomputer/tev1`，接著 `uv sync --locked`。
2. 設定環境變數：複製 `.env.example` 為 `.env`，填入 `TOGETHER_API_KEY`（`JEV_MODEL` 先留空）。
3. 下載並正規化資料：依序執行 `uv run python fetch_sources.py` 與 `uv run python build_all.py`，把八個資料源統一成同樣的 JSON 格式。
4. 啟動微調：執行 `uv run --with together --env-file .env python examples/train_together.py --launch`，腳本會自動上傳訓練資料並在 Together AI Fine-tuning 服務上啟動任務，過程約需 25 分鐘，也可用 `tg fine-tuning retrieve` 查詢狀態。
5. 部署成端點：取得 `model_output_name` 後，用 `tg endpoints create` 搭配 `1x_nvidia_h100_80gb_sxm` 硬體建立專屬端點，再把端點名稱寫回 `.env` 的 `JEV_MODEL`。

模型接受的輸入格式是結構化 JSON，包含 `state`（狀態描述）、`question`（問題）與 `options`（選項清單，每個選項有 label、key、description）。文章舉的範例是客服意圖分類：給模型一段「同一筆訂閱被重複扣款」的客戶留言，讓它從四個候選意圖中選出最匹配的一項。

⚠️ 適用場景與限制

這套流程的定位很清楚：不是要做出一個通用對話模型，而是針對「狀態 + 固定問題集 → 結構化答案」這類任務做輕量化微調。若不想自己訓練，Together AI 也提供已經部署好的 together/Tev1-4B-experimental 可直接呼叫。

🎯 實務啟示

對於需要大量重複性分類判斷（客服分流、內容審核、路由決策）的團隊，這篇教學提供了一條成本可控、步驟透明的路徑：不必依賴大型通用模型做這類任務，一個 4B 規模、針對性微調的分類器可能就足夠快、也足夠便宜。文中提供的資料混合比例，也是規劃自有分類任務資料集時值得參考的起點。

🔗 來源
- 標題：How to train your own Jev for $17
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/how-to-train-your-own-jev

#TogetherAI #Qwen #FineTuning #Classification #LLM #OpenSource #MLOps #Jev #AIEngineering #MachineLearning
