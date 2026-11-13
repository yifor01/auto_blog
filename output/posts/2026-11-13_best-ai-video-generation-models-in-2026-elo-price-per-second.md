---
title: 'Best AI Video Generation Models in 2026: Elo, Price per Second, Open Weights'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/13/best-ai-video-generation-models-2026/
model: claude-code/sonnet
generated_at: '2026-11-13T22:51:17.369991'
score: 85
---

📌 2026 AI 影片生成模型排行與定價全解析

TL;DR：以盲測 Elo、每秒 API 價格與開源狀態三個維度，整理當前 AI 影片生成模型的實際選型依據。

開源權重模型首次擠進影片生成榜單的前三名；而同一個 MiniMax H3 底座衍生出的多個 post-train 版本，有的只用五分之一的價格就打平甚至超越原版表現。

🤔 **一年內的變化與評分方式**

這份排行（截至 2026 年 11 月 13 日）觀察到的變化是：原生音訊已成為標配，影片長度拉長到 15 到 30 秒，而且首次有開源權重模型擠進前三名。評分來源是 Artificial Analysis Video Arena 的盲測人類偏好 Elo：每次投票由經驗證的評審比較同一個 prompt 產生的兩段 clip，排名依據是含音訊的 AA-Video-T2V v2.1 榜，並同時參考 AA-Video-I2V v2.1 的影像轉影片分數。Kling 3.0 1080p（Pro）在兩個榜上都被固定為 1000 Elo 作為錨點，低於 1000 代表評審更常選擇 Kling 3.0。價格則取各家 API 每分鐘報價（盡量統一到 1080p）除以 60 換算成每秒價格。多數前十名分數的信賴區間落在 ±13 到 ±15 Elo 之間，25 分以內的差距應視為統計上接近，排名第 3 到第 8 名更適合當作一個群組而非絕對順序。

📊 **各模型定位與報價**

- **Wan 3.0**（Alibaba，2026/8/24 上線）：文字轉影片榜首，背後有 7,651 票支持，可生成 30 秒 1080p 影片，支援以文字、PDF、投影片作為輸入，報價 $0.20/秒；沒有開放權重，Alibaba 上一個開源影片旗艦仍是 Wan 2.2；在影像轉影片榜上則掉到第 11 名。
- **Utopai X**（Utopai Studios）：兩個榜單都排進前兩名，是在 MiniMax H3 上 post-train 而成，表現超越原版 H3，但只能透過自家 PAI 平臺使用（每秒 93 credits，方案從 $15／1,000 credits 起），無法透過一般 API pipeline 呼叫。
- **MiniMax H3**：影片頂層中第一個開源權重模型，2026/7/31 推出 API、8/3 公開權重，是 33B 的 dense 單串流 Transformer，以 Qwen3-VL-32B 作為編碼器，輸出原生 32 kHz 立體聲音訊；Hugging Face 權重的授權附有地區排除限制，下載前需仔細閱讀。它已成為 2026 年影片模型的基礎層，Utopai X、HeyGen Video 1、fal 的 H3 Max、Pika H3 Flex 都是它的 post-train 版本。
- **Seedance 2.5**（ByteDance）：影像轉影片榜首，2026/7/31 起透過 Jimeng AI 與 Doubao Pro 推出，支援長達 30 秒的生成，並可接受最多 30 張圖片、10 段影片、10 段音訊作為參考；Artificial Analysis 列出的報價是 $34.12/分鐘（全榜最高），但 BytePlus 報價一段不含影片輸入的 5 秒 720p clip 為 $1.156（約 $0.23/秒），使用前需先確認所在地區的 API 存取權限。
- **Gemini Omni Flash 1.2**（Google）：2026/11/5 正式開放，新增 3 到 15 秒的片長，較 1.1 版降價 30%，影片輸出報價 $12／1M tokens，換算約 $0.070/秒（720p），在文字轉影片上比 1.1 版多拿下 27 Elo；從 2026/12/3 起，所有呼叫 1.1 的請求會自動導向 1.2。
- **FLUX 3 Max**（fal Research 與 Black Forest Labs 合作，2026/10/19 上線）：fal 表示一段 10 秒 720p 的 clip 約 12 秒內即可渲染完成，相較之下 Seedance 2.5 在 fal 自己的對照測試中要花 277.80 秒；它與 fal 的 H3 Max 共用同一套 API，切換模型只需更改 model ID。
- **HeyGen Video 1**：同樣是 MiniMax H3 的 post-train，但定位是通用場景生成器而非 avatar 引擎，在無聲（audio-off）文字轉影片榜上以 1146 Elo 居冠，報價 $0.04/秒，大約是原版 H3 的一半價格卻拿到接近的分數。
- **fal H3 Max**：fal Research 在開源的 MiniMax H3 基礎上 post-train 而成，專攻 prompt 服從度與畫質，fal 宣稱一段 5 秒 clip 約 3 秒即可渲染完成，2026 年 8 月上線後曾短暫拿下影像轉影片榜首,後被更新的 post-train 版本超越。
- **SkyReels V4**（2026 年 3 月）：雖然推出時間較早，仍在影像轉影片榜上排進前五，但 $0.35/秒的報價在文字轉影片場景下已難以與不到三分之一價格、分數更高的 Gemini Omni Flash 1.2 競爭。
- **FLUX 3**（Black Forest Labs）：BFL 的第一個影片模型，支援 20 秒片長與原生音訊，同一套 backbone 還能用於機器人動作預測；BFL 表示稍晚會釋出開放權重版本，在 FLUX 3 Dev 上市前仍只能透過 API 使用。
- **MiniMax H3 家族輕量化版本**：Pika H3 Flex（2026/10/29 上線）把 H3 壓縮到只需 6 個 sampling steps，但本地推理仍需要 H100 80GB 以及約 215GB 的下載量；Video Rebirth 的 HyperFlow H3 Flash 則把 H3 壓到 13.7B，以 9.1GB 的 GGUF 檔案就能在 24GB GPU 上執行，其姊妹版本 Hyperflow H3 在影像轉影片榜上排名第 7（1120 Elo）。
- **LTX-2.5**（Lightricks，2026/8/11 上線）：22B 模型，支援原生多鏡頭（multishot）生成與同步音訊，授權規定年營收超過 $1,000 萬美元的企業需取得付費授權；分數落後 H3 家族約 200 Elo，但由於是以營收而非地區作為授權門檻，對美歐團隊反而是個務實的預設選擇。
- **Apache 2.0 選項**：Wan 2.2 與 HunyuanVideo 1.5 仍是追求寬鬆授權或單張消費級 GPU 部署的首選，但兩者目前都未列在 Artificial Analysis 的現行榜單上。

💡 **品質與價格已經脫鉤**

目前最便宜的三個頂層模型，全都是 MiniMax H3 本身或它的衍生版本。如果用「(Elo − 1000) ÷ 每秒價格」粗略估算性價比（僅供參考，未考慮解析度與片長差異），可以看到 Wan 3.0 比 HeyGen Video 1 多拿到約 23 Elo，卻要付出 5 倍的每秒價格——值不值得，取決於實際使用中要丟棄重新生成多少次。

🎯 **實務啟示**

選型前先確認需求能否走 API pipeline，還是只能停留在像 Utopai X 這種封閉的 studio 工具；同一家公司在不同管道（如 Artificial Analysis 報價與 BytePlus 報價）之間的價格可能差距很大，下決策前務必自行核實；授權條件上，地區排除（如 MiniMax H3）與營收門檻（如 LTX-2.5）這類限制，往往比 Elo 分數更早決定一個模型能不能真正被你的團隊採用。

🔗 **來源**
- 標題：Best AI Video Generation Models in 2026: Elo, Price per Second, Open Weights
- 作者／機構：Michal Sutter（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/11/13/best-ai-video-generation-models-2026/

#AIVideo #TextToVideo #GenerativeAI #OpenWeights #MiniMax #Wan3 #Seedance #GeminiAPI #VideoGeneration #AIBenchmark
