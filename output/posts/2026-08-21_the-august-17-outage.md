---
title: The August 17 outage
source: Hacker News
url: https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/
model: claude-code/sonnet
generated_at: '2026-08-21T06:41:22.434129'
score: 63
---

📌 GitHub 當機 7 小時 47 分：問題不是程式碼，是規模跟不上

TL;DR：GitHub 8月連兩次重大當機，官方坦承根因都是容量沒跟上流量成長。

如果你 8 月 17 日那天正在趕 deploy，卻發現 github.com、Actions、PR、Issues 全部打不開，你不是唯一一個。這場停機整整持續了 7 小時 47 分鐘，而且是這個月第二次重大事故。

🤔 一個月內兩次，問題出在哪

8 月 17 日的事故起因是流量衝上新高峰，GitHub 位於美國中部（Central US）資料中心的一項關鍵基礎設施元件沒能即時擴充容量。壓力隨後擴散到整個系統，引發身分驗證失敗，連帶影響 github.com、Actions、API、PR、Issues 以及 Copilot 等多項服務。這是繼 8 月 6 日 Actions 故障之後，該月第二起重大事故。GitHub 官方明確表示，兩次事故都不是程式碼或設定變更造成的，核心都是「容量沒跟上」。

🧩 復原過程：Copilot 的重試風暴讓問題雪上加霜

團隊透過重新導流、隔離受影響基礎設施、分階段恢復服務來處理事故。多數服務當天較早就恢復，但 Copilot 相關服務花了更久時間。原因是這些服務發生錯誤後，觸發了用戶端的重試迴圈（retry loop），在復原過程中反而把流量又推高了一波，團隊必須先緩解這個重試行為，才能安全地把流量導回來。

📊 這段時間 GitHub 做了什麼

官方指出，自 4 月以來每月 commit 數已從 14 億成長到 29 億，這解釋了系統承受的壓力，但不構成停機的藉口。作為今年稍早承諾的可靠性改善的一部分，GitHub 圍繞三個重點推進：增加容量、提升效率、移除架構瓶頸。目前已新增超過 300 萬顆 CPU 核心、120PB 高速儲存空間，並擴充了大量網路容量；在既有資料中心把供電允許範圍內的硬體全部裝滿，同時加速遷移到 Azure。如今 Azure 已承擔 GitHub 平臺約 58% 的負載、一半的 Git 操作，相較 5 月時僅 12% 有大幅提升。下一個里程碑是讓讀取容量能隨讀取者數量線性擴充的架構，將先從最大型的 monorepo 開始逐步推出。

💡 兩項立即改變：重試預算與被忽視的告警

這兩起事故各自帶來一項立即行動。第一，GitHub 正在服務間互動中導入一致的重試次數上限、重試預算與可變逾時（variable timeout），避免重試風暴造成連鎖負載，這正是 Copilot 復原延遲的成因。第二，團隊正在重新檢視過去被視為低優先級的 CPU 與記憶體告警，找出那些可能在流量驟增時率先失效的元件。

🎯 實務啟示

如果你的系統依賴外部服務，這次事故是一個提醒：客戶端重試邏輯若沒有退避（backoff）與上限設計，會在對方系統復原時反而成為壓垮駱駝的最後一根稻草。同時，容量規劃不能只看歷史峰值，成長速度本身（GitHub commit 量一年內翻倍）也該是告警與擴容策略的輸入變數。

🔗 來源
- 標題：The August 17 outage
- 作者／機構：GitHub（經 Hacker News 使用者 0xedb 分享）
- 連結：https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/

#GitHub #Outage #SiteReliability #Azure #CloudInfrastructure #Capacity #RetryStorm #DevOps #Incident #SoftwareEngineering
