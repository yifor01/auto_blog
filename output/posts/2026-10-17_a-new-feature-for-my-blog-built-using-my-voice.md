---
title: A new feature for my blog, built using my voice
source: Simon Willison
url: https://simonwillison.net/2026/Oct/9/built-using-my-voice/
model: claude-code/sonnet
generated_at: '2026-10-17T19:41:49.300929'
score: 74
---

📌 用語音寫程式:Simon Willison 邊煮晚餐邊讓 ChatGPT Codex 生出新功能

TL;DR:語音加本機預覽的混合工作流,能把煮飯時間變成寫程式時間,但精確細節仍得靠打字收尾。

🎣 一邊炒菜一邊口述需求,電腦另一端就把資料庫遷移、View、樣板全部生出來——這不是什麼示範影片,是 Simon Willison 幫自己部落格加新功能時的真實紀錄。

🤔 他早就習慣用語音跟 AI 工作,但這次多了一塊「看得到的畫面」

Simon Willison 先前就常在遛狗時用 ChatGPT 語音模式做研究與腦力激盪,偶爾也讓它寫寫程式碼片段。這次不同的地方在於,他改用 ChatGPT 桌面版的 Codex 分頁,搭配語音對話模式,並且是對著本機開發環境在講話,所以能隨時用瀏覽器看到目前的進度。

🧩 流程:先開本機伺服器,再用語音把需求講給模型聽

1. 在本機 simonwillisonblog 專案輸入指令,啟動開發伺服器並在瀏覽器開啟預覽。
2. 點擊「Start new voice chat」(不是麥克風按鈕,是右側的語音對話鍵),把筆電搬進廚房,邊煮飯邊對話。
3. 用口語描述需求:這是一種新的內容類型(Newsletter),不該出現在標籤頁、日期彙整頁或部落格首頁,但要出現在對應日期的彙整頁;其中月費限定的內容,公開一個月後要能被搜尋到。
4. 模型(GPT-6 Astra High)理解需求後,陸續生成新的 model、資料庫遷移、view 程式碼、樣板,以及匯入外部資料的函式,過程中偶爾會反問澄清問題。
5. 整段語音對話持續約半小時,剛好是煮飯的時間,功能幾乎做到可以上線的程度。

💡 語音能帶你走到「幾乎完成」,但匯入邏輯還是得坐下來打字

其中一支匯入腳本的資料來源是私有 GitHub 儲存庫,Astra 原本選擇用 git 在子程序裡處理,但 Simon 認為用 API 金鑰的方式更適合他既有的其他匯入腳本做法,於是切換成打字模式,請 Codex 把這段改成以 API 存取,並新增一支 API 金鑰。最後讓 Codex 建立分支並開 PR,他在 GitHub 的 PR 介面裡 review 程式碼,除了把匯入機制換掉之外,還做了幾處公開頁面顯示上的微調,又花了額外半小時的打字式 prompt 才定案並正式上線部署。他的結論是:這套語音加視覺預覽加打字的混合互動方式,比單純語音模式強大許多,但還不會變成他的日常工作方式——一旦涉及貼錯誤訊息、直接指向某段程式碼這類精確溝通,打字依然比口述更有效率。他也坦言,在共享辦公空間根本不會想這樣對電腦講話,主要是在家工作才可行;對他來說,這個模式最大的價值是能一邊做家事一邊真正產出東西,而不只是聽播客。

🎯 這個案例顯示,語音驅動 coding agent 目前最適合處理「需求釐清」與「大範圍功能骨架搭建」這類模糊度較高、對話式的工作;一旦進入精確除錯、貼錯誤訊息或指定特定程式碼區塊,切回鍵盤仍是更有效率的做法。如果工作環境允許(例如在家工作、需要同時處理其他事情),語音加本機預覽的混合模式值得一試,能把原本「純用耳朵」的空檔時間轉換成實際產出。

🔗 來源
- 標題:A new feature for my blog, built using my voice
- 作者/機構:Simon Willison
- 連結:https://simonwillison.net/2026/Oct/9/built-using-my-voice/

#VoiceCoding #AIAgent #ChatGPT #Codex #DeveloperWorkflow #LLM #AIAssistant #Django #CodingAgent #AIProductivity
