---
title: "Executable Agentic Memory for GUI Agent"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.12294
score: 116
model: tencent/hy3-preview:free
generated_at: 2026-05-13T20:28:54.984999
---

📌 **可執行Agentic記憶框架**

你以為讓 AI 直接看畫面、一步步點擊就能穩定完成長任務？實際上，當任務跨越多個畫面時，純 LLM 的逐步生成會變得極其脆弱。

🤔 **長 horizon 任務讓純 LLM 步驟生成變得脆弱**  
現代 GUI 代理通常採用模型為中心、逐步互動的範式：每個畫面都需要 LLM 重新解讀 UI 並重新決策動作。這種方式在需要多步驟、長時間序列的自動化任務中容易累積錯誤，導致任務失效。

🧪 **以 Knowledge Graph 為核心的記憶與搜尋框架**  
本文提出 **Executable Agentic Memory (EAM)**，一種結構化的 Knowledge Graph (KG)，將 GUI 規劃從自由形式的生成轉為可靠的「檢索‑執行」流程。記憶的建構採用樣本效率高的管線：  
- 透過 **state-aware DFS** 搜尋狀態空間  
- 利用 **action-group mining** 壓縮多步驟例行程序  

為了高效規劃，文件設計了一個 **value‑guided graph search**：輕量的 Q‑function 模型引導蒙特卡羅樹搜尋 (MCTS) 在 KG 上進行路徑規劃。理論上證明了 Q‑model 的 bias‑consistency，並推導出路徑恢復的樣本複雜度上界。

🔍 **核心發現：性能顯著提升、成本大幅下降**  
在 AndroidWorld 基準上，EAM 優於目前最佳的 UI‑TARS‑7B 基線：**最高達 19.6%** 的成功率提升。同時，相較於 GPT‑4o，**token 成本降低 6×**，平均延遲僅 **2.8 秒**，實現了快速且可靠的長 horizon GUI 自動化。

💡 **深入分析：輕量 Q‑model 如何賦予 MCTS 優勢**  
透過將 Q‑function 作為價值引導，MCTS 能在 KG 中優先探索高回報路徑，從而在保證搜尋效率的同時，理論上保持 bias‑consistency。這意味著即使在有限樣本下，搜尋過程也不會系統性地偏向錯誤路徑，為後續的路徑恢復提供保證。

⚠️ **研究限制：僅基於現有摘要可見的範圍**  
所提供的摘要與評分理由未詳細說明實驗的外部效力（例如其他作業系統或真實機型的適配度）、長期穩真度，或是記憶建構管線在極大規模應用時的擴展瓶頂。這些方面需參考全文或後續工作才能進一步釐清。

🎯 **實務啟示：結構化記憶是降低成本與延遲的關鍵**  
對於需要長序列 GUI 操作的場景（如自動化測試、重複性後台任務），採用類似 EAM 的 Knowledge Graph 檢索‑執行範式，可顯著減少每步的 token 消耗與整體延遲，同時提升任務成功率。工程師在設計 Agentic 系統時，可考慮先建構狀態‑動作圖，再以輕量價值模型導向搜尋，以獲得更穩健且具成本效益的自動化解決方案。

🔗 **論文連結**  
📝 Executable Agentic Memory for GUI Agent  
👤 Zerui Qin, Sheng Yue, Xingyuan Hua, Yongjian Fu, Ju Ren (Tsinghua University; Sun Yat-sen University)  
🔗 https://arxiv.org/abs/2605.12294  

你目前的 GUI 自動化流程是否仍在逐步生成模式？歡迎在留言區分享你的經驗或對結構化記憶的看法 👇

#AI #GUIAgent #AgenticMemory #KnowledgeGraph #MCTS #AndroidWorld #Tsinghua #SunYatSen #自動化 #LLM #技術成長
