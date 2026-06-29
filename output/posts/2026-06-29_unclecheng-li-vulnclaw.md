---
title: Unclecheng-li/VulnClaw
source: GitHub Trending
url: https://github.com/Unclecheng-li/VulnClaw
score: 102
model: google/gemma-4-31b-it:free
generated_at: '2026-06-29T20:24:51.968630'
---

📌 **VulnClaw：用自然語言驅動的 AI 滲透測試 Agent**

TL;DR：整合 LLM Agent 與 MCP 工具鏈，將「資訊收集到報告生成」的滲透流程自動化。

傳統的滲透測試依賴安全工程師在大量工具（如 Nmap, Burp Suite）之間手動切換並分析結果。如果能用「人話」下指令，讓 AI 自動編排工具鏈並驗證漏洞，滲透測試的效率將發生質變。

🧩 **以「目標驅動」取代固定工作流**

VulnClaw 並非簡單的指令指令碼，而是一個可獨立執行的 AI Agent。它將滲透測試建模為從 origin（起點）向 goal（目標）的狀態空間搜尋，核心設計包含：

- **黑板圖狀態空間搜尋**：透過記錄 Fact（已確認事實）與 Intent（探索方向），確保 AI 在探索過程中不會原地打轉。
- **目標驅動求解引擎**：不採取固定輪數，而是根據「目標是否達成」、「探索前沿是否耗盡」或「安全預算」來決定終止，讓執行過程自動收斂。
- **證據級反幻覺閘門**：為解決 LLM 常見的幻覺問題，所有聲稱的 flag 或結論必須在真實工具的輸出中「逐字元出現」才會被採信，防止 AI 編造假勝利。

🛠️ **核心技術架構與工具鏈**

VulnClaw 透過 LLM Agent 協調多方能力，實現從自然語言到實際攻擊的轉換：

1. **MCP 工具鏈**：整合 4 個 MCP 服務。`fetch` 與 `memory` 為本地實現；`chrome-devtools` 與 `burp` 則對接外部服務，實現瀏覽器自動化與 HTTP 抓包重放。
2. **Skill 體系**：內建 21 個滲透 Skill（7 個核心 + 14 個專項，涵蓋 Web/Crypto/Misc 等），並提供 180 個參考檔案。
3. **精確操作工具**：內建 29 種編解碼與加解密工具（如 Base64, AES, JWT 等），讓 LLM 透過精確呼叫而非猜測來處理資料。
4. **自適應反思機制**：將已知事實與攻擊鏈結構化沉澱，若攻擊失敗會自動歸類，並按 L0-L4 級別漸進式升級 payload 繞過策略。

📊 **自動化滲透的四個階段**

使用者僅需輸入如「幫我對 http://target.example.com 進行滲透測試」，Agent 將自動執行以下迴圈：

- **Round 1 資訊收集**：執行指紋識別、埠掃描、目錄列舉。
- **Round 2 漏洞發現**：檢測注入點、已知 CVE 及配置缺陷。
- **Round 3 漏洞利用**：進行 PoC 驗證並嘗試獲取許可權。
- **Round 4 報告生成**：產出結構化報告及 Python PoC 指令碼。

💡 **靈活的模型支援與執行控制**

- **廣泛的模型相容性**：支援 13 個 LLM Provider（包含 OpenAI, DeepSeek, MiniMax 等），透過 OpenAI 相容協議與 Tool Calling 實現一鍵切換。
- **持續性測試**：預設執行週期迴圈（100 輪/週期 × 10 週期），每週期自動生成報告直到手動終止。
- **執行環境**：內建 `python_execute` 工具用於構造 payload 與解析響應（作者提醒此功能目前屬高風險實驗能力，非強隔離沙箱）。

⚠️ **適用場景與限制**

本工具適用於已授權的滲透測試、CTF 競賽、安全教學及紅隊演練。使用者可透過 `think on/off` 切換是否顯示 LLM 的思考過程，以獲取乾淨的結論輸出。

🎯 **實務啟示**

對於安全工程師而言，VulnClaw 展現了「LLM Agent + 專業工具鏈」的整合潛力。其「證據級反幻覺」與「狀態空間搜尋」的設計，提供了將非結構化探索轉化為結構化攻擊路徑的參考實作，能大幅降低初步漏洞掃描與驗證的人力成本。

🔗 **來源**
- 標題：VulnClaw
- 作者／機構：Unclecheng-li
- 連結：https://github.com/Unclecheng-li/VulnClaw

#AI #LLM #PenetrationTesting #CyberSecurity #Agent #MCP #CTF #RedTeaming #Automation #VulnClaw
