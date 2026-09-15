---
title: Can Skills Learned in Games Transfer to Real-World Work?
source: Latent Space
url: https://www.latent.space/p/good-start-labs
model: claude-code/sonnet
generated_at: '2026-09-15T20:43:25.583073'
score: 80
---

📌 桌遊裡學到的策略，能搬進辦公室嗎？

TL;DR：Good Start Labs 訓練 AI 玩桌遊，發現「多輪貫徹策略」比單輪問答更容易遷移到真實工作任務。

一場 2025 年的 Twitch 直播,讓一群觀眾意外看到了不同前沿模型的性格差異：面對外交遊戲《Diplomacy》,OpenAI 的 o3 靠著策劃背叛贏得所有對局，而 Anthropic 的 Claude Opus 4 因為拒絕說謊而「被打得體無完膚」。這個畫面成了一整間新創公司的起點。

🤔 **從一場直播到一家公司**

當時任職於 Every 的 Alex Duffy 觀察到，不同模型在遊戲情境下會展現截然不同的行為模式，這讓他相信像 Diplomacy 這類「結果可驗證」的遊戲，能拿來訓練模型的策略思考能力。他後來與 Tyler Marques 一起，從 Every 獨立出 Good Start Labs，並取得 General Catalyst、Inovia、Every 與天使投資人共 360 萬美元的資金。Duffy 表示，強化學習環境是教會模型「任何可驗證事物」最可靠的方式之一。

🧩 **1830 鐵路遊戲：訓練設計才是關鍵變數**

Good Start Labs 最具代表性的實驗，是在十九世紀鐵路策略遊戲《1830: The Game of Railroads and Robber Barons》中訓練一個 30B 模型，再拿同一個模型去做金融研究任務。遊戲裡的股票交易機制，被設計成模擬真實金融工作流程：模型要在資料庫中尋找對局紀錄、整理進 Excel、進行推理並建立計算函式。

實驗比較了兩種訓練設計：單純被丟一個遊戲局面、要求給出下一步的「單輪問答」，以及能使用工具探索環境、規劃策略並即時調整的「多輪終端代理」。兩種設計都改善了各自在遊戲內的表現，但只有多輪終端代理的訓練方式，能同時提升模型在 Finance-Agent 基準上的表現。

💡 **Harness（訓練框架）比模型本身更重要**

Duffy 強調「你怎麼設計這個 harness，完全決定了模型能學到什麼」——用圖片呈現局面的模型，會學到跟讀純文字或用 Python 呈現局面不同的東西。這個理念也體現在他與 Marques 和多所大學研究者共同發表的論文《COS-PLAY》中：系統讓一個決策代理擁有可學習的「技能庫」來指導行動，另一個獨立的技能庫代理則負責研究對局軌跡並更新技能庫，再迴圈餵回下一輪訓練。

在比較新一代模型時，Duffy 提到新模型雖然普遍更擅長遊戲，但會在「背叛、合作、心智理論」等人格傾向上出現分歧；模型越強，完成同一任務所需的引導確實越少，但在「把環境當課程」的訓練哲學下，harness 反而變得更重要而非更不重要——例如 GPT-6 Astra 傾向減少思考鏈、直接跳到答案，這時候 harness 就是強迫模型用可信賴方式（例如寫程式而非心算）解題的工具。

Good Start Labs 目前主要販售兩類東西給前沿實驗室：一是代理玩遊戲產生的軌跡資料（觀察、決策、動作與結果），二是遊戲開發商客製的即時互動資料；所有賣給模型開發商的資料都會去除個人識別資訊。公司也在嘗試把各個遊戲專用的專家模型，統一成一個通用的「遊戲智慧」。

⚠️ **證據還在早期階段**

Duffy 自己也承認，目前最清楚的證據只支持「目標導向的執行力會遷移、推理能力會遷移」這件事，他舉出的具體案例僅有兩個：1830 遊戲遷移到金融任務，以及 Diplomacy 訓練意外產生更好的客服代理。至於這種遷移能力是否能更廣泛地類推到其他真實世界任務，目前尚無定論。

🎯 **實務啟示**

對於設計 RL 訓練環境或評估基準的工程師，這篇文章的重點在於：決定遷移效果的關鍵變數往往不是遊戲本身，而是訓練時「要求模型如何互動」——多輪、可使用工具、需要規劃調整的任務設計，比單輪問答更可能培養出可遷移的能力。

🔗 **來源**
- 標題：Can Skills Learned in Games Transfer to Real-World Work?
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/good-start-labs

#ReinforcementLearning #LLMTraining #AIAgents #GameAI #Diplomacy #AgenticAI #RLEnvironments #FrontierModels #AITraining #MachineLearning
