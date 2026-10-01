---
title: 'SCLATE: A Substrate for Continual-Learning Agent Training and Evaluation'
source: Apple ML
url: https://machinelearning.apple.com/research/sclate-agent-training-evaluation
model: claude-code/sonnet
generated_at: '2026-10-01T22:10:57.879277'
score: 80
---

📌 Apple 研究：連續學習 Agent 評測，為何每次都要重造排程輪子

TL;DR：SCLATE 讓 benchmark 與 agent 共用同一事件時鐘，評測框架不再各自為政。

一個能長期運作的 AI agent，不會只是「回答一個問題就結束」，它得在數週、數月的時間跨度裡，經歷 session 的停止與重啟、定時排程（cron）、記憶整併等事件。問題是，現有的 benchmark 與訓練框架通常只排程「benchmark 自己的事件」，agent 本身的生命週期事件完全沒有被納入考量，於是每換一組 benchmark 與 agent 配對，就得重新寫一套客製化的排程迴圈。Apple 這篇研究提出的 SCLATE，就是想解決這個基礎設施層級的痛點。

🤔 **核心問題：誰來統一排程 agent 與 benchmark 的事件**

連續學習（continual-learning）agent 是由模型、harness（執行框架）與記憶系統組成的複合系統，運作在長達數個 session 的時間軸上。評估與訓練這類 agent，需要把 benchmark 任務與 agent 自身的事件（session 開關、cron、記憶整併）交錯排程。但現況是，benchmark 與訓練框架各自只管自己的事件，agent 的事件被排除在外，導致每個 benchmark／agent 組合都得客製開發排程邏輯。

🧩 **方法與架構：一個開放的事件排程器 + 混合模擬時鐘**

SCLATE 是一個執行基礎設施（execution substrate），benchmark 與未經修改的 agent 都能透過一個 adapter，把各自的事件加入同一個開放的事件排程器。其核心是一個「混合模擬時鐘」：當 agent 正在運作時，時鐘以真實時間流動；遇到空閒間隔則直接跳過，藉此把一個月長的情境壓縮進數小時內完成。

同時，SCLATE 也扮演 rollout 引擎的角色：它能在不修改 agent 的 harness 與記憶系統的情況下直接執行，並透過容器內的 proxy，記錄每一次模型呼叫的 token 與 log probability。

📊 **十個模型、十組設定的交叉比較**

研究團隊把七個 benchmark 移植到 SCLATE 上，針對十種未修改的 harness／記憶系統組合，在十個模型上進行交叉比較。結果顯示：額外加裝的記憶系統，並不保證會勝過 harness 原生的記憶機制；不同模型即便套用同一套 harness 與記憶系統，使用方式也相差甚遠。

研究團隊接著用 SCLATE 對 Qwen3.5-4B 進行後訓練（post-train），讓模型學會透過未修改的 harness 與記憶系統運作。結果是：模型讀取的檔案行數減少了 6.8 倍，SWE-bench Verified 的通過率提升 16.7 個百分點，寫出的記憶紀錄也更豐富，在held-out 的 MetaClaw 測試上準確率最高提升 11.8 個百分點。

🎯 **實務啟示**

對正在建構或評估長時程 agent 系統的工程師來說，SCLATE 揭示的重點是：記憶系統不是裝了就有用，harness 與記憶的「配合方式」本身就值得被訓練，而不只是被動設計。若團隊正苦於為每個 agent／benchmark 組合重寫排程邏輯，這類開放事件排程基礎設施值得關注。

🔗 **來源**
- 標題：SCLATE: A Substrate for Continual-Learning Agent Training and Evaluation
- 作者／機構：Youngmok Jung, Sirajul Salekin, Henry Tran, Javier Movellan, Zhao Huang, Manjot Bilkhu（Apple）
- 連結：https://machinelearning.apple.com/research/sclate-agent-training-evaluation

#ContinualLearning #AIAgents #Apple #MachineLearning #AgentEvaluation #SWEBench #PostTraining #Qwen #AgentHarness #AIResearch
