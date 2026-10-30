---
title: We ran AI agent swarms in Minecraft and Mindustry
source: Hacker News
url: https://labs.ycombinator.com/projects/games/index.html
model: claude-code/sonnet
generated_at: '2026-10-30T21:36:01.037617'
score: 109
---

📌 YC Labs 實驗:50 個 AI agent 如何在 Minecraft 裡「建國」

TL;DR:YC Labs 讓 50 個 LLM agent 在 Minecraft 自組社會,首夜就死了 22 次。

如果把 50 個會寫程式、會傳訊息的 AI agent 丟進一個資源有限的生存遊戲裡,要求牠們「建立一個繁榮的文明」,會發生什麼事?答案是:牠們先把附近的樹砍到一棵不剩,然後組了一個政府。

🤔 **多智能體對齊的老問題,換了個遊樂場**

理解多智能體動態是 AI alignment 裡最棘手的課題之一。朝共同目標前進的 agent 群體會湧現角色分工、層級結構與協作模式,素材提到這類行為既可能帶來強大效益(如近期數千個 agent 組成的群體一口氣解開數百個開放數學問題),也可能帶來危險(素材提及的「近期 OpenAI-Hugging Face 事件」)。研究既需要形式化模型描述可能行為的範圍,也需要實證觀察實際會出現什麼。YC Labs 與專門為前沿實驗室打造多智能體環境的 Olam Labs 合作,在 Minecraft 與 Mindustry 兩款遊戲裡做了一系列實驗,本文聚焦 Minecraft 的部分。

🧩 **自建的開源 harness,接在 Mineflayer 上**

Minecraft 的開放世界天然適合研究群體行為:環境危機、生存目標(覓食、建屋、探索資源)一應俱全,也有長久的 AI 測試場歷史,從 OpenAI 的 video pretraining 到 Google DeepMind 擊敗 Ender Dragon 的 agent。由於市面上沒有現成的「長時間在線遊玩」harness,團隊自己打造了一套並已開源(github.com/yc-software/minecraft-agent-harness)。agent 需要觀察世界、推理、記憶、行動、傳訊息並寫/執行腳本,核心 agentic loop 跑在 Pi 上,世界互動則透過 Mineflayer 的腳本工具,整體概念參考了既有專案 Mindcraft,也具備類似 Hermes、OpenClaw 等前沿 agent harness 的特性。

📊 **5,900 封訊息,34 次死亡,還有一份居民公約**

代號 Civ50 的實驗讓 50 個 GPT-6.1 Sol agent 在一個生存模式的 Minecraft 世界跑了 3 小時,目標就一句話:「建立一個繁榮的文明」。牠們擁有 agent 目錄、共用沙盒與私訊能力,整場跑下來發送了約 5,900 則訊息。

剛開始活動非常密集,agent 們四散探索地圖,並異常專注於砍樹,開局 90 秒內就把 spawn 點周邊能摸到的樹全部砍光。隨著 agent 目錄順序排序,第一位的 Ada 自然成為領袖,其他 agent 會向她請求批准,她也在共用沙盒寫下整個聚落的計畫文件(plans/settlement.md),裡面詳細記錄了儲物箱座標、作物位置、夜間避難所、各成員任務分配,甚至標註了「未成熟的小麥不要收割」。

然而第一夜就是一場浩劫:全程 34 次死亡裡,22 次集中在第一夜。Rafe 挖煤時被殭屍追殺致死;Vera 一邊用火把照亮採石場一邊擊殺了殭屍和骷髏,把骷髏掉落的骨頭製成骨粉送往農場,結果到了農場卻遭遇「蜘蛛/骷髏/苦力怕齊聚」,很快被蜘蛛殺死。由於死亡在這個環境裡除了裝備掉落沒有其他懲罰,死亡事件卻讓 agent 群體整體變得愈來愈保守,許多原本野心勃勃的任務被放棄。到了第三夜後,Ada 直接下令「停止非必要的大規模挖掘/建造與遠徵偵察,窩在有照明的封閉避難所裡,等待被指派的短期生產任務」。

💡 **從「建文明」到「分食物」的治理漂移**

50 張嘴要吃飯,讓這場實驗的重心迅速從「建立文明」滑向「活下去」。agent 們自發形成一套配給制度,由 Ines 負責統籌,她透過共用機器上的 food-queue.md 記錄誰申請了什麼、誰核准了什麼、哪個儲物箱裡還有多少存糧,並要求其他 agent 在「實際確認收件人拿到食物並吃下」之前都不算完成配送。整個過程像極了一個臨時政府在資源稀缺下運作:配給帳本、書面規則、許可證制度,以及被任命的「操作員」。

🎯 **實務啟示**

這場實驗顯示,給一群 agent 一個模糊但宏大的目標(「建立文明」),牠們不會直接朝目標前進,而是先被環境的生存壓力重新定義優先順序,進而自發湧現出分工、層級與治理結構。對正在設計多 agent 系統的工程師來說,這提示了一個現實:共享記憶(沙盒檔案)、溝通通道(DM)與明確的角色分工文件,往往比目標描述本身更決定群體的實際行為路徑。YC Labs 開源的 harness 也提供了一個現成的測試場,值得想研究 agent 群體湧現行為的人直接拿來實驗。

🔗 **來源**
- 標題:We ran AI agent swarms in Minecraft and Mindustry
- 作者/機構:sandslash(YC Labs,與 Olam Labs 合作)
- 連結:https://labs.ycombinator.com/projects/games/index.html

#AIAgents #MultiAgentSystems #Minecraft #AIAlignment #EmergentBehavior #LLMAgents #OpenSource #Mineflayer #AgentSwarm #AISafety
