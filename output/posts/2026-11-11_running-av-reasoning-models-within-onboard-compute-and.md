---
title: Running AV Reasoning Models Within Onboard Compute and Latency Limits
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/running-av-reasoning-models-within-onboard-compute-and-latency-limits/
model: claude-code/sonnet
generated_at: '2026-11-11T23:53:54.574419'
score: 88
---

📌 2B 參數的車載模型，如何在 Thor 晶片上即時推理

TL;DR：NVIDIA Alpamayo 2 Edge 是專為車載運算與延遲限制設計的自駕推理 VLA 模型，搭配閉環強化學習後駕駛表現提升 48.9%。

自駕系統要在車上有限的運算資源與嚴苛的延遲預算內完成推理,大模型可以當作能力的起點，但要真正搬上車,還得想辦法縮小模型、保留住有用的推理能力，並在目標硬體上實測驗證才算數。

🤔 **把推理模型搬上車的真正難題**

核心問題是：當模型尺寸被壓縮以符合車上算力與延遲限制時，要如何保留住推理品質與駕駛行為的水準?這需要一套能夠衡量「推理品質」的方法，並把衡量結果回饋到模型改進的流程裡。

🧩 **Alpamayo 2 Edge 的技術組合**

NVIDIA Alpamayo 2 Edge 是一款自適應推理的 vision-language-action（VLA）模型，設計目標是在 NVIDIA DRIVE AGX Thor 上實時運作。它建構於 NVIDIA Cosmos 3 Edge 的 2B 參數 Nemotron 推理骨幹之上，搭配一個 diffusion action expert，利用環景相機觀測、時間上下文與導航輸入，生成 Chain-of-Causation（CoC）推理與未來行駛軌跡。

它的「自適應」體現在：只在必要時才生成推理內容，一般行駛情境下會直接輸出特殊的 `<NOMINAL>` token 取代完整推理，藉此減少不必要的 token 生成與推理運算量。模型在 NVIDIA AlpaGym 中以閉環強化學習進行後訓練，相較於沒有閉環 RL 的最佳 checkpoint，閉環駕駛表現提升了 48.9%。

其他技術特點包括：以 Alpamayo 2 Super 生成的 CoC 推理自動標註進行離線蒸餾；多解析度輸入以有效率地線上編碼環景觀測；搭配 DFlash2 的推測解碼（speculative decoding），在不犧牲品質的前提下加速線上推理；以及針對 NVIDIA TensorRT 與 TensorRT-Edge-LLM 的量化與推理加速配方。

官方提供的推理程式片段顯示了實際運作流程：載入模型後，先用環景相機觀測、導航文字與歷史 ego-motion 準備模型輸入，再透過 `model.sample_trajectories_from_data` 搭配 top_p、temperature 等取樣設定與 diffusion 推理步驟，最終輸出未來軌跡（xyz、旋轉）以及推理過程。

為了驗證推理品質，團隊同時推出 NVIDIA AlpaJudge，一套經人類校準的評估與獎勵模型，用於評估推理軌跡、挑選更有價值的訓練資料，並在強化學習階段提供獎勵訊號。

📊 **對比 Qwen-Drive-1.0 與夥伴實測成果**

官方將 Alpamayo 2 Edge（2B）與 Qwen-Drive-1.0（4B）在閉環駕駛、開環軌跡預測、場景理解與推理等基準上進行比較，其中 Alpamayo 2 Edge 在 AlpaSim 中達到約 60 倍於對照模型的「兩次疑似肇責事件之間的行駛距離」。

早期合作夥伴的實測回饋提供了具體數字：
- PORT（CTO Matas Simonavicius）在倫敦街景的 NuRec 重建場景中測試，Alpamayo 2 Edge 的保持車道成功次數是 Alpamayo 1.5 的兩倍以上，從偏離車道中恢復的頻率高出約 40%，在同一張 GPU 上的規劃速度大約是手動調校的 Alpamayo 1.5 伺服器版的兩倍。
- Niulinx（共同創辦人兼動作規劃負責人 Luca Crotti）在感測器配置差異顯著的情況下，zero-shot 評估中位移誤差（minADE）比 Alpamayo 2 Super 降低 13.6%，3 秒時的側向預測誤差（RMSE）降低 46.1%；在自家資料上微調後，位移誤差相較 Edge 基準再降 44.2%；收到模型後僅幾天就在真實車輛上完成首次測試。
- Embedl（CEO 兼共同創辦人 Hans Salomonsson）在不到 48 小時內，讓 Alpamayo 2 Edge 在 AGX Thor 上以 10 Hz 的速度實現即時規劃。

💡 **BF16 預設就能跑，但真正上車還要再優化**

從 Hugging Face 下載的 Alpamayo 2 Edge 權重預設為 BF16，可以直接作為 PyTorch 模型在任何支援的 NVIDIA GPU 上執行；但要在 DRIVE AGX Thor 上達到即時運作，仍需要進一步的推理最佳化，這也是官方特別提供 TensorRT 與 TensorRT-Edge-LLM 量化配方的原因。

🎯 **實務啟示**

對自駕系統工程團隊而言，Alpamayo 2 Edge 展示了一套可參考的完整工作流程：自適應推理降低例行駕駛情境下的運算量、AlpaGym 的閉環 RL 後訓練提升駕駛表現、AlpaJudge 負責資料篩選與獎勵訊號，再搭配推測解碼與量化配方把模型壓進車載晶片的延遲預算。這些環節環環相扣，為「如何在縮小模型的同時不犧牲推理品質」提供了具體可複製的方法，而不只是停留在理論層面。

🔗 **來源**
- 標題：Running AV Reasoning Models Within Onboard Compute and Latency Limits
- 作者／機構：Marco Pavone（NVIDIA）
- 連結：https://developer.nvidia.com/blog/running-av-reasoning-models-within-onboard-compute-and-latency-limits/

#AutonomousVehicles #NVIDIA #EdgeAI #VLA #ReinforcementLearning #DRIVEAGXThor #Robotics #ReasoningModels #Quantization #SelfDriving
