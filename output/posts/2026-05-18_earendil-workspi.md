---
title: "earendil-works/pi"
source: GitHub Trending
url: https://github.com/earendil-works/pi
score: 104
model: tencent/hy3-preview:free
generated_at: 2026-05-18T20:33:57.679361
---

📌 **Pi Agent Harness: Open‑Source Coding Agent Suite**  

你是否想要一個能自行擴展、支援多家 LLM 的 coding agent，同時又能把開發過程分享到 Hugging Face？這個剛上 GitHub Trending 的專案正好提供了這樣的一站式方案。  

🤔 **為何需要一個可自擴展的 coding agent 生態系統**  
隨著 AI 輔助編程工具的普及，開發者不僅希望提升產能，也希望能夠自訂 agent 的行為、追蹤真實世界的使用情況，並將寶貴的 OSS 會話回饋給社群，以避免只依賴玩具基準進行評估。  

🧪 **Pi Agent Harness 的核心組成與貢獻流程**  
此單一倉庫（mono repo）包含三個主要套件：  
- @earendil-works/pi-coding-agent：互動式 coding agent CLI  
- @earendil-works/pi-agent-core：具備工具呼叫與狀態管理的 agent 執行階段  
- @earendil-works/pi-ai：統一的多提供者 LLM API（支援 OpenAI、Anthropic、Google 等）  

專案採用「預設自動關閉」的 Issue 與 PR 機制，維護者會每日審閱這些自動關閉的內容，詳情請參閱 CONTRIBUTING.md。此外，pi.dev 網域由 exe.dev 捐贈，提供線上示範與文件。  

💡 **提供即插即用的套件與 session 分享工作流**  
開發者可以直接安裝上述套件，使用 CLI 與 agent 互動。若想將自己的 OSS coding agent 會話分享給社群，專案提供了一條至 Hugging Face 的發布路徑：  
1. 安裝 badlogic/pi-share-hf  
2. 準備好 Hugging Face 帳號與 CLI  
3. 依照其 README.md 進行設定後發布會話  

作者也會定期將自己的 pi-mono 工作 session 發布至 badlogicgames/pi-mono，供大家參考。  

⚠️ **概念並非全新，社群興趣才是推動力**  
雖然 coding agent、工具使用與 session 日誌的理念在學界與業界已有先例，但該專案將這些元素整合成易於上手的套件，並透過清晰的貢獻指南與自動化的 Issue 管理，降低參與門檻。GitHub star 的快速成長反映了社群對此類「可自擴展 + 會話分享」工作流的當前關注度。  

🎯 **工程師可直接上手實驗、貢獻或分享自己的 coding agent 會話**  
- 若想快速體驗 multi‑provider LLM 呼叫，可先安裝 @earendil-works/pi-ai。  
- 若希望自行擴展 agent 行為，可以 @earendil-works/pi-agent-core 為基礎加入自訂工具。  
- 若想貢獻真實世界的使用數據，請遵循上述 session 分享流程，將會話推送至 Hugging Face，讓社群在實際任務、失敗與修復上獲得更具說服力的改進依據。  

🔗 **專案連結**  
📂 GitHub：https://github.com/earendil-works/pi  
🌐 官方站與示範：pi.dev  
📖 文件：同上網站內的 documentation 連結  
🎥 會話發布示範影片：專案頁面中所附的影片連結  

#OpenSource #CodingAgent #LLM #HuggingFace #GitHubTrending #AIEngineering #PiAgent #DevTools
