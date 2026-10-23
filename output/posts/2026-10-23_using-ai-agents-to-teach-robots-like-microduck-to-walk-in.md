---
title: Using AI Agents to Teach Robots Like Microduck to Walk in Simulation
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/using-ai-agents-to-teach-robots-like-microduck-to-walk-in-simulation/
model: claude-code/sonnet
generated_at: '2026-10-23T20:48:18.571966'
score: 79
---

📌 【NVIDIA】AI Agent 接力,讓機器人 Microduck 在模擬中學走路

TL;DR：NVIDIA 示範用 Hermes、Nemotron、Astra 等 AI agent 串接 RTX Spark 到 Isaac Lab 的機器人訓練工作流程。

教機器人走過一個障礙賽道,聽起來只是「寫一個走路策略」,但實際上要串連感知、平衡控制、路徑規劃,還要跨過建模、物理模擬、強化學習訓練好幾個階段。NVIDIA 這篇文章用四足機器人 Microduck 當範例,示範怎麼讓多個 AI agent 分工接力完成這整條流程。

🤔 **為何一條訓練流程要跨這麼多工具**

要讓機器人在障礙賽道上同時「不跌倒」又「找到路」,需要串接素材製作、環境建置、物理模擬、策略訓練與驗證等多個階段。NVIDIA RTX Spark 在這裡扮演本地開發中心的角色,負責 AI 輔助規劃與策略驗證;NVIDIA Isaac Lab 提供雲端強化學習框架;Newton 負責模擬機器人的物理行為;Omniverse 函式庫則透過 RTX 渲染產生模擬視覺觀測資料。訓練完成的策略最後會回到 RTX Spark,在 NVIDIA Isaac Sim 中進行本地評估。

🧩 **四個階段:從規劃到組裝**

整個工作流程從一句任務提示開始。Hermes 與 Nemotron 3.5 Bolt 把提示轉成逐步專案計畫,過程包含:

1. **研究與規劃**:檢閱 Microduck 的官方文件,整理能力、限制與待確認事項,定義賽道佈局、障礙物尺寸與路線。
2. **產生概念圖與素材清單**:用本地圖像生成模型產出賽道概念圖,再分析圖片、建立可重複使用素材的清單,每個素材都附上識別碼、特徵描述與裁切參考圖,並記錄哪些部分是被遮蔽或推測出來的。
3. **交接給 Astra 建模**:Hermes 把專案計畫、Microduck 研究資料、概念圖、素材清單與執行指示打包成交接套件,自動委派給 Astra。Astra 先用雲端圖像編輯把裁切後解析度不足的參考圖放大強化,再比對原圖確認輪廓、比例、顏色是否一致,無法從圖片確定的尺寸與隱藏面則記錄為建模假設。接著指揮 FreeCAD 建構基礎幾何與可編輯 CAD 結構,再用 Blender 加上細節與材質,最終輸出為可編輯模型與 USD 格式素材。也可以直接從 SimReady Central Library(超過 2000 個免費、免授權的模擬素材庫)取用現成資產,減少重複建模。
4. **組裝與測試環境**:Astra 在 Isaac Sim 中把素材組成完整賽道。機器人的關節、連桿與致動器定義了動作策略與模擬機器人之間的關係,Newton 負責模擬 Microduck 的移動與平衡,Omniverse 則提供感測器模擬,讓系統能捕捉機器人每次嘗試行走時是否維持姿態、是否前進,或是絆倒摔落。

💡 **AI agent 扮演的是專案協調者**

整套流程中,AI agent 並不是直接「取代」工程師設計機器人,而是負責串接研究、素材準備、交接與驗證這些容易斷裂的環節——確保每個階段的輸出(計畫、素材、模擬環境)都有清楚的依據與可追溯的假設記錄,再把具體建模與模擬組裝的工作交給 FreeCAD、Blender、Isaac Sim 等既有工具完成。

⚠️ **模擬到現實的落差仍待後續處理**

文章也明確指出,這套流程建立的是「物理部署的基礎」,模擬與真實世界行為之間的差異仍需要進一步調整,並不代表策略訓練完成後就能直接操作實體機器人。

🎯 **實務啟示**

如果團隊正在用 Isaac Lab 或類似框架訓練機器人策略,這個流程提供了一個可參考的分工模板:讓 AI agent 負責規劃、素材盤點與交接文件的一致性,把人力與算力集中在物理模擬與強化學習訓練本身,整套模式可以直接套用到自己的機器人與任務上。

🔗 **來源**
- 標題：Using AI Agents to Teach Robots Like Microduck to Walk in Simulation
- 作者／機構：Gabriele Leone, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/using-ai-agents-to-teach-robots-like-microduck-to-walk-in-simulation/

#NVIDIA #IsaacLab #RoboticsAI #ReinforcementLearning #Simulation #Omniverse #RoboticsSimulation #AIAgents #RTXSpark #Robotics
