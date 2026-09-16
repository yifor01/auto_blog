---
title: Building a Linux GPU Driver for the M4 Mac Mini in One Month
source: Hacker News
url: https://codyho.dev/blog/gpu-driver/
model: claude-code/sonnet
generated_at: '2026-09-16T20:20:47.149665'
score: 89
---

📌 一個月逆向出M4 Mac Mini的Linux GPU驅動，AI協同加速逆向工程

TL;DR：兩位工程師靠hypervisor擷取硬體trace，一個月內逆向出Apple GPU韌體並做出可跑Minecraft的Linux驅動。

正常情況下，寫一個GPU驅動要花上好幾年。Cody Ho和Niklas卻在大約一個月內，替M4 Mac Mini與MacBook Neo做出一份完全符合OpenGL ES 3.0規範的驅動，讓Chrome、Firefox能跑WebGL、Minecraft能飆到200fps。

🤔 **延續上一個逆向專案，這次目標是GPU**

這個專案是作者先前打造一支用來逆向macOS的hypervisor之後的延伸。GPU幾乎是任何現代系統的必需品，沒有它一切都得靠CPU渲染，效能與能耗都差上好幾個量級。他們的目標是替M4 Mac Mini與MacBook Neo做出符合規範的OpenGL（接下來還打算做Vulkan）驅動，原本樂觀地想在幾天內做完，最後花了幾週。

🧩 **User Space與Kernel Space的分工**

現代GPU驅動一律拆成兩塊：kernel space負責跟硬體／韌體溝通、配置緩衝區與排程，user space則負責真正理解GPU的運作方式並填滿那些緩衝區。

在Apple Silicon上，kernel driver不會直接碰硬體，而是跟一顆執行自訂RTOS「RTKit」的GPU韌體溝通，所以第一步不是碰硬體，而是先搞懂韌體的ABI。作者形容Apple的做法像是「把一個正常的kernel driver切一半，一半塞進GPU韌體裡，另一半靠共享記憶體結構跟host端溝通」，許多結構裡韌體自己擁有的欄位跟host端控制的欄位是交錯排列的，必須靠逆向工程才能搞懂哪些欄位不能亂動。作者對比了Asahi Lina過去逆向M1/M2韌體ABI的知名成果，指出A18 Pro的韌體結構比M1/M2還複雜：結構數量多了1.5倍、指標數量多了2倍，送出工作的流程也更複雜。

作者採用的方法延續M1/M2那套逆向路線：先觀察macOS實際怎麼做，重播（replay）一遍，再自己動手重現。這一切都靠先前打造的hypervisor擷取硬體trace來實現。有趣的是，當作者向LLM（Codex）描述這個「重播」策略時，Codex把它照字面執行：等待第一個韌體可見事件（稱為「kick」）、存下整份GPU記憶體狀態，重開機後把存好的狀態複製回host記憶體、執行kick、觀察輸出頁面的變化，再嘗試順著指標重建出物件。隨著多次實驗，Codex逐步減少需要複製回去的頁面數量，直到完全靠自己從頭建構出所有物件。作者也提到，Codex展現出不錯的判斷力，知道什麼時候該再戳一下硬體、什麼時候該直接跑hypervisor自己去擷取狀態。

📊 **卡關兩次：render時機問題與336MB的compute trace**

過程中遇到三個主要問題，都源自難以取得一份「乾淨」的host端工作紀錄。第一個問題是韌體啟動後才送出的render工作：韌體啟動前預先排入的工作能正常完成，但一旦韌體開始運作，之後送進去的工作只會被ACK後直接丟棄，不會真正執行。作者後來讓Codex改用韌體生命週期中最早的一次擷取（韌體剛啟動後的第一筆），Codex幾乎馬上就找出問題，是缺了一個byte的descriptor，這個問題花了幾天排除。

第二個、也是唯一真正卡住進度的問題是compute工作。AGX支援render與compute兩種工作，在一般GUI流程裡，compute工作要等大量render工作跑完後才會被排程，導致很難拿到一份乾淨的compute擷取。Codex最終拿到的一份compute trace高達336MB，完全無法重播，即便嘗試靠分析內容自己重建物件，也花了超過一週仍未成功，內容太雜亂難以梳理。最後的解法反而來自另一個Codex session：開機進入單使用者模式關掉GUI（就不會有render工作）、安裝一個LaunchDaemon在Metal（Apple的專屬圖形框架）剛可用的最早時機執行、跑一個極小的自製Metal程式，成功擷取並重播了這份純compute的trace。

💡 **AI在逆向工程中的角色**

這篇文章讀起來最有意思的地方，是Codex並非單純被動執行指令，而是能自主決定何時該繼續戳硬體、何時該換一種擷取策略，甚至在被引導到正確的擷取時間點後，很快就自己定位出缺失的位元組。作者也強調整個過程屬於乾淨室（clean room）逆向：從頭到尾沒有查看任何Apple的二進位檔案，只依賴hypervisor擷取的硬體trace以及自己撰寫的shader，且所有實驗紀錄都已公開（文中提到的twin agx-re repos），供外界驗證來源正當性。

⚠️ **驅動還沒到能交給一般使用者的階段**

作者明確表示，這份驅動目前還未準備好給終端使用者使用，團隊的目標是盡快把它推向可用狀態。目前完成的是OpenGL ES 3.0的user-space驅動與對應的Linux kernel driver，Vulkan支援則是「接下來」的計畫。

🎯 **實務啟示**

這個案例展示了把LLM Agent用在需要大量試錯、狀態擷取與逐步重建物件的逆向工程流程中的可行性：只要人類負責把任務拆解成可驗證的小步驟（例如「先抓最早的一次擷取」），Agent就能在龐大又雜亂的硬體trace裡做出有效判斷，加速原本以年為單位的工作。

🔗 **來源**
- 標題：Building a Linux GPU Driver for the M4 Mac Mini in One Month
- 作者／機構：ADevWithAnIdea
- 連結：https://codyho.dev/blog/gpu-driver/

#GPU #ReverseEngineering #LinuxKernel #AppleSilicon #OpenGL #Vulkan #AIAssistedCoding #Codex #DriverDevelopment #SystemsProgramming
