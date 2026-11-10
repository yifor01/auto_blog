---
title: Introducing Claude Fable 5.2 on AWS
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/introducing-claude-fable-5-2-on-aws/
model: claude-code/sonnet
generated_at: '2026-11-10T00:57:50.954912'
score: 91
---

📌 Claude Fable 5.2 上架 AWS Bedrock，資料留存規則你該先搞懂

TL;DR：Fable 5.2 上架 Bedrock，資料留存與拒答重試機制牽動合規與計費。

如果你的團隊打算把 Claude Fable 5.2 導入生產環境，光是「這個查詢被拒絕了該怎麼辦」這個問題，就可能牽動到計費與資料留存政策，這正是本次 AWS 公告裡最容易被忽略的細節。

🤔 兩款新模型，兩種用途
Fable 5.2 是 Anthropic 目前公開可用、最強的技術向模型，主打 coding 與科學領域的高難度任務。文中指出它能處理模糊、多步驟的工作，自行驗證輸出，甚至可以不間斷運行數小時到數天，期間會解讀提示、反覆迭代、捕捉自身錯誤並持續最佳化。

Mythos 5.2 則僅透過 Anthropic 的 verification programs 提供，面向 cyber security 與 life sciences 兩個高風險領域的進階工作。

文中提到，在 Anthropic 的 alignment 測試中，Mythos 5.2 比 Opus 5.5、Sonnet 5.5 與 Mythos 5.1 更少出現 hallucination，任務完成度更穩定，也更一致地揭露重要資訊、更誠實地自我回報問題；Anthropic 預期 Fable 5.2 會有類似表現。

🧩 查詢被拒後怎麼辦：重試機制與 fallback credit
若 cyber security 查詢被拒絕，可以改用 Opus 4.8 重試；若 biology 查詢被拒，則改用 Opus 5 重試。但在 Amazon Bedrock 上，這個重試是「你的程式碼該做的事」，而不是系統自動切換模型。如果被拒絕的請求原本命中了 prompt cache，拒答回應會附帶一個 fallback credit token；把這個 token 帶入重試請求，就會以 cache read 的價格計費，不必為同一份快取內容重複支付寫入費用。

🧩 資料留存：從 30 天保留到 ZDR
Anthropic 將 Claude Fable 5.2 列為 Covered Model，預設使用時須保留資料最長 30 天並經過人工安全審查；在 Amazon Bedrock 上，這項審查由 AWS 信任邊界內的 Amazon 人員執行，使用前需先在帳戶或專案層級設定 aws_review 資料留存模式。

Anthropic 與 AWS 共同打造的 Enterprise Frontier Safeguards（EFS）現已可用，結合 zero data retention（ZDR）的隱私保障與最新的濫用偵測機制。文中提到未來還會推出讓資料留在客戶自有 bucket、由客戶自行掌控金鑰的版本，但目前尚未上線；在此之前，符合資格的客戶可在 2027 年 6 月 30 日前以 ZDR 方式使用 Fable 5.2。

🧩 升級既有程式碼：claude-api skill
對已經在 Bedrock 上跑 Claude 模型的團隊，Claude Code 內建的 claude-api skill 可協助升級到 Fable 5.2。這是一個開源 skill，收錄了讓 Claude API 程式碼能順利運作的細節：哪種 agent 模式適合哪種任務、不同模型世代間哪些參數會變動、何時該套用 prompt caching，並會隨 Anthropic SDK 更新持續跟進。它也會偵測你的部署平臺（Amazon Bedrock、Claude Platform on AWS 或其他環境），自動調整 model ID 格式與功能設定，例如在 Bedrock 上使用 global.anthropic.claude-fable-5-2 這種結構化 model ID 格式。這個 skill 已開源於 anthropics/skills，也被整合進 CodeRabbit、JetBrains IDE（包括 Junie）、Resolve AI 與 Warp。

🎯 實務啟示
導入 Fable 5.2 前，先確認團隊的資料治理需求：是否需要 aws_review 流程、是否符合 EFS 的 ZDR 資格，以及拒答重試邏輯要不要在程式碼裡實作 fallback credit 的轉嫁，這些都會直接影響合規與成本。若已有既有 Claude 整合，直接用 claude-api skill 跑一次掃描，比手動排查 model ID 與參數差異更省力。

🔗 來源
- 標題：Introducing Claude Fable 5.2 on AWS
- 作者／機構：Dani Mitchell, AWS ML Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/introducing-claude-fable-5-2-on-aws/

#Anthropic #ClaudeFable #AmazonBedrock #AWS #LLM #EnterpriseAI #DataRetention #AISafety #CloudAI #GenerativeAI
