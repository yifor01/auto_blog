---
title: "SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2603.24755
score: 108
model: gpt-4o-free
generated_at: 2026-03-28T18:53:41.451996
---

📌 【SlopCodeBench：AI 寫程式的長期迭代能力，真的扛得住嗎？】

你可能覺得 AI 幫你寫程式能省下大量時間，但如果這些程式碼越改越亂、越寫越難維護，這真的值得嗎？最新研究 SlopCodeBench 揭示了一個令人擔憂的真相：AI 在長期迭代開發中的表現遠不如人類，甚至會讓程式碼「質量崩壞」。

🎣 **AI 程式碼問題不在於「能不能跑」，而是「能不能改」**

目前的 AI coding benchmark（如 HumanEval、MBPP）多半只關注「單次解題成功率」：AI 能否產生通過測試案例的程式碼。然而，真正的軟體開發是個「迭代過程」——需求會不斷變更，功能會不斷擴展，程式碼也需要持續維護。

SlopCodeBench 聚焦解決這個痛點：AI 在反覆修改自己程式碼的過程中，能否保持程式碼的可擴展性與架構清晰？答案可能比你想像的更糟。

🤔 **程式碼越補越爛：AI 長期表現的隱憂**

研究團隊設計了一個全新 benchmark，包含 20 個問題和 93 個檢查點，要求 AI 代理在規格不斷變化的情況下，基於自己的舊程式碼進行多次擴展。這些規格並未限制實現細節，而是迫使代理面對架構設計上的權衡。

結果顯示：
- **無一模型能在任何問題上完成端到端解答**，最高檢查點通過率僅 17.2%。
- **80% 的程式碼軌跡出現架構惡化**（Structural Erosion），即複雜度嚴重集中於少數高複雜度函式。
- **89.8% 的程式碼軌跡變得冗長重複**（Verbosity），AI 生成的程式碼比人類多出 2.2 倍的重複內容。

更令人擔憂的是，研究還比較了 48 個開源 Python 專案發現：
- 人類編寫的程式碼品質隨時間保持穩定；
- AI 編寫的程式碼隨著每次迭代，架構崩壞與冗長問題都持續惡化。

🧪 **即使介入輔助，AI 程式碼仍無法根治劣化**

研究人員嘗試通過提示（prompt intervention）來改善 AI 初始輸出程式碼的品質，結果發現初始品質有所提升，但這並未能阻止後續的品質惡化。這說明了目前的 AI 模型在架構設計和迭代開發的基本能力上仍然存在根本性缺陷。

💡 **現有 Benchmarks 的盲點揭開**

這項研究的核心洞察在於：單次解題成功率（pass-rate benchmarks）無法充分衡量程式碼的「擴展韌性」——也就是在多次迭代中，程式碼是否仍然易於維護與修改。SlopCodeBench 提供了一個新視角，能夠更真實地模擬軟體開發的長期需求，填補了現有方法的空白。

⚠️ **研究限制：模型與場景的真實性仍需提升**

儘管 SlopCodeBench 提供了全新思路，但研究仍有一些限制：
- **僅測試了 11 個現有模型**，可能無法涵蓋最新的 generative AI 模型。
- 測試場景基於模擬問題，可能與真實商業軟體開發的複雜性存在差距。

🎯 **對工程師的啟示：AI 寫程式是工具，不是捷徑**

1. **審視 AI 與人類的分工**：AI 工具當前更適合用於簡化重複性任務，而非完全接管軟體設計與架構工作。
2. **適度干預 AI 的輸出**：不要盲目接受生成的程式碼，應該主動進行審查與優化。
3. **推動更好的工具與評估方法**：研究者和業界需要共同努力，設計能捕捉長期迭代挑戰的工具與模型。

🔗 **論文連結**
📝 SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks  
🔗 [HuggingFace 論文連結](https://huggingface.co/papers/2603.24755)

你有使用過 AI 幫助寫程式嗎？你的體驗是增效還是增負擔？留言分享，讓我們一起討論！👇

#AI #CodingAgents #SlopCodeBench #MachineLearning #SoftwareDevelopment #HuggingFace #人工智慧
