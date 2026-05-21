---
title: "CALMem : Application-Layer Dual Memory for Conversational AI"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.20724
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-21T20:47:18.819766
---

📌 **CALMem：應用層雙記憶架構，讓 LLMs 擁有 virtually 無限對話上下文（無需模型改動）**

你有沒有遇過 AI 聊天中途「忘記」之前說的內容？當上下文被壓縮時，那些寶貴的對話歷史就永遠消失了。

🤔 **固定視窗極限了對話的連續性**  
大型語言模型受限於固定長度的 context window。當對話超過此限制時，系統會進行 compaction（壓縮），被壓掉的對話輪次會被永久捨棄；當對話結束時，所有記憶又會歸零。現有的做法—擴大視窗、檢索增強生成（RAG）或類似 MemGPT 的記憶增強架構—要麼需要改動底層模型、要麼造成供應商綁定、要麼無法解決壓縮後連續性的問題。

🧪 **應用層的雙記憶設計**  
CALMem（Conversational Application‑Layer Memory）提出一種純應用層的雙記憶架構，無需更動底層 LLM。其核心包含兩個互補的記憶子系統：  
1. **情景記憶層**：以滑動視窗的向量嵌入保存對話歷史，使得即使被壓縮掉的輪次仍可透過向量檢索找回。  
2. **語義記憶層**：由代理人可寫入的結構化事實庫，儲存較為穩定的知識或使用者偏好。  

為了在每輪對話中注入相關過去資訊，文中設計了一個名為 **MOIM（Message of Injected Memory）** 的 token‑budget‑adaptive 注入機制。MOIM 會根據當前 context 壓力動態調整注入深度：context 越緊湊，注入的過去資訊越少；context 較寬鬆時，則可注入更多相關歷史。這樣的設計使得系統能夠在不改動模型的前提下，實現「virtually unbounded effective context」。

🔑 **關鍵貢獻： intra‑session 檢索**  
與先前工作不同，CALMem 能在同一個對話 session 內檢索那些已被 compaction 移除的輪次，彌補了既有記憶增強方法在壓縮連續性上的空白。

💡 **架構與實作特點**  
- 整個系統以純應用層方式實作於生產環境的 Rust 程式碼基礎，故具有供應商無關（provider‑agnostic）的特性。  
- 當功能關閉時，系統會自然退化為原始 LLM 行為，額外開銷為零。  
- 作者在論文中詳細說明了架構決策、設計權衡以及效能特徵，並分析了每項實作選擇背後的 trade‑off。

⚠️ **說明的限制（基於論文所提供資訊）**  
- 論文著重於架構概念與實作細節，未在此摘要中提供具體的基準測試數據或人類評估結果。  
- 作為應用層方案，其效能會受到底層嵌入模型與檢索回覆品質的影響，這在實際部署時需要額外調校。  
- 零開銷的退化機制假設在關閉狀態下不會額外佔用資源，但在高流量情境下仍需監測記憶體與延遲表現。

🎯 **對工程師的實務啟示**  
- 若您正在構建對話助理且需要更長的記憶跨度，CALMem 提供了一種「即插即用」的選項，無需重新訓練或鎖定特定模型供應商。  
- 透過開關切換，您可在需要最大吞吐時關閉記憶功能，恢復原始 LLM 的延遲與成本。  
- 該設計鼓勵開發者思考如何在不改動模型的前提下，透過外部記憶層解決上下文限制問題——這正是當前 AI 社群正在積極探索的方向。

🔗 **論文連結**  
📝 CALMem: Application‑Layer Dual Memory for Conversational AI  
👤 Rajendra Narayan Jena, Rajan Padmanabhan, Sankar Arumugam @ Infosys Limited  
🔗 https://arxiv.org/abs/2605.20724  

如果你曾為 AI 聊天的「短記憶」感到困擾，歡迎在留言區分享你的看法或實作經驗 👇

#AI #ConversationalAI #LLM #MemoryArchitecture #Infosys #Rust #機器學習 #自然語言處理
