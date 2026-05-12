---
title: "LASAR: Latent Adaptive Semantic Aligned Reasoning for Generative Recommendation"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.10207
score: 116
model: tencent/hy3-preview:free
generated_at: 2026-05-12T20:34:00.071889
---

📌 【Beihang University & Baidu】LASAR：讓推薦系統的「隱藏思考」更快更準  

你是否曾好奇，推薦系統在背後進行多步推理時，是否一定要像人類一樣逐字寫出思考過程？如果能把這種「思考」壓縮成潛在的連續狀態，既能保留推理品質，又能大幅降低延遲，會不會是實時推薦的突破點？  

🤔 **隱藏推理的潛力與三個阻礙**  

大型語言模型透過 Chain‑of‑Thought (CoT) 展現出強大的多步推理能力，但在延遲敏感的推薦場景中，token‑by‑token 的生成方式卻成為瓶頸。潛在推理（latent reasoning）嘗試在連續隱藏狀態空間裡完成多步推理，以達到更低的計算成本，但在生成式推薦裡仍鮮有探索。論文指出，直接將潛在推理套用到生成式推薦會遇到三個獨特挑戰：  
1. **Semantic ID (SID) 與潛在空間的語義斷層** – SID 符號本身缺乏預訓練語義，難與潛在推理空間聯合優化。  
2. **缺乏推理鏈監督導致的表示漂移** – 沒有明確的 CoT 指導，潛在狀態容易在推理過程中偏離正確語義。  
3. **固定推理深度的次優性** – 對所有樣本使用同一推理步數，既浪費也可能不足。  

🧪 **兩階段 SFT‑then‑RL 框架與自適應步數**  

LASAR 採用 SFT‑then‑RL 的兩階段訓練流程來逐一解決上述問題：  

- **第一階段：語義 grounding**  
  先以監督微調（SFT）讓模型學習 SID 的語義表示，為後續引入潛在推理奠定共享的語義基礎。  

- **第二階段：潛在推理與對齊**  
  在已具備 SID 語義的基礎上，引入潛在推理。為防止表示漂移，採用逐步雙向 KL 散度，將潛在推理的軌跡約束在從 CoT 文本萃取出的隱藏狀態錨點周圍；同時設計一個 Policy Head 預測每個樣本的所需推理深度。  

- **RL 階段：動態步長與終端對齊**  
  基於 GRPO 的強化學習階段，僅在終端進行 KL 對齊，以容納變長的推理過程；透過 REINFORCE 優化 Policy Head，使模型能依據樣本難度動態分配推理步數。  

實驗結果顯示，此設計幾乎將平均潛在步數減半，同時仍能提升推薦品質；推論端僅增加極小的延遲，且相較於產出完整 CoT 文本，**快約 20 倍**。  

🔑 **核心發現：步數減半、品質提升、延遲可忽略**  

- 在三個真實世界資料集上，LASAR 全部優於現有基線。  
- 平均潛在推理步數降低約 50%。  
- 推薦效果（請參考原論文對應指標）相較於基線有顯著提升。  
- 推論延遲僅有微小增加，與生成完整 CoT 文本相比，速度提升約 20 倍。  

💡 **關鍵洞察：語義對齊與自適應深度是成功的關鍵**  

研究表明，僅減少推理步數並不足以保證效果；必須先確保 SID 擁有穩定的語義基礎（階段一），再透過逐步 KL 對齊將潛在推理軌跡綁定在可信的語義錨點上（階段二），最後讓模型學會依據樣本特性決定何時停止推理。這樣的「語義對齊 + 動態步長」機制，才讓潛在推理在不犧牲品質的前提下實現大幅加速。  

⚠️ **研究限制：僅驗證生成式推薦、未探討更長 horizon**  

- 實驗集中在三個公開的推薦資料集，未涵蓋所有可能的產業場景。  
- 本工作聚焦於單次推論的潛在推理步數，未探討多輪互動或長期使用者行為建模的影響。  
- 雖然方法設計為通用，但具體超參數（如 KL 係數、Policy Head 結構）仍需依資料集調校。  

🎯 **實務啟示：在延遲敏感的推薦系統中優先考慮潛在推理＋自適應步數**  

- 若系統現階段依賴顯式 CoT 解釋或多步推理，可評估將推理壓縮至潛在空間，並搭配語義對齊機制。  
- 在訓練流程中，先確保離散 ID（如 Semantic ID）具備足夠語義表達，再引入潛在推理階段，可避免表示漂移。  
- 透過簡單的 Policy Head 學習每樣本所需步數，可在不犧牲準確率的前提下，顯著削減平均計算成本。  

🔗 **論文連結**  
📝 LASAR: Latent Adaptive Semantic Aligned Reasoning for Generative Recommendation  
👤 Yiwen Chen, Fuwei Zhang, Zehao Chen, Deqing Wang, Hehan Li @ Beihang University; Baidu  
🔗 https://arxiv.org/abs/2605.10207  

你在推薦系統中是否也嘗試過把多步推理「藏起來」？歡迎在留言區分享你的經驗或疑問 👇  

#AI #RecommendationSystems #LLM #LatentReasoning #BeihangUniversity #Baidu #LASAR #MachineLearning #InformationRetrieval
