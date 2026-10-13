---
title: Build long-horizon agents with Grok 4.7 on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-long-horizon-agents-with-grok-4-7-on-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-10-13T22:01:11.505823'
score: 96
---

📌 【AWS 實測】Grok 4.7 的 reasoning effort 怎麼調,72 次 agent 實驗給答案

TL;DR:AWS 用 72 次受控 agent 實驗量化 Grok 4.7 的 reasoning effort 設定對準確率與 token 成本的取捨。

多數人在用推理模型時,對 reasoning effort 的設定多半是憑直覺調一個「感覺夠用」的等級。AWS 這篇文章反其道而行,直接設計了三個「必須搜尋而非查表」的任務,把 xAI Grok 4.7 在 Amazon Bedrock 上四個 reasoning effort 等級(low、medium、high、xhigh)跑了整整 72 次,量化出一條清楚的成本/準確率曲線。

🤔 **核心問題:effort 調高,agent 真的答得更準嗎?**

根據 SpaceXAI(xAI)的說法,Grok 4.7 使用比 Grok 4.6 更大的基礎模型,並以更長的強化學習訓練在偏重「需要花上數小時完成」的更難任務組合上練成,號稱更擅長自我驗證與管理更長 context。SpaceXAI 公開的 benchmark 顯示,相對 Grok 4.6 進步最大的項目集中在「衡量持續性工作」而非單輪問答的類別。但 benchmark 衡量的是標準任務,AWS 想驗證的是:在真正會呼叫工具、需要多步驟驗證的 agent 場景裡,reasoning effort 的邊際效益長什麼樣子。

🧩 **三個「只能靠搜尋,不能查表」的任務**

AWS 建了一個包含 20 個服務、7 個工具的合成環境,設計三個任務:從兩個服務的告警中診斷故障、在互相牽制的限制條件下安排維護排程,以及在預算限制下選出最佳的一組遷移方案。每個任務都刻意設計成「答案無法直接從資料讀出,必須先提出候選答案再驗證」,且透過窮舉方式驗證每個任務都恰好只有一個正確答案。

為了讓評測結果可信,AWS 遵循幾個原則:在提示詞中寫清楚評分依賴的每一條規則(例如明確說明「故障的服務不會自己發出告警」),用窮舉法先證明每個任務只有一個答案,只評分要求的最終結論行(例如 `FINAL: auth, checkout`)而不是整段推理過程,並把「格式缺失」與「答案錯誤」分開追蹤。系統提示詞特別要求 agent 在給出答案前自我檢查。整個 agent loop 是標準的工具呼叫迴圈:帶著設定好的 reasoning_effort 呼叫模型、執行回傳的工具呼叫、把結果掛回對應的 tool_call_id,重複直到模型不再請求工具,並全程追蹤 prompt_tokens 與 completion_tokens。

📊 **xhigh 全對,low 用八分之一 token 答對 15/18**

三個任務在四個 effort 等級下各跑 6 次,共 72 次,整體答對 67 次。

| Effort | 正確率 | 平均輸出 token | 中位秒數 |
|---|---|---|---|
| xhigh | 18/18 | 9,147 | 較長 |
| high | 17/18 | — | — |
| medium | 17/18 | — | — |
| low | 15/18 | 1,184 | 18 秒 |

值得注意的是,工具呼叫次數在各個 effort 等級幾乎不變(每次運行 17.2 到 18.7 次),也就是說 effort 改變的不是 agent「探索了多少」,而是它「針對同樣的事實做了多少推理」。由於每個任務每個等級只跑 6 次,等級之間的差異屬於「指向性」而非統計上的結論,但三個任務呈現的方向一致。

💡 **low 的成本/準確率比值其實很划算**

在 low 等級下,agent 用大約 xhigh 八分之一的輸出 token,答對 18 題中的 15 題,中位執行時間只要 18 秒。對於可以接受稍低完成率、或答案會經過人工複核的場景,low 是效率相當高的選擇。

⚠️ **樣本量小,結論僅供參考方向**

每個任務每個 effort 等級只跑 6 次,AWS 自己也坦承這樣的差異只能說是「指向性」而非統計上的確定結論。另外,reasoning token 會被計入輸出 token 並從 max_completion_tokens 扣除,如果上限設太低、推理階段就把額度用完,回應會沒有答案文字,AWS 建議在 agent 程式碼中特別檢查這種空內容的情況。

🎯 **實務上怎麼用**

如果你要在 Bedrock 上串接 Grok 4.7 做 agent,關鍵行動是針對自己的任務形狀重做這套測量,而不是直接套用別人的 benchmark 結論;同時在 Converse API 中,把 reasoning effort 等參數放進 additionalModelRequestFields,並把 maxTokens 設得足夠寬裕,讓推理和最終答案都有空間完成。

🔗 **來源**
- 標題:Build long-horizon agents with Grok 4.7 on Amazon Bedrock
- 作者／機構:Suheel Farooq(AWS Machine Learning Blog)
- 連結:https://aws.amazon.com/blogs/machine-learning/build-long-horizon-agents-with-grok-4-7-on-amazon-bedrock/

#Grok47 #AmazonBedrock #AgenticAI #ReasoningEffort #LLMEvaluation #ToolCalling #xAI #AIAgents #PromptEngineering #AWS
