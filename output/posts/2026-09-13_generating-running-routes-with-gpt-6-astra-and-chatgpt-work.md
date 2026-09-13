---
title: Generating running routes with GPT-6 Astra and ChatGPT Work
source: Simon Willison
url: https://simonwillison.net/2026/Sep/12/astra-running-routes/
model: claude-code/sonnet
generated_at: '2026-09-13T19:41:28.756800'
score: 80
---

📌 讓 ChatGPT 規劃跑步路線,結果連它自己都說不清「怎麼算出來的」

TL;DR：Simon Willison 用 GPT-6 Astra 生成跑步路線成功了,但事後想看程式碼卻因對話被壓縮而消失。

想像你請一位工程師幫你寫了一段程式,結果一轉身,對方連自己剛剛寫了什麼都拿不出來——這正是 Simon Willison 這次實測 ChatGPT Work 搭配 GPT-6 Astra（Max）時遇到的狀況。

🤔 **一個看似完美的任務:規劃跑步路線**

Willison 給 ChatGPT Work 的指令很直白:告訴它自己的地址,請它用 OSM（OpenStreetMap）資料規劃出從家裡出發、繞一圈回來的 5K 與 10K 跑步路線。系統運作了 27 分鐘,最終產出正是他要的東西:一個嵌入式視覺化地圖,加上可下載的 GPX 與 GeoJSON 檔案。

🧩 **拆解 Agent 怎麼做到的**

當 Willison 追問它是怎麼生成路線的,ChatGPT 回覆:先用 Nominatim 定位地址,再用 Overpass 下載當地 OpenStreetMap 的道路與步道資料,最後在本地計算出迴圈路線。地圖顯示的部分則是透過所謂的「visualize skill」,產生了一個名為 `/workspace/el-granada-5k-share.html` 的檔案直接嵌入 ChatGPT 介面,其中的 HTML 使用 D3.js（從一個白名單允許的 CDN 載入)來繪製路線與地圖幾何。

⚠️ **壓縮機制吃掉了程式碼,也吃掉了透明度**

問題出在 Willison 事後想索取實際執行過的 Python 程式碼時,ChatGPT 已經無法提供——原因似乎是該對話串已經被「壓縮」（compacted）過。他直言這種缺乏透明度是一種「反功能」(anti-feature):任何使用對話壓縮機制的 LLM 系統,都應該保留壓縮前的原始文字,並讓 agent 能透過工具呼叫重新取用這些內容,否則使用者將永遠無法驗證或重現 agent 實際執行過的邏輯。

🎯 **實務啟示**

如果你正在打造或評估具備長任務執行能力的 agent 系統,這是一個值得放進設計清單的教訓:壓縮上下文是控制成本與 token 用量的必要手段,但壓縮後的資訊消失,等同於讓系統的可稽核性、可重現性直接歸零。無論是偵錯、合規審查,或單純想理解 agent 的決策過程,都需要一條能回溯到「壓縮前原始執行紀錄」的路徑,而不是把黑盒子做得更黑。

🔗 **來源**
- 標題：Generating running routes with GPT-6 Astra and ChatGPT Work
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Sep/12/astra-running-routes/

#ChatGPT #GPT6Astra #AIAgent #LLMTransparency #OpenStreetMap #AgentTooling #PromptEngineering #AITransparency #ContextCompaction #GenerativeAI
