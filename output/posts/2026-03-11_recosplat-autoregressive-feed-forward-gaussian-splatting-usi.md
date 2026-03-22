---
title: "ReCoSplat: Autoregressive Feed-Forward Gaussian Splatting Using Render-and-Compare"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.09968
score: 113
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-11T18:30:29.935257
---

📌 【ReCoSplat】用「看過去畫過來」解決視覺重建的 pose 不一致問題

當相機圍繞場景移動時，如何從不斷湧入的畫面中重建 3D 場景？Gaussian Splatting 在視覺效果上已經相當驚豔，但長期存在一個關鍵挑戰：當使用預測的相機姿態 (predicted poses) 而非真實姿態 (ground-truth poses) 時，重建品質會大幅下降。

🤔 **重建 3D 場景的 pose 不一致困境**

Gaussian Splatting 重建場景時，需要知道每張照片的相機姿態。如果使用真實姿態訓練，模型會穩定收斂，但實務上我們只能預測姿態，導致訓練時與推論時的輸入分布不一致 (train-test mismatch)，進而影響重建品質。

🧪 **ReCo: 用「看過去畫過來」解決分布不一致**

ReCoSplat 提出 Render-and-Compare (ReCo) 模組，核心概念很直觀：用**當前重建的場景**，從**預測的視角**渲染一張圖片，然後與**實際觀察到的圖片**比較，用這個比較結果作為穩定的條件訊號。

這就像在說：「我用預測的姿態看過去，畫出來的東西應該跟你實際看到的一樣。」這個方法有效補償了姿態預測的誤差，讓模型在推論時也能保持穩定表現。

🎯 **核心創新點**

- **ReCo 模組**: 用渲染比較提供穩定條件訊號，解決 pose 不一致問題
- **KV cache 壓縮**: 結合 early-layer truncation 與 chunk-level selective retention，100+ 幀壓縮 90% 以上
- **通用輸入支援**: 支援有無相機內參、有無相機姿態的各種輸入設定

⚡ **效率突破：100+ 幀壓縮 90% 以上**

對於長序列視頻重建，ReCoSplat 提出混合的 KV cache 壓縮策略：
- Early-layer truncation: 早期層只保留部分記憶
- Chunk-level selective retention: 按塊選擇性保留重要資訊

這讓模型能處理超過 100 幀的長序列，同時大幅降低記憶體需求。

 **超越現有方法的視覺效果**

ReCoSplat 在各種輸入設定下都達到 state-of-the-art 表現：
- 有 pose + 有內參
- 無 pose + 有內參  
- 無 pose + 無內參

在 in-distribution 與 out-of-distribution 的 benchmark 上都展現優異性能。

⚠️ **研究限制與考量**

- 仍依賴一定數量的初始觀察來建立場景基礎
- 壓縮策略可能在極端長序列中仍有優化空間
- 模型複雜度增加可能影響推論速度

🎯 **實務應用價值**

- **AR/VR 內容創作**: 從手機拍攝快速重建沉浸式場景
- **智慧監控**: 從多角度影片重建 3D 場景進行分析
- **自駕車感知**: 從連續觀察建立環境的 3D 理解

🔗 **論文連結**
📝 ReCoSplat: Autoregressive Feed-Forward Gaussian Splatting Using Render-and-Compare
👤 Freeman Cheng, Botao Ye, Xueting Li, Junqi You, Fangneng Zhan
🏫 University of California Merced; ETH Zurich; NVIDIA; Shanghai Jiao Tong University; Hong Kong University of Science and Technology
🔗 論文：arxiv.org/abs/2603.09968
🔗 專案頁面：freemancheng.com/ReCoSplat

Gaussian Splatting 的 pose 問題終於有了解決方案！你認為這項技術最有潛力的應用場景是什麼？歡迎討論 👇

#GaussianSplatting #3DReconstruction #ComputerVision #PoseEstimation #NVIDIA #AI研究 #視覺計算
