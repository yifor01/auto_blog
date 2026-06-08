---
title: 'Meet Harness-1: A 20B Retrieval Subagent Trained With Reinforcement Learning
  Inside a Stateful Search Harness on gpt-oss-20b'
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/06/meet-harness-1-a-20b-retrieval-subagent-trained-with-reinforcement-learning-inside-a-stateful-search-harness-on-gpt-oss-20b/
score: 107
model: google/gemma-4-31b-it:free
generated_at: '2026-06-08T20:36:00.744371'
---

📌 【UIUC / UC Berkeley / Chroma 最新研究】讓 AI 專注於「決定」而非「記憶」：Harness-1 重新定義檢索代理架構

目前的 AI 搜尋代理（Search Agents）通常面臨一個巨大的認知負荷：模型必須在同一個策略（Policy）中，同時處理「如何搜尋」的決策，以及「記住看過什麼、哪些證據重要、哪些聲明已驗證」的繁瑣簿記工作。

這種將決策與記憶混在一起的設計，讓強化學習（RL）在優化時必須同時處理這兩種截然不同的任務，效率自然受限。

🤔 **搜尋代理的困境：決策與簿記的混亂**

大多數搜尋代理將整個對話紀錄（Transcript）視為策略的輸入，這意味著模型必須在龐大的上下文中自行管理所有狀態。研究團隊指出，這對模型來說「要求太多了」。當模型需要花精力去記錄哪些資訊已讀時，它在核心的搜尋決策上的表現反而會被削弱。

🧪 **Stateful Cognitive Offloading：將記憶「外包」給狀態機**

來自 UIUC、UC Berkeley 與 Chroma 的研究團隊提出了一套全新的解決方案：**Harness-1**。

這是一個基於 `gpt-oss-20b` 的 20B 參數檢索子代理（Retrieval Subagent）。其核心創新在於將架構拆分為兩個部分：
1. **Policy (策略)**：僅負責語義決策（決定搜什麼、如何篩選、何時停止）。
2. **Stateful Harness (狀態機外殼)**：負責所有繁瑣的簿記工作（Bookkeeping）。

這種設計被稱為「狀態化認知卸載」（Stateful Cognitive Offloading），讓模型不再需要記憶瑣碎的狀態，而只需根據外殼提供的精簡狀態做出決定。

⚙️ **核心設計：狀態機如何分擔壓力？**

Harness-1 並不直接回答問題，而是為後續的回答模型提供一套經過排序的文件集。其運作流程是一個循環：外殼渲染目前的搜尋狀態 $\rightarrow$ 模型發出一個結構化動作 $\rightarrow$ 外殼執行並更新狀態 $\rightarrow$ 再次渲染觀察結果。

外殼中維護的關鍵狀態包括：
- **候選池 (Candidate Pool)**：存放壓縮且去重的文件。
- **精選集 (Curated Set)**：最終輸出，上限 30 份文件，並標記重要程度（very_high, high, fair, low）。
- **全文儲存 (Full-text Store)**：將所有檢索到的片段存放在 Prompt 之外，減少上下文壓力。
- **證據圖譜 (Evidence Graph)**：透過 Regex 提取專有名詞、年份與日期，為資訊增加結構化關聯。

💡 **模組化檢索：從「全能模型」轉向「專業子代理」**

Harness-1 的設計體現了 Agentic AI 的一個重要趨勢：**模組化**。

與其訓練一個試圖處理所有事情的巨型模型，不如將其拆解為「決策子代理」與「狀態管理系統」。這種拆分讓強化學習能更專注於優化搜尋路徑的品質，而將數據管理交給更可靠的狀態機。這不僅提升了可控性，也讓檢索管線（Search Pipeline）變得更加透明且易於調優。

⚠️ **定位為子代理，不直接產生最終答案**

需要注意的是，Harness-1 的定位是「檢索子代理」，它的產出是高品質的參考文獻集，而非最終答案。因此，其實際效果仍依賴於後端接接的回答模型（Downstream Answering Model）的理解能力。

🎯 **實務啟示：開發 AI Agent 時應區分「邏輯」與「狀態」**

對於開發 AI Agent 的工程師來說，這項研究提供了一個重要的設計方向：
- **不要強迫模型管理狀態**：將重複性的記錄、去重、標記等工作移至程式碼層級（Harness）。
- **精簡 Prompt 內容**：透過外部儲存（如 Full-text Store）減少 Token 消耗，只將必要的「狀態摘要」餵給模型。
- **結構化輸出**：要求模型發出結構化動作，而非自然語言描述，能顯著提高執行穩定性。

🔗 **論文與資源**
📝 Meet Harness-1: A 20B Retrieval Subagent Trained With Reinforcement Learning Inside a Stateful Search Harness on gpt-oss-20b
👤 Asif Razzaq 等
🔗 論文連結：https://arxiv.org/pdf/2606.02373
（權重與 Harness 程式碼已公開發布）

如果你正在構建複雜的 RAG 或 AI Agent 系統，這種「決策與狀態分離」的架構或許能解決你遇到的上下文崩潰問題。

#AI #AgenticAI #RAG #ReinforcementLearning #OpenSource #MachineLearning #UIUC #Berkeley #Chroma
