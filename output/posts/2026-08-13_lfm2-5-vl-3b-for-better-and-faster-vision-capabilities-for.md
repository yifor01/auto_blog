---
title: LFM2.5-VL-3B for Better and Faster Vision Capabilities for the Edge
source: HuggingFace Blog
url: https://huggingface.co/blog/LiquidAI/lfm2-5-vl-3b
model: claude-code/sonnet
generated_at: '2026-08-13T07:28:28.928072'
score: 108
---

📌 【LiquidAI】3B 模型讀懂螢幕,邊緣裝置也能跑

TL;DR:LFM2.5-VL-3B 是主打邊緣裝置的視覺語言模型,強化螢幕理解、物件定位與工具調用,同時維持高速直答。

當多數視覺語言模型還在比誰的推理鏈更長、參數更大時,LFM2.5-VL-3B 反其道而行:它不推理,直接回答,把速度留給裝置端的即時應用。

🤔 **為邊緣裝置而生的多模態模型**

LFM2.5-VL-3B 是 LiquidAI 目前最強的可自架視覺語言模型,能同時理解文件與螢幕畫面,具備物件定位(grounding)能力,並支援工具調用(function calling)。相較於前一代,它在四個方向做出改進:螢幕與 UI 理解(涵蓋不同裝置的數位畫面)、更精準的物件定位與自然語言查詢、跨多張圖片的推理能力,以及大幅強化的工具調用能力(涵蓋純文字與圖文混合情境)。它的設計選擇直接回答而不進行推理鏈,讓回應在即時與裝置端應用中保持低延遲。

🧩 **架構與訓練:34T tokens,詞彙表翻倍**

模型搭配 SigLIP2 400M NaFlex 視覺編碼器,與 LFM2.5-2.6B 文字模型相同的預訓練骨幹。預訓練資料量約 34T tokens,視覺資料量是前代的 4 倍,取材自經過篩選與合成的圖說、OCR、物件定位與指令遵循資料集。為了支援非拉丁語系文字,團隊將詞彙表從原本規模翻倍至 128K,做法是就地擴充既有 tokenizer,而非重新訓練。後訓練分兩階段進行:第一階段是監督式微調(SFT),結合來自更大教師模型的知識蒸餾,以及所謂的 Antidoom 訓練;第二階段則是多重獎勵的強化學習(RL)。

📊 **同尺寸最強,螢幕理解尤其突出**

在涵蓋一般視覺理解、多語言、視覺數學與科學推理、文件理解、物件定位、多圖推理與螢幕理解的評測中,LFM2.5-VL-3B 在同尺寸模型中整體平均分數達到 69.4,追平參數量更大的 InternVL 3.5 4B。部分關鍵指標如下:

| 任務 | 基準測試 | LFM2.5-VL-3B (3.1B) | LFM2-VL-3B (3.1B) | Qwen3.5-4B (4.7B) |
|---|---|---|---|---|
| 一般理解 | MMBench (dev EN v1.1) | 81.0 | 80.0 | 78.4 |
| STEM | MathVista (mini) | 68.5 | 62.1 | 63.6 |
| 物件定位 | RefCOCO-avg | 87.9 | 57.1 | 86.6 |
| GUI | ScreenSpot-v2 Mobile | 81.2 | 7.6 | 81.4 |
| 多圖推理 | MuirBench | 58.3 | 34.9 | 62.0 |

其中 ScreenSpot 與 RefCOCO 的躍進最引人注目,較前代 LFM2-VL-3B 有數十個百分點的提升,顯示這一代訓練特別針對螢幕與定位任務加強。在純文字的工具調用測試中,LFM2.5-VL-3B 在 ToolSandbox 與 BFCL V4 上與 Gemma-4-E2B、Qwen3.5-2B 相當。

⚡ **推理速度:M5 Max 上跑 228 tokens/s**

在裝置端推理,LFM2.5-VL-3B 於 M5 Max 上解碼速度達 228 tokens/s,在 Ryzen AI Max+ 395 上為 116 tokens/s,僅需約 3GB 記憶體;在 Galaxy S26 Ultra 上也能達到 20 tokens/s,代表可以完全在裝置端離線運行。GPU 推理方面,它在多張圖片輸入情境下延遲最低,輸出吞吐量在所有受測模型中也最快,高併發下可達約 11K tokens/秒,大約是同屬 4B 級模型的 2 倍,單張 H100 上每日輸出量可接近 1B tokens。模型已支援 llama.cpp、MLX、vLLM、SGLang、ONNX 等推理生態系統。

🎯 **適合高流量、裝置端的實務場景**

如果你的應用需要在裝置端處理高流量的視覺任務,例如螢幕自動化、文件 OCR 或需要工具調用的視覺 agent,LFM2.5-VL-3B 的直答設計與低記憶體需求是明確的優勢。透過 `transformers>=5.10.1` 即可載入使用,官方文件也提供多圖輸入、定位、OCR、工具調用的範例。

🔗 **來源**
- 標題:LFM2.5-VL-3B for Better and Faster Vision Capabilities for the Edge
- 作者/機構:LiquidAI(HuggingFace Blog)
- 連結:https://huggingface.co/blog/LiquidAI/lfm2-5-vl-3b

#VisionLanguageModel #EdgeAI #OnDeviceAI #LiquidAI #LFM #MultimodalAI #ScreenUnderstanding #FunctionCalling #ModelRelease #OpenWeights
