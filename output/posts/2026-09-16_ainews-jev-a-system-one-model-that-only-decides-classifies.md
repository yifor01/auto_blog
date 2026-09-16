---
title: '[AINews] Jev: a “System One Model” that only decides/classifies/routes/scores
  — >100x faster, >200x cheaper than small frontier LLMs'
source: Latent Space
url: https://www.latent.space/p/ainews-jev-a-system-one-model-that
model: claude-code/sonnet
generated_at: '2026-09-16T20:20:47.149567'
score: 90
---

📌 不推理、不寫程式碼的「System One」模型：Jev主打決策比LLM快百倍

TL;DR：TypeSafe發布Jev，一款專做分類、路由、評分決策的模型，宣稱比小型前沿LLM快20到200倍。

在一個Gemini 3.8 Live與Periodic Labs都有重大發表的日子裡，一個「不會寫程式、也不會推理」的模型，卻整天霸佔Hacker News首頁。這聽起來反直覺，但這正是TypeSafe想做的事：不是取代會思考的LLM，而是接手那些根本不需要思考的決策工作。

🤔 **System One，而非取代System Two**

TypeSafe創辦人Diogo Almeida把Jev定位成「System One模型」，用來補完速度較慢、擅長推理的「System Two」LLM。概念上很直白：如果一個任務只是分類、打分、選路徑，你並不需要一個會生成連續字串、會胡言亂語的自迴歸模型，你需要的是一個又快又準的決策器。

🧩 **用RLCD訓練出「校準過的決策」**

Jev是透過TypeSafe稱為RLCD（calibrated decisions）的方法訓練，目標是拿掉傳統LLM decoding過程中的三個痛點：一是可以平行取樣（parallel sampling），二是宣稱「無幻覺」，三是輸出經過校準（calibration），也就是模型給出的信心分數真的可信。這也呼應了HuggingFace研究者Clementine近期點出的研究前沿：校準決策（calibrated decisions）。

📊 **宣稱快20到200倍、便宜40到400倍**

根據TypeSafe公布的部落格與評測，Jev號稱比小型前沿LLM快20到200倍、成本低40到400倍，而且輸出token免費。這款發表在HN上獲得極高討論度，官方部落格、評測與文件加總已累積數百萬次瀏覽，此前也曾在AI Engineer的pre-launch場合先行預覽。

💡 **業界怎麼解讀：分類器、Judge、路由policy的便宜替代品**

多位工程師的第一反應都指向同一個使用情境：用Jev取代LLM在生產環境中擔任結構化分類器（classifier）、評審（judge）或路由policy，這些場景本來就不需要自迴歸生成的開銷。也有人把它類比為DSPy風格的typed signature／typed prediction抽象，暗示未來的架構可能是：把昂貴的LLM呼叫拆解、編譯成一堆小型、專門任務的AI函式，只在真正需要生成自由文字時才呼叫大模型。

⚠️ **它不是通用語言模型**

社群也有清醒的反面意見：Jev並非通用語言模型，行為更接近一個受限（constrained）或diffusion-like的決策模型，無法產生自由格式的文字，必須搭配預先定義好的輸出格式使用。正確的心智模型不是「GPT替代品」，而是「一個便宜、校準過的決策推論引擎」。

🎯 **實務啟示**

如果你的產線裡有大量LLM呼叫其實只是在做分類、打分或路由這類固定輸出格式的工作，這類「System One」決策模型可能是值得評估的成本最佳化方向；但別指望它處理需要自由文字生成或開放式推理的任務。

🔗 **來源**
- 標題：[AINews] Jev: a "System One Model" that only decides/classifies/routes/scores — >100x faster, >200x cheaper than small frontier LLMs
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-jev-a-system-one-model-that

#AI #MachineLearning #LLM #TypeSafe #ModelInference #Classification #AIAgents #DSPy #RLCD #AIInfrastructure
