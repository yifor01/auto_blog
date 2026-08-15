---
title: Maximizing the value of your Claude Code sessions
source: Claude Blog
url: https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions
model: nvidia/nemotron-3-ultra-550b-a55b:free
generated_at: '2026-08-15T06:14:33.727612'
pinned: true
---

📌 Anthropic 官方教學：如何讓 Claude Code 的每個 Token 都花在刀口上

TL;DR：官方揭露 Token 計費細節與快取機制，六個指令習慣能大幅降低無效上下文與成本。

Claude Code 等代理式編碼工具改變了開發成本結構：同一個修復任務，依據操作習慣可能相差數倍 Token。Anthropic 官方部落格近日發文，從模型選擇、輸入輸出定價、Prompt Caching 原理三個維度拆解成本來源，並給出六條可立即套用的操作建議。

🎣 **同一個 Bug，為何你花的 Token 比別人多？**

傳統編輯器是「平價制」，修一個測試或五十個成本相同。但 Claude Code 依實際推理用量計費：同樣修復一個測試，有的 Session 只讀兩個檔案就搞定；有的卻先 grep 全倉庫、讀十幾個無關檔案，每一輪對話還得把早餐前讀進去的上下文一起帶著跑。結果相同，帳單卻天差地遠。

🧩 **Token 價格由三個變數決定**

1. **模型大小**：模型越大，對輸入與輸出 Token 的單位運算成本越高。建議：真正困難、模糊的任務用大模型；常規工作換小模型。
2. **輸入 vs 輸出**：推理分 Prefill（讀取請求與上下文）與 Decode（逐 Token 生成輸出）兩階段。Decode 佔用 GPU 時間久得多，因此輸出 Token 價格約為輸入的 5 倍。思考 Token 也屬輸出，`/effort` 等級直接控制單輪思考量。
3. **Prompt Caching**：若請求前綴與上一輪完全一致，伺服器可直接讀取快取狀態，讀取價格僅為輸入的 0.1 倍。寫入快取單價略高（最多 2x），但只發生一次，後續每輪皆享 0.1x 優惠。Claude Code 自動管理快取，**但切換模型或 effort 等級會打破快取鏈**，導致成本暴增。

📊 **六個立即生效的省 Token 習慣**

| 指令 / 動作 | 核心效果 | 關鍵原理 |
|-------------|----------|----------|
| `/clear` 在任務間執行 | 清除無關歷史上下文 | 避免無關 Token 進入下一輪 Prefill |
| 先跑 `/model`、`/effort` 定調 | 鎖定模型與思考強度 | 防止中途切換導致快取失效 |
| `@檔案路徑` 替代口述檔名 | 直接附加檔案內容 | 省去 Read 呼叫或搜尋成本 |
| 嘈雜指令加 quiet flag 或丟給 subagent | 隔離大量輸出 | 指令輸出同樣會佔用對話上下文 |
| 新 Session 跑一次 `/context` | 檢視已載入內容 | 移除不必要的 `CLAUDE.md`、MCP 定義 |
| 離開鍵盤前 `/compact` | 壓縮對話歷史 | 快取一小時後過期，趁熱打鐵摘要更便宜 |

💡 **深入分析：快取鏈的脆弱性與實戰意義**

文章以「修復 utils.test.ts」為例逐輪拆解：五個 Request 全含完整對話歷史，但只有最新增量（Read 呼叫、檔案內容、Edit 結果、測試輸出）按完整輸入價計費，其餘皆為 0.1x 快取讀取。這意味著**保持請求前綴不變是低成本的關鍵**——任何改動系統提示、工具定義、`CLAUDE.md` 順序，甚至中途換模型，都會強制整條鏈重新 Prefill。

訂閱制用戶雖不直接見到單價，但同樣受限於配額扣除邏輯；壓縮 Token 用量等同延長可用額度。

🎯 **實務啟示：把「省 Token」內化為肌肉記憶**

1. **Session 衛生**：把 `/clear`、`/compact` 當成 Git commit 前的 `git status` 一樣自然。
2. **決策前置**：開 Session 先跑 `/model` `/effort` 確認預設值，避免「順手改模型」炸掉快取。
3. **上下文極簡主義**：`/context` 定期檢視，能砍的 `CLAUDE.md` 區塊、MCP 工具全砍掉；檔案用 `@` 直給，別讓模型去找。
4. **噪音隔離**：大量 log、建置輸出丟 subagent 或加 quiet flag，別讓主對話變成垃圾場。

🔗 **來源**
- 標題：Maximizing the value of your Claude Code sessions
- 作者／機構：Lydia Hallie @ Anthropic
- 連結：https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions

#ClaudeCode #Anthropic #LLM #TokenOptimization #PromptCaching #DeveloperTools #AIEngineering #CostOptimization #CodingAssistant #Productivity
