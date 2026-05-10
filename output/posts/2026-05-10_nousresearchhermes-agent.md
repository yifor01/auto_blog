---
title: "NousResearch/hermes-agent"
source: GitHub Trending
url: https://github.com/NousResearch/hermes-agent
score: 122
model: tencent/hy3-preview:free
generated_at: 2026-05-10T19:16:12.294399
---

📌 **Hermes Agent**

你有沒想過，一個 AI 代理能自己寫技能、在使用中變得更好，而且不綁死在你的筆電？  
它可以跑在 $5 VPS 上，閒置時幾乎不花錢，卻隨時透過 Telegram、Discord 甚至 CLI 與你對話。  
開發者再也不用被單一模型鎖住，想換就換，零程式碼異動。

🤔 **為什麼現在需要「自學習」代理？**  
隨著 LLM 能力提升，單次 prompt 已無法滿足長期、複雜任務的需求。開發者希望代理能從實際操作中累積經驗、自行改進技能，並且在不同對話階段保持記憶連續性——這些是目前多數開源代理仍缺少的能力。

🧪 **Hermes Agent 的核心設計**  
- **內建學習迴圈**：代理會根據過往對話自行創造技能，並在實際使用過程中自我優化。  
- **跨會話記憶**：透過 FTS5 全文搜尋 + LLM 摘要，能檢索並總結先前對話，構建「誰是你」的深入模型（Honcho dialectic user modeling）。  
- **多平台統一入口**：單一 gateway 同時支援 Telegram、Discord、Slack、WhatsApp、Signal 與 CLI，語音備忘錄亦可轉錄。  
- **終端級體驗**：完整 TUI，支援多行編輯、斜線命令自動補全、中斷與重導向、工具輸出即時串流。  
- **模型自由切換**：透過 hermes model 指令，可即時切換 Nous Portal、OpenRouter（200+ 模型）、NVIDIA NIM、Xiaomi MiMo、z.ai/GLM、Kimi/Moonshot、MiniMax、Hugging Face、OpenAI 或自有端點，無需改碼、無鎖定效應。  
- **自動化與維護**：內建 cron 排程器，可將任務結果發送至任意平台，並提供每日回報、夜間備份、週次審核。

🔍 **深入分析：閉環學習如何改變使用模式**  
傳統代理依賴外部提示或人工微調才能學會新技能；Hermes 讓代理自己觀察任務結果、產出新的「skill」，並在後續使用中不斷打磨。這意味著：  
1. **知識沉澱**：經驗不再隨對話結束而遺失，而是被納入代理的長期記憶庫。  
2. **技能自我迭代**：同一個技能在反覆使用過程中會變得更有效率、更貼合使用者的工作流程。  
3. **使用者模型持續精進**：Honcho dialectic 會根據跨會話行為調整對使用者的理解，使後續互動更具個人化。

⚠️ **已知限制（基於目前說明）**  
- 效能高度依賴底層 LLM 的品質與回應速度。  
- 文件中未提供正式基準測試，實際技能獲取與改進速度需社群驗證。  
- 作為早期專案，部分進階功能（例如複雜多代理協作）尚未詳述。

🎯 **給開發者的實務建議**  
- 先在低成本 VPS 上部署，體驗跨平台對話與語音轉錄的即時性。  
- 利用「hermes model」指令快速在不同模型間切換，評估哪種後端最適合你的特定任務。  
- 把日常重複的指令或工作流程包裝成 skill，讓代理在使用過程中自行優化，減少手動維護成本。  
- 定期查看代理產出的每日報告與週次審核，確保學習迴圈朝預期方向發展。

🔗 **專案連結**  
📂 GitHub：https://github.com/NousResearch/hermes-agent  
🏷️ #HermesAgent #NousResearch #AIAgents #OpenSource #LLM #SelfImproving #TUI #CrossPlatform

歡迎在留言區分享你的部署經驗或對自學習代理的期待 👇
