---
title: Perplexity and Intelligence
source: OpenAI Blog
url: https://openai.com/index/perplexity-and-intelligence
model: claude-code/sonnet
generated_at: '2026-11-22T22:31:06.871789'
pinned: true
---

📌 OpenAI 揭密：他們到底用什麼數字追蹤模型進步

TL;DR：OpenAI 公開內部長年追蹤 pretraining 進展所依賴的指標——perplexity（以 cross-entropy loss 呈現），並揭露 2026 年 loss 出現明顯加速。

當外界還在用 benchmark 分數爭論哪個模型更強時，OpenAI 透露，他們自己盯著進度儀表板時，看的其實是一個更基礎、也更古老的指標：perplexity。而這篇文章裡最耐人尋味的一句話是——最新一代模型的設計，已經有「有意義的貢獻」來自 AI 本身。

🤔 **Perplexity 不是壓縮檔，是預測能力**

文章先澄清一個常見誤解：這裡說的「compressor（壓縮器）」不是像 GZIP 那樣產出壓縮檔案的工具，而是指一個能透過預測未見過的資料來完成壓縮的模型。換句話說，一個在某份語料上訓練出來的最佳 compressor，不代表它「記住」了語料內容，而是學到了預測資料分佈的能力。在實務上，OpenAI 追蹤的是 perplexity 的 log 值，也就是我們熟知的 cross-entropy loss。

🧩 **為什麼是內部程式碼庫，而不是公開語料**

自 GPT-3.5 以來，OpenAI 用來追蹤進度的主要 held-out 資料集，來源是自家的內部程式碼庫（internal codebase），文中公布的數字正是在這份固定快照（fixed snapshot）上測得的結果。

💡 **用程式碼當尺，量不同時代的模型會失真**

這裡有個值得工程師留意的方法論陷阱：GPT-2 與 GPT-3 當年訓練時用的資料組成，跟現在差異很大，用「預測程式碼的能力」去衡量它們，其實是一個很差的通用能力代理指標（proxy）。這也點出用 perplexity 作為跨模型共用指標時，資料集選擇本身就是個挑戰。不過作者認為，把這些舊模型和現代模型放在一般文字（general text）上一起評估，仍然具有參考價值；而選擇以內部程式碼庫的 perplexity 作為本文主軸，單純是因為這是 OpenAI 目前在 pretraining 上最依賴、最能反映進展的數字。

📊 **2026 年 loss 曲線明顯加速，但原因不只是自動化**

文章提到，把 OpenAI 歷代模型的 loss 畫成一張圖，會看到 2026 年出現一段明顯加速下降的區段。OpenAI 將這主要歸因於長期研究與算力投資的累積成果，自動化（即 AI 參與研究流程）只是較小的一部分原因。但值得注意的是，對於最新一批模型，他們已經觀察到 AI 在模型設計上帶來了「有意義的貢獻」。

⚠️ **指標本身有邊界**

文中也坦言，perplexity 作為共用指標的侵蝕點在於資料集選擇：不同世代模型的訓練資料分佈不同，用單一固定語料（尤其是程式碼）比較，容易誤判誰的「通用智能」更強。這是解讀任何跨模型 loss 比較圖時都該放在心上的前提。

🎯 **對工程師的實務啟示**

如果你也在追蹤自家模型的 pretraining 進度，這篇文章等於給了一個背書：固定 held-out 集上的 cross-entropy loss，仍是業界最可靠、最被長期依賴的進度刻度，比起花俏的 benchmark 排行榜更穩定。但同時也要記住，跨世代、跨資料分佈比較 perplexity 時，數字好看不代表能力真的可比；而「AI 開始對模型設計本身做出貢獻」這個訊號，值得持續關注後續會不會成為研究流程的常態。

🔗 **來源**
- 標題：Perplexity and Intelligence
- 作者／機構：OpenAI
- 連結：https://openai.com/index/perplexity-and-intelligence

#OpenAI #Perplexity #CrossEntropyLoss #LLM #Pretraining #MachineLearning #AIResearch #ModelEvaluation #GPT #AIAutomation
