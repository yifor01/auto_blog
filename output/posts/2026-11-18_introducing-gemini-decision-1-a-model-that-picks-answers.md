---
title: 'Introducing Gemini Decision 1: A Model That Picks Answers Instead of Writing
  Them'
source: KDnuggets
url: https://www.kdnuggets.com/introducing-gemini-decision-1-a-model-that-picks-answers-instead-of-writing-them
model: claude-code/sonnet
generated_at: '2026-11-18T23:37:47.961335'
score: 105
---

📌 Gemini Decision 1：Google 推出不寫一字的決策模型

TL;DR：Google推出純機率輸出模型，定位agent決策層。

讀取顧客留言不用生成一句話回覆，而是直接告訴你該送進哪個客服佇列，機率0.98。這就是Google最新模型唯一的工作。

🤔 背景：agent stack 需要的是「不會寫字」的模型

每個agent系統背後都跑著大量判斷性呼叫：這句話要交給哪個工具、算不算違規、該用哪個model tier。多數團隊用全功能的生成模型搭配JSON parser處理這些任務，等於替丟棄的輸出token付錢。Google現在把這一層單獨拆出來賣。

🧩 怎麼運作：輸入一次，最多問1000題

Decision 1 在單次forward pass中讀取文字、圖片、影片、音訊、PDF，輸入上限262,144 tokens。對同一份輸入，可以問最多1,000道封閉式問題，分三種類型：

- Yes/No（API中稱noul）：回傳0.01~0.99的機率
- Choice：2到255個選項，各自回傳機率
- Score：依評分量表給出加權分數，以及每個等級的機率

每個答案都附帶confidence值。計價是每百萬輸入token 0.10美元，共用的輸入只算一次，輸出因為不存在文字生成而完全免費；AI Studio還提供免費額度做原型驗證。能力表上明確列出不支援文字生成、thinking、function calling、structured outputs、batch與caching——它是一個評分引擎，不是聊天機器人。

📊 實測：三個案例的延遲與花費

| 測試 | 輸入 | 結果 | 中位延遲 | 輸入token |
|---|---|---|---|---|
| Quickstart | 「馬克杯裂了」 | Damaged 0.99／Queue: replacements 0.98 | 407 ms | 173 |
| 模糊訊息 | 「被重複收費、把手缺角」 | Damaged 0.99／Queue: replacements 0.50 vs billing 0.48 | 574 ms | 181 |
| 圖片+文字 | 休息室檯面照片 | Spill 0.95／Action: wipe with cloth 0.98／Severity 1.19（滿分2） | 1,343 ms | 1,326 |

文章作者實測，文字查詢每次花費約0.000017美元，約58,000次查詢才花1美元；圖片查詢每次約0.00013美元。Google自家四款產品已在用這個API：Gemini Notebook用它做model與thinking tier路由（文章引述聲稱日常查詢延遲可降40%）、Stitch用在wireframe的語音/點擊編輯、Labs的CC用它從200多種表情符號中挑反應、Search則用它檢查MCP工具是否有惡意行為。

💡 深入分析：信心分數才是真正賣的東西

作者強調，模糊訊息那題才是關鍵測試：模型沒有硬選一個答案掩蓋不確定，而是誠實回報50%對48%的拉鋸，confidence也只有0.50；同一次呼叫裡，對明顯的把手缺角仍給出0.99。但choice欄位在模糊案例中依然回傳「replacements」這個winner，沒有附加任何警示——只讀choice而不檢查confidence的程式碼，會把模糊案例和清楚案例同等自信地路由出去。這套機制只有在你自己設定confidence門檻，把低於門檻的狀況導去人工或備援時，才真正有價值。

⚠️ 限制：延遲宣稱與基準數字都是Google自己訂的

Google宣稱端到端延遲150~250ms，但作者實測文字呼叫穩定在339~577ms，圖片呼叫中位數達1.1~1.4秒，是宣稱值的5到9倍；Google的延遲數字只涵蓋16K tokens以內的context，而非完整的262K上限，且同樣的呼叫延遲落差超過300ms。另外，「比Gemini 3.5 Flash-Lite便宜近5倍」的說法，是Google自選benchmark、拿自家模型互相比較，無法反映它跟你現有的小型fine-tuned分類器相比誰更划算。模型頁面一面宣傳可用於即時多模態串流分類，另一面卻把Live API列為不支援；目前僅限Gemini生態，雖已上架OpenRouter、LangChain、Vercel AI SDK、LiteLLM等，但Google Cloud的支援仍標示「即將推出」。

🎯 實務啟示

把它用在路由與政策檢查這類高頻、判斷性的呼叫上；從第一天就讀取confidence而不是只讀winner；上線前務必拿自己的圖片或影片素材實測延遲，別直接拿Google的數字去承諾即時系統。

🔗 來源
- 標題：Introducing Gemini Decision 1: A Model That Picks Answers Instead of Writing Them
- 作者／機構：Shittu Olumide, KDnuggets
- 連結：https://www.kdnuggets.com/introducing-gemini-decision-1-a-model-that-picks-answers-instead-of-writing-them

#GeminiDecision1 #Google #LLM #AIAgents #MachineLearning #ClassificationAPI #AIEngineering #ModelRouting #ArtificialIntelligence #DecisionAPI
