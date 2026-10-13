---
title: 'Alibaba Qwen Introduces QwenGyre: Elastic Reinforcement Learning RL for XLong-Horizon
  Agents'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/12/alibaba-qwen-introduces-qwengyre-elastic-reinforcement-learning-rl-for-xlong-horizon-agents/
model: claude-code/sonnet
generated_at: '2026-10-12T23:50:37.200092'
score: 97
---

📌 Qwen推出QwenGyre：讓訓練agent的GPU不再閒置

TL;DR：阿里Qwen團隊用彈性排程與前綴共享軌跡樹,讓小時級、百萬token的agent訓練速度翻倍。

訓練一個能跑好幾個小時、處理近百萬token的coding agent,聽起來就是GPU資源調度的夢魘。阿里Qwen團隊推出的QwenGyre,打的就是這個主意。

🤔 **什麼是「XLong-horizon」任務**

研究團隊把「XLong-horizon」定義為橫跨數小時、涉及數百次模型與工具互動的agent任務,例子包括依規格生成整個程式碼庫(如NL2Repo-Bench)。這類任務的rollout(推演)時間長、分支多,傳統的同步或固定資源分配訓練方式,很難把GPU用好用滿。QwenGyre是一套線上強化學習系統,透過不修改、黑箱式的harness來訓練coding agent,目標正是這類長達數小時、接近百萬token的rollout。

🧩 **兩個核心設計:GPU彈性搬移 + 把分支歷史變成有界訓練樣本**

QwenGyre把GPU分成共享同一套訓練佈局的「cell」,每個cell可以選擇服務rollout,也可以作為完整的訓練副本。其中有一個core cell持有權威的模型權重與optimizer狀態,其他satellite cell會在之後加入訓練。排程器會追蹤一個「rollout waterlevel」指標(排隊中與正在執行的任務數),當剩餘cell仍能撐住所有正在跑的工作時,其他cell就會切換去做訓練。

為了讓底層那個不能修改的harness持續運作,模型呼叫會經由一個proxy重新導向:這個proxy用token-in、token-out(TITO)的方式,記錄精確的token ID與行為log機率,並把這些呼叫存成「前綴共享的軌跡樹(prefix-shared trajectory trees)」。團隊發現把分支上限設為5,訓練分數就能追平不設上限的版本,同時把前向反向傳播時間縮短25.2%。訓練本身採用經過調整的GSPO,每組16個rollout。

📊 **48步跑了75小時,評估通過率從52.48%升到58.54%**

所有對照實驗都用Claude Code 2.1.220作為harness,並維持相同的GPU預算與一致的staleness設定。在Qwen自家旗艦Qwen3.8 2.4T模型上,QwenGyre完成48個訓練步驟耗時75.42小時;相較之下,Async方式要134.55小時,Colocate方式要91.47小時。訓練後的評估通過率也從52.48%提升到58.54%。

⚠️ **數字背後的保留**

文章特別提醒,這些加速數字是各自專案在自身設定下量出來的,並不能直接跨專案比較——換句話說,QwenGyre相對Async、Colocate的優勢,是在同一套實驗條件下的內部對照,不代表放到別的系統上也會有同樣倍數的提升。

🎯 **實務啟示**

對於要訓練長流程、重度呼叫工具的coding agent的團隊,QwenGyre示範了兩個可借鏡的思路:一是讓GPU在rollout與訓練之間彈性流動,而不是靜態分配;二是用前綴共享的軌跡樹管理分支歷史,把本來難以利用的發散rollout轉成有界、可訓練的樣本。這對任何想壓榨長horizon RL訓練效率的工程團隊,都是值得研究的系統設計範本。

🔗 **來源**
- 標題：Alibaba Qwen Introduces QwenGyre: Elastic Reinforcement Learning RL for XLong-Horizon Agents
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/12/alibaba-qwen-introduces-qwengyre-elastic-reinforcement-learning-rl-for-xlong-horizon-agents/

#QwenGyre #Qwen #ReinforcementLearning #Alibaba #CodingAgent #LLMTraining #GSPO #LongHorizonRL #GPUScheduling #OnlineRL
