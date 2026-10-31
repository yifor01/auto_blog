---
title: Vercel Labs Open-Sources agent-desktop for Agent Computer Use
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/31/vercel-labs-agent-desktop-computer-use/
model: claude-code/sonnet
generated_at: '2026-10-31T20:32:28.002284'
score: 97
---

📌 Vercel開源agent-desktop：不靠螢幕截圖,用無障礙樹操控電腦

TL;DR：Vercel Labs開源CLI工具agent-desktop,讓Agent透過OS無障礙樹讀取並操作桌面應用,自報token消耗可降78%至96%。

現在多數computer use方案靠截圖加座標點擊來操作電腦,一張截圖動輒上千token。agent-desktop選了另一條路:直接讀取作業系統的無障礙樹(accessibility tree),把畫面變成結構化JSON。

🤔 **螢幕截圖的隱性成本**

素材提到,Anthropic文件指出每張截圖約耗費1000到1800個輸入token,其工具集定義本身還會再增加約4500個輸入token。OpenAI的工具同樣以click、type、scroll動作讓程式執行。這些以視覺模型驅動的computer use方案,token消耗和模型依賴都偏重。

🧩 **一個工具,不是一個Agent**

agent-desktop是Vercel Labs用Rust寫的CLI與C函式庫,用於讀取並操作桌面應用,版本1.0.2於2026年10月30日以Apache-2.0授權釋出。它明確定位為「Agent呼叫的工具,不是Agent本身」——不內嵌LLM,沒有GUI,每個指令只印出一個JSON封包就結束,觀察、行動、驗證的迴圈留在呼叫它的Agent裡。

架構上,CLI或C函式庫呼叫agent-desktop-core,core只透過PlatformAdapter trait接觸作業系統,再由各平臺crate去對接原生無障礙API,core本身不會引入任何平臺crate,每個編譯出的binary只驅動一個作業系統。快照會分配帶限定格式的ref,例如@s8f3k2p9:e8,ref內含快照ID因此具有自我描述性,一個裸的@e8會被判定INVALID_ARGS拒絕;當UI發生變化,動作會回傳STALE_REF或AMBIGUOUS_TARGET,Agent需要重新拍一次快照——整套ref解析走的是嚴格、失敗即關閉而非猜測的路線。每個錯誤還帶有disposition標記,只有標示safe時Agent才該重試。

面對節點數量龐大的應用,--skeleton快照只讀取3層深度,被省略的容器會回報children_count並附上drill ref,再用snapshot --root把某個區塊讀進同一份快照。Ref動作是透過無障礙API執行,不會移動滑鼠遊標或搶走焦點,這讓Agent可以在背景操作、不打斷使用者手上的工作,全域的--headed旗標則允許在需要時切換成實體輸入;每個ref動作還會自動等待最多5000毫秒,直到目標變得可見、可用且穩定。

📊 **自報數據:Apple Maps單次讀取從3811token降到273**

建構者自報,相較於完整樹狀傾印,在Slack、VS Code、Notion中可減少78%至96%的token消耗;在Apple Maps中,每次讀取的token數從3811降到273;一個模擬的52步驟任務,token消耗從198k降到31k。素材特別註明,這些是自報數據,並非獨立基準測試結果。

安裝方式為npm install -g agent-desktop,也支援Bun、Yarn、pnpm,套件內附x64與ARM64原生binary。C函式庫讓Python、Swift、Go、Ruby、Node等語言可以直接呼叫,Agent可透過內建文件以agent-desktop skills get desktop指令學習工具用法,skills.sh上也有收錄。針對Electron網頁內容,launch --cdp可開啟DevTools埠供agent-browser使用。

⚠️ **數據未經第三方獨立驗證**

如前所述,78%至96%的token節省以及Apple Maps、52步驟任務的具體數字都是建構者自行測試後公開的結果,目前沒有獨立第三方複現的資料。

🎯 **實務啟示**

如果你的Agent需要操作本機GUI應用,且不想為每次觀察都燒一次視覺模型的token,agent-desktop提供了一個模型無關、結構化的替代路徑,可以和既有的shell-capable coding agent直接搭配使用。它嚴格的ref失效機制(STALE_REF/AMBIGUOUS_TARGET)也是個值得參考的設計:與其讓Agent對著過期狀態瞎猜,不如明確要求它重新觀察。

🔗 **來源**
- 標題：Vercel Labs Open-Sources agent-desktop for Agent Computer Use
- 作者／機構：Michal Sutter，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/31/vercel-labs-agent-desktop-computer-use/

#AIAgent #ComputerUse #VercelLabs #AccessibilityTree #OpenSource #AgentTools #DeveloperTools #RustLang #LLM #AgentDesktop
