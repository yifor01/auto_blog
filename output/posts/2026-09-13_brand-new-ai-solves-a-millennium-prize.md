---
title: Brand New AI Solves a Millennium Prize
source: Don't Worry About the Vase
url: https://thezvi.wordpress.com/2026/09/13/brand-new-ai-solves-a-millennium-prize/
model: claude-code/sonnet
generated_at: '2026-09-13T19:34:46.815181'
score: 92
---

📌 一場 AI 解千禧年難題引爆的署名羅生門

TL;DR：AI 助攻攻克 Navier-Stokes 相關難題，卻在掛名與功勞上鬧翻。

千禧年七大難題之一終於出現重大突破，這原本該是一則純粹振奮人心的 AI 科研進展新聞。但如果你以為故事到「AI 解出難題」就結束了，那才剛開始，Zvi 這篇文章形容這是「典型的星期二」：三個故事疊在一起，第一個故事遠比第二個重要，第二個又遠比第三個重要，但三個都值得說。

🤔 **眼睛盯著最重要的那件事：AI 真的解出了難題**

故事從 Tristan Buckmaster 與 Levent Alpoge 一年的工作成果說起，他們拿出一系列結果：對不可壓縮多孔介質方程（incompressible porous media）、Boussinesq 方程、以及三維不可壓縮 Euler 方程，證出帶平滑外力（smooth forcing）的有限時間 blowup；他們也相信自己拿到了 hypo-dissipative Navier-Stokes 的 blowup，只是 Lean 形式化驗證尚未完成。Buckmaster 說明，這個研究方向的基本構想並非他們提出，功勞應歸於 Diego Cordoba 與 Luis Martínez-Zoroa，兩人多年來探索帶外力 blowup 的建構方式；他們是把 Cordoba 與 Martínez-Zoroa 針對粗糙外力（rough forcing）的成果，在大量 LLM 協助下推進到平滑外力與 Euler 方程。Buckmaster 甚至公開表示，就這整套工作而言，他認為 Martínez-Zoroa 值得一座費爾茲獎。唯一美中不足的是，他們自認被迫提早發表，沒有時間把證明打磨到數學家習慣的可讀程度，Buckmaster 甚至把 Euler 那篇寫法自嘲比作「AI 產出的垃圾文字」。

📊 **OpenAI 88 小時、2.7 百萬則訊息，正面硬幹整條難題**

9 月 1 日，OpenAI 聽到一個（後來證實為假的）傳聞，說有兩個千禧年難題已被解開。為了不讓別人搶先，OpenAI 動用了一個比 Astra 更強的內部模型，花費數百萬美元的推論成本，把所有尚未解決的千禧年難題全部掃過一遍，並在 88 小時內攻克整個 Navier-Stokes 問題，外加 17 小時讓 Astra 完成 Lean 形式化與驗證。根據 OpenAI 公布的數字，在所有嘗試過的難題上，Agent 總共發送了 490 萬則訊息，用掉約 3,000 億個輸出 token；光是 Navier-Stokes 這一題，就用了 270 萬則訊息、約 1,300 億個輸出 token。以一般客戶計費估算，這相當於約 2,200 萬美元，若只算內部邊際成本則是數百萬美元。OpenAI 的 roon 在社群上打趣說「一年後同等的 Agent swarm 大概只要一塊半」，Sam Altman 則諷刺回應「AI 真是泡沫，聽說他們在虧本賣 token，他們知道這東西只值一百萬美元嗎」。OpenAI 表示無意領取獎金，文章直言：「這從來就不是為了獎金，對任何人來說都是，這一直是關於功勞歸屬。」

💡 **署名之爭：誰該掛名，誰被要求下車**

Buckmaster 在聽到傳聞後主動聯繫 OpenAI，據他轉述，OpenAI 的 Sebastien Bubeck 表示內部模型在過去幾天內完成了 forced Navier-Stokes 有限時間 blowup 的證明；經過兩通電話，Buckmaster 稱自己一開始被誤導了，其實是整個團隊動用了他形容為「瘋狂」的算力（也就是那 1,300 億到 3,000 億輸出 token）。OpenAI 提出兩個方案：一是他們發布 Euler 結果，OpenAI 隔天發布 Navier-Stokes 結果；二是由 Buckmaster 獨自撰寫 Navier-Stokes 論文並註明是內部模型解出的。但 Bubeck 兩度要求把 Levent 從作者名單移除，理由包括「很煩人」的一點是 Levent 任職於 Anthropic；如果 OpenAI 在他們之後發布，會表示 Buckmaster 和 Alpoge「應得 Clay 獎」、是「最接近答案的人類」。Buckmaster 拒絕了兩個方案，並表示若 OpenAI 照原計畫發布，他會公開這整段過程，得到的回應是：「你為什麼要毀掉自己的職涯？」他澄清自己是學術界人士，反問為何公開這件事會毀掉職涯，對方回答：「如果你不想要我客氣，那我也可以不客氣。」Buckmaster 特別聲明，自己沒有看過 OpenAI 的證明，不知道他們的模型做了什麼、怎麼做的，也不知道自己的資料是否被使用，他不是在指控任何人，只是在陳述自己被告知的內容、時間與提議。Levent Alpoge 則有不同的敘事角度：他對 OpenAI 坦承「不能排除我們產品使用中去識別化的資料，可能被用來改進他們的模型」一事表示「這樣直接認了也算給他們加分」，並提到 OpenAI 的證明看起來更像他們手上另一版 Euler blowup 證明的思路，還開玩笑說當初他們把某個猜想暱稱為「smooth criminale」；他表示自己其實很樂意合作，不在乎作者排名，但聽到走廊裡討論「只要把他從論文移除就給千禧年獎金」的對話後，就明白局勢已經定了，還笑稱自己這邊的工作「大部分就是我跟 Claude 在角落裡瞎玩」而非機構行為。Bubeck 則反駁：「什麼都沒有被鎖定，我們只是願意談，但你沒有找我們談⋯我們願意做得更多、盡可能多談以達成共識。」

⚠️ **各說各話，仍有待查證**

值得留意的是，這整段對話目前僅有當事人各自的說法，Buckmaster 本人也主動聲明他沒有看過 OpenAI 的證明、不確定其模型的運作方式，也不確定己方資料是否被用到，文章呈現的是雙方各自的敘述，而非已核實的事實。

🎯 **實務啟示**

這起事件提醒從事 AI 輔助科研的工程師與研究者：當大型實驗室能在數十小時內投入百億級 token 的推論成本去「搶時間」，速度已經不再是稀缺資源，稀缺的會是「誰先說出來、以什麼方式署名」，這也讓跨機構協作前先把資料使用、掛名規則講清楚，變得比以往更重要。

🔗 **來源**
- 標題：Brand New AI Solves a Millennium Prize
- 作者／機構：TheZvi，Don't Worry About the Vase
- 連結：https://thezvi.wordpress.com/2026/09/13/brand-new-ai-solves-a-millennium-prize/

#OpenAI #Anthropic #MillenniumPrize #NavierStokes #AIforMath #LeanProver #AIResearch #Astra #MathAI #AIControversy
