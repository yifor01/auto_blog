---
title: Building and shipping Mac and iOS apps without opening Xcode
source: Hacker News
url: https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/
score: 88
model: tencent/hy3:free
generated_at: '2026-07-14T08:06:52.559742'
---

這篇內容屬於「產業新聞／部落格報導」，重點在於分享一種開發流程的實作方法。

📌 【開發者實踐】不用開啟 Xcode，也能開發與釋出 Mac 與 iOS App

TL;DR：只要安裝 Xcode，即可透過指令行工具實現完全 Headless 的 App 建置與釋出流程。

最近許多關於 Apple 的播客都在討論 Xcode 的使用體驗，認為它過於晦澀難懂。雖然這點值得討論，但作者提出了一個更直接的思考方式：既然 Xcode 這麼難用，為什麼我們還需要開啟它？透過一些前置作業，你可以實現完全不需要開啟 Xcode GUI 的「Vibe-coding」開發流程。

🧩 **核心理念：將 Xcode 工具化而非 GUI 化**

開發者並非不需要 Xcode，而是不需要 Xcode 的圖形介面。作者指出，許多關鍵的建置與釋出工具都封裝在 Xcode 內，並能直接從 Shell（終端機）中執行：

- `xcodebuild`：用於執行建置與封裝。
- `notarytool`：用於處理 Apple 的公證（Notarization）流程。
- `stapler`：用於將公證資訊附加至 App。
- `devicectl`：用於裝置相關的指令操作。

⚠️ **僅需一次性的 GUI 設定**

雖然建置過程可以完全 Headless（無介面），但仍有少數步驟必須透過 GUI 或互動式終端機完成：
- 登入 Apple ID。
- 建立 Developer ID 憑證。
- 儲存公證密碼（Notarization password）。

一旦這些前置作業完成，之後的建置與部署就能完全透過指令行完成。

📊 **自動化釋出流程：從 Archive 到安裝**

針對 Mac App，作者建議撰寫一個指令碼（例如 `scripts/release.sh`）來處理整條自動化鏈條：

`Archive` → `Developer ID Sign` → `Notarize` → `Staple` → `Install to /Applications`

在安全性方面，簽署流程是基於「憑證與鑰匙圈 (Certificate-and-keychain)」的機制。簽署金鑰會儲存在登入鑰匙圈（login keychain）中，`xcodebuild` 會自動找到它，因此程式碼庫（Repo）中不需要存放任何敏感資訊。

🎯 **實務啟示**

對於追求自動化（CI/CD）或偏好 CLI 工具的工程師來說，這提供了一個將 Apple 開發流程與 LLM 輔助開發（如 Claude Code）結合的可能性。你可以直接將這套邏輯提供給 AI 助手，讓它幫你處理那些你不想要的複雜設定。

🔗 **來源**
- 標題：Building and shipping Mac and iOS apps without opening Xcode
- 作者／機構：speckx
- 連結：https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/

#Xcode #iOSDevelopment #macOS #Automation #Headless #CI/CD #Swift #AppleDeveloper #DevOps #ShellScripting
