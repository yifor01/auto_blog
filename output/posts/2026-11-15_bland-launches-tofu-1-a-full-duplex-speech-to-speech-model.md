---
title: Bland Launches Tofu-1, a Full-Duplex Speech-to-Speech Model for Calls
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/15/bland-tofu-1-full-duplex-speech-to-speech-model/
model: claude-code/sonnet
generated_at: '2026-11-15T21:51:32.288288'
score: 72
---

📌 Bland Tofu-1：不轉文字稿的全雙工通話語音模型

TL;DR：Bland 發布語音對語音模型 Tofu-1 研究預覽,邊聽邊想邊答,電話客服系統少了一道轉文字環節。

多數語音助理其實是「接力賽」：先把語音轉文字,丟給語言模型,再把回覆轉回語音。這個過程中,語氣、停頓、背景聲音這些訊息,往往在轉文字的那一刻就消失了。Bland 這次要解決的,正是這個問題。

🤔 語音級聯架構的盲點

根據 MarkTechPost 報導,舊式語音代理的串接架構（speech-to-text → LLM → text-to-speech）會丟失語氣、猶豫與背景聲音等訊息。Bland 的 Tofu-1 直接處理音訊輸入,讓這些訊息在模型推理過程中保留下來。

🧩 全雙工、三種音訊技能,但架構未公開

Tofu-1 是「全雙工」(full-duplex)模型,代表它可以邊說話邊聽,並在說話的同時進行推理。Bland 在產品頁列出三項音訊技能,其中提到使用者可以在 Tofu-1 說話中途打斷或糾正它,而它會在繼續處理請求的同時維持對話進行,只在工作真正完成時才回報結果,不會提前宣稱任務完成。報導也指出,Bland 並未公開 Tofu-1 的內部架構細節。

因為 Tofu-1 直接建模「通話的聲音」本身,它也能夠產生通話場景,包括第二個說話者、房間環境音與線路雜訊,這也是其所謂「TV Test」測試的設計基礎：測試模型能否在電視音量通常比來電者更大聲的情況下,仍然專注跟隨來電者的語音、忽略背景電視的聲音。

📊 benchmark 要小心解讀

MarkTechPost 特別提醒,Bland 標註其 TV Test 演示為「示意性質」,並非實際錄製的模型輸出；競品數據則來自各廠商自己的官網,而 FDB（full-duplex benchmark）的結果因為各家使用不同版本,彼此之間並不能直接比較。這些提醒本身就說明,目前公開的這些數字還不是獨立、可直接比較的評測結果。

Tofu-1 的設定場景也很具體：行駛中的車輛、醫院病房、訊號不穩的電話線路。目標產業則鎖定銀行、醫療、保險與政府部門,而研究預覽的申請表單會詢問企業每月通話量,從低於 1,000 通到 5 萬通以上都有對應選項。

⚠️ 仍是研究預覽,架構細節全缺

目前 Tofu-1 只開放給有限數量的企業做研究預覽,沒有公開的內部架構說明,所有效能比較也都附帶「不可直接比較」的但書。

🎯 實務啟示

對做電話代理（phone agent）的團隊來說,Tofu-1 代表的方向值得關注：用單一模型直接吃音訊、吐音訊,省掉文字稿這個中間層,理論上能保留更多語氣與情境訊息。但在架構未公開、benchmark 又明確標註為「示意」或「不可比較」的現況下,評估時應該以自己場景的實測為主,而不是直接採信官方頁面上的數字。

🔗 來源
- 標題：Bland Launches Tofu-1, a Full-Duplex Speech-to-Speech Model for Calls
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/15/bland-tofu-1-full-duplex-speech-to-speech-model/

#SpeechToSpeech #VoiceAI #FullDuplex #Bland #ConversationalAI #PhoneAgent #AIResearch #SpeechRecognition #VoiceAgent #AIProduct
