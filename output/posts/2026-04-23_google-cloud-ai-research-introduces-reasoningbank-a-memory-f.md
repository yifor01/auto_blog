---
title: "Google Cloud AI Research Introduces ReasoningBank: A Memory Framework that Distills Reasoning Strategies from Agent Successes and Failures"
source: MarkTechPost
url: https://www.marktechpost.com/2026/04/23/google-cloud-ai-research-introduces-reasoningbank-a-memory-framework-that-distills-reasoning-strategies-from-agent-successes-and-failures/
score: 102
model: tencent/hy3-preview:free
generated_at: 2026-04-23T20:01:21.453727
---

📌 **【Google Cloud AI 新突破】ReasoningBank：讓 Agent 從成功與失敗中學會「為什麼」**  

你有沒有發現，現在的 AI 代理人每次執行任務時，都像是第一次見到這件事？即使剛剛在同樣的網站上踩過相同的坑，它仍會重蹈覆轍。這背後的根本問題，就是「記憶力」——大多數 Agent 只會把行為原始紀錄保存起來，卻不會抽取出失敗與成功的推理原因。  

🤔 **Agent 仍在「忘記」：現有記憶方式的盲點**  

- **Trajectory Memory**（Synapse）只存原始行為軌跡——每一次點擊、滑動、輸入都被記錄。雖完整，卻噪聲太多、資訊過於冗長，難以直接在新任務中重用。  
- **Workflow Memory**（Agent Workflow Memory, AWM）則只抽取成功執行的步驟流程。結果是：**失敗的寶貴訊號全被丟棄**，而 Agent 在真實環境中失敗的次數遠高於成功次數。  

🔬 **ReasoningBank 的三階段閉環記憶流程**  

1. **Memory Retrieval** – 任務開始前，以嵌入向量相似度搜尋取回最相關的 k 個記憶項目（預設 k=1）。  
2. **Memory Extraction** – 從取回的原始紀錄中萃取「為什麼成功／失敗」的推理策略，而不是僅保留表面行為。  
3. **Memory Consolidation** – 把抽象出的策略以可重用、通用的形式寫回記憶庫，供未來任務直接引用。  

> **實驗發現**：取回多於一筆記憶會降低效能，成功率從 49% 直接跌至更低，說明過多噪聲反而干擾了推理。  

💡 **從「做」到「思考」的跨越**  

ReasoningBank 不只是把「做過什麼」寫進 Prompt，而是把「為什麼這樣做」寫進 Prompt。這讓 Agent 在新情境下能夠：

- 快速套用過去失敗的教訓，避免重蹈覆轍。  
- 從成功案例中抽象出通用策略，提升跨任務遷移能力。  
- 以最少的上下文（k=1）即獲得顯著效能提升，降低 Prompt 長度與計算成本。  

⚠️ **研究限制與未解決問題**  

- 目前僅在單一任務類型（Web 瀏覽）上進行驗證，尚未測試於多模態或長期任務的持續效能。  
- 記憶抽取的策略生成仍依賴手工設計的提示，未完全自動化，可能受限於提示工程的品質。  
- 大規模部署時的記憶庫大小與檢索效率尚未公開評估。  

🎯 **對工程師的實務建議**  

1. **先行試用開源原型**：ReasoningBank 已釋出原型程式碼，將其作為現有 Agent 流程的插槽，觀察成功率變化。  
2. **控制檢索數量**：根據實驗結果，保持 k=1 或微調至最小可用數量，避免過多上下文干擾。  
3. **結合失敗分析工具**：在自己的系統中加入失敗日志的自動標註，讓 ReasoningBank 能夠更完整地抽取失敗推理。  

🔗 **論文與資源**  
📝 *ReasoningBank: A Memory Framework that Distills Reasoning Strategies from Agent Successes and Failures*  
👤 作者：Asif Razzaq 等（Google Cloud AI, UIUC, Yale）  
🔗 文章連結： https://www.marktechpost.com/2026/04/23/google-cloud-ai-research-introduces-reasoningbank-a-memory-framework-that-distills-reasoning-strategies-from-agent-successes-and-failures/  

💬 你在開發或使用 AI 代理人時，有遇過類似「每次都忘記上次失敗」的情況嗎？不妨分享你的經驗，或直接在下方討論如何把 ReasoningBank 融入你的工作流！  

#AI #AgentMemory #ReasoningBank #GoogleCloudAI #MachineLearning #PromptEngineering #AIResearch #技術分享  
