---
title: Record, train, and deploy from one place with Strands Agents, LeRobot, and
  Hugging Face Storage Buckets
source: HuggingFace Blog
url: https://huggingface.co/blog/amazon/strands-lerobot-streaming-data-loop
model: claude-code/sonnet
generated_at: '2026-08-14T07:23:44.467588'
score: 95
---

📌 【AWS × Hugging Face】一條 Agent 迴圈搞定機器人的錄製、訓練與部署

TL;DR：Strands Robots 搭配 Hugging Face Storage Buckets，讓機器人資料從錄製到訓練部署共用同一套 LeRobot 格式，不必重複搬運。

如果你曾經寫過機器人資料蒐集流程，大概都遇過同一個麻煩：錄一次沒問題，但每天持續錄製、訓練、部署、再蒐集，就會開始為同樣的位元組付出重複代價，上傳的錄製檔愈長愈大，每次訓練都要把整個資料集複製到 GPU 才能開始，新的 checkpoint 出去、下一批錄製又回來。AWS 與 Hugging Face 這篇文章示範了如何用一個 Agent 迴圈，把這條路徑打通成一條真正可以「跑一整天」的管線。

🤔 **問題不在錄製，而在重複搬運**

這篇文章是 Strands Robots 系列的第二篇。第一篇介紹了 Strands Robots：一套由 AWS 開源（Apache 2.0 授權）的 SDK，把機器人抽象、模擬環境與 LeRobot 技術堆疊，包裝成可以組合進單一 Strands Agent 的 AgentTools，涵蓋 Robot() 工廠函式、在模擬環境中錄製示範動作、執行策略，以及把同一份 Agent 程式碼部署到實體 SO-101 機器人。Robot() 工廠會依名稱比對一份涵蓋機械臂、人形機器人、移動底盤與機械手的登錄表，文中示範用的 SO-100 只是其中支援的一種形態。

第一篇文章走的是單向路徑：從 Hub 資料集到實體機器人。這一篇則反過來，追蹤資料從第一個錄製畫格，回流到部署好的策略的完整迴圈。

🧩 **四個階段共用同一套後端**

整條迴圈的核心是 Hugging Face Storage Buckets：一種可變、不具版本控制、以 Xet 為底層的物件儲存儲存庫類型（2026 年 3 月發布），與資料集儲存庫並列在同一個 hf:// 命名空間下，直接沿用既有的 hf CLI 工具。錄製、同步、訓練、部署四個階段共用同一個後端：

- Robot("so100") 透過共用的 DatasetRecorder 錄製一份 LeRobotDataset。
- sync_dataset_to_bucket(...) 把資料集同步進 Storage Bucket，每次同步只上傳有變動的位元組。
- stream_dataset(...) 直接從 Hub 邊讀邊解碼相機影片串流回來訓練，不需要完整下載資料集。
- 訓練完的 checkpoint 只要改一個關鍵字參數，就能部署回同一個 Robot()，在硬體上錄下的新示範動作也回流到同一個 bucket。

整段流程用文章附的範例程式碼可以濃縮成幾行：建立 Robot("so100")、組成 Agent，用自然語言請 Agent 錄製一段示範並同步到 bucket，接著用 stream_dataset(...).dataloader(batch_size=64) 直接串流訓練，全程不需要先把資料集下載到本機。文中提到，LeRobot 的資料集格式目前已被 Hub 上超過 9 萬個資料集與模型使用，來自超過 8,000 位發佈者（依 LeRobot Project Pulse 統計），因此用 Strands Robots 錄製的資料集不需要額外轉換，任何原本就支援讀取 LeRobot 資料的工具都能直接使用。

⚙️ **怎麼跑起來**

最小可行路徑（預設模擬環境）需要 Python 3.12 以上、Linux 或 macOS（Apple Silicon 支援 MuJoCo 後端）、一個 Strands 相容的模型供應商（Amazon Bedrock、Anthropic API、OpenAI 或本機 Ollama），以及安裝指令 `uv pip install -U "strands-robots[sim-mujoco,lerobot]>=0.5.1"`，其中 lerobot extra 會一併帶入 LeRobot（>=0.6.1）、datasets、av 與 torchcodec，讓錄製與影片解碼不需額外設定。

若要進一步串接 Storage Buckets、實體硬體或真正的策略訓練，則需要 Hugging Face 帳號與具備寫入權限的 token、hf CLI（`pip install -U "huggingface-hub>=1.6.0,<2.0.0"` 後執行 `hf auth login`）、實體 SO-101 leader/follower 一對機器人（或其他 LeRobot 支援的機器人）搭配校正檔案、本機 VLA 推論用的 NVIDIA GPU，以及訓練時需要的 `uv pip install "lerobot[training]"`。

⚠️ **預設路徑跑得動，但不代表有用**

文章特別提醒：預設模擬路徑用的是 mock policy，能錄出一份「有效」的資料集，但不是一份「有用」的資料集；若沒安裝 lerobot[training]，呼叫 trainer.train() 會直接回傳錯誤結果，而非真正的 checkpoint。也就是說，這篇文章展示的是完整迴圈的骨架，實際要訓練出可用策略，仍需要接上真正的訓練環境與 GPU 資源。

🎯 **實務啟示**

對於正在建置機器人資料蒐集與訓練管線的工程師，這套架構的價值在於「一份格式走到底」：錄製、儲存、串流訓練、部署共用同一份 on-disk LeRobot 格式，省去反覆轉換與重複搬運整個資料集的成本。如果你的機器人專案已經在用 LeRobot 生態，Storage Buckets 提供的「只同步變動位元組」與「邊讀邊訓練不必整包下載」，值得評估是否能省下持續蒐集資料時的頻寬與時間成本。

🔗 **來源**
- 標題：Record, train, and deploy from one place with Strands Agents, LeRobot, and Hugging Face Storage Buckets
- 作者／機構：Sundar Raghavan、Steven Palma、Cagatay Cali、AWS Arron、Yin Song（AWS）／Hugging Face Blog
- 連結：https://huggingface.co/blog/amazon/strands-lerobot-streaming-data-loop

#RoboticsAI #LeRobot #HuggingFace #AWS #AgenticAI #OpenSource #MachineLearning #EdgeAI #DataPipeline #StrandsAgents
