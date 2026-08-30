---
title: 'Anthropic Opens a Research Preview of the Model Hardware Standard (MHS): A
  Shared Specification for  AI Agents to Safely Operate Physical Devices'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/29/anthropic-opens-a-research-preview-of-the-model-hardware-standard-mhs-a-shared-specification-for-ai-agents-to-safely-operate-physical-devices/
model: claude-code/sonnet
generated_at: '2026-08-30T10:55:39.497757'
score: 91
---

📌 【Anthropic 研究預覽】MHS 標準讓 AI Agent 操作實驗室硬體，設定從數週縮到數分鐘

TL;DR：Anthropic 推出 Model Hardware Standard（MHS），標準化 AI agent 與實體裝置溝通的驅動層，讓跨廠牌儀器整合不再需要人工寫轉譯程式。

一支四人團隊花了數個月手寫的雷射重鎖腳本，成功率只有 58%；同樣的問題交給透過 MHS 運作的 agent 迴圈，一夜之間跑出一支決定性 Python 腳本，700 次嘗試中成功 695 次。這是 Anthropic 這次研究預覽公開的其中一個案例，也點出了它想解決的核心痛點。

🤔 **實驗室硬體整合，卡在「沒有共通語言」**

一張實驗桌或一座工廠產線，通常是由彼此從未打算互通的廠商設備拼湊而成。每臺儀器都有自己的程式介面，專家得為每一對裝置手寫轉譯程式；就算接好線，agent 也沒有統一方式取得裝置狀態或安全地操作它們。根據 Anthropic 團隊的說法，這類設定通常要花上數週到數月，MHS 的目標是把這個時間壓縮到數小時甚至數分鐘。

🧩 **標準化「驅動層」：讀寫 + 探索 + 安全知識**

MHS 鎖定的是作業系統與裝置之間的「驅動」這一層，提供一組精簡的原語：read（例如讀取溫度）、write（例如設定溫度），加上裝置探索機制，讓裝置與 agent 能跨網路互相找到彼此，不再需要中間的轉譯層。

它也承載了程式碼本身無法編碼的知識，例如機械手臂的承重限制。使用者可以用自然語言寫下這些「driver tags」，或是讓 agent 直接訪談使用者來收集設定資訊；驅動程式會將這些標籤編譯成一份參考檔案，記錄裝置能量測什麼、能調整什麼、有哪些安全限制。控制介面則透過三種方式進行：Model Context Protocol（MCP）、CLI，以及程式碼檔案。MHS 是模型無關的，任何 agent harness 都能透過標準協定存取它。

📊 **五個實測場景的數據**

MarkTechPost 報導中列出了多個試用單位的具體結果：

| 單位 | 場景 | 結果 |
|---|---|---|
| Genentech | BCA 蛋白質分析自動化（液體處理機、機械手臂、盤讀儀） | Claude 自行試轉染色液、讀取吸光值，並以 RMSE 對照專家評分，收斂到水溶液 ~140 µL/s（0.016 RMSE）、黏稠 BSA 溶液 10 µL/s（0.181 RMSE），自動化專家確認參數合理 |
| QuEra Computing | 雷射重鎖腳本 | 人工腳本成功率 58%、每次約 150 秒；MHS agent 迴圈跑出的腳本成功率 99.3%（700 次中 695 次），最難情境僅需 10–14 秒（人工需 5–10 分鐘） |
| QuEra Computing | 伺服器調校 | Claude 將殘餘誤差從專家的 15.7 mV 降到 1.55 mV，19 小時運行中未曾失鎖，而專家調校平均每小時失鎖約 1.6 次 |
| Carnegie Mellon | 跨三臺不相容電腦的劑量反應實驗 | 從撰寫驅動到完成曲線約 8 小時（vendor 方案需數週），速度約快 3 倍；agent 曾在偵測到 R² < 0.9 時自主重跑；6 種人為製造的故障情境全數在裝置動作前被攔截 |
| University of Washington | Baker 與 Pinglay 實驗室 | 一名博士生一週內連接六臺儀器，含驅動撰寫 |

此外，Tetsuwan Scientific 將 MHS 與其 ResearchOS 平臺結合用於 qPCR 汙染分析；Janelia 的顯微鏡系統則從原本需依序啟動七支程式，簡化成單一儀表板點擊。

⚠️ **仍是研究預覽，泛用性有待驗證**

以上案例多來自 Anthropic 與合作單位提供的個案，屬於研究預覽階段，尚未經過大規模、跨產業的獨立驗證。MHS 能否成為業界公認標準，仍取決於更多廠商與實驗室的實際採用情況。

🎯 **實務啟示**

對於需要串接多臺異質儀器（尤其是缺乏統一 API 的老舊設備）的實驗室或產線團隊，MHS 提供了一個值得關注的方向：把「驅動」標準化，讓 agent 能透過 MCP、CLI 或程式碼檔案直接操作硬體，而不用每接一臺新裝置就重寫一次轉譯邏輯。目前可透過官方公告申請研究預覽資格。

🔗 **來源**
- 標題：Anthropic Opens a Research Preview of the Model Hardware Standard (MHS): A Shared Specification for AI Agents to Safely Operate Physical Devices
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/29/anthropic-opens-a-research-preview-of-the-model-hardware-standard-mhs-a-shared-specification-for-ai-agents-to-safely-operate-physical-devices/

#Anthropic #AIAgents #Robotics #LabAutomation #MCP #HardwareStandard #AIsafety #Automation #ScientificComputing #AgenticAI
