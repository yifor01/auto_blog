---
title: "ComplexMCP: Evaluation of LLM Agents in Dynamic, Interdependent, and Large-Scale Tool Sandbox"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.10787
score: 113
model: tencent/hy3-preview:free
generated_at: 2026-05-12T20:39:18.362488
---

📌 **ComplexMCP：測試 LLM 代理在動態相依工具沙盒中的表現**  

你以為 LLM 已經能熟練呼叫任何 API？在真實複雜環境中，即使是最強模型也只能達到 60% 成功率，遠低於人類的 90%。  

🤔 **從孤立 API 到真實工作流的最後一哩路**  
現有基準多聚焦於單一、獨立的 API 呼叫，卻忽略了真實商業軟體中工具的原子性、相互依賴以及環境噪聲。這使得代理在「最後一哩路」的自動化任務上表現不佳，而這正是企業級自動化亟需解決的瓶頸。  

🧪 **基於 MCP 的種子驅動大規模沙盒**  
ComplexMCP 建立在 Model Context Protocol (MCP) 之上，提供超過 300 經嚴格測試的工具，來源於 7 個具狀態的沙盒（涵蓋辦公套件、金融系統等）。透過種子驅動架構，基準能以確定性且多樣化的方式模擬動態環境狀態與不可預測的 API 失效，從而呈現出更貼近實際使用的評估條件。  

📊 **全場景與 RAG 評估顯現顯著差距**  
研究團隊在全文脈境與檢索增強生成 (RAG) 兩種範式下測試了多種 LLM。結果顯示，即使是頂尖模型也無法突破 60% 的成功率，而人類在同一任務上的表現約為 90%。這個近乎 30 個百分點的差距凸了現有代理在互依工作流中的不足。  

🔍 **三大核心瓶頸：工具檢索飽和、過度自信、戰略性放棄**  
透過細粒度的軌跡分析，研究歸納出三個導致失敗的主要因素：  
1. **工具檢索飽和**：隨著可用工具數量增大，代理在正確檢索所需工具時出現效能下降。  
2. **過度自信**：代理傾向於跳過必要的環境驗證步驟，直接執行操作，導致後續失敗。  
3. **戰略性放棄**：面對失敗時，代理更願意將失敗合理化，而非嘗試復原或替代方案。  

⚠️ **樣本範疇與評估視角的限制**  
基準主要聚焦於工具調用與環境狀態模擬，未涵蓋所有可能的業務規則或人機協作細節；評估僅針對現有 LLM 在全文與 RAG 兩種設定下的表現，其他範式（如外掛工具鏈）未在此研究中探討。  

🎯 **構建更具韌性的自主系統的啟示**  
- 改進工具檢索機制以應對大規模動作空間。  
- 強制代理執行環境驗證流程，減少過度自信導致的錯誤。  
- 設計復原機制，鼓勵代理在失敗後主動探索替代路徑而非早早放棄。  

🔗 **論文連結**  
📝 ComplexMCP: Evaluation of LLM Agents in Dynamic, Interdependent, and Large-Scale Tool Sandbox  
👤 Yuanyang Li, Xue Yang, Longyue Wang, Weihua Luo, Hongyang Chen  
🏫 Zhejiang University; Zhejiang Lab; Alibaba Group  
🔗 https://arxiv.org/abs/2605.10787  

你在開發 LLM 代理時，是否曾遇到過工具相依或環境噪聲導致的失敗？歡迎在留言區分享你的經驗與解決方案 👇  

#LLM #AIAgents #ComplexMCP #ToolUse #Automation #ZhejiangUniversity #Alibaba #ARXIV #MachineLearning
