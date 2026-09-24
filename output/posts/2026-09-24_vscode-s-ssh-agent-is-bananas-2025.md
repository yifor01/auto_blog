---
title: VSCode's SSH Agent Is Bananas (2025)
source: Hacker News
url: https://fly.io/blog/vscode-ssh-wtf/
model: claude-code/sonnet
generated_at: '2026-09-24T20:47:03.858269'
score: 83
---

📌 VSCode 的 SSH 遠端外掛，行為像不像後門程式？

TL;DR：Fly.io 工程師實測發現，VSCode 遠端 SSH 連線會在對端偷偷灌一整套 agent，具備任意編輯檔案與開 shell 的能力。

當你在遠端伺服器上打開 VSCode 做遠端編輯，你以為只是連上一個終端機視窗，實際上發生的事情遠比這複雜：一段 Bash 指令碼會在對端下載一個包含完整 Node.js 執行環境的 agent 程式，並透過 WebSocket 連回你本機的 VSCode 前端。Fly.io 的 Thomas Ptacek 在研究如何把 VSCode 遠端編輯串接進 Fly Machine 時，意外挖出了這套機制的細節。

🤔 **為什麼要在乎 VSCode 怎麼連遠端**

文章的起點是 AI 輔助開發的趨勢：現在人人都在用 VSCode 的各種 fork 搭配 LLM 生成程式碼，而讓效果最好的用法，是把 LLM 與一個能執行程式碼的環境串成閉環（agent 設定）——LLM 寫程式碼、agent 執行、錯誤回饋給 LLM、如此反覆迭代，這是對抗幻覺（hallucination）相當有效的手段。但問題是，你不會希望這個反覆試錯的過程發生在自己的開發筆電上，因為 LLM 一樣會很樂意去「迭代」你的系統設定，而不只是你手上的 Git 專案。理想做法是把這個閉環丟到一個乾淨、用完即丟的雲端執行環境裡，而這正是作者想把 VSCode 遠端編輯接進 Fly Machine 的原因。

🧩 **對照 Emacs Tramp：VSCode 選擇的是「整套進駐」**

作者拿 Emacs 世界的遠端編輯始祖 Tramp 做對照：Tramp 是「就地取材」（live off the land），只要對端有能跑 Bourne shell 指令的互動環境（通常是 SSH session）就能運作。VSCode 也有類似遠端編輯功能，但做法完全不同：它會在對端執行一段 Bash 指令碼，下載並安裝一個 agent，其中包含一份 Node.js 的二進位安裝檔。這個 agent 透過連接埠轉發的 SSH 通道運行，並與本機 VSCode 前端建立一條 WebSocket 連線。

💡 **這條連線能做的事，作者的形容很直接**

文章指出，這條 WebSocket 連線底層協定可以：在檔案系統中任意遊走、編輯任意檔案、啟動自己的 shell PTY 處理程序，以及讓自己持續存在（persist）。作者提到，在資安圈裡，這種行為模式的工具有一個對應的名稱，但他選擇不直接說出口，只暗示那個詞帶有「鼠類」的意味——言下之意是這套機制的行為特徵與 rootkit 類工具相當接近。他表示自己會對讓人用 VSCode 遠端編輯連上開發用伺服器感到不安，若這發生在正式環境的事故處理過程中，更會是災難級的情況。

⚠️ **最後其實繞過了這個問題**

值得注意的是，作者最後說明，Fly.io 要讓自訂連線在 VSCode 裡對接 Fly Machine，其實完全不需要碰到上述這套機制，所以這些細節在深層意義上「不影響」他們原本要做的事——純粹是研究過程中順帶弄清楚、也想讓讀者一併知道的背景知識。

🎯 **實務啟示**

如果你的團隊會用 VSCode（或其 AI 編碼 fork）遠端連線到開發機、測試機，甚至正式環境伺服器，值得先弄清楚對端到底被裝了什麼、那個 agent 擁有多大的操作權限，再決定是否要在敏感主機上開放這種連線方式，尤其是在事故排除等高風險時刻。

🔗 **來源**
- 標題：VSCode's SSH Agent Is Bananas (2025)
- 作者／機構：Thomas Ptacek，Fly.io
- 連結：https://fly.io/blog/vscode-ssh-wtf/

#VSCode #RemoteSSH #DevSecOps #AICoding #AgenticAI #SoftwareSecurity #Flyio #DeveloperTools #LLMAgents #InfoSec
