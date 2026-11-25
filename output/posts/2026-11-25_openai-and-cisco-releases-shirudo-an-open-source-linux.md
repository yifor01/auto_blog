---
title: 'OpenAI and Cisco Releases Shirudo: An Open-Source Linux Runtime Allowing Agents
  to Defend Systems Without Downtime'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/24/openai-cisco-shirudo-ebpf-linux-runtime/
model: claude-code/sonnet
generated_at: '2026-11-25T01:38:43.193484'
score: 104
---

📌 OpenAI 與 Cisco 聯手推出 Shirudo：用 eBPF 讓 AI Agent 在不停機下即時防堵漏洞

TL;DR：開源 Linux runtime Shirudo 讓 AI agent 寫出暫時性的 eBPF「盾」,在真正修補程式上線前先擋住已知漏洞。

修補漏洞從來不是「發現就馬上修好」這麼簡單,測試與部署真正的 patch 往往要花上數天甚至數週。而在這段空窗期裡,直接關掉整個有問題的 Linux 操作又太冒險,因為攻擊流量常常和正常請求共用同一條路徑。OpenAI 與 Cisco(背後工程團隊來自 Isovalent,也就是 Cilium 與 Tetragon 的開發者)針對這個「修補窗口」推出了 Shirudo。

🤔 **問題不是要不要修,而是修之前的這段空窗怎麼辦**

Shirudo 這個名字就是日文的「盾」。它本質上是 Isovalent 2022 年推出的 eBPF 安全平臺 Tetragon 的改寫版,核心想法是讓 AI agent 在等待真正 patch 的期間,先寫出一個臨時的「盾」來擋住漏洞被利用的那條程式路徑,同時讓合法請求繼續正常通行。

🧩 **三種盾、四個階段,Codex 當控制平面**

Shirudo 利用 eBPF 這個機制,在 Linux 核心內的掛鉤點(hook)執行經過驗證的小型程式。一個盾能做三件事:封鎖漏洞需要的程式路徑、替換掉有問題的程式碼,或是單純加入偵測可視性。這些盾被稱為 upatches,是以 BPF C 語言寫成、經過簽名的小型產出物。按照 Linux Plumbers 會議上 Daniel Borkmann 與 John Fastabend 的說法,團隊刻意沒有設計一套策略用的 DSL(領域特定語言),理由是 agent 直接寫程式碼反而效果更好。

Isovalent 描述了四個階段的流程,並以 Codex 作為控制平面:agent 先產生盾,操作者可以先在「觀察模式」看這個盾造成的實際影響,確認無誤後才核准正式啟用封鎖。安全把關不只這一層:核心會檢查每個載入器(loader)的簽名是否符合 .bpf keyring,eBPF 驗證器(verifier)接著檢查程式本身的安全性,TPM 2.0 則會記錄每一次載入與卸載的動作,並對驗證證據(attestation evidence)簽名。測試套件使用 ML-DSA-87 這種後量子簽名演算法,registry 流量則走 TLS 1.3 搭配混合式後量子金鑰交換。

📊 **實測案例:Java4Shell,一個 CVSS 9.2 的 Base64 解碼漏洞**

公開揭露的實測案例是 Java4Shell(CVE-2026-114938),一個存在於 OpenJDK Base64 解碼器裡的堆積損毀(heap corruption)漏洞,CVSS 4.0 評分 9.2,影響 OpenJDK 17.0.6 及之後版本、搭配支援 AVX-512 VBMI 的 x86-64 處理器。這個漏洞由 Calif.io 於 10 月 24 日用 Codex 發現,Oracle 於 11 月 17 日發布正式修補。在空窗期間,Codex 針對 java.util.Base64$Decoder.decode0 產生了一個防護盾,掛載到一個正在運行的 Elasticsearch 9.5.5 節點上,成功擋下攻擊輸入,服務維持正常運作。不過這是目前唯一公開揭露的測試案例,沒有公布誤判率(false-positive rate)或額外的效能負擔數字。

⚠️ **宣稱是 eBPF,實際案例卻是 Java bytecode**

值得注意的是素材裡出現了一個描述上的落差:OpenAI 把盾整體定調為 eBPF 機制,但 Isovalent 自己的技術文章指出,這次 Java4Shell 的具體案例其實是 Java bytecode 層級的盾,而 Java agent 的文件也把這類 upatch 稱為「應用程式內的緩解措施」,而非核心層級的防線;這些文件還提到該機制設計上只在啟動時(startup-time)載入,但這次示範卻是在執行階段(runtime)動態掛載上去的。另外,系統需求相當嚴格,對舊版核心完全沒有退路(fallback)方案。

🎯 **給工程師的啟示**

如果你的團隊常常被「漏洞已公開、patch 還沒準備好」的空窗期搞得提心吊膽,Shirudo 這種「先隔離、再修補」的思路值得關注,但目前只有一個公開案例、缺乏誤判率與效能數據,距離正式納入生產環境的安全事件應變流程,恐怕還需要更多獨立驗證。另外也要留意文件本身對 eBPF vs. Java bytecode 這種機制邊界的描述並不完全一致,評估時建議直接去讀 GitHub 原始碼確認真正的攔截層級。

🔗 **來源**
- 標題：OpenAI and Cisco Releases Shirudo: An Open-Source Linux Runtime Allowing Agents to Defend Systems Without Downtime
- 作者／機構：Asif Razzaq / MarkTechPost(技術來自 OpenAI 與 Cisco Isovalent)
- 連結：https://www.marktechpost.com/2026/11/24/openai-cisco-shirudo-ebpf-linux-runtime/

#eBPF #Shirudo #OpenAI #Cisco #Isovalent #LinuxSecurity #AgenticAI #ZeroDay #CloudSecurity #DevSecOps
