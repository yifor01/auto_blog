---
title: "NVIDIA Releases Polar, a Token-Faithful Rollout Framework for GRPO Training Across Codex, Claude Code, and Qwen Code"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/27/nvidia-releases-polar-a-token-faithful-rollout-framework-for-grpo-training-across-codex-claude-code-and-qwen-code/
score: 101
model: tencent/hy3-preview:free
generated_at: 2026-05-27T20:59:49.138406
---

📌 【NVIDIA 最新研究】Polar：無需修改即可在多種 Code Agent 上做 GRPO 訓練  

你以為要讓 AI 程式碼助手強化學習必須改寫整套工具鏈？  
NVIDIA 的 Polar 框架卻證明，只要把模型端點指向一個 gateway，就能在不動原始 harness 的情況下完成完整的 token‑faithful rollout。  

🤔 **現有 RL 訓練流程與 agent harness 的衝突**  
強化學習（RL）在多輪工具使用、長上下文及多代理協同的場景中變得日益複雜。現有的 agent harness（如 Codex CLI、Claude Code、Qwen Code）負責系統提示、工具格式、上下文工程以及 patch 提交，這些細節直接影響評估時的行為。傳統 RL 基礎設施要求將 harness 邏輯包裝在框架自有的環境 API（env.init()/env.step()/env.reset()）後面，每種 harness 都需要額外的整合程式碼，且在過程中可能遺失原生 harness 的執行細節。  

🧪 **Polar 的設計：在模型 API 邊界放置 proxy**  
Polar 的核心觀察是：每個基於 LLM 的 agent 必須呼叫模型。因此，團隊在模型 API 邊界部署了一個 gateway proxy。對於每筆進入的模型請求，proxy 執行四個步驟：  
1. 取得非串流的上游回應。  
2. 對於串流請求，合成一個符合 provider 形狀的串流，以保持 harness 對 Server‑Sent Events 的期望。  
3. 確保完整的 token 捕獲（token‑faithful）。  
4. 唯一必要的改動是將 harness 的 model base URL 指向此 gateway。  

Polar 包含兩個核心元件：  
- **Rollout Server**：接收 TaskRequest，依照 num_samples 展開為獨立的 session；每個 session 帶有 session ID、task ID、timeout、runtime 規格、agent 規格、trajectory builder、evaluator 與 callback URL。  
- **Gateway Nodes**：負責執行上述 proxy 步驟，並將 session 分發至適當的節點，接受回調。  

🔑 **核心發現：無程式碼更改即可在多種 harness 上進行 GRPO 訓練**  
透過上述設計，Polar 成功讓研究者在不修改 Codex CLI、Claude Code、Qwen Code 等原始 harness 的情況下，完成 GRPO（Generative Reward Policy Optimization）訓練流程。因為所有 token 都經過 proxy 原樣傳遞，訓練過程不會因串流處理或格式轉換而失真，因而保留了 harness 原本的工具使用與上下文行為。  

💡 **為何 token‑faithful 及 harness‑agnostic 如此重要？**  
- **Token‑faithful** 確保強化學習獎訊號是基於實際產生的 token 序列，避免因合成或截斷導致的偏差。  
- **Harness‑agnostic** 意味著同一套 RL 基礎設施可以直接套用於各種現有的 coding agent，大幅降低實驗門檻與工程成本。  
- 透過只改變模型端點，研究團隊可以快速在不同 agent 上比較獎勵函式、探索新的 multi‑turn 策略，而不必重新實作工具鏈或擔心行為漂移。  

⚠️ **目前已知的限制**  
- 所述實驗主要聚焦於 Codex CLI、Claude Code 與 Qwen Code 三種 harness；其他類型的 agent（例如非 coding 任務的助手）尚未驗證。  
- 框架引入的 gateway 可能會增加網路來回延遲；實際吞吐量與資源開銷仍需後續基準測試。  
- 目前的說明著重於 rollout 階段的設計，訓練穩定性、獎勵函式收斂性等長期效果尚未公開詳述。  

🎯 **對工程師的實務建議**  
- 若您希望在現有的 coding agent 上進行 RL 實驗，先評估是否可將模型端點指向 Polar gateway，這樣可避免重寫 harness 程式碼。  
- 在實施前，先量測 gateway 增加的延遲是否能接受於您的訓練迴圈。  
- 考慮將 Polar 與您現有的獎勵函式或曲線學習演算法結合，以充分利用 token‑faithful 的特性獲得更可靠的政策更新。  

🔗 **論文連結**  
📝 NVIDIA Releases Polar, a Token‑Faithful Rollout Framework for GRPO Training Across Codex, Claude Code, and Qwen Code  
👤 作者：Asif Razzaq（MarkTechPost 報導）  
🔗 https://www.marktechpost.com/2026/05/27/nvidia-releases-polar-a-token-faithful-rollout-framework-for-grpo-training-across-codex-claude-code-and-qwen-code/  

你的團隊是否已經在類似的 agent 上嘗試過免修改的 RL 整合？歡迎在留言區分享經驗或疑問 👇  

#AI #ReinforcementLearning #NVIDIA #Polar #CodeAgent #GRPO #MachineLearning #開發工具
