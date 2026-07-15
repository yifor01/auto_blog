---
title: 'Cursor 0day: When Full Disclosure Becomes the Only Protection Left'
source: Hacker News
url: https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left
score: 88
model: tencent/hy3:free
generated_at: '2026-07-15T08:27:21.276706'
---

📌 Cursor 0day：開專案自動執行惡意 git

TL;DR：Cursor 在 Windows 開專案時自動執行根目錄惡意 git.exe，導致任意程式碼執行，至今未修。

🎣 一款擁有 700 萬活躍使用者的 AI 編輯器，居然在開發者開啟資料夾時，默默執行了攻擊者預埋的程式？這不是概念驗證，而是發生在日常操作中的真實漏洞。

🤔 700 萬使用者的 Cursor，安全實踐卻令人意外
報導指出，Cursor 是最廣泛採用的 AI 輔助開發環境之一，擁有 700 萬以上活躍使用者、100 萬以上每日活躍、100 萬以上付費使用者，並被 5 萬多家公司使用，傳聞市值達 600 億美元。如此規模下，理應具備基本安全實踐，但該漏洞顯示並非如此。

🧩 開專案自動執行根目錄惡意 git.exe
在 Windows 上，開發者用 Cursor 開啟一個儲存庫時，IDE 會嘗試在各種位置尋找 git 二進位檔，包含目前工作區。若專案根目錄存在一個惡意的 git.exe，Cursor 會在載入專案後自動執行它。整個過程沒有點選、沒有提示、沒有批准對話方塊或警告，且會以某個頻率重複觸發。結果就是任意程式碼執行（arbitrary code execution）。

📊 超過六個月、197+ 版本仍未修補
Mindgard 於 2025 年 12 月 15 日首次識別此漏洞，當天即通報並後續多次回報。然而超過六個月、累積 197 個以上新版本後，最新測試版本仍存在該問題。在 Hacker News 上，這則討論已獲得 328 點讚與 160 則評論，顯示社群高度關注。

⚠️ 無需提示注入，開箱即用的攻擊鏈
該漏洞並非理論風險，也不依賴複雜的利用鏈、prompt injection、模型操縱或 jailbreak。只要專案根目錄放了惡意檔案，開發者單純開啟資料夾就會中招。

🎯 別隨便用 Cursor 開啟來路不明專案
對工程師的實際行動建議：避免直接以 Cursor 開啟從網路下載或來歷不明的程式庫；可先用手動檢查或隔離環境確認無惡意 git.exe。在官方修補前，全披露（full disclosure）可能是使用者唯一能提早防範的途徑。

🔗 來源
- 標題：Cursor 0day: When Full Disclosure Becomes the Only Protection Left
- 作者／機構：Synthetic7346
- 連結：https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left

#Cursor #ZeroDay #Vulnerability #CodeExecution #Security #AIIDE #Windows #Git #DevTools #Disclosure
