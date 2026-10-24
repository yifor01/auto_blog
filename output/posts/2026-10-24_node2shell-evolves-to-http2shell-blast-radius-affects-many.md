---
title: Node2Shell evolves to HTTP2Shell, blast radius affects many HTTP libs and apps
source: Hacker News
url: https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497
model: claude-code/sonnet
generated_at: '2026-10-24T19:41:44.549063'
score: 50
---

📌 Brotli 解碼漏洞三天內擴散:Node2Shell 進化成 HTTP2Shell,CVSS 9.2

TL;DR：CVE-2026-111497 影響幾乎所有解碼 Brotli 的 HTTP 函式庫,務必立即檢查依賴並升級。

一個星期前,這還只是 Node.js 社群自己的麻煩;三天後,它變成了 Python、C++、curl、Envoy、Istio 共同要面對的危機。這起被稱為「Node2Shell」,如今演變為「HTTP2Shell」的漏洞,正考驗整個 HTTP 生態系的修補速度。

🤔 **Brotli 是什麼,為什麼牽連這麼廣**

Brotli 是 Google 開發的無損壓縮演算法與資料格式,被廣泛用於 HTTP 內容壓縮,像 HTML、CSS、JavaScript 傳輸前都會先用它壓縮,接收端再解壓縮還原。正因為幾乎所有現代 HTTP 客戶端與伺服器都內建或依賴它做壓縮,一旦解碼器本身出問題,波及範圍會是整條 HTTP 生態系。

🧩 **CVE-2026-111497 到底哪裡壞了**

這是 Google Brotli 解碼器中的一個 out-of-bounds write 缺陷,影響 1.0.3 到 1.2.0 版本,CVSS v4.0 評分高達 9.2(Critical)。簡單說,解碼器在該拒絕資料時仍持續接受更多位元組,導致小型工作緩衝區溢位、破壞記憶體,攻擊者可藉此洩漏敏感資料、使程序當機,甚至執行任意程式碼。

更值得注意的是,OpenAI 表示他們早在 2026 年 2 月就發現此問題,並回報為「無需驗證的遠端程式碼執行」,而且是雙向的:惡意用戶端可攻陷未修補的伺服器,惡意伺服器也可攻陷接受壓縮回應的未修補用戶端。當時 Brotli 原始碼雖已修正根因,但沒人意識到這是安全漏洞,因此遲遲沒有對應的安全發布版本,導致每個打包了 Brotli 的專案都得自行補上這次更新。

📊 **受影響範圍與修補時程**

只要環境中存在 1.2.0 以下的 Brotli 或 brotlicffi 1.2.0.x 版本就屬於暴露範圍,而 requests、httpx、aiohttp 等 AI/ML 工程師日常使用的 HTTP 客戶端,只要偵測到這些套件存在就會自動載入。截至 10 月 23 日,各家安全資料庫尚未把這個 CVE 對應到 PyPI 套件,因此 pip-audit、Dependabot、Safety 目前都還抓不到。

已公布修補版本如下:

| 專案 | 修補版本 | 備註 |
|---|---|---|
| Node.js | 22.23.4 / 24.22.1 / 26.12.1 | 需使用對應支援中的release line |
| Bun | 1.4.4 | 已內含 Brotli 1.2.1 |
| Envoy | 1.40.0 / 1.39.3 / 1.38.6 / 1.37.8 | 1.36.12 也有修補但該分支已不再支援 |
| Istio | 1.29.9 / 1.30.6 / 1.31.2 | 1.29 已 EOL,建議升級到受支援分支 |
| Google Brotli(上游) | 1.0.10 / 1.1.1 / 1.2.1 | 依所用分支選擇對應修補版 |

此外,curl／libcurl 需更新其 Brotli 依賴至 1.2.1 或供應商修補版;若是靜態連結的應用程式,則要重新建置。值得慶幸的是,Apache 與 Nginx 預設都不解碼 Brotli,不在立即暴露範圍內。

⚠️ **還沒能升級?先做這些**

- Python 應用程式若 Brotli 支援是可選的,可直接卸載 Brotli 與 brotlicffi,並移除如 `httpx[brotli]` 這類會重新安裝它們的依賴 extras,重新產生 lock 檔案後重建並重啟服務。這樣 HTTPX、Requests、urllib3 仍保有 gzip、deflate 支援,但伺服器仍可能回傳 Brotli 導致回應無法解析,自動降級不保證成立。
- 在 Reverse Proxy、Load Balancer 或應用層 middleware 攔截 `Content-Encoding` 含有 `br`(不分大小寫)的請求,在任何有漏洞的解碼器處理前就拒絕。
- 對外發出的請求移除 Accept-Encoding 中的 br,並在自動處理回應前先檢查並拒絕 Content-Encoding 含 br 的回應——因為惡意伺服器可以無視用戶端宣告的編碼直接回傳 Brotli,urllib3 是依回應標頭來選擇解碼器,光改 Accept-Encoding 並不足夠。

🎯 **實務啟示**

對任何維運 API 服務或呼叫外部 HTTP 服務的工程師來說,這是一次典型的「隱藏在依賴鏈深處」的供應鏈風險:你可能從未直接匯入 Brotli,卻因為 requests 或 httpx 偵測到套件存在而自動載入。現在就該盤點專案依賴,確認 Brotli／brotlicffi 版本,並留意漏洞資料庫尚未同步到位、自動掃描工具暫時失靈的空窗期。

🔗 **來源**
- 標題：Node2Shell evolves to HTTP2Shell, blast radius affects many HTTP libs and apps
- 作者／機構：Dania Durnas, Aikido Security(經 Hacker News／theanonymousone 轉貼)
- 連結：https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497

#CVE #Brotli #HTTP2Shell #SupplyChainSecurity #NodeJS #Python #WebSecurity #CriticalVulnerability #Envoy #AppSec
