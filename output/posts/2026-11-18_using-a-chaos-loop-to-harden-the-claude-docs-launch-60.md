---
title: 'Using a "chaos loop" to harden the Claude Docs launch: 60 server errors across
  billions of requests'
source: Claude Blog
url: https://claude.dev/blog/chaos-loop-claude-docs-launch/
model: claude-code/sonnet
generated_at: '2026-11-18T23:33:25.656627'
score: 105
---

📌 20億次請求、60次伺服器錯誤：Claude Docs怎麼扛住上線尖峰

TL;DR：Anthropic讓Claude自主跑兩週混沌測試，把Docs服務硬撐過上線尖峰且從未回滾。

三週前，Claude Docs還只是跑在單一節點上的概念驗證，內部使用者僅幾千人。上線後六天，使用者就建立了超過460萬份文件，橫跨20億次請求，伺服器錯誤只有60次，而且從頭到尾沒有一次回滾。撐起整個服務的，只有大約50個記憶體最佳化的pod。

🤔 **從幾千名內部使用者，到一天百萬份文件的壓力測試**

幾千名內部使用者跑在單一機器上，完全無法告訴團隊服務能不能撐過真實上線流量，而他們也沒有真實的上線流量可以拿來測試。於是團隊在上線前約兩週（9月4日），讓Claude操作一個鏡像正式環境的staging cluster，每天模擬超過一百萬份合成文件的流量，並故意刻意打垮核心元件，然後就讓它持續跑下去。

🧩 **混沌迴圈：一個coordinator session，底下掛著10幾個sub-agent**

整套架構是一個留在Claude Code裡持續運行的session：挑一個情境、跑測試harness、讀取telemetry、提出修正方案、把修正部署到staging、重複。這個coordinator session把大部分工作交給sub-agent執行，最忙的那週平均同時有11個sub-agent在跑，尖峰時達到30個。Coordinator還會透過Slack MCP跟Anthropic內部版的Claude Tag（beta）對話，向處理過類似規模服務的其他基礎設施團隊的agent請教擴展上踩過的坑。

團隊刻意設計了幾個偏執的情境：單日新增1000萬份文件、22,000個即時連線同時重新連接、一份熱門文件有數百人同時觀看時伺服器被強制關閉且資料庫同時卡住。每輪迴圈的流程固定：harness把某個功能（例如建立文件）的流量推到飽和，Claude讀取telemetry後回報幾個選項與一個建議方案；如果這個建議容易復原，Claude就直接寫程式碼、部署到staging、重新測試。

上線前，作者先告訴Claude哪些決策需要人工核准，基本上就是難以復原的變更，例如資料庫schema、key的排列方式，或是文件儲存與具體化方式的改變；Claude碰到這類決策會停下來徵詢意見，通常附帶一個建議，而作者多數時候都採納了。整個測試過程中，Claude必須遵守兩個不變條件：文件必須幾乎瞬間開啟（即使歷史很長），而且伺服器一旦確認收到編輯，測試就必須證明這筆編輯確實保留下來。

📊 **讓Claude看得懂系統，才是真正解決問題的關鍵**

每輪迴圈，Claude都會讀取telemetry，並補上它認為缺少的量測。記憶體問題是最具體的例子：某份大型文件一度在其pod上吃掉約3GB記憶體，Claude第一次嘗試是縮小其中一個快取讓伺服器更早釋出文件，但下一輪測試顯示記憶體其實藏在某個依賴套件內部的獨立快取裡,這個修正方向被放棄。Claude接著用更細粒度的記憶體剖析逐步縮小範圍,最終發現每次按鍵都會把文件複製進好幾種不同的資料結構，每次新增幾MB。解法是把這些結構改成copy-on-write，讓它們共用同一份參照而不是各自持有複本。經過約三天反覆迭代，那份文件的記憶體用量最終穩定在約180MB，團隊對上線所需pod數量的估計，也從超過500個記憶體最佳化pod降到約50個。

為了讓Claude量到的每個數字都能回溯到團隊自己寫的程式碼，他們挑選技術時特別挑剔：整個服務用Rust寫成，沒有垂圾回收機制，文件的所有記憶體都存放在他們自己定義的結構裡，一旦記憶體成長，Claude就能直接指出是哪個結構造成的，修改後立刻能在下一輪看到結果。他們也盡量減少依賴套件的數量，真正需要用到的少數套件則直接vendor進專案，方便自行檢視與量測。

📊 **上線週：首百萬份文件僅花30小時**

上線後約30小時就出現第一百萬份文件，到9月22日累積超過460萬份。整個9月團隊對正式環境部署了629次，一次回滾都沒有發生。

⚠️ **這套做法建立在特定的技術選擇之上**

文中強調，這整套流程之所以可行，關鍵前提是刻意避開使用記憶體或CPU行為不受程式碼直接控制的runtime（例如帶有垂圾回收的runtime），並坦言這也仰賴近期前沿模型的進步，使用的是大致相當於Claude Fable 5.2的內部研究模型,能連續數週維持同一個目標而不偏移。換成記憶體行為較不透明的技術棧，或模型能力不足以長時間自主運作，這套方法能否複製仍是未知。

🎯 **實務啟示**

對準備大規模上線的工程團隊而言，有兩個可直接借鏡的做法：一是在上線前用接近真實規模的合成流量，讓AI agent自主執行長時間的混沌測試,而不是只做小規模內部試跑；二是在系統設計上刻意追求「對AI legible」，也就是讓每一個可觀測指標都能明確回溯到自己寫的程式碼與決策，這樣AI才能真正做到自主診斷、修正並驗證，而不只是表面上跑測試。

🔗 **來源**
- 標題：Using a "chaos loop" to harden the Claude Docs launch: 60 server errors across billions of requests
- 作者／機構：Anthropic
- 連結：https://claude.dev/blog/chaos-loop-claude-docs-launch/

#AI #ChaosEngineering #Claude #Anthropic #SiteReliability #Rust #SoftwareEngineering #Scalability #AgenticAI #Infrastructure
