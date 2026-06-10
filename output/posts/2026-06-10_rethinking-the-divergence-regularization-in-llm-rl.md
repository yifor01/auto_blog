---
title: Rethinking the Divergence Regularization in LLM RL
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.09821
score: 113
model: google/gemma-4-31b-it:free
generated_at: '2026-06-10T18:04:29.425321'
---

📌 【新方法】LLM 強化學習的「硬遮罩」到底卡住了什麼？  

你可能已在 PPO、DPPO 上看到「ratio‑clipping」或「divergence mask」的字樣，卻沒注意到：當罕見詞彙的機率被推得太遠時，梯度會直接被「砍掉」——模型無法自我修正，訓練甚至會失穩。  

🧩 **LLM RL 為何需要 Trust‑Region？**  
大型語言模型在 RL‑HF（Human‑Feedback）階段通常採用 off‑policy 訓練，這會產生「訓練‑推理不匹配」與「策略陳舊」兩大問題。為避免政策跳躍太大，必須在參數更新時加上 trust‑region 限制，使每一步的分布變化保持在安全範圍內。  

🔧 **現有方法的盲點：比例裁剪 vs. 散度遮罩**  
- **PPO / GRPO**：透過 importance ratio 的裁剪（ratio‑clipping）近似 trust‑region，但在長尾詞彙上 ratio 往往失真，無法真實反映分布位移。  
- **DPPO**：改用「散度遮罩」根據抽樣 token 的絕對機率變化定義 trust‑region，理論上更貼近實際分布。然而，一旦 token 的機率跨過安全邊界，梯度會被 **硬性刪除**，模型失去修正的機會。  

🧪 **DRPO：用平滑正則化取代硬遮罩**  
研究提出 **Divergence Regularized Policy Optimization (DRPO)**，核心改動如下：  
1. **平滑二次正則項**：以 advantage‑weighted 的 quadratic 正則化取代硬遮罩，對政策位移給予連續、受限的梯度權重。  
2. **保持相同 Trust‑Region 幾何**：正則項的設計保留 DPPO 定義的「絕對機率位移」邊界，只是將「斷點」變成「緩衝」的坡度。  
3. **提供邊界外的修正訊號**：即使 token 已越過安全區，梯度仍會以遞減方式作用，避免梯度完全失效。  

📈 **實驗結果：穩定性與效率雙提升**  
- 在多種模型規模（小至中大型）和不同架構（Transformer、Decoder‑only）上測試。  
- 針對 FP16、BF16 等精度設定，DRPO 均顯示出更快的收斂速度與更低的 loss 波動。  
- 相較於 PPO/DPPO，訓練過程中出現的「梯度爆炸」或「策略崩潰」次數明顯下降。  

⚠️ **研究限制**  
- 論文未提供大規模商用 LLM（如 GPT‑4）上的實驗，僅在公開可得的中小模型上驗證。  
- 正則化係數的選擇仍需依據具體任務與資料分布微調，缺乏一套通用的自動調參機制。  

🎯 **對工程師的實務建議**  
- **直接套用**：DRPO 的正則項實作簡潔，可在現有的 OpenAI‑Gym、RL‑HF 或 HuggingFace 🤗 Transformers RL 框架中替換 PPO 的 clipping 步驟。  
- **監控散度**：在訓練過程加入 token‑level probability shift 的統計圖表，確保正則項發揮預期的「平滑」效果。  
- **混合策略**：對於極長尾詞彙，可先使用 DRPO，後期再加上少量的 hard‑mask 以防止過度保守。  

🔗 **論文資訊**  
📝 *Rethinking the Divergence Regularization in LLM RL*  
📚 來源：HuggingFace Daily Papers  
🔗 論文連結：https://huggingface.co/papers/2606.09821  

---

💬 你在 LLM RL 訓練中有遇到過「梯度被裁剪」卻無法收斂的情況嗎？試試 DRPO，或分享你的調參心得吧！  

#LLM #ReinforcementLearning #RLHF #TrustRegion #DRPO #DPPO #PPO #AIResearch #MachineLearning #HuggingFace 🚀
