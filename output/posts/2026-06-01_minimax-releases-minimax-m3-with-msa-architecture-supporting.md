---
title: "MiniMax Releases MiniMax M3 with MSA Architecture Supporting 1M-Token Context, Native Multimodality, and Agentic Coding"
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/01/minimax-releases-minimax-m3-with-msa-architecture-supporting-1m-token-context-native-multimodality-and-agentic-coding/
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-06-01T22:04:58.505310
---

📌 **MiniMax M3：1M‑Token 視窗＋原生多模態**  

你以為 128K 已是長文本的極限？MiniMax 今早在 2026‑06‑01 直接把上下文拉長到 1M token，且聲稱在速度上不只沒變慢，反而更快。這到底是怎麼做到的？

🤔 **長上下文與多模態的雙重挑戰**  
隨著 AI 應用從單輪對話延伸至長文檔閱讀、影像/影片理解以及自動化編程（Agentic Coding），模型必須同時處理龐大的 token 序列與多種模態資訊。傳統的全注意力機制在序列長度成長時會導致計算量呈二次方爆炸，成為實務部署的瓶頸。

🧪 **MSA（MiniMax Sparse Attention）架構設計**  
MiniMax M3 的核心創新是提出的 MSA。與標準全注意力不同，MSA 在計算注意力前加入一個預篩選階段，將 KV 快取分成更細的區塊。根據團隊說明，這種「KV outer gather Q」的做法讓每個 KV 區塊只被讀取一次，記憶體存取具備連續性，從而避免了傳統稀疏注意力（如 DSA、MoBA）在區塊劃分上的粗放。  

在 MiniMax M3 的頭部配置下，團隊報告 MSA 比開源的 Flash‑Sparse‑Attention 與 flash‑moba 快 **4 倍以上**。更進一步，在 1M token 長度的情況下：  
- 每個 token 的計算量僅為前一代 M2 模型的 **1/20**；  
- 前填（prefill）階段提速 **9×+**；  
- 解碼（decoding）階段提速 **15×+**。  

多個消融實驗顯示，MSA 在主要任務上與全注意力表現相當，意味著在不犧牲準確度的前提下獲得了顯著的效率提升。

💡 **原生多模態與 Agentic Coding 能力**  
除了長上下文，M3 內建支援圖像與影像輸入，並能直接在桌上型電腦上運行。官方將其定位為「開放權重」模型，結合前沿級編程表現、1M‑token 視窗與原生多模態於單一架構—— MiniMax 認為這是業界首次同時達成的組合。模型權重與技術報告預計在發布後 10 天內公開，目前可透過 MiniMax Code、MiniMax Token Plan 與 MiniMax API 立即呼叫。

⚠️ **已知限制與待驗證點**  
- 模型權重與完整技術報告尚未公開，現有資訊主要來自官方聲明與 MarkTechPost 報導；  
- 速度與準確度的數據基於內部測試，尚未見獨立基準驗證；  
- 目前說明僅涵蓋頭部配置下的效能，不同硬體或不同注意力頭數的表現仍需進一步觀察。  

🎯 **對開發者的實務啟示**  
如果 MSA 的效能主張經外部驗證，這意味著：  
- 長文檔、多媒體理解與自動編程等場景可在單一模型中實現，降低系統複雜度；  
- 開發者可利用 1M‑token 視窗進行更深層的上下文推理（例如整個專案的程式碼基礎）而不必依賴分段或檢索技巧；  
- 待權重開放後，社群可在本地或私有雲端進行微調，進一步探索其在 Agentic 工作流中的潛力。  

🔗 **資訊來源**  
📝 MiniMax 官方公告（經 MarkTechPost 報導）  
👤 作者：Asif Razzaq  
🔗 文章：https://www.marktechpost.com/2026/06/01/minimax-releases-minimax-m3-with-msa-architecture-supporting-1m-token-context-native-multimodality-and-agentic-coding/  

你對 1M‑token 長文本與原生多模態的結合有什麼期待？歡迎在留言區分享你的看法！  

#MiniMax #MSA #LongContext #MultimodalAI #AgenticCoding #AI開發 #MarkTechPost
