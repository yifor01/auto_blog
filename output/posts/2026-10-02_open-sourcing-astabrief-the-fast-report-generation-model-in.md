---
title: Open-sourcing AstaBrief, the fast report-generation model in Asta
source: HuggingFace Blog
url: https://huggingface.co/blog/allenai/astabrief
model: claude-code/sonnet
generated_at: '2026-10-02T21:34:09.171823'
score: 92
---

📌 Ai2 開源 AstaBrief：8B 小模型把科研報告生成時間砍去近 3.5 倍

TL;DR：Ai2 開源出專為科研報告生成訓練的 8B 模型 AstaBrief，速度明顯快於原本依賴的 Claude 方案。

當研究者向 Asta（Ai2 的科研用 agentic 平臺）丟出一個需要跨文獻比較、還要兼顧特定方法與族群限制的複雜問題時，若報告生成動輒要等上三分鐘，體驗其實不太好。Ai2 這次給出的答案，是自己訓練一個更小、更快、而且開放權重的模型。

🤔 科研報告跟一般聊天機器人的答案不一樣

Asta 的使用者多半不是丟短短幾個關鍵字，而是帶著大量脈絡、多重限制條件進來提問，而且常常會回頭把生成的報告當成持續更新的研究素材，而不是一次性的答案。這對模型提出了額外要求：答案要緊扣證據、不能悄悄把研究結論誇大，而且使用者要能夠驗證最終輸出。為此，Ai2 想知道一個專門訓練來做科研報告生成的小型開放模型，能否在報告品質上追上他們原本使用的專有模型，同時大幅降低生成時間與服務成本。

🧩 捨棄 RL，改用一次到位的 SFT + DPO

AstaBrief 8B 以 Qwen3-8B 為基礎模型。Ai2 先前的 DR Tulu 已顯示強化學習（RL）搭配 judge 模型能改善長文報告生成品質，團隊也考慮過這條路，但最終選擇以監督式微調（SFT）加上直接偏好最佳化（DPO）為主的訓練組合，理由是 RL 訓練不穩定且成本高，而一套更簡單、更容易除錯迭代的流程，反而讓他們能把更多心力放在訓練資料本身的品質上。為了加快速度，AstaBrief 被訓練成直接在一次生成（one pass）中，根據使用者問題與檢索到的文獻片段，直接寫出完整報告，略過 Claude 版 Thinking mode 所需要的片段摘要、分群階段，也不再逐節撰寫答案。團隊發現，這樣做並沒有犧牲品質。

📊 90K 真實查詢過濾出 47K 筆訓練資料

訓練資料來自 Asta／ScholarQA 系統中真實使用者送出的查詢，而非純合成或純 benchmark 題目。團隊過濾掉測試人員與機器人流量、過短的查詢，並用 LLM 做額外篩選，剔除非英文、非科學性內容與含個資的提問，最終留下 9 萬筆研究導向查詢。針對 SFT，團隊用既有的多階段 ScholarQA 流程（檢索文獻、組織成節、再用一個生成模型合成出有引用的報告）產生目標輸出，背後混用了 Claude 3.5 Sonnet、Claude 3.7 Sonnet、o3、o4-mini 與 GPT-4.1 等多個專有系統，經品質過濾後得到 4.7 萬筆可用訓練樣本。DPO 則需要另一種資料形式：同一個查詢對應一組「較佳」與「較差」的報告配對。

📊 Fast mode 比 Thinking mode 快 3.5 倍

在完整的 Asta 流程中，採用 AstaBrief 的 Fast mode 平均每份報告耗時 51.1 秒，相較之下由 Claude 驅動的 Thinking mode 平均要 178.5 秒，快了約 3.5 倍。Ai2 同時開源了模型權重與訓練資料，並額外釋出一套範例工作流程，讓研究者能把自己的 PDF 檔案接進去，作為本地端報告生成的起點。開放權重也讓機構能在自家基礎設施上跑模型，這在研究問題涉及敏感或尚未發表的工作時特別重要。

⚠️ 評測基準停在 2025 年的前沿模型

文中特別提醒，絕大部分訓練與評測工作是在 2025 年完成，用來生成訓練資料與作為比較基準的專有模型，反映的是當時的技術前沿，團隊並未針對今日的前沿模型重新跑過完整評測。因此這些結果更適合被理解為「這套訓練與系統設計選擇有效」的證據，而不是一個放諸四海皆準的絕對品質宣稱。

🎯 實務啟示

對於需要在自有基礎設施上跑科研助理、又在意資料敏感性的機構，AstaBrief 提供了一個現成的起點：用真實使用者查詢搭配精心過濾的資料，SFT + DPO 這種相對單純的訓練組合，也有機會在特定任務上逼近專有模型的品質，同時換來數量級的速度提升。

🔗 來源
- 標題：Open-sourcing AstaBrief, the fast report-generation model in Asta
- 作者／機構：Kyle Wiggers（Ai2）
- 連結：https://huggingface.co/blog/allenai/astabrief

#AstaBrief #Ai2 #OpenSource #LLM #ScientificAI #RAG #SFT #DPO #Qwen3 #ResearchTools
