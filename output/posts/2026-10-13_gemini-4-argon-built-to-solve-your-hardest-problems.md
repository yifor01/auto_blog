---
title: 'Gemini 4 Argon: Built to solve your hardest problems'
source: Google DeepMind
url: https://deepmind.google/blog/introducing-gemini-4-argon/
model: claude-code/sonnet
generated_at: '2026-10-13T21:58:59.579708'
pinned: true
---

📌 【Google DeepMind】Gemini 4 Argon 正式開放，程式碼重構案例曝光

TL;DR：Gemini 4 Argon 全球上線，在金融、法律、程式碼等多項基準排名第一，並已協助 Chrome、ADK、xTB 等專案完成實質最佳化。

當一個模型被拿去重構 Chromium 裡四千萬行程式碼中的六百萬行遺留資料夾，而且是用數週時間完成原本要數月的工作時，這已經不只是基準測試分數的提升了。

🤔 **全面上線，定位「深度工作」模型**

Gemini 4 Argon 今日起透過 API（AI Studio 與 Gemini 平臺）、Google Antigravity（Google AI Ultra 訂閱者）以及 Gemini App 與 AI Mode in Search（Ultra 與 Pro 訂閱者）向開發者與企業全面開放。DeepMind 表示 Argon 擅長 coding、finance、legal、cybersecurity、science 等領域的複雜多步驟任務，並在衡量金融、程式碼、法律、稅務等關鍵經濟領域表現的 Vals Index 上排名第一。模型定價為每百萬輸入 token 2 美元、每百萬輸出 token 10 美元，快取輸入 token 可享 95% 折扣。

🧩 **內部團隊已經拿它解決真實工程問題**

DeepMind 列舉了多個已落地案例：

- Chrome 重構：Argon 協助 Chrome 團隊把核心網頁處理邏輯從約六百萬行的遺留瀏覽器功能資料夾中拆分出來，一次推送多組乾淨的程式碼變更，完成跨數百個檔案的架構重構，原本要花數月的工作壓縮到數週內完成。
- ADK 效能優化：針對 Google 開源的 Agent Development Kit（ADK），團隊只給了一份 .agents/skills 規則手冊與一段目標描述，Argon 在 Antigravity 中自主工作一整夜，找出的最佳化已合併進 google/adk-python，將長對話 session 的記憶體準備時間縮短 40%，冷啟動匯入速度加快 21%。
- xTB 量子化學套件：這套被廣泛引用的開源量子化學工具用於預測分子 3D 結構、篩選藥物與材料候選物。使用 Argon 後，xTB 預測分子結構的速度提升達 2.3 倍，conformer 搜尋加快 1.8 倍，相關改動已貢獻回官方 GitHub 儲存庫。
- Gemma 推論加速：在 A100 上透過 vLLM，Argon 協助達成 2.85 倍端到端推論加速，Gemma 4 E2B 的吞吐量從每秒約 37,900 token 提升到超過 108,000 token，同時維持 100% token 一致性且無品質下降，耗時僅數天，官方表示這類工作通常要數月。

📊 **內部開發流程的量化成效**

Google 表示在 Antigravity 中使用 Argon 後，軟體工程師的 agentic 程式碼提交量增加超過 35%，程式碼回退（rollback）減少近三分之一。

💡 **多代理視覺批判迴圈，拿來做 3D 內容生成**

除了程式碼最佳化，DeepMind 也展示 Argon 搭配 Antigravity 中的多代理（multi-agent）視覺批判迴圈，自主完成複雜任務：例如自主雕塑出帶有擬真建築、植被與燈光的多棟寺廟建築群模型，或把一張書桌實拍照片轉成可遊玩的迷你賽車遊戲（物件建模與碰撞檢測用 Blender MCP、貼圖用 Nano Banana、物理與音效用 Three.js 及 Gemini Omni Flash）。在企業應用端，Argon 也被用於整合約 50GB 的空載光達掃描、GIS 向量與 CAD 圖紙重建 Chaco Canyon 的 3D 模型，以及在 Isomorphic Labs 作為加速藥物發現研究流程的夥伴。

🎯 **實務啟示**

對工程團隊而言，比起單一基準分數，更值得參考的是這些案例展現的工作模式：給模型明確的規則手冊與目標，讓它在 agentic 框架中自主迭代多個檔案的變更，再由人把關合併，這可能是大型遺留程式碼庫重構與效能調校的可行路徑。

🔗 **來源**
- 標題：Gemini 4 Argon: Built to solve your hardest problems
- 作者／機構：Koray Kavukcuoglu，Google DeepMind
- 連結：https://deepmind.google/blog/introducing-gemini-4-argon/

#GeminiArgon #GoogleDeepMind #LLM #CodeRefactoring #AIAgents #Antigravity #DeveloperTools #AIforScience #PerformanceEngineering #AIAdoption
