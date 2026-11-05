---
title: 'OpenAI Launches GPT-Image-2.6 Flare and Sunburst: Adds GIFs, SVG Export and
  6-Second API Generation'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/04/openai-gpt-image-2-6-flare-sunburst/
model: claude-code/sonnet
generated_at: '2026-11-05T23:09:04.879620'
score: 79
---

📌 OpenAI推出GPT-Image-2.6:Flare、Sunburst雙模型,6秒出圖還能輸出GIF與SVG

TL;DR:OpenAI的GPT-Image-2.6把出圖速度提升50%,新增GIF、SVG輸出與markup編輯,API模型拆成Flare與Sunburst兩款。

當你的產品團隊還在等一張圖渲染完成,OpenAI宣布旗下新模型最快6秒就能出圖,而且畫質設定拉高也不用額外付費。這次升級橫跨ChatGPT、Codex與API,核心是全新的GPT-Image-2.6模型家族。

🤔 背景:影像生成已經是日常工作流程的一部分

OpenAI表示,目前ChatGPT與API加總每週生成超過40億張圖片,平均每天超過5億張,相較8週前Images 2.5推出時的每週30億張明顯成長。這個量級的使用,讓出圖速度與輸出格式的細節開始變得和模型品質一樣重要。

🧩 架構:兩款模型分工,一個參數決定模型「想多久才畫」

GPT-Image-2.6是OpenAI在API上的影像生成與編輯模型家族,接受文字與圖片輸入、輸出圖片。Flare主打快速迭代與互動工作流程,OpenAI表示在quality設為low時最快6秒就能出圖;Sunburst則主打細緻構圖與編輯一致性,在medium或high品質下表現更穩定。

這次新增的complexity參數,決定模型渲染前要規劃多少,分成low、medium、high三個等級,若省略則兩款模型都預設high。官方指南建議:做局部編輯(例如改背景、改招牌文字)用low就好;處理密集文字、複雜版面或物件之間的關係則適合high,但OpenAI也提醒,複雜度拉高會增加延遲,還可能帶入非預期的變化。complexity與控制渲染細節的quality是分開的參數,調整complexity本身不會額外收費。

另外還加入了markup-guided edits,讓使用者直接標出想修改的確切區域;官方發布文章說markup功能「即將開放給API」,但技術指南已經把這項功能列為兩款模型都支援。輸出端則新增SVG與動態GIF:ChatGPT使用者可以把一段prompt或一張照片變成動畫GIF,調整播放速度、編輯單一畫面再分享;SVG輸出則讓icon、圖表、UI素材能無損縮放,省掉後製步驟。使用者也可以在ChatGPT裡儲存並標記人物、寵物、角色的參考圖,之後重複使用不用再上傳。

📊 定價:token計價,但和競品比起來不夠透明

Flare與Sunburst採相同的token計價方式。對照同業,Google的Nano Banana 2.1每1K張圖從0.0336美元起、4K時漲到0.113美元;BFL的FLUX 3 Image每1K張圖從0.048美元起、4K時到0.607美元,其開放權重版本FLUX 3 Image Klein甚至能在RTX 3090這類消費級GPU上跑。相較之下,OpenAI的優勢是原生支援GIF與SVG輸出,但缺口在於沒有公開每張圖的實際成本與對應品質,開發者得自己用token換算。

🎯 實務啟示

如果產品需要icon、圖表這類必須無損縮放的素材,SVG輸出可以直接省掉一道後製;如果是社群或產品demo需要動畫素材,GIF輸出省掉額外串接動畫工具的麻煩。但在導入前,建議先用小量token實測換算出實際每張圖成本,因為OpenAI目前沒有像Google、BFL那樣公開逐檔計價,直接套用token單價估算容易失準。

🔗 來源
- 標題:OpenAI Launches GPT-Image-2.6 Flare and Sunburst: Adds GIFs, SVG Export and 6-Second API Generation
- 作者／機構:Asif Razzaq, MarkTechPost
- 連結:https://www.marktechpost.com/2026/11/04/openai-gpt-image-2-6-flare-sunburst/

#OpenAI #GPTImage #ImageGeneration #GenerativeAI #DeveloperTools #SVG #ComputerVision #AIImageTools #ChatGPT #APIUpdate
