---
title: How to Use AI Agents to Prepare 3D Scenes for Simulation
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/how-to-use-ai-agents-to-prepare-3d-scenes-for-simulation/
model: claude-code/sonnet
generated_at: '2026-09-17T20:33:35.374841'
score: 97
---

📌 【NVIDIA 實作】多 Agent 協作，把 Blender 場景變成機器人模擬世界

TL;DR：NVIDIA 展示用 Codex、Hermes 子 agent 與 Omniverse Libraries，自動把 Blender 場景整理成可訓練機器人的 SimReady OpenUSD 世界。

訓練機器人策略時，工程師常把注意力放在演算法與訓練迴圈上，但真正卡住專案的，往往是更早的一步：機器人根本沒有一個「模擬就緒」的世界可以練習。NVIDIA 這篇文章示範了如何用 agent 工作流，把 3D 美術做出來的 Blender 場景，變成 Isaac Sim 或 Isaac Lab 能直接使用的 OpenUSD 世界。

🤔 **場景「看起來」完成了,但模擬要用的東西都齊了嗎**

素材裡列出一連串容易被忽略的檢查項：物件有沒有貼上語意標籤？碰撞網格（collision mesh）對不對？材質對模擬有意義嗎？感測器有沒有放置與設定好？場景能不能乾淨匯出成 USD？機器人能不能感知到目標物件？場景在丟進 Isaac Sim 或 Isaac Lab 之前，能不能先通過驗證？這些準備工作瑣碎、重複，還很容易出錯，卻正是 agentic 系統可以發揮的地方，前提是它們有對的工具可用。

🧩 **三層架構：主 agent 協調、子 agent 推理、Omniverse Libraries 動手做**

這套工作流的分工方式是：由 Codex（搭載 OpenAI GPT-6 Astra）擔任主 agent，負責把開發者的目標拆解成任務、判斷任務間的依賴關係，並審查各個專門子 agent 回報的結果。這些子 agent 用 Hermes agent harness 建構、透過 NVIDIA NemoClaw 部署，各自負責一項具體工作，例如要讓一個物件變成「可抓取」，就需要同步更新它的語意標籤、剛體設定與碰撞幾何，Astra 的角色就是串起這些跨子 agent 的依賴關係，判斷流程往下走之前還需要哪些檢查。

真正動手修改場景的是 NVIDIA Omniverse Libraries：OpenUSD 操作建立共用的場景結構，ovphysx 負責撰寫與檢查物理屬性，ovrtx 負責渲染視覺化的 preflight 畫面，SimReady 驗證則用來評估最終資產是否符合目標模擬設定檔的要求。安全、機械性的問題可以自動修復；牽涉開發者意圖判斷的決策，例如語意標籤該怎麼標、物理行為該如何設定，則會連同相關脈絡與建議下一步，上報給人類決定。

🧩 **實際操作：先定義目標，再由子 agent 逐步盤點**

文中示範先明確設定主要目標：輸入是 Blender 場景，目標是準備好機器人模擬用途，輸出是 USD 格式的模擬就緒世界，目的地是 Isaac Sim 或 Isaac Lab，驗證方式是視覺化 preflight 加上 SimReady 驗證。有了這個結構，Codex 就能協調任務並判斷工作何時真正完成。

第一步是透過 Blender MCP（Model Context Protocol）伺服器盤點場景。MCP 讓 agent 能用受控的工具介面直接呼叫 Blender，檢視物件、集合、變換、材質、攝影機與燈光，而不是靠螢幕截圖用猜的，或依賴人工匯出。這個子 agent 要回答的問題包括：場景裡有哪些物件、集合與階層？指派了哪些材質？有哪些攝影機和燈光？哪些看起來像機器人的目標物、障礙物、地板、貨架或箱子？還缺少哪些模擬相關資料？輸出會被整理成結構化格式，例如列出物件數、材質數，以及缺少的項目（語意標籤、碰撞網格、相機感測器、物理材質等），作為後續所有子 agent 共用的起點。文中示範用的場景是 Alex Trevino 製作的《The Junk Shop》（原始概念來自 Anais Maamar）。

💡 **關鍵在於「共用場景狀態」與「驗證關卡」**

這套工作流真正的價值，不只是讓 agent「看懂」場景需要整理，而是把一個模糊的請求——「讓這個場景可以用來模擬」——拆解成有明確驗收標準、持續累積場景狀態、並在關鍵節點插入驗證與人工審核的工程流程。Blender MCP 提供的結構化盤點結果，成為後續所有子 agent 共同依賴的事實來源，避免各自對場景現況有不同假設。

🎯 **實務啟示**

對機器人模擬工程師來說，與其把 Blender 場景整理視為訓練前必須手動熬過的雜務，可以考慮把它拆成「盤點、標註、物理設定、渲染驗證、SimReady 驗證」幾個有明確輸入輸出的子任務，交給不同的專門 agent 各司其職，只在真正需要判斷力的地方才引入人工審核，藉此把準備模擬場景的時間，從人力密集的流程轉為可重複執行的自動化管線。

🔗 **來源**
- 標題：How to Use AI Agents to Prepare 3D Scenes for Simulation
- 作者／機構：Tanya Lenz, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/how-to-use-ai-agents-to-prepare-3d-scenes-for-simulation/

#NVIDIA #RoboticsSimulation #AgenticAI #OpenUSD #IsaacSim #IsaacLab #Omniverse #DigitalTwin #MultiAgent #SimReady
