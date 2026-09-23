---
title: Advancing Private AI Compute with secure, server-side memory
source: Google DeepMind
url: https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/
model: claude-code/sonnet
generated_at: '2026-09-23T20:30:34.043925'
score: 118
---

📌 【Google DeepMind】雲端也能像裝置一樣私密的 AI 記憶架構

TL;DR：Private AI Compute 新增伺服器端持久記憶層，用裝置端加密金鑰確保雲端運算不犧牲隱私。

你的 AI 助理要記得你上週在智慧眼鏡上看過的組裝說明，還要在你切換到筆電時接得上話，這意味著它必須把你的資訊留在雲端。但「留在雲端」向來是隱私的天敵。Google DeepMind 這次要解決的，正是這個長期存在的兩難。

🤔 背景：裝置端隱私標準，遇上雲端規模的 AI

本地裝置端運算一直是隱私保護的黃金標準，但前沿 AI 模型所需的運算能力，往往超出單一裝置所能提供。Google 先前推出的 Private AI Compute 平臺，允許使用者在硬體隔離的雲端 enclave 中處理複雜任務，但這項技術以及業界類似方案，此前都是「無狀態」的，也就是任務一結束就清除所有上下文。像是讓 AI 儲存一份個人事實與偏好清單這類替代方案，並不足以支撐人們期待的那種豐富、持續性的個人助理體驗。

🧩 架構設計：金鑰留在裝置上，資料在雲端「密封」

這次更新為 Private AI Compute 加入一個新的持久記憶層，運作方式像是雲端裡的一個安全數位保險箱。協助使用者所需的資訊被封存在專屬的加密儲存空間中，而解鎖這些資訊所需的加密金鑰只保存在使用者自己的裝置上，確保任何人（包括 Google 本身）都無法存取這些資料。

具體流程可拆成幾個步驟：當 AI 模型需要存取資訊以協助使用者時，裝置與雲端之間會先建立一條經過驗證的端對端加密通道；這條通道連接到雲端中一個受保護的隔離環境，也就是所謂的「安全隔離區」（secure enclave）；該隔離區會在隔離記憶體中暫時解密資料以處理請求；處理完成後，任何新產生的上下文會被儲存並立即重新加密。整套架構結合了硬體強制的安全隔離區、加密通道，以及由裝置端金鑰保護的每使用者專屬資料庫，確保資料完全私密且由使用者自己掌控。

💡 深入分析：從無狀態運算到跨裝置記憶的意義

這項技術要解決的核心問題，是如何讓雲端規模的 AI 安全地跨時間、跨裝置保留上下文，同時維持與裝置端運算相當的隱私標準。官方舉的例子是：使用者可以在筆電上叫出先前透過智慧眼鏡看過的組裝說明，或是在手機與網頁之間接續複雜的對話。這代表持久記憶不再只是「儲存一串個人偏好」，而是能讓 AI 真正記得跨場景、跨裝置的使用脈絡。

⚠️ 限制與信任建立方式

團隊也強調，光有架構設計還不夠，使用者的信任同樣重要。因此 Google 同步發布了更新後的技術白皮書，以及一份防竄改的伺服器軟體公開紀錄，執行 Private AI Compute 的裝置可以在傳送任何個人資料之前，驗證伺服器軟體的真實性與未被竄改。這項技術也經過一家主要資安公司的獨立稽核。這項研究由 Google DeepMind 與 Platforms & Devices、Core、Cloud 等團隊共同開發，並由 Four Flynn、Jay Yagnik 與 David Kleidermacher 擔任高層贊助人。

🎯 實務啟示

對於正在設計 AI 產品記憶功能的工程團隊來說，這個架構提供了具體參考：與其在雲端存一份「使用者偏好清單」當作記憶的替代方案，不如思考如何用裝置端金鑰搭配硬體隔離環境，讓記憶資料即使離開裝置也維持同等的私密性。這也提醒我們，跨裝置持久記憶與端到端加密並非互斥，只要金鑰管理與硬體隔離的架構設計得當，兩者可以同時達成。

🔗 來源
- 標題：Advancing Private AI Compute with secure, server-side memory
- 作者／機構：Google Private AI Compute Team, Google DeepMind
- 連結：https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/

#PrivacyEngineering #GoogleDeepMind #PrivateAICompute #ConfidentialComputing #DataPrivacy #SecureEnclave #Encryption #AIAssistant #CloudSecurity #TrustAndSafety
