---
title: "Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model"
source: Hacker News
url: https://github.com/cactus-compute/needle
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-05-13T20:33:12.647445
---

📌 【Cactus 最新研究】26M 參數注意力模型 Needle，工具呼叫也能在手機上跑  

你以為工具呼叫需要巨大模型？一個只有 26M 參數的注意力網路就能在手機上達到與 270M 模型相近的表現。  
這意味著未來的 AI 代理或許不再依賴雲端運算。  

🤔 **工具呼叫其實是檢索與組裝，不需要巨大模型的推理能力**  
團隊指出，當前在資源受限的裝置上建立代理體驗一直受限，因為大家普遍認為需要大型模型來進行推理。他們觀察到，工具呼叫的核心工作是「匹配查詢到工具名稱、提取參數值、輸出 JSON」，本質上是檢索與組裝，並不需要複雜的推理。因此，龐大的前饋網路（FFN）參數在此規模下是被浪費的。  

🧪 **在 16 顆 TPU v6e 上預訓練 200B tokens，再用 Gemini 合成 2B tokens 的工具呼叫資料進行後訓練**  
Needle 的訓練分兩階段：首先在 200B 個 tokens 上進行無監督預訓練，使用 16 顆 TPU v6e，耗時約 27 小時；接著以 2B 個 tokens 的合成函式呼叫資料進行後訓練，這些資料是透過 Gemini 生成，涵蓋 15 個工具類別（計時器、訊息、導航、智慧家居等），後訓練僅需 45 分鐘。整個模型採用純注意力結構（Simple Attention Networks），全程無 MLP／FFN 層。  

📊 **在單次工具呼叫基準上，Needle 超過 FunctionGemma-270M 等更大模型，同時在消費設備上達到 6000 tok/s 前填、1200 tok/s 解碼**  
實驗顯示，Needle 在單次工具呼叫任務上優於 FunctionGemma-270M、Qwen-0.6B、Granite-350M、LFM2.5-350M 等參數量更大的模型。在消費級裝置上，模型的前填吞吐量約為 6000 tokens/秒，解碼吞吐量約為 1200 tokens/秒，顯示其具備即時、低延遲的運行潛力。  

💡 **無 FFN 的注意力網路足以處理工具呼叫，因為任務本質是匹配與參數抽取，記憶事實可透過輸入提供**  
因為工具呼叫不需要模型內部 memorize 事實，所有所需知識（例如工具簽名、參數範圍）都可以透過提示或檢索提供給模型。此時，交叉注意力機制足以完成「查詢 → 工具名稱」的匹配與「參數抽取」工作，而 FFN 在此場景下並不帶來顯著收益，因而被移除也不會影響效能。這個發現也被團隊指出，在任何模型能夠直接取得外部結構化知識的情境下（如 RAG、檢索增強生成），同樣的「無 FFN」設計可能具有普遍適用性。  

⚠️ **目前僅驗證單次工具呼叫，未測試多輪對話或更廣泛的任務，且訓練資料依賴 Gemini 合成**  
Needle 的評估專注於單次函式呼叫場景，尚未在多輪對話或更複雜的推理任務上進行系統性測試。後訓練資料完全來自 Gemini 的合成，這意味著模型的行為可能受限於合成資料的分佈與品質。此外，模型仍是實驗性質的原型，尚未在大規模真實裝置上進行長期穩定度驗證。  

🎯 **開發者可直接在手機或可穿戴設備上運行、微調自有工具，模型採用 MIT 授權，權重已在 HuggingFace 公開**  
Needle 的程式碼與權重皆以 MIT 授權開放，開發者可以在 GitHub 取得原始碼，或直接從 HuggingFace 下載權重進行微調。專案同時提供 Playground，讓使用者在自己的電腦上測試並依需求調整工具集。作為 Cactus 推理引擎的一部分，Needle 旨在支援行動裝置、可穿戴設備以及自訂硬體上的即時代理應用。  

🔗 **專案連結**  
💻 GitHub：https://github.com/cactus-compute/needle  
🤗 HuggingFace 權重：https://huggingface.co/Cactus-Compute/needle  
📖 架構說明：https://github.com/cactus-compute/needle/blob/main/docs/simp...  
🔧 Cactus 推理引擎：https://github.com/cactus-compute/cactus  
💬 先前 HN 討論：https://news.ycombinator.com/item?id=44524544  

#AI #Agent #ToolCalling #OnDeviceAI #Cactus #Needle #OpenSource #MachineLearning #EdgeComputing
