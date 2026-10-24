---
title: Block’s new voice model sounds eerily human
source: TechCrunch AI
url: https://techcrunch.com/2026/10/24/blocks-new-voice-model-sounds-eerily-human/
model: claude-code/sonnet
generated_at: '2026-10-24T19:36:14.891230'
score: 85
---

📌 Jack Dorsey 旗下 Block 發布全雙工語音模型 Dessa，聲音「不像 AI」

TL;DR：Block 研究團隊推出可本地執行的全雙工語音模型 Dessa，標榜情感內建於語音本身而非文字驅動。

當多數語音 AI 還是靠文字轉語音加情緒標籤硬湊出「聽起來像人」的效果時，Block 這次直接宣稱自己做出了一個完全不經過文字管線、靠語音資料本身訓練出情感的模型。

🤔 **問題出在哪：語音被先轉成文字，情緒就丟光了**

Block 在部落格文章中指出，現有語音 AI 的痛點在於會先把使用者的聲音轉成文字，而文字本身無法承載語氣、情緒等大量資訊，導致「最強的 AI 聽不出你的感受」。他們認為這不只讓體驗變差，甚至可能有風險。相較之下，市面上像 ElevenLabs v4 或 Fish Audio Drama 3 等模型多是用「語音標籤（voice tags）」去驅動情緒生成，而 Block 強調 Dessa 的情緒是模型本身內建的，但報導也提到目前並不清楚這種情緒表現是否仍是由某種標籤機制在背後引導。

🧩 **全雙工架構與訓練方式**

根據公司說法，Dessa 是一個全雙工（full-duplex）語音模型，可以同時說話與聆聽，概念上類似 OpenAI 今年早些時候推出的 GPT-Live。Dessa 完全以人類語音資料訓練，並且只用了單一組 NVIDIA GPU rack。值得注意的是，一般語音模型通常會搭配一個大型語言模型做知識檢索，但 Block 表示 Dessa 的知識來源就是它所訓練的對話資料本身。公司展示了多段對話範例，包括模型表示自己工作很累時聲音聽起來真的疲憊，以及在互動中聲音變得情緒化、幾乎語帶哽咽的片段。

📊 **目前狀態：可在消費級硬體跑，但不公開**

Block 表示 Dessa 可以在如 MacBook M4 Max 等消費級電腦上本地執行。不過目前沒有公開存取管道，公司已發出徵求安全研究人員測試模型的呼籲，報導推測這可能是為了測試語音 Agent 是否會被用來欺騙對話另一端的人。

💡 **為什麼是 Block 在做這件事**

Block 的主業是金融與中小企業解決方案，旗下 Square 已經在用語音 AI 處理點餐等場景。擁有自家可本地執行的語音模型，意味著 Block 未來能以更低成本把語音體驗整合進更多商業與消費應用中。

🎯 **實務啟示**

對語音 AI 開發者而言，Dessa 釋出的訊號值得關注：全雙工、無文字中介的語音模型若真能在單機 GPU rack 規模訓練出自然情感表現，可能代表語音互動體驗的下一個門檻不在模型規模，而在訓練資料與架構設計；但在沒有公開存取與技術細節的情況下，目前只能從公司描述與展示片段做初步判斷。

🔗 **來源**
- 標題：Block's new voice model sounds eerily human
- 作者／機構：Ivan Mehta, TechCrunch AI
- 連結：https://techcrunch.com/2026/10/24/blocks-new-voice-model-sounds-eerily-human/

#VoiceAI #SpeechModel #FullDuplex #Block #Dessa #OnDeviceAI #ConversationalAI #JackDorsey #SpeechToSpeech #AIProduct
