---
title: "Refinement via Regeneration: Enlarging Modification Space Boosts Image Refinement in Unified Multimodal Models"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.25636
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-04-29T19:54:01.467529
---

📌 【清華大學 × Tencent HY】統一多模態模型精練新範式：從「編輯」走向「再生」

目前多模態生成系統在「產出後精練（refinement）」時，多半要求模型只改錯、不亂動。這項限制聽起來合理，卻讓模型在對齊複雜語意時束手束腳。我們是否能透過擴大修改空間，在不犧牲穩定性的前提下，把對齊能力推上一層樓？

🤔 **統一多模態模型具備「生成後再改」潛力，但現有做法受限太深**

統一多模態模型（UMMs）在同一框架內同時具備視覺理解與生成能力。對文字生圖（T2I）任務而言，這意味模型可以在初次生成後，進一步自我精練，理論上有機會突破原本的性能上限。  
但目前以 UMM 為基礎的精練方法多採「編輯導向精練（RvE）」：模型先產出編輯指令，再依指令修改未對齊區域、保留已對齊內容。這種做法面臨兩個瓶頸：一是編輯指令對「提示詞—圖像」誤差的描述過於粗略，容易漏改；二是強制像素級保留，雖然適合圖像編輯，卻壓縮了精練階段的有效修改空間。

🧪 **以「條件再生」取代「編輯」，保留語意而非像素**

本研究提出 Refinement via Regeneration（RvR），將精練重新定義為**條件圖像再生**。RvR 不依賴編輯指令，也不強制嚴格內容保留，而是以目標提示詞與初始圖像的語意 token 為條件，進行整體再生。藉由鬆綁像素級約束，模型能更完整地修正語意對齊問題，並在可控範圍內擴大修改空間。

☑️ **用 RvR 的那組，三項基準指標全面提升**

- Geneval：0.78 → 0.91  
- DPGBench：84.02 → 87.21  
- UniGenBench++：61.53 → 77.41  

這些提升顯示，放寬修改空間並以再生取代局部編輯，能更有效解決提示詞與圖像之間的語意落差，尤其在複雜屬性、組合關係與細節一致性上。

💡 **從「保留像素」轉向「重建語意」，精練邏輯被重新定義**

RvR 的核心洞察在於：精練的本質不是「把圖修得更像提示詞」，而是「在保持原始語意骨架的前提下，再生一張更符合目標的圖」。  
當模型不再被編輯指令與像素約束限制，它能更自由地調整區域配置、材質與空間關係，從而提升整體對齊程度。這也意味，未來的可控 T2I 系統可以更接近「推論—再生」的循環式優化，而非單步修補。

⚠️ **目前以基準測試為主，長期穩定性與邊界情況待驗證**

本研究聚焦於基準指標的提升，並未深入探討極端提示詞、長尾概念或跨域遷移的穩定性。此外，再生導向方法在計算成本與可控粒度上的權衡，也有待進一步實務驗證。

🎯 **可控生成系統的精練流程，值得重新設計**

- 將「再生」視為精練的可行選項，而非僅限於編輯  
- 在工作流中保留語意 token 的傳遞，以穩定再生範圍  
- 藉由循環優化提升 T2I 系統的可控性與提示詞忠實度  

🔗 **論文連結**  
📝 Refinement via Regeneration: Enlarging Modification Space Boosts Image Refinement in Unified Multimodal Models  
👤 Jiayi Guo, Linqing Wang, Jiangshan Wang, Yang Yue, Zeyu Liu（清華大學；Tencent HY）  
🔗 https://arxiv.org/abs/2604.25636  

你在可控生圖的實務經驗中，最常遇到的「改了又錯、改了又違和」問題，如果換成再生式精練，可能會如何改變？欢迎留言討論 👇

#AI #Multimodal #TextToImage #GenAI #ComputerVision #清華大學 #TencentHY #CVPR
