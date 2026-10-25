---
title: 🗞️DeepSeek’s $15B Round, Moonshot launches K3.1 Pro, and China’s AI Jobs Policy
source: Recode China AI
url: https://www.recodechinaai.com/p/deepseeks-15b-round-its-38gpu-hour
model: claude-code/sonnet
generated_at: '2026-10-25T19:51:32.368458'
score: 66
---

📌 DeepSeek 傳募資 150 億美元，Kimi K3.1 Pro 搶先卡位百萬 token

TL;DR：這週中國 AI 圈同時發生大額融資、模型發布與就業政策三條線，是觀察中國 AI 生態節奏的好樣本。

一週 306 篇報導，一次濃縮成三條主線：資金、模型、政策——這正是本期 Recode China AI 週報想呈現的畫面。

🤔 **一週 306 篇報導背後的三條主線**

這份週報由 China AI Index newsfeed 彙整、AI 代理起草、編輯 Tony Peng 事實核查後完稿，涵蓋 2026 年 10 月 16 日至 23 日期間、90 篇英文與 216 篇中文報導。

🧩 **融資、模型與政策三則大事**

- **DeepSeek 傳募資約 150 億美元**：據 Reuters／Bloomberg 報導，本輪募資規模約為人民幣 1000 億元，對應投前估值人民幣 5000 億元；騰訊與寧德時代（CATL）是最大投資方，美團、吉利、兆易創新（GigaDevice）等也參與，預計近期完成，條款仍可能調整。
- **中國國務院辦公廳發布 AI 就業政策指引**：涵蓋六大領域共 18 項任務，一邊推動 AI 創造新職業、協助中小企業維持並擴大用工，一邊評估 AI 導入帶來的就業風險，並建立就業市場監測預警機制，同時要求強化對彈性與零工工作者的勞動保障與社會保險（財聯社）。
- **Moonshot AI 發布 Kimi K3.1 Pro**：支援百萬 token 的 context window，並提供速度快 2 至 3 倍的 Highspeed 版本，官方宣稱目標場景包括寫程式、建立可編輯的 3D 資產與財務研究。在 Moonshot 自報的 Terminal-Bench 4.0 成績中，K3.1 Pro 拿下 65.7%，領先 GPT-6 Astra 的 58.2%，僅略低於 Claude Opus 5.5 的 66.4%；在 Artificial Analysis Intelligence Index 上獲得 55 分，排名第四。團隊也在中後訓練階段主動移除與網路攻擊相關的資料，以抑制模型的 hacking 能力。兩個版本已可透過 Kimi 產品與 API 使用，完整權重預計 11 月 4 日前釋出。

📊 **其他值得留意的技術與供應鏈動態**

- 美國國土安全部發布命令，禁止 DeepSeek 相關產品進入聯邦民用機關採購，並要求從既有系統（包含部分第三方實作）移除；同時中國的 AI 出口管制草案仍在徵詢意見階段（至 11 月 15 日），其中為開源釋出留有便利條款，據官方媒體報導，DeepSeek 與 MiniMax 已完成開源與海外授權的登記。
- DeepSeek 開源自研推理框架 DeepInfer，支援 Nvidia SM100 Blackwell 與華為 Ascend 950 兩種硬體跑 V4.1-Flash，官方宣稱單一叢集每日可處理 155 兆 token，即便在離峰定價下，每 GPU 小時仍能創造 38 美元營收。
- MiniMax 發布 M3.1 Flash，API 定價為每百萬輸入 token 0.15 美元、輸出 token 0.60 美元；VentureBeat 報導其在商業任務上表現強勁，但幻覺率偏高。
- 螞蟻集團開源醫療向 MoE 模型 Ling-3.0-flash-Sante，總參數 1240 億、每 token 啟用參數 51 億，另發布五款涵蓋語音合成、音訊理解與語音辨識的 Ming-3.0 模型。
- 字節跳動、阿里巴巴、騰訊合計訂購逾 300 萬張 Nvidia RTX PRO 5500 顯卡，標價總額超過 350 億美元；Reuters 指出這些是出口合規的工作站級 GPU（主要用於推理），且 Nvidia 無法保證如期交付，因需求已超出其規劃產能。

💡 **算力瓶頸仍在，便宜智慧背後有硬體代價**

即便模型價格戰持續（如 MiniMax 的低定價），算力端的瓶頸依然明顯：Cambricon 第三季獲利年增 148%、約 2.1 億美元，但 Bloomberg 指出其銷售不及預期且產能受限；CXMT 雖然因記憶體價格上漲而轉虧為盈，股價仍下跌逾 6%。這些訊號說明「便宜智慧」的敘事背後，供應鏈與產能限制仍是現實的制約。

🎯 **實務啟示**

對關注中國模型生態的工程師，DeepSeek 開源的 DeepInfer 提供了另一套高吞吐推理框架的設計參考；Kimi K3.1 Pro 權重 11 月 4 日釋出後值得實測其百萬 token context 與實際成本表現；而 MiniMax M3.1 Flash 的低定價搭配偏高幻覺率，也提醒在選型時不能只看單價，仍要評估任務對準確度的容忍度。

🔗 **來源**
- 標題：DeepSeek's $15B Round, Moonshot launches K3.1 Pro, and China's AI Jobs Policy
- 作者／機構：Tony Peng, Recode China AI
- 連結：https://www.recodechinaai.com/p/deepseeks-15b-round-its-38gpu-hour

#DeepSeek #KimiAI #MoonshotAI #ChinaAI #LLM #OpenWeights #AIInfrastructure #Nvidia #InferenceEngine #AIPolicy
