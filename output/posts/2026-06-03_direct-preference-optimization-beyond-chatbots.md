---
title: Direct Preference Optimization Beyond Chatbots
source: HuggingFace Blog
url: https://huggingface.co/blog/Dharma-AI/direct-preference-optimization-beyond-chatbots
score: 100
model: tencent/hy3-preview:free
generated_at: '2026-06-03T21:34:29.561344'
---

📌 **【HuggingFace Blog】DPO 降低 OCR 文字退化率，平均下降 59.4%**

你以為 Direct Preference Optimization (DPO) 只能讓聊天機器人更友善？研究顯示，同樣的技術其實能把 OCR 模型的「文字退化」錯誤率砍掉近九成。

🤔 **OCR 的隱形瓶頸：文字退化難以被 SFT 完全消除**

在結構化文件擷取任務（例如巴西葡萄牙語的 OCR），模型常會產生重複循環而不是正確的轉錄——這被稱為文字退化率。雖然監督式微調 (SFT) 能降低多數模型的退化率，但卻很少達到生產環境可接受的水準，顯示 SFT 僅能針對「正確輸出」優化，卻沒有明確懲罰退化行為。

🧪 **在 SFT 基礎上加入第二階段 DPO，使用模型自身的失敗樣本**

研究團隊先對多個開放原始碼與商業視覺語言模型家族進行 SFT，然後在同樣的文件集合上，使用同一個模型再進行第二次訓練——這次採用 Direct Preference Optimization。DPO 的訓練資料來自模型自身的失敗案例（即所謂的「rejection pairs」），讓模型學習哪些輸出應該被降低機率。整個流程僅在 SFT 完成後進行，未改變基礎模型或資料來源。

📈 **DPO 在所有測試模型家族中均顯著降低文字退化率**

- 平均減少：59.4%  
- 最佳案例（Nanonets‑OCR2‑3B）：從 1.61% 降至 0.20%，減幅達 87.6%  
- 沒有例外：每個測試的模型家族都呈現相同的改善方向，僅幅度有差異。

這表示 DPO 能夠有效補足 SFT 在處理退化模式上的不足，且效果穩定跨越不同模型架構。

💡 **為什麼 DPO 在這個客觀任務上也能發揮作用？**

與聊天對齊不同，OCR 任務沒有主觀的「有用」或「無害」判斷；正確與錯誤是可量化的。DPO 透過直接從模型自己的失敗中學習，能夠在訓練過程中明確抑製產生重複循環的輸出，因而把原本只能透過 SFT 間接改善的問題轉變為可直接優化的目標。

⚠️ **研究限制：僅聚焦於巴西葡萄牙語結構化文件、短期評估**

- 實驗僅在結構化文件擷取（特別是巴西葡萄牙語 OCR）上進行，其他語言或非結構化場景尚未驗證。  
- 評估基於即時的文字退化率，未探討長期穩定性或對下游任務（如資訊抽取）的連帶影響。  
- 未涉及更大規模的商業部署測試，因此生產環境的實際成本與延遲仍需進一步觀察。

🎯 **實務啟示：將 DPO 作為 OCR 管線的第二階段微調**

對於從事文件擷取或視覺語言模型工程的開發者，可在完成標準的 SFT 後，加入一個使用模型自身失敗樣本的 DPO 步驟。這種做法是開放原始碼、無需額外標註人力，且已在多個模型家族上證明能顯著降低文字退化率，提升 OCR 的實用品質。

🔗 **論文連結**  
📝 Direct Preference Optimization Beyond Chatbots  
👤 Erick Lachmann, Gabriel Pimenta de Freitas Cardoso (Dharma‑AI)  
🔗 https://huggingface.co/blog/Dharma-AI/direct-preference-optimization-beyond-chatbots

你是否在 OCR 或相關視覺語言任務上嘗試過類似的二階段優化？歡迎在留言區分享你的經驗與觀察 👇

#HuggingFace #DPO #OCR #VisionLanguageModel #機器學習 #NLP #AI工程 #文件擷取
