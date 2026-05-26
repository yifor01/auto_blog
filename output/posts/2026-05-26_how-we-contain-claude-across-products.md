---
title: "How we contain Claude across products"
source: Anthropic Engineering
url: https://www.anthropic.com/engineering/how-we-contain-claude
score: 89
model: tencent/hy3-preview:free
generated_at: 2026-05-26T21:16:46.286719
---

📌 【Anthropic Engineering】如何在多產品中限制 Claude 的 blast radius  

你以為讓 AI 獲得更多存取權只會帶來生產力提升？  
Anthropic 的實測顯示，權限開大後，內部服務被誤關的風險也在同步上升。  
這正是他們今天必須解決的「爆炸半徑」問題。  

🤔 **AI 能力提升伴隨風險雙升**  
隨著 Claude 在 claude.ai、Claude Code 與 Cowork 等產品中被賦予更多任務，其潛在破壞範圍（blast radius）也隨之擴大。風險由兩部分組成：失敗發生的機率，以及單次失敗可能造成的損害大小。防護措施與模型訓練的進步成功降低了前者，但後者則會隨著能力與存取權的增加而持續成長。  

🧪 **在三個產品中實施 containment 的做法**  
Anthropic 的工程團隊先後在 claude.ai（對話介面）、Claude Code（程式輔助）與 Cowork（協作平台）上部署了防護機制。其中包括：  
- 透過環境控制來限制 agent 能造成的相對損害；  
- 在 Claude Code 中採用 human‑in‑the-loop，每一步動作都要求使用者授權；  
- 持續監測遙測資料，觀察使用者對建議動作的批准比例。  

 **human‑in‑the-loop 並非萬靈藥**  
遙測顯示，使用者大約同意了 93% 的建議動作。這意味著即使有授權機制，仍有約 7% 的操作可能被誤核准，導致非預期行為發生。此外，團隊曾指出，單純依賴人工確認在實務上會變得脆弱，無法完全消除風險。  

💡 **爆炸半徑的兩面性與權衡**  
雖然提升 Claude 的能力會讓爆炸半徑變大，但不部署同樣帶來機會成本。當關鍵系統被加固、防護措施成熟時，即使存在剩餘風險，高實用值的模型也變得適合廣泛發行。這正是他們認為 Claude Mythos Preview 在 2026 年 4 月仍未發布的原因——其 blast radius 被評估為過高，但隨著防護能力提升，未來較有可能開放。  

⚠️ **工程經驗的限制**  
- 所述經驗主要來自內部遙測與產品觀察，未進行對照實驗或統計顯著性檢驗；  
- 人機互動的 93% 同意率僅反映特定使用情境，不同使用者族群或任務類型可能有所不同；  
- 防護措施的效能會隨著模型版本與部署環境變化而需重新評估。  

🎯 **對建置 agentic 系統的實務建議**  
1. 將 blast radius 視為可管理的參數，透過環境隔離與最小權限原則來設定上限；  
2. 在 human‑in‑the-loop 中補充自動化檢查（例如規則引擎或第二層模型），以降低人工疏失的影響；  
3. 持續收集遙測資料，監測使用者同意率與異常行為，以便及時調整防護門檻；  
4. 在關鍵基礎設施完成加固之前，對具高 blast radius 的模型採取漸進式發佈，先在受控環境驗證安全性。  

🔗 **原始參考**  
📝 How we contain Claude across products  
👤 Anthropic Engineering  
🔗 https://www.anthropic.com/engineering/how-we-contain-claude  

你在使用 Claude 或其他 agent 時，是否也設定過類似的「權限上限」？歡迎在留言區分享你的經驗與做法 👇  

#AI安全 #AgenticAI #Claude #Anthropic #爆炸半徑 #人機協作 #工程實務
