---
title: "Claude Code's source just leaked — I extracted its multi-agent orchestration system into an open-source framework that works with any LLM"
source: r/LocalLLaMA
url: https://www.reddit.com/r/LocalLLaMA/comments/1s8xj2e/claude_codes_source_just_leaked_i_extracted_its/
score: 98
model: gpt-4o-free
generated_at: 2026-04-01T12:30:08.731967
---

📌 **Claude Code 多智慧代理協調層被開源，可與任意 LLM 搭配使用**

近日在 r/LocalLLaMA 看到貼文：Claude Code 的完整原始碼透過 source map 外洩，涵蓋 500K+ 行 TypeScript——查詢引擎、工具系統、協調模式、團隊管理等皆一併曝光。作者 JackChen02 表示，他專注研究其中的多智慧代理協調架構（目標拆解為任務、團隊系統、訊息總線、具依賴解析的任務排程器），並從零重新實作這些模式，打造出一個獨立的開源框架，宣稱可與任何 LLM 互通。

🤔 **洩漏的原始碼提供了研究頂級代理框架的罕見機會**

Claude Code 作為 Anthropic 推出的程式輔助工具，其內部設計多被業界視為構建複雜 AI 工作流的參考範例。然而，因為原始碼長期封閉，外界難以直接考察其協調層如何實現目標分解、任務依賴管理與跨代理訊息傳遞。此次外洩讓研究者得以細看這些關鍵組件，進而評估其概念是否可被抽象化、重用於其他模型。

🧪 **從零重建協調層，專注於可插拔的多智慧代理架構**

作者提取了 Claude Code 中負責「協調器」的核心元件：目標分解模組、團隊管理結構、訊息總線（message bus）以及帶有依賴解析的任務排程器。這些元件被重新用 TypeScript 實作，並刻意去除所有與 Claude 特有的依賴（例如特定的工具鏈或提示模板），使得得到的框架僅保留協調邏輯，理論上可以插入任何支援函式呼叫或工具使用的 LLM。

🔑 **核心貢獻：將頂級代理協調模式開源、LLM‑agnostic**

- **協調器**：接受高階目標，產生任務圖（DAG），負責依賴追蹤與調度。
- **團隊系統**：允許註冊多個代理實例，每個代理可具備不同的工具集或提示策略。
- **訊息總線**：提供發布/訂閱機制，代理間透過標準化訊息交換狀態與結果。
- **任務排程器**：根據依賴關係與資源狀態動態調整執行順序，支援重試與回滾。

這些實作均在作者提供的倉庫中可見，並附有基本使用範例，示範如何將框架掛載於 OpenAI、Llama 或其他本地模型上。

💡 **開源讓先進協調概念觸手可及，但仍需注意實作細節**

將 Claude Code 的協調層抽象出來，意味著開發者不必從零開始設計任務分解與依賴管理的邏輯，可直接專注於代理的具體行為（例如工具實作或領域知識注入）。這對於快速構建多代理工作流（如自動化程式除錯、跨步驟資料處理）具有實際誘因。

然而，作者並未在貼文中提供效能基準或與原始 Claude Code 的行為比較，亦未說明框架在極端規模（數千個代理、深層依賴圖）下的穩定性。因此，雖然概念已被證實可行，但在投入生產環境前仍建議進行壓力測試與客製化調整。

⚠️ **僅重建協調層，未涵蓋其他原始元件（如查詢引擎、工具系統）**

貼文清楚指出，作者的工作專注於「多智慧代理協調層」——即目標分配、訊息傳遞與任務排程。原始 Claude Code 尚包括查詢引擎、內建工具鏈、使用者介面等，這些部分並未被移植或開源。若欲獲得完整的 Claude Code 體驗，仍需自行補充或尋找替代實作。

🎯 **實務建議：先評估框架與自身 LLM 的介面相容性，再逐步擴充代理能力**

1. 檢查所使用的 LLM 是否支援工具呼叫或函式執行（如 OpenAI 的 function calling、Llama.cpp 的工具插件）。
2. 按照倉庫的 README 將協調器、訊息總線與團隊管理掛載至所選模型的包裝層。
3. 從簡單的單任務代理開始，觀察訊息流與狀態同步是否符合預期。
4. 逐步加入多個具備不同工具的代理，測試任務分解與依賴解析的表現。
5. 在正式部署前，針對錯誤處理、超時與重試機制進行單元與整合測試。

🔗 **資料來源**
📌 Reddit 貼文：https://www.reddit.com/r/LocalLLaMA/comments/1s8xj2e/claude_codes_source_just_leaked_i_extracted_its/
👤 作者：JackChen02
🧩 框架倉庫（如貼文中所述）：於該 Reddit 貼文內的連結中可取得（未在此另行提供，請參考原始貼文）。

你是否已嘗試使用此開源框架來搭建自己的多智慧代理系統？歡迎在留言區分享經驗或遇到的挑戰 👇

#AI #LLM #MultiAgent #ClaudeCode #OpenSource #AgentFramework #LocalLLaMA #JackChen02
