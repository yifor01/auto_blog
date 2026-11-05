---
title: The October inflection point for vibe game development
source: Simon Willison
url: https://simonwillison.net/2026/Oct/28/vibe-game-development/
model: claude-code/sonnet
generated_at: '2026-11-05T23:05:25.902262'
score: 87
---

📌 Claude Opus 5.5讓AI做遊戲真正「好玩」了

TL;DR：知名工程部落客實測四款AI生成遊戲，發現Opus 5.5開始懂得什麼叫「好玩」。

AI做遊戲做到「看起來像遊戲」已經很久了，但「好玩」始終是另一個維度的難題——直到現在。

🤔 **背景：為什麼「看起來像遊戲」不等於「好玩」**

Simon Willison此前寫過，2025年11月是coding agent的拐點，Claude Opus 4.5與GPT-5.1的能力跨過門檻，讓coding agent成為軟體工程師日常可靠的工具。他認為2026年10月出現了另一個拐點，這次是針對「vibe coding」電玩遊戲。模型很早就能生成「看起來像遊戲」的東西，但要做出一個「玩起來真的好玩」的遊戲一直被認為是困難的，因為遊戲設計本身是一門需要在挑戰難度與學習曲線之間取得平衡的工藝。Willison自稱不是遊戲設計專家，但他原本並不認為模型能做到這件事，直到他對Claude Opus 5.5下了一個簡單指令：「Make it a LOT more fun」，結果模型真的做到了。

🧩 **四個「vibe coded」出來的遊戲**

過去幾週，Willison在完全沒看程式碼的情況下（vibe coding的古典定義），做出四款他自己真心覺得好玩的遊戲，全部以HTML與JavaScript寫成、跑在瀏覽器裡：

- **Tree Appreciator**：用Claude一般聊天介面（不需要Claude Code）做出的three.js小遊戲，玩法是比較兩棵演算法生成的樹的差異。他的prompt只要求「想清楚怎麼讓它同時好玩又漂亮」，結果一次就做出成品，收集完成的樹木還會放進一本「herbarium」圖鑑，帶來一種輕鬆的成就感。
- **一款奇幻村莊RPG**：同樣用Claude一般聊天介面逐步擴充，從最初的俯視角RPG引擎原型（玩家帶著同伴走動、進入建築時牆面變透明）開始，一路加到有地形高低差、有地下通道串連的地窖、山洞裡睡著的巨怪，最後要求模型「把這個變成一個真正的遊戲，加入不太老套的劇情與magic系統」。這個專案花了更多時間在playtesting與修bug（例如NPC因為劇情推進跑錯位置），完成後有一個約15分鐘可以玩完的完整故事，Willison說自己被結局打動，而圖像、劇情、對話全部出自模型，他自己的創意輸入幾乎只有「這是個奇幻村莊，山洞裡有隻睡著的巨怪」。他也拿同一串prompt餵給ChatGPT GPT-6 Pro做對照，畫面同樣好看，但他認為玩起來不如Opus 5.5的版本。
- **Battle Drones**：一款Command & Conquer風格的即時戰略遊戲，兩隊（後來擴充到四隊）機器人軍隊採集資源、建造單位互相攻防。最早版本在7月用Claude Fable 5做出來，只是堪用但不好玩的2D版本，直到用Opus 5.5下指令「Make it a LOT more fun」，接著再要求「把遊戲移植到three.js」，整個遊戲才脫胎換骨。目前版本支援2到4人多人連線（透過vibe coded的WebSocket relay伺服器）、有獎章、重播、七張地圖、隨機地圖產生器，還有讓不同LLM互相對戰的模式。Willison已以Apache 2.0授權釋出原始碼，隔天就有開發者Gabriel Turpin把它fork成蒸汽龐克風格、背景設定在1900年代巴黎美好年代的「Panache」，換上新模型、新音樂與動畫開場。
- **Quarter Sun Cove**：靈感來自他居住地Half Moon Bay一年一度的南瓜節與巨型南瓜秤重比賽，主題是種南瓜、養出巨型南瓜，並應付十月南瓜季的忙碌，目前仍在持續迭代中。

💡 **Opus 5.5與GPT-6 Astra的落差**

Willison提到他沒有做過嚴謹的系統性比較，但他目前的印象是GPT-6 Astra「還沒到位」，它能夠做出一款遊戲，但在「好玩」的判斷力上還追不上Opus 5.5，他預期OpenAI會在年底前補上這個差距。

⚠️ **一個人的觀察，不是嚴謹研究**

以上結論都來自Willison個人的實測與主觀感受，並非正式的對照研究，他自己也強調「沒有做過exhaustive study」。這類評價受限於單一使用者的prompt風格與遊戲品味，不同人、不同遊戲類型得到的結果可能不同。

🎯 **對工程師的實務啟示**

如果你也想嘗試vibe coding遊戲開發，幾個從素材中可以直接複用的技巧值得注意：明確要求模型使用three.js來處理3D畫面，效果不錯；在卡關或遊戲不好玩時，直接下「Make it a LOT more fun」這種直白指令，反而比精雕細琢的prompt更有效；而規模較大的專案（如Battle Drones、奇幻RPG）都需要額外的playtesting與bug修正，代表「一次生成」在複雜遊戲上仍不可靠，迭代仍是必要環節。

🔗 **來源**
- 標題：The October inflection point for vibe game development
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Oct/28/vibe-game-development/

#ClaudeOpus55 #Anthropic #VibeCoding #GameDev #AIGames #ThreeJS #GenerativeAI #CreativeCoding #LLM #IndieGames
