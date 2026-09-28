---
title: Prompting Claude Opus 5.5
source: Hacker News
url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
model: claude-code/sonnet
generated_at: '2026-09-28T22:43:11.548694'
score: 96
---

📌 Anthropic 出手：Claude Opus 5.5 提示詞怎麼跟著調整？

TL;DR：Opus 5.5 的 thinking 恆常開啟且預設 effort 下修至 medium，舊提示詞能跑，但省錢省時間得靠重新校準。

如果你的 Agent pipeline 是照著 Claude Opus 5 的參數硬搬過來的，先別急著慶祝「相容」。Anthropic 官方最新發布的 Prompting Claude Opus 5.5 指南開宗明義提醒：舊提示詞「應該」能正常運作，但這句話背後藏著一個關鍵變化，thinking（模型的內部推理）現在是恆常開啟的，你再也不能用 `thinking: {"type": "disabled"}` 把它關掉了。

🤔 **為什麼需要一份新的提示指南**

根據官方說明，Opus 5.5 產生輸出 token 的速度比 Opus 5 快超過 30%，完成同一任務所需的 token 數也更少。但這份效能提升不是免費午餐：Opus 5.5 的預設 effort 是 medium，而 Opus 5 的預設是 high；效果分級的名稱在不同模型間並不代表同樣的思考量。換句話說，你原本設定的 effort 值，在新模型上可能代表完全不同的成本與延遲曲線，直接照搬容易讓某些任務跑得比預期久、比預期貴。

🧩 **兩個必須重新測試的情境**

第一是效果分級（effort）的校準。官方建議從 medium 開始，明確設定數值，再拿自己的評測集去比較不同等級的表現，而不是延用 Opus 5 時代的設定。在 Anthropic 的測試中，Opus 5.5 的 medium 就能打平或超越 Opus 5 的 high，在部分程式碼評測上，甚至 low 就能以更低成本逼近 high 的表現。同時要注意，同一個 effort 等級下，Opus 5.5 傾向比 Opus 5 思考得更多，尤其是在 xhigh 與 max 等級，因此需要把 `max_tokens` 拉高（官方在長時間 agentic 任務中，用到模型上限的 128,000 效果不錯），否則思考用掉的 token 可能會把回覆截斷。

第二是「thinking disabled」的遷移。Opus 5 允許在 high 以下的 effort 關閉 thinking，Opus 5.5 不再接受這個設定。如果你原本的整合是關閉 thinking 跑的，官方建議：先從 low effort 開始測量效果與延遲；移除當初為了取代 thinking 而寫的「請把推理過程寫在回覆裡」之類指令，改成讀取 summarized thinking 區塊；重新測試舊的 thinking-disabled 因應措施是否還必要；並且改用逐一檢查回覆區塊型別（block type）的方式讀取結果，而不是假設第一個內容區塊就是文字。

📊 **在程式碼、知識工作與視覺理解上的具體差異**

官方測試指出，在真實程式碼庫裡進行多步驟工作時，Opus 5.5 在預設 medium effort 下就能打平甚至超越 Opus 5 在 high effort 下的表現，且步驟數與 token 用量都更少；它也更能撐住長時間、少人監督的自動化任務，例如多小時的程式碼庫稽核與遷移。在知識工作上，模型更不容易講錯數字或引錯來源，在財務建模與抓出投影片與試算表中細節錯誤上也有改善。在視覺理解方面，即便設定最低的 effort，Opus 5.5 讀取密集圖表數值的準確度仍優於 Opus 5 在最高 effort 下的表現，且只用一小部分的輸出 token；在需要依賴「位置關係」判讀的任務（例如流程圖箭頭連到哪個方塊）上也更可靠，操作電腦應用程式（computer use）的成功率在預設 effort 下就能達到 Opus 5 需要更高 effort 才能達到的水準。

💡 **一個容易踩到的快取陷阱**

指南特別提醒：在頂層改變 effort 數值會讓 prompt cache 失效。如果只是想針對個別回合調整思考量，應該使用「單一訊息層級的 effort 變更」（beta 功能），這樣才能保留快取效益。

🎯 **實務啟示**

不要假設「舊提示詞能跑」等於「舊設定是最佳設定」。把 effort 明確寫死、針對自己的評測集掃過幾個等級、重新檢視是否還在用 thinking-disabled 時代的因應手法，再依任務把 `max_tokens` 拉高，是遷移到 Opus 5.5 時最值得花時間做的事。

🔗 **來源**
- 標題：Prompting Claude Opus 5.5
- 作者／機構：Michelangelo11（Hacker News 提交）
- 連結：https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5

#Anthropic #ClaudeOpus #PromptEngineering #LLM #AgenticAI #AIcoding #ThinkingTokens #DeveloperTools #GenerativeAI #MachineLearning
