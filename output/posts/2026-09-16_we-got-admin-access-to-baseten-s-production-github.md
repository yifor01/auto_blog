---
title: We got admin access to Baseten's production GitHub
source: Hacker News
url: https://www.strix.ai/blog/baseten-harbor-github-pat-takeover
model: claude-code/sonnet
generated_at: '2026-09-16T20:20:47.149455'
score: 92
---

📌 自主駭客Agent 25分鐘從公開映像檔挖出Baseten管理員金鑰

TL;DR：資安公司Strix用自家滲透測試Agent，在無任何憑證下挖出Baseten一枚存活逾3年的GitHub管理員Token。

如果一家估值130億美元、被大量企業信賴用來跑推論的公司，其最核心的GitHub repo管理權限，能被一支沒有原始碼、沒有任何登入憑證的自動化程式在25分鐘內拿到，你還會放心把資料交給它嗎？資安公司Strix在準備採用Baseten做推論服務前，先用自己開發的自主駭客Agent「Strix」對*.baseten.co做黑箱測試，結果就撞見了這個場景。

🤔 **為何一家推論服務商會被自己的潛在客戶掃描**

Strix打造了一款自主滲透測試Agent，因為需要便宜且快速的推論算力，Baseten是候選之一。但身為資安公司，他們的原則是：在把資料、模型或程式碼交給任何第三方之前，先掃一遍。這次他們刻意不提供任何原始碼存取或帳密，純粹從外部黑箱角度出發，理由是「最嚴重的漏洞常常藏在你自己都忘記的子網域服務上」。

🧩 **從公開的Harbor Registry一路挖到GitHub Token**

Strix先做網路資產枚舉、掃描憑證日誌，找到一個位於 `gcp-us-east4-zlw.registry.baseten.co` 的Harbor容器登錄伺服器。其中一個project被設為公開，Strix不需要任何Token，就能用匿名pull token列出repository並下載映像檔的manifest與blob，其中包括一個叫 `baseten/baseten-app` 的映像檔。

Strix沒有止步於「登錄伺服器暴露」這種metadata層級的回報，而是實際拉下映像檔，用開源工具TruffleHog掃描並直接檢視映像檔的build history。它先在裡面找到一組AWS金鑰，但用 `sts:GetCallerIdentity` 測試回傳 `InvalidClientTokenId`，代表這組金鑰已失效。接著,它在映像檔config的 `history[].created_by` 欄位裡，發現了一個RUN指令，裡面直接展開了 `GITHUB_TOKEN` 環境變數的實際值，也就是一枚貨真價實的GitHub個人存取Token（PAT）。

📊 **一枚2023年的Build Token，仍握有Admin權限**

Strix用這枚Token對GitHub發出唯讀的 `GET /user` 請求，回應是200，帳號名稱是 `basetenbot`。進一步檢查權限：GitHub回傳的 `X-OAuth-Scopes` 是 `repo`，帳號屬於 `basetenlabs` 組織。逐一檢查repository權限後發現，這枚Token對多個內部repo擁有 `admin: true`、`push: true`，包括Baseten的主要產品repo與驅動叢集的GitOps repo，另外還對數個私有repo（包含特定客戶專屬repo）擁有讀寫權限。這個build步驟的時間戳記是2023年3月3日，Strix在2026年7月測試時，這枚Token依然有效。確認影響範圍後，Strix沒有進一步clone、push或改動任何設定，直接停手並發出揭露信。

💡 **問題根源：把Token寫進了git設定，也寫進了映像檔歷史**

這個錯誤模式很常見：build過程需要抓取私有依賴套件，於是有人把GitHub Token當作build參數傳入，並用 `git config --global --add url."https://${GITHUB_TOKEN}@github.com/".insteadOf` 的方式讓git改用帶Token的URL做認證。問題是，Docker會把RUN指令的內容連同build history一起記錄進映像檔的config裡，即使日後清掉檔案本身，這份build history仍留著一份Token副本。Docker官方文件本身也對這種寫法有明確警告。

⚠️ **修復方式：不留痕跡，還要撤銷舊Token**

正確做法是用BuildKit的secret mount搭配臨時認證，確保憑證不會寫進映像檔任何層或config；同時要記得，改了Dockerfile不會影響已經被人下載走的舊映像檔，唯一的解法就是撤銷舊Token。值得一提的是，Baseten的資安團隊反應相當迅速，在確認為重大（critical）等級後，隔天下午前就鎖住了登錄伺服器project並輪換了Token。

🎯 **實務啟示**

不只要掃你的原始碼repo，也要定期檢查容器映像檔的build history，即使映像檔本身沒有留下憑證檔案，history裡的RUN指令仍可能藏著明文Token；任何用ARG傳入的憑證都該搭配BuildKit secret mount，並對長期存在的build用Token設定到期或定期輪換機制。

🔗 **來源**
- 標題：We got admin access to Baseten's production GitHub
- 作者／機構：bearsyankees (Strix)
- 連結：https://www.strix.ai/blog/baseten-harbor-github-pat-takeover

#Security #PenTesting #DevSecOps #Docker #GitHub #AIAgent #SupplyChainSecurity #ContainerSecurity #CredentialLeak #Baseten
