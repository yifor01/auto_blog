---
title: "TETO: Tracking Events with Teacher Observation for Motion Estimation and Frame Interpolation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.23487
score: 120
model: gpt-4o-free
generated_at: 2026-03-25T19:26:00.999789
---

**TETO：25分鐘真實數據教 Event Camera 估運動**

你以為 Event Camera 需要大量合成資料才能學會估運動？TETO 用只有 25 分鐘的未標註真實錄影，就能透過老師學生蒸餾達到最佳效果。這意味著機器人與 AR/VR 系統未來可能只需少量實地采集即可獲得高精度運動估計。

**合成資料鴻溝讓 Event Camera 運動估計難以落地**  
Event 機器能以微秒級解析度捕捉每個像素的亮度變化，提供連續的運動資訊，這是傳統相機在幀之間所遺失的。然而，現有的事件基礎運動估計器仰賴大規模合成資料，而合成與真實之間的鴻溝往往導致效能大打折扣。如何在不依賴龐大合成資料庫的情況下，直接從真實世界錄影中學習運動估計，成為該領域的關鍵挑戰。

**老師學生框架利用預訓練 RGB Tracker 進行知識蒸餾**  
TETO 提出一種師生蒸餾架構：先利用在常見 RGB 影像上預訓練好的追蹤模型作為「老師」，從該老師模型的輸出中蒸餾知識給學生網路，學生網路則專門處理事件流。為了從極少的未標註資料中學到有用的訊號，研究團隊設計了運動感知的資料策選與查詢抽樣策略，明確分離物體自身運動與 dominante ego‑motion（自身移動引起的背景流），使學生能在只有約 25 分鐘的真實事件錄影上有效地學習點軌跡與密集光流的聯合預測。

**僅用約 25 分鐘真實資料即達 EVIMO2 點追蹤與 DSEC 光流 SOTA**  
實驗顯示，該學生估計器在 EVIMO2 基準上達成了最新的點追蹤表現，並在 DSEC 上達到最新的光流結果，訓練資料量僅是傳統合成資料方法的萬分之一。更重要的是，這些運動估計被直接作為顯式運動先驅，條件化一個預訓練的 Video Diffusion Transformer，進而在 BS-ERGB 與 HQ-EVFI 兩個幀插值基準上展現出更佳的插值品質，說明精準的運動估計能直接轉化為下游任務的提升。

**運動先驅條件化的 Video Diffusion Transformer 提升幀插值品質**  
由 TETO 產出的點軌跡與密集光流被視為運動先驅，注入到視頻擴散變換器中，使模型在生成中間幀時能更精確地遵循真實運動軌跡。此設計讓框架不僅在點追蹤與光流上優於現有方法，也在幀插值任務上獲得顯著的品質提升，證明運動先驅的顯式引入是提升擴散模型時域一致性的有效途徑。

**實驗主要聚焦戶外與特定場景，長時間序列與極端光照表現未知**  
目前的驗證僅限於 EVIMO2、DSEC、BS-ERGB 與 HQ-EVFI 四個基準，這些資料集多為戶外或室內結構化場景。對於長時間序列、快速光線變化或極端低光環境下的表現，文中未提供進一步探討，因此泛化能力仍需後續工作補強。

**對機器人、AR/VR 與低延遲視覺系統意味著可大幅降低資料收集成本**  
由於只需少量未標註的真實事件錄影即可獲得高品質的運動估計，TETO 大幅降低了對昂貴合成資料產生與標註的依賴。對於需要即時運動感知的機器人導航、擴增實境與虛擬實境系統，這種「少資料、高效能」的學習範式不僅縮短了系統部署的準備時間，也降低了能源與計算開銷，為實際應用帶來具體的經濟與技術優勢。

**論文連結**  
📝 TETO: Tracking Events with Teacher Observation for Motion Estimation and Frame Interpolation  
👤 Jini Yang, Eunbeen Hong, Soowon Son, Hyunkoo Lee, Sunghwan Hong (KAIST AI; ETH Zurich; Korea Aerospace University)  
🔗 https://arxiv.org/abs/2603.23487  

你是否也在思考如何用最少的真實資料訓練高感知模型？歡迎在留言區分享你的看法與經驗 👇

#AI #EventCamera #MotionEstimation #FrameInterpolation #KnowledgeDistillation #KAIST #ETHZurich #ComputerVision #ARVR #Robotics
