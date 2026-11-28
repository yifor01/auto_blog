---
title: Inside the AI Training Data Market — Gabe Greenberg, G2i
source: Latent Space
url: https://latent.space/p/inside_the_ai_training_data_market_gabe_greenberg_g2i/
model: claude-code/sonnet
generated_at: '2026-11-28T00:43:20.293771'
score: 77
---

📌 訓練資料怎麼標價？G2i 創辦人揭露 Lab 採購內幕

TL;DR：G2i 創辦人揭露 frontier lab 怎麼買訓練資料與 RL 環境，獨家授權比共享資料貴上一截。

你以為把模型變強只靠更多算力、更多網路爬蟲文字？事實上，各大 lab 現在花大錢採購的是「人類專家精心設計的任務」，背後是一整條你我都不太熟悉的採購鏈。在 AI Engineer CODE 現場，G2i 創辦人 Gabe Greenberg 向 swyx 拆解了這個市場的運作方式。

🤔 從人工標註到專家工程設計

Gabe 描述 G2i 的業務演進：從早期替 lab 提供人工標註（human labels），逐步走向由資深工程師親自設計訓練任務的「專家工程」模式。這個轉變反映出 lab 對資料品質的要求越來越接近真實工程工作，而不只是簡單的對錯標註。G2i 本身就是靠「資深工程師」組成團隊，專門打造訓練資料與 reinforcement learning（強化學習）環境。

🧩 一筆好的訓練任務，要剛好超出模型現有能力

Gabe 提到一個核心原則：好的訓練任務難度應該「剛好在模型目前能力的前緣」，太簡單沒有訓練價值，太難則無法有效評分。圍繞這個原則，實際流程包含三個要素：

- Task（任務）：由資深工程師設計，難度要卡在模型能力邊界附近
- Seed data（起始資料）：挑選適當的初始資料作為任務的輸入基礎
- Verifier（驗證器）：建立能夠為模型輸出結果打分的機制

節目中也談到 G2i 如何篩選工程師以勝任這類 agentic（代理式）工作的任務設計，顯示這不是隨便找人標註就能完成的工作，而需要具備實際工程判斷力的人才。

💡 獨家 vs 共享：lab 怎麼決定付多少錢

訪談點出一個關鍵的採購邏輯：frontier lab 可以選擇付更高價格換取資料的「排他性」（該資料只有自己能用），或是接受折扣價購買其他 lab 也能買到的共享資料。Gabe 也談到小規模的 pilot 訂單如何逐步演變成更大型的長期合作關係，以及在什麼情況下，lab 會判斷乾脆自建內部資料團隊，而不是持續外包。此外，節目也涉及 lab 如何編列預算與定價訓練資料，以及「原始公司資料」（raw company data）本身形成的另一塊市場。

🎯 實務啟示

對資深工程師而言，這揭露了一條過去不太顯眼的職涯/收入路徑：設計訓練任務、挑選種子資料、打造 verifier，本質上是把工程判斷力轉化成可被 lab 採購的資產。對關注模型能力演進的人來說，理解這條採購鏈，也有助於理解「模型能力邊界」實際上是怎麼被一筆一筆訓練任務推著往前走的。

🔗 來源
- 標題：Inside the AI Training Data Market — Gabe Greenberg, G2i
- 作者／機構：Latent Space
- 連結：https://latent.space/p/inside_the_ai_training_data_market_gabe_greenberg_g2i/

#AI #TrainingData #LLM #ReinforcementLearning #AIEngineering #MachineLearning #DataMarket #AIStartups #RLHF #FrontierModels
