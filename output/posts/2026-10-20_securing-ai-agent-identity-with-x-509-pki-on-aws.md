---
title: Securing AI agent identity with X.509 PKI on AWS
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/securing-ai-agent-identity-with-x-509-pki-on-aws/
model: claude-code/sonnet
generated_at: '2026-10-20T20:50:21.893330'
score: 95
---

📌 當AI Agent互相喊話時,誰能證明「我真的是我」?

TL;DR:AWS與Keyfactor用X.509 PKI打造多層憑證鏈,讓multi-agent系統具備zero-trust級的身份驗證。

當一個orchestrator agent把任務轉交給資料庫agent,再轉交給email agent時,接收端要怎麼確定對方不是被冒充的?答案不是共用API key,也不是把OAuth token一路傳下去,而是回到密碼學的老方法:X.509 公開金鑰基礎設施(PKI)。

🤔 **MCP沒有內建身分驗證,這是個缺口**

多agent框架越來越依賴Model Context Protocol(MCP)讓LLM agent呼叫外部工具與資料來源。但MCP在設計上是transport-agnostic,完全沒有定義身分驗證標準。這意味著任何元件理論上都能冒充agent、重播攔截到的憑證,或是在未授權的情況下呼叫工具。企業要落地zero-trust,這個缺口必須補上。

🧩 **三層信任邊界,四種機制**

這篇文章提出的參考架構結合AWS服務與Keyfactor的EJBCA(一套支援高可用部署、REST API自動化與OCSP驗證的PKI平臺),用四種機制交織出三層信任邊界:

- **簽署請求信封(signed request envelope)**:提供proof-of-possession。orchestrator每次呼叫sub-agent時,會把工具名稱、參數、timestamp與一個隨機nonce一起用RSA-PSS-SHA256私鑰簽署,接收端能驗證對方確實持有對應私鑰。
- **使用者簽署的委派聲明(delegation assertion)**:使用者的私鑰簽署一份JSON文件,列出三個agent憑證的SHA-256指紋、使用者subject name、發行時間與有效期限,證明使用者授權這些特定agent代表自己行動,而agent完全不持有使用者的私鑰或完整session的OAuth token。
- **RFC 8693 audience-scoped token**:應用程式先用OAuth 2.0 password grant向Keycloak取得完整session token,再透過RFC 8693 token exchange換成受眾(audience)限縮在MCP伺服器的downscoped token——只有這個範圍受限的token會交給agent,就算洩漏也碰不到組織內其他服務。
- **即時OCSP撤銷檢查**:憑證狀態變更能即時傳遞給所有agent。

整個流程從登入開始:應用程式在本地產生RSA 2048位以上金鑰對,透過EJBCA的`pkcs10enroll` REST API端點送出CSR,EJBCA簽署後回傳憑證;憑證與私鑰打包成PKCS12容器存進AWS Secrets Manager,私鑰從未離開應用邊界,不會傳給EJBCA、不會分享給agent,也不會寫入檔案系統。三個agent角色各用同樣流程取得各自憑證。

接收端收到簽署信封後,會執行六項驗證檢查才處理請求;若orchestrator需要重送同一個請求(例如暫時性失敗後重試),必須產生帶有新nonce的全新信封,舊信封即使是合法傳送者也無法重播。最終的MCP伺服器(FastMCP)是資料庫操作前的最後一道防線,在放行任何工具呼叫前會執行四項檢查,形成defense-in-depth。

💡 **私鑰不落地,才是這套設計的核心**

整套架構的精妙之處在於:使用者的身分始終留在登入流程裡,agent拿到的是「授權證明」而不是「使用者本人的金鑰」。這種分離讓單一agent被滲透時,攻擊者拿到的頂多是範圍受限、可被即時撤銷的短期憑證,而不是可以四處橫向移動的萬能憑證。

⚠️ **這是企業級方案,不是輕量套件**

EJBCA Enterprise是Keyfactor的商用產品,文中提到Keyfactor服務全球1,500多家企業客戶(金融、醫療、製造、政府等),要落地這套架構,代表企業需要具備對應的PKI維運能力與授權成本考量,並非拿來即用的開源工具。

🎯 **實務啟示**

雖然這篇以資料庫為保護資源做示範,但同樣的驗證模式可以套用在任何相容MCP的工具伺服器上。對於正在把多agent系統從demo推向生產環境、且必須符合zero-trust要求的團隊,這套「簽署信封 + 委派聲明 + 範圍受限token + OCSP即時撤銷」的四件組,是目前少見把PKI完整整合進agent通訊鏈的公開參考架構,原始碼已釋出在GitHub repo供調整套用。

🔗 **來源**
- 標題:Securing AI agent identity with X.509 PKI on AWS
- 作者／機構:Deepakkumar Sharma
- 連結:https://aws.amazon.com/blogs/machine-learning/securing-ai-agent-identity-with-x-509-pki-on-aws/

#AIAgent #ZeroTrust #PKI #X509 #MCP #AWS #Keyfactor #AmazonBedrock #CyberSecurity #MachineIdentity
