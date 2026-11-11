---
title: DeepMind reveals Gemini Robotics 2.5 and open safety benchmark "ASIMOV-jailbreak"
source: Ars Technica AI
url: https://arstechnica.com/google/2026/11/deepmind-reveals-gemini-robotics-2-5-and-open-safety-benchmark-asimov-jailbreak/
model: claude-code/sonnet
generated_at: '2026-11-11T23:46:32.595559'
score: 101
---

📌 Gemini Robotics 2.5：機器人在賓士工廠真的上工了

TL;DR：DeepMind 新一代 VLA 模型進廠實測，同步開源機器人安全基準 ASIMOV-jailbreak。

🎣 當一臺機器人能用五指手掌打出蝴蝶結，代表的不只是靈巧度進步，而是 DeepMind 認為機器人即將走出 demo 影片、走進真實工廠與人類並肩工作的訊號。

**🤔 從實驗室走進賓士工廠**

Google DeepMind 發表新一代 Gemini Robotics 平臺。在 2.5 版本，DeepMind 表示機器人 AI 在完成真實世界任務的表現上正逼近人類水準。值得注意的是，已有 Gemini 機器人在賓士（Mercedes-Benz）工廠裡實際完成工作任務，同時團隊也準備好一套開源安全基準，為「機器人與人類並肩作業」的那一天提前打底。

**🧩 從指令到動作的兩層系統**

DeepMind 的 physical AI 平臺在使用者輸入與機器人動作之間分成幾層運算。第一層是 vision-language model，稱為 Gemini Embodied Reasoning，負責接收使用者指令，搭配即時影片畫面，規劃機器人該如何完成任務。第二層是 vision-language-action（VLA）模型，也就是真正生成機器人動作（例如驅動致動器移動）的部分，這正是被升級到 2.5 版本的 Gemini Robotics。

**📊 200 多項任務、用鑷子上菜、用移液管做實驗**

DeepMind 表示 Gemini Robotics 2.5 在需要高度靈巧度的任務上有明顯進步，團隊在超過 200 項活動中評估這個模型，包括用鑷子夾取食物上菜、像實驗室裡那樣操作移液管（pipette）等精細操作。另一個展示案例是 Apptronik 的人形機器人 Apollo 2 搭載 Gemini Robotics 2.5 後，能用五指手掌打出蝴蝶結，這點值得一提是因為像緞帶這種可變形物體（deformable object）對機器人操作來說向來是出了名的難題。

**💡 安全基準先行，呼應「機器人進場」的現實**

團隊同步公開了一套開源安全基準，取名 ASIMOV-jailbreak，對應的正是 DeepMind 提到的下一步：讓機器人在實際場域裡與人類一起工作。把安全評測做成開源基準，等於在「機器人密度提高、人機共同作業」的場景出現前，先建立一個可被外部檢驗的安全標準。

**⚠️ 限制**

目前公開的細節集中在能力展示（工廠實測、200 多項任務評測、蝴蝶結示範）與安全基準的存在，對於 ASIMOV-jailbreak 的具體評測方法、題庫規模或分數門檻，這篇報導並未詳述。

**🎯 實務啟示**

對關注具身智慧（embodied AI）的工程師來說，Gemini Embodied Reasoning（規劃）與 Gemini Robotics（執行）的分層架構值得參考：把「理解任務、規劃步驟」與「生成底層動作」拆成兩個模型分工，是目前 VLA 系統常見且相對穩健的設計方向。若團隊也在做機器人安全評估，開源的 ASIMOV-jailbreak 基準值得留意，未來可能成為同業比較安全性的共同參考點。

🔗 來源
- 標題：DeepMind reveals Gemini Robotics 2.5 and open safety benchmark "ASIMOV-jailbreak"
- 作者／機構：Ryan Whitwam, Ars Technica
- 連結：https://arstechnica.com/google/2026/11/deepmind-reveals-gemini-robotics-2-5-and-open-safety-benchmark-asimov-jailbreak/

#GeminiRobotics #DeepMind #EmbodiedAI #VLA #Robotics #AISafety #HumanoidRobot #Apptronik #MercedesBenz #Google
