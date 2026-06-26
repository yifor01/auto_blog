---
title: 'OpenBioRQ: Unsolved Biomedical Research Questions for Agents'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.21959
score: 94
model: google/gemma-4-31b-it:free
generated_at: '2026-06-26T20:04:59.653958'
---

📌 OpenBioRQ：測試 AI Agent 能否在「無標準答案」的生物醫學研究中生存

TL;DR：新基準 OpenBioRQ 揭露 AI Agent 在面對未解決的生物醫學問題時，常出現引用錯誤與推理失效。

當我們習慣於用有標準答案的 Benchmark 來評估 LLM 時，現實世界的科研卻截然不同：許多問題根本沒有答案。如果一個 AI Agent 在找不到答案時依然「堅稱」自己找到了，這在生物醫學領域將導致嚴重的錯誤導向。

🤔 **挑戰「無答案」的生物醫學研究問題**

OpenBioRQ 建立了一個全新的評估基準，專門測試 Agentic models 處理「未解決研究問題」的能力。與傳統問答不同，這些問題沒有預設的答案金鑰 (answer keys)，目的是檢驗模型在面對未知領域時的誠實度與精準度。

🧩 **檢驗來源驗證與虛假引用的能力**

該基準的核心在於評估模型在以下兩個維度的表現：
1. **來源驗證**：模型是否能正確驗證其檢索到的資訊來源。
2. **避免虛假引用**：在沒有答案的情況下，模型是否會捏造引用文獻（False Citations）來掩蓋知識缺口。

📊 **檢索增強推理與工具使用顯著失效**

研究結果顯示，目前的 Agentic models 在處理這類任務時表現不佳，尤其在以下兩點出現顯著失敗：
- **檢索導向推理 (Retrieval-grounded reasoning)**：即使提供了檢索工具，模型仍無法將檢索到的資訊有效轉化為正確的推理過程。
- **工具使用 (Tool usage)**：在呼叫工具獲取資訊與分析資料的過程中，存在明顯的執行失效。

🎯 **實務啟示：建立 AI 科研 Agent 的「誠實機制」**

對於開發生物醫學 AI Agent 的工程師而言，這項研究提醒我們：單純增加 RAG (Retrieval-Augmented Generation) 的檢索量並不夠。更關鍵的挑戰在於如何讓模型在「找不到答案」時能正確識別並回報，而非透過虛假引用來維持對話的流暢度。在醫療與科研的高風險場景中，「承認不知道」比「給出錯誤答案」具有更高的工程價值。

🔗 **來源**
- 標題：OpenBioRQ: Unsolved Biomedical Research Questions for Agents
- 連結：https://huggingface.co/papers/2606.21959

#AI #Biomedical #LLM #Agent #Benchmark #RAG #Bioinformatics #Reasoning #FactChecking #OpenBioRQ
