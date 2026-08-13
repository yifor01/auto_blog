---
title: Putting sign language AI into users’ hands
source: Google DeepMind
url: https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/
model: claude-code/sonnet
generated_at: '2026-08-13T07:25:58.803401'
pinned: true
---

📌 【Google DeepMind】讓 AI 看懂手語：SL2T 模型讓打字變成「用手就能說」

TL;DR：DeepMind 推出多語手語轉文字模型 SL2T，已在 Pixel 11 的 Gboard 與 Live Transcribe 上線，從 ASL 轉英文開始。

全球有超過 200 種手語、約 7,000 萬名聾人與聽損人士使用，但語音辨識與翻譯技術突飛猛進的這幾十年，手語幾乎沒有搭上這班車。Google DeepMind 在 8 月 12 日發布的文章中，介紹了他們口中「品質與泛化能力上的突破」：sign-language-to-text（SL2T）模型。

🤔 **手語翻譯比語音辨識難在哪**

文章指出手語翻譯有兩個核心挑戰。第一，語音轉文字本質上是同一語言內「聲音對應文字」的序列映射，但手語是擁有獨立文法與詞彙的自然語言，因此需要的是真正的機器翻譯，而非單純的手勢對詞彙轉換。第二，模型必須學會「看懂」肢體動作：手語透過手部、手臂、軀幹、頭部與臉部表情同時傳遞語意，要在高影格率下準確追蹤這些動作，是計算量龐大的電腦視覺任務。文章也提到，早期像「手語手套」這類方案之所以效果有限，正是因為手語不是「用手打的英文」，而是需要精細的全身視覺感知加上完整的語言翻譯能力。

🧩 **繞過 gloss 標註，直接從骨架點翻成文字**

為了保護使用者隱私，SL2T 不是直接處理原始攝影機畫面，而是先透過裝置端模型 MediaPipe Holistic 追蹤手語使用者身體上的座標點，只把這些幾何座標傳到伺服器做翻譯，原始影像可以立即捨棄。更關鍵的是，SL2T 直接把座標序列翻譯成文字，略過先前手語翻譯研究普遍採用的中介標註「gloss」。文章解釋，gloss 標註無法捕捉手語中非線性的元素，例如非手部標記（non-manual markers）與空間結構，直接從座標點翻譯則能去除人為的詞彙上限，讓翻譯品質可以隨資料量直接擴展。

📊 **超過 10 萬小時、50 種以上手語的訓練資料**

SL2T 的訓練資料涵蓋超過 100,000 小時、50 多種手語，其中約四分之一是美國手語（ASL）。DeepMind 表示，聯合多種語言、方言與不同熟練程度的資料一起訓練，能讓模型學到共通的底層結構，在他們的實驗中表現優於單一語言模型。在評估 ASL 轉英文品質的 FLEURS-ASL（sd-test）基準上，SL2T 達到 70 分的 zero-shot BLEURT 分數，文章形容這「明顯高於過去任何已公開的分數」。團隊也特別針對真實使用情境做了工程優化，包括降低串流延遲、避免對非手語輸入產生幻覺、確保對左撇子使用者（約佔手語使用者的一成）的公平性，以及改善單手比劃（另一手拿著手機時常見）的辨識表現。

⚠️ **仍會在罕見手勢與快速指拼上出錯**

DeepMind 也坦承目前模型的侷限：在罕見手語詞彙、快速指拼（fingerspelling，例如把「prey」誤譯成「grey」）、被動語態、classifier depiction（例如漏掉「claws」爪子的描述），以及缺乏上下文時的時態判斷上，仍會出現錯誤。

🎯 **從實驗室走進消費性產品**

SL2T 目前已實際應用在 Pixel 11 的 Gboard 手語輸入與 Live Transcribe，讓聾人使用者可以在任何原本要打字的地方改用手語輸入，例如搜尋網頁、撰寫訊息或文件，甚至對 Gemini 下指令；在 Live Transcribe 對話中也可以直接比手語回覆，而不必打字往返。DeepMind 表示這是手語 AI 首度被整合進消費性產品，未來會擴大到更多裝置與語言。文章也強調整個專案是與聾人社群共同打造，從概念發想、資料蒐集、使用者研究到成立 AI Sign Language Advisory Committee（AISLAC），都有聾人專家與全球聾人組織參與。

🔗 **來源**
- 標題：Putting sign language AI into users' hands
- 作者／機構：Google DeepMind
- 連結：https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/

#GoogleDeepMind #SignLanguageAI #ASL #Accessibility #SL2T #ComputerVision #MachineTranslation #DeafCommunity #Gboard #AIforGood
