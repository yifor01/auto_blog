---
title: Claude新模型釋出！跑分暴擊GPT-6 Luna，價格比梁文谷還便宜，OpenAI只能送重置卡挽尊
source: 量子位
url: https://www.qbitai.com/2026/10/501832.html
model: claude-code/sonnet
generated_at: '2026-10-08T22:21:21.251260'
score: 94
---

📌 Claude Haiku 5.5 開賣：跑分叫板 GPT-6 Luna，定價也直接看齊

TL;DR：Haiku 5.5 用更低成本換來遠高於前代的 agent 表現，定價規則正面對標 GPT-6 Luna。

這次 Anthropic 沒有把主角戲留給 Opus 或 Sonnet，反而先端出小模型 Haiku 5.5。更特別的是，官方跑分選的對照組不是上一代自己，而是 GPT-6 Luna，逐項比較的意味相當明顯。

🤔 **小模型賽道的新守門員**

量子位報導指出，Claude Haiku 5.5 在跑分上直接超越了此前被視為小模型「斬殺線」的 DeepSeek V4.1 Flash 與 GLM-5.3-Flash。報導還提到，由於過去常用的鵜鶘騎腳踏車測試已經飽和，業界開始轉用「奔跑斑馬測試」做橫向比較，顯示小模型之間的跑分競爭已經相當白熱化。

🧩 **effort 分檔機制首次下放到 Haiku**

Haiku 5.5 是系列中第一個支援 effort 調節的 Haiku 模型，延續了 Claude 家族從 low 到 max 的五檔配置，使用者可以依任務難度在速度與品質之間取捨。相比之下，上一代 Haiku 4.5 在計算機操作（computer use）與編碼類任務上表現非常薄弱，這一代則被形容為「直接進化」。

📊 **低檔打贏前代的最高檔**

根據官方數據，在 OSWorld 2.1（測試 agent 操作真實電腦完成多步任務）中，Haiku 5.5 的 Low 檔準確率為 42.0%，單次成本 $0.07；Max 檔則來到 72.4%，成本 $0.61。對比 Haiku 4.5 的 Max 檔，只有 15.7% 準確率，成本卻要 $1.45。也就是說，新模型最省錢的檔位，表現就已經超過舊模型最貴的檔位。

在 GDPval-AA v2.1（測試 44 個職業的真實專業工作）上也出現類似曲線：Haiku 5.5 的 Low 檔 Elo 為 1125、成本 $0.01；Max 檔 Elo 1620、成本 $0.87。Haiku 4.5 的 Max 檔僅有 Elo 735、成本 $0.24。

💡 **換了 tokenizer，省下的錢打了折扣**

Haiku 5.5 改用與 Sonnet 5.5、Opus 5.5 相同的新 tokenizer，同樣內容會耗費更多 token，程式碼、表格與非英語內容的膨脹幅度可能更明顯。這意味著在 AA 測評中，雖然 API 標價降了，但「完成任務的平均成本」實際省下的幅度並沒有宣傳數字那麼理想。

Haiku 5.5 的定位依然是執行層，不是 Sonnet 的平替。Terminal-Bench 4.0 上，Haiku 5.5 僅拿下 39.2%，Sonnet 5.5 則是 70.6%，在複雜多步編碼、跨檔案重構與長週期自主規劃上差距明顯。Anthropic 也建議複雜 agent 編碼任務優先選用 Sonnet 5.5 或 Opus 5.5。報導提到一個組合案例：Cognition 的 Devin 用 Opus 5.5 做主模型、Haiku 5.5 做子智慧體，在 FrontierCode 測試中跑到 66.2%，高於兩個模型各自單跑的成績，說明 Haiku 5.5 更適合扮演「任務已拆好、驗收標準明確、可並行執行」的角色。

⚠️ **五個遷移地雷**

從 Haiku 4.5 切換過來並非改個模型名就能上線，報導列出五項破壞性變更：budget_tokens 的手動思考配置會直接報錯，必須改成自適應思考搭配 effort 參數；temperature、top_p、top_k 全部鎖定在預設值，依賴取樣參數做創意控制或多樣化生成的應用需要調整邏輯；assistant 訊息預填充功能被取消，原本靠預填充強制 JSON 開頭的寫法得改用工具呼叫或結構化輸出介面；計算機操作工具版本從 computer_20250124 換成 computer_toolset_20260801，介面格式與回傳結構可能不同；自適應思考預設開啟後，回應的第一個內容塊可能是思考塊而非正文，解析邏輯需按 type 欄位過濾。

另外兩項附帶更新：Sonnet 5.5 的快取讀取價格從每百萬 token $0.20 降到 $0.10，Anthropic 表示多數 agent 任務因此成本約降 20%；Max 與 Team 訂閱使用者本週起可領取 API 額度（Max 5x 每月 $100、Max 20x 每月 $200、Team 最多每月 $500 團隊共享），可用於所有模型的實驗性開發。

🎯 **實務啟示**

如果現有服務正在用 Haiku 4.5，升級前務必先對照 Anthropic 的遷移指南，尤其是取樣參數鎖定與思考塊解析這兩項最容易讓請求直接報錯。效益最大的場景是把 Haiku 5.5 當作拆解好任務的執行節點，搭配 Sonnet 5.5 或 Opus 5.5 作主規劃模型，而不是期待它直接取代中型模型的複雜推理能力。

🔗 **來源**
- 標題：Claude新模型釋出！跑分暴擊GPT-6 Luna，價格比梁文谷還便宜，OpenAI只能送重置卡挽尊
- 作者／機構：夢晨（量子位）
- 連結：https://www.qbitai.com/2026/10/501832.html

#Claude #Haiku #Anthropic #LLM #AIAgent #ModelPricing #GPT6Luna #AIBenchmark #PromptEngineering #AICoding
