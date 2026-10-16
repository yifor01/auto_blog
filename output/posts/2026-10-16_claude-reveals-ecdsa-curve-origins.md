---
title: Claude reveals ECDSA curve origins
source: Anthropic Research
url: https://www.anthropic.com/research/ecdsa-curve-origins
model: claude-code/sonnet
generated_at: '2026-10-16T20:06:19.068239'
pinned: true
---

📌 【Anthropic】Claude 解開 ECDSA 曲線種子 25 年懸案

TL;DR：Claude 不到 30 分鐘就查出 NIST 加密曲線種子的真正來源，終結了業界 25 年的後門疑雲。

NIST 在 2000 年公布的橢圓曲線加密標準裡，藏著一組由 NSA 提供、卻從未附上任何解釋的神秘數字。25 年來，密碼學界始終在猜：這組數字裡，是不是藏著只有 NSA 知道的後門。

🤔 **一個被懷疑了 25 年的「種子」**

ECDSA 是目前最廣泛使用的橢圓曲線加密標準，2000 年由 NIST 納入 FIPS 186-2 數位簽章標準。標準為不同大小與安全等級的曲線各列出一個「seed」參數，其雜湊值會用來決定曲線係數 b。以 NIST P-256 為例，標準只給出一串十六進位數字，完全沒有說明這串數字從何而來。Koblitz 與 Menezes 曾為此寫下知名的〈A Riddle Wrapped in an Enigma〉，業界甚至為解謎設立懸賞。流傳最廣的說法來自前 NSA 工程師 Jerry Solinas：種子可能是把一句玩笑話（像「給 Bob 和 Jerry 加薪」）雜湊產生的，但他本人也說不清楚細節，實際寫程式的同事也記不得了。Solinas 於 2023 年去世後，這條線索就此斷了。

🧩 **Claude 不信那個玩笑話，改用逆向工程的方式去猜**

Anthropic 員工先按傳聞中的那句玩笑話去搜尋，一無所獲。研究人員後來請一個內部研究模型嘗試在不被提示線索的情況下，自己找出種子的生成方式。Claude 改走另一條路：推測生成這些曲線的程式，當年很可能用的是 1990 年代 C 函式庫裡常見的偽隨機數生成器（PRNG），而這類老舊演算法的輸出帶有可被辨識的規律。Claude 寫了一個掃描程式，逐個位元滑動比對每個公開種子，檢驗相鄰區塊是不是某個 1990 年代 PRNG 的連續輸出，總共測試了 34 種生成器與輸出切片的組合。過程中它發現一個異常：十組種子裡有四組，寫成五個 32 位元字後，前導位元全部是 0，純屬機率巧合的可能性只有 1/5810。這正是 linear congruential generator「lrand48」的特徵，它的 48 位元內部狀態只會輸出最高的 31 位元。針對這四組，Claude 窮舉剩下 17 個隱藏位元的 2 的 17 次方種可能，驗證後續四個字是否接續，全部成功還原。至於其餘的質數曲線種子，因為保留的位元更少，還原內部狀態變成一個標準的格（lattice）問題，Claude 改用 Lenstra–Lenstra–Lovász（LLL）格基約化演算法在每個可能的位元窗口上求解，最終發現 5 組 NIST 與 5 組 ANSI X9.62 質數曲線種子，全都符合「lrand48() >> 23」的模式。

📊 **時間戳記，不是雜湊：P-256 跑了 1842 次才湊出標準種子**

由於這個生成器可以直接逆推，Claude 把狀態往回推算到 srand48 的初始化形式（低 16 位元固定為 0x330E），進而還原出對應的 Unix 時間戳記。結果顯示，十組質數曲線種子對應的初始化時間，全部落在 1997 年 5 月到 1998 年 4 月之間；以 P-256 為例，程式整整跑了 1842 次迭代才產生出標準化的種子。另外四組二元曲線（binary curve）種子的時間戳記讀出來是 1984 年 2 月，但若把數值加倍，則對應到 1998 年 4 月 17 日，剛好在 P-224 產生後兩週，這讓 Claude 推測當年的程式可能把時鐘數值減半處理。在調查過程中，Claude 也順帶找出 P-192 與五條 ANSI X9.62 曲線（同在 1997 年 5 月生成）基點（base point）的來源線索。

💡 **這不是漏洞，而是「清白證明」**

Anthropic 特別強調：這項發現不是密碼學攻擊，也不是曲線本身的弱點，反而讓人更有信心這些曲線並未被蓄意植入後門。因為種子的生成方式極其簡單、完全透明，只是一個用時鐘初始化的常見 PRNG，任何人現在都能重現同樣的流程，這讓「刻意動手腳」的操作空間大幅縮小。

🎯 **實務啟示**

這個案例展示了 LLM 在資安鑑識與逆向工程上的一種新用法：不是暴力比對已知線索，而是從「當年的工程師可能用什麼工具」反推，再動手寫程式驗證假設。對做安全研究或處理老舊系統稽核的工程師，這種「假設生成演算法 → 寫掃描工具驗證 → 用數學方法還原內部狀態」的流程，值得作為處理類似歷史謎團的參考範本。

🔗 **來源**
- 標題：Claude reveals ECDSA curve origins
- 作者／機構：Anthropic (Frontier Red Team)
- 連結：https://www.anthropic.com/research/ecdsa-curve-origins

#Anthropic #Claude #ECDSA #Cryptography #NIST #SecurityResearch #ReverseEngineering #PRNG #LLL #InfoSec
