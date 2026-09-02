---
title: 'Introducing @huggingface/kernels: 200+ WebGPU Kernels for Local AI'
source: HuggingFace Blog
url: https://huggingface.co/blog/webgpu-kernels
model: claude-code/sonnet
generated_at: '2026-09-02T10:08:32.875382'
score: 91
---

📌 Hugging Face 開源 @huggingface/kernels：瀏覽器端 207 個 WebGPU 核心函式庫

TL;DR：Hugging Face 把 WebGPU 核心做成可測試、可版控的獨立套件，瀏覽器推論實測快 2.57 倍。

瀏覽器裡跑 AI 模型，最終都會被拆解成一連串 GPU 運算：矩陣乘法、正規化、卷積、attention 原語、量化運算等等。問題是，WebGPU 雖然讓這些運算能跨瀏覽器執行，但「能跑」跟「跑得快」是兩回事，Hugging Face WebAI 團隊這次先從最底層的核心函式庫下手。

🤔 **可攜性不等於效能**

WGSL（WebGPU Shading Language）提供了跨瀏覽器的共通 shader 語言，但同樣的運算、同樣的輸出，兩個 shader 實作在不同加速器上的表現可能天差地遠。workgroup 大小、記憶體存取模式、向量化、資料型別、fusion 策略都會影響效能，而且最佳選擇還會隨輸入形狀、裝置、瀏覽器、可用的 WebGPU 特性而改變。這正是為什麼核心函式庫需要被當成獨立的基礎層來對待：只要把運算做成可獨立發現、可測試、可基準測試、可版控的單元，上層 runtime 就能專注於排程，而底層實作可以獨立演進。

🧩 **每個核心都是一個完整的套件，不只是一段 shader**

Hugging Face 這次發布 @huggingface/kernels，一個用來從 Hugging Face Hub 載入並執行最佳化 WebGPU 核心的最小函式庫，搭配 huggingface.co/webgpu-kernels 上首批 207 個核心，全部採 Apache-2.0 授權，各自獨立成一個 repository。每個核心的 repository 內都包含：

- manifest.json：定義輸入、輸出、屬性、型別限制與形狀推導規則的操作契約
- metadata.json：記錄核心識別碼、digest 與來源
- test.json：正確性測試案例
- bench.json：用於評估的基準測試與調校案例
- *.wgsl.jinja：產生 shader 的參數化 WGSL 實作範本

以 ai.onnx.Add（逐元素加法，支援多方向廣播）為例，其 kernel card 記錄了兩個輸入、廣播後的輸出形狀、支援的資料型別，以及針對不同形狀與裝置提供的變體，包括同形狀直接相加、向量化廣播、純量處理與一般廣播四種實作路徑，讓 runtime 能在不改變應用端 API 的情況下，依當下呼叫與裝置自動選擇合適實作。

Hugging Face 同時推出 Fleet，一個瀏覽器內的 GPU 基準測試與測試套件，能在使用者自己的硬體上執行並評分這些核心。使用者同意後，每次執行都會回傳私有的正確性與效能證據，幫助團隊找出錯誤結果、異常緩慢的案例，並改善核心變體與最佳化決策，這是傳統測試實驗室難以覆蓋到的真實硬體多樣性。

📊 **實測：跟 ORT WebGPU 相比快 2.57 倍**

Hugging Face 在 Apple M4 GPU 上，用 ONNX Runtime Web 1.30.0-dev.20260826-b1f76d586a 版本，將自家核心與 ORT WebGPU 做頭對頭比較。從全部 207 個運算、1,756 個測試案例中，篩選出雙方輸出一致且計時可靠的 809 個案例，在這些案例上，Hugging Face 的核心以幾何平均計算快了 2.57 倍。

💡 **怎麼用：一行安裝，呼叫模式不變**

安裝方式為 npm install @huggingface/kernels@preview，執行環境需要支援 WebGPU 的瀏覽器，可以在 JavaScript 中用 "gpu" in navigator 檢查。使用方式是呼叫 getKernel 搭配 Hub repository ID 與契約版本號，取得函式後直接傳入型別化的輸入資料與張量形狀：

```javascript
import { getKernel } from "@huggingface/kernels";

const add = await getKernel("webgpu-kernels/ai.onnx.Add", { version: 1 });
const { c } = await add({
  a: { data: new Float32Array([1, 2, 3, 4, 5, 6]), shape: [2, 3] },
  b: { data: new Float32Array([10, 20, 30]), shape: [3] },
});
```

第二個輸入會沿第一維度廣播，產生形狀 [2, 3] 的輸出，輸出形狀與邏輯資料型別皆由 manifest 契約搭配輸入自動推導。這個加法範例刻意選得很小，GPU 往返成本遠高於運算本身，重點在於呼叫模式：無論是這種輕量運算，還是矩陣乘法（ai.onnx.MatMul）這類真正吃重最佳化的運算，呼叫方式完全一致，只有 repository ID 與輸入內容不同。這裡的 version: 1 指的是核心契約版本，與 ONNX opset、算子的 since_version、或模型版本是各自獨立的概念，讓應用端可以依賴穩定的 JavaScript 介面，底層實作則能持續演進。

🎯 **實務啟示**

對正在做瀏覽器端推論或 WebGPU runtime 整合的工程師而言，這批核心可以直接當成生產可用的最佳化實作來用，也可以當成自行開發 WebGPU 核心時的參考實作。由於每個核心都附帶正確性測試與基準測試案例，導入前可以直接用同一套契約驗證行為是否符合預期，不必自行重造測試基礎設施。

🔗 **來源**
- 標題：Introducing @huggingface/kernels: 200+ WebGPU Kernels for Local AI
- 作者／機構：Nico Martin, Joshua Xenova, Hugging Face
- 連結：https://huggingface.co/blog/webgpu-kernels

#WebGPU #HuggingFace #BrowserAI #OpenSource #EdgeAI #MachineLearning #WebDev #JavaScript #Inference #WGSL
