---
title: "Misaligned by Reward: Socially Undesirable Preferences in LLMs"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.05003
score: 93
model: tencent/hy3-preview:free
generated_at: 2026-05-07T20:57:38.540532
---

📌 【Stuttgart 研究】Reward Model 會學會不良社會偏好嗎？

你以為訓練出更聰明的 AI 就能自動擁有良好道德判斷？最新研究顯示，Reward Model 反而可能學會偏好社會不良的選擇。

🤔 **標準對齊基準忽略了社會偏好的細節**  
Reward model 是大型語言模型對齊過程中的人類偏好代理，但現有評估多聚焦於廣泛的指令遵循基準，難以看出模型是否真的捕捉到「社會可取」的偏好。這樣的評估盲點可能讓社會層面的對齊失靜悄悄發生。

🧪 **把社會評估資料轉成成對偏好來測試五個 Reward Model**  
研究團隊提出一個框架：將社會評估資料（偏見、安全、道德、倫理推理四個領域）轉換為成對偏好資料。在有標準答案時直接使用 gold label；沒有時則依據方向性偏見指標來建構偏好對。此方法使得我們能直接檢測 reward model 是否更傾向選擇社會不良的選項，以及其偏好是否會導致所選輸出的分布出現系統性偏差。

🔍 **Reward Model 常偏好社會不良選項，並產生有系統的偏分布**  
在五個公開的 reward model 與兩個作為 reward proxy 的指令調整模型上進行實驗，結果顯示：模型在不同領域上的表現差異很大，沒有單一模型在所有領域中表現最佳。總體來看，它們遠未達到強社會智慧的水準——經常偏好社會不良的選項，且這些偏好會產生明顯的系統性偏分布。

💡 **追求公平會犧牲對上下文的敏感度，揭示對齊的權衡**  
進一步分析發現，當模型被設計得更嚴格地避免偏見時，對輸入上下文的敏感度反而會下降。這揭示了一個重要的對齊權衡：在減少偏見結果與保持對情境的忠實理解之間，難以同時達成兩極。

⚠️ **僅測五個公開模型，未涵蓋最新專有模型，社會領域範圍有限**  
本研究的樣本限於五個公開可用的 reward model 以及兩個指令調整模型作為 proxy，並未涵蓋業界最新的專有模型。此外，雖然已納入偏見、安全、道德、倫理推理四個社會重要領域，但其他潛在的社會維度仍未被探討。

🎯 **評估對齊時需直接量化社會偏好，而非只依賴通用基準**  
對於從事 LLM 對齊的研究者與工程師來說，結果提醒我們：標準的 reward 基準不足以衡量模型的社會對齊品質。未來的評估應該直接納入社會偏好測量（如上述成對偏好框架），並在追求公平與保持上下文忠實度之間做出明確的權衡決策。

🔗 **論文連結**  
📝 Misaligned by Reward: Socially Undesirable Preferences in LLMs  
👤 Gayane Ghazaryan, Esra Dönmez @ University of Stuttgart  
🔗 https://arxiv.org/abs/2605.05003

你在使用 AI 輔助工具時，有否注意到模型在道德或偏見上的傾向？歡迎在留言區分享你的觀察與經驗 👇

#AI #LLM #RewardModel #對齊 #社會偏見 #Stuttgart #機器學習 #AI倫理
