---
title: "conorluddy/ios-simulator-skill"
source: GitHub Trending
url: https://github.com/conorluddy/ios-simulator-skill
score: 83
model: tencent/hy3-preview:free
generated_at: 2026-05-03T19:40:18.253893
---

📌 Claude Code iOS 開發自動化技能包

還在手動敲 xcodebuild 指令編譯 iOS 專案、切換模擬器跑測試？
這個近期登上 GitHub Trending 的開源技能包，讓 Claude Code 直接接手整個流程。
22 支腳本同時支援人類開發者與 AI Agent 使用。

🤔 **AI Agent 開始切入原生 App 開發場景**
近期AI Agent 進入原生 App 開發領域的趨勢明顯，Claude Code 作為主流 AI 編程工具之一，此前較少有針對 iOS 開發全場景的專用自動化技能包。本次介紹的 ios-simulator-skill 專案由開發者 conorluddy 釋出，是針對 Claude Code 打造的生產級工具，覆蓋 iOS App 構建、測試、模擬器操作全流程，對接 AI Agent 與原生開發工具鏈的需求。

🧪 **22 支腳本覆蓋構建與模擬器雙核心場景**
該技能包共包含 22 支腳本，同時優化給人類開發者與 AI Agent 使用，核心覆蓋兩大場景：
1. Xcode 構建自動化：透過 build_and_test.py 包裝 xcodebuild 工具，支援編譯、測試與結果解析，採用漸進式錯誤披露設計，輸出 token 效率高，構建完成後僅返回單行摘要與 xcresult ID。
2. 模擬器交互自動化：透過 xcrun simctl 與 idb 工具，支援語義 UI 導航、無障礙測試、設備生命周期管理。
若僅需 Xcode 構建工具、不需要模擬器相關腳本，可改用同作者的 xclaude-plugin 插件版本。
