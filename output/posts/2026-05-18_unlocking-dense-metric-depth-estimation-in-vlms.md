---
title: "Unlocking Dense Metric Depth Estimation in VLMs"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.15876
score: 116
model: tencent/hy3-preview:free
generated_at: 2026-05-18T20:17:01.114057
---

📌 【DepthVLM】讓 VLM 也能直接預測密集深度  

當 VLM 只能看圖片、寫描述時，它對空間的真實理解仍是空白。  
DepthVLM 透過輕量深度頭與兩階段訓練，讓單一模型同時輸出語言與完整解析度深度圖。  
這意味著，未來的多模態助手或機器人，可能在不犧牲語言能力的前提下，真正「看見」世界的幾何結構。  

🔹 **VLM 在 2D 任務上表現優異，但 3D 幾何感知仍受限**  
現有視覺語言模型在物件定位、圖像描述等二維任務上已達到很高的表現，然而它們的監督訊號多僅來自純文字，無法提供足夠的幾何約束，導致難以恢復密集的深度資訊。  

🔹 **輕量深度頭 + 兩階段統一視覺-語言訓練**  
作者在 VLM 的語言主幹上掛載一個參數量較小的深度頭，並採用統一的視覺-文字監督範式。訓練分為兩階段：先讓模型學會基本的視覺-語言對應，再引入深度監督，使得深度頭能在不破壞原有語言能力的情況下產生全解析度的 metric 深度圖，全部在一次前向傳遞中完成。  

🔹 **DepthVLM 在密集深度預測上優於現有 VLM，甚至超過部分純視覺模型，並提升複雜空間推理**  
實驗顯示，DepthVLM 在作者提出的室內-室外統一 metric 深度基準上，明顯優於既有的 VLM 方法；同時，它的推理效率更高，且在某些指標上已超過領先的純視覺深度估計模型。此外，模型在需要空間推理的下游任務上也有所改善，顯示出向真正統一基礎模型邁進的潛力。  

🔹 **統一訓練讓語言與深度任務互不干擾，避免外部蒸餾誤差**  
與先前需要從外部視覺模型蒸餾幾何資訊、或是透過逐像素查詢、粗糙 token 輸出的做法不同，DepthVLM 的深度頭直接與語言主幹共享特徵，並在同一訓練目標下優化。這種設計減少了誤差累積的風險，也讓模型在生成文字時仍能保留對幾何結構的敏感度。  

🔹 **作者未詳細說明在極端光線或遮蔽情況下的表現，具體邊界條件有待後續工作探索**  
論文著重於方法的有效性與開源計畫，但未提供對惡劣視野條件的消融實驗或失敗案例分析。這意味著在實際部署時，仍需進一步驗證其在強光、夜景或遮蔽場景下的穩定性。  

🔹 **對於需要即時語言與深度輸出的場景（如 AR、機器人導航）提供即用的開源模型**  
隨著程式碼與權重的公開釋放，從事多模態感知或三維推理的工程師可以直接將 DepthVLM 作為底座，在不犧牲對話能力的前提下獲得密集深度圖，加速從理解場景到決策行動的閉環。  

🔗 **論文連結**  
📝 Unlocking Dense Metric Depth Estimation in VLMs  
👤 Hanxun Yu, Xuan Qu, Yuxin Wang, Jianke Zhu, Lei ke (Zhejiang University; Tencent Hunyuan LLM; HKUST; Shenzhen Loop Area Institute)  
🔗 https://arxiv.org/abs/2605.15876  

你認為這種「一模多任務」的設計，會在未來的多模態系統中扮演什麼角色？歡迎在留言區分享你的見解 👇  

#AI #VisionLanguageModel #DepthEstimation #3DUnderstanding #Tencent #ZhejiangUniversity #HKUST #OpenSource #AR #Robotics
