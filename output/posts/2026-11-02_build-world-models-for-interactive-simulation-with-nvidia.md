---
title: Build World Models for Interactive Simulation with NVIDIA Cosmos
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/build-world-models-for-interactive-simulation-with-nvidia-cosmos/
model: claude-code/sonnet
generated_at: '2026-11-03T00:05:32.250381'
score: 91
---

📌 NVIDIA Cosmos：世界模型從訓練到部署一條龍

TL;DR：NVIDIA Cosmos Framework 把訓練、強化學習、推理最佳化與NIM服務化整合成一套流程，加速物理AI世界模型落地。

物理AI開發者要讓世界模型真正派上用場，中間卡著兩道關：如何把模型調整成貼合自己的感測器與任務，以及如何把調好的模型穩定地塞進應用程式裡跑起來。NVIDIA最近把這兩個問題一次打包進Cosmos平臺。

🤔 背景：訓練與部署，兩道分開的關卡
物理AI開發者面對的第一道關卡,是把世界模型（world model）調整到符合自己的感測器、任務與資料；第二道關卡,則是如何讓調好的模型可靠地跑進應用程式。Cosmos平臺用兩塊拼圖分別處理：Cosmos Framework提供訓練、資料處理、最佳化與推理用的agent skills與recipe；Cosmos NIM microservices則透過應用程式API做GPU加速的服務化部署。

🧩 訓練、強化學習到推理，一套框架全包辦
Cosmos Framework是開放且模組化的框架,涵蓋世界模型從訓練、最佳化到推理的完整生命週期,並以新的agent skills驅動。除了原本的Cosmos 3,現在也擴展支援NVIDIA Alpamayo、GR00T、Qwen、pi0.5等相容Hugging Face模型。

訓練端可以用文字、影像、影片、音訊與動作資料訓練模型,支援LoRA做參數效率的adaptation,或完整的supervised fine-tuning（SFT）更新所有參數;資料可透過JSONL、WebDataset、LeRobot或自訂adapter載入,並支援跨GPU訓練與checkpoint續跑。

強化學習部分現在同時涵蓋online與offline RL路徑,支援的pipeline包括:DPO做offline偏好最佳化;GRPO是搭配規則或模型reward、用vLLM rollout的online RL;PPO是actor-critic RL,搭配frozen reference與critic,也能用於模擬環境中訓練embodied policy;OPD是從frozen teacher做on-policy distillation;DiffusionNFT則是針對diffusion世界模型的online RL。這些角色（rollout、reward、training）可以共用GPU,也能分開用獨立資源池運作,並能接上支援的模擬器收集經驗。

最佳化與推理端,可以用distillation縮小模型或減少生成步數,或用量化（quantization）降低記憶體用量;相容的checkpoint能跑在Hugging Face Diffusers、PyTorch、SGLang、vLLM-Omni、vLLM、TRT-LLM、TRT-Edge-LLM,或直接用NVIDIA NIM服務化。

📊 四張GPU跑出七支環景影片與LiDAR點雲
文中給出具體的模擬範例:用Cosmos3-Nano-Transfer-Auto(雙向生成的offline合成資料checkpoint)在四個GPU上,透過torchrun搭配cosmos_framework.scripts.inference,輸入七支同步的World Scenario Map(WSM)影片、每個camera的caption、首幀RGB條件與HD-map LiDAR控制,參考流程跑出的結果是七支720p、每支297幀(30 FPS)的影片,以及99個LiDAR sweep。驗證時需檢查sample_outputs.json是否成功、lidar.safetensors的數值是否finite,並確認WSM與多camera/LiDAR之間的對齊一致性。

另一個版本Cosmos3-Nano-Sim-Auto,是Transfer-Auto的causal、few-step-distilled變體,支援自回歸(autoregressive)串流生成:隨著AV policy或人類駕駛輸入透過WSM renderer更新場景,模型逐步產生觀測,生成的camera與LiDAR畫面再回饋給policy,形成closed-loop評估迴路。

💡 同一套WSM控制,換個prompt就能換天氣
AV模擬的兩個checkpoint都吃prompt與WSM控制(代表車道、物體、道路標誌、路緣等),聯合RGB-LiDAR生成還額外使用HD-map rangemap控制,也可選擇輸入初始LiDAR觀測。Prompt裡描述天氣、光線、時間、路況,前面再加camera-rig與視野資訊;也可選擇性提供初始camera影像引導畫面外觀。文中舉例,只要改prompt就能把同一段白天行駛畫面換成雨夜,同時保留一樣的道路配置與車輛軌跡,用這種變化訓練和評估感知與駕駛模型在不同天氣光線下的表現。

⚠️ 目前聚焦特定硬體與場景
這些checkpoint目前在NVIDIA Hopper與Blackwell GPU上測試,新recipe聚焦在Cosmos 3 Nano系列(機器人模擬、場景生成、多camera駕駛模擬、手術policy評估),若要套用到自訂感測器、action space或資料領域,仍需依照post-training guide額外調整。

🎯 實務啟示
如果你的團隊正在做自駕或機器人的感知/決策模型,Cosmos Framework提供的是一條可以直接從已發布checkpoint開始跑的路徑:先用agent skills做smoke test驗證環境,再評估在held-out資料上與base model的差異,甚至比較不同精度下的品質、記憶體與延遲的取捨,不用從零打造訓練與模擬pipeline。

🔗 來源
- 標題：Build World Models for Interactive Simulation with NVIDIA Cosmos
- 作者／機構：Elizabeth Goodman, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/build-world-models-for-interactive-simulation-with-nvidia-cosmos/

#NVIDIA #Cosmos #WorldModels #PhysicalAI #Robotics #AutonomousVehicles #Simulation #ReinforcementLearning #NIM #GenerativeAI
