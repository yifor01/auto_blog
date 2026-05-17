---
title: "simular-ai/Agent-S"
source: GitHub Trending
url: https://github.com/simular-ai/Agent-S
score: 101
model: tencent/hy3-preview:free
generated_at: 2026-05-17T19:31:37.540487
---

📌 【simular-ai】Agent S 首次超越人類 OSWorld 基準 (72.60%)

你以為 AI 只能玩遊戲？Agent S 讓電腦使用代理首次在 OSWorld 超過人類表現，得分 72.60%，並連續刷新多項基準的最佳紀錄。

🤔 **電腦使用代理亟需突破人類瓶頸**  
過去的 CUA（Computer‑Use Agent）雖能自動化桌面操作，但多停留在特定任務或單一平台，難以匹配人類在跨應用、跨系統的靈活操作。隨著 OpenAI 的 CUA/Operator 與 Anthropic 的 Claude 3.7 Sonnet Computer‑Use 相繼發表，社區開始尋求更通用、更強大的解決方案。

🧪 **gui-agents 庫與跨平台評估**  
simular-ai 團隊開源了 gui-agents 庫，並在 OSWorld、WindowsAgentArena、AndroidWorld 三個主流基準上進行測試。實驗分為數個版本：  
- Agent S3（最新）在 OSWorld 上達到 72.60%，首次超越人類參考分數。  
- Agent S2 曾於 COLM 2025 被接收，並取得 OSWorld‑Verified 新 SOTA。  
- Agent S（最初版）於 ICLR 2025 獲得 Best Paper Award。  
所有版本均報告比 OpenAI 的 CUA/Operator 與 Claude 3.7 Sonnet Computer‑Use 更高的分數，並展示較好的泛化能力（在 WindowsAgentArena 與 AndroidWorld 上亦有顯著提升）。

📈 **核心發現：簡單即強大，首次超越人類**  
- Agent S3 的 72.60% 分數不僅是 OSWorld 新紀錄，也意味著電腦使用代理在模擬真人操作的基準上首次達到並超越人類平均表現。  
- 相較於先前 SOTA（69.9%），Agent S3 在保持簡單架構的同時，提升了速度與靈活性，使得代理在多平台環境下更易於部署與二次開發。  
- 實驗顯示該庫在 WindowsAgentArena 與 AndroidWorld 上亦具強 generalizability，證明其設計不限於單一作業系統。

💡 **深入分析：簡潔設計帶來更佳泛化**  
團隊指出，Agent S 系列的成功關鍵在於：  
1. **模組化的 gui-agents 庫**，讓開發者能快速替換或擴充感知與規劃元件。  
2. **統一的跨平台介面**，減少對特定 OS 的依賴，提升在 Windows、Android 與網頁環境的遷移能力。  
3. **訓練與推流程的簡化**，使得實驗週期縮短，便於快速迭代與社區貢獻。

⚠️ **目前可見的限制**  
所提供的資訊僅涵蓋基準測試結果與論文發表情況；尚未見長期實際桌面環境部署、真實使用者互動或安全性等方面的詳細評估。實際產品化前仍需進行更廣泛的實測與風險分析。

🎯 **實務啟示：開源庫降低電腦使用代理開發門檻**  
- 工程師可直接克隆 simular-ai/Agent-S 存儲庫，使用 gui-agents 庫建構自訂的電腦使用代理。  
- 基於已發表的 S2、S3 論文（COLM 2025、ICLR 2025 Workshop）可快速了解最佳實驗設定與基準分數。  
- 專案持續更新（2025/12/15 發布 Agent S3），適合作為研究原型或生產前概念驗證的起點。

🔗 **論文與資源連結**  
📝 Agent S3 技術報告：[S3 Paper]（連結於 GitHub 頁面）  
📝 Agent S2 論文（COLM 2025）：[S2 Paper]  
📝 Agent S 論文（ICLR 2025 最佳論文獎）：[S1 Paper]  
💻 開源專案：https://github.com/simular-ai/Agent-S  
🌐 線上體驗（Simular Cloud）：可直接跳過本地安裝試用 Agent S3。

你認為電腦使用代理未來會如何改變日常工作流？歡迎在留言區分享你的看法 👇

#AI #ComputerUseAgent #AgentS #OSWorld #OpenSource #guiAgents #simularai #ICLR #COLM #AI研究
