---
title: 'Google AI Releases Gemini Omni 1.1 Flash: 40-Second Scene Extension, First/Last
  Frame Control, and 4K Upscaling'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/29/google-ai-releases-gemini-omni-1-1-flash-40-second-scene-extension-first-last-frame-control-and-4k-upscaling/
model: claude-code/sonnet
generated_at: '2026-08-30T10:53:35.594460'
score: 100
---

📌 【Google】Gemini Omni 1.1 Flash：能記住 10 秒的影片編輯模型

TL;DR：Gemini Omni 1.1 Flash 加入 40 秒場景延伸、首尾幀控制與 4K 放大，讓影片生成從「產生」變成「可被導演」。

過去的影片延伸模型只看得到前一幀畫面就要接著往下畫，銜接處常常一秒就出戲；Gemini Omni 1.1 Flash 現在能讀取前面長達 10 秒的內容，再決定接下來要畫什麼。

🤔 從「能生成」到「可被導演」

Google 發布 Gemini Omni 1.1 Flash（gemini-omni-1.1-flash），是其原生多模態影片生成與編輯模型的正式版更新。這次更新的重點是把 Omni 從一個能生成影片的模型，推進成一個能被精確控制的工具：場景延伸不再只參考最後一幀，而是讀取前面最長 10 秒的上下文；可以釘住首幀與尾幀來控制運鏡；草稿能先用 360p 生成、成本只要 720p 的三分之一；最終成品能放大到 4K；影片片段也能作為角色一致性的參考素材。

🧩 有狀態編輯與可控的鏡頭語言

Omni Flash 的核心建立在三個特性上：原生多模態（文字、圖片、音訊、影片一起處理）、透過 Interactions API 的對話式編輯，以及繼承自 Gemini 的世界知識。編輯是有狀態的——傳入 previous_interaction_id，模型會在保留你沒提到的部分的前提下套用修改，不需要重新上傳整支影片。

場景延伸方面，Omni 1.1 會分析前面最長 10 秒的上下文，Google 表示前一代模型只參考最後一秒畫面。延伸以 10 秒為單位累加，最長可到 40 秒，單次呼叫產生 3 到 10 秒的延續內容，輸入影片結尾的部分畫面也會被重新編輯以確保銜接連續。限制也很具體：延伸只能接在片尾，不能往前插或中間插；上傳的輸入影片必須在 10 秒以內，除非是在多輪對話中延伸模型自己先前生成的影片；如果上傳的影片裡有人在說話，延伸時不能新增對白，對白支援僅限透過 previous_interaction_id 的多輪延伸。

首尾幀控制則是提供首幀與尾幀，模型生成中間連續的過程，這正是做出環繞運鏡、dolly zoom、無縫循環的機制。提示詞用標籤把素材綁定到角色：<FIRST_FRAME>、<LAST_FRAME>、<IMAGE_REF_N>、<VIDEO_REF_N>。影片參考最多 3 支、每支最長 3 秒，主要用於還原人物特徵，影片中的音訊會被忽略，也不支援跨多支影片的推理，硬用可能讓輸出品質下降。解析度方面，response_format 的 resolution 參數支援 360p、720p（預設）、1080p、4k，後兩者屬於放大而非原生生成；Google 表示 360p 預覽的生成速度最多快 60%，成本只要 720p 的三分之一，因此「先用 360p 疊代、確定後再放大一次」是官方建議的正式生產流程。

📊 定價與已知限制

計費方式：輸入（文字／圖片／影片／音訊）每 100 萬 token 1.50 美元；輸出文字每 100 萬 token 9.00 美元，輸出影片每 100 萬 token 17.50 美元。影片計費以每秒 720p 影片 5,792 token 計算，換算下來標準定價約每秒 0.10 美元。每支生成影片都帶有 SynthID 浮水印，人眼看不到，但可被程式偵測以供溯源。

已知限制不少：不支援 system instructions、temperature、top_p、stop sequences、negative prompt（負面描述要寫進提示詞本文）；不支援語音編輯；不支援音訊參考；不能用 YouTube 網址當來源；英文完整支援，其他語言尚未經過評估；輸出超過 4MB 時要改用 delivery="uri"，並輪詢 Files API 直到檔案狀態變成 ACTIVE。

💡 產品邏輯像在往剪輯軟體靠攏

把「10 秒上下文＋首尾幀控制＋360p 草稿／4K 定稿」這三件事拼在一起看，其實是在把影片生成的工作流程往剪輯軟體的方向設計：先低成本試運鏡與銜接，確認滿意後再用高解析度算一次正式版本。

🎯 已進駐多家生產環境

Omni Flash 已上架 Google AI Studio 的 Gemini API 與 Gemini Enterprise Agent Platform，Adobe（Firefly）、Figma Weave、GMI Cloud、Runway 是已在生產環境使用的客戶，Google Flow 的 AI Plus、Pro、Ultra 訂閱者也能在 Gemini App 中使用場景延伸功能。對要把影片生成整合進產品的工程師，「有狀態編輯」省下重新上傳影片的成本，而 360p 草稿／4K 定稿的兩段式流程也直接對應到成本控制策略，值得在設計呼叫流程時參考。

🔗 來源
- 標題：Google AI Releases Gemini Omni 1.1 Flash: 40-Second Scene Extension, First/Last Frame Control, and 4K Upscaling
- 作者／機構：Michal Sutter，MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/29/google-ai-releases-gemini-omni-1-1-flash-40-second-scene-extension-first-last-frame-control-and-4k-upscaling/

#GeminiOmni #GoogleAI #VideoGeneration #GenerativeAI #MultimodalAI #VideoEditing #AIStudio #ProductionAI #TextToVideo #CreativeAI
