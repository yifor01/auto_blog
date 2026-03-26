---
title: "Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs"
source: arXiv
url: http://arxiv.org/abs/2603.24511v1
score: 112
model: gpt-4o-free
generated_at: 2026-03-26T19:39:23.114485
---

📌 【Claudini】LLM Agent 自動發現 SOTA 對抗攻擊演算法  

🎣 你以為 AI 只能防禦？Claudini 顯示它也能自動發現更強的攻擊  

🤔 **自動化研究管線變成攻擊發現引擎**  
Anthropic 的 Claudini 框架以 Claude Code 為核心的 autoresearch 代理，從已知的白箱攻擊（如 GCG）出發，透過迭代優化產出新演算法。這意味著安全研究的循環可以由 LLM 自動驅動。  

🧪 **從現有攻擊出發的迭代優化流程**  
研究團隊以既有的 30+ 攻擊方法為基礎，讓 Claude Code 在安全評估任務上進行自動搜尋與改造。每次迭代產出候選攻擊，使用密集的量化回饋（攻擊成功率）進行選擇，直至無法再提升。  

 **在 CBRN 查詢上達到 40% 攻擊成功率，遠超既有方法 ≤10%**  
在 GPT-OSS-Safeguard-20B 上，Claudini 發現的攻擊平均成功率達到 40%，而所有既有白箱攻擊的最佳表現不超過 10%。此提升在 jailbreak 與 prompt injection 評估中皆顯著。  

💡 **發現的攻擊具有強泛化性：在未見模型上達 100% ASR**  
將在 surrogate model 上優化的攻擊直接套用於 Meta‑SecAlign‑70B，實現 100% 攻擊成功率；而目前最佳基線僅達 56%。此結果顯示攻擊具有良好的跨模型遷移能力。  

⚠️ **研究聚焦於白箱場景，且依賴現有攻擊作為起點**  
Claudini 的設計假設攻擊者能存取模型梯度或內部表示，且其演化過程依賴於既有攻擊實作（如 GCG）作為種子。黑箱或僅限 API 的情境未在此研究中探討。  

🎯 **安全團隊可將自動攻擊生成納入紅隊流程，持續壓測防禦**  
建議將類似的 autoresearch 管線作為紅隊例行工具，定期產出新攻擊樣本以評估與更新防禦機制；同時注意僅在授權且受控環境下進行，以避免濫用。  

🔗 **論文連結**  📝 Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs  
👤 Alexander Panfilov, Peter Romov, Igor Shilov, Yves-Alexandre de Montjoye, Jonas Geiping  
🔗 arXiv: http://arxiv.org/abs/2603.24511v1  💻 程式碼：https://github.com/romovpa/claudini  

#AI #LLM #AdversarialAttack #RedTeam #ClaudeCode #Autoresearch #Security #MachineLearning
