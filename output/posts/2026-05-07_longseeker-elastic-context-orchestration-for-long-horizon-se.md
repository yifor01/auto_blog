---
title: "LongSeeker: Elastic Context Orchestration for Long-Horizon Search Agents"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.05191
score: 93
model: tencent/hy3-preview:free
generated_at: 2026-05-07T20:54:57.831286
---

📌 **LongSeeker：彈性上下文編排讓長程搜尋代理更準確**  

你以為讓 AI 記得越多越好？研究顯示，過載的工作記憶反而讓長程搜尋代理更易出錯。  

🤔 **長程搜尋需要「適度遺忘」**  
當代理在推理、呼叫工具與觀察資訊時，中間產生的內容會快速累積。若一味保留所有細節，不僅增加運算成本，也會提升幻覺與錯誤的風險。因此，有效的上下文管理應該是自適應的：根據當前任務的相關性，以不同細節程度保留軌跡的各個部分。  

🧪 **Context-ReAct：五種彈性操作的統一迴路**  
論文提出一個通用的 agentic 範式 —  — Context-ReAct，將推理、上下文管理與工具使用融入同一個迴圈。它提供五種原子操作：  
- **Skip**：直接跳過不相關的片段  
- **Compress**：將已解決的資訊壓縮為摘要  
- **Rollback**：回到先前的狀態以探索其他分支  
- **Snippet**：保留關鍵證據的原始片段  
- **Delete**：刪除無用的分支  

這些操作讓代理能動態重塑工作記憶，既保留重要證據，又控制上下文大小。理論上，**Compress** 算子具有表達完整性，而其他專門算子則提供效率與保真度的保證，以降低生成成本與幻覺風險。  

🚀 **LongSeeker：在 Qwen3-30B-A3B 上微調的長程搜尋代理**  
基於 Context-ReAct，研究團隊以 10k 合成軌跡微調 Qwen3-30B-A3B，得到 LongSeeker。在四個代表性搜尋基準上進行評估：  
- **BrowseComp**：LongSeeker 達到 **61.5%**，顯著優於 Tongyi DeepResearch（43.2%）與 AgentFold（36.2%）  
- **BrowseComp-ZH**：LongSeeker 達到 **62.5%**，優於 Tongyi DeepResearch（46.7%）與 AgentFold（47.3%）  

結果表明，透過主動塑造工作記憶，代理能在長程推理中同時提升可靠性與效率。  

💡 **關鍵洞察：彈性上下文即是「適度遺忘」的藝術**  
高表現不來於記住一切，而是透過 Skip、Compress、Rollback 等操作，在需要時保留證據、在不需要時摘要或刪除。這種「依需求調整細節」的機制，正是降低幻覺與控制成本的核心。  

⚠️ **研究限制：合成資料與基準範圍**  
- 訓練軌跡為合成生成，真實世界的雜訊與分布偏移尚未驗證  
- 基準僅涵蓋 BrowseComp 系列，其他類型的長程任務表現未知  
- 未於論文中強調開放原始碼或工具，限制即時的實務採用  

🎯 **對工程師的實務建議**  
- 在構建長程代理時，考慮將上下文管理設計為可插拔的操作層，而非固定的累積機制  
- 可參考 Context-ReAct 的五種原子操作，先從 Compress 與 Delete 開始實驗，觀察成本與準確度的 trade‑off  
- 若有能力自行合成軌跡，可嘗試以同樣規模的資料微調開源大模型，以驗證彈性上下文是否帶來類似提升  

🔗 **論文連結**  
📝 LongSeeker: Elastic Context Orchestration for Long-Horizon Search Agents  
👤 Yijun Lu, Rui Ye, Yuwen Du, Jiajun Wang, Songhua Liu (Shanghai Jiao Tong University)  
🔗 https://arxiv.org/abs/2605.05191  

你在設計長程 AI 代理時，會如何平衡「記得」與「忘記」？歡迎在留言區分享你的經驗與想法 👇  

#AI #LongHorizonSearch #ContextManagement #AgenticAI #Qwen3 #上海交大 #機器學習 #GenAI
