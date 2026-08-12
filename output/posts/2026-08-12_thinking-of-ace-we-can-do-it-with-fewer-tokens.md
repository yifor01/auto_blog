---
title: Thinking of ACE? We Can Do It with Fewer Tokens
source: HuggingFace Blog
url: https://huggingface.co/blog/ibm-research/altk-evolve-sldd
model: claude-code/sonnet
generated_at: '2026-08-12T07:33:24.655348'
score: 92
---

📌 【IBM Research】同樣讓 Agent 從經驗中學習，ALTK-Evolve 為何只花 ACE 四成 token

TL;DR：ALTK-Evolve 與 ACE 都靠 agent 過往軌跡累積經驗，但按需檢索讓推論成本大砍近九成。

兩套系統學到的東西一模一樣，最後的 token 帳單卻能差到七倍——差別不在「學到什麼」，而在「怎麼把學到的東西交回給模型」。

🤔 Agent 不是不懂 API，是不知道怎麼穩定用它

給 LLM agent 一個真實的多步驟任務——分帳單、找一首歌、在九個模擬 App 之間核對訂單——失敗時通常不是因為模型不懂這些 API，而是它把分頁參數搞錯、認錯了對象，或是在不該回傳值的時候硬要回傳一個值。模型知道 API 存在，卻沒有內化「如何穩定使用它」，而這件事恰好可以從 agent 自己過去的操作歷史中學到。ACE（Agentic Context Engineering）與 IBM Research 的 ALTK-Evolve 都是針對這個現象設計的「agentic memory」：把 agent 過去的軌跡轉換成可重複使用的經驗，在推論時餵回去，不更新權重、不需要人工標註。

兩者甚至對「哪裡最難」有共識，只是對「學到的東西」命名不同：本文統一稱為 lesson（教訓／經驗），ACE 把它們整理成一份持續演化的 playbook（手冊），ALTK-Evolve 則整理成一組可個別檢索的 guidelines（準則）——同樣的經驗，兩種容器。

🧩 都拒絕壓縮，但「怎麼建立」與「怎麼送出」不同

兩套系統都同意一件事：不能把 agent 辛苦累積的經驗壓縮成一份精簡摘要。ACE 明確指出兩個失敗模式：brevity bias（最佳化過程收斂成簡短、籠統的指令）與 context collapse（要求模型每一步重寫整個上下文，反而把細節摘要掉）。它的解法是維持一份豐富、逐條列出的 playbook，每條都附上 helpful／harmful 計數器，讓模型在讀取當下自行判斷相關性。ALTK-Evolve 的作法方向相反卻殊途同歸：每一條獨立的 guideline 都保留 support count（有多少個獨立案例產生了這條經驗），從不把經驗庫摘要成少數幾條規則。一條被五個不同任務各自發現的教訓，和只出現過一次的教訓是不同的物件，兩者都值得保留。

真正的差異出在兩處：經驗庫怎麼建立（consolidation），以及推論時怎麼送出（delivery）——而正是後者決定了 token 帳單。ACE 透過 Generator → Reflector → Curator 迴圈持續擴充同一份 playbook，以增量式更新並用 embedding 去除重複；ALTK-Evolve 則把相近的 lesson 聚類、在群集內合併，且合併時「保留支持度」——多條經驗合併後，存活下來的那條會繼承所有經驗的總 support count，經驗庫因此縮小但不會丟失背後的經驗量。ALTK-Evolve 還會抽取帶類型的 guideline（策略、恢復、最佳化），附上因果歸因與回溯到原始軌跡的 provenance，且顆粒度細到 subtask 層級，讓一個 App 上學到的教訓能遷移到另一個 App。

在送出方式上，ACE 每一步都注入完整的 playbook，不論模型或任務為何皆一致；ALTK-Evolve 則把「送出多少」當成一個可調的旋鈕：一小組高 support 的核心 guideline 固定送出，再依任務額外挑選少數幾條（用 cosine 或 LLM 引導、依優先權加權），若模型有足夠餘裕，也可以送出完整的整合經驗庫。兩者能取用的經驗其實一樣多，差別只在於 ACE 永遠全送，ALTK-Evolve 只送模型「真正用得上」的份量。

📊 強模型雙贏、弱模型省七倍成本

團隊在 AppWorld benchmark 上，用相同的 base ReAct agent，於內部同時跑了兩套系統：

| 模型 | 系統 | TGC／SGC | 每任務 Tokens |
|---|---|---|---|
| DeepSeek-V3.2 | ACE | 80.4／73.2 | 634K |
| DeepSeek-V3.2 | ALTK-Evolve | 89.3／80.4 | 263K |
| gpt-oss-120b | ACE | 54.8／35.7 | 777K |
| gpt-oss-120b | ALTK-Evolve | 56.0／37.5 | 116K |

在較強的 DeepSeek-V3.2 上，ALTK-Evolve 兩項指標都勝出，推論成本卻只有 ACE 的約四成。在較弱的 gpt-oss-120b 上，ALTK-Evolve 以 56.0 對 54.8 小幅領先（團隊重跑一次得到 54.8，與 ACE 幾乎打平，落在該 benchmark 的執行間雜訊範圍內，故視為打平），但成本僅約 ACE 的七分之一。團隊也坦言，ACE 的效率故事著重在「便宜地建立」上下文，而 ALTK-Evolve 的效率故事在於「怎麼把它送出去」——每次任務只檢索少數幾條 guideline，而非每一步都注入整份 playbook，正是 token 節省的來源。

依難度拆解後能看到兩個不同的故事：在 DeepSeek-V3.2 上，ALTK-Evolve 在 Easy、Hard 與 Overall 都領先，ACE 只在 Medium 略勝；在 gpt-oss-120b 上，ACE 在 Easy 與 Medium 領先，但 ALTK-Evolve 在 Hard 任務上勝出，並因此拿下整體排名。團隊的解讀是：在 gpt-oss-120b 上，Easy／Medium 任務靠通用指令遵循就能解決大半，完整 playbook 反而有利；但 Hard 任務需要「挑對那一條經驗」而非在一堆經驗裡跋涉，這時精準檢索就會勝出，也正是這個難度層級決定了整體排名。在 DeepSeek-V3.2 上，較強的模型足以吸收 ACE 的完整 playbook，因此在 Medium 上打平甚至略勝，但當模型有更多餘裕時，ALTK-Evolve 送出更多經驗只會持續帶來幫助，而不會互相干擾，因此在 Easy、Hard、Overall 都保持領先。團隊也強調，他們替每個模型挑選最適合的配置——強模型用完整整合經驗庫，弱模型用選擇性檢索——因為過大的上下文對能力較弱的模型反而是干擾而非幫助。

⚠️ 說明範圍

以上數據來自 AppWorld 的 test_normal 子集（168 個任務），使用會在每一步撰寫 Python、由環境回傳輸出的 ReAct code agent；TGC（Task Goal Completion）與 SGC（Scenario Goal Completion，要求場景所有變體都通過）均為單次執行（pass@1）結果，經驗僅從 train／dev 資料中挖掘，這是該 benchmark 的標準做法。文中的 ACE 數據是團隊在相同 AppWorld 切分與相同 base model 上自行跑出的結果，而非直接引用原論文數字。

🎯 實務啟示

如果你正在替 agent 系統設計記憶機制，這篇文章給出的核心提醒是：「要不要壓縮經驗」和「要不要一次全部送出」是兩個獨立的決策，前者的答案幾乎肯定是不要壓縮，但後者值得依模型能力動態調整——對能力強的模型可以放心送出更完整的經驗庫，對能力較弱的模型，過量的上下文反而會拖累表現，這時精簡、依任務檢索的策略更划算。

🔗 來源
- 標題：Thinking of ACE? We Can Do It with Fewer Tokens
- 作者／機構：IBM Research（HuggingFace Blog）
- 連結：https://huggingface.co/blog/ibm-research/altk-evolve-sldd

#AgenticAI #LLMAgent #ContextEngineering #IBMResearch #AppWorld #AgenticMemory #TokenEfficiency #ReAct #PromptEngineering #InferenceCost
