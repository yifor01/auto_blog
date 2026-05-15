---
title: "Quantifying and Mitigating Premature Closure in Frontier LLMs"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.15000
score: 112
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:25:36.401179
---

📌 【Stanford 最新研究】前沿 LLMs 會過早下結論嗎？

你以為 AI 回答越多越好？研究顯示，在資訊不足時，它竟然還是堅持給出答案。

🤔 **「過早結論」在醫療 AI 中是個隱形風險**  
過早結論（premature closure）指的是在資訊不足時仍做出決定。在臨床診斷中，這是錯誤的重要來源；同樣的問題在大型語言模型（LLM）中卻鮮被檢視。若模型在不確定時給出建議或答案，而更安全的做法應該是澄清、拒絕或升級，則可能導致錯誤的醫療建議。

🧪 **五個前沿 LLM 在結構化與開放式醫療任務上的評估**  
研究團隊選取了五個前沿 LLM，分別在兩個結構化基準與兩個開放式基準上進行測試：  
- 結構化任務：MedQA（n = 500）與 AfriMed‑QA（n = 490），在每題中將正確答案移除，觀察模型是否仍選擇一個選項。  
- 開放式任務：HealthBench（861 題）與醫師撰寫的對抗性查詢（191 題），檢查模型是否給出不適當的答案。

📊 **即使資訊不足，模型仍高率給出答案**  
- 在 MedQA 中，基礎錯誤行為率（false‑action rate）落在 55%～81% 之間；在 AfriMed‑QA 中為 53%～82%。  
- 在開放式評估中，模型在平均 30% 的 HealthBench 問題上給出不適當答案，而在醫師對抗性查詢上這個比例升至 78%。  
- 加入安全導向的提示（safety‑oriented prompting) 能降低這些比例，但錯誤仍然存在，顯示模型在「何時不該回答」方面仍有缺口。

💡 **模型需要學會「知道自己不知道」**  
結果顯示，即使模型能夠在資訊充足時給出正確答案，但在不確定情境下，它們傾向於「過早承諾」而不是選擇澄清或拒絕。這意味著現有的安全提示雖有幫助，卻無法完全消除過早結論的傾向。未來的模型評估與訓練必須把「知道何時保持沉默」納為核心能力，才能在臨床決策支援中達到可信賴的表現。

⚠️ **研究限制**  
- 評估僅限於五個前沿 LLM 與四個特定基準，未涵蓋所有可能的醫療場景。  
- 安全導向提示的形式與強度在實際部署中可能有所不同。  
- 未進行真實臨床環境的前瞻性研究，長期影響尚未知。

🎯 **對工程與研究的啟示**  
- 在開發醫療 LLM 時，應將「拒絕回答」或「請求更多資訊」視為可接受的輸出，並以此為目標進行微調或強化學習。  
- 建立專門衡量模型在不確定下是否選擇澄清或拒絕的基準，以追蹤隨時間的改善。  
- 安全提示雖可降低風險，但不應被視為最終解決方案；模型內在的不確定性感知能力仍需提升。

🔗 **論文連結**  
📝 Quantifying and Mitigating Premature Closure in Frontier LLMs  
👤 Rebecca Handler, Suhana Bedi, Nigam Shah @ Stanford University  
🔗 https://arxiv.org/abs/2605.15000

你在使用 AI 進行醫療諮詢時，會如何判斷它是否該給出答案？歡迎在留言區分享你的經驗與看法 👇

#AI #MedicalAI #LLM #Safety #Stanford #PrematureClosure #HealthCare #MachineLearning
