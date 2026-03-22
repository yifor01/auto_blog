---
title: "ByteDance 開源了一個「檔案系統式」的 Agent 記憶體——OpenViking 到底在做什麼"
date: "2026-03-16"
paper_url: "https://github.com/volcengine/OpenViking"
paper_title: "OpenViking: An Open-Source Context Database for AI Agent Systems"
tags: [Agent, Memory, RAG, ByteDance, Open Source]
tldr: "把 Agent 的記憶從向量堆變成檔案系統"
---

現在的 AI Agent 有個很尷尬的問題：它們的記憶基本上就是一坨向量。你跟它聊了什麼、給它餵了什麼文件、它上次學到了什麼教訓——全部打成 embedding 扔進同一個向量資料庫，然後用最近鄰搜尋去撈。這在簡單場景下夠用，但一旦上下文類型變多——使用者偏好、對話歷史、工具使用記錄、外部知識文件——全部攪在一起搜尋，品質就開始崩壞。ByteDance 的火山引擎團隊開源了 OpenViking，核心想法出奇地直覺：把這坨向量變成一個有階層的檔案系統。

🗂️ 用檔案系統的方式管理 Agent 記憶

OpenViking 不是又一個向量資料庫。它在向量搜尋之上疊了一層檔案系統的抽象。所有 Agent 的上下文都透過一個自訂的 URI 來定位：

→ viking://resources/docs — 外部知識文件
→ viking://user/memories — 使用者記憶與偏好
→ viking://agent/skills — Agent 學會的技能
→ viking://session/current — 當前對話狀態

這個設計的好處是什麼？當 Agent 需要找「使用者上次提到不喜歡表格格式」這種記憶時，它不用從所有向量裡搜，只要鎖定 viking://user/ 這個 scope 去找就好。搜尋空間一下子縮小很多，精準度自然上來。

🧊 三層漸進式載入：L0 / L1 / L2

這是我覺得 OpenViking 最聰明的設計。每份被匯入的文件都會自動被處理成三個抽象層次：

→ L0（約 100 tokens）：一句話摘要。用來快速判斷「這份文件跟我的問題有沒有關」
→ L1（約 2,000 tokens）：核心內容概要。Agent 做決策時看這層就夠了
→ L2：完整原文。只在真的需要深入閱讀時才載入

搜尋時先用 L0 做全局篩選，找到相關的目錄後再載入 L1 做判斷，最後只有被選中的少數文件才會載入完整的 L2。

為什麼這件事重要？因為 Agent 系統最燒 token 的環節就是上下文注入。如果你把所有檢索到的文件原文都塞進 prompt，context window 很快就爆了。L0/L1/L2 這個漸進式架構讓 Agent 在大多數情況下只需要讀摘要就能做決策，token 消耗大幅下降。

📊 實際效果

在 LoCoMo10 benchmark（1,540 個長對話測試案例）上：

→ 準確率比 baseline 提升「49%」
→ token 消耗減少「83%」

跟 OpenClaw agent 框架整合後的測試更有意思：

→ 純 OpenClaw：任務完成率「35.65%」，消耗「2,460 萬」input tokens
→ OpenClaw + OpenViking：完成率跳到「52.08%」，tokens 降到「426 萬」

完成率高了快 16 個百分點，token 用量卻只剩不到五分之一。這個 trade-off 相當漂亮。

🔄 Agent 會自己進化

OpenViking 另一個值得注意的功能是自動記憶萃取。每次 session 結束時，它會從對話歷史裡自動提取 8 種記憶：

使用者側有 profile、偏好、提到的實體、事件記錄。Agent 側有學到的 case、執行模式、工具使用統計、技能指標。

提取完會自動去重，然後存進對應的 viking:// 路徑。下次對話時 Agent 就能調用這些記憶。換句話說，Agent 用得越多就越了解你，也越知道自己擅長什麼——這不就是我們一直想要的 long-term memory 嗎？

🤔 我的看法

我覺得 OpenViking 解決的是一個真實的工程問題。現在做 Agent 的團隊多少都踩過「記憶管理太亂」的坑——文件、對話歷史、工具記錄全混在一起，retrieval 品質隨著資料量增長而下降。用檔案系統的概念去組織這些東西，方向是對的。

不過有幾件事我想提醒：

第一，L0/L1 的摘要品質取決於背後的 LLM。如果摘要生成得不好，後續的檢索和決策都會受影響。論文沒有特別討論不同 LLM 生成的摘要品質差異。

第二，這套系統的部署複雜度不低。它背後有 Python service 層、Go 寫的 AGFS 儲存層、C++ 的向量索引、Rust 的 CLI 工具——四種語言。對小團隊來說，debug 和維護可能是個挑戰。

第三，目前還是 Alpha 階段。GitHub 上有 4,700 多顆星，社群關注度不錯，但 API 穩定性和向後相容性還需要時間觀察。

話說回來，如果你正在做 Agent 而且被記憶管理搞到頭痛，OpenViking 的 L0/L1/L2 三層架構和 URI scope 設計是值得借鑑的思路——就算不直接用它的框架，這個概念本身就能改善你的 retrieval pipeline。

🔗 GitHub：https://github.com/volcengine/OpenViking

<!-- fb -->

現在的 AI Agent 有個很尷尬的問題：它們的記憶基本上就是一坨向量。你跟它聊了什麼、給它餵了什麼文件、它上次學到了什麼教訓——全部打成 embedding 扔進同一個向量資料庫，然後用最近鄰搜尋去撈。一旦上下文類型變多，全部攪在一起搜尋，品質就開始崩壞。ByteDance 的火山引擎團隊開源了 OpenViking，核心想法出奇地直覺：把這坨向量變成一個有階層的檔案系統。

🗂️ 用檔案系統管理 Agent 記憶

OpenViking 在向量搜尋之上疊了一層檔案系統抽象。所有 Agent 上下文都透過自訂 URI 定位：

→ viking://resources/docs — 外部知識
→ viking://user/memories — 使用者記憶
→ viking://agent/skills — Agent 技能
→ viking://session/current — 對話狀態

當 Agent 需要找「使用者不喜歡表格格式」這種記憶時，它只要鎖定 viking://user/ 去搜就好。搜尋空間縮小，精準度自然上來。

🧊 三層漸進式載入

每份文件自動處理成三個抽象層次：

→ L0（約 100 tokens）：一句話摘要，快速判斷相關性
→ L1（約 2,000 tokens）：核心概要，Agent 決策用
→ L2：完整原文，只在需要深讀時載入

搜尋時先用 L0 篩選，找到相關目錄再載入 L1 判斷，最後只有少數文件載入完整 L2。大多數情況下 Agent 讀摘要就能做決策，token 消耗大幅下降。

📊 效果

在 LoCoMo10 benchmark 上：準確率提升「49%」，token 消耗減少「83%」。

跟 OpenClaw agent 框架整合：任務完成率從「35.65%」跳到「52.08%」，input tokens 從「2,460 萬」降到「426 萬」。完成率高了 16 個百分點，token 只剩不到五分之一。

🔄 自動記憶萃取

每次 session 結束時自動從對話歷史提取 8 種記憶（使用者偏好、Agent 技能、工具統計等），去重後存進對應 URI。Agent 用得越多就越了解你——這就是我們一直想要的 long-term memory。

🤔 我的看法

方向是對的。用檔案系統概念組織 Agent 記憶解決了真實的工程問題。

不過它的部署有 Python + Go + C++ + Rust 四種語言，小團隊維護可能吃不消。目前還是 Alpha 階段，API 穩定性需要觀察。

但就算不直接用它的框架，L0/L1/L2 三層架構和 URI scope 設計的概念本身就能改善你的 retrieval pipeline。

🔗 GitHub：https://github.com/volcengine/OpenViking（4,700+ stars，Apache 2.0）

#GenAI #Agent #Memory #RAG #ByteDance #OpenSource #LLM #ContextDatabase
