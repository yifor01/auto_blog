---
title: Gemini Omni 1.1 Flash
source: Hacker News
url: https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/
model: claude-code/sonnet
generated_at: '2026-08-28T18:00:47.219939'
score: 100
---

📌 【Google DeepMind】生成影片能接續 40 秒,還能指定頭尾幀

TL;DR:Gemini Omni 1.1 Flash 開放場景延伸、頭尾幀控制與 4K 輸出,讓生成影片開發更可控、更好迭代。

生成影片最尷尬的地方,從來不是「畫面漂不漂亮」,而是「第二個鏡頭接不接得上第一個」。Google DeepMind 這次針對的正是這個痛點。

🎬 **場景延伸從參考 1 秒,拉長到參考 10 秒**

Gemini Omni 1.1 Flash 是一套面向開發者的生產就緒(production-ready)更新,透過 Google AI Studio 或 Gemini Enterprise Agent Platform 提供的 Gemini API 存取。其中的場景延伸(scene extension)功能可以接續既有影片,從影片停止的地方無縫繼續生成。相較於先前版本只參考影片最後 1 秒的畫面,Omni 1.1 現在能分析長達 10 秒的先前脈絡,官方表示這讓視覺一致性與敘事連貫性都有提升;開發者可以每次以 10 秒為單位延伸,累積總長最多可達 40 秒。

🧩 **指定頭尾幀,做出乾淨的鏡頭轉場**

另一項新功能是可以指定一個鏡頭的起始幀與結束幀,由模型在兩個關鍵影格之間生成連續的影片內容,適合用在複雜的運鏡環繞、縮放轉場或需要無縫循環的片段。此外,Omni 1.1 也支援在多模態輸入中加入最長 3 秒的參考影片,讓生成過程能維持角色與視覺脈絡的一致性。

📊 **360p 草稿最快省 60% 時間、成本剩三分之一**

為了加快原型設計與分鏡迭代的速度,開發者可以先用 360p 解析度生成輕量預覽,官方數據顯示相較於 Omni 1.1 標準的 720p 解析度,360p 生成速度最高可快 60%,成本則只要三分之一;確定方向後再輸出至 1080p 甚至 4K 解析度,做成可直接用於正式production的成品。

🧩 **API 呼叫方式**

延伸場景的呼叫方式是透過 `previous_interaction_id` 帶入前一段影片的 interaction id,再指定 `response_format` 的 `resolution` 參數(例如 `"360p"`)產生延伸內容,整個流程走的是 Gemini API 的 `client.interactions.create` 介面。

🎯 **實務啟示**

對正在開發生成式影片工具或媒體編輯軟體的團隊來說,這次更新把「先用低解析度快速迭代分鏡、確定後再放大輸出」的工作流程直接內建進 API,加上頭尾幀控制與場景延伸,等於把過去需要多次拼接、後製修補的流程,收斂成更少的呼叫次數與更可預期的成本結構。

🔗 **來源**
- 標題:Gemini Omni 1.1 Flash
- 作者/機構:Anish Nangia、Alisa Fortin(Google DeepMind Product Manager)
- 連結:https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/

#GeminiOmni #GoogleDeepMind #GenerativeVideo #AIVideoGeneration #GeminiAPI #TextToVideo #4K #GenAI #DeveloperTools #VideoEditing
