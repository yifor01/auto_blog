---
title: Nvidia’s AI advantage is moving beyond the GPU
source: TechCrunch AI
url: https://techcrunch.com/2026/08/29/nvidias-ai-advantage-is-moving-beyond-the-gpu/
model: claude-code/sonnet
generated_at: '2026-08-30T10:58:36.302464'
score: 57
---

📌 Nvidia的護城河，正從GPU本身移到整個機櫃

TL;DR：財報後市場發現，Nvidia的優勢已從單顆GPU擴大到整套資料中心編排系統。

過去大家擔心的故事是：超大規模業者陸續自研晶片，Nvidia的GPU霸權正被一點點蠶食。但這週財報公布後，投資人開始意識到一件事：Nvidia真正難以複製的優勢，可能根本不只在GPU裡。

🤔 從GPU競爭焦慮，到系統編排的新戰場

2023年初到2025年中，Nvidia市值成長10倍，但過去一年股價成長趨緩，主因是市場對GPU競爭的疑慮。隨著AI運算規模邁向gigawatt等級，把巨型資料中心維持在效率高峰運作，變成一項越來越複雜的任務。即便運算力常被視為一種商品，實際操作大型資料中心、讓部署規模越做越大、速度越來越快的同時仍保持效率，依然十分困難，而這正是Nvidia已經投入建置相關硬體的領域。

🧩 一整個機櫃，而不只是一顆GPU

Nvidia目前正在推出的Vera Rubin架構，把Rubin GPU搭配一整組其他單元銷售，包括Vera CPU、Groq 3 LPX推論加速器，以及對應的儲存與網路機櫃。這些系統高度專用，但作用不是處理更多token，而是確保GPU以外的一切環節盡可能有效率地運作——如果說GPU是引擎，這些就是車子的其餘部分。其中Vera CPU專門處理資料的編排問題。Nvidia storage技術副總裁Jason Hardy指出，單一伺服器或運算平臺能塞的記憶體終究有限，即使記憶體容量持續擴大，要在對的時間把資料送到GPU手上並不簡單。

📊 3倍效能提升的說法

Hardy表示，在這類資料搬運與排程操作上，Vera CPU帶來「upwards of 3x」的效能提升，讓flash儲存的效能得以完全發揮，而不會被資料搬運卡住（bottleneck）。

💡 兩種不同路線，同一個邏輯

OpenAI自研的Jalapeño晶片走的是相反方向：透過把整個工作負載留在單一連接系統內，從根本上減少資料搬移與通訊延遲，讓一次請求從頭到尾都能維持快速與高效。Nvidia的做法則是用一整套專用硬體（CPU、推論加速器、儲存與網路機櫃）去解決資料流動的問題。兩者路線不同，但邏輯一致：效率的提升不再單純依靠堆疊更多運算週期，而是靠更聰明地控制資料如何在系統裡移動。這也讓競爭的戰場出現轉移，造出一顆更快的GPU不再是唯一關鍵，能讓整套系統高效運作才是，而目前看來Nvidia在這個新戰場上仍佔有明顯優勢。

🎯 實務啟示

在評估AI基礎建設或訓練、推論成本時，除了看GPU算力峰值，也值得把資料編排與系統整合效率一併納入考量；像tokens-per-watt這類指標，可能比單純的算力數字更能反映實際的部署成本與效率瓶頸所在。

🔗 來源
- 標題：Nvidia's AI advantage is moving beyond the GPU
- 作者／機構：Russell Brandom，TechCrunch AI
- 連結：https://techcrunch.com/2026/08/29/nvidias-ai-advantage-is-moving-beyond-the-gpu/

#Nvidia #AIInfrastructure #DataCenter #VeraRubin #GPU #AIChips #OpenAI #Semiconductors #MachineLearning #TechCrunch
