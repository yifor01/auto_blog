---
title: The Agent Said It Was Done. The Database Disagreed.
source: HuggingFace Blog
url: https://huggingface.co/blog/microsoft/thinkingbox
model: claude-code/sonnet
generated_at: '2026-10-04T20:14:55.885282'
score: 100
---

📌 Agent 回報「已解決」，但資料庫不買單

TL;DR：ThinkingBox 用後端資料庫狀態而非回覆文字評分 agent，揭露表面成功背後的真實失敗率。

一位客戶的 745 美元廚房家電卡在貨運「例外」狀態十五天。AI agent 做了九次工具呼叫：查訂單、看物流、查客戶檔案、確認政策、開工單、整理時間軸，流程看起來無可挑剔。它最後把工單標記為「已解決」，回覆客戶「問題已解決，還有什麼能幫您的嗎？」。問題是，貨運的例外狀態根本沒解除，應該停在「待處理」，而客戶實際想問的事也沒被回答。九次工具呼叫全部格式正確，但資料庫裡的真實狀態說了不一樣的故事。

🤔 **工具呼叫不等於結果**

這正是微軟與 Hugging Face 聯合發布的 ThinkingBox 想揭露的問題：檢查 agent 有沒有正確呼叫工具、有沒有說出聽起來合理的結尾，都只是代理指標（proxy），不是真正的結果。只有 agent 最終在後端留下的資料狀態與副作用，才是唯一的證據。

在一組涵蓋 12 個 LLM 模型、121,680 次有效試驗的共同集合消融實驗中，79,853 次嘗試在可執行檢查（executable checks）下被判定失敗。這些失敗裡，67.24% 其實是「乾淨結束」：agent 呼叫了會改變狀態的工具，也沒有回報任何工具錯誤，看起來完全正常。但實際檢查資料庫後，77.61% 的失敗案例欄位值是錯的，43.30% 產生了不該有的額外副作用，25.36% 漏掉了必要的動作。

🧩 **507 個任務，每個跑 20 次**

ThinkingBox 把每個任務在乾淨的後端環境下重複執行 20 次獨立嘗試，涵蓋零售、車險、旅遊、新創銀行（neobank）、顧問五個領域，共 507 個場景。並報告三種分數：

| 指標 | 衡量什麼 | 回答什麼問題 |
|---|---|---|
| pass@1 | 所有嘗試中成功的比例 | 平常表現如何？ |
| pass@20 | 20 次中至少成功一次的任務比例 | 它能不能做到這件事？（廣度） |
| observed 20/20 | 20 次全部成功的任務數 | 它能不能每次都對？ |

📊 **分數高不代表可靠**

整體 pass@1 排名中，Claude Opus 5.5 以 67.16% 居冠，略高於 Claude Opus 5 的 66.50%；開源模型中 Kimi-K3 以 57.37% 領先。但看「20 次全對」的穩定度，故事完全不同：GPT-6 Astra 保留了 78% 的單次分數，Claude Opus 5.5 與 Claude Opus 5 各保留 71%，而 GLM-5.1、Kimi-K2.6、DeepSeek-V4-Pro 只剩下約 8%。

Kimi-K3 覆蓋面最廣，507 個任務中有 476 個（93.89%）至少成功過一次，是場上被完全擊敗任務數最少的模型；但它在「20 次全對」上只拿下 68 個任務（13.41%），是最不穩定的模型之一。相反地，Claude Opus 5 雖然只解開 79.09% 的任務（有 106 個任務完全攻不下），卻能在 47.53% 的任務上每次都成功。

💡 **升級模型未必買到可靠度**

Claude Opus 5.5 比 Claude Opus 5 的每次嘗試平均分數更高（67.16% 對 66.50%），也解開更多至少成功一次的任務，但兩者「20 次全對」的任務數完全相同：241 個。換句話說，半個百分點的headline分數提升，沒有換到任何額外的穩定性。

🎯 **實務啟示**

如果你要選一個模型去做會真正寫入資料庫、觸碰真實記錄的 agent 工作（退款、保單變更、訂單處理），不要只看 pass@20 這種「有沒有可能做到」的數字，它會系統性高估不穩定模型的可用性。應該盯著 pass@1 與 20/20 全對率，這才反映你部署後每天會實際遇到的情況。

🔗 **來源**
- 標題：The Agent Said It Was Done. The Database Disagreed.
- 作者／機構：Tuhin Kundu, Microsoft × Hugging Face
- 連結：https://huggingface.co/blog/microsoft/thinkingbox

#AIAgents #LLMEvaluation #ThinkingBox #Microsoft #HuggingFace #AgentBenchmark #Reliability #MCP #EnterpriseAI #LLM
