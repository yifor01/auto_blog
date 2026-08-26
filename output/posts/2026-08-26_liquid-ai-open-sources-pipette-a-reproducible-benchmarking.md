---
title: 'Liquid AI Open-Sources Pipette: A Reproducible Benchmarking Suite That Measures
  On-Device Models, Quantization, Runtime and Hardware Together'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/25/liquid-ai-open-sources-pipette-a-reproducible-benchmarking-suite-that-measures-on-device-models-quantization-runtime-and-hardware-together/
model: claude-code/sonnet
generated_at: '2026-08-26T06:21:52.878140'
score: 107
---

📌 【Liquid AI】邊緣模型測不準？Pipette 把「機型＋量化＋執行環境」綁在一起測

TL;DR：Liquid AI 開源 Pipette，把模型、量化、runtime、硬體視為同一套「部署設定」來測效能，破解手機上跑模型的效能黑箱。

模型卡上寫的分數，通常是伺服器等級、全精度條件下測出來的。同一顆模型換一支手機跑，數字可能完全不是那回事——這正是 Liquid AI 這次要解決的問題。

🤔 問題核心：模型效能其實是「系統」的屬性

Liquid AI 與 Artificial Analysis 合作（作為獨立方驗證測試方法論），釋出開源邊緣裝置基準測試平臺 Pipette。它的核心主張很直白：裝置端行為是「已部署系統」的屬性，而不是模型本身單獨的屬性。Pipette 測量的最小單位不是模型，而是一組完整配置：模型 + 量化 + runtime + 裝置。

🧩 超過千種配置組合，涵蓋四大平臺

首發資料集涵蓋五項裝置端效能指標，橫跨超過 1,000 種「模型 × 量化 × runtime × 裝置 × 上下文長度」組合，包含 30 多個模型、macOS／iOS／Windows／Android 上的 llama.cpp build，以及 256 到 8,192 token 的多種上下文長度。初期驗證結果來自 MacBook Pro（M5 Max）、iPhone 17 Pro 與 Galaxy S26 Ultra，AMD Ryzen AI Max+ 395 與 Radeon 8060S 的結果則列為即將推出。

一個可被實測驗證的具體案例：兩個同樣是 350M 參數、同樣量化等級的模型，在同一支手機上、4,096 token 情境下，decode 吞吐量保留率分別為 78.4% 與 33.8%——同規格模型在裝置端的表現可以差到這麼多。

品質分數（IFBench、GPQA Diamond、MATH-500）則是另外追蹤，目前這些分數來自 llama.cpp 在 NVIDIA H100 80GB 參考系統上的評測結果，再依相同模型與量化配對到裝置端的效能結果——也就是說，手機吞吐量旁邊顯示的品質分數，並不是在手機上實測出來的，這點 Liquid AI 有明確揭露。

📊 測試方法：固定流程、失敗就不發布

效能測試遵循公開的方法論：固定 token 形狀、貪婪解碼（greedy decoding）、捨棄暖機（warm-up）結果、五次重複測量，並設有就緒門檻（readiness gating）。每次計時前都會檢查裝置的散熱與負載狀態，未通過檢查的跑分不會被發布。評測（quality）則用另一套協定，採確定性、model-blind 評分，且 pipette-scores 完全看不到生成過程的來源資訊。每筆提交都會記錄基準版本、token 形狀、模型檔案、量化方式、runtime 版本與設定、裝置硬體與作業系統。

Pipette 整套以 Apache 2.0 授權釋出，包含 pipette-mgmt、pipette-clients、pipette-scores 三個元件、公開結果資料集、託管式儀表板，以及原生 iOS／Android 測試 App，沒有候補名單門檻；不過社群提交結果的公開發布功能目前仍在 beta 階段。

🎯 實務啟示

如果你的產品要在手機或邊緣裝置上部署 LLM，光看伺服器端跑分基本不具參考價值。Pipette 提供的是「換一臺裝置、換一種量化，吞吐量到底會掉多少」的可重現數據，選型時可以直接拿目標裝置＋目標量化組合去查表，而不是憑經驗猜測。

🔗 來源
- 標題：Liquid AI Open-Sources Pipette: A Reproducible Benchmarking Suite That Measures On-Device Models, Quantization, Runtime and Hardware Together
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/25/liquid-ai-open-sources-pipette-a-reproducible-benchmarking-suite-that-measures-on-device-models-quantization-runtime-and-hardware-together/

#LiquidAI #Pipette #OnDeviceAI #EdgeComputing #ModelQuantization #Benchmarking #LLM #OpenSource #MobileAI #ArtificialAnalysis
