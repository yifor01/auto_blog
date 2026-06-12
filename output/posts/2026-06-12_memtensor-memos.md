---
title: MemTensor/MemOS
source: GitHub Trending
url: https://github.com/MemTensor/MemOS
score: 98
model: google/gemma-4-31b-it:free
generated_at: '2026-06-12T20:40:16.505395'
---

📌 【GitHub Trending】MemOS：為 AI Agent 打造的「記憶操作系統」，讓長期記憶不再是黑盒子

目前的 AI Agent 雖然能處理大量資訊，但長期記憶（Long-term Memory）始終是個痛點。大多數方案依賴簡單的向量資料庫（Embedding Store），導致記憶像個黑盒子：你很難精確地編輯、檢查或管理 AI 到底記住了什麼。

MemOS 提出了一個大膽的構想：將記憶視為一個「操作系統 (OS)」，透過統一的 API 來管理 AI 的存儲、檢索與演化。

🤔 **從「向量儲存」轉向「可管理的操作系統」**

傳統的 RAG 或記憶機制往往將資料丟進向量空間，雖然能檢索，但缺乏結構化的管理能力。MemOS 的核心設計理念是將記憶結構化為「圖 (Graph)」，讓記憶變得可視化且可編輯。這意味著記憶不再僅僅是相似度檢索，而是一個可以被精確管理、編輯與刪除的系統。

🧪 **分層演化機制：從痕跡到世界模型的演進**

MemOS 2.0 (Stardust) 引入了一套自我演化的記憶層級設計，讓 AI 的記憶能隨時間與回饋而升級：
- **L1 Trace**：記錄原始的互動痕跡。
- **L2 Policy**：將痕跡轉化為行為策略。
- **L3 World Model**：構建對世界的認知模型。
- **Crystallized Skills**：最終將經驗結晶化為具體的技能。

這種分層設計讓 Agent 不僅僅是「記得」過去，而是能透過回饋機制將經驗轉化為能力。

🚀 **數據實測：精度提升，成本降低**

根據官方數據，MemOS 2.0 在多項記憶評測中表現強勁，且在效率上有顯著優化：
- **精度提升**：相比 OpenAI Memory，準確度提升了 43.70%。
- **評測表現**：在 LongMemEval (+40.43%) 與 PersonaMem (+40.75%) 等指標上大幅領先，尤其在 PrefEval-10 上有極高幅度的提升。
- **成本優化**：透過 LoCoMo 技術，記憶 Token 的使用量降低了 35.24%；若使用 OpenClaw Cloud Plugin，Token 使用量甚至可降低 72%。

💡 **工程實踐：從 Local-first 到雲端同步**

對於開發者而言，MemOS 提供了高度靈活的部署選項，方便快速整合進現有 Agent（如 Hermes Agent 或 OpenClaw）：
- **本地優先 (Local-first)**：提供 `memos-local-plugin`，支持 Docker 部署（需設定 `MEMOS_HOME`），適合對數據隱私要求高的場景。
- **雲端服務 (Cloud Service)**：支持透過 `user_id` 實現多 Agent 之間的記憶共享。
- **整合便捷**：提供 NPM 套件與統一的 API，將存儲、檢索、編輯與刪除整合在單一接口中。

⚠️ **開源專案的整合成本與學習曲線**

由於 MemOS 引入了圖結構記憶與分層演化機制，其配置複雜度會高於簡單的向量資料庫。開發者在部署 Docker 時需特別注意環境變數的設定，且將其整合至現有工作流中，需要重新思考記憶的存取邏輯，而非單純的 API 替換。

🎯 **實務啟示：建構具備「經驗成長」能力的 Agent**

如果你正在開發需要高度個人化、或需要根據用戶反饋持續進化能力的 AI Agent，MemOS 提供了一個從「靜態檢索」轉向「動態演化」的實踐路徑。建議嘗試將其 L1-L3 的分層機制應用在複雜的任務流中，觀察 AI 如何將碎片化資訊轉化為結構化技能。

🔗 **專案連結**
📝 MemOS: Memory Operating System for LLM & AI Agents
🐙 GitHub: https://github.com/MemTensor/MemOS
📦 NPM: 可於 NPM 搜尋 `memos-local-plugin`

你認為 AI Agent 的記憶應該是像資料庫一樣精確，還是像人類一樣模糊且會演化？歡迎在評論區分享你的看法 👇

#AI #LLM #AIAgents #OpenSource #LongTermMemory #MemOS #GitHubTrending #軟體工程
