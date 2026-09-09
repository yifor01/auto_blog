---
title: Recreating a 70-year love story frame by frame
source: Google AI Blog
url: https://blog.google/innovation-and-ai/technology/ai/love-rendered-film/
model: claude-code/sonnet
generated_at: '2026-09-09T19:53:52.347431'
pinned: true
---

📌 DeepMind 用 AI 幫失智老人「補拍」70 年前初遇畫面

TL;DR：Google DeepMind 與導演團隊用影像修復加表演捕捉技術，重建一對老夫妻從未被記錄下的初遇記憶。

有些記憶從來沒被拍下來，卻真實存在腦中七十年。當失智症逐漸奪走這段記憶，AI 能不能把它「還原」出來？

🤔 一段沒有照片的記憶，如何重建？

紀錄短片《Love, Rendered》記錄了結婚超過 70 年的 Burt 與 Ethelle Shatz 夫婦。隨著 Burt 認知能力衰退，他逐漸遺忘的記憶之一，是兩人在 Cleveland 一間學生合作社初次相遇的那一天。因為那天沒有被拍照或錄影，這段記憶只存在他們的腦海裡。素材提到，這部片由奧斯卡提名導演 Liz Garbus 執導，Dan Cogan 與 Darren Aronofsky 共同製作，由 Google DeepMind 與 Aronofsky 的創意工作室 Primordial Soup 合作完成。

🧩 兩項技術疊加：影像修復 + 表演捕捉

技術團隊採用兩階段做法：

- 影像修復（image restoration）：用生成式模型修復 Burt 與 Ethelle 年輕時的黑白照片，確保後續重建的畫面忠實呈現原本樣貌。
- 姿態與表演控制（pose and performance control）：工程師用 performance capture（表演捕捉）模型，把兩人「現在」的細微舉止，像是 Burt 頭部傾斜的角度、說話時短暫的停頓、眼角的細紋，映射到他們年輕時的樣貌上。

素材指出，這兩種技術結合，讓團隊得以把 Burt 與 Ethelle 的「過去」與「現在」交織在一起，生成一段他們表示「感覺真實」的記憶畫面。過程中，Ethelle 本人也擔任共同創作者的角色，親自校正樓梯的曲線、鞋跟的形狀等細節，確保還原結果忠於事實。

💡 從 reminiscence therapy 到生成式工具

素材提到，這個專案的靈感來自導演們對記憶韌性的長期觀察：Liz Garbus 曾在紀錄片《Coma》中看到病人聽到熟悉聲音時 fMRI 掃描出現反應；Darren Aronofsky 也接觸過患有阿茲海默症的芭蕾舞者，聽到《天鵝湖》音樂時，仍能從輪椅上跳出當年的舞步。這些經驗把團隊帶向 reminiscence therapy（懷舊療法），一種利用歌曲、家族故事、老照片等感官線索來刺激記憶、促進對話的臨床做法。但這次的挑戰在於：如果一段記憶根本沒有對應的感官線索，生成式工具是否能補上這個缺口。

🎯 你也能用 Gemini App 修復自己的家庭照片

負責技術的 Google DeepMind 工程師 Michael Chang 在文中提到，他也用同樣的影像修復技術測試了自己父母年輕時相遇的老照片，並用影片模型讓照片「動」起來，這個經驗讓他更直觀感受到這類工具如何幫助留住正在流逝的記憶。素材指出，一般使用者也可以在 Gemini app 中上傳老照片，並詢問：「Can you restore and colorize this photo? Preserve the appearance, expression, and pose of the people.」即可取得修復與上色後的照片。

⚠️ 侷限

素材並未說明影像修復與表演捕捉模型的具體架構、訓練資料或評估方式，這部分細節僅止於「使用生成式模型」與「performance capture 模型」的描述，無法進一步展開技術內容。

🎯 實務啟示

這個案例展現生成式 AI 在「情感修復」而非單純內容生成場景的應用潛力：當團隊把技術定位為「由人類主導、AI 輔助」的工具（如 Aronofsky 所說，工具本身不會做任何事，除非被人手引導），反而更容易在敏感題材上取得使用者信任。對於做多模態生成應用的工程師，這也是把影像修復與姿態/表演映射結合、產出具情感真實性內容的參考案例。

🔗 來源
- 標題：Recreating a 70-year love story frame by frame
- 作者／機構：Google — Michael Chang
- 連結：https://blog.google/innovation-and-ai/technology/ai/love-rendered-film/

#GoogleDeepMind #GenerativeAI #ImageRestoration #PerformanceCapture #AIForGood #Gemini #Documentary #DigitalMemory #ComputerVision #AIatWork
