---
title: NVIDIA Nemotron 3.5 Lightning now available in Amazon SageMaker JumpStart
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/nvidia-nemotron-3-5-lightning-now-available-in-amazon-sagemaker-jumpstart/
model: claude-code/sonnet
generated_at: '2026-08-18T06:32:47.082881'
score: 86
---

📌 30B 模型只啟用 3B 參數，NVIDIA Nemotron 3.5 Lightning 上架 SageMaker JumpStart

TL;DR：專為高頻 agentic 任務設計的開源 MoE 模型，現可在 SageMaker JumpStart 免調度直接部署。

當一個 agent 系統整天在做的事情，是分類警報、從表單擷取欄位、對照政策檢查紀錄，把每一步都丟給前沿大模型處理，等於花前沿模型的成本和延遲，去做一件小模型就能做的事。NVIDIA Nemotron 3.5 Lightning 現在已經上架 Amazon SageMaker JumpStart，鎖定的正是這種高頻、可重複、對速度敏感的 agentic workload。

🤔 **為什麼「一直開著的 agent」需要專用模型**

常駐運作的 agent 會持續蒐集情境、觀察環境、對已知資訊做推理、然後採取行動，這些步驟很多都牽涉模型呼叫，但並非每一步都需要同等能力。規劃多階段工作流程或協調子 agent 可能需要前沿級推理，但分類一則警報、從表單擷取欄位、對照政策做檢查，往往可以交給更小、更專精的模型處理——而這類任務常常佔掉呼叫量的大宗。System-of-models 的做法是把每一步路由給合適的模型，Nemotron 3.5 Lightning 的定位就在這個系統裡高流量的一端。

🧩 **30B 總參數，僅啟用 3B：MoE 架構怎麼幫上忙**

Nemotron 3.5 Lightning 是從 NVIDIA 前沿模型 Nemotron 3 Ultra 蒸餾而來、與 Nemotron Coalition 共同開發的公開基礎模型，採用混合式 Mixture-of-Experts（MoE）架構，並針對主流 agent harness 中的工具使用做了訓練。模型總參數量 30B，但每次前向傳播只啟用其中 3B，因此能在單一支援的 GPU 上運行，讓 agent workflow 裡重複、專精的步驟不需要前沿等級的基礎設施即可執行。NVIDIA 宣稱這是同量級中速度最快的開放模型，在高流量 agentic workload 上可達到最高 4 倍的吞吐量提升與最高 30% 的任務完成加速。

除了 MoE 架構本身，模型還搭配 DFlash 投機解碼（speculative decoding）進一步降低每個 token 的延遲，並提供 1M token 的上下文視窗，讓 agent 在長時間、多輪的 session 中可以攜帶累積狀態，不需要反覆重新建立情境。若你的技術棧中有 NVIDIA NeMo Switchyard，可以用它把工作流程中個別步驟路由到不同模型池，Lightning 適合被選為高流量、專精步驟的執行者。

📊 **NVFP4 與 BF16 的精度落差**

模型同時提供 NVFP4 與 BF16 兩種變體。根據 NVIDIA 發佈的評測（評測配方與指令公開於 NeMo Gym，並在一致的測試框架下測得，結果可能與各廠商自行公布的數字有出入），NVFP4 在多項任務上的準確率與 BF16 相近。作為開放模型，NVIDIA 表示使用者可以用 NeMo 對其進行 post-train，針對自家工具、工作流程與政策做客製化，並保留對訓練後模型權重的所有權，部署在自選環境中；不過本次 SageMaker JumpStart 上架的模型卡並未開放 JumpStart 平臺內的客製化功能。

🧩 **部署方式**

透過 SageMaker JumpStart 部署 Nemotron 3.5 Lightning，不需要自行設定serving 框架，在主控臺搜尋模型名稱、選擇實例類型即可建立端點；也可以直接從 Hugging Face 模型頁面選擇 Deploy → Amazon SageMaker AI 進入相同的部署流程。JumpStart 提供 NVFP4（模型 ID huggingface-reasoning-nemotron-3-5-lightning-30b-a3b-nvfp4）與 BF16（huggingface-reasoning-nemotron-3-5-lightning-30b-a3b-bf16）兩種模型 ID 可選。需注意部署後會建立持續計費的 SageMaker AI 端點，用完務必刪除以避免持續產生費用。

🎯 **實務啟示**

如果你的 agent 系統已經因為把每一步都丟給前沿模型而在成本或延遲上吃緊，Nemotron 3.5 Lightning 提供了一個具體的路由對象：把警報分類、欄位擷取、政策檢查這類高頻、低複雜度的步驟切出來，交給這個開放、可自行 post-train、單 GPU 可跑的模型處理，前沿模型留給真正需要多步推理與跨 agent 協調的工作。

🔗 **來源**
- 標題：NVIDIA Nemotron 3.5 Lightning now available in Amazon SageMaker JumpStart
- 作者／機構：Venu Kanamatareddy, AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/nvidia-nemotron-3-5-lightning-now-available-in-amazon-sagemaker-jumpstart/

#NVIDIA #Nemotron #SageMaker #AWS #MoE #AgenticAI #OpenModel #LLMInference #EdgeDeployment #AIInfrastructure
