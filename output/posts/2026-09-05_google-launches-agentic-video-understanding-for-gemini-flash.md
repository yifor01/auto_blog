---
title: Google Launches Agentic Video Understanding for Gemini Flash Models, Cutting
  Video Tokens by Up to 88%
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/04/google-agentic-video-understanding-gemini-flash-models/
model: claude-code/sonnet
generated_at: '2026-09-05T19:09:34.927395'
score: 102
---

📌 Gemini Flash 新增 agentic 影片理解，Token 用量最多省 88%

TL;DR：Google 讓 Gemini Flash 自己決定怎麼看影片，而非整支逐秒吃進 context，官方數據顯示成本最多降 66%。

過去要讓 Gemini 理解一部 90 分鐘的演講影片，不管你問的是「幫我摘要」還是「講者什麼時候切到報價那張投影片」，模型都得用固定的每秒一幀把整支影片吃進 context。這種一次到位的處理方式，逼得開發者只能二選一：付出整條時間軸的成本，或是事先切好片段，卻可能剛好漏掉真正重要的細節。這週，Google 在 Flash 模型系列中推出 agentic 影片理解，讓模型不再是被動吃完整支影片，而是自己決定要看哪一段、用什麼幀率、透過哪種模態去看。

🤔 固定每秒一幀，是目前所有 Gemini 模型的預設處理方式

素材指出，靜態處理目前仍是所有 Gemini 模型的預設行為：以每秒一幀的速率單次擷取畫面，音訊以 1 Kbps 單聲道處理，並每秒插入一次時間戳記。這種做法對短影片沒什麼問題，但面對長影片，不管問題多聚焦，模型都得把整條時間軸的成本吃下去。

🧩 讓模型自己搜尋、掃描、檢視目標片段

agentic 處理則把這個單次流程換成一個迴圈：模型結合自身推理與原生的影片工具，在畫面、音訊與逐字稿之間搜尋、掃描並檢視目標片段，只載入提示詞真正需要的部分。素材特別點出，開發者原本就能自己手動組出這樣的流程，這次的改變是 Gemini 把這個迴圈內建在模型內部執行，開發成本因此被省下來。

在回應的 steps 陣列裡，agentic 處理新增了兩種步驟類型：`processing_call` 代表模型請求載入某個片段或逐字稿，`processing_result` 則是該次載入完成後對應出現的結果，兩者會穿插在 thought 步驟之間、並排在 `model_output` 之前，因此可以用來在介面上即時呈現處理進度，也是用來確認 agentic 模式是否真的有啟動的依據。Token 計費也隨之拆分：導覽推理算作 thought tokens（`total_thought_tokens`），依需求載入的畫面、音訊與逐字稿則算作 tool-use tokens（`total_tool_use_tokens`）。

📊 Token 省最多 88%，成本降最多 66%，準確率還提升最多 7%

在 Google 自己的評測中，搭載 agentic 理解的 Gemini 3.7 Flash 在受測模型裡，於影片分析的準確率對成本權衡上落在 Pareto 前緣。效率提升主要集中在長影片內容，從 10 分鐘的教學影片到長達數小時的錄影都在受益範圍內。官方數據顯示，在標準影片 benchmark 上，token 用量最多減少 88%、成本最多降低 66%、準確率則最多提升 7%。

🎯 實務啟示

這個功能目前只能透過 hosted API 使用，沒有開放權重、也無法自行部署，透過 Gemini API（Google AI Studio）與 Gemini Enterprise Agent Platform 提供，同時支援檔案上傳與公開 YouTube 連結，計費方式沿用標準 Gemini API token 定價、不額外收取功能費用。開發者只需要在影片 part 上設定一個欄位就能啟用，而且同一個請求裡可以混用模式，例如長篇演講用 agentic、短片段維持靜態處理。如果你的應用場景需要處理長影片但只在乎其中特定片段，這會是一個值得優先評估、且不需要自建搜尋迴圈的選項；但如果你需要自架模型或離線處理，目前這個功能還幫不上忙。

🔗 來源
- 標題：Google Launches Agentic Video Understanding for Gemini Flash Models, Cutting Video Tokens by Up to 88%
- 作者／機構：Michal Sutter／MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/04/google-agentic-video-understanding-gemini-flash-models/

#Gemini #GoogleAI #VideoUnderstanding #AgenticAI #MultimodalAI #GeminiFlash #AIStudio #LLM #TokenEfficiency #AIEngineering
