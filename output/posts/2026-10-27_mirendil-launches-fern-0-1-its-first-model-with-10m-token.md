---
title: Mirendil Launches Fern 0.1, Its First Model, With 10M-Token Context
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/27/mirendil-fern-10m-token-context-model/
model: claude-code/sonnet
generated_at: '2026-10-27T21:32:06.117912'
score: 96
---

📌 一人、3.5 個月、不到千萬美元:Mirendil 推出千萬 token 編碼模型 Fern

TL;DR:新創 Mirendil 發表首款模型 Fern,context window 衝上 1000 萬 token,專攻 AI R&D 場景的長文本程式碼理解。

把一整個 Megatron-LM 規模的程式碼庫,一次塞進模型的 context 視窗裡,會發生什麼事?這正是新創實驗室 Mirendil 想回答的問題。

🤔 **不是通用聊天模型,是給 AI R&D 用的工具**

Mirendil 是一家 AI 研發實驗室,剛發布旗下第一個模型 Fern 0.1。根據官方說明,Fern 的 context window 最高可達 1000 萬 token,換算約 23 MB 的程式碼,相當於 50 萬行,規模比得上 Megatron-LM 這種等級的程式碼庫。Mirendil 強調 Fern 不是拿來聊天的通用模型,而是瞄準 AI R&D 工作,列出 6 種目標用途(具體內容官方未展開細節)。對開發者來說,實際意義是可以一次載入整個 repo、一份完整的訓練紀錄,或是連續好幾天的 agent 執行軌跡。

🧩 **一位研究者、PyTorch 加 JAX,從零寫起**

Fern 建立在 Mirendil-Base 之上,經過一輪短期 post-training 而成。根據 Mirendil 的說法,Mirendil-Base 是由一位研究者在 3.5 個月內完成預訓練,總運算成本(含實驗、agent token 花費與資料處理)低於 1000 萬美元。過程中超過 99% 的程式碼由 AI agent 撰寫,研究者的角色是決定要嘗試什麼、何時介入。訓練資料只來自公開來源,包括 GitHub、公開程式碼、網頁與公開資料集;Mirendil 表示沒有使用蒸餾(distillation)、合成資料或授權資料,整套程式碼在 PyTorch 與 JAX 上從零寫成。

Fern 是 Mirendil 規劃中 3 款模型裡最小的一個。參數規模 0.5 到 2T 的 Mirendil-Base-Large,預訓練進度已超過 80%;2 到 10T 參數的 Mirendil-Base-XL 則剛過 20%。

📊 **長 context 的曲線撐住了,但等長比較未必佔優**

Mirendil 用自家 repository 串接成 42.9 MB 的資料流,做 next-token prediction 測試,以 bits per byte 衡量 cross-entropy(數字越低越好),視窗大小以 byte 而非 token 計算:

| Context 視窗 | Fern cross-entropy (bits/byte) |
|---|---|
| 32K bytes | 0.246 |
| 16M bytes | 0.155 |
| 23M bytes | 0.155 |

對照組模型只測到約 100 萬 token(它們官方宣稱的上限)。在 100 萬 byte 視窗下,Kimi-K3 拿到 0.140,Fern 是 0.165——也就是在相同長度下,Fern 並非最準的預測者,它的優勢在於曲線能一路延伸到其他模型停下來的地方之後。

在長文本標準測試 RULER 上,Mirendil 針對尚未經過 post-training 的 Mirendil-Base 跑了 5 項任務(greedy decoding、關閉 thinking、精確字串比對)。檢索類任務表現穩定,但多跳推理(multi-hop reasoning)在 1000 萬 token 時掉到 45%;需要留意的是,1000 萬 token 那一格只用了 20 個範例,其他長度用的是 100 個。Mirendil 表示更完整的長 context 結果會陸續公布。

在與其他開源與前沿模型的對比中,Fern 0.1 在 5 項測試中的 4 項勝過 Inkling 與 Nemotron 3 Ultra;在 SWE-Pro v2 Hard 上與 Beam 打平,同為 76.5 分;但在 SWE-Bench Verified 上落後 Beam,73.4 分對 81.6 分。表中列出的每一個前沿與大型開源模型,整體排名都領先 Fern。

💡 **數字要帶著一個但書看**

上述對比數據來自 Mirendil 自家公告圖表,其他模型的分數部分取自 model card、leaderboard 或 Mirendil 自己跑的結果,屬於自我報告性質,尚未見到第三方覆核。

⚠️ **長不代表強,多跳推理是明顯弱點**

Fern 在等長比較下輸給 Kimi-K3,多跳推理隨 context 拉長明顯退化,而且在程式碼相關 benchmark 上全面落後表中列出的前沿模型與大型開源模型。它的賣點是「能撐到別人撐不住的長度」,不是「同等長度下最準」。

🎯 **實務啟示**

如果工作流程本身就需要一次處理超長的 repo、訓練日誌或 agent 軌跡,Fern 這類超長 context 模型值得納入評估;但若任務落在百萬 token 以內,目前數據顯示傳統前沿模型在準確度與下游任務上仍有優勢,超長 context 更適合當作互補工具而非直接取代。

🔗 **來源**
- 標題:Mirendil Launches Fern 0.1, Its First Model, With 10M-Token Context
- 作者/機構:Michal Sutter, MarkTechPost
- 連結:https://www.marktechpost.com/2026/10/27/mirendil-fern-10m-token-context-model/

#Mirendil #Fern #LongContext #LLM #CodingModel #AIResearch #OpenPretraining #PyTorch #JAX #RULER
