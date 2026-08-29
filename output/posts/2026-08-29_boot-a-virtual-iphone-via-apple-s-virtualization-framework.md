---
title: Boot a Virtual iPhone via Apple's Virtualization.framework
source: Hacker News
url: https://github.com/Lakr233/vphone-cli
model: claude-code/sonnet
generated_at: '2026-08-29T11:59:48.401849'
score: 98
---

📌 【開源工具】用Apple Virtualization Framework開機一支虛擬iPhone

TL;DR：vphone-cli讓你在Apple Silicon Mac上用官方Virtualization framework跑出完整iOS虛擬機。

在Hacker News上拿下294點與82則討論的vphone-cli,做的事情聽起來像天方夜譚:在Mac上,用蘋果自己的Virtualization framework,真正開機一支虛擬iPhone。

🤔 **解決什麼問題**

vphone-cli是一個命令列工具,利用蘋果的Virtualization.framework與PCC(Private Cloud Compute)研究用VM基礎架構,在Apple Silicon Mac上啟動虛擬iPhone。目標使用者是需要做iOS安全研究、越獄開發或自動化App測試,卻不想或不能佔用實體裝置的工程師。

執行前提包括:Apple Silicon、macOS 15(Sequoia)以上的主機、Xcode加iOS SDK(用來交叉編譯guest端的守護程式vphoned),以及放寬SIP/AMFI限制,以允許未簽章二進位使用私有的PV=3 entitlement。額外依賴透過Homebrew安裝,包含python@3.13、aria2、wget、gnu-tar、openssl@3、ldid-procursus、sshpass、keystone、cmake、libusb、ipsw、zstd。

🧩 **一行指令跑完整條pipeline**

安裝方式是`brew install zqxwce/tap/vphone-cli`,或從原始碼建置:clone repo(含子模組)後執行`./scripts/setup_tools.sh`安裝相依套件與工具鏈,再執行`./scripts/build.sh`完成簽章建置,產出.app bundle並交叉編譯vphoned。

最小可行範例只需兩個指令:

```
vphone-cli vm create myphone -V jb
vphone-cli vm launch myphone
```

第一行會自動跑完整條流程:下載IPSW→修補開機鏈→進入DFU模式還原→安裝CFW(客製韌體)→首次開機。如果想手動逐步操作,也可以拆成`vm new`(建立空的VM bundle)、`fw prepare`(下載並合併IPSW)、`fw patch`(修補開機鏈)、`vm launch --dfu`(進DFU開機)、`restore --get-shsh`與`restore`(還原)、`cfw install`(安裝CFW)、`vm launch`(正式開機)等步驟。工具本身也提供VM管理指令,如list、info、clone(快速APFS複製並產生全新裝置識別)、export/import(以zstd壓縮打包)、rename、delete。

修補韌體提供5種變體,依安全繞過程度遞增:`less`(4項修補,2階段,不繞過iOS原生防護機制)、`regular`(42項修補,10階段,繞過AMFI/SSV/Img4/TXM)、`dev`(53項修補,12階段,額外繞過TXM entitlement與debug限制)、`jb`(113項修補,14階段,完整越獄,首次開機自動安裝Sileo與TrollStore)、`exp`(141項修補,18階段,越獄功能的超集,額外加入反VM偵測的研究用修補)。

連線方式方面,越獄版可透過`ssh -p 22222 mobile@<vm-ip>`(密碼alpine)連入,一般版與dev版則用root帳號;也支援VNC(`vnc://<vm-ip>:5901`)。所有VM資料預設放在`~/.vphone/`下,細分VMs(各VM的bundle)、ipsws(下載並快取的IPSW)、tools(APFS seal-volume快取)、debs(CFW安裝時寫入guest的套件快取)、venv(自動建立的Python環境),每個路徑都可透過對應的環境變數覆寫。

要放寬SIP/AMFI限制有兩種做法:一種是在Recovery模式下完全關閉SIP(`csrutil disable`,並允許research guest),重開機後透過`nvram boot-args`加上`amfi_get_out_of_my_way=1`,屬於最寬鬆的做法;另一種是保留SIP在debug-only的放寬模式(`csrutil enable --without debug`),再用`vphone-amfidont`把工具本身加入白名單,讓系統其他部分的AMFI維持啟用。

README附上了實測過的主機與系統組合表,涵蓋Mac16,6/8/11/12等多款Apple Silicon機型,搭配從iOS 26.1到27.0 beta2、cloudOS 26.1到26.4等版本組合。

💡 **可程式化控制,適合接上AI測試流程**

vphone-cli還開放一個host端的控制socket(`<bundle>/vphone.sock`),可以用程式方式操控畫面截圖、觸控、滑動手勢、硬體按鍵與剪貼簿,每個動作都會回傳一張內嵌截圖,方便串接AI驅動的端到端測試。專案也提到有對應的vphone-mcp,把這個控制介面包裝成MCP server。

⚠️ **限制與已知問題**

README提及若主機本身就是一臺虛擬機,Virtualization無法巢狀執行PV=3 guest,必須用非巢狀的macOS 15+實體主機。另外也記錄了一個已知的相依套件bug:目前Homebrew穩定版的ldid-procursus(到2.1.5-procursus7)在處理entitlements plist中值為0的整數欄位時,因為對`__builtin_clzll(0)`缺少零值防護,會導致寫入迴圈失控、記憶體持續攀升,官方建議改用`brew install --HEAD ldid-procursus`從原始碼建置。專案特別鳴謝了wh1te4ever/super-tart-vphone-writeup作為參考基礎。

🎯 **實務啟示**

對做iOS安全研究或App自動化測試的工程師來說,vphone-cli把原本需要實體裝置或商用工具才能做的事,變成可以完全自動化、可腳本化、可批次建置的流程,加上開放的控制socket,很適合直接整合進CI或AI agent的測試管線中;但要留意它高度依賴放寬系統安全限制,部署前務必評估在自己環境中的風險。

🔗 **來源**
- 標題：Boot a Virtual iPhone via Apple's Virtualization.framework
- 作者／機構：hentrep(Hacker News), Lakr233/vphone-cli
- 連結：https://github.com/Lakr233/vphone-cli

#iOS #Virtualization #macOS #AppleSilicon #SecurityResearch #Jailbreak #OpenSource #DevTools #MCP #MobileTesting
