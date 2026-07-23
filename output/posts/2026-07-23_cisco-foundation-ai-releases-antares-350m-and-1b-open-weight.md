---
title: 'Cisco Foundation AI Releases Antares: 350M and 1B Open-Weight Models That
  Localize Known Vulnerabilities Inside Real Codebases'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/21/cisco-foundation-ai-releases-antares-350m-and-1b-open-weight-models-that-localize-known-vulnerabilities-inside-real-codebases/
model: tencent/hy3:free
generated_at: '2026-07-23T08:22:45.338000'
score: 81
---

根據您提供的資訊，這屬於「開源專案與產業新聞」的結合，重點在於 Cisco 發布的新模型及其技術細節。以下是為您撰寫的技術部落格文章：

📌 【Cisco Foundation AI】Antares 釋出：專攻程式碼漏洞定位的輕量化 SLM 模型

TL;DR：Cisco 發布 Antares 系列 SLM，透過結合 CWE 描述與終端機指令，精準定位程式碼庫中的漏洞檔案。

🤔 **安全開發的痛點：將外部漏洞知識與內部原始碼連結**

軟體安全性高度依賴於將外部的漏洞知識（如公共資料庫、公告或 CWE）與內部複雜且具依賴性的原始碼進行對接。對開發者而言，手動在大型模組化專案中搜尋、追蹤呼叫路徑並比對檔案，是一項極其耗時的成本支出。Cisco 將此「初步篩選（Triage）」階段視為成本最集中的環節。

🧩 **Antares：基於 IBM Granite 4.0 的專用安全小模型**

Cisco 釋出的 Antares 是一系列專為「漏洞定位（Vulnerability Localization）」任務設計的安全小語言模型（SLM）。其核心目標是：給定一個漏洞描述與一個程式碼庫，找出包含該缺陷的檔案。

*   **模型規格**：包含 350M、1B 及 3B 引數的三種 decoder-only transformer 架構。
*   **技術底層**：皆從 IBM Granite 4.0 檢查點（checkpoints）初始化，並共享相同的 tokenizer 與架構，包含 grouped-query attention、SwiGLU MLPs、RMSNorm 與 RoPE。
*   **運作機制**：模型並非作為獨立的序列模型評估，而是在受限的迴圈中執行。模型僅接收 CWE 類別描述，不提供公告文本或檔案提示，並透過 Docker 沙盒（停用網路）發出唯讀的終端機指令，指令輸出會截斷至 2,000 字元。

📊 **效能表現：與大型模型與 GPT-5.5 的對比**

Cisco 同時釋出了 Vulnerability Localization Benchmark (VLoc Bench) 進行評估。實驗結果顯示，Antares 並非追求突破性的 SOTA（State-of-the-art），而是展現了小模型在特定任務上的潛力：

| 模型 | File F1 分數 |
| :--- | :--- |
| Antares-1B | 0.209 |
| GPT-5.5 | 0.229 |
| 753B 開源模型 | 0.186 |

⚠️ **並非取代現有的安全工具鏈**

Cisco 特別強調，Antares 並不打算取代現有的應用程式安全工具鏈。開發團隊仍需依賴依賴項掃描（dependency scanning）、金鑰掃描（secret scanning）、動態測試、容器檢查、威脅建模以及專家審查。Antares 的定位是作為這些工具的前置篩選步驟。

🎯 **實務啟示**

對於安全工程師而言，Antares 的意義在於展示了「窄領域專業模型（Narrow SLM）」的價值。透過將模型限制在特定任務（如漏洞定位）並賦予其與終端機互動的能力，可以在維持輕量化的同時，實現比超大型模型更具針對性的開發流程最佳化。

🔗 **來源**
- 標題：Cisco Foundation AI Releases Antares: 350M and 1B Open-Weight Models That Localize Known Vulnerabilities Inside Real Codebases
- 作者／機構：Michal Sutter @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/21/cisco-foundation-ai-releases-antares-350m-and-1b-open-weight-models-that-localize-known-vulnerabilities-inside-real-codebases/

#Cisco #AI #Cybersecurity #SLM #OpenSource #MachineLearning #VulnerabilityLocalization #IBMGranite #SoftwareSecurity #LLM
