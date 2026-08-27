---
title: Gemini Omni 1.1 Flash lets you build with more control
source: Google DeepMind
url: https://deepmind.google/blog/gemini-omni-1-1-flash-lets-you-build-with-more-control/
model: claude-code/sonnet
generated_at: '2026-08-27T17:12:02.225217'
pinned: true
---

📌 【Google DeepMind 發布】Gemini Omni 1.1 Flash,把生成影片的控制權交還給開發者

TL;DR:Google DeepMind 推出 Gemini Omni 1.1 Flash,支援場景延伸、首尾影格控制與 4K 升頻,主打生產級生成影片。

生成式影片一直有個尷尬之處:模型能生出漂亮的片段,但開發者很難精準控制鏡頭怎麼動、故事怎麼接下去。Google DeepMind 這次推出的 Gemini Omni 1.1 Flash,想解決的正是「控制力不足」這個問題。

🤔 **從能生成,到能精準掌控**

根據官方部落格,Gemini Omni 系列先前的重點是為生成式創作帶入現實世界的推理能力,而這次的 1.1 版本則進一步把重心放在「生產可用」上,提供開發者更細緻的創作控制工具,透過 Google AI Studio 中的 Gemini API 或 Gemini Enterprise Agent Platform 存取。

🧩 **五項核心能力**

- **場景延伸(Scene extension)**:可在既有影片基礎上無縫接續生成後續畫面。Omni 1.1 能分析前 10 秒的上下文,相較舊模型只能參考最後 1 秒,大幅提升了畫面一致性與敘事連貫性;可以 10 秒為單位延伸,累計長度最高達 40 秒。
- **首尾影格插補(First and last frame interpolation)**:開發者可指定一個鏡頭的起始與結束影格,模型會在兩者之間生成連續畫面,適合處理複雜運鏡、變焦轉場或無縫循環片段。
- **360p 快速草稿**:提供 360p 的輕量預覽模式,官方宣稱生成速度比標準 720p 快up to 60%,成本僅為三分之一,方便快速迭代與分鏡測試。
- **4K 升頻**:可將最終成品升頻至 1080p 或 4K 解析度,達到專業級輸出品質。
- **多段影片參考輸入**:可在多模態輸入中引用最長 3 秒的影片片段作為參考,協助在生成過程中維持角色與視覺風格的一致性。

💡 **開發者怎麼串接**

官方也提供了呼叫場景延伸功能的程式碼範例,透過 `google.genai` 的 client 建立 interaction,並帶入 `previous_interaction_id` 指向前一段影片、搭配文字提示「Continue the scene.」,即可延續生成;`response_format` 中可指定解析度(如 360p)來平衡速度與成本。

⚠️ **使用門檻與定位**

文中提到的效能提升(如 360p 比 720p 快 60%)是基於系統吞吐量的官方宣稱數據,實際表現可能因使用情境而異;此外,本次更新聚焦在生成式影片的控制與生產流程優化,並未提及模型在推理或其他模態上的其他變化。

🎯 **實務啟示**

對正在建構生成式影片工作流程、創作工具或媒體編輯軟體的團隊來說,場景延伸與首尾影格控制讓「AI 生成的鏡頭語言」更貼近實際製作需求;而 360p 快速草稿模式則提供了一個務實的開發流程:先用低成本模式快速試錯,確定分鏡與運鏡後,再升頻輸出成品,有效降低反覆生成的成本。

🔗 **來源**
- 標題:Gemini Omni 1.1 Flash lets you build with more control
- 作者／機構:Google DeepMind — Anish Nangia、Alisa Fortin
- 連結:https://deepmind.google/blog/gemini-omni-1-1-flash-lets-you-build-with-more-control/

#GeminiOmni #GoogleDeepMind #GenerativeVideo #AIVideoGeneration #GeminiAPI #GoogleAIStudio #VideoAI #CreativeAI #TextToVideo #4KVideo
