---
title: "dograh-hq/dograh"
source: GitHub Trending
url: https://github.com/dograh-hq/dograh
score: 113
model: tencent/hy3-preview:free
generated_at: 2026-05-26T20:45:53.432421
---

📌 Dograh開源語音  

你以為語音 Agent 必須依賴付費 SaaS？Dograh 讓你兩分鐘內就能跑出自己的 bot，而且完全開源、自架。  
透過拖拉放置的工作流程建構器，零程式經驗也能快速組合語音對話。  

🤔 **開源自我架的必要性**  
現行的 Vapi、Retell 等方案均為封閉 SaaS，使用者必須接受供應商定價、資料托管與功能限制。當團隊希望完全掌控語音管線、自行選擇 LLM/TTS/STT 供應商時，現有選項往往會造成供應商鎖定。Dograh 正是為了解決這個問題而誕生：提供一個可以自行部署、原始碼完全可見的語音 Agent 平台。  

🧪 **拖拉放置工作流程 + 一鍵 Docker 部署**  
Dograh 的核心是一個視覺化的工作流程建構器，使用者可以直接拖曳節點來設計對話流程、插入 LLM 呼叫、連結 STT/TTS 服務。完成後，只要執行一行 Docker 指令（專案頁面提供完整指令），即可在本機或自有伺服器上啟動服務，官方宣稱「從零到可用 bot 低於兩分鐘」。  

🚀 **核心特點：BSD 授權、自架自由、完全可客製**  
- 授權：BSD 2-Clause，允許自由修改與再發布。  
- 自架：✅ 支援一鍵 Docker，亦可透過雲端服務取用（使用量計費）。  
- 模型與服務：✅ 帶入任意 LLM、STT、TTS 提供商，或使用 Dograh 內建堆疊。  
- 原始碼層級客製：✅ 每一行程式碼皆可修改，無閉源限制。  
- 資料與鎖定：✅ 資料住於自有基礎設施，供應商鎖定為零。  
- 其他：由 YC 畢業生與離職創辦人維護，曾被 Better Stack 專題報導，提供中文與英文文件。  

💡 **開放生態 vs. 封閉 SaaS 的取捨**  
與 Vapi、Retell 相比，Dograh 在授權、自架能力與原始碼透明度上具有明顯優勢，適合希望避免供應商鎖定、需要深度客製化或有特殊資料合規需求的團隊。不過，作為新興專案，其周邊工具鏈與社群套件仍在成長階段，企業級 SLA 與長期穩定性尚待更多實際案例驗證。  

🎯 **給工程師的實務建議**  
1. 若評估語音 Agent 平台，先在本機跑 Docker 版驗證核心功能。  
2. 依據現有技術棧選擇 LLM/TTS/STT 供應商，Dograh 允許「自帶模組」而不被綁定。  
3. 如需內部審計或資料主權，直接將服務部署於自有 VPS 或 K8s 叢集，享受完全的資料住宿權。  
4. 記得可透過設定 `ENABLE_TELEMETRY=false` 關閉匿名使用數據上傳，保護內部遙測需求。  

🔗 **專案連結**  
📂 GitHub：https://github.com/dograh-hq/dograh  
📖 文件與快速開始指南同上頁面提供  
📺 Better Stack 實機走through：專案頁面內含連結  

#Dograh #開源 #語音Agent #SelfHosted #VoiceAI #Docker #YC #BetterStack #AI開發 #無供應商鎖定
