---
title: 'ALTK-Evolve: How learned memory tops the τ²-bench leaderboard on customer
  service tasks without a frontier model'
source: HuggingFace Blog
url: https://huggingface.co/blog/ibm-research/altk-evolve-bc
model: claude-code/sonnet
generated_at: '2026-10-20T20:44:32.554863'
score: 106
---

📌 IBM 用學習記憶讓 GPT-4.1 登頂客服 benchmark

TL;DR：不升級模型、只靠從過往對話學到的 playbook，GPT-4.1 客服 agent 打贏所有 retail 榜單對手。

一個基於 GPT-4.1 的基本 ReAct agent，沒有更新任何權重，光靠在 system prompt 裡多塞一段「學來的守則」，就在 τ²-bench retail 榜上超越了所有其他 retail 參賽項目。這聽起來違反直覺：大家都在比模型多強，IBM Research 的 ALTK-Evolve 卻示範了「記憶」本身就能是勝負關鍵。

🤔 **τ²-bench 在考什麼：政策遵循下的客服對話**

τ²-bench（來自 Sierra）測量 agent 在真實限制下處理客服對話的能力。每個任務讓 agent 面對一個由 LLM 模擬、帶有特定目標的客戶，配上一組領域工具（查訂單、辦退款、改機票），以及一份 agent 必須遵守的政策文件。agent 必須問出正確細節、守住政策邊界，並執行正確、往往不可逆的動作；任務只有在最終資料庫狀態完全符合預期時才算解決，是嚴格的二元獎勵。文章使用 τ²-bench 自帶的基本 ReAct agent 實作（THINK → ACT 兩階段迴圈），agent 模型為 gpt-4.1，客戶模擬模型為 gpt-5.5，每個任務跑 4 次試驗，涵蓋 retail 與 airline 兩個領域。

🧩 **方法：讓同一個模型自己寫下自己的守則**

ALTK-Evolve 的做法是分析 agent 在訓練任務上的歷史嘗試，用同一個 gpt-4.1 模型把成功與失敗的經驗提煉成簡短的行為規則——例如如何驗證客戶身分、如何確認交易、如何處理退貨——再把這些守則附加到 agent 的 system prompt 上，套用在後續對話中。整個流程不需要更新權重，也不需要人工標註；提煉守則與驅動 agent 用的是同一個模型。文章提供了實際守則範例，像是「在進行任何訂單相關操作前先驗證使用者身分」「處理退貨或換貨時主動列出明細並說明退款時程，不等使用者問」「每個步驟只做一件事：不要把工具呼叫和回覆訊息放在同一輪，並等待工具結果再回覆」。守則從 τ²-bench 訓練任務集的軌跡中提取，然後原封不動套用到held-out測試集上。

📊 **數據：守則越多，可靠度提升越明顯**

每條守則都帶有 support count（它是從多少筆不同訓練任務中提取出來的），文章比較三種設定：

| 設定 | 說明 | Retail 守則數 | Airline 守則數 |
|---|---|---|---|
| baseline | 不加任何守則 | 0 | 0 |
| sup3 | 只保留 support ≥ 3 的高信心核心守則 | 31 | 14 |
| lossless | 保留整合後所有守則（support ≥ 1） | 292 | 101 |

評估用兩個指標：Mean Accuracy（4 次試驗平均成功率，衡量能力）與 Pass^4（4 次試驗全部通過的任務比例，衡量可靠度，也是 τ²-bench 榜單採用的指標）。held-out 測試結果如下：

| 領域（測試任務數） | 設定 | Mean Accuracy | Pass^4 |
|---|---|---|---|
| Retail (40) | baseline | 78.1% | 57.5% |
| Retail (40) | sup3 | 78.8%（+0.7） | 60.0%（+2.5） |
| Retail (40) | lossless | 82.5%（+4.4） | 67.5%（+10.0） |
| Airline (20) | baseline | 57.5% | 35.0% |
| Airline (20) | sup3 | 60.0%（+2.5） | 45.0%（+10.0） |
| Airline (20) | lossless | 65.0%（+7.5） | 40.0%（+5.0） |

Retail 領域的 Pass^4 從 57.5% 提升到 67.5%，正是這個提升讓它超越了榜單上其他 retail 項目。

💡 **守則的「劑量」要依領域調整**

兩個領域對守則數量的反應並不一致：retail 領域「越多越好」，sup3 的少量核心守則對 accuracy 幾乎沒有幫助，要上到 lossless 的全量守則才有明顯跳升；airline 領域則在可靠度這端反過來——lossless 在 accuracy 上領先（65% 對 60%），但精簡的 sup3 核心（僅 14 條）反而在 Pass^4 上更可靠（45% 對 lossless 的 40%）。文章將此總結為：support count 是一個該依領域調校的參數，而不是寫死的固定值。

⚠️ **代價出現在 token，不是對話輪數**

文章提到，守則帶來的成本主要反映在 prompt 的輸入 token 數量上，而不是讓對話變得更冗長、更迂迴；換句話說，效能提升來自「資訊更充足的單次呼叫」，而非「多繞幾圈對話」。

🎯 **實務啟示**

對於已經在用 GPT-4.1 這類非推理型（non-reasoning）模型跑 agent 的團隊，這個結果提示：在換更貴的前沿模型之前，先檢查是否把過往成功與失敗的經驗系統性地沉澱進了 prompt。而守則數量（support 門檻）不是一次設定就通用，需要依任務領域實際測試找出最適劑量。

🔗 **來源**
- 標題：ALTK-Evolve: How learned memory tops the τ²-bench leaderboard on customer service tasks without a frontier model
- 作者／機構：IBM Research（Ashwath Vaithinathan Aravindan、Vatche Isahagian、Vinod Muthusamy 等）
- 連結：https://huggingface.co/blog/ibm-research/altk-evolve-bc

#AIAgents #CustomerServiceAI #GPT4 #PromptEngineering #LLMEvaluation #IBMResearch #ReAct #AgentMemory #TauBench #LLMOps
