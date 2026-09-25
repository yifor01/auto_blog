---
title: Perplexity Trains Its Computer Agent on Real Mistakes With Hint-Guided Self-Distillation
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/25/perplexity-trains-its-computer-agent-on-real-mistakes-with-hint-guided-self-distillation/
model: claude-code/sonnet
generated_at: '2026-09-25T20:46:06.258349'
score: 95
---

📌 Perplexity 讓模型從自己的失敗紀錄中學糾錯

TL;DR：Perplexity 用「提示引導自我蒸餾」訓練 agent，把工具呼叫失敗率壓低了 21.2%,但方法沒開源。

一個 agent 明明答對了任務，卻可能是因為它在中途犯了錯又僥倖救回來。如果只模仿「成功的完整軌跡」，等於連那個錯誤動作也一起學進去了。Perplexity Research 這篇最新的後訓練研究，就是想解決這個矛盾。

🤔 **成功的軌跡裡藏著該丟掉的錯誤**

Perplexity Research 發表一份新的後訓練研究，直接用 Perplexity Computer 裡真實使用者的 session（包含失敗的 session）訓練模型。標準的拒絕採樣微調（rejection sampling fine-tuning，RFT）做法是評判每個 session，只模仿成功的那些。但「成功」不代表每一步都正確,agent 完全可能在某次工具呼叫犯錯後又自行修正,最終給出正確答案,若把整段軌跡照單模仿,反而會把那個錯誤動作也一併強化。反過來，直接丟掉失敗的 session，又等於白白浪費了「這裡有個明確可避免的錯誤」這個清楚的訓練訊號。

🧩 **拆成兩個決策：模仿什麼、糾正什麼**

Perplexity 團隊把問題拆成兩個獨立決策：哪些 session 裡的行為值得模仿，哪些 turn（對話輪次）裡的錯誤值得糾正。成功的 session 可以同時提供模仿目標與糾正目標，失敗的 session 則只提供糾正目標。

糾正的核心是一種「提示（hint）」機制：hint 是一段簡短的糾正指示，且必須根基於模型當下已經擁有的資訊。文中舉例，一次搜尋呼叫把 `recency_filter` 設成 'year'，但 schema 只允許 'day'、'week' 或 'month'，hint 會指出是哪次呼叫失敗、附上驗證錯誤訊息，並建議一個允許值或直接省略該可選欄位。

糾正的訓練機制稱為 On-Policy Self-Distillation（OPSD）：訓練器對同一筆記錄的 turn，用同一個 GLM 5.2 checkpoint 跑兩次，teacher 那次看得到 hint，student 那次看不到，兩者都使用 teacher forcing，因此不會生成替代答案。teacher 的下一個 token 機率分布被 detach（脫離梯度）後，透過前向 KL 散度作為 student 的軟目標。合併後的損失函式是 (CE + λ × KL) 除以被模仿的 token 數，當 λ 設為 0 就退回標準的 SFT。CE 項不可或缺,因為若只靠糾正項訓練,teacher 與 student 有可能靠忽略上下文本身就達成一致,反而學不到真正有用的訊號。

📊 **A/B 測試：工具呼叫失敗率降了 21.2%**

在一次上線的 A/B 測試中，兩個訓練 checkpoint 之間，工具呼叫失敗率從 2.24% 降到 1.77%，Perplexity 團隊表示這是統計上顯著的 21.2% 相對降幅。

資料管線只取自 GLM 5.2 服務、且符合訓練資格的 Computer session，含個資（PII）與已選擇退出的使用者一律排除。一個 LLM judge 先篩出難度落在 5 分量表中 4 或 5 分的任務；判斷一個 session 是否算「成功」，須經過兩個 LLM judge 都認可最終交付結果；針對使用者回饋，則由三個 LLM judge 定位出真正該負責的 turn，至少兩個判斷一致才算數。這個機制的重要性在於，文中提到使用者抱怨前的最後一個 assistant turn，只有大約一半的機率才是真正的問題根源。每一條 hint 也會反向檢查，確保它只使用「錯誤發生之前」模型就已掌握的資訊，藉此降低後見之明偏誤（hindsight bias）。文中另舉一例：使用者在 Paychex 上詢問自己的「w3」，模型誤判為 W-2 的筆誤而搜錯表單，對應的 hint 針對的是「更早的理解錯誤」，而不只是修正最終答案。

⚠️ **目前無法直接部署**

Perplexity 尚未釋出後訓練後的權重或訓練程式碼，這個模型目前只作為 Perplexity Computer 裡的一個模型選項存在；底層的基礎模型 GLM 5.2 本身則是在 Hugging Face 上公開可取得的。

🎯 **實務啟示**

這套「模仿與糾正目標分離」的思路，對自建 agent 訓練 pipeline 的團隊有直接參考價值：與其把失敗 session 整批丟棄，不如區分「哪個 turn 出錯」與「哪個 session 的整體行為值得模仿」，再用根基於既有資訊的 hint 做 teacher forcing 式的自我蒸餾。可惜方法雖具體，訓練程式碼與權重都未開源，想要複現目前只能依賴論文本身描述的損失函式與資料篩選流程自行實作。

🔗 **來源**
- 標題：Perplexity Trains Its Computer Agent on Real Mistakes With Hint-Guided Self-Distillation
- 作者／機構：Michal Sutter，MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/25/perplexity-trains-its-computer-agent-on-real-mistakes-with-hint-guided-self-distillation/

#Perplexity #SelfDistillation #PostTraining #AgentTraining #RejectionSampling #LLM #GLM #AIAlignment #ToolUse #MachineLearning
