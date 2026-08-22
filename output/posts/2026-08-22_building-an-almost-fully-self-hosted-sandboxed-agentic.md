---
title: Building an (almost) fully self-hosted, sandboxed, agentic software factory
source: Hacker News
url: https://blog.jakesaunders.dev/building-an-almost-fully-self-hosted-sandboxed-agentic-software-factory/
model: claude-code/sonnet
generated_at: '2026-08-22T06:27:58.128669'
score: 81
---

📌 一臺舊電腦，一句提示詞：自架沙盒化Agent軟體工廠實測

TL;DR：工程師用兩臺自架伺服器打造隔離的Agent開發環境，一句指令跑完從寫程式到上線的整條SDLC。

把root權限交給AI在auto模式下自由發揮，你敢嗎？部落格作者 jakelsaunders94 選擇了另一條路：不是信任AI，而是用實體隔離把它結構性地關住。

🤔 為什麼不直接用雲端Agent

作者平時用Claude一次性寫小工具已經很習慣，但讓LLM在自己機器上擁有root存取權，始終讓他不安。於是他提出挑戰：能不能打造一個完全遠端的Agent開發環境，讓LLM自主走完研究技術棧、規劃寫程式碼與測試、提交Git並跑CI、最後部署到具備資料庫、可觀測性與SSL網域的「正式環境」——而且全程跑在自己的家用伺服器上，不額外增加雲端帳單。

🧩 兩臺伺服器與一整套自架工具鏈

作者手上有兩臺機器：一臺是跑了五年家用實驗室的2014年雙核i3，同時扛著這個部落格與約45個Docker容器（從Pi-hole到Prometheus／Loki／Grafana），並且對外轉發了443埠；另一臺是剛從eBay買來、乾淨無安裝的2021年第10代i7、32GB記憶體，專門用於這次實驗。

核心開發技術棧全部自架：Pi-hole 提供本地DNS規則；Tailscale 讓家用網路跟著人走；Coolify 是架在Docker上的自架版Heroku式PaaS；Forgejo 搭配runners提供自架Git與CI；Hermes（含WebUI）是使用Codex做推論的類OpenClaw虛擬助理；Telegram讓作者能隨時跟Agent對話；自架版Firecrawl作為Agent與網頁之間的爬取／轉譯層；Porkbun作為網域註冊商，搭配Let's Encrypt動態簽發SSL憑證。整個實驗中，唯一額外的持續成本是每月20英鎊的Codex訂閱，推論本身仍走OpenAI雲端。

🔐 隔離設計：實體隔離＋零對外入口

第一層防護很直接：新伺服器是獨立實體機，就算Agent下了`rm -rf /`，最壞情況也只是花幾小時重建。第二層是網路層面：這臺新機器沒有對外轉發443埠，等於沒有任何對外入口，砍掉一大塊攻擊面，也避開了針對每個DNS紀錄探測`/wp-admin`之類的背景雜訊掃描。

要在沒有對外入口的情況下仍能用手機存取服務，作者利用Tailscale把舊伺服器設為出口節點，出門在外連上後流量會經過Pi-hole解析自訂DNS，再靠dnsmasq規則把`*.internal.jakeshomelab.me`導向新伺服器內網IP，由Coolify的反向代理接手服務。

SSL憑證則靠DNS-01挑戰解決：在Porkbun申請具寫入權限的API金鑰，寫進Coolify環境變數，並在Coolify的Docker Compose設定中加上lego與Porkbun provider的挑戰參數。之後每次註冊新網址，Traefik／Coolify會透過Porkbun API建立`_acme-challenge`子網域的TXT紀錄，Let's Encrypt驗證通過後核發憑證，全程不需要對外公開任何A或AAAA紀錄——網址仍可能出現在公開的憑證透明度紀錄中，但服務本身只有在Tailscale網路內才能連上。

📊 一句提示詞跑完的成果

按作者描述，這套環境從單一提示詞出發，自動建立倉庫、寫出應用程式與測試、讓CI變綠、佈建Postgres，並把完成的應用部署到HTTPS網域之下，過程中作者沒有再發一則訊息。

⚠️ 還沒解決的麻煩

作者坦言把Hermes與Firecrawl的金鑰設定到位是「一件很痛苦的事」；不使用GitHub是因為擔心把GitHub token交給這臺機器會削弱隔離性，且GitHub的API與CI分鐘數限制也撐不住這種規模的自動化。整套系統也並非完全自架：推論本身，以及Tailscale、Telegram、DNS、ACME等整合服務仍走公開雲端。

🎯 給工程師的參考價值

這篇實測示範了一種務實的Agent安全邊界思路：與其在同一臺機器上信任LLM的行為，不如用獨立硬體＋零對外入口的網路拓樸做結構性隔離，再靠DNS-01挑戰在不暴露公開IP的前提下，仍然拿到可用的HTTPS憑證。對於想在本機或內部環境實驗自主Agent、又不放心給予機器完整存取權的團隊，這套組合（實體隔離＋Tailscale出口節點＋DNS-01）是一個成本可控、可複製的起點。

🔗 來源
- 標題：Building an (almost) fully self-hosted, sandboxed, agentic software factory
- 作者／機構：jakelsaunders94
- 連結：https://blog.jakesaunders.dev/building-an-almost-fully-self-hosted-sandboxed-agentic-software-factory/

#AIAgent #SelfHosted #HomeLab #DevOps #Sandboxing #Tailscale #Coolify #Forgejo #LLMSecurity #SoftwareFactory
