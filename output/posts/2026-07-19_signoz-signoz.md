---
title: SigNoz/signoz
source: GitHub Trending
url: https://github.com/SigNoz/signoz
score: 81
model: tencent/hy3:free
generated_at: '2026-07-19T08:05:55.111825'
---

📌 【SigNoz】用 OpenTelemetry 打造一體化開源可觀測性平臺

TL;DR：基於 OpenTelemetry 的開源 observability 平臺，整合日誌、指標、追蹤於單一介面。

監控工具鏈碎片化是許多團隊的痛點：日誌一套、指標一套、追蹤又一套。SigNoz 試圖把這些全部收進同一個地方。

🤔 **解決碎片化監控堆疊的問題**

SigNoz 是一套開源可觀測性（observability）平臺，建立在 OpenTelemetry 之上。README 指出，其目標是打造企業級的替代方案，取代碎片化的監控堆疊，將 logs、metrics、traces、alerts 與 dashboards 整合於單一平臺。

🧩 **三種部署模式，從雲端到自託管**

專案提供不同的執行方式，供不同需求的團隊選擇：

- SigNoz Cloud（推薦）：全託管服務，提供 30 天免費試用，不需信用卡，用量計費從 $49 起，並支援區域資料託管。
- Enterprise：包含 Enterprise Cloud、BYOC 或 Enterprise Self-Hosted，提供合規、支援、自訂保留期、RBAC、 ingestion 控制、資料駐留與區域選擇。
- Community：免費開源版本，可執行於自有基礎設施，透過 Docker、Kubernetes 或 Linux 部署，資料平面（data plane）完全由使用者掌控。

📊 **可監控的範圍涵蓋應用與基礎設施**

README 列出的監控能力包括：

- APM Overview：監控服務延遲、錯誤率、吞吐量、Apdex、熱門端點、資料庫呼叫與外部呼叫。
- Log Management：透過視覺化查詢建構器（visual query builder）擷取、搜尋、聚合日誌，並與 traces、metrics 關聯。
- Metrics and Dashboards：使用 Query Builder、PromQL 或 ClickHouse SQL 建立應用、基礎設施與自訂指標儀錶板。
- Infrastructure Monitoring：監控基礎設施（摘要於此處截斷，細節未完整提供）。

🎯 **實務啟示**

對於不想被綁死在單一商業監控產品、又希望減少工具維運成本的團隊，SigNoz 的 Community 版提供一條基於 OpenTelemetry 標準、可自託管的整合路徑；若人力不足，則可評估其雲端或企業方案。

🔗 **來源**
- 標題：SigNoz/signoz
- 作者／機構：SigNoz
- 連結：https://github.com/SigNoz/signoz

#OpenTelemetry #Observability #SigNoz #Monitoring #Logs #Metrics #Traces #APM #OpenSource #Kubernetes
