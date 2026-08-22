---
title: 'From Atari to EVE Online: Building on 15 Years of AI Research in Games'
source: Google DeepMind
url: https://deepmind.google/blog/from-atari-to-eve-online-building-on-15-years-of-ai-research-in-games/
model: claude-code/sonnet
generated_at: '2026-08-22T06:10:31.220285'
pinned: true
---

📌 DeepMind攜手EVE Online打造持久世界AI

TL;DR：Google DeepMind公開15年遊戲AI研究脈絡，並與EVE Online開發商展開新研究合作。

從Atari的像素畫面到圍棋棋盤，再到一個由數萬名玩家共同經營二十多年的太空宇宙，Google DeepMind這篇回顧文章串起了一條清晰的技術路線：遊戲從來不只是娛樂，而是AI研究最嚴苛的試煉場。

🤔 **為什麼遊戲是AI研究的天然實驗室**

文章指出，Google DeepMind自2010年成立以來，遊戲world就是理解智慧的核心場域。共同創辦人Demis Hassabis本人是前遊戲開發者，團隊中也有許多人具備遊戲開發背景，這讓他們與遊戲工作室的合作不只是技術授權，而是「深度夥伴關係」——例如與Fenris Creations（EVE Universe的開發商）、Hello Games、Coffee Stain Studios、Foulball Hangover等工作室的合作。

🧩 **從DQN到SIMA：每個里程碑都在拓展能力邊界**

素材回顧了一條完整的技術演進線：
- Deep Q-Network（DQN）於2015年發表在Nature，直接從原始像素學會玩49款Atari 2600遊戲，未做任何遊戲專屬工程，催化了現代深度強化學習的興起。
- AlphaGo於2016年擊敗世界冠軍李世乭；AlphaGo Zero完全透過self-play學習，不使用任何人類棋譜；AlphaZero將同一套演算法推廣到西洋棋、將棋與圍棋；MuZero則進一步做到連遊戲規則都不需要事先知道。
- AlphaStar於2019年在StarCraft II中達到宗師（Grandmaster）等級，處理即時性與資訊不完整的挑戰。

摘要特別提到，AlphaGo著名的「第37手」一度被專業棋評誤認為失誤，卻顛覆了圍棋界數百年累積的定式認知，AlphaZero也同樣啟發了西洋棋的全新走法。這種探索精神後來延伸到AlphaFold，協助解開蛋白質結構預測這個五十年來的重大難題，並獲得2024年諾貝爾化學獎肯定。

在此之後，研究方向從「精通遊戲」轉向「理解遊戲」——這正是SIMA（Scalable Instructable Multiworld Agent）要回答的問題：AI能否像人類一樣理解並操作任何遊戲世界？SIMA不追求破紀錄，而是透過畫面觀察、自然語言指令理解，並以一般鍵盤滑鼠操作與遊戲互動，不需要API或原始碼存取。由Gemini驅動的SIMA 2具備即時推理與對話能力，已在No Man's Sky、Valheim、Hydroneer等複雜3D環境與研究場景中展現接近人類的表現。

💡 **EVE Online：為什麼是持久多人宇宙**

這次與Fenris Creations的合作被視為新篇章。EVE Online自2003年上線，是一個由數千名玩家共享單一宇宙的太空模擬遊戲，二十多年來持續演化，擁有真實供需驅動的玩家經濟體系，以及橫跨數千個星系的貿易網路。摘要指出，這樣的世界恰好對應到Google DeepMind認為前沿AI必須具備的四項能力：持續學習（在不斷變化的世界中學習新技能而不遺忘舊有能力）、記憶（跨越遠超今日模型context window的時間尺度累積與檢索知識）、長遠規劃（以週、月甚至年為單位推理）、以及複雜的多智能體動態（大規模的合作、競爭、談判與經濟行為）。Fenris Creations執行長Hilmar Pétursson也表示，這項合作要探索的是AI必須在沒有其他遊戲環境要求的時間尺度上學習、適應與記憶。

🎯 **實務啟示**

對從事agent與強化學習研究的工程師而言，這篇文章勾勒出一個值得關注的訊號：評估AI能力的場域正從「有明確分數與規則的封閉遊戲」轉向「沒有API、沒有既定目標、由人類長期互動塑造的開放世界」。若你在設計agent的記憶機制或長期規劃能力，EVE Online這類持久多人環境提供的挑戰，可能比傳統benchmark更接近真實世界的複雜度。

🔗 **來源**
- 標題：From Atari to EVE Online: Building on 15 Years of AI Research in Games
- 作者／機構：Alexandre Moufarek and Adrian Bolton, Google DeepMind
- 連結：https://deepmind.google/blog/from-atari-to-eve-online-building-on-15-years-of-ai-research-in-games/

#GoogleDeepMind #ReinforcementLearning #SIMA #AlphaGo #GameAI #AGI #Gemini #MultiAgent #ContinualLearning #EVEOnline
