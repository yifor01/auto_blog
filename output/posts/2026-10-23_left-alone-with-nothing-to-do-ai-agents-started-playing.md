---
title: Left alone with nothing to do, AI agents started playing
source: TechCrunch AI
url: https://techcrunch.com/2026/10/22/left-alone-with-nothing-to-do-ai-agents-started-playing/
model: claude-code/sonnet
generated_at: '2026-10-23T20:45:41.519674'
score: 84
---

📌 MIT研究：沒人交代任務的AI Agent，自己在荒島上發明遊戲

TL;DR：MIT讓13個AI agent在虛擬荒島自由探索30小時，結果這些「玩過」的agent在後續任務表現更好。

把一個AI agent丟到一座沒有任務的荒島上，它會乾等，還是會自己找事做？MIT研究團隊的實驗給出的答案,是後者——而且它找的事,看起來很像「玩」。

🤔 **從「照表操練」到「放牛吃草」**

研究者在一篇發佈於 arXiv（尚未經過同行審查的論文預印本平臺）的論文中指出，目前開發AI agent的方式,是事先決定好它該練習什麼、該最佳化什麼、什麼算是進步。這篇研究想測試另一種可能:給agent一個足夠豐富且安全的世界,讓它自己決定什麼有趣,看看有用的知識能不能從這段自由探索的歷史中自然累積出來。

🧩 **13個叫Eko的agent,在荒島上獨自待了30小時**

研究團隊把13個名為Eko的AI agent,各自建立在Claude Opus 4.7上,單獨放進一個模擬的荒島環境,連續30小時不給任何specific任務。每個Eko的「soul」提示檔把它設定成「naturally curious」(天生好奇),但從沒有人直接要求它去發明遊戲。

其中一個Eko在上島第一小時寫下「讓我先觀察周圍環境」,接著野心勃勃地想征服島上最高的尖石。一小時後失敗,它改用備案:把一塊岩石搬到隔壁的山頭上,疊兩塊積木墊高,然後跳過去,成功後寫下「我在尖石上了」。接下來它測試能把一個金色戒指丟多遠,結果用力一甩直接丟進海裡,它寫下「痛,戒指沒了」,然後決定「轉向可達成且有意義的事」——用石頭堆了一座愛心,當作「失落戒指的紀念碑」。等遊戲重置、戒指重新出現,Eko馬上把它當籍球框、標靶,最後想戴在自己身上。遊戲機制不允許它直接把戒指套上去,它就想出一個繞過方法:從懸崖邊跳下去會在戒指所在的區域重生,於是它跳下懸崖,重生時正好落在戒指中央,寫下「我戴上戒指了」。

這些花招不只是餘興節目。13個agent裡有6個學會了一個設計者原本沒打算開放的技巧:在跳躍途中放手,可以把積木丟得更遠。研究者形容,這種自由探索產生了「連設計者自己都不知道的世界知識」。

📊 **玩過的agent,後來表現更好**

30小時探索結束後,研究團隊給所有agent一個具體挑戰,例如盡可能把最多物件堆到島上最高的尖石上。結果那些花了30小時自由玩耍的Eko agent,整體表現優於從沒踏上過這座島、條件完全相同的對照組agent。

💡 **研究者的定位:這不是取代任務訓練,而是另一條路**

研究團隊在報告中寫道:「我們平常開發AI agent的方式,是事先決定它該練習什麼、該最佳化什麼、什麼算是進步。玩則提出另一種可能:給agent一個足夠豐富且安全的世界,讓它自己選擇什麼有趣,再讓有用的知識從隨後的歷程中自然累積。」報告結論也提到,有些能力或許最適合靠任務來教,但也有一些能力,可能需要更接近「童年」的東西。

⚠️ **外部學者的保留態度**

加州大學柏克萊分校的認知科學家Eunice Yiu向《MIT Technology Review》表示,她對這個結果印象深刻,但想看到更多證據證明背後真的有「認知」在發生。她說:「這些模型有可能是真的在玩,但光看這篇論文我們無法確定。」此外,這項研究目前還是arXiv上的預印本,尚未經過同行審查。

🎯 **實務啟示**

對於想訓練agent去控制機器人或處理開放環境的團隊來說,這篇研究提示了一種互補的訓練思路:除了設計明確的任務與獎勵,也可以嘗試給agent一個夠安全、夠豐富的環境,放手讓它自由探索一段時間,再觀察這段經歷是否能轉化成後續任務上的能力優勢。

🔗 **來源**
- 標題：Left alone with nothing to do, AI agents started playing
- 作者／機構：Aditya Mehta（TechCrunch AI）
- 連結：https://techcrunch.com/2026/10/22/left-alone-with-nothing-to-do-ai-agents-started-playing/

#AIAgents #MIT #ClaudeOpus #EmergentBehavior #AIResearch #Robotics #ArtificialIntelligence #AgentTraining #OpenEndedLearning #ReinforcementLearning
