---
title: 'AnyLanguageModel 1.0: One Year of Local Models on Apple Platforms'
source: HuggingFace Blog
url: https://huggingface.co/blog/anylanguagemodel-1-0
model: claude-code/sonnet
generated_at: '2026-10-20T20:55:28.803758'
score: 83
---

📌 AnyLanguageModel 滿一週年:一行 import 切換任意模型

TL;DR：Hugging Face 的 AnyLanguageModel 滿週年推出 1.0,讓 Apple 平臺 App 用同一套 API 切換本地與雲端模型。

去年 11 月,Hugging Face 發表了 AnyLanguageModel,一年後的今天,它迎來 1.0 版本,連同 swift-huggingface 與 swift-xet 一起升級。對 Apple 平臺開發者而言,這代表「本地模型還是雲端 API」這個選擇,終於不再需要為每種方案重寫一套串接程式碼。

🤔 **開發者想用本地模型,但不想自己兜串接層**

AnyLanguageModel 的起點,是開發者社群的回饋:大家對本地模型感興趣,卻不確定如何上手,也想避免同時支援多種推論供應商帶來的額外複雜度。本地推論與雲端推論各有優勢,統一的 API 讓開發者能依任務選擇合適的模型,而不被綁死在單一方案上。

🧩 **作為 Foundation Models 的 drop-in replacement**

核心設計沒有變:AnyLanguageModel 是 Apple Foundation Models 框架的 drop-in replacement,只要把 import FoundationModels 換成 import AnyLanguageModel,原本的 session 程式碼就能無縫搭配系統內建模型、透過 llama.cpp / MLX / Core ML 執行的開源權重模型,以及下方列出的多家雲端供應商。

過去一年新增的主要能力包括:工具呼叫(tool calling)對所有供應商皆可用;guided generation 同樣對所有供應商可用,且支援巢狀的 @Generable 型別與其陣列;圖片支援讓開發者可以用 Foundation Models 27 的語法把圖片附加進 prompt,這在 iOS、macOS、visionOS 27 上搭配系統內建模型時也適用;在 OS 27 上,AnyLanguageModel 還能搭配任何符合 Foundation Models 的 LanguageModel protocol 的模型,包含 Core AI 模型。同時,團隊也發展出 swift-huggingface 與 swift-xet,為 Swift App 帶來來自 Hub 的加速模型下載。

雲端模型支援也擴大了,目前涵蓋:OpenAI 的 Chat Completions 與 Responses API;Open Responses,適用於任何相容端點的供應商;Anthropic 的 Messages API,支援 adaptive thinking 與 effort 選項;Google 的 Gemini API;Ollama;OS 27 上的 Private Cloud Compute;以及 Hugging Face Inference Providers 和其他 OpenAI 相容端點(例如 OpenRouter),可透過自訂 base URL 串接。例如要透過 Inference Providers 使用裝置上跑不動的大型開源模型,只需要:

```swift
let model = OpenAILanguageModel(
    baseURL: URL(string: "https://router.huggingface.co/v1/")!,
    apiKey: ProcessInfo.processInfo.environment["HF_TOKEN"]!,
    model: "openai/gpt-oss-120b",
    apiVariant: .chatCompletions
)
```

雲端供應商享有與本地模型相同的能力:guided generation、支援串流的工具呼叫,以及回應中的 token 使用量。推理(reasoning)過程現在也被納入 transcript 的一部分;切換供應商時,若新供應商無法回放 reasoning 區塊,系統會自動從請求中省略這些內容。API 金鑰也從單純字串改為透過 closure 提供,讓 App 能向自己的伺服器取得短期有效的 token;README 中說明了何時該讓使用者自帶金鑰、何時該透過代理伺服器轉發請求。此外,AnyLanguageModel 現在也能在 Linux 上執行,同一套程式碼可以直接用在伺服器端。

📊 **開源權重模型也更強了**

目前 Hub 上下載量最高的幾個模型包括:Google 的 Gemma 4 E2B,GGUF 格式,採用 quantization-aware training,Q4_0 量化下約 3.4 GB;Liquid AI 的 LFM2.5 2.6B,GGUF 格式,Q4_K_M 量化下約 1.7 GB;Alibaba 的 Qwen3.8 27B(MLX 版本),4-bit 量化下約 16 GB。前兩者可以直接塞進 iPhone,Qwen3.8 27B 則需要 32 GB 記憶體以上的 Mac。選用 MLX 模型只需要一行程式碼:

```swift
let model = MLXLanguageModel(modelId: "mlx-community/Qwen3.8-27B-4bit")
```

至於 Z.ai 的 GLM-5.3,BF16 格式下需要約 1.5 TB,得靠四臺滿血 Mac Studio 才跑得動——對大多數人來說,透過 Inference Providers 使用會更實際。

🎯 **實務啟示**

升級到 1.0 只需要把套件相依性指向 `.package(url: "https://github.com/huggingface/AnyLanguageModel", from: "1.0.0", traits: ["MLX"])`,既有專案可參考 release notes 中的遷移指引。如果你的 App 需要在「裝置端跑小模型」與「雲端呼叫大模型」之間彈性切換,這套統一 API 讓你不必為每個供應商各寫一套整合程式碼,而官方也預告下一步會把同樣的設計理念延伸到「會做決策」與「會聽覺輸入」的模型類型。

🔗 **來源**
- 標題：AnyLanguageModel 1.0: One Year of Local Models on Apple Platforms
- 作者／機構：HuggingFace
- 連結：https://huggingface.co/blog/anylanguagemodel-1-0

#AnyLanguageModel #AppleDeveloper #OnDeviceAI #SwiftLang #HuggingFace #LocalLLM #MLX #FoundationModels #OpenWeightModels #MobileAI
