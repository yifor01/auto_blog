---
title: "Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.15871
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-05-18T20:19:26.132699
---

📌 【Meta FAIR 最新研究】AI 代理自主設計神經網路架構，超越 Llama 3.2  

🎣 你以為只靠人類設計的 Transformer 已經是極限？Meta 最新研究讓 31 個 AI 代理在 24 小時內自行搜尋並實作新架構，結果竟…  

🤔 **當人類設計遇上瓶頸，AI 代理能否接過神經網路架構的接力棒？**  
隨著大型語言模型的規模與複雜度不斷提升，手動設計新架構的成本日益高昂。研究團隊提出一個問題：是否能讓 LLM 代理像研究員一樣，自動探索並實作出優於現有基線的神經網路？  

🧪 **31 個 LLM 代理、24 小時預算，分層搜尋與實作**  
論文提出雙框架方法：  
- **AIRA-Compose**：由 11 個代理在 24 小時的計算預算下，探索基礎運算原始塊，評估百萬參數級候選架構，並將優秀設計外推至 350M、1B、3B 規模。  
- **AIRA-Design**：由 20 個代理負責撰寫新穎的注意力機制（以處理長程依賴）以及高效能的訓練腳本。  

這兩個階段共同產生了兩個架構家族：AIRAformers（基於 Transformer）與 AIRAhybrids（Transformer‑Mamba 混合）。  

🔍 **核心發現：AIRAformers 與 AIRAhybrids 在 1B 規模下，準確率提升 2.4%~3.8%，擴展速度快上 54%~71%**  
- 在 1B 參數規模的預訓練中，AIRAformer‑D 與 AIRAhybrid‑D 分別比 Llama 3.2 高 2.4% 與 3.8%的下游任務準確率。  
- 就擴展效率而言，AIRAformer‑C 的擴展速度比 Llama 3.2 快 54%，比 Composer 最佳 Transformer 快 71%；AIRAhybrid‑C 則比 Nemotron-2 快 23%，比 Composer 最佳混合架構快 37%。  
- 在 Long Range Arena 基準上，代理設計的架構在文件匹配與文字分類任務上分別只落後人類最佳狀態 2.3% 與 2.6%。  
- 在 Autoresearch 基準上，Greedy Opus 4.5 在固定時間預算下達到 0.968 驗證位元組每位元（bits‑per‑byte），超越已發表的最低基線。  

💡 **高層搜尋與低層機制設計的分工，讓代理既能探索宏觀結構，又能創新注意力機制**  
AIRA-Compose 負責在較高的抽象層次上搜尋「什麼樣的計算原始塊」最有潛力；AIRA-Design 則深入具體機制，設計新的注意力形式與訓練腳本。這種分層合作讓代理既能跳出傳統 Transformer 的框架，又能在細節上提出可用的算法優化。  

⚠️ **程式碼與模型權重尚未公開，實驗規模受時間預算限制**  
雖然結果令人鼓舞，但論文尚未釋放程式碼或預訓練權重，限制了工程師直接複現與移植。此外，所有搜尋均在 24 小時的固定預算下進行，長期演化或更大規模的探索尚未驗證。  

🎯 **未來模型設計可考慮代理協同流程，但需等待開放資源以驗證與移植**  
- 研究展示了「代理驅動的架構搜尋」作為一種可行的範式，未來可結合更大的運算預算或多輪遞迴，以逼近遞迴自我改進的目標。  
- 對於工程團隊而言，目前的首要步驟是關注官方後續發布的程式碼與模型，以便在內部平台上進行驗證與微調。  

🔗 **論文連結**  
📝 Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design  
👤 Alberto Pepe, Chien-Yu Lin, Despoina Magka, Bilge Acun, Yannan Nellie Wu @ FAIR, Meta  
🔗 https://arxiv.org/abs/2605.15871  

你認為 AI 代理參與模型設計會成為主流嗎？歡迎在留言區分享你的看法 👇  

#AI #Meta #FAIR #NeuralArchitectureSearch #LLMAgents #Llama3 #機器學習 #深度學習 #AI研究 #模型設計
