---
title: Claude Haiku 5.5
source: Simon Willison
url: https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/
model: claude-code/sonnet
generated_at: '2026-10-07T22:27:39.081292'
score: 84
---

📌 Claude Haiku 5.5降價追平GPT-6 Luna,但藏了個tokenizer陷阱

TL;DR:Haiku 5.5價格打平GPT-6 Luna,但新tokenizer讓實際花費悄悄變貴。

一年前,Anthropic的Haiku 4.5定價是GPT-6 Luna的整整10倍。今天Anthropic終於把價格拉平——但魔鬼藏在一個大家容易忽略的細節裡:tokenizer。

🤔 **Haiku 4.5真的老了**

Simon Willison指出,前一代Haiku 4.5上市快一年,定價是每百萬input token 1美元、output token 5美元,即使在發布當時也偏貴,更是OpenAI GPT-6 Luna(上個月發布)定價的10倍。

📊 **新定價怎麼算**

新的Haiku 5.5把價格直接對齊GPT-6 Luna:兩者在10萬token以內都是每百萬token input 0.10美元、output 0.50美元。差異出現在超過門檻之後:

| 模型 | 門檻內價格(input/output) | 超過門檻後價格 |
|---|---|---|
| Claude Haiku 5.5 | $0.10 / $0.50(10萬token內) | $0.50 / $2.50 |
| GPT-6 Luna | $0.10 / $0.50(27.2萬token內) | $0.20 / $0.75 |

也就是說,工作量在10萬token以內,兩家價格一樣,但Haiku 5.5在benchmark分數上報得更高;超過10萬token之後,Luna的漲幅遠比Haiku 5.5溫和,整體更划算。

💡 **還有一個隱藏漲價:新tokenizer更「貪」**

Willison用自己的Claude Token Counter工具測試,發現同一段長prompt在Haiku 5.5上耗用的token數量,大約是Haiku 4.5的1.25倍。換句話說,即使牌面單價打平了,實際帳單可能因為tokenizer效率變差而悄悄墊高。

🧩 **用鵜鶘畫圖測試推理強度**

Willison照慣例請模型畫鵜鶘,分別測了low、medium、high、xhigh、max五個推理強度。新Haiku不能關掉推理,預設是medium。結果除了low以外的每個強度都畫出了還算像樣的自行車車架(他測試系列的另一個固定梗)。low強度的鵜鶘花費0.0936美分、耗時7秒;max強度則花了5分9秒,但也只花了3.3826美分。相比之下,一年前Haiku 4.5畫的鵜鶘花了0.7583美分(當時不支援推理強度選項),畫得很糟。

📊 **同天的另外兩個公告**

Anthropic同時宣布把Sonnet 5.5的cache read價格砍半,並且為Max與Team訂閱戶加碼每月API額度:Max 5x用戶每月100美元、Max 20x用戶200美元、Team訂閱戶最高500美元(團隊內共用)。額度金額剛好對應訂閱費用本身,且可以設定關閉API自動加值,餘額用完就直接停止請求,不會有意外扣款的風險;但額度不會累積到下個月,用不完就作廢。文中也提到,OpenAI目前仍允許Codex訂閱額度挪來做個人API用量,對重度API使用者來說仍是更好的方案,這次Anthropic的新額度制度至少拉近了一些差距。

🎯 **實務啟示**

選模型時別只看牌面單價:如果你的工作負載大多落在10萬token以內,Haiku 5.5和GPT-6 Luna價格相同,而Haiku報的benchmark分數更高,值得一試;但如果常跑長上下文(超過10萬甚至27萬token),Luna的漲幅曲線明顯更溫和。另外,換模型時務必重新估算token用量,新tokenizer可能讓同樣的prompt變貴,別只拿舊的成本估算套用到新模型上。訂閱Max或Team的團隊也該去Billing設定裡確認是否已經領取新的API額度,這筆錢不會自動累積。

🔗 **來源**
- 標題:Claude Haiku 5.5
- 作者/機構:Simon Willison
- 連結:https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/

#ClaudeHaiku #Anthropic #LLMPricing #GPT6 #TokenCounting #AIBenchmark #PromptEngineering #SonnetAPI #LLM #DeveloperTools
