---
title: Six Chinese AI firms accused of aggressively copying US frontier models
source: Ars Technica AI
url: https://arstechnica.com/tech-policy/2026/09/six-chinese-ai-firms-accused-of-aggressively-copying-us-frontier-models/
model: claude-code/sonnet
generated_at: '2026-09-10T20:08:46.878622'
score: 82
---

📌 美國三大機關點名六家中國AI公司「工業級」蒸餾美系模型

TL;DR：NSA、CISA、FBI聯合指控DeepSeek等六家中國AI公司透過API濫用大規模蒸餾美國前沿模型，可能為中國省下數十億美元研發成本。

如果有人用數百萬筆幾乎一模一樣的提示詞，對著同一個模型API瘋狂提問，你會怎麼解讀？美國國安機關給出的答案是：這不是壓力測試，這是規模化的智慧財產竊取。

🤔 **三大機關聯手指控，鎖定六家中國AI公司**

美國國家安全局（NSA）、網路安全暨基礎設施安全局（CISA）與聯邦調查局（FBI）於週二發布聯合聲明，指控DeepSeek、Moonshot AI、阿里巴巴（Alibaba）、MiniMax、StepFun與Z.AI等六家中國AI公司，自2024年底以來針對美國前沿模型發動「工業級」的蒸餾攻擊，鎖定對象包括Claude、GPT、Gemini與Grok等模型的變體。三大機關表示，這些公司「很可能」是在「中國政府知情」的情況下進行這些行動。

聲明中指出，透過工業級蒸餾（distillation）萃取美國模型能力的中國AI公司，能顯著縮短開發時程、減少訓練前沿模型所需的財務支出，這也是美方認定此舉威脅到美國在AI競賽中領先地位的核心原因。

🧩 **手法一：假帳號洪水攻擊推論API**

第一種手法是大量利用AI模型的推論（inference）API。攻擊者透過批量購買未經合法使用者註冊的假帳號，組成帳號群，執行「高度協調的查詢」，這些查詢帶有相同或相似的提示文字，針對相似主題可能發送出從數千筆到數百萬筆不等的請求。

🧩 **手法二：誘導模型吐出隱藏的思維鏈**

第二種手法是利用提示注入（prompt injection）技巧來越獄模型，刻意設計能迫使模型揭露其隱藏的chain-of-thought推理過程的提示詞。聲明特別點名DeepSeek曾使用指示模型「想像並逐步寫出」已完成回應背後內部推理過程的提示詞。

💡 **建議因應：偵測代理帳號與灰色市場**

為了讓美國AI公司更難被竊取能力，機關建議業界必須提升對這類複雜攻勢的偵測能力，包括辨識依賴「灰色市場代理」、藉此規避地理限制，並透過多重路徑路由蒸餾請求以取得未授權存取的數萬帳號集群。

🎯 **實務啟示**

對建構或維運LLM推論服務的工程團隊而言，這份聲明等於是一份具體的異常流量特徵清單：大量相似或雷同的提示文字、針對同主題的巨量查詢、以及誘導模型輸出內部推理鏈的越獄嘗試，都值得納入API濫用偵測與速率限制策略的優先觀察項目。

🔗 **來源**
- 標題：Six Chinese AI firms accused of aggressively copying US frontier models
- 作者／機構：Ashley Belanger, Ars Technica
- 連結：https://arstechnica.com/tech-policy/2026/09/six-chinese-ai-firms-accused-of-aggressively-copying-us-frontier-models/

#AI #NationalSecurity #ModelDistillation #DeepSeek #LLMSecurity #PromptInjection #APIAbuse #ChinaAI #Cybersecurity #FrontierModels
