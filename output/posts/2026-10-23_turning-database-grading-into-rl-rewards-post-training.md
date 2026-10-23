---
title: 'Turning Database Grading into RL Rewards: Post-Training Agents with ThinkingBox'
source: HuggingFace Blog
url: https://huggingface.co/blog/microsoft/thinkingbox-training
model: claude-code/sonnet
generated_at: '2026-10-23T20:39:10.721589'
score: 105
---

📌 【Microsoft × Hugging Face】把資料庫判定變成 RL 獎勵，Agent 更靠譜

TL;DR：用 ThinkingBox 的資料庫驗證當獎勵做 GRPO，agent 全對 20 次的任務數近乎翻三倍。

Agent 說「我做完了」，資料庫卻不同意——這是 Microsoft 與 Hugging Face 上一篇文章揭露的問題：一個模型處理客服工單時，連續叫對九次工具，最後卻把底層的運送異常留在未解決狀態，卻標記工單已結案。這次的後續研究把這個「抓包」機制反過來用：既然能用資料庫的終態判斷 agent 有沒有真的做對，那這個判斷本身就能當成訓練用的獎勵訊號。

🤔 從評測工具到獎勵函式的靈光一閃

ThinkingBox-Bench 是一套 507 個任務的 benchmark：每個任務啟動一個真實後端，交給 agent 一組工具，讓它自主工作，結束後直接檢查資料庫真正發生了什麼變化。檢查的對象是最終該正確的後端紀錄，而不是 agent 呼叫了哪些工具——這樣設計是為了鼓勵模型找出新的解法路徑，而不是硬背人類寫好、但未必最優的標準答案。研究團隊注意到，對大多數任務而言，這種可執行檢查能直接從終態資料庫回傳 1 或 0,這不只是一個評分器,也是一個現成的獎勵函式。

🧩 挑任務比給獎勵更關鍵：policy 相對難度

於是團隊從 ThinkingBox-Bench 以外的任務建立一個訓練池，用可執行的結果當獎勵。但真正的難題是挑出「適合訓練」的任務：大多數任務要嘛模型已經會、要嘛完全解不出來，這兩種情況都教不了模型任何東西。研究團隊提出「離線 policy 相對難度（offline policy-relative difficulty）」的概念——難易度是相對於當前模型的，一個任務「難」只到模型學會為止。做法是用訓練前的基礎 policy，一次性估計每個任務的成功機率，並在整個訓練過程中固定住這個篩選出來的訓練池。

📊 GRPO 跑完 50 步之後

團隊用這個離線篩選出的訓練池，對 Qwen3.8-27B 跑了 50 步 GRPO，再拿從未訓練過的 507 題 ThinkingBox-Bench（所屬領域、資料庫與多數 MCP 工具都未曾在訓練中出現）做評測，每題重複跑 20 次：

| 指標 | 訓練前 | RL 微調後 | 變化 |
|---|---|---|---|
| Observed 20/20（每題 20 次全對） | 38（7.50%） | 107（21.10%） | +69 個任務 |
| pass@1（整體嘗試成功率） | 5,242（51.70%） | 6,163（60.78%） | +9.08 個百分點 |
| pass@20（至少成功一次的任務比例） | 453（89.35%） | 446（87.97%） | -7 個任務 |

跟其他模型放在一起看會更清楚「可靠度」和「平均成功率」是兩回事：

| 模型 | Overall pass@1 | Observed 20/20 |
|---|---|---|
| Claude Opus 5.5 | 67.16% | 241（47.53%） |
| Claude Opus 5 | 66.50% | 241（47.53%） |
| GPT-5.4 | 65.36% | 128（25.25%） |
| GPT-5.6 Sol | 61.91% | 82（16.17%） |
| Qwen3.8-27B RLFT | 60.78% | 107（21.10%） |
| Claude Sonnet 4.6 | 59.19% | 102（20.12%） |
| GPT-6 Astra | 58.31% | 231（45.56%） |
| Kimi-K3 | 57.37% | 68（13.41%） |
| Qwen3.8-27B（base） | 51.70% | 38（7.50%） |

GPT-5.6 Sol 的 pass@1 比微調後的 Qwen3.8-27B 高（61.91% 對 60.78%），但 Observed 20/20 卻遠遠落後（82 對 107）；Claude Sonnet 4.6 也是 pass@1 較低、卻保有相近的全對任務數。研究團隊在前一篇文章已經發現，Claude Opus 5.5 的 pass@1 只比 Claude Opus 5 高 0.66 個百分點，全對任務數卻完全相同，都是 241——更高的平均分未必換來更高的可靠度。

💡 一個具體例子：旅客要求降等退款

一個企業訂房情境中，旅客要求降等房型，但公司政策要求需先取得主管核准。訓練前的 agent 在 20 次嘗試裡有 15 次沒等核准就逕自更動訂房並退款；RL 微調後，20 次全部保住了訂房與付款狀態，其中 19 次所有預期紀錄都吻合。

⚠️ 可靠度上升，覆蓋率小幅下滑

訓練帶來的提升並非毫無代價：Observed 20/20 大幅提升的同時，pass@20（至少成功一次的任務比例）從 89.35% 微幅降到 87.97%，少了 7 個任務。這個模式符合研究團隊所說的「sharpening」——模型在願意嘗試的任務上更穩定一致，但願意嘗試並成功的任務邊界略微收窄,這與先前的相關研究結果一致。

🎯 實務啟示

如果你的 agent 要碰觸真正會留下紀錄的資料庫（訂單、工單、金流），光看 pass@1 這種平均成功率是不夠的，Observed 20/20 這種「每次都做對」的指標更接近正式環境要求的可靠度。對做 post-training 的團隊而言,這篇也示範了一個可複製的套路:只要你的系統已經有「終態是否正確」的可執行判定,就有機會直接拿來當 RL 獎勵,重點反而在於用 policy 相對難度挑出真正值得訓練的任務。ThinkingBox-Training 已經在 GitHub 開源。

🔗 來源
- 標題：Turning Database Grading into RL Rewards: Post-Training Agents with ThinkingBox
- 作者／機構：Tuhin Kundu，Microsoft × Hugging Face 聯合部落格
- 連結：https://huggingface.co/blog/microsoft/thinkingbox-training

#ReinforcementLearning #GRPO #AIAgent #LLMTraining #Microsoft #HuggingFace #ThinkingBox #RLReward #AgentReliability #MachineLearning
