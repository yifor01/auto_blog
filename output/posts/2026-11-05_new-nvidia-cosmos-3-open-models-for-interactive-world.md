---
title: New NVIDIA Cosmos 3 Open Models for Interactive World Simulation
source: HuggingFace Blog
url: https://huggingface.co/blog/nvidia/cosmos-interactive-world-simulation
model: claude-code/sonnet
generated_at: '2026-11-05T23:00:10.522314'
score: 96
---

📌 NVIDIA開源Cosmos 3四款世界模型,讓機器人預演「如果這樣做會怎樣」

TL;DR:NVIDIA開源四個Cosmos 3 Nano checkpoint,用文字、模擬器控制或機器人動作生成逼真影片,打造可互動的世界模擬環境。

機器人或自駕政策在真正上路之前,最想知道的問題是:「如果我這樣做,世界會怎麼回應?」NVIDIA的Cosmos世界模型平臺這次新增四個開放權重checkpoint,正是為了回答這個問題,涵蓋互動式世界模擬與多感測器、多視角的駕駛場景生成。

🤔 **為什麼機器人與自駕研究需要這類模型**

機器人需要能在不斷變化的場景與視角下回答「接下來會發生什麼」的環境模擬;自駕研究則需要外觀與幾何能互相對應的場景,也就是視覺觀測要和3D感測(如LiDAR)一致。每一次觀測又會影響下一步動作,因此串流式生成需要能把影片預測和持續互動串接起來。

🧩 **四個checkpoint各司其職**

四款模型都是Cosmos 3 Nano的post-trained版本,具備16B可訓練參數,採用OpenMDW1.1授權,允許商用與非商用用途。

- Cosmos3-Nano-Transfer-Auto:雙向模型,用於離線合成駕駛資料生成,能同步產生最多11個camera視角(含魚眼鏡頭)的影片,並支援RGB與LiDAR聯合生成。每個camera用World Scenario Map(WSM)控制場景結構與交通動態,文字提示則引導外觀,也可選擇提供初始RGB影像來固定場景外觀;聯合LiDAR生成還會用上對齊的HD-map range-map控制。它同時是把Cosmos適配到自有感測器配置的基礎:先在自己的資料上post-train,再經過causal training與少步數蒸餾,就能做成串流即時模擬版本。
- Cosmos3-Nano-Sim-Auto:Transfer-Auto的causally distilled串流版本,只用少數幾個denoising步驟就能連續生成一小段一小段同步的camera影片與LiDAR,靠已生成的歷史與更新後的駕駛控制支援快速串流與長時間的互動rollout。
- Cosmos3-Nano-Sim-Transfer:把模擬器算出的空間控制訊號(深度、分割、邊緣、模糊等)與一段文字提示,轉換成策略可消費的彩色觀測影像,流程大致是:動作 → 模擬器更新 → 空間控制訊號 → 生成RGB影像 → 策略下一步動作。文字負責引導外觀,物理與真實狀態仍由模擬器掌握。
- Cosmos3-Nano-Sim-Bimanual:根據雙臂機器人的動作模擬環境如何演變,支援YAM與AgiBot兩種機身的互動式雙臂模擬,可由策略或人類操作搖桿控制,從一張起始影像出發,移動機器人或攝影機就能生成下一幀觀測。

🧩 **核心架構:Mixture-of-Transformers加上時序因果attention**

Cosmos 3的骨幹是Mixture-of-Transformers,透過attention把獨立的文字處理網路與視覺生成網路連接起來。生成器根據提示詞、可用控制訊號與已生成的歷史,預測每個短片段,流程是:控制訊號加歷史 → 生成片段 → 解碼成影像 → 更新歷史。Denoising會把帶噪、壓縮過的影片表示還原成一個片段;時序因果attention讓模型能讀取已有的歷史與控制訊號,同時擋住尚未發生的目標觀測,並用key/value cache保留attention資訊供下一次預測使用。模型實際操作的是壓縮後的影片表示「latent」,初始影像之外,每個latent時間步代表4個RGB影格;Transfer系列每個片段預測1步,技術報告中提到的最佳化版Bimanual設定則預測2步,片段越小,新的控制訊號就能越頻繁地影響生成結果。

📊 **怎麼開始用**

每個checkpoint都附有對應的open skill與notebook可以直接跑推理:Transfer-Auto、Sim-Auto、Sim-Transfer、Sim-Bimanual各自有獨立的推理指引。其中Sim-Bimanual的範例使用59個控制數值(訓練時補齊到64個),有明確定義座標系、旋轉、夾爪校準、有效性遮罩與控制範圍的schema,使用時需遵循這套慣例,並確保時間對齊(T個transition需要T+1個觀測)。運行環境需要Linux、NVIDIA GPU、Docker與NVIDIA Container Toolkit,官方公開的vLLM-Omni設定是在單顆GB200上測試的,但這並非最低記憶體需求。

⚠️ **這些問題仍然困難**

NVIDIA在文章中坦言,接下來的工作是去衡量這些模型在哪些地方真正能支援policy learning與評估、理解模型的限制,並在不足之處持續改進,開放權重與post-training方法只是提供一個共享的起點。

🎯 **實務啟示**

如果手上的感測器配置或機器人機身跟官方預訓練的設定不同,官方建議的路徑是先用自己的資料post-train Transfer-Auto,再做causal training與蒸餾變成Sim-Auto,而不是直接從頭訓練,這對想把世界模型接到自有硬體的團隊是相對務實的切入點。

🔗 **來源**
- 標題:New NVIDIA Cosmos 3 Open Models for Interactive World Simulation
- 作者/機構:NVIDIA(Pranjali Joshi、Rick Z、Yao Xu等人),發布於Hugging Face Blog
- 連結:https://huggingface.co/blog/nvidia/cosmos-interactive-world-simulation

#NVIDIA #Cosmos #WorldModel #Robotics #AutonomousDriving #OpenWeights #HuggingFace #MixtureOfTransformers #SimToReal #GenerativeVideo
