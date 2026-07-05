---
title: Command and Conquer Generals natively ported to macOS, iPhone, iPad using Fable
source: Hacker News
url: https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main
score: 78
model: google/gemma-4-31b-it:free
generated_at: '2026-07-05T19:35:35.069749'
---

📌 將 2003 年的《將軍》原生移植到 Apple Silicon 與 iOS/iPadOS

TL;DR：透過 Fable 專案將 C&C Generals 引擎編譯至 ARM64，實現原生執行並將 DirectX 8 轉譯為 Vulkan。

對於許多 RTS 玩家來說，能在現代裝置上執行 20 年前的經典遊戲通常得依賴效能損耗巨大的模擬器。但這次的實作直接挑戰了最困難的路徑：將 2003 年的遊戲引擎原生編譯到 Apple Silicon 平臺上。

🧩 **從 DirectX 8 到 Vulkan 的渲染路徑**

這個專案的核心在於讓舊時代的圖形 API 在現代 Apple 裝置上運作。其渲染流程並非透過模擬，而是採取了以下轉譯路徑：
DirectX 8 → DXVK → Vulkan

這種方式讓遊戲能以原生 ARM64 指令集執行，而非透過模擬層，因此能直接執行在 macOS、iPhone 以及 iPad 上。

📱 **針對觸控裝置重新設計的 RTS 操作**

為了讓即時戰略（RTS）遊戲在 iPhone 和 iPad 上具有可玩性，專案內建了專為觸控設計的控制方案：
- 點選選擇（Tap-select）
- 拖曳選框（Drag-box）
- 長按取消選擇（Long-press deselect）
- 雙指捲動（Two-finger scroll）
- 捏合縮放（Pinch zoom）

目前移植的版本已支援原有的戰役（Campaign）、遭遇戰（Skirmish）以及將軍挑戰（Generals Challenge）模式。

🎯 **實務啟示**

這個專案展示了利用 DXVK 型別的轉譯層，將舊版 DirectX 遊戲移植到非 Windows 平臺的可能性。對於工程師而言，這證明瞭只要解決指令集編譯（ARM64）與圖形 API 轉譯（DX8 → Vulkan）這兩個核心問題，即使是 20 年前的舊引擎也能在現代行動裝置上原生執行。

🔗 **來源**
- 標題：Command and Conquer Generals natively ported to macOS, iPhone, iPad using Fable
- 作者／機構：asronline
- 連結：https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main

#CommandAndConquer #AppleSilicon #iOS #iPadOS #DXVK #Vulkan #DirectX8 #GamePorting #ARM64 #OpenSource
