---
title: "PixVerve: Advancing Native UHR Image Generation to 100MP with a Large-Scale High-Quality Dataset"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.20147
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-20T21:14:59.910794
---

📌 **PixVerve：開啟100MP原生圖像生成**

你見過 AI 生成的圖片，解析度竟能達到 1 億像素嗎？  
傳統 Text‑to‑Image 模型多停留在 1K‑2K 解析度，  
但最新研究卻直接衝向 100MP，開啟超高解析視覺新紀元。

🤔 **UHR 需求爆發，但資料稀缺成為瓶頸**  
隨著顯示技術與影像應用對細節的極端追求，超高解析度（UHR）圖像需求急遽上升。然而，現有公開資源多集中在 1K‑2K 範圍，缺乏足夠解析度與標註豐富的圖文對，導致模型在更高解析度上訓練困難。

🧪 **PixVerve‑95K：95K 張、每張≥100M 像素的開源 UHR 資料集，附七維標註**  
論文首次發布 PixVerve‑95K，內含 95K 張圖片，每張最低像素數達 100 M（約 100MP），覆蓋多種場景。除了圖文配對，資料集還提供七維標註（例如物體、材質、光線、風格等），為後續模型訓練與評估奠定高品質基礎。基於此資料集，研究團隊探索了三種不同的訓練方案，使多種既有 T2I 基礎模型能以原生方式直接產出 100MP 圖像。

🔍 **成功將多種 T2I 基礎模型延伸至原生 100MP 生成，並提出全面評估基準**  
透過上述訓練策略，論文證明既有模型在未額外增加參數規模的情況下，可在 100MP 解析度下保持圖像的視覺保真度與語意對齊。為全面衡量 UHR 生成效果，研究者設計了 PixVerve‑Bench 評估基準，結合傳統畫質指標（如 FID、IS）與多模態大語言模型的語意一致性評估，提供視覺品質與語意準確度的雙重視角。

💡 **資料品質與訓練策略是突破解析度瓶頸的關鍵**  
實驗顯示，資料集的高解析度與細膩七維標註，使模型在學習細部紋理與空間結構時獲得更強的先驗。同時，三種訓練方案中，以逐步提升解析度的累積式微調與對抗式細節增強，在保持訓練穩定性的同時，有效降低高解析度生成常見的失真與 artefactual 問題。這說明，資料的品質與訓練流程的設計，才是推動 UHR 生成的核心杠桿。

⚠️ **僅報告訓練與基準設計，尚未公開大規模人類主觀評估或長穩定性測試**  
論文主要聚焦於資料集建構、訓練方案探討與自動評估基準的提出。雖然提供了豐富的自動化指標，但未詳細報告大規模人類主觀研究（例如平均意見分數）或模型在長時間生成、不同硬體平台上的穩定性表現。這意味著實際產線應用前，仍需進一步驗證模型在真實使用場景中的可靠性。

🎯 **研究者可直接使用 PixVerve‑95K 與 PixVerve‑Bench 進行 UHR 模型開發與評估**  
- 資料集與評估腳本已開源，可即時下載用於實驗。  
- 三種訓練方案提供了可參考的起點，團隊鼓勵社群基於此進行消融與創新。  
- 結合多模態 LLM 的語意評估，可更全面檢視模型在高解析度下的概念理解與細節保存程度。

🔗 **論文連結**  
📝 PixVerve: Advancing Native UHR Image Generation to 100MP with a Large-Scale High-Quality Dataset  
👤 Haojun Chen, Haoyang He, Chengming Xu, Qingdong He, Junwei Zhu  
🏫 Zhejiang University; Fudan University; Nanjing University; National University of Singapore; Tsinghua University; Nanyang Technological University  
🔗 https://arxiv.org/abs/2605.20147  

你對 100MP 級別的 AI 圖像生成有什麼期待或疑問？歡迎在留言區分享 👇  

#AI #TexttoImage #UHR #PixVerve #GenerativeAI #ComputerVision #OpenDataset #CVPR2026 #ZhejiangUniversity #FudanUniversity #NUS #Tsinghua #NTU
