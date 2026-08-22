---
title: 'DeepSeek-V4-Flash-Vision-Exp Release: Multimodal API Now Live'
source: DeepSeek
url: https://api-docs.deepseek.com/news/news260821
model: claude-code/sonnet
generated_at: '2026-08-22T06:10:31.220363'
pinned: true
---

📌 DeepSeek新模型讓文字agent「看得懂圖」

TL;DR：DeepSeek-V4-Flash-Vision-Exp上線，多模態agent表現逼近Opus-4.8，文字能力維持V4-Flash水準。

如果你的agent pipeline一直卡在「純文字模型看不懂截圖、看不懂UI」這個瓶頸，DeepSeek這次的更新值得留意：他們在保留V4-Flash文字能力的前提下，直接把視覺理解塞進了同一個模型。

🤔 **問題：文字強不代表能處理多模態任務**

DeepSeek在公告中指出，這款實驗性多模態模型DeepSeek-V4-Flash-Vision-Exp在文字能力上（包括agent、推理與世界知識）與DeepSeek-V4-Flash打平。換句話說，這不是一個「犧牲文字能力去換視覺能力」的取捨版本，而是同時具備兩者。

🧩 **多模態agent能力的躍進**

公告特別強調，在多模態agent benchmark上，V4-Flash-Vision-Exp相較V4-Flash有「重大躍進（major leap）」，將多模態agent表現拉近到Opus-4.8的水準。這意味著模型不只是「看得懂圖」，而是能在需要視覺理解搭配工具呼叫的agent流程中實際發揮作用。要使用這個模型，只需在API呼叫中設定`model='deepseek-v4-flash-vision-exp'`。

同日發布的DeepSeek Harness 0.1.1，也對這個新模型提供了開箱即用的支援，讓它能順暢接入既有的agent框架，把視覺理解與各種工具串接起來，解鎖更多實際可用的workflow。

📊 **API使用細節**

根據官方文件，這個模型在整合上有幾個實務重點：
- 計費方式：圖片會被tokenize計費，每張圖最多384個token，計價比照V4-Flash的價格。
- 相容介面：支援Chat Completions、Messages與Responses三種介面。
- 輸入格式：支援文字與圖片混合輸入，圖片可透過base64編碼、外部URL，或Files API提供。
- 效率設計：圖片只需上傳一次，之後可透過`file_id`重複引用，不必每次請求都重新上傳，藉此節省請求頻寬；同一張圖片可在多次請求中重複使用。

🎯 **實務啟示**

對正在打造agent系統的工程師來說，最值得評估的是「多模態agent benchmark逼近Opus-4.8」這個宣稱——如果情況屬實，代表在需要同時處理畫面理解與工具呼叫的場景（例如UI自動化、螢幕截圖分析類agent），現在多了一個不必犧牲文字推理能力的選項。而Files API的`file_id`重複引用機制，也是在設計長對話、多輪視覺任務時值得直接採用的最佳化手法，能有效降低重複上傳圖片的頻寬與成本。由於這仍是「experimental」版本，建議先在非關鍵路徑上驗證其穩定性與實際表現，再考慮大規模導入。

🔗 **來源**
- 標題：DeepSeek-V4-Flash-Vision-Exp Release: Multimodal API Now Live
- 作者／機構：DeepSeek
- 連結：https://api-docs.deepseek.com/news/news260821

#DeepSeek #MultimodalAI #LLM #AIAgent #VisionLanguageModel #API #Opus48 #AgentFramework #GenAI #ToolUse
