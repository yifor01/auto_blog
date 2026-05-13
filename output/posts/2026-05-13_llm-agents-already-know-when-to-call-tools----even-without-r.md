---
title: "LLM Agents Already Know When to Call Tools -- Even Without Reasoning"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.09252
score: 97
model: tencent/hy3-preview:free
generated_at: 2026-05-13T20:55:33.780622
---

📌 **LLM Agents Already Know When to Call Tools -- Even Without Reasoning**

你以為 LLM 只有在明確被要求時才會呼叫工具？實際上它早已在內部「知道」該不該用工具，只是不願意付諸行動。

🤔 **模型內部已具備工具必要性的感知**  
When2Tool 基準測試揭示，LLM 能從隱藏狀態中預測何時需要調用外部工具，但卻常常未能根據這項預測執行實際的工具呼叫。

🧪 **透過基準測試發現認知與行動的脫節**  
研究團隊設計了 When2Tool 基準，系統地檢測模型在各種任務下對工具必要性的內部判斷與實際行動之間的一致性。結果顯示，模型的內部預測準確度較高，但實際呼叫工具的頻率卻顯著低於預期。

📊 **Probe&Prefill 方法可減少近半不必要的工具呼叫**  
基於上述發現，研究提出 Probe&Prefill 技術：先以輕量探測（Probe）捕捉模型隱藏狀態中的工具需求訊號，再在適當時刻預填（Prefill）相應的工具呼叫觸發條件。實驗表明，此方法能將不必要的工具呼叫減少約 48%，同時僅造成極小的準確度下降。

💡 **內部知覺與外部行動的脫節是效率瓶頸**  
模型能夠「知道」何時需要工具，卻未能將此知覺轉化為行動，說明現有的決策機制在工具使用上存在斷層。Probe&Prefill 透過在隱藏狀態層面進行早期偵測與補償，彌補了這個斷層，從而在不犧牲任務表現的前提下降低計算成本。

⚠️ **基準設計限制與方法適用範圍尚需進一步驗證**  
目前的結論主要建立在 When2Tool 基準的特定任務集合上，不同工具類型或更複雜的多步驟代理場景中的表現尚未詳細探討。此外，Probe&Prefill 的實施需額外的隱藏狀態探測步驟，在資源受限的環境中可能帶來額外開銷。

🎯 **在部署 LLM 代理時，可先考慮內部需求偵測機制**  
- 開發者可在模型推論管線中加入輕量的探測模組，以捕捉工具必要性的早期訊號。  
- 透過 Prefill 動作，將偵測到的需求轉換為精準的工具呼叫觸發條件，減少無效的 API 調用。  
- 此策略特別適合對成本敏感且工具呼叫頻繁的應用，例如代理式搜尋、資料增強或自動化工作流程。

🔗 **論文連結**  
📝 LLM Agents Already Know When to Call Tools -- Even Without Reasoning  
🔗 https://huggingface.co/papers/2605.09252  

你在設計 LLM 代理時，是否也曾觀察到模型「知道」但「不做」的情況？歡迎在留言區分享你的經驗與看法 👇

#LLM #Agent #ToolUse #AI_Efficiency #HuggingFace #ProbeAndPrefill #MachineLearning #AIResearch
