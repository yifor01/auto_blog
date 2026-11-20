---
title: 'Frostbite: A new CPU architecture discovered, designed and verified by AI'
source: Hacker News
url: https://architectlabs.com/blog/frostbite
model: claude-code/sonnet
generated_at: '2026-11-20T23:17:20.773677'
score: 106
---

📌 Frostbite：AI 從零設計的 CPU，效能功耗比衝上 4.59 倍

TL;DR：AI agent 群從零設計 CPU，效能功耗比達傳統核心 4.59 倍。

單核心 CPU 效能從 2000 年代初期就幾乎停滯不前，業界轉而靠堆疊多核心硬撐。Architect Labs 這次沒有在既有架構上微調，而是讓 AI 系統從零開始「發現」一套全新的指令集與硬體設計。

🤔 共享可變狀態，是效能停滯的根源

主流程式語言編譯到通用 CPU 時，會隱藏程式各部分之間的依賴關係：任何一段程式碼都能透過共享的可變狀態讀寫任何變數，硬體因此必須在執行期假設最壞情況，重新推算哪些指令之間真正互相依賴。這也是單核心效能停滯後業界要靠 Intel Xeon、AMD Zen、NVIDIA Vera 這類大型多核心 CPU 撐效能的原因；但多核心必須維持每個核心看到的記憶體都一致的假象，這需要很深的快取層級與一致性協定，耗費大量面積與功耗，且擴展性不佳。

🧩 用 interaction nets 把依賴關係直接攤開

Frostbite 的核心概念是 interaction nets：把程式表示成一個節點圖，計算就是透過節點的 port 重寫成對連接的節點。每次重寫只動到圖裡很小、局部的一塊；因為每個節點只有一個 principal port，不會有兩個活躍對互相重疊，所以這些重寫可以任意順序進行、甚至同時全部進行，結果都一樣。interaction nets 同時具備線性特性：每個值只會被使用一次，硬體不需要為共享可變狀態做任何保護。像 Vine 這樣的語言可以把一般寫法的程式直接編譯成 interaction nets。

文中以經典的五皇后問題為例：傳統 C++ 程式一步步走訪搜尋樹，而同一個搜尋寫成 interaction net 後可以同時探索許多分支，整個過程只需要 3,183 次互動、關鍵路徑僅 262 步，平均每一步就有約 12 次互動可以同時執行，而這個平行度並不是改寫程式換來的，是因為依賴關係本來就沒有被丟掉。理論上這帶來兩個好處：一是免費的多執行緒，平行度直接來自程式本身，不需要執行緒、鎖或競爭條件，也不需要傳統核心用來挖出平行度的失序機制；二是因為每個值只有一個擁有者、每一步都是局部的，資料可以就近放在小型本地記憶體，省掉傳統晶片花在大型快取子系統上的面積與功耗，以及維持快取一致性的系統複雜度。

🧩 先探索架構，再建系統模型，最後才寫 RTL

整個設計流程由 AI agent 群自主推進，且是零架構先驗起步。團隊先定義 Frostbite 該在哪些負載上表現優異，依照程式暴露平行度的方式分成五類：大量獨立工作、分輪次的平行工作、長序列鏈、資料相依分支、遞迴。每一類都建立了一組搜尋集與一組保留到最後才評估的 held-out 評估集，確保最終設計能推廣到從未調校過的程式上。FFT、radixsort、LU 等 kernel 沿用 SPLASH-2 benchmark 的實作，但縮小到 64 分之一的規模，因為正常規模不適合探索性工作；後續又加入 Kalman filter、PCA、有限元素分析、LU 求解、LZ4 解壓縮等 5 個更貼近實務的負載到 held-out 集合。

Agent 彙整研究論文與現有 benchmark，建立 Python 模型來權衡不同高層架構概念，最終收斂到單一架構概念，產出一份 141 頁的 PDF，涵蓋提議的程式設計模型、runtime 與晶片的高層區塊。但這份文件在第一輪 RTL 生成完成後就被刪除了，因為當中許多數字與估計與物理可行性有明顯落差。接下來進入正式的系統建模階段：團隊設計了一套全新的內部規格語言 ASL，並用它寫出 Frostbite 的系統模型「Arcmodel」。ASL 支援在 RTL、系統模型、UVM、SVA 等不同層級之間做可機器檢查的轉換與精煉，並透過「contracts」提供形式化驗證；其效能與功耗估算誤差在 1–5% 之間，執行速度比 RTL 模擬快約 200 倍。

📊 效能功耗比衝到 4.59 倍

在最初選定的 25 個負載（其中 15 個保留到最終評估才使用）上，Frostbite 相較於一顆經過矽驗證的現代超純量（雙發行、順序執行）CPU 核心，效能功耗比達到 4.59 倍。AI 系統自主迭代了編譯器、指令集、架構、微架構、RTL、驗證直到最終的 GDS。

⚠️ 文章未說明的部分

作者提到團隊在檢視所發現的架構原語時，發現了一些原本難以人工設計出來的硬體實作與 runtime 特性，但文中並未進一步說明這套架構在哪些負載類別上表現較弱，或量產良率、面積等細節。

🎯 實務啟示

這篇文章在 Hacker News 上拿到 600 點、316 則留言，熱度相當高，反映業界對「AI 能否自主發現硬體架構」這個問題的高度關注。對晶片與系統設計工程師而言，值得關注的不只是最終的效能數字，而是整套用形式化規格語言快速迭代架構、刪除過時文件、讓 agent 自主跑完整個 tapeout 流程的方法論，這或許比單一顆 CPU 的數字更值得借鏡。

🔗 來源
- 標題：Frostbite: A new CPU architecture discovered, designed and verified by AI
- 作者／機構：Architect Labs（經 Hacker News 用戶 shioyama 分享）
- 連結：https://architectlabs.com/blog/frostbite

#CPUArchitecture #InteractionNets #AIforChipDesign #HardwareDesign #RTL #ChipDesign #Semiconductors #AIAgents #ComputerArchitecture #Frostbite
