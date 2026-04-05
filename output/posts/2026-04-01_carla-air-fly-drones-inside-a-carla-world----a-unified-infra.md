---
title: "CARLA-Air: Fly Drones Inside a CARLA World -- A Unified Infrastructure for Air-Ground Embodied Intelligence"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2603.28032
score: 82
model: gpt-4o-free
generated_at: 2026-04-01T12:45:43.452778
---

📌 【CARLA-Air】統一空地模擬，讓無人機也能在 CARLA 世界裡飛行  

你以為 CARLA 只能模擬街道？  
這次它把無人機也帶進來了，  
地面與空中 agent 終於能在同一個 photorealistic 環境裡共訓練。  

🤔 **需要一個真正的空地聯合平台**  
隨著機器人與自動系統向立體作業發展，單一的地面或飛行模擬已無法滿足研究需求。研究者需要一個能同時呈現道路與低空場景、且具備多模態感測的統一環境，來訓練與測試能夠在空中與地面無縫切換的 embodied agent。  

🧪 **在 CARLA 基礎上擴充無人機飛行**  
CARLA-Air 建立在開源的 CARLA 模擬器之上，使用 Unreal Engine 引擎保持高保真度。它補充了多旋翼無人機的飛行動力學模型，並保留原有的車輛感測器（如相機、LiDAR、雷達）與新增的空中感測選項，使得同一個世界內可以同時產生地面與空氣的多模態數據。  

🚀 **提供可直接用於訓練與測試的開源工具**  
透過這個統一平台，研究者得以在同一個場景裡訓練既能在道路上導航，也能在低空執行任務的 agent，或是測試它們在空地切換時的感知與決策表現。這降低了搭建複雜雙域實驗的門檻，加速了 embodied intelligence 的跨域探索。  

💡 **使空地協同研究變得更具可行性**  
過去要研究空地協同，常需分別使用兩個模擬器並自行同步資料，過程繁瑣且易產生環境不一致。CARLA-Air 把這兩個世界佈在同一個引擎裡，確保感測資料、物理特性與光照條件完全對齊，讓實驗結果更具可比性與可重複性。  

⚠️ **建立於既有工作之上，創新點在於實用整合**  
評論指出，CARLA-Air 的核心概念建構於現有模擬器的基礎上，其主要貢獻在於提供一個開源、易於擴充的實作工具，讓社群能直接應用於需要空地協同的機器人與自動系統研究。  

🎯 **適合需要同時測地面與空中行為的專案**  
- 若你的工作涉及無人機與地面車輛的協同導航、避障或物流運送，CARLA-Air 提供了一個省時又高保真度的實驗台。  
- 開源特性意味著你可以根據專案需求自行添加感測器、飛行控制器或任務腳本。  

🔗 **論文連結**  
📝 CARLA-Air: Fly Drones Inside a CARLA World -- A Unified Infrastructure for Air-Ground Embodied Intelligence  
🔗 https://huggingface.co/papers/2603.28032  

你有試過在同一個模擬器裡測試空地切換的 agent 嗎？歡迎在留言區分享你的經驗或想法 👇  

#CARLA #無人機 #機器人 #模擬器 #空地協同 #EmbodiedAI #UnrealEngine #開源工具 #HuggingFace Papers
