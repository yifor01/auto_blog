---
title: 'NVIDIA Researchers Introduce Physis-Lang: Self-Evolving Physical Language
  That Lifts Cosmos 3 Past Veo 3.1 on Physics Benchmarks'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/30/nvidia-researchers-introduce-physis-lang-self-evolving-physical-language-that-lifts-cosmos-3-past-veo-3-1-on-physics-benchmarks/
model: claude-code/sonnet
generated_at: '2026-09-30T21:36:45.301678'
score: 102
---

📌 【NVIDIA／MIT／牛津研究】讓影片模型懂物理，靠的是改寫字幕

TL;DR：用「物理語言」重寫影片字幕，讓Cosmos 3在物理基準上反超Google Veo 3.1。

影片世界模型畫面越來越逼真，卻常常違反物理常識：奶油像油漆一樣攤開，球會直接穿牆而過。NVIDIA聯合MIT與牛津大學的研究團隊提出一個反直覺的修法：不加額外的視覺、latent或數值訊號，只靠重寫文字描述本身，就能讓模型學會物理。

🤔 **傳統字幕只說「發生了什麼」，沒說「為什麼」**

一般影片字幕像是「溫度升高，奶油融化了」，只描述現象，沒有解釋背後的熱傳導或重力等物理機制。研究團隊提出的框架Physis-Lang，把「物理語言」當成一個可被最佳化的共享表示，同一段文字同時驅動資料整理、模型訓練與推論三個階段。

🧩 **在字幕裡加一個physics_reasoning欄位**

Physis-Lang在每則基礎字幕上新增physics_reasoning欄位，寫明場景中的實體、成因、交互作用、支配原理、時間演變與結果。它同時會生成場景專屬的physics_negative_prompt，描述可能出現的不合理結果（例如石頭浮在水面上），在推論階段作為負向條件輸入。

整套系統採用自我演化迴圈：負責寫字幕的GPT-5.5模型本身保持凍結，演化的只有它的指令prompt。流程先在一個固定的20支影片開發集（含273條人工驗證的斷言）上生成字幕，由Gemini-3.1-Pro擔任具物理意識的評判者，從兩個維度評分；演化代理（evolution agent）再根據分數與逐條斷言的失敗情況重寫prompt。每次修改後的prompt都會在新建的PhysCapBench基準（246支影片、3,794條人工驗證斷言）上驗證效果。

演化過程並非一路順利：字幕F1分數從第1輪的78.64一路提升到第9輪的87.82，但第2輪一度因字幕過度謹慎而跌到76.28；第9輪則要求涵蓋每個可見的因果步驟，並把取樣幀率從2fps提高到4fps。

此外，系統還有一個GPT-5.5診斷代理，負責把生成影片的失敗案例對應到剛體運動、碰撞、流體力學等物理類別，再用這份「缺陷畫像」去比對大型影片庫中的物理標籤進行檢索，檢索鎖定的是物理內容而非畫面外觀相似度。最終訓練集包含18.3萬支影片：7.1萬支來自WISA-80K篩選、11.2萬支來自檢索。摘要指出，光是檢索這一步就在3個基準上平均提升3.01分，在VideoPhy-2上，化學與熱力過程兩項各提升8.00分。

模型微調採用LoRA，只調整attention投影層，不更動架構或訓練目標。

📊 **跨骨幹模型的提升幅度**

| Backbone | 提升幅度 |
|---|---|
| Wan2.1-14B | +7.05 |
| Cosmos3-Edge-4B | +3.24 |
| Cosmos3-Nano-16B | +6.22 |
| Cosmos3-Super-64B | +5.02 |

在Physics-IQ Verified排行榜（2026年9月29日快照）上，搭載Physis-Lang的Cosmos3-Super排名第一，得分48.2±1.4；Cosmos3-Nano版本排名第二，得分43.3±1.5。整體畫質指標VBench-I2V則維持穩定，Cosmos3-Nano從88.32小幅提升到88.69，顯示物理能力的提升沒有犧牲畫面品質。研究也發現光靠prompt本身就有效：加上物理推理與負向prompt後，一個完全凍結的Cosmos3-Nano在PhyGenBench上的分數從61.67提升到67.29。

💡 **把GPT pipeline蒸餾成兩個小模型，成本砍到兩百分之一**

研究團隊把原本依賴GPT-5.5與Gemini-3.1-Pro的pipeline，蒸餾成兩個Qwen3-VL-4B-Instruct模型：負責寫字幕的PhysThinker-C，以及負責prompt upsampling的PhysThinker-U。在Wan2.1-14B上，原本的商用pipeline帶來+7.05分的提升，但API成本約2.412萬美元；換成PhysThinker-C後，提升幅度維持在+6.76，成本降到約120美元；完全本地部署成本降為0，仍能帶來+4.76的提升。

⚠️ **數據來源與比較基準**

文中所有分數皆取自Physis-Lang論文的Table 1至4，各基準在統一協議下執行（PhyGenBench與VideoPhy-2使用GPT-5.5作為評分者），Physis-Lang相關數字均以Cosmos3-Nano骨幹為準，發布狀態檢查日期為2026年9月30日。

🎯 **實務啟示**

對於做影片生成或world model的團隊，這項研究說明了一個容易被忽略的槓桿：與其堆疊額外的視覺或數值監督訊號，先把字幕的「推理密度」拉高，可能是提升物理一致性最划算的路徑；而蒸餾成本的巨幅下降，也讓中小團隊有機會直接複用這套字幕管線而不必負擔龐大的API開銷。

🔗 **來源**
- 標題：NVIDIA Researchers Introduce Physis-Lang: Self-Evolving Physical Language That Lifts Cosmos 3 Past Veo 3.1 on Physics Benchmarks
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/30/nvidia-researchers-introduce-physis-lang-self-evolving-physical-language-that-lifts-cosmos-3-past-veo-3-1-on-physics-benchmarks/

#NVIDIA #VideoGeneration #WorldModel #PhysicsAI #Cosmos #LoRA #SelfEvolving #MIT #Oxford #GenerativeVideo
