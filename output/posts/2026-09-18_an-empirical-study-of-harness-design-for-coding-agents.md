---
title: An empirical study of harness design for coding agents
source: Hacker News
url: https://arxiv.org/abs/2609.20804
model: claude-code/sonnet
generated_at: '2026-09-18T19:47:11.499293'
score: 98
---

📌 176組實驗告訴你:Coding Agent的Harness該怎麼組

TL;DR:一篇新論文固定執行迴圈、只變動三個元件,拆解出context management、planning、action space各自對coding agent效能的真實貢獻。

Coding agent的Harness(執行框架)常被當成一個整體來評測,好或壞說不出具體是哪個環節的功勞。這篇論文決定把它拆開來看。

🤔 現有評測把Harness當成一個黑盒子

論文指出,coding harness決定了模型能力如何轉化為長流程(long-horizon)軟體工程任務的實際表現,但既有研究通常把harness當成一個單體系統來評測,導致個別元件的效果不清楚。為了做元件層級的比較,作者設計了一個輕量級coding harness,固定執行迴圈(execution loop)不變,只變動三個元件:planning(規劃)、action space(動作空間)與context management(上下文管理)。

🧩 四個模型、176組配置,兩個標準測試集

研究在四個模型上,於SWE-Bench Verified與Terminal-Bench 2.1兩個測試集進行評測,總共評估176組匹配的設定,涵蓋五種context-management策略、四種context-window預算,以及針對planning與action space的針對性消融實驗(ablation)。

📊 四個關鍵發現

- Context management的價值隨著context window預算收緊而遞增,其效益大部分來自防止context-overflow(上下文溢位)失敗,而不是提升準確率本身。
- 在幾種context-management策略中,先做基於規則的elision(刪減)、再交給LLM做摘要的分階段做法,整體效率最強;而讓被刪減的內容可還原(recoverable)雖然多了一套機制,但模型實際上很少用到,也沒有帶來準確率提升。
- Planning對較弱的模型是準確率的支撐架構,但對較強的模型則轉變為省成本的手段,對準確率本身影響不大。
- 預先定義好的工具(predefined tools)能提升bash能力較弱模型的表現;而bash能力強的模型單靠純bash介面就能有效運作,成本顯著更低,在以命令列為中心的任務上尤其明顯。

論文的軌跡層級(trajectory-level)分析進一步解釋了這些效果的成因:context management延長了執行軌跡的長度,但沒有明顯改變agent的行為模式;planning改變的是軌跡在哪裡停下來;action space則改變了程式碼被寫出時的顆粒度(granularity)。

🎯 實務啟示

如果你正在自己組裝或調整coding agent的harness,這篇論文給出的是可以直接落地的取捨依據:context window預算越緊,越該優先投資context management,且elision-then-summarize的分階段設計比追求可還原性更划算;面對強模型,planning可以優先當成省Token的手段而非硬性流程;而選擇predefined tools還是bash-only介面,應該視模型本身的bash能力而定,而不是一律套用同一套動作空間。

🔗 來源
- 標題:An Empirical Study of Harness Design for Coding Agents
- 作者/機構:Run-Ze Fan, Zihao Zhang, Simin Ma, Yebowen Hu, Shouju Wang, Kaiqiang Song, Fei Liu, Hamed Zamani, Xiaoyang Wang
- 連結:https://arxiv.org/abs/2609.20804

#CodingAgent #LLM #AgentHarness #SWEBench #ContextManagement #AIResearch #SoftwareEngineering #PromptEngineering #MachineLearning #AutonomousAgents
