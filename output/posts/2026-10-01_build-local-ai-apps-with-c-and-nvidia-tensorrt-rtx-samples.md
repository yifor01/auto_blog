---
title: Build Local AI Apps with C++ and NVIDIA TensorRT RTX Samples
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/build-local-ai-apps-with-c-and-nvidia-tensorrt-rtx-samples/
model: claude-code/sonnet
generated_at: '2026-10-01T22:10:57.879422'
score: 79
---

📌 用 C++ 打造本地 AI 應用：NVIDIA TensorRT RTX 範例全解析

TL;DR：開源 C++ 範例集串接 ONNX Runtime 與 TensorRT RTX，加速本地 AI 應用部署。

把一個訓練好的模型放進本地應用程式，聽起來簡單，實際上要同時搞定可攜的模型格式、穩定的執行階段（runtime），以及能跨平臺運作的硬體加速，三者缺一不可。NVIDIA 釋出的 Do Inference Now（DIN）Deploy，就是一套針對這個痛點而生的開源 C++ 範例集合。

🤔 **解決什麼問題、為誰而做**

DIN Deploy 鎖定的是想把 AI 模型嵌入原生應用程式的開發者。它結合 ONNX Runtime 與 NVIDIA TensorRT RTX 執行提供者（execution provider），協助開發者從一個模型檢查點（checkpoint），一路走到 Windows 與 Linux 上支援硬體加速的原生應用程式。同一套 ONNX Runtime API 也可以透過 WinML 2.0 存取。

🧩 **核心架構：Python 匯出、C++ 落地**

每個 DIN Deploy 範例都從一個 Python 匯出工具開始：下載 Hugging Face 上的模型檢查點，轉換成 ONNX 格式。應用程式端則是建立在 ONNX Runtime 之上的原生 C++ CLI。這種切分方式把「模型轉換」與「部署邏輯」分開，開發者拿到匯出的模型後，不需要依賴特定模型的執行環境就能整合進本地應用程式。

大多數範例程式碼使用 C++ 的 ONNX Runtime session 與張量（tensor）API；CUDA API 與 kernel 等廠商專屬程式碼，只出現在選用的加速路徑裡。只要執行提供者支援所需的 ONNX Runtime 張量 API，共用程式碼就能在其上運作；ORT 的 copy tensor API 也讓資料局部性（data locality）的管理不需要依賴特定廠商 API。在前處理與後處理環節，FLUX.2 範例使用了 ONNX Runtime 1.25 版引入的圖形互通（graphics interop）能力，搭配 Vulkan 與 DirectX 做取樣；其中 DirectX 僅限 Windows 平臺。專案提供 Windows 與 Linux（含 Arm64）的 CMake 預設組態。

**支援的 AI 任務類型**：
- 語音辨識（ASR）：OpenAI Whisper 涵蓋離線轉錄，NVIDIA Parakeet TDT 與 NVIDIA Nemotron ASR Streaming 則提供串流管線，示範如何讓音訊在原生應用程式中流動並即時取得轉錄結果，同時善用 GPU 加速。
- Meta SAM 2.1：支援圖片與影片的互動式遮罩（masking），把模型輸出轉換成原生應用程式可用於選取、追蹤等電腦視覺工作流程的分割遮罩。
- FLUX.2-klein-4B：提供以提示詞驅動的圖片生成，範例同時展示如何用 NVIDIA Model Optimizer 做訓練後量化（PTQ），產生量化版 ONNX 模型；由於 ONNX 介面保持不變，量化模型可以直接替換、不需改動應用程式程式碼。

📊 **DGX Spark 上的 GPU／CPU 效能對比**

| 模型 | GPU（DGX Spark） | CPU（DGX Spark） |
|---|---|---|
| openai/whisper-large-v3-turbo | 58.5 倍實時 | 3.8 倍實時 |
| nvidia/nemotron-3.5-asr-streaming-0.6b | 39.01 倍實時 | 3.24 倍實時 |
| nvidia/parakeet-tdt-0.6b-v3 | 206.41 倍實時 | 14.44 倍實時 |
| facebook/sam2.1-hiera-base-plus | 38.3 FPS | 0.5 FPS |

（音訊任務以相對即時倍數呈現，數字越高代表越快）

🎯 **實務啟示**

想要上手的開發者可以直接從儲存庫提供的 CMake 預設組態開始，設定並建置專案後，把模型匯出為 ONNX，再用 TensorRT RTX 執行 CLI，或是直接把範例程式碼搬進自己的應用程式。CMake 預設會自動下載 ONNX Runtime 與 TensorRT RTX，省去不少環境建置的麻煩。對於要在 Windows／Linux 原生應用程式中整合語音辨識、影像分割或生成式影像功能的團隊，這套範例提供了可直接參考的落地路徑。

🔗 **來源**
- 標題：Build Local AI Apps with C++ and NVIDIA TensorRT RTX Samples
- 作者／機構：Luca Spindler（NVIDIA Developer）
- 連結：https://developer.nvidia.com/blog/build-local-ai-apps-with-c-and-nvidia-tensorrt-rtx-samples/

#NVIDIA #TensorRT #ONNXRuntime #CPlusPlus #LocalAI #EdgeAI #SpeechRecognition #ImageGeneration #Quantization #OnDeviceAI
