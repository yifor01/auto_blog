---
title: I'm making LLMs work on small and old devices
source: Hacker News
url: https://github.com/hyperionaidev/smolmaxxing/
model: claude-code/sonnet
generated_at: '2026-11-12T23:09:30.025158'
score: 84
---

📌 把LLM塞進電視盒和10年前的iPad裡

TL;DR：smolmaxxing靠自製kernel與記憶體技巧，讓老裝置也能跑16B模型。

家裡閒置的電視盒、抽屜裡那臺舊平板，CPU、記憶體和快閃儲存其實大半天都閒著沒事做。開源專案smolmaxxing做的事情，就是想辦法讓這些老裝置也能跑得動參數規模遠超它們記憶體容量的語言模型。

🤔 舊硬體也能跑大模型？

smolmaxxing的目標很直接：在你手邊最小、最舊的硬體上，跑你能跑得動的最大語言模型。目前專案已經在兩款裝置上驗證：Xiaomi TV Box S（第三代）與2013年的iPad Air。

| 項目 | Xiaomi TV Box S (3rd Gen) | iPad Air (2013) |
|---|---|---|
| 晶片 | Amlogic S7D，4核Cortex-A55 | Apple A7，2核 |
| 記憶體 | 1.9GB（約1GB可用） | 1GB（約700MB可用） |
| 作業系統 | Android 14，未root | iOS 12.5.7，已jailbreak |
| 日常模型 | Qwen3.5-2B，7.7 tok/s | Bonsai-1.7B（1-bit），24-26 tok/s |
| 最大可跑模型 | Ling-mini-2.0（16B），5.1 tok/s | Ling-mini-2.0（16B），2.6-4.5 tok/s |

兩款裝置都能在約1GB記憶體下，跑起8B與16B規模的mixture-of-experts（混合專家）模型。

🧩 核心技術：客製化kernel、精簡記憶體、從快閃儲存分頁載入專家

README指出，smolmaxxing整個專案是以llama.cpp為基礎打的patch，核心手法有三個方向：

- 為晶片量身打造的kernel：包含一個1-bit lookup-table kernel，以及為Cortex-A55重新打包的2-bit與ternary格式；針對沒有dot-product指令的Apple A7，另外做了對應版本。
- 降低每個模型佔用的記憶體：大部分小模型的詞表（vocabulary）裡，很多輸出列幾乎用不到，因此直接捨棄這些列。在電視盒上，還有一個「headless」模式，跑模型時會關掉launcher和Google服務，把記憶體讓出來。
- 讓MoE模型的專家從快閃儲存分頁載入：mixture-of-experts模型每個token只會用到少數專家，smolmaxxing把常用的專家留在記憶體，其餘的則在需要時才從快閃儲存讀取，同時預先讀取下一層會用到的部分。作者表示，這就是8B、16B模型能在1GB RAM上跑起來的關鍵。

對於比記憶體還大的密集（dense）模型，專案也做了對應的streaming機制，讀取速度可以貼著快閃儲存本身的頻寬上限。

🧩 怎麼用

依README說明，最快的上手方式是直接從Hugging Face抓現成的模型檔案，但這些檔案需要搭配專案patch過的llama.cpp才能載入，原生llama.cpp無法讀取。電視盒或其他ARMv8.2 Android裝置可以照docs/tv-box-setup.md的步驟設定；已jailbreak的iOS 12 iPad則對應ipad-air/README.md。專案也提供了模型重建方式與對應的checksum清單。

⚠️ 目前仍在早期階段

專案目前只驗證了兩款裝置，作者表示手機、單板電腦和路由器等更多裝置的支援還在路上。README也附上一份完整的實驗記錄（EXPERIMENT.md），記載了160次實驗，包含失敗的嘗試，顯示這套技巧仍在持續打磨中。

🎯 實務啟示

對於想在邊緣裝置或IoT硬體上跑LLM的工程師，smolmaxxing提供了一套具體可驗證的做法：kernel只需要基本的NEON指令集，flash streaming則能在任何記憶體小於模型大小的Linux/Android裝置上使用，不侷限在這兩款已測試的裝置。如果你手上也有類似規格的閒置硬體，這個專案的patch與實測數據，是目前少見、連1GB RAM裝置都附完整benchmark的參考案例。

🔗 來源
- 標題：I'm making LLMs work on small and old devices
- 作者／機構：mrashad74（Hacker News）／smolmaxxing專案（hyperionaidev）
- 連結：https://github.com/hyperionaidev/smolmaxxing/

#LLM #EdgeAI #llamacpp #OnDeviceAI #Quantization #MixtureOfExperts #OpenSource #EmbeddedAI #AIOptimization #LocalLLM
