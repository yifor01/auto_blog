---
title: Active intrusion campaign against Check Point security management servers
source: Hacker News
url: https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign
model: claude-code/sonnet
generated_at: '2026-11-25T01:52:58.175229'
score: 67
---

📌 22 個組織淪陷：Check Point 管理伺服器遭入侵事件追蹤

TL;DR：GreyNoise 追蹤跨多國攻擊行動 GT13，疑似動用 LLM 與 agent 自動化滲透 Check Point 伺服器。

從一臺 Rejetto HFS 伺服器的隨機數產生器漏洞起手，攻擊者一路擴大成跨 22 個組織、24 臺 Check Point 管理伺服器的入侵行動，GreyNoise 甚至認為背後很可能有 agentic 系統在自動跑流程。

🤔 GreyNoise 怎麼發現這起攻擊

GreyNoise 用自家的 Global Observation Grid（GOG）感測器網路，刻意吸引攻擊性掃描與入侵嘗試，近乎即時捕捉完整入侵鏈，不需要等事後的事件調查。這次發現的是針對 Check Point Security Management Servers 的入侵行動，確認攻擊活動時間落在 2026 年 10 月 17 日到 11 月 2 日之間，影響至少 22 個組織。GreyNoise 把這組活動命名為 GT13，目前不歸因於任何已知或公開追蹤的 threat group，也沒有足夠資訊判斷動機或是否有國家背景。受害組織分布不集中於特定地區或產業，資產橫跨英國、愛爾蘭、法國、荷蘭、希臘、德國、奧地利、保加利亞、波蘭、印度、泰國、越南、南韓、香港、中國、澳洲、美國，涵蓋金融服務、能源、政府、運輸、礦業、工程、製造業等多個領域。

🧩 攻擊手法：偽造 session cookie，架起中繼跳板

攻擊者使用了 99 個 IP 位址，多數是用完即丟的拋棄式網路基礎設施，另外還有一臺被攻陷的伺服器被當作「operational relay box」（ORB，俗稱跳板），用來存放從 24 臺不同 Check Point Security Management Server 偷來的指令結果與資料。工具箱包括 Nmap、Chisel、Impacket、Paramiko 及其他 Python 工具，用於內部偵查、權限提升、橫向移動。攻擊者利用或嘗試利用的 CVE 包括 CVE-2026-61500（Rejetto HFS）、CVE-2025-5777（Citrix NetScaler）、CVE-2024-21893（Ivanti）、CVE-2026-41089（Windows NetLogon）、CVE-2026-16232（Check Point SmartConsole 認證繞過觸發 Run Script）、CVE-2026-98432（Linux IPv4 UAF）。

HFS 的入侵細節特別值得工程師留意：loginSrp1 端點每次 POST 都會回傳一個以 JavaScript Math.random() 產生 sid 值的 signed session cookie，攻擊者連續多次登入後蒐集到足夠輸出，重建出 V8 PRNG 的內部狀態，進而推算出 session cookie 的簽名金鑰，偽造出一個 admin session cookie，不用密碼就能登入管理員帳號。偽造出的 cookie 還帶著 allow_session_ip_change:true，等於讓這張 cookie 可以在任何 IP 下使用,對躲在 VPN 或多個出口後的攻擊者相當方便。時間線大致是：10 月 2 日偽造 cookie 拿到控制權 → 10 月 5 日安裝 HFS middleware hook，把 SSH 金鑰塞進 /root/.ssh/authorized_keys → 10 月 8 日用 HFS 指令 hook 執行「uname -a; df -h / | tail -1; whoami」確認狀態 → 沉寂到 10 月 19 日，攻擊者又重新用同一套 HFS 漏洞流程嘗試下載一個疑似叫「ZULT」的 Linux 植入程式，但下載失敗,還花時間排查原因 → 10 月 20 日改用直接 SSH 連線，建立 /root/exfil/srv_post2_<redacted>.py 架設未驗證的 HTTP server 開始上傳檔案,第一個外洩的 .tgz 壓縮檔就包含來自某臺已被入侵 Check Point Security Management Server 的網路路由掃描結果,證明攻擊者此前已拿到受害資產的存取權,接著還裝上 Nmap、Chisel,並把 Chisel server 架成 reverse proxy。

📊 攻擊規模

整起行動涉及 1400 多個 network session、800 多個 command-line artifact、1200 多個上傳、下載或建立的檔案。GreyNoise 的可視範圍在 11 月 2 日之後中斷,但因為攻擊者對受害的 Check Point 設備仍保有持續存取權,研判這起入侵行動可能仍在進行中,目前正與國際政府夥伴及 CERT 合作,通報受害組織。

💡 AI agent 到底有沒有參與？

GreyNoise 表示雖然觀察到 hands-on-keyboard 的操作痕跡,但「相信」跟現在多數攻擊一樣,攻擊者使用了 LLM 與 agentic 系統執行漏洞掃描、exploit 開發、工具開發與自動化互動——這是 GreyNoise 的研判,並非確鑿證據。一個旁證是 10 月 19 日那次操作：攻擊者明明已經透過 SSH 拿到存取權,卻「不知道為什麼」又繞回 HFS 漏洞流程重新偽造 cookie 去嘗試安裝惡意軟體,GreyNoise 推測這可能是 multi-agent 架構出了問題所致。

⚠️ 目前沒有歸因、沒有動機判斷,攻擊可能仍在持續進行。

🎯 給維運與資安工程師的實務啟示

如果環境中有 Check Point Security Management Server、Rejetto HFS、Citrix NetScaler、Ivanti 或暴露在外的 Windows NetLogon 服務,上述 CVE 的修補狀態都該立即盤點。另外也值得檢查自家系統的 session cookie 簽名機制是否仍依賴像 Math.random() 這類可預測的隨機數來源——這類弱點被用自動化工具重建 PRNG 狀態攻破的成本正在下降。

🔗 來源
- 標題：Active intrusion campaign against Check Point security management servers
- 作者／機構：GreyNoise
- 連結：https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign

#CyberSecurity #ThreatIntelligence #CheckPoint #GreyNoise #Infosec #CVE #IncidentResponse #AIAgents #NetworkSecurity #ExploitAnalysis
