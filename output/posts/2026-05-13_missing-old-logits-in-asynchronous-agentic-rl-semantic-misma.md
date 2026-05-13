---
title: "Missing Old Logits in Asynchronous Agentic RL: Semantic Mismatch and Repair Methods for Off-Policy Correction"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.12070
score: 100
model: tencent/hy3-preview:free
generated_at: 2026-05-13T20:50:18.196726
---

📌 異步強化中 Logits 問題  

你以為讓大語言模型自己學習行為只需要更多資料？實際上，異步更新會讓關鍵的歷史 logits 消失，導致學習不穩定。  

🤔 **異步更新讓 PPO 失效，歷史 logits 成為缺失環節**  
在大型語言模型的離線或異步強化學習中，策略更新往往延遲發生。這樣的延遲使得原本用於 PPO‑style 零策略修正的歷史 logits 無法取得，產生所謂的「missing logits」問題，進而削弱修正的效果與訓練穩定性。  

🧪 **理論修正：快照追蹤與改進的 PPO‑EWMA**  
論文提出兩種離策略修正途徑：一種是透過「快照追蹤」完整保存過去策略的 logits，以精確重建所需的歷史資訊；另種是對傳統 PPO‑EWMA 進行修訂，使其在缺少即時 logits 時仍能提供近似的修正項，同時降低計算開銷。  

🔍 **核心發現**  
精確與近似兩種方法均能夠在理論上彌補 missing logits，從而恢復 PPO‑style 零策略修正的有效性。這代表在異步強化學習框架下，有可能獲得較為穩定的策略更新過程。  

💡 **深入分析**  
快照追蹤的核心在於將每次策略更新的 logits 做版本控制，當需要進行離策略校正時，直接查閱對應的快照；修訂的 PPO‑EWMA 則藉由調整衰減因子與補項公式，在無法取得精確 logits 時，利用最近的近似值進行修正，以求在正確性與效率間取得平衡。  

⚠️ **研究限制**  
目前僅止於理論探討與算法描述，尚未公開原始碼或進行大規模實驗驗證，因此其在真實訓練系統中的實際表現與開源社群的即時影響仍有待觀察。  

🎯 **實務啟示**  
對於正在嘗試異步 Agentic 訓練的研究團隊，該論文提供了兩種可行的離策略修正思路：若資源允許，可考慮快照追蹤以獲得精確修正；若求輕量級實作，則可嘗試採用改進的 PPO‑EWMA。未來補上實驗基準與開源實作，將有助於評估這些方法在大規模語言模型訓練中的實用价值。  

🔗 **論文連結**  
📝 Missing Old Logits in Asynchronous Agentic RL: Semantic Mismatch and Repair Methods for Off-Policy Correction  
👤 作者：未在摘要中詳列  
🔗 https://huggingface.co/papers/2605.12070  

你在異步 RL 訓練中是否也遇過 logits 消失的困擾？歡迎在留言區分享你的經驗或看法 👇  

#强化学习 #大语言模型 #PPO #离策略修正 #AgenticAI #HuggingFacePapers #AI研究
