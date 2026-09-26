---
title: I created an interactive digital avatar of myself — and you can talk to it
source: TechCrunch AI
url: https://techcrunch.com/2026/09/26/i-created-an-interactive-digital-avatar-of-myself-and-you-can-talk-to-it/
model: claude-code/sonnet
generated_at: '2026-09-26T20:03:41.149825'
score: 43
---

📌 記者打造自己的AI分身：拆解互動虛擬人的技術串接

TL;DR：TechCrunch 記者體驗 Synthesia 打造的個人互動分身，揭露語音、語言、影像模型如何串成一套對話系統。

一位公關人員在會議上問記者是否介意收到 AI 生成的新聞稿。第二天，這位記者就見到了公關人員自己的 AI 互動分身，能回答關於公司業務的常見問題。她形容這是「AI 用在公關上的終極形態」，而接下來，她自己也成為了下一個實驗對象。

🤔 一家估值 40 億美元的虛擬人公司

Synthesia 是一家以影片生成起家的虛擬人新創公司,同類競爭者包括 D-ID、HeyGen 與 Colossyan。今年初它的估值來到 40 億美元，去年營收（ARR）已突破 1 億美元。Synthesia 讓企業用 AI 虛擬人製作訓練影片，也推出了名為 Roleplay Sessions 的產品,讓員工可以與互動式 AI 虛擬人練習銷售話術,並由系統給出評分。

🧩 一段兩分鐘錄音，換來一個會對話的分身

記者受邀在 Synthesia 紐約新辦公室內的小型攝影棚拍攝多張照片,並錄製兩分鐘的語音樣本，簽署同意書後,團隊花了幾天時間為她打造出四種版本的分身：兩種是「一般版」（只會朗讀給定的腳本，分別戴眼鏡與不戴眼鏡），另外兩種是「互動版」（能聽、能回答，同樣分兩個版本）。

互動分身背後的技術流程可以拆解成四步：
1. 語音轉文字模型，將使用者說的話轉成文字。
2. 具備代理能力的語言模型，理解文字內容並判斷該採取的回應或行動。
3. 文字轉語音模型，把回應轉成語音。
4. Synthesia 自研的影像模型，讓虛擬人隨著語音同步做出對嘴與動作。

Synthesia 表示，語音與影像模型可以替換成自家以外的選項，例如 Cartesia、ElevenLabs、Google 或 OpenAI 的模型，企業客戶也能選擇自建雲端主機，或付費交由 Synthesia 代管。整套產品線分為三類：一般的影片製作與發佈平臺、Roleplay Sessions 這類互動代理平臺，以及讓客戶自行串接影像與語音模型的 API 平臺。

📊 「決定性」的分身：只回答訓練過的內容

這次記者的互動分身被限定只訓練回答她所寫的一篇關於創投背景的新創公司詐欺率報導,屬於「決定性（deterministic）」型態，也就是只會針對訓練範圍內的內容作答。記者的父母試圖詢問「只有他們知道」的私人問題，模型都沒有回應，而是反覆導回那篇報導；她的母親則稱這個分身「amazing」。

⚠️ 聲音相似度普通，且無法臨場發揮

記者身邊的非科技圈朋友認為互動分身的聲音不太像她本人，相似度不如朗讀腳本的一般版分身。由於是決定性系統，這個分身永遠不會臨場說出訓練範圍外的新內容——記者形容自己看著分身說完話後陷入沉默，彷彿在等它眨眼、微笑，或做出某種「知道自己是誰」的回應，但那從未發生。她也提到，如果換成非決定性、由聊天機器人自由生成回應的版本，使用者反而更容易陷入某種「AI 心理依附」的狀態。

🎯 對工程師的實務啟示

這個案例展示了一種務實的產品設計選擇：把互動代理限定在單一資料來源、單一決定性回答範圍內，能有效避免模型「亂講話」的風險，特別適合客服、公關問答、企業培訓等需要可控輸出的場景。如果你正在設計企業級對話代理，「限定領域＋決定性回應」可能比追求開放式生成更適合正式對外場合。

🔗 來源
- 標題：I created an interactive digital avatar of myself — and you can talk to it
- 作者／機構：Dominic-Madori Davis, TechCrunch AI
- 連結：https://techcrunch.com/2026/09/26/i-created-an-interactive-digital-avatar-of-myself-and-you-can-talk-to-it/

#DigitalAvatar #Synthesia #AIAgent #VoiceAI #TextToSpeech #VideoGeneration #ConversationalAI #EnterpriseAI #DigitalTwin #AIinPR
