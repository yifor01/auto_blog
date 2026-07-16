---
title: 'Google Releases LiteRT.js: A JavaScript Binding of LiteRT That Runs .tflite
  Models in Browsers via WebGPU'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/15/google-releases-litert-js-a-javascript-binding-of-litert-that-runs-tflite-models-in-browsers-via-webgpu/
score: 94
model: tencent/hy3:free
generated_at: '2026-07-16T08:15:56.971555'
---

📌 【Google 發布】LiteRT.js：用 WebGPU 在瀏覽器跑 .tflite 模型

TL;DR：Google 推出 LiteRT.js，把原生推理執行環境搬進瀏覽器，宣稱最高快 3 倍。

當大多數前端 AI 方案還在用 JavaScript 寫的運算核心苦苦撐著效能，Google 直接把原生 runtime 編譯進 WebAssembly，讓瀏覽器也能吃到硬體加速的紅利。

🤔 **從 TensorFlow Lite 改名而來的在地推理庫**

LiteRT 是 Google 的裝置端（on-device）推理函式庫，前身就是 TensorFlow Lite。這次推出的 LiteRT.js 是它的 JavaScript 繫結（binding），能直接在瀏覽器內執行 .tflite 模型。推理全程留在本地端，Google 指出這帶來更好的使用者隱私、零伺服器成本，以及極低延遲。

🧩 **不是新格式，而是把原生 runtime 編譯成 Wasm**

LiteRT.js 並沒有發明新的模型格式。Google 做法是把現有的原生跨平臺 runtime 編譯為 WebAssembly（Wasm），再暴露給 JavaScript 使用。過去的網頁 AI 方案（如 TensorFlow.js）依賴 JS-based kernels，Google 認為那些效能較差；LiteRT.js 則原封不動帶入原生 runtime 的最佳化，讓網頁應用直接繼承 Android、iOS、桌面端已做的效能升級、量化改善與硬體最佳化。

⚠️ **委派規則：要麼全給加速器，要麼退回 CPU**

LiteRT.js 針對三種後端（backends）排程，且有兩條硬性規則：
- 不支援 partial delegation：計算圖不能拆分到 CPU 與 GPU 上混合執行。
- 每個模型是 all-or-nothing 委派：若模型無法完全委派給選定的加速器，就整個退回 wasm 的 CPU 路徑執行。
- CPU 路徑擁有最廣的運算元（operator）涵蓋率。

📊 **官方宣稱的效能資料與測試環境**

Google 團隊給出兩組對比結果：
- 對比其他網頁 runtime：CPU 與 GPU 推理最高快 3 倍，涵蓋傳統電腦視覺與音訊處理模型。
- 對比自身 CPU 執行：改用 GPU 或 NPU 可獲得 5–60 倍加速，適用於物件追蹤、音訊轉錄等即時任務。

兩項基準都在受控瀏覽器環境、2024 年 MacBook Pro（M4 Apple Silicon）上跑。Google 也提醒，實際結果會因本地 GPU、熱節流（thermal throttling）與驅動最佳化而異。另外，隨發布流傳的「10x」數字並未出現在官方公告中。

💡 **PyTorch 轉檔有一道嚴格前提**

LiteRT Torch 可單步將 PyTorch 模型轉成 .tflite，但 README 指出前置條件相當嚴格（摘要在此截斷，未說明具體限制）。

🎯 **實務啟示**

對前端與邊緣推論工程師來說，若產品已在 Android/iOS/桌面用 LiteRT 並累積最佳化，現在能用同一套 .tflite 直接進瀏覽器、吃到 WebGPU 加速，且不用重訓練或換格式。但部署前要注意：模型必須能整張圖委派給加速器，否則會靜默退回 CPU；對運算元覆蓋率要求高的場景，先確認 CPU 路徑是否支援。

🔗 **來源**
- 標題：Google Releases LiteRT.js: A JavaScript Binding of LiteRT That Runs .tflite Models in Browsers via WebGPU
- 作者／機構：Michal Sutter
- 連結：https://www.marktechpost.com/2026/07/15/google-releases-litert-js-a-javascript-binding-of-litert-that-runs-tflite-models-in-browsers-via-webgpu/

#LiteRT #WebGPU #Wasm #TensorFlowLite #BrowserInference #OnDeviceAI #JavaScript #TFLite #EdgeAI #Google
