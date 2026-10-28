---
title: The October inflection point for vibe game development
source: Simon Willison
url: https://simonwillison.net/2026/Oct/28/vibe-game-development/
model: claude-code/sonnet
generated_at: '2026-10-28T22:02:36.202689'
score: 79
---

📌 2026年10月,AI終於學會把遊戲做得「好玩」

TL;DR：Simon Willison觀察到Claude Opus 5.5讓vibe coding做出的遊戲第一次真正好玩,不只是看起來像遊戲。

讓AI做出一個「看起來像遊戲」的東西已經不難,但要做出一個「真的好玩」的遊戲,一直是AI過不去的坎,直到Simon Willison對Opus 5.5下了一句指令:「讓它變得更好玩很多」。

🤔 **從coding agent拐點到遊戲開發拐點**

Simon Willison之前寫過,2025年11月是coding agent的拐點,Opus 4.5與GPT-5.1當時跨過了讓agent成為工程師日常可靠工具的門檻。他認為2026年10月出現了另一個拐點,這次輪到vibe coding電腦遊戲:Claude Opus 5.5在幾個關鍵能力上有明顯進步,其中最重要的是「設計出真正有趣的遊戲循環」。他坦言自己不是遊戲設計專家,但深知打造一個難度曲線恰到好處、讓玩家有成就感的玩法循環是一門精細手藝,過去他並不認為模型能做到,直到親自測試Opus 5.5。

🧩 **四個親手做出的遊戲案例**

過去幾週,Willison用純聊天方式(完全沒看過程式碼)vibe coding出四款他真心覺得好玩的遊戲,全部用HTML與JavaScript寫成、可在瀏覽器執行:

- **Tree Appreciator**:最小的一款,單靠一句prompt「做一個用three.js的賽局,顯示兩棵演算法生成的樹,玩法是比較兩棵樹的差異,想清楚如何讓它同時有趣又好看」,一次生成就完成,無需任何後續調整,成了一款放鬆的「找不同」小遊戲。
- **奇幻村莊RPG**:從一個俯視角RPG引擎原型開始,逐步用「讓地形不要那麼平」「幫兩棟建築加地下室並用隧道連接」「加入一座藏著睡著的山怪的山洞」等指令疊代,最後要求「把它變成真正的遊戲,加入不落俗套的劇情與魔法系統」,完成後是一款約15分鐘能玩完、附帶關卡編輯器的完整遊戲。Willison提到自己在結局時情緒上被打動,而這整個遊戲的美術、劇情、角色、音樂、對話全部出自模型。他也用同一組prompt在GPT-6 Pro上做了對照,結果視覺效果同樣不錯,但遊玩體驗不如Opus 5.5版本。
- **Battle Drones**:一款類似《終極動員令》的即時戰略遊戲,兩隊機器人軍隊採集資源並爭奪地盤。最初版本是今年7月用Claude Fable 5做出的2D版,遊玩體驗並不出色,直到他對Opus 5.5下了「讓它變得更好玩很多」以及「把這個遊戲移植到three.js」的指令,遊戲才脫胎換骨。目前已具備2到4人連線對戰(透過vibe coded的WebSockets中繼伺服器)、獎牌、重播、七張地圖、隨機地圖產生器,以及一組可調整規則的「mutator」,還能讓不同LLM互相對戰。Willison已將Battle Drones以Apache 2.0授權開源,隨後Gabriel Turpin以此為基礎fork出了以1900年代美好年代風格重新演繹的Panache。
- **Quarter Sun Cove**:Willison居住地Half Moon Bay每年舉辦南瓜重量比賽節,他以此為靈感做了一款種植巨型南瓜、應付十月南瓜旺季的農場經營遊戲,目前仍在持續疊代中。

💡 **模型之間的「有趣感」差距**

Willison觀察到,GPT-6 Astra已經能夠建出一款遊戲,但他認為它對「有趣」的判斷還不及Opus 5.5,並預期OpenAI會在今年底前補上這個差距。他也強調這並非嚴謹研究,只是個人密集實驗後的印象。

⚠️ **並非一次到位**

除了Tree Appreciator是一次生成就成功外,奇幻村莊RPG與Battle Drones都經歷了不少疊代與除錯,尤其是遊戲邏輯層面的問題,例如角色因劇情推進而移動到別處,導致任務觸發位置錯位。

🎯 **實務啟示**

對工程師而言,這篇觀察提供了幾個可直接套用的prompt技巧:用「讓它更好玩很多」這種直白的指令去反覆疊代玩法,比一次性描述完整需求更有效;明確要求模型使用three.js能穩定得到品質不錯的3D成果;而把成品開源讓社群自由fork(如Panache案例),也可能加速概念的擴散與再創作。

🔗 **來源**
- 標題：The October inflection point for vibe game development
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Oct/28/vibe-game-development/

#VibeCoding #ClaudeOpus #GameDev #AIGeneratedGames #ThreeJS #GenerativeAI #IndieGameDev #LLM #CreativeCoding #AIAgents
