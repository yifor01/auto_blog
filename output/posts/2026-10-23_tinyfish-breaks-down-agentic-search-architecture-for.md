---
title: TinyFish Breaks Down Agentic Search Architecture for Production AI Agents
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/23/tinyfish-agentic-search-architecture-deep-research/
model: claude-code/sonnet
generated_at: '2026-10-23T20:42:18.298011'
score: 89
---

📌 生產級搜尋 Agent 為何總在上線後翻車？TinyFish 給出架構拆解

TL;DR：TinyFish 拆解自家 agentic search 架構的七階段控制迴圈，揭露讓搜尋 agent 在生產環境裡不翻車的設計細節。

Demo 裡表現完美的搜尋 agent，一上生產環境就可能因為檢索結果不完整、重試一直重複同樣的失敗動作、或是執行超過時間與成本上限而失靈。網頁基礎設施公司 TinyFish 發布了兩份技術指南，一份定義生產級 agentic search 架構，另一份分享打造深度研究系統的實戰教訓。

> 提醒：本篇原文由 TinyFish 贊助發表，內容含有該公司自身的 benchmark 數據，閱讀時宜留意其行銷性質。

🤔 **讓模型只管推理，其餘交給確定性的程式邏輯**

TinyFish 的核心主張是：模型負責推理，而周圍的應用程式負責管理狀態、執行工具、處理證據、落實執行期策略與驗證輸出。這樣的分工讓 agent 能處理結果不完整、可恢復的失敗，以及中途改變的資訊需求。這套架構奠基於一篇 2026 年 2 月的架構 preprint，核心是透過型別化（typed）工具介面，把推理與執行解耦，並建立起必要的系統護欄：詳細的 tracing，以及對 token 數、執行時間、總成本、工具呼叫次數的嚴格上限。

🧩 **四個 web 原語、七階段控制迴圈**

TinyFish 的系統建立在四個 web 原語之上：TinySearch、TinyFetch、TinyBrowser、TinyAgent，並以圍繞 base model 的七階段控制迴圈運作。其中第 2 階段處理的是 ChainRAG（ACL 2025）所稱的「lost-in-retrieval」問題——在多跳（multi-hop）問題拆解過程中，關鍵實體會中途消失。第 6 階段則借鏡 Search-R1：模型能在推理過程中判斷先前檢索不足時，主動產生額外的搜尋查詢；在 7 個 QA 資料集上，這種學習型多輪搜尋比 RAG baseline 分別在 Qwen2.5-7B 上高出 41%、在 Qwen2.5-3B 上高出 20%。

TinyFish 強調兩個設計原則：路由（routing）應該跟著「資訊缺口」走，而不是固定的升級階梯——結果不夠好未必要升級到更重的工具，查詢品質不好該換個查詢，證據互相矛盾則需要更強的證據而非更重的工具；重試則應該依失敗類型而定並設有上限，暫時性錯誤可以直接重試，但不完整或互相衝突的證據需要換一種做法，而瀏覽器的重試更要注意是否已完成某些動作，避免重複送出同一張表單這類副作用。

💡 **深度研究系統踩過的三個坑**

TinyFish 的深度研究 agent 負責搜尋、瀏覽並產出附引用的完整報告，而打造過程中最大的挑戰集中在上下文管理、系統編排與產品設計三方面。最初版本用一個每次重新呼叫的獨立規劃器，只傳入結構化狀態，結果像「只聚焦東南亞的定價風險」這類後續追問，反而讓 agent 又飄回廣泛的市場研究——後來團隊把規劃邏輯併入 orchestrator 自身的統一推理迴圈才解決。另一個問題是最初為每個搜尋查詢各配一個獨立 subagent，拉高了上下文切換開銷、延遲與成本，團隊後來把排序搜尋結果、分類來源、萃取證據這類可重複的任務改成工具呼叫，大幅減少回傳給 orchestrator 的資訊量，讓它能專注在研究規劃與決定下一步調查方向。此外，團隊一開始把系統最佳化目標放在「來源覆蓋率」，但使用者其實更看重證據的品質與相關性，因此調整了來源排序邏輯讓它依研究目標而定，並加入優先、排除、限制特定網域的控制選項，同時建立以 LLM 作為評審的內部評估機制，評估報告的相關性、證據強度、引用可信度與來源多樣性。

📊 **OpenBenchmarks 上的數字**

TinyFish 引用 SearchAgent-X（ICLR 2026）的發現，說明為何要以整個任務、而非單一呼叫為單位做預算控管：過於精確的檢索會增加額外開銷，過於粗略的檢索又會迫使模型做更多額外推理，對應的修正讓他們在測試的 baseline 上達到最高 3.4 倍的吞吐量與 5 倍更低的延遲。在 OpenBenchmarks（固定模型 gpt-5.6-sol、100 個任務與預算、僅變動 provider，分數取 3 次執行平均，更新於 2026 年 9 月 26 日，任務範圍僅限企業文件）上，TinyFish 在程式撰寫任務達到 79.0% 的完成率，同時擁有受測中最低的任務中位數成本（0.050 美元）與 token 用量。在僅比較「search-only」的設定下，TinyFish 完成率為 59.3%，低於 Perplexity 的 77.3%、Firecrawl 的 70.3%、Exa Fast 的 66.3%；但原文特別註明，這組數字不應直接拿來跟 search-and-fetch 的分數比較，因為兩種設定下可用的檢索能力並不相同。

⚠️ **贊助內容，數字需帶著保留態度看待**

這篇文章由 TinyFish 贊助刊出，benchmark 數字來自其自有的 OpenBenchmarks 排行榜，且任務範圍僅限企業文件，解讀時應留意立場與樣本侷限。

🎯 **實務啟示**

無論是否採用 TinyFish 的架構，其揭露的幾個原則都值得借鏡：把規劃邏輯收斂進單一的推理迴圈、用工具呼叫取代大量獨立 subagent 以降低上下文切換成本、依失敗類型而非固定升級路徑去設計重試邏輯，並且用任務整體預算（而非單次呼叫）來控管檢索的精細度，是打造生產級搜尋 agent 時可以直接參考的設計取捨。

🔗 **來源**
- 標題：TinyFish Breaks Down Agentic Search Architecture for Production AI Agents
- 作者／機構：Asif Razzaq, MarkTechPost（本文為 TinyFish 贊助內容）
- 連結：https://www.marktechpost.com/2026/10/23/tinyfish-agentic-search-architecture-deep-research/

#AIAgents #AgenticSearch #RAG #DeepResearch #TinyFish #LLM #InformationRetrieval #AIBenchmark #SearchR1 #ProductionAI
