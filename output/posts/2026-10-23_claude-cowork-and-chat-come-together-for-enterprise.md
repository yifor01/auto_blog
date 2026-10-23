---
title: Claude Cowork and chat come together for Enterprise
source: Claude Blog
url: https://claude.com/resources/articles/unified-claude-enterprise
model: claude-code/sonnet
generated_at: '2026-10-23T20:35:23.232011'
pinned: true
---

📌 Anthropic 官方發布：Claude Chat 與 Cowork 正式合一，Enterprise 版全面開放

TL;DR：Claude Enterprise 的 Chat 與 Cowork 合而為一，雲端代理可離線持續工作。

以前用 Claude，得先決定「這只是問個問題」還是「這是要交付的完整專案」，兩種模式分開管理、分開收費邏輯也不同。現在 Anthropic 把這個選擇題直接拿掉了。

🤔 **從「選工具」變成「不用選」**

今年九月，Chat 與 Cowork 的整合體驗先在 Pro 與 Max 方案上線；這次則是正式推展到 Claude Enterprise 方案，屬於全面可用（GA）狀態。團隊成員不再需要在開始工作前先決定「這題該用 Chat 還是 Cowork」——對話一律從聊天開始，如果只是個簡單問題，馬上就能得到答案；當任務需要執行程式碼或處理檔案，Claude 會接著在雲端把工作做完，回傳完成的文件、分析或簡報。

🧩 **背後是 Anthropic 自己管理的雲端環境**

這套「代理型工作」跑在 Anthropic 管理的雲端環境裡，所以即使使用者關掉筆電，工作仍會持續進行，之後可以在網頁、桌面應用或手機上接續查看。原本在 Chat 與 Cowork 裡使用的對話記錄、專案、connector、skills 與 plugin，都會沿用到這個統一後的體驗中，不需要重新設定。

📊 **企業客戶怎麼說**

文章引用了幾家企業的回饋。LabX 的 CTO Daniel Padilla 表示，整合前 Chat 與 Cowork 是分開管理的兩套系統，整合後變得單純，而且 connector、skills、MCP 的轉換過程中「什麼都沒壞」。某機構的 CFO Paul Simpson 提到，他們不到十分鐘的提示過程，就讓 Claude 爬過一疊縣、州、聯邦層級的預算與公開會議文件，整理出資金流向，產出一份原本要花團隊數週才能完成的報告。Quantium 的 Harley Barnes 則說，整合解決了客戶常問的「該用哪個 Claude」的困惑；Carvana 的 Charles Sellers 指出，員工可以在電腦上開始任務，之後用手機接續查看，符合他們不只是坐在辦公桌前工作的團隊型態。

💡 **成本怎麼控管**

由於代理型工作比單純聊天可能消耗更多 token，Anthropic 為 Enterprise 管理員準備了四種控管工具：新推出的 Efficient mode 會把整合後的 Claude 體驗限制在 Sonnet 與 Haiku 模型上；Model entitlements 可設定每個角色能使用哪些模型；Spend limits 可在組織、群組、個別成員三個層級設定花費上限；而「pooled group budgets」則讓群組共享一筆每月預算。計費仍是按使用量計算，文章也提到新一代模型的效率提升：Claude Opus 5.5 在典型工作負載下的執行成本比 Claude Opus 5 低 40%，Claude Sonnet 5.5 則比 Claude Sonnet 5 便宜最多 30%。

⚠️ **安全與既有設定的銜接**

這次整合建立在企業已經在用的安全控制之上，包括 SSO 與 Compliance API，資料在傳輸與儲存時皆加密，且預設不會用於模型訓練。代理型工作在雲端 session 中執行，每個 session 跑在獨立的虛擬機器裡，Enterprise 方案預設關閉網路對外連線（egress），connector 的憑證也保存在沙箱之外。若組織原本使用 Claude Code 的零資料保留、HIPAA-ready 設定或客戶自管加密金鑰，則會維持現有設定不受影響。

🎯 **實務啟示**

對工程團隊而言，這代表以後不用再教新人「什麼時候該切到 Cowork」，入口統一後，心智負擔降低；但管理員需要重新熟悉 Efficient mode、model entitlements 等新的用量控管工具，才能避免代理型工作在不知不覺間消耗掉比預期更多的 token 預算。

🔗 **來源**
- 標題：Claude Cowork and chat come together for Enterprise
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/unified-claude-enterprise

#Claude #Anthropic #ClaudeEnterprise #AIAgent #EnterpriseAI #Cowork #AIProductivity #CloudComputing #AISecurity #LLM
