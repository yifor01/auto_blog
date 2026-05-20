---
title: "EngiAI: A Multi-Agent Framework and Benchmark Suite for LLM-Driven Engineering Design"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.19743
score: 119
model: tencent/hy3-preview:free
generated_at: 2026-05-20T20:52:18.813614
---

📌 EngiAI：多智能體框架與工程設計基準套件  
🏫 ETH Zurich；Autom8.build — Gioele Molinari, Florian Felten, Soheyl Massoudi, Mark Fuge  

你以為 LLM 能直接幫你完成複雜的工程設計嗎？實際上，多步驟的條件判斷仍是最大瓶頸。  

🤔 工程設計需要結合模擬、檢索與製造準備，現有評估無法涵蓋多智能體系統  
隨著 LLM 代理被應用於工程設計，既有基準多聚焦於單一任務，缺少對同時涉及模擬、檢測資料與製造準備的多智能體工作流的評估。  

🧪 包含工作流、RAG 與 HPC 三部分基準的七種提示風格實驗  
EngiBench 提供三個評估維度：（1）工作流基準，使用七種提示風格考察直接工具使用、語義消歧、條件分割與工作記憶等認知需求；（2）RAG 基準，透過閘得分隔離檢索對參數選擇的貢獻；（3）HPC 基準，在 SLURM 叢集上量測端到端機器學習訓練的編排表現。  

 私有模型在 Beams2D 上任務完成率達 96-97%，開源 4B 模型僅 55-78%，條件分支表現最弱  
在四種 LLM 後端與兩個 EngiBench 問題上，私有模型平均任務完成率為 96‑97%；同規模的開源 4B 參數模型則落在 55‑78% 之間，顯示明顯的代際差距。條件分支風格對應的完成率驟降至 20‑53%（Photonics2D），成為目前最具挑戰性的認知需求。  

💡 檢索增強生成的閘得分證明檢索貢獻極大，多步驟指令遵循隨工作流長度下降  
RAG 基準的閘得分顯示，啟用檢索時得分接近 1.0，未啟用則接近 0，驗證了基準能有效隔離檢索效果。在 HPC 編排測試中，有一個模型在所有運行中完成全部管線步驟（100%），而另一個模型僅達 50%，說明多步驟指令的遵循能力會隨工作流長度而衰減。  

⚠️ 僅測試兩個 EngiBench 問題與四個 LLM 後端，長期穩定性與更大規模系統未探討  
本研究的評估範圍限於 Beams2D 與 Photonics2D 兩個設計問題，以及四種代表性 LLM 後端；未涵蓋更長時效的穩定性測試或更大規模的多智能體部署。  

🎯 基於 LangGraph 的 EngiAI 參考實作提供可直接評估與改進多智能體工程流程的工具  
EngiAI 以 LangGraph 為基礎，透過監督架構協調七個專門代理，統一拓撲優化、文件檢索、HPC 工作編排與 3D 印表機控制。此參考實作搭配 EngiBench 基準，為工程師提供可量測的途徑來檢討並提升 LLM 驅動的多智能體設計管線。  

🔗 論文連結  
📝 EngiAI: A Multi-Agent Framework and Benchmark Suite for LLM-Driven Engineering Design  
👤 Gioele Molinari, Florian Felten, Soheyl Massoudi, Mark Fuge (ETH Zurich; Autom8.build)  
🔗 https://arxiv.org/abs/2605.19743  

#AI #LLM #EngineeringDesign #MultiAgentSystems #LangGraph #RAG #HPC #ETHZurich #Autom8Build
