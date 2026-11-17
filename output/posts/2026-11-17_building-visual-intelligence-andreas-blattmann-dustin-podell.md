---
title: Building Visual Intelligence — Andreas Blattmann & Dustin Podell, Black Forest
  Labs
source: Latent Space
url: https://latent.space/p/bfl/
model: claude-code/sonnet
generated_at: '2026-11-17T01:03:12.515300'
score: 92
---

📌 從靜態圖到會動又會響：BFL 讓 FLUX 3 一次學影像、影片和聲音

TL;DR：Black Forest Labs 用影像、影片、聲音三種訊號一起訓練 FLUX 3，想教模型學會「視覺智慧」而非只生成好看的單張圖。

有人把球丟向你，手在球還沒抵達之前就已經開始移動，這種反應沒辦法寫成一條軌跡公式，卻是每個人都具備的能力。在 Latent Space 這集訪談裡，Black Forest Labs（BFL）共同創辦人 Andreas Blattmann 用這個例子解釋他口中的「視覺智慧」(visual intelligence) 到底是什麼，也順勢說明了 FLUX 3 為什麼要同時吃進影像、影片、聲音三種訊號。

🤔 從 Stable Diffusion 到自立門戶

Andreas Blattmann 是 Stable Diffusion 的共同創造者，也是其背後 latent diffusion 方法的共同發明人；另一位主角 Dustin Podell 曾主導 FLUX Kontext、並是 SDXL 的第一作者。兩人都出身 Stability AI 的影像生成團隊。Stability AI 後來分崩離析，核心團隊在 Anj Midha 協助下獨立出來成立 BFL，隨即推出了廣受關注的 FLUX 系列模型。

🧩 一張靜態圖告訴你球在哪裡，一段影片告訴你它怎麼飛過來的

Andreas 的論點是：靜態影像只能呈現「球在哪裡」這個瞬間，影片才能呈現「球是怎麼飛過來的」這個過程；而聲音則能告訴你物體何時撞上了什麼，即便鏡頭根本沒拍到接觸的那一刻。這正是 BFL 把三種訊號放在一起訓練 FLUX 3 的理由，如果只盯著單一畫面是否「好看」，其實測不出模型到底理解了多少東西。節目開場展示的「奔馬」範例，以及 FLUX 3 Video 的音效示範，都是用來驗證這個想法的具體成果。

Andreas 進一步舉例：如果攝影機從一個人的正面開始繞到背後拍，模型在某個時間點就必須合理地補出這個人後腦勺的樣子。他認為一般的二維影片其實已經隱含了大量「物體從其他角度看起來是什麼樣子」的證據。這不代表模型真的「理解物理」，這點兩人在訪談中來回辯論，沒有給出定論，但比起只問「這一張畫面是否真實」，這確實是更好的測試方式。

💡 把每一格畫面修得更漂亮，播放起來卻會閃爆

訪談裡有個很具體的工程案例：如果把一段影片的每一格畫面分別拿去做銳化處理，單獨看每一張可能都很漂亮，但按下播放鍵之後，多出來的細節卻會不斷閃爍抖動，因為放大演算法在每一格都做出了稍微不同的決定。BFL 的解法是讓影片升頻器（upscaler）直接從同一套 FLUX 3 骨幹衍生而來，即使使用者要的只是一個解析度更高的檔案，時間軸上的一致性仍然至關重要。

自回歸（autoregression）是不是正在吃掉影像生成？Andreas 替另一邊說話：自回歸模型的優勢是能一次從訓練樣本裡的所有 token 學習，而擴散模型這邊，團隊則可以把一條很長的取樣過程蒸餾成幾個步驟就完成。哪種優勢更重要，取決於你在意的是訓練成本，還是使用者等待一張圖算完的時間。

🎯 從「狗戴帽子」的直覺，到花幾個月補齊資料與模型

Dustin Podell 分享了 Kontext 專案最早的實驗：他猜測，一個會畫「狗戴帽子」的影像模型，應該已經隱含知道帽子該戴在哪個位置。他和同事收集了一小批標註了「物件關係」的照片，訓練了幾個小時，就讓模型學會把一個 logo 貼到一件 T-shirt 上，結果很粗糙，但已經足以說服團隊在下一次內部會議上投入資源。接下來，團隊花了好幾個月去打磨資料與模型本身。

訪談後段提到一個讓 Dustin 自己都沒預料到的使用案例：有使用者把家裡老舊、已經損壞的家族合照丟進 FLUX，修復完之後拿給家人看。在整場討論「如何在編輯、甚至跨畫面之間保留一個人的身分特徵」之後，這是一個很能說明「誰會真正在意你有沒有做對」的例子。

🎯 實務啟示

對做影像／影片生成的工程師來說，這集訪談點出了一個容易被忽略的評測盲點：只看單張畫面是否逼真，測不出模型對運動與因果的理解；如果你的產品牽涉到放大、修復或跨畫面編輯，時間軸上的一致性可能比單格畫質更值得優先投資。

🔗 來源
- 標題：Building Visual Intelligence — Andreas Blattmann & Dustin Podell, Black Forest Labs
- 作者／機構：Latent Space
- 連結：https://latent.space/p/bfl/

#FLUX3 #BlackForestLabs #StableDiffusion #LatentDiffusion #VideoGeneration #GenerativeAI #ImageGeneration #DiffusionModels #AIResearch #Multimodal
