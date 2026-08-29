---
title: '[AINews] OpenAI shuts off Cursor'
source: Latent Space
url: https://www.latent.space/p/ainews-openai-shuts-off-cursor
model: claude-code/sonnet
generated_at: '2026-08-29T12:05:24.859297'
score: 57
---

📌 OpenAI 切斷 Cursor：AI 圈的站隊戰正式開打

TL;DR：Cursor 被 SpaceX 收購後，OpenAI 隨即比照 Anthropic 對 Windsurf 的做法切斷存取，理由是「與 Musk 旗下公司往來的違約經驗」。

一年前，Cursor 還站在 GPT-5 發表影片的舞臺上；如今 Cursor 被 SpaceX 收購剛滿一週，OpenAI 就做出了 Anthropic 當初在 Windsurf 疑似被 OpenAI 收購時做過的同一件事——切斷存取。這不只是一次商業決策,更是 AI 生態圈站隊態勢愈趨明顯的一個訊號。

🤔 **一場醞釀已久的恩怨**

根據 Latent Space 的 AINews 彙整，OpenAI 官方部落格給出的主要理由是「我們與 Elon Musk 旗下公司違反合約的經驗」。這延續了雙方領導人多年的公開摩擦：Musk 曾是 OpenAI 創立初期的關鍵資助者，雙方今年稍早還打過一場最終敗訴的官司。從這個脈絡看，這次切斷存取雖然突然，卻並非完全無跡可循。

📊 **Cursor 的回應與市場現況**

Cursor 目前的回應偏向外交辭令：一方面強調 OpenAI 只佔其流量的 5%，另一方面並未接受這是最終定局。與此同時，市場格局也早已今非昔比：GPT-5.6 如今已是能與 Claude 5 系列並駕齊驅的正式編程對手，而「CursorSpaceXai」正在力推 Grok 4.6，Grok 4.6 也是 xAI 首次真正站穩腳步的編程模型，Grok Bot 更被視為 Codex/ChatGPT 的可行競爭者。換句話說，OpenAI 與 Cursor 雙方都已經打拚到「彼此不再需要對方也能被認真看待」的位置，這次切斷存取某種程度上正是雙方各自成功的證明。

💡 **同一週的其他重要動態**

除了 OpenAI 與 Cursor 的紛爭，同一週的 AI 圈還有幾件事值得留意：

| 模型 | 總參數／啟用參數 | Context | 重點 |
|---|---|---|---|
| GLM-5.3（Z.ai） | 744B / 40B | 1M，最大輸出 128K | 定位為 agentic coding 與 cyber defense；vLLM day-0 支援 |
| Hy4-preview（Tencent） | 770B / 49B | 1M | 據稱可並行協調多個 Codex session 做研究工作流；Code Arena WebDev 排名躍升 115 分 |
| Qwen3.8-Flash（Alibaba） | 125B / 6B | 1M | 定價約 $0.15／1M input、$0.47／1M output；早期回報對 FP8 穩定性看法不一 |

推論系統方面，vLLM 針對投機解碼（speculative decoding）做了一輪跨模型家族（Gemma、Qwen、Kimi、MiniMax）在 AMD MI300X/MI355X 上的實測比較，結論是 MTP、EAGLE-3、DFlash、DSpark 等方法沒有單一贏家，最佳選擇取決於模型家族、工作負載與投機深度，應被當成一個持續調整的參數面向，而非一次性開關。Agent 評測則開始從「答案品質」轉向「驗證任務是否真的完成」：Alibaba Accio 開源的 CommerceAgentBench 涵蓋採購、上架、營運、履約、售後 107 個任務，最佳測試結果也只通過 66 題（61.7%），顯示目前的 agent 距離可靠的商業自動化仍有相當距離。

⚠️ **仍有不確定性**

Cursor 官方尚未接受這次切斷是最終決定，後續走向仍待觀察；Qwen3.8-Flash 在 FP8 精度下的多輪對話追蹤問題，也仍有社群回報混合結果，並非一致正面。

🎯 **實務啟示**

如果你的產品或內部工具鏈同時依賴多家模型供應商，這次事件是一個提醒：模型 API 的可用性可能受供應商之間的商業或政治關係影響，而非純粹的技術或定價考量,建議在架構上保留切換供應商的彈性。另外，投機解碼與 agent 評測的最新結果都指向同一個方向：這些能力愈來愈需要被當成持續調整、持續驗證的系統元件，而非一次性導入就能長期穩定的功能。

🔗 **來源**
- 標題：[AINews] OpenAI shuts off Cursor
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-openai-shuts-off-cursor

#OpenAI #Cursor #SpaceX #AIIndustry #Grok #GLM #Qwen #SpeculativeDecoding #AgentBenchmark #AICompetition
