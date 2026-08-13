---
title: '[AINews] SpaceXAI Grok 4.6 and Grok @Bot'
source: Latent Space
url: https://www.latent.space/p/ainews-spacexai-grok-46-and-grok
model: claude-code/sonnet
generated_at: '2026-08-13T07:36:05.709681'
score: 87
---

📌 一天五款新模型齊發：Grok 4.6 靠效能稱王

TL;DR：xAI、阿里巴巴、DeepSeek、微軟、Upstage 同日推新模型，戰場是價格效能而非架構突破。

短短一兩天內，五家實驗室各自端出新模型，但真正讓工程師停下手邊工作的，往往不是哪個榜單分數最高，而是同樣的智慧程度，價格能砍到多低。

🤔 **AI 隊友之戰，也是新模型的舞臺**

今年反覆出現的主題之一，是 coding agent 正在往一般知識工作外溢，AI 隊友、多人協作、multi-agent 逐漸成為下一個 AI 戰場。在 Claude Tag 評價兩極、Block 的 Buzz 又偏技術門檻較高的情況下，市場仍有新龍頭出線的空間，而這次的主角是搭載 Grok 4.6 的新代理系統。Grok 4.6 被形容為「同價位下最大幅度的進步」，也被 Cognition 與 Elon Musk 本人承認是全球第二強的知識工作模型。

🧩 **Grok 4.6：更長的訓練、更聚焦的代理任務**

xAI 揭露的訓練細節指出，Grok 4.6（1.5T 模型）經歷了比 Grok 4.5 更長的補充訓練，使用經篩選的模型生成資料強化推理與進階技術概念，搭配高品質工程資料與改良過的最佳化器與訓練配方，打造出更強的基礎模型，再由 Grok 4.5 重新生成跨推理強度、agent harness 與 STEM、軟體工程、知識工作等領域的 SFT 軌跡，並以模型自動檢查濾除有問題的樣本。後續的 agentic RL 涵蓋一般編程、知識工作，以及核武級冷門任務如 kernel 最佳化、網頁開發、電腦輔助設計（CAD）等領域專屬環境。Elon Musk 也透露 Grok 4.7 已完成初步訓練，接下來會用 SpaceX 內部資料做補充訓練。

📊 **數據看板：61 分、88.4%、每百萬字元 2 美元**

- Artificial Analysis 將 Grok 4.6 的 Intelligence Index 評為 61 分，大致與 GPT-5.6 Sol Max 同level，落後 Claude Opus/Fable
- Terminal-Bench v2.1 達 88.4%，GDPval-AA v2 Elo 為 1753
- 定價每百萬 token 輸入 2 美元、輸出 6 美元，明顯低於同級競品
- 阿里巴巴的 Qwen3.8-Max 以開放權重釋出，總參數 2.4T、啟動參數 95B 的 MoE 架構，vLLM 當日就支援，並針對 NVIDIA B300 與 AMD MI355X 推出 4-bit 版本；但初版釋出僅支援文字，尚無視覺輸入能力
- DeepSeek V4 Pro 正式版定價約每百萬輸入 0.435 美元、輸出 0.87 美元，Cline 指出比 Fable 5 便宜約 57 倍，且 Terminal Bench 分數比預覽版提升 15.8%
- Upstage 的 Solar Pro 4 在 Intelligence Index 上從 14 分躍升到 42 分，agentic 與長上下文任務進步明顯，但整體仍落後前沿與開放模型的頂端
- 微軟則發布自研的 MAI-Thinking-1 推理模型，已上架 Foundry，團隊特別徵求工具使用（tool use）方面的回饋

💡 **價格戰多於架構戰**

把這些發布放在一起看，會發現一個共通點：多數團隊強調的是「同樣能力、更低價格」或「同架構、更長訓練」，而非全新的模型設計。DeepSeek V4 Pro 被部分早期使用者認為「不錯但未必勝過 Kimi 或 Flash」，暗示下一波突破可能更依賴 RL 環境與 agent 任務設計，而非單純堆參數規模。這種以效能/成本比拚代替架構創新的態勢，或許才是這波「前沿模型日」真正值得留意的訊號。

🎯 **給工程師的實務啟示**

如果你的工作負載是編程或抓 bug，Grok 4.6 的低價與代理任務表現值得納入評估；若預算優先，DeepSeek V4 Pro 的定價值得測試但要留意其在特定任務上未必贏過現有選項；若需要開放權重且要跑視覺任務，Qwen3.8-Max 目前還得等視覺版本釋出。

🔗 **來源**
- 標題：[AINews] SpaceXAI Grok 4.6 and Grok @Bot
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-spacexai-grok-46-and-grok

#Grok46 #xAI #Qwen38Max #DeepSeekV4 #MAIThinking1 #SolarPro4 #LLM #AIAgents #OpenWeightModels #AIpricing
