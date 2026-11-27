---
title: 'Distilling Kimi-K3.1-Pro into Qwen3.8-27B: Teaching a model a new language'
source: Together AI
url: https://www.together.ai/blog/distilling-kimi-into-qwen
model: claude-code/sonnet
generated_at: '2026-11-27T01:10:28.456574'
score: 88
---

📌 教 Qwen3.8-27B 寫寮語：LoRA 蒸餾只花 260 美元

TL;DR：用 Kimi-K3.1-Pro 當老師，花 260 美元把小模型的寮語翻譯分數從 5.5 拉到 44.3 分。

當你要求一個小模型翻譯成寮語（Lao），它卻自信滿滿地回你一段泰文，這不是翻譯錯誤，而是模型根本不知道「寮語」長什麼樣。Together AI 在實驗中踩到了這個坑，也順手把修法寫成了一篇完整的技術筆記。

🤔 **小模型的語言盲點**

Together AI 發現，熱門的小型語言模型（SLM）Qwen3.8-27B 在 FLORES-200 的寮語測試集上只拿到 5.5 分（chrF++，一種 0 到 100 分、衡量譯文與人工參考譯文重疊程度的指標），而且輸出中只有 11% 的內容真的是寮語文字。多數時候模型把寮語請求誤判成「翻成泰文」，因為寮語和泰文是近親語言，但使用完全不同的書寫系統。作為對照，Kimi-K3.1-Pro 在同一測試集拿下 47.5 分。文中舉的例子很直接：同一句英文，Qwen3.8-27B 給出的是一段語意通順但語言錯誤的泰文，Kimi-K3.1-Pro 給出的才是真正的寮文。作者稱這是「jagged intelligence（能力參差）」的典型案例：大模型輕鬆搞定的小眾任務，小模型卻完全失手。

🧩 **off-policy 蒸餾：讓大模型當文字生成器，不必共用 tokenizer**

因為 Kimi 和 Qwen 的 tokenizer 不同，無法採用需要逐 token 對齊機率的 on-policy distillation（讓學生生成文字、教師逐 token 打分的方式），團隊改用 off-policy distillation：直接讓教師模型（Kimi-K3.1-Pro，關閉 thinking 模式）生成翻譯文字，過濾掉非目標文字系統的輸出，再拿這些譯文當作 SFT（supervised fine-tuning）訓練目標，訓練 Qwen3.8-27B 的 LoRA adapter。整套流程用的是 Together Post-Training 平臺：同一個模型資源同時負責訓練 LoRA 與取樣評估，邊訓練邊用 held-out 測試句子打分。

評估用了四個指標：FLORES-200 devtest 上的 chrF++、寮文字元比例（直接檢查是否還在寫泰文）、泰文保留度（檢查學新語言有沒有把舊能力弄壞），以及用 Kimi 把輸出的寮文倒譯回英文、比對原句的「迴譯充分度」。

📊 **泰文意外失守，又意外補回來**

第一個對照實驗只用 945 句人工寮語參考句訓練，結果 25 步內寮語分數從 6.7 衝到 43.3，但泰文翻譯能力從 46.7 崩到 11.7，訓練結束時只剩 5.3 分，且 0% 的泰文輸出還留在泰文字母。換句話說，模型學到的是「被問翻譯就寫寮文」，而不是「寫使用者要的語言」。改用 Kimi 的寮語翻譯取代人工參考句，崩壞速度變慢，但泰文仍在第三個 epoch 滑到 44.3，300 句泰文測試裡有 17 句被寫成了寮文。真正解決問題的做法，是額外加入約 1,000 筆 Kimi 的泰文翻譯一起訓練，泰文分數最終落在 47.4 和 47.8，比原始模型還高，且整個訓練過程中沒有低於 47.3。最終版本的學生模型在每一句測試句都輸出寮文，chrF++ 達到 44.3 分，相當於教師分數的 93%，同時保住了泰文能力。整套實驗加總成本是 260 美元。

💡 **人工參考句 vs. 教師譯文：各有優勢**

文中也點出一個細節：用約 950 筆人工寮語參考句訓練的學生，在對照人工參考答案的 chrF++ 上拿到 44.7 分，略高於兩個蒸餾版本的 41.8、41.9 分，原因是訓練資料與測試資料（devtest）都出自同一套人工翻譯流程，風格天然貼近。但如果改用 Kimi 自己的翻譯當評分基準，蒸餾學生從 8 分衝到 58 分，反而超過人工訓練版本的 47 分。這說明蒸餾學到的是教師風格，而人工參考句的供給量終究有限，教師模型卻能無限產生訓練資料。

🎯 **實務啟示**

這篇文章給出的最大啟示，不是寮語翻譯本身（作者自己也承認這是小眾需求），而是「持續學習要記得保護舊能力」這個通用教訓：教模型一項新技能時，混入能保護既有強項的資料，否則最容易被新知識覆蓋的往往是語意最相近、最容易混淆的那個舊能力。對任何要用 LoRA 微調補強小模型弱點的團隊，這套 off-policy 蒸餾＋混合資料的流程、成本與評估方式都值得參考。

🔗 **來源**
- 標題：Distilling Kimi-K3.1-Pro into Qwen3.8-27B: Teaching a model a new language
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/distilling-kimi-into-qwen

#LLM #KnowledgeDistillation #LoRA #FineTuning #MachineTranslation #SmallLanguageModels #TogetherAI #Qwen #LowResourceLanguages #NLP
