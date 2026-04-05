---
title: "Leveraging Synthetic Data for Enhancing Egocentric Hand-Object Interaction Detection"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.29733
score: 93
model: gpt-4o-free
generated_at: 2026-04-01T12:34:21.096097
---

📌 合成資料強化手物互動偵測  

真實標註資料往往難以取得，特別是在第一人稱視角的手物互動場景。當標註成本高、數據稀少時，我們是否能靠合成資料彌補這個缺口？  

🤔 合成資料能否在真實標註稀少時顯著提升偵測效果  

在 AR/VR 與機器人應用中，手物互動（HOI）的準確偵測是關鍵。然而，取得大量精確標註的第一人稱影像成本高昂，導致實際應用常面臨資料不足的問題。本研究探討合成資料在這種情況下的實用價值。  

🧪 在 VISOR、EgoHOS、ENIGMA-51 上進行合成與真實資料的比較實驗  

研究團隊建構了一套合成資料生成管線，並以此產出帶有手物接觸狀態、邊界框與像素級分割遮罩的合成影像。在 VISOR、EgoHOS 與 ENIGMA-51 三個基準資料集上，分別進行了僅使用真實標註資料的基線訓練，以及合成資料加上僅 10% 真實標註資料的混合訓練，以觀察偵測效果的變化。  

 合成資料加少量真實標註即可顯著提升 Overall AP  

- 在 VISOR 上，混合訓練相對於純真實資料訓練提升 **+5.67%** Overall AP  
- 在 EgoHOS 上，提升 **+8.24%** Overall AP  
- 在 ENIGMA-51 上，提升 **+11.69%** Overall AP  

此外，隨著合成資料在物件類別、抓取方式與環境場景上與真實基準的對齊程度提升，偵測效益亦持續增加。  

💡 合成資料的價值取決於與真實世界的對齊度  

實驗結果表明，單純增加合成資料量並不一定帶來改善；關鍵在於讓合成資料的物件分佈、抓取模式及背景環境盡可能貼近目標真實資料集。這意味著，一個可調整的合成資料管線比單一靜態合成資料庫更具實用價值。  

⚠️ 實驗僅在三個特定資料集上進行，未涵蓋更廣泛的場景  

研究的結論基於 VISOR、EgoHOS 與 ENIGMA-51 三個資料集的表現。未在其他第一人稱 HOI 資料集或真實產線環境中進行驗證，因此泛化能力仍需進一步探討。此外，論文未說明合成資料生成的計算成本或生成時間。  

🎯 在資料標註成本高的情況下，優先考慮可對齊的合成資料管線  

對於 AR/VR 應用或機器人感知系統，若標註資料取得困難，可先建構能夠依據目標物件、抓取方式與環境進行調整的合成資料管線，再搭配少量真實標註進行微調。此策略在本研究中已示明可在僅使用 10% 真實標註的情況下，顯著提升偵測精度。  

🔗 論文連結  
📝 Leveraging Synthetic Data for Enhancing Egocentric Hand-Object Interaction Detection  
👤 Rosario Leonardi, Antonino Furnari, Francesco Ragusa, Giovanni Maria Farinella (University of Catania; Next Vision s.r.l.)  
🔗 論文：https://arxiv.org/abs/2603.29733  
💻 程式碼與資料：https://fpv-iplab.github.io/HOI-Synth/  

你在專案中是否也遇過標註不足的問題？合成資料的對齊策略是否值得嘗試？歡迎在留言區分享經驗 👇  

#AI #ComputerVision #SyntheticData #HandObjectInteraction #EGO #ARVR #Robotics #UniversityofCatania #NextVision #HOI-Synth #CVPR2026
