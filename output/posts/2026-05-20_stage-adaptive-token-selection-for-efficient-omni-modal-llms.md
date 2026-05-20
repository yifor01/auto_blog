---
title: "Stage-adaptive Token Selection for Efficient Omni-modal LLMs"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.20035
score: 115
model: tencent/hy3-preview:free
generated_at: 2026-05-20T20:59:10.494172
---

【階段自適應選 token 技術】

你以為 omni‑modal LLM 必須把每幀影像、每段聲音都塞進巨大模型才能理解嗎？實際上，許多後層的音視訊 token 已經變得多餘。如果能在適當的階段把它們剔除，速度能提升近五倍，卻只犧牲不到 4% 的效能——這正是本文提出的 SEATS 方法所做到的。

**密集音視訊 token 拖慢 omni‑LLM 推理**  
現有的 omni‑LLM 會將影像與聲音編碼成時間對齊的 token 序列，並在 LLM 中逐層處理。這種 dense 的非文字 token 在整個網路中持續運算，造成顯著的計算開銷。雖然已有訓練免費的 token 選擇方法，但多數僅作用於視訊單一模態，或在 LLM 前以固定比例剪枝，無法捕捉跨模態 token 重要性隨層數變化的規律。

**隨著層數加深，音視訊依賴呈塊狀遞減**  
研究團隊首先分析了 omni‑LLM 中層級的 token 依賴關係。發現視訊與音訊的依賴呈塊狀分布，且隨著網路深度逐漸變弱，意味著許多後層的非文字 token 在跨模態融合後已變得冗餘。基於此觀察，他們提出 SEATS（Stage‑adaptive Token Selection），一種訓練免費、階段自適應的 token 選擇策略。

**僅保留 10% 音視訊 token，速度提升 4.8×，效能損失不到 4%**  
在 Qwen2.5‑Omni 與 Qwen3‑Omni 上的實驗顯示，SEATS 在 LLM 前透過注意力加權的多樣性選擇移除時空冗餘；在 LLM 內部則逐區塊進行剪枝，並根據 query 相關分數動態調整時間窗與模態的保留預算；在後層，一旦跨模態融合完成，會直接刪除所有剩餘的非文字 token。僅保留原始音訊與視訊 token 的 10%，即可達成 9.3× FLOPs 減少、4.8× 前填加速，同時保留原始效能的 96.3%。

**前中後層分階段策略：先去冗餘、動態分配、最終清除**  
SEATS 的核心在於「階段」：  
- **LLM 前**：利用注意力權重進行多樣性選擇，消除空間與時間上的重複資訊。  
- **LLM 內部**：以區塊為單位逐步裁剪，並透過 query 相關分數在時間窗與模態間重新分配保留配額。  
- **後層**：檢測到跨模態融合完成後，一次性移除所有剩餘的音訊與視訊 token，因為此時它們對後續語言生成已無貢獻。  
這樣的設計讓模型在早期保留足夠的多模態線索，在後期則專注於語言推理，從而在不犧牲理解力的前提下大幅提升效率。

**目前實驗僅在 Qwen2.5‑Omni 與 Qwen3‑Omni 上進行，尚未在更大規模或不同架構的 omni‑LLM 上驗證**  
雖然 SEATS 是訓練免費且可直接插入現有 omni‑LLM，但文中僅報告了兩個具體模型的結果。不同架構、更大規模的模型或其他多模態任務（例如跨語言音視訊）是否具有同樣的剪枝效益，仍需後續工作進一步探討。

**無需重訓練，直接插入現有 omni‑LLM 即可獲得近 5× 風速提升**  
對工程師而言，SEATS 提供了一種「即插即用」的加速方案：不需要重新訓練模型，只需在推理管線中加入該選擇模組，即可在保持原有理解能力的同時，顯著降低計算成本與延遲。特別適合對即時性要求高的場景，如實時視訊字幕、語音助理或邊際設備上的多模態理解。

🔗 **論文連結**  
📝 Stage-adaptive Token Selection for Efficient Omni-modal LLMs  
👤 Zijie Xin, Jie Yang, Ruixiang Zhao, Tianyi Wang, Fengyun Rao (Renmin University of China; WeChat Vision, Tencent Inc.)  
🔗 https://arxiv.org/abs/2605.20035  

你是否已在專案中嘗試過類似的 token 剪枝技巧？歡迎在留言區分享你的經驗與見解 👇

#AI #多模態 #LLM #效能提升 #Qwen #騰訊 #人民大學 #SEATS
