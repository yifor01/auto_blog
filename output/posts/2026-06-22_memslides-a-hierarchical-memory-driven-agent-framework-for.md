---
title: 'MemSlides: A Hierarchical Memory Driven Agent Framework for Personalized Slide
  Generation with Multi-turn Local Revision'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.17162
score: 78
model: google/gemma-4-31b-it:free
generated_at: '2026-06-22T21:10:18.805544'
---

📌 MemSlides：利用階層記憶框架實現個人化投影片生成與區域性修訂

TL;DR：透過三層記憶機制（長期、工作、工具記憶），讓 AI 代理能穩定維持個人化風格並支援多輪區域性修改。

製作投影片最痛苦的往往不是生成第一版，而是在多輪修改中，AI 總是忘了你之前的風格偏好，或者在修改區域性內容時弄亂了整份簡報的結構。

🤔 **解決個人化與區域性修訂的不穩定性**

MemSlides 提出了一個階層化記憶（Hierarchical Memory）框架，旨在解決個人化投影片生成代理（Agent）在多輪修訂中容易失去方向的問題。其核心目標是讓 AI 能在維持使用者個人偏好的同時，穩定地執行區域性編輯。

🧩 **三層記憶架構設計**

為了確保生成的穩定性與可靠性，MemSlides 將記憶拆分為三個獨立層級：

- **長期記憶 (Long-term User Profiles)**：儲存使用者的個人偏好與設定，確保生成的投影片具有一致的個人化風格。
- **工作記憶 (Working Memory)**：記錄當前對話 session 的約束條件，用以處理即時的生成需求。
- **工具記憶 (Tool Memory)**：儲存可重複利用的執行經驗，提升在呼叫工具執行投影片編輯時的可靠度。

這種分離設計讓代理在面對「多輪區域性修訂 (Multi-turn Local Revision)」時，不需要每次重新讀取所有資訊，而是能精準地從對應層級提取記憶。

🎯 **實務啟示**

對於開發 AI Agent 的工程師來說，MemSlides 的設計證明瞭「記憶分層」能有效解決長對話中的資訊混亂問題。將「使用者偏好（靜態）」、「對話上下文（動態）」與「工具操作經驗（經驗）」分開管理，是提升複雜生成任務（如簡報、檔案編輯）穩定性的有效路徑。

🔗 **來源**
- 標題：MemSlides: A Hierarchical Memory Driven Agent Framework for Personalized Slide Generation with Multi-turn Local Revision
- 連結：https://huggingface.co/papers/2606.17162

#AI #Agent #HierarchicalMemory #Personalization #SlideGeneration #LLM #MultiTurnRevision #ProductivityTools #MemoryFramework #AIResearch
