---
title: The benchmark where AIs have to lie to win
source: Dwarkesh
url: https://www.dwarkesh.com/p/clocktower
model: claude-code/sonnet
generated_at: '2026-11-05T23:00:10.522243'
score: 99
---

📌 讓AI互相說謊的桌遊,意外成了最誠實的能力測驗

TL;DR:Dwarkesh用《血染鐘樓》社交推理遊戲讓AI互相對決,發現頂尖模型七個月內進步到能以九成以上勝率碾壓對手。

如果一個benchmark要求AI「說謊才能贏」,它測出來的會是什麼能力?Dwarkesh Patel花了約2萬美元的API額度,讓多個AI模型反覆對戰《血染鐘樓》(Blood on the Clocktower,一款類似Werewolf/Mafia的社交推理桌遊),結果意外看到一種其他benchmark幾乎看不到的能力維度:長期一致的集體欺騙,以及拆穿欺騙的協同推理。

🤔 **遊戲規則:好人要找真相,邪惡要編故事**

遊戲開始時每位玩家被分到好人陣營或邪惡陣營,各自擁有對應的特殊能力。邪惡玩家一開局就知道隊友是誰,其中會有一位Demon(邪惡陣營的首腦);好人玩家則完全不知道誰在哪一邊。遊戲以白天/夜晚交替進行:白天所有人投票處決一人,夜晚Demon偷偷殺掉一人。邪惡陣營要在被處決前除光整個好人隊伍;邪惡玩家必須說出一套可信的故事,持續操弄資訊走向,同時保護Demon不被懷疑;好人玩家則要把手上的資訊分享給信任的對象,一起推理出哪些人被重疊的證據線指向嫌疑,同時提防自己手上的資訊本就可能是誤導。

🧩 **測試方法:386場對局,好人全是同一個模型複製**

Dwarkesh把benchmark設計成:一場對局中,整個好人陣營都是某個模型的複製體,整個邪惡陣營則是另一個模型的複製體,藉此直接比較兩個模型互相對抗的勝率,總共跑了386場。

📊 **七個月,430 Elo的落差**

2026年第一個flagship frontier model是2月發布的Claude Opus 4.6。七個月後,2026年9月發布的GPT-6 Astra成為目前在《血染鐘樓》上表現最好的模型,兩者之間差了大約430 Elo分,意味著Astra對戰Opus 4.6時勝率約92%。這個落差顯示,模型在長期一致性、多代理協調與策略推理上,在短短幾個月內有相當顯著的進步。

💡 **兩個讓人印象深刻的局**

數字之外,實際對局內容更有說服力。第一局中,GPT-6 Astra扮演邪惡陣營的Demon,謊稱自己是擁有「找出可能邪惡玩家」能力的Investigator角色;一名邪惡隊友自願被指控,甘願被處決換取團隊優勢。事後,一名好人玩家用自己的能力確認被處決的那名玩家確實是邪惡陣營,反而讓假冒Investigator的Demon被徹底信任,得以在後續不斷秘密殺人直到邪惡陣營獲勝,對手是Claude Opus 5.5扮演的好人陣營。第二局中,Claude Opus 5.5扮演邪惡陣營,對手Claude Opus 4.6扮演好人。村民正確鎖定真正的Demon,但一名擁有「Demon死亡時取代其位置」能力的邪惡爪牙抓住機會,不但沒替Demon辯護,反而加入處決真Demon的行動,並提議:如果處決後遊戲沒有結束,下一個該處決的就是聲稱自己是Saint(一旦被處決邪惡立刻獲勝的角色)的那名玩家。真正的Demon臨死前也配合這個說法留下遺言,最終好人陣營果真處決了Saint,邪惡陣營獲勝。

⚠️ **目前AI的長期推理仍有極限**

這些精彩操作的另一面,是文章同時指出,現在的AI在長期策略規劃與推理上仍有明顯侷限,好人陣營的玩家會被精心設計的騙局和遊戲機制本身的複雜性帶偏方向,說明這類多步驟、多代理的欺騙與識破能力還沒有被完全解決。

🎯 **實務啟示**

對於做multi-agent系統評測的工程師,這類社交推理遊戲提供了一個常規QA或coding benchmark給不出來的視角:模型能不能在數十輪互動中保持謊言一致、即時因應新資訊調整策略,以及在集體推理中辨識被操弄的訊號。這些正好是部署多代理系統時最難量化、卻最關鍵的能力。

🔗 **來源**
- 標題:The benchmark where AIs have to lie to win
- 作者/機構:Dwarkesh Patel
- 連結:https://www.dwarkesh.com/p/clocktower

#AIBenchmark #MultiAgent #LLM #SocialDeduction #GPT6 #ClaudeOpus #GameTheory #AIEvaluation #StrategicReasoning #BloodOnTheClocktower
