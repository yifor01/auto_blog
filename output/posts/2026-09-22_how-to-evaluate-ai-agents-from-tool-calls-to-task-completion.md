---
title: How to Evaluate AI Agents From Tool Calls to Task Completion
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/how-to-evaluate-ai-agents-from-tool-calls-to-task-completion/
model: claude-code/sonnet
generated_at: '2026-09-22T20:30:19.164805'
score: 90
---

📌 評估 AI Agent，不能只看單次呼叫像不像

TL;DR：NVIDIA 部落格梳理 agent 評測如何從單次呼叫進化到整個任務成敗。

一個 agent 呼叫的 API 語法完全正確、參數也填對，但如果背後該做的檢查或更新被跳過了，這個任務仍然算失敗——這正是為什麼「評估 agent」和「評估模型輸出」是兩件完全不同的事。

🤔 **從單一輸出到多步驟任務，舊評測框架不夠用**

早期的評測工具是為靜態任務設計的：給一個輸入，看一個輸出字串對不對。第一個與模型無關、開源的評測框架，把模型和評測協定分離開來，但 agent 打破了這個假設，它要在多步驟任務中呼叫工具、處理錯誤、觀察結果，單一輸出字串已經不夠用了。Berkeley Function-Calling Leaderboard（BFCL）因此出現，用來評估單輪與多輪情境下的函式選擇與參數準確度。但 BFCL 只評估「個別呼叫」本身，文章舉例：一次語法正確的 issue_refund 呼叫，如果背後該執行的檢查或更新被跳過了，任務照樣算失敗。呼叫正確是必要條件，但不是充分條件。

🧩 **完整的 agent 評測，需要一個真正會執行的環境**

要完整評估 agent，需要一個能執行每次工具呼叫、追蹤跨步驟狀態、並在事後讀取世界狀態來判斷任務是否完成的執行環境。在這個環境之上疊了兩層評分：Step-level（過程評分）問「在當下的狀態下，這次呼叫是否有效、相關且有用？」；End-to-end／E2E（結果評分）忽略過程，只看最終狀態，例如退款有沒有真的入帳、工單有沒有正確分派。Step-level 能告訴你鏈條在哪裡斷掉，適合除錯或決定微調的施力點；E2E 則會把「第一步就失敗」和「第九步才失敗」都算成同一種「任務失敗」，但 E2E 才是使用者真正體驗到的結果，所以多數上線評測會把 E2E 當作放行的關卡，同時保留 step-level 追蹤在底層供除錯用。這兩種分數其實是同一份東西的兩種讀法：trace（追蹤紀錄），是單次嘗試的完整有序紀錄，包含使用者訊息、每一步，以及嘗試結束時的環境狀態；process scoring 是對每一列打分，E2E scoring 則是對最終狀態打分。

一個工具呼叫的評測，依序評估三件事：要不要用工具、選對工具、把參數填對。該用工具卻直接給答案，跟該給答案卻硬要呼叫工具，都一樣算失敗；成本與延遲則疊加在上面，由呼叫的冗長程度與執行時間決定。

每一次評測執行都依循一個固定的層級關係：Benchmark → Trial → Task → Turn → Step。Trial 是在固定設定下，對整個任務集合跑一次獨立的嘗試；Task 是一個可以獨立打分的問題實例，有自己的 task ID；Turn 是一次「訊息進、agent 回覆出」之間的交換邊界，中間發生的一切都屬於這個 turn；Step 則是 turn 裡的一個原子動作，可能是一次工具／指令呼叫，也可能是非工具的輸出，例如一份計畫或最終回覆。Step 通常就是一次工具呼叫，往上所有的分數都是從這些 step 一路捲上去的。

📊 **該追蹤的指標，收斂成三個軸：準確度、冗長度、成本**

| 指標 | 公式 | 軸向 | 為什麼重要 |
|---|---|---|---|
| Task success rate | successful_tasks / tasks | 準確度 | 放行的關鍵門檻，環境是否真的到達目標狀態 |
| Consistency | 3-5 次 trial 間成功率的區間 | 準確度 | 90%／74% 的分佈不等於 84%，該報範圍而非單一點估計 |
| Tool-call precision | correct_calls / calls_issued | 準確度 | 幻覺呼叫、多餘呼叫會在這裡現形，而非在成功率上 |
| Argument accuracy | correct_args / calls_with_right_tool | 準確度 | 區分「呼叫錯 API」和「呼叫對 API 但填錯參數」 |
| Steps per success | steps / successful_tasks | 冗長度 | 任務真的完成時，軌跡跑了多長 |
| Cost per success | spend / successful_tasks | 成本 | token 與 GPU 秒數只有換算成每個成功任務才有意義 |

這些指標要成對看：只看成功率不看一致性，等於把一個隨機系統的表現當成單一個點估計，一個時而 90%、時而 74% 的模型，比一個穩定維持在 84% 的模型風險更高；只看 tool-call precision 不看 argument accuracy，會把填錯參數的失敗藏起來。同一個任務下，不同模型之間差異最大的軸往往是 step 數（四步 vs 十五步），不過在 Terminal-Bench 2.0 這類套件上，每個 turn 的 step 數本身也會變動，所以哪個軸差異最大要看具體 benchmark。平行工具呼叫可以縮短 step 數與延遲，但不會減少呼叫次數，一個 turn 裡同時打出四個工具呼叫，仍然是四次呼叫。重點是要依序捲上分數，不能把 step 數拿去平均後當成 benchmark 總分。

💡 **看懂一份評測結果，要分辨三個維度**

兩個都號稱在測「工具呼叫」的 benchmark，數字可能完全不能比。差異通常來自三個維度：任務複雜度（單輪單一工具，還是需要規劃、錯誤恢復與狀態管理的多輪任務）；狀態性（環境是否隨每個動作更新，有狀態的 benchmark 才能揭露漂移、上下文遺失、狀態損壞這些靜態測試看不到的問題）；評測方法（可執行驗證，例如資料庫是否真的更新、測試是否真的通過，是黃金標準；參考答案式評測需要人工維護一份標註答案集；LLM-as-a-Judge 可以填補沒有可執行檢查的空白，但分數在對照一批人工評分驗證之前，都只能算是暫定值）。文章也提到，污染問題已經不只是訓練資料外洩，還包括即時的變形，例如會上網搜尋的 agent 在評測過程中直接查到答案，或是 Hugging Face 上的資料集很快被重新爬進預訓練語料庫；不可被爬取的私有領域評測，天生就不會有這個問題。

📊 **一筆真實 trace：SWE-bench Verified 上的除錯過程**

文章附上一段來自 SWE-bench Verified（真實 GitHub issue、可執行測試驗證）的公開 trace，任務 ID 為 pytest-dev__pytest-5262（trial .2，turn 0 到 4）。使用者／使用者模擬器的指令是「在 /testbed 中完成必要修改，滿足 issue 的要求」，issue 內容是 _pytest.capture.EncodedFile 從底層 buffer 回報的 mode 是 rb+（binary），但它的 write() 只接受 str，導致像 youtube-dl 這類外部程式碼寫入 bytes 時會崩潰。這次評測用的是 OpenHands agent harness，暴露的工具有 terminal、file_editor、task_tracker、finish，平行工具呼叫關閉（每個 turn 只能呼叫一次工具），repo 狀態會跨 turn 保留（是真實的檔案系統與 git，不是模擬）。

trace 顯示：step 1（turn 0）用 terminal 的 find 指令定位到 capture.py，判定為 valid；step 2（turn 1）用 file_editor 檢視整個檔案（超過 400 行），判定為 redundant，因為先用 grep 縮小範圍會更精準；step 3（turn 2）用 terminal 的 grep 搜尋 EncodedFile，判定為 recovered，修正了 step 2 的沒效率；step 4（turn 3-4）用 file_editor 檢視特定行數範圍，準確定位到問題根因（__getattr__ 沒有過濾就直接把 mode 委派給底層 binary buffer），判定為 valid。

🎯 **實務啟示**

如果你正在為自家的 agent 選 benchmark 或搭評測管線，這篇文章給出一個清楚的檢查清單：光報一個「成功率」數字沒有意義，要同時看一致性區間；區分呼叫是否正確跟參數是否正確，才能定位問題在哪；用 E2E 當作上線的放行門檻，但保留 step-level trace 做除錯；比較不同 benchmark 的分數之前，先確認彼此的任務複雜度、狀態性與驗證方法是否對得上，否則就是在比較兩個不同的東西。

🔗 **來源**
- 標題：How to Evaluate AI Agents From Tool Calls to Task Completion
- 作者／機構：Elizabeth Goodman @ NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/how-to-evaluate-ai-agents-from-tool-calls-to-task-completion/

#AIAgents #LLMEval #ToolCalling #BenchmarkDesign #NVIDIA #AgenticAI #SWEBench #MachineLearning #MLOps #EvalMetrics
