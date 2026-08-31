---
title: Continuous Diffusion Language Models (CDLM's)
source: Hacker News
url: https://sander.ai/2026/08/24/continuous-dlms.html
model: claude-code/sonnet
generated_at: '2026-08-31T12:16:18.796088'
score: 24
---

📌 連續擴散語言模型的滅絕與復甦：一段被自回歸掩蓋的技術史

TL;DR：離散擴散稱霸語言生成三年後，連續版本近期又出現一波研究熱潮。

2023 年之前，連續擴散（continuous diffusion）與離散擴散（discrete diffusion）在語言生成的研究版圖上還算勢均力敵；但一張 2025 年survey論文的示意圖顯示，2024 年之後幾乎所有新論文都轉向離散方法，連續擴散彷彿一夜之間集體滅絕。Google DeepMind 研究者 Sander Dieleman（曾參與 Imagen、Veo、Nano Banana 等專案）在部落格中回顧了這段歷史，也點出近期一波新研究似乎正在讓連續擴散捲土重來。

🤔 **自回歸稱霸之外，還有別條路**

現代語言模型多為自回歸（autoregressive）：一次生成一個 token，這種分解方式讓所有生成步驟共享同一套「根據前文預測下一個 token」的任務，並透過 Transformer 架構搭配 teacher forcing 達到高效平行訓練，最終催生了今天的大型語言模型。但自回歸並非唯一選項；受影像與影片生成領域的 diffusion model 成功啟發，研究者也嘗試將擴散機制搬到語言生成上——用「逐步破壞資訊、再反向還原」的方式取代逐 token 生成。

🧩 **從離散到連續，再從連續退回離散**

2021 年，multinomial diffusion、D3PM、SUNDAE 等研究率先把擴散機制離散化，以處理語言這種類別資料，藉此緩解自回歸因 teacher forcing 帶來的 exposure bias，以及在填空與受限生成任務上的侷限。

2022 年風向一轉：Diffusion-LM 提出改用連續嵌入向量（embedding）代表離散類別，讓原本為影像設計的高斯噪聲擴散機制可以直接套用在語言上，不需額外修改。此後短短數月內，DiffuSeq、SSD-LM、Difformer、SeqDiffuSeq、GENIE、LD4LG，以及作者本人參與的 self-conditioned embedding diffusion（SED）與 continuous diffusion for categorical data（CDCD）陸續問世，理由很簡單：連續方法能直接借用影像／影片擴散領域已經成熟的取樣與蒸餾工具鏈，這些工具在離散擴散上往往難以套用，甚至完全不可行。

📊 **一個關鍵數字：訓練效率差了 64 倍**

風向在 2023 年底急轉直下。2023 年 5 月，Gulrajani 與 Hashimoto 量化了以概似估計（likelihood-based）訓練的連續擴散語言模型 Plaid-1B 的訓練效率，結果是比自回歸基準線低 64 倍。在當時業界高度關注 Chinchilla-optimal（訓練運算量與困惑度的最佳平衡）的氛圍下，效率差距近兩個數量級的方法很難被認真看待。此後，幾乎所有新的擴散語言模型研究都轉向了離散方法。

💡 **作者的猜測：時機與心態的雙重轉變**

Sander Dieleman 認為原因難以確定，但提出兩個可能因素：其一是 ChatGPT 時刻讓整個研究社群的焦點從「理論優雅」轉向「追上甚至超越自回歸模型的實際效能」，而離散方法在概念上更接近自回歸，被認為更有機會補齊效能差距；其二是 LLaMA 在 2023 年 2 月才剛發布、開始主張把推論成本也納入考量，社群當時可能還沒真正消化這個典範轉移，因此仍以訓練效率作為評判標準，連續方法因而吃虧。他也坦言連續擴散原本具備逐 token 表達不確定性、以及可沿用豐富取樣工具的優勢，放棄這些特性在他看來可能是個錯誤，但整個研究社群顯然選擇了另一條路。

⚠️ **這段歷史敘述本身高度主觀**

作者多次強調，關於滅絕原因的推論「純屬推測」，也歡迎讀者提出不同意見；他自己在 2023 年後也已離開這個領域，是從旁觀察這段演變。

🎯 **實務啟示**

若連續擴散真的迎來復興，對工程師而言值得關注的是它原本被放棄的兩項特性：逐 token 的不確定性表達，以及可直接沿用影像／影片擴散領域成熟的取樣與加速技術。這意味著一旦效率差距被解決，連續方法在可控生成、填空任務上的潛力可能重新被重視。

🔗 **來源**
- 標題：Continuous Diffusion Language Models (CDLM's)
- 作者／機構：peter_d_sherman
- 連結：https://sander.ai/2026/08/24/continuous-dlms.html

#DiffusionModels #LanguageModels #DeepLearning #GenerativeAI #MachineLearning #NLP #Autoregressive #ContinuousDiffusion #AIResearch #DeepMind
