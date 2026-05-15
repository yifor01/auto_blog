---
title: "Warp-as-History: Generalizable Camera-Controlled Video Generation from One Training Video"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.15182
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:19:03.276243
---

📌 【Shanghai Jiao Tong 等】Warp-as-History：一支影片讓 AI 生成影片跟著鏡頭走  

你以為讓生成影片遵循特定鏡頭軌跡，必須重新訓練模型或花費大量標註資料？這篇論文提出一個不用任何訓練、不改模型結構、也不需要測試時優化的介面，直接利用模型原有的視覺歷史通路。更驚喜的是，僅用一支已標註的影片做微小 LoRA 調整，就能泛化到未見過的影片。  

🤔 **鏡頭控制視訊生成的成本高昂，現有方法依賴大規模標註或測試時優化**  
既有的 camera‑controlled 視訊生成通常需要透過相機編碼器、控制分支或位置編碼的修改來學習條件，這意味著必須在大量帶有相機標註的影片上進行後訓練。雖然有訓練‑free 的做法能避免這樣的成本，但往往把負擔轉移到測試時的優化或額外的去噪引導，對實務部署不太友好。  

🧪 **利用凍結視訊生成模型的視覺歷史通路，構建相機產生的偽歷史**  
Warp-as-History 把相機運動產生的 warp 視為可重用的歷史資訊：給定目標相機軌跡，我們從過去的觀測中產生相機 warp 的偽歷史，並把它送入模型原本的視覺歷史路徑。關鍵在於把這段偽歷史的位置編碼與正在去噪的目標幀對齊，同時刪除那些沒有對應真實來源觀測的 warp token。整個過程不需要任何額外訓練、模型結構改動或測試時優化。  

🔍 **核心發現：零射擊即可跟隨相機軌跡，且僅用一支影片的 LoRA 微調即顯著提升泛化能力**  
在凍結的視訊生成模型上直接套用 Warp-as-History 已經展現出非凡的零射擊相機控制能力。進一步在只有單一支帶有相機標註的影片上進行輕量的離線 LoRA 微調，能讓這種能力泛化到未見過的影片，同時提升相機遵循度、視覺品質與運動動態，且仍不需要測試時優化或針對目標影片做適應。  

💡 **深入分析：將相機‑induced warp 視為可重用的歷史資訊，避免額外計算並保持模型原有動態**  
這個方法的成功在於它並未嘗試去重新學習如何產生影片，而是把已經學會的時空動態（透過視覺歷史路徑）重新利用。透過位置對齊與可見 token 選擇，偽歷史只保留真實可觀測的部分，因而不會引入噪誤或破壞模型原本的運動建模能力。這也是為什麼即使不做任何訓練，模型仍能理解並跟隨新的相機軌跡。  

⚠️ **研究限制：實驗僅在特定資料集上驗證，長時程或極端相機運動的表現尚未探討**  
論文的實驗涵蓋了多樣化的資料集以驗證方法的有效性，但未涉及非常長的視訊序列或極端的相機轉動情況。此外，雖然離線 LoRA 微調只需一支標註影片，但對於完全沒有任何相機標註的領域，泛化的上限仍需進一步探索。  

🎯 **實務啟示：工程師可透過微小的離線 LoRA 調整，在不影響推論速度的情況下為現有視訊生成模型加入相機控制**  
對於已經部署的視訊生成管線，Warp-as-History 提供了一種「即插即用」的選項：不必重新訓練大模型、不必在運行時做優化，只需要準備一支具有相機標註的樣本影片，做少量的 LoRA 微調，即可獲得可控鏡頭的生成能力。這對需要快速迭代或資源受限的應用（例如廣告、虛擬製作、實時互動）特別具吸引力。  

🔗 **論文連結**  
📝 Warp-as-History: Generalizable Camera-Controlled Video Generation from One Training Video  
👤 Yifan Wang, Tong He @ Shanghai Jiao Tong University; Shanghai AI Laboratory; Shanghai Innovation Institute  
🔗 https://arxiv.org/abs/2605.15182  

#AI #視訊生成 #相機控制 #LoRA #ShanghaiJiaoTong #CVPR2026 #可控生成 #技術分享
