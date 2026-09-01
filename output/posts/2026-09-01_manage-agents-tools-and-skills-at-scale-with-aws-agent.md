---
title: Manage agents, tools and skills at scale with AWS Agent Registry
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/manage-agents-tools-and-skills-at-scale-with-aws-agent-registry/
model: claude-code/sonnet
generated_at: '2026-09-01T10:52:56.722560'
score: 81
---

📌 AWS Agent Registry：AI Agent 的集中治理目錄

TL;DR：AWS Agent Registry 正式 GA，提供企業級 Agent／工具／Skill 集中治理目錄。

當一個組織裡的 AI Agent 從幾十個長到幾百上千個，「這個工具還有沒有人在維護」會變成比「怎麼做出更多 Agent」更迫切的問題。

🤔 規模化後撞上的三個共通問題

隨著組織擴大 Agent 與工具的使用規模，會遇到三個問題：各團隊各自為政開發，沒有單一紀錄能說明有哪些資源存在、誰擁有它、是否還在維護，結果是重複投入、版本漂移，以及散落各處、無人追蹤的能力堆積；即使好用的工具、Agent、Skill 已經存在，其他團隊的開發者也因為找不到而選擇重新造輪子；此外沒有中央登記機制，就無法追蹤誰有權存取哪些資源、是否通過安全審查、故障發生時如何追溯回特定版本與擁有者。

🧩 架構：Governance Plane 與 Discovery Plane

AWS Agent Registry 現已全面上市（GA），提供一個單一、可搜尋、受治理的目錄，涵蓋組織環境中的 Agent、工具、Skill 與自訂資源。內部架構分成兩個互補層面：Governance Plane 是完整登記資源的權威儲存區，不論生命週期處於哪個階段都會被涵蓋，管理員在這裡設定資源如何被管理的規則；Discovery Plane 則是消費者日常互動的介面，只呈現通過組織核准門檻的資源，提供精選、高效能的檢視畫面。兩者分工清楚：管理員透過 Governance Plane 取得完整可見性與政策控制，消費者則透過 Discovery Plane 取得快速、受治理的搜尋體驗，且只看得到已準備好可用的資源。Registry 支援四種紀錄型別，並內建語意搜尋與存取控制。

📊 已在導入的企業案例

西南航空 CIO／EVP Lauren Woods 提到，他們的 Agent 與工具原本散落在多個技術團隊、沒有共享紀錄，導入後變成組織上下都信任的單一治理目錄，平臺團隊得以完整掌握部署了什麼、誰擁有、是否已審查，開發者能用語意搜尋在數秒內找到已核准的能力，而不是重新打造別人已經做過的東西，並表示 Registry 顯著減少了重複開發、成為他們治理 agentic AI 的骨幹。PepsiCo Chief Strategy & Transformation Officer Athina Kanioura 指出，Agent Registry 提供一個集中方式在企業規模上發現、治理、重用 Agent、工具與整合。Syngenta 的 Enterprise Architect Sandeep Rayasa 表示，他們把 AI Agent 治理建立在 AWS Agent Registry 之上，讓團隊發布一次、之後就能發現並重用已可行的東西，而不是從頭重建 Agent、連接器與商業流程，並且在分享給組織其他人之前，每項能力都會先登記、審查、核准。Amdocs 的 Ron Dublero 提到，他們把 Registry 整合進自家的 aOS Cognitive Core 平臺，取得跨環境 Agent 資產的統一視圖，同時簡化治理、合規與生命週期管理。PwC Australia 的 Dr. Binqi Zhang 則提到，Registry 能一致地管理 Agent 能力，同時允許客製化整合既有技術環境，並協助緩解規模化後常見的「Agent 氾濫（agent sprawl）」這類新興維運風險。

🎯 實務啟示

對正在多團隊、多雲環境下擴張 Agent 數量的組織來說，Agent Registry 處理的其實是軟體工程裡老問題的 Agent 版本：套件／服務目錄與治理。如果組織已經出現「不同團隊各自寫了功能重複的 Agent 或工具」的徵兆，這類集中登記、審核後才開放發現的機制，值得作為 Agent 治理策略的評估起點；不過從內容看，這更像是把既有企業目錄／治理模式套用到 Agent 情境，而非全新的技術突破。

🔗 來源
- 標題：Manage agents, tools and skills at scale with AWS Agent Registry
- 作者／機構：Chaitra Mathur（AWS ML Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/manage-agents-tools-and-skills-at-scale-with-aws-agent-registry/

#AWS #AgentRegistry #AgenticAI #AIGovernance #EnterpriseAI #MCP #CloudComputing #AIOps #Bedrock #AIAgents
