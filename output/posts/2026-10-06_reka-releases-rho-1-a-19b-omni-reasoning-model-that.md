---
title: 'Reka Releases Rho-1: A 19B Omni-Reasoning Model That Understands, Generates
  Video and Outputs Robot Actions in One'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/05/reka-releases-rho-1-a-19b-omni-reasoning-model-that-understands-generates-video-and-outputs-robot-actions-in-one/
model: claude-code/sonnet
generated_at: '2026-10-06T21:51:00.654128'
score: 109
---

📌 Reka Rho-1：一個模型統一生成、理解與機器人動作

TL;DR：Reka 發表 19B 研究預覽模型 Rho-1，單一網路同時做文字、影像、影片與機器人動作，省去模型間的 handoff。

多數多模態系統其實是一條 pipeline：中樞模型負責規劃，再把任務分派給影像、影片或偵測專用的子模型。每一次 handoff 都是一次延遲，每個專家模型也只看得到任務的片段。Reka 這次做的事情很直接：把這整條 pipeline 塞進同一個神經網路裡。

🤔 **為什麼要拆掉 pipeline**

Reka 認為當前 agentic 多模態系統的痛點在於「交接」：規劃模型決定要畫圖還是生影片後，必須呼叫外部的影像或偵測模型，每個專家只看得到窄化後的請求，也無法共用上下文。Reka 官方展示的一段未剪輯 session 中，Rho-1 在 5 個對話回合內，不呼叫任何工具、不切換模型，就畫出一座燈塔、框出邊界框、把它動畫化、再把影片編輯成暴風雪場景，最後還能解釋前後差異。

🧩 **雙專家流共享同一組 KV cache**

根據 Reka 的研究說明，每個 transformer block 內部都有兩條專家權重流：理解流（understanding stream）負責語言與視覺解析，生成流（generation stream）負責把 latent 去噪成影像與影片。兩條流共享 attention 與同一份 KV cache。當回覆需要輸出像素時，理解流會發出一個離散的 handoff token，生成流再根據累積的完整狀態進行渲染。訓練上結合了離散序列的 next-token prediction，以及連續輸出的 flow matching。

這個設計帶來幾個實際效果：邊界框是直接以座標 token 輸出，不需要額外的偵測器；影片第一幀會重用上下文中已有的影像表示，而不是重新編碼一份。

📊 **7 秒出第一支影片，distilled 版本只要 1 秒**

Reka 測得基礎模型以中位數 0.79 倍即時速度生成影片，約 6 秒就能開始串流觀看；官方量測首支影片的生成時間為 7.0 秒，對照他們列舉的多代理 pipeline 示意值 13.8 秒。一個 distilled 版本把去噪步數從 99 步壓到 8 步，官方表示品質損失極小，回傳一支 5.3 秒影片僅需約 1 秒。Reka 內部測試中，這個版本的影像生成速度追上了最快的專用影像模型，文字首 token 速度也是受測模型中最快的——但需注意這些都是廠商自行執行的測試，並非第三方基準。

新指令可以在影片持續串流時從理解流即時插入並更新狀態，Reka 示範了同一開頭分岔出「向左轉」與「向右轉」兩種延續。機器人應用上，動作與未來幀是從同一個 latent 狀態解碼而成，一段 LIBERO 模擬任務中 Rho-1 輸出了 7 個動作通道。為了解決遙操作資料稀缺的問題，Reka 將 Rho-1 與自家的 Inverse Dynamics Model 搭配使用，從原始影片反推出控制訊號。

⚠️ **廠商自測，仍待第三方驗證**

目前公開的速度與品質數據均來自 Reka 內部測試，尚未有獨立基準驗證,、架構細節也僅限於官方部落格披露的程度。

🎯 **對工程師的啟示**

如果你正在搭建多模型協作的 agentic pipeline，Rho-1 的設計提醒了一件事：統一上下文、共享 KV cache 能大幅減少 handoff 延遲。對機器人資料稀缺的場景，用 Inverse Dynamics Model 從影片反推控制訊號，也是值得參考的擴增資料思路。

🔗 **來源**
- 標題：Reka Releases Rho-1: A 19B Omni-Reasoning Model That Understands, Generates Video and Outputs Robot Actions in One
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/05/reka-releases-rho-1-a-19b-omni-reasoning-model-that-understands-generates-video-and-outputs-robot-actions-in-one/

#MultimodalAI #RoboticsAI #Rho1 #RekaAI #VideoGeneration #FlowMatching #AgenticAI #Transformers #OmniModel #AIResearch
