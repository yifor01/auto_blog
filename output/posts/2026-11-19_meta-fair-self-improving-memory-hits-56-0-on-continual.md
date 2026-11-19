---
title: Meta FAIR Self-Improving Memory Hits 56.0 on Continual Learning Bench
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/19/meta-fair-self-improving-memory-harness-distillation/
model: claude-code/sonnet
generated_at: '2026-11-19T23:44:51.204056'
score: 99
---

📌 讓 AI 自己寫記憶使用手冊,再蒸餾進權重裡

TL;DR：Meta FAIR 提出兩階段法,讓 agent 先發現最佳記憶策略再蒸餾進模型,持續學習任務上平均進步 14.6%。

如果一個 AI agent 每次處理新任務都要從空白 context 開始,只靠一個共用的記憶資料夾延續過去的經驗,它該怎麼決定「這次該記什麼、下次又該怎麼讀」?Meta FAIR 的答案是:別人工寫死規則,讓模型自己試出來,再把試出來的技能訓練進權重裡。

🤔 **核心問題:沒有一種手寫記憶策略能贏到底**

Self-Improving Memory 是 Meta FAIR 提出的兩階段方法,共同作者包括華盛頓大學與約翰霍普金斯大學的研究者。設定是這樣的:agent 要處理一串 subtask,每個 subtask 都從空白 context 開始,唯一能延續下去的是一個用檔案工具編輯的持久記憶目錄。兩個 prompt 控制這個記憶流程:OFFLOAD 在 subtask 結束後更新記憶,LOAD 在下一個 subtask 開始前取回筆記。一般版本的 OFFLOAD/LOAD 把「怎麼記、怎麼取」的策略完全交給模型自己判斷。研究團隊在一次 pilot study 中發現,沒有任何單一的手寫策略能在所有任務上都贏。

🧩 **第一階段:讓 meta agent 搜尋出更好的記憶 prompt**

搜尋從 4 個人工撰寫的種子策略開始:Summary、Retrieval、Skill 與 Hypothesis。每個候選 prompt 都會把完整的任務流程跑 5 次,取平均分數最高的 4 個作為下一輪的「父代」。針對每個父代,meta agent 會讀取過去的 trajectories、分數與最終的記憶目錄內容,據此提出修訂版的 prompt。篩選則使用 meta agent 看不到的 holdout set,避免它針對已知測試過度擬合。

搜尋出來的 prompt 相當具體:針對 Database 任務,最佳策略要求先讀 GUARDRAILS.md,再讀 SCHEMA.md,之後才能回答問題;針對 Codebase 任務,最佳設計是用一個 quickstart 檔案,搭配一個有索引的 fix registry,以及分開存放的個別 fix 檔案。

**第二階段:Discover-Demonstrate-Distill 蒸餾流程**

task agent 先用第一階段搜尋出的最佳化 prompt,跑過訓練用的 subtask,過程中每一次模型呼叫都會被記錄下來。接著,研究團隊把歷史紀錄中的最佳化 prompt,替換回原本的 generic 版本——這個置換之所以成立,是因為行為本身在 generic 指示下依然有效,例如維持 QUICKSTART.md、REGISTRY.md、SCHEMA.md 等檔案的存在,或是在做聚合運算前先驗證 join keys 是否正確。

之後用 LoRA(rank 64)對 attention 投影層做微調,loss 只計算 assistant 產生的 token,包含推理過程與工具呼叫,每個任務給予相同權重。值得注意的是,meta agent 與 task agent 用的是同一個 Kimi-K2.6 模型,也就是說,最終的模型是被訓練去內化它自己發現出來的記憶管理技能。

📊 **三個持續學習任務上全面超越手寫種子**

測試使用 Continual Learning Bench 中的 3 個任務:Database(SQL)、Codebase(修復程式碼倉庫問題)與 Spectrum(無線電頻譜掃描)。測試用的 subtask 經過設計上的 phase shift,因此結果衡量的是模型對同類任務「新實例」的泛化能力,而非單純背答案。

最佳化後的記憶 harness 在三個任務上都贏過最好的手寫種子,其中 Codebase 進步最多,達 20.6 分。不過搜尋過程本身相當不穩定:44 個生成出來的修訂版本中,有 37 個沒能贏過前一輪的最佳版本。Database 與 Spectrum 任務都在第一代搜尋就達到峰值,而 Codebase 則持續進步到第四代才收斂。

蒸餾完成後,所有模型統一跑 generic harness 進行比較:蒸餾後的模型在 10 個配對種子上平均得分 43.1,而直接用 generic trajectories 做 SFT 的模型只有 37.6。這代表一個 5.5 分、約 14.6% 的提升。

💡 **跟其他「搜尋記憶策略」的方法比起來,少了一道校正步驟**

文中提到,近期已有多種方法會搜尋 agent 的記憶或 harness,其中 Harness-Zero 是最接近的對照方法,但它需要另一個獨立的 agent 來校正 student 模型的行為;Self-Improving Memory 則直接省略了這一道校正步驟,改用蒸餾本身完成內化。作者也提醒,各方法使用的 benchmark 不同,headline 數字之間並不能直接比較。

⚠️ **搜尋過程本身噪音很大**

44 個生成修訂中有超過八成沒能超越前一輪最佳版本,顯示這套搜尋機制本身效率並不穩定;三個任務的收斂速度也不一致,有的第一代就封頂,有的要到第四代才見效。這意味著實際落地時,搜尋輪數與運算成本可能因任務而有明顯差異。

🎯 **實務啟示**

對於正在打造長任務 agent 的工程師,這個方法提供了一條具體可行的路徑:先讓模型自己試出最適合的記憶管理策略,驗證過行為在 generic 指示下依然成立後,再用 LoRA 這種低成本微調方式把技能內化進權重,不需要在推理時持續依賴特製 prompt。

🔗 **來源**
- 標題：Meta FAIR Self-Improving Memory Hits 56.0 on Continual Learning Bench
- 作者／機構：Michal Sutter / MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/19/meta-fair-self-improving-memory-harness-distillation/

#MetaFAIR #ContinualLearning #AIMemory #LoRA #AgentMemory #SelfImprovement #KnowledgeDistillation #LLMAgents #FineTuning #MachineLearningResearch
