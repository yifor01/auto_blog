---
title: Run AI Models for Edge Application Development with Just a Few Commands
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/run-ai-models-for-edge-application-development-with-just-a-few-commands/
model: claude-code/sonnet
generated_at: '2026-10-30T21:46:51.875699'
score: 75
---

📌 幾行指令，在 NVIDIA DGX Spark 上跑通邊緣 LLM

TL;DR：TensorRT Edge-LLM 搭配 trtedge CLI，幾個指令就能在 DGX Spark 上部署並測試邊緣推理模型。

當 AI 走出資料中心，開始監控駕駛員注意力、協助機器人理解環境、協調生產線上的機器艦隊時，模型必須在極其有限的記憶體、功耗與延遲預算內運作。但把一個模型準備到「可以跑」的狀態，往往需要大量環境設定工作，這正是 NVIDIA TensorRT Edge-LLM 想解決的問題。

🤔 從資料中心到邊緣裝置的最後一哩路

NVIDIA DGX Spark（現已推出 64GB 版本）提供嵌入式開發者一個原型、微調與測試模型與代理的平臺。TensorRT Edge-LLM 則是一個專為嵌入式工作負載設計的輕量級 C++ 推理執行環境，讓開發者可以用同一套推理框架，先在 Spark 上開發，再部署到 NVIDIA Jetson Thor、NVIDIA DRIVE AGX Thor、NVIDIA IGX Thor 等平臺。整套流程的入口是一個叫 trtedge 的命令列工具（CLI），它會下載指定模型，並為 Spark 建置最佳化的 TensorRT 推理引擎。

🧩 實際跑一次：用 Nemotron-3.5 Lightning 聊天與架 API

教學以純文字模型 NVIDIA Nemotron-3.5 Lightning 為例。前置需求是一臺搭載受支援 NVIDIA 軟體堆疊的 DGX Spark、NVIDIA CUDA 13、TensorRT 10.16.1.11（10.x 系列內）以上版本，以及 Python 3.10 至 3.12；文中範例在 TensorRT Edge-LLM 0.11.1 與 TensorRT 10.16.1.11 上測試過。

安裝步驟很精簡：建立並啟用虛擬環境後，安裝 tensorrt-edgellm[server]==0.11.1，接著用一行 Python 指令確認 TensorRT 版本相容並能成功載入 Edge-LLM 執行環境。

啟動聊天只需一行指令：
`trtedge chat nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4`

第一次啟動會下載約 21GB 的模型並建置推理引擎（預設存放在 ~/.cache/tensorrt-edgellm），之後的啟動會重複利用已快取的引擎。輸入「Convert 25°C to Fahrenheit. Answer in one sentence.」範例題，模型會回覆「25°C is equal to 77°F.」。

若要把模型包裝成應用程式可呼叫的服務，trtedge serve 會在本機架起一個相容 OpenAI 介面的 API 伺服器，開發者可以用 curl 打 /health/ready 確認伺服器就緒，再透過 /v1/chat/completions 端點以串流方式取得回應。

🧩 用 DSpark 推測解碼加速生成

教學也介紹了 DSpark speculative decoding：讓一個草稿模型（draft model）一次提出多個候選 token，再由主模型一次驗證，藉此加速生成。啟用方式是在 --speculative-config 參數中指定草稿模型與 num_speculative_tokens（範例設為 3），開發者可自行調整草稿 token 數量與其他設定，為自己的工作負載調校生成速度。

📊 DGX Spark 64GB 上的實測數據

| 推測解碼 | 工作負載 | TTFT 中位數（ms） | 平均生成速度（tokens/s） |
|---|---|---|---|
| 關閉 | SpeedBench 1K | 201.0 | 73.3 |
| 關閉 | SpeedBench 2K | 329.5 | 72.8 |
| 關閉 | HumanEval prompts | 98.1 | 73.4 |
| 開啟（DSpark） | SpeedBench 1K | 203.0 | 108.5 |
| 開啟（DSpark） | SpeedBench 2K | 331.6 | 105.3 |
| 開啟（DSpark） | HumanEval prompts | 98.7 | 126.9 |

此表格衡量的是 Nemotron-3.5 Lightning 在 DGX Spark 64GB 上的 time to first token（TTFT）與平均生成速度（不含首個 token 的時間）。測試條件為 DGX OS 7.6.0（Ubuntu 24.04.4 LTS）、NVFP4 精度、開啟 thinking、batch size 為 1、單一串流請求、輸出上限 128 token；DSpark 使用三個草稿 token。SpeedBench 1K、SpeedBench 2K、HumanEval 的平均輸入長度分別為 1,153、2,247、139 個 token。啟用 DSpark 時，系統峰值記憶體用量（含作業系統）為 27.9GB。

⚠️ 限制

文中數據只涵蓋單一並發請求、batch size 1 的情境，實際部署在多請求併發場景下的表現，官方並未在此提供數據。模型下載與引擎建置本身也需要不少磁碟空間與時間，首次啟動體驗不像後續啟動那樣即時。

🎯 實務啟示

對做邊緣 AI 應用（車載、機器人、產線）的工程師來說，這套流程把「模型下載、引擎建置、API 服務」三件事收斂成幾個指令，且同一套 TensorRT Edge-LLM 可以無縫從 Spark 開發環境搬到 Jetson Thor、DRIVE AGX Thor、IGX Thor 等正式部署平臺，值得在評估邊緣推理方案時納入測試清單。

🔗 來源
- 標題：Run AI Models for Edge Application Development with Just a Few Commands
- 作者／機構：Shara Tibken, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/run-ai-models-for-edge-application-development-with-just-a-few-commands/

#NVIDIA #EdgeAI #TensorRT #LLMInference #DGXSpark #JetsonThor #SpeculativeDecoding #Nemotron #OnDeviceAI #PhysicalAI
