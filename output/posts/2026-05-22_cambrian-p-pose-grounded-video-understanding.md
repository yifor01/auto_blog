---
title: "Cambrian-P: Pose-Grounded Video Understanding"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.22819
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:51:04.042843
---

📌 【Cambrian-P】讓 AI 看影片時也懂相機位置  

你有沒有想過，AI 看影片就像在看一堆斷裂的快照？它缺少了我們最直覺的線索：相機在哪裡、指向哪個方向。  

🤔 **相機姿態是多模態模型的盲點**  
現有的多模態大語言模型將影片處理成一系列獨立的 2D 畫面，忽略了每個視角的位置與方向所構成的共享空間座標。這使得模型在需要理解物體相對位置、運動軌跡或場景幾何時，缺乏人類自然具備的三維線索。  

🧪 **為每幀加入可學習的相機 token 與姿態回歸頭**  
Cambrian-P 在視訊多模態大語言模型的架構中，為每幀引入一組可學習的相機 token，並附加一個姿態回歸頭。透過精心設計的抽樣策略，該模型能在訓練過程中同時學習視覺語義與相機的六自由度姿態。  

 **在空間推理基準上提升 4.5%~6.5%，並在八個其他影片問答基準上泛提升**  
實驗顯示，Cambrian-P 在空間推理基準（如 VSI‑Bench）上相較於基線模型獲得 4.5%~6.5% 的絕對提升。此外，該模型在八項額外的空間與一般影片問答基準上皆表現出一致的泛化改善。作為副產品，它在 ScanNet 上實現了最佳的串流姿態估計效果。  

💡 **姿態資訊不僅幫助空間推論，連一般影片問答也受益**  
有趣的是，利用野外影片產生的偽標註姿態進行進一步訓練，反而提升了一般影片問答基準的成績。這表明相機姿態不只是純粹的幾何輔助，它作為一種物理世界的訊號，能協助模型在更廣泛的視訊理解任務中建立更正確的時空關聯。  

⚠️ **僅依賴合成姿態與有限基準，長尾場景效果尚未驗證**  
目前的結果主要來自合成或半合成的姿態標註，以及幾個特定的學術基準。對於真實世界中極端光線、遮蔽或快速運動的長尾場景，模型的行為仍需進一步驗證。  

🎯 **未來影片模型應將姿態視為基本訊號，易於插入現有架構**  
這項工作表明，將相機姿態作為輕量級監督訊號注入多模態大語言模型，不僅實現簡單，而且能帶來跨任務的效能提升。對於希望讓模型更貼近人類對實體空間感知的研究與工程團隊，這提供了一條低成本且具潛力的改進路徑。  

🔗 **論文連結**  
📝 Cambrian-P: Pose-Grounded Video Understanding  
👤 Jihan Yang, Zifan Zhao, Xichen Pan, Shusheng Yang, Junyi Zhang (New York University; UC Berkeley; Meta FAIR)  
🔗 https://arxiv.org/abs/2605.22819  

你認為在訓練影片理解模型時，該不該把相機姿態當作必備輸入？歡迎在留言區分享你的看法 👇  

#AI #ComputerVision #VideoUnderstanding #MultimodalML #PoseEstimation #CambrianP #NYU #UCBerkeley #MetaFAIR
