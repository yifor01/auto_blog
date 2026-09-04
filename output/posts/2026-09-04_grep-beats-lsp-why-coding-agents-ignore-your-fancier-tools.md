---
title: Grep beats LSP? Why coding agents ignore your fancier tools
source: Hacker News
url: https://www.agentconnect.md/blog/grep-beat-lsp-harness/
model: claude-code/sonnet
generated_at: '2026-09-04T19:49:09.202039'
score: 94
---

📌 為什麼 Coding Agent 寧願用 grep，也不太碰 LSP？

TL;DR：實測顯示 Claude 系列模型在自由選擇時，多數情境仍偏好 grep，關鍵在工具回傳的資訊形狀，而非語意精準度。

如果有一個檢索工具能精確分辨「這是真正的函式呼叫」還是「註解裡剛好出現同一個字」，照理說 agent 應該優先選用它。但一項針對 coding agent 的小型研究發現，情況並非如此：在多數任務中，agent 主動選擇語意導航（LSP-backed navigation）的比例甚至只有 0% 到 6%。

🤔 精準的工具，為什麼沒被優先選用

作者比較了兩種程式碼檢索方式：grep 進行的是文字比對的 lexical search；測試中的 LSP-backed 工具則透過 references、definitions、document symbols 做語意導航，能區分真正的函式呼叫與純文字巧合。研究涵蓋三個 Claude 模型（Opus 4.8、Sonnet 4.6、Haiku 4.5）、多個 Python 與 TypeScript 專案，並僅在兩種方法都成功完成任務時才計算 token 使用量，避免「提早失敗反而顯得省 token」的評估誤差。

🧩 路由行為隨任務類型改變，不是單純的習慣

在簡單的程式碼定位任務上，三個模型主動選用語意工具的比例都極低（0% 到 6%），若強制走語意優先路徑，成功率甚至從 100% 掉到 89%。

但在「找出所有呼叫者」這類 reference-completeness 任務中，情況完全不同：模型主動選用語意導航的比例來到 45% 到 57%，且 LSP 路徑的 precision 達到 1.00，明顯高於 grep 的 0.76。不過兩種方法的 recall 都停留在約 0.66，代表語意導航並沒有多找到更多真正的呼叫，瓶頸出在 agent 搜尋的徹底程度，而非檢索精準度本身。

| 任務 | Opus 4.8 | Sonnet 4.6 | Haiku 4.5 |
|---|---|---|---|
| Localization | 0% | 4% | 6% |
| Reference-completeness | 45% | 50% | 57% |
| Multi-file rename | 3% | — | — |

📊 同一個語言，兩個專案，結論完全相反

研究也發現，程式碼庫本身的「文字雜訊」程度，比程式語言是否為靜態型別更能預測語意導航的價值：

| 專案 | 語言 | grep precision | ΔF1（LSP − grep） | Token 成本變化 |
|---|---|---|---|---|
| remeda | TypeScript | 1.00 | +0.000 | +16% |
| hono | TypeScript | 0.51 | +0.246 | −12% |
| requests | Python | 0.76 | +0.072 | +19% |

在乾淨的 remeda 專案上，grep 本身就能正確解析所有參照，語意導航幾乎沒有增益；但在雜訊較多的 hono 專案上，語意導航帶來 +0.246 的 F1 提升，同時還省下 12% 的 token。

💡 真正的關鍵：回傳的內容形狀，不只是檢索是否精準

作者接著做了一個關鍵實驗：原本測試的 LSP 工具只回傳位置（檔案路徑、行號、欄號），agent 必須再開檔案才能看到程式碼；而 grep 通常會直接附上匹配的那一行文字。當作者把語意導航的輸出改成同樣附帶原始程式碼片段後，rename 任務的 pass@1 從 0.67 提升到 0.83，後續額外開檔次數則從 15.2 次降到 3.2 次（比 grep 自己的 4.3 次還低）。整個過程中語意檢索後端完全沒變，只是回傳資訊的形狀不同。

| 方式 | pass@1 | Site recall | Tokens | 後續讀檔次數 |
|---|---|---|---|---|
| grep | 1.00 | 1.000 | 2,451 | 4.3 |
| LSP（只回位置） | 0.67 | 0.930 | 4,131 | 15.2 |
| LSP（附帶內文） | 0.83 | 0.958 | 3,336 | 3.2 |

這呼應了 Anthropic 在《Writing effective tools for agents》中強調的觀點：工具是給非確定性 agent 使用的介面，回傳的上下文本身就是設計的一部分。一個語意上完全正確的工具，若每次結果都需要額外幾步才能解讀，仍會拖累整體工作流程。

⚠️ 結構性差異，也是 grep 佔優勢的原因之一

作者也指出，grep 的優勢不完全來自模型的訓練慣性，還有結構性原因：語意參照（semantic reference）只是文字出現位置的子集合。例如 rename 任務可能也需要更新註解、docstring、設定檔或字串，而 find_references 依設計不會回傳這些內容，grep 卻可以。因此即使模型對 LSP 工具訓練得再熟練，在需要「全文字層級」修改的任務上，grep 仍可能是更合適的檢索工具。作者也坦言，訓練資料分布是否影響模型的工具偏好，仍只是與觀察結果一致的假設，本研究並未直接操弄訓練資料來證明因果關係。

🎯 對打造 agent 平臺的實務啟示

這篇研究的重點不是「LSP 沒用」，而是工具介面設計必須考慮 agent 實際如何使用它：回傳的上下文要足夠讓下一步能直接行動，格式要貼近模型熟悉的互動模式。與其單獨評估檢索後端的精準度，更該評估「這個工具回傳的內容，能不能讓 agent 少走幾步」。對正在設計 agent 工具鏈的工程師來說，這代表 tool 的輸出格式本身值得像 API 設計一樣被嚴肅對待。

🔗 來源
- 標題：Grep beats LSP? Why coding agents ignore your fancier tools
- 作者／機構：kaonashi-tyc-01（Hacker News）
- 連結：https://www.agentconnect.md/blog/grep-beat-lsp-harness/

#AIAgents #CodingAgents #LLM #LSP #DeveloperTools #SoftwareEngineering #ToolDesign #ClaudeAI #CodeSearch #AgentHarness
