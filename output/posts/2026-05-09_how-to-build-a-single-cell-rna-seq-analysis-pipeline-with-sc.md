---
title: "How to Build a Single-Cell RNA-seq Analysis Pipeline with Scanpy for PBMC Clustering, Annotation, and Trajectory Discovery"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/08/how-to-build-a-single-cell-rna-seq-analysis-pipeline-with-scanpy-for-pbmc-clustering-annotation-and-trajectory-discovery/
score: 66
model: tencent/hy3-preview:free
generated_at: 2026-05-09T19:42:32.318582
---

📌 **Scanpy PBMC 單細胞分析教學**  

你是否曾覺得單細胞 RNA‑seq 分析流程繁瑣，不知從哪裡開始？一份完整的教學能否讓你直接上手，從品質控制到軌跡追蹤一氣呵成？  

🤔 **單細胞分析的門檻在哪裡？**  
PBMC（周邊血單核細胞）是單細胞 transcriptome 常用的基準資料集，涵蓋 T 細胞、B 細胞、NK 細胞、單核球等多種免疫細胞。正確地進行品質控制、正規化、聚類與標註，是後續功能解讀（如 interferon 反應、分化軌跡）的前提。然而，許多新手在這些步驟上會因參數選擇或工具鏈不熟悉而卡住。  

🧪 **以 Scanpy 為核心的完整工作流程**  
本教學使用 PBMC‑3k 基準資料集，示範從資料載入到結果保存的每一個環節：  

1. **載入與檢查** – 讀取 h5ad 檔案，確保基因名稱唯一，檢視 AnnData 結構。  
2. **品質控制** – 計算線粒體與核糖體基因比例，繪製小提琴圖與散佈圖，篩選低品質細胞與低表達基因。  
3. **雙體細胞偵測** – 透過 Scanpy 整合的 Scrublet，預測並移除潛在的雙體。  
4. **正規化與變換** – 保存原始計數，進行總計數正規化、對數轉換，挑選高變異基因。  
5. **細胞週期評分** – 定義 S 期與 G2/M 期標誌基因，為每個細胞計算週期分數，並將總計數與線粒體百分比的技術變異迴歸掉。  
6. **尺度縮減** – 執行 PCA，檢視解釋方差（僅說明已執行），接著計算 UMAP 與 t‑SNE 以供視覺化。  
7. **聚類與標註** – 使用 Leiden 演算法進行細胞聚類，尋找標記基因，參照經典 PBMC 標誌（如 CD3D、MS4A1、GNLY 等）完成細胞類型標註。  
8. **軌跡探索** – 建立 PAGA 圖，計算擴散偽時間，初步探討細胞分化或激活軌跡。  
9. **自訂評分** – 根據 interferon 反應基因集，計算每個細胞的 interferon‑response 分數。  
10. **結果保存** – 將完整處理後的 AnnData 物件寫入磁碟，供後續分析或重複使用。  

💡 **每一步的設計考量**  
- 品質控制不僅去除低讀數細胞，亦能降低線粒體污染帶來的偏誤。  
- Scrublet 的雙體偵測在大規模資料中尤為重要，避免人工合成的基因表現偽象。  
- 對數正規化與高變異基因選擇是多數下游方法（PCA、聚類）的標準前處理，可保留生物變異而抑制技術噪音。  
- 迴歸細胞週期與線粒體百分比，旨在減少這兩個已知的混淆因子，使後續聚類更側重於真實的表型差異。  
- Leiden 演算法在保持聚類穩定性的同時，提供可調節的解析度參數，方便依據研究需求微調。  
- PAGA 與擴散偽時間提供了無需監控的軌跡推斷，適合初步探索分化路徑或激活狀態。  
- 自訂評分方式展示了如何將已知基因集合併入 Scanpy 的觀測欄位，方便後續可視化或統計檢定。  

⚠️ **教學的邊界與適用範圍**  
- 本文僅以 PBMC‑3k 為示範資料集，步驟參數（例如過濾門檻、PCA 主成分數）可能需依據實際樣本特性重新調整。  
- 未涉及批次效應校正（如 Harmony、BBKNN）或多樣本合併分析，若您的實驗包含多個捐贈者或不同平台，需另行加入對應步驟。  
- 教學使用的是傳統的 Scanpy 工作鏈，並未引入新穎的演算法或最新的模型（例如深度學習基礎模型），因此在方法創新方面屬於標準最佳實踐。  
- 文中未提供實際的數值結果（例如聚類數目、U MAP 分佈圖），僅說明了流程執行的步驟，讀者仍需自行執行程式碼以觀察具體結果。  

🎯 **實務上的建議**  
- 先在小規模子集上跑完整管線，確認每個步驟的輸出是否符合預期，再擴大至完整資料集。  
- 若您的研究聚焦於特定免疫亞種群，可在標註階段加入更具體的標誌基因或使用已有的細胞類型註釋工具（如 SingleR、scCATCH）進行對照。  
- 對於希望追蹤動態過程的實驗，建議將擴散偽時間與已知的激活標誌（如 IFN‑stimulated genes）進行相關性檢定，以驗證軌跡的生物學意義。  
- 最後，將處理好的 AnnData 物件版控（例如使用 Git‑LFS 或資料管理平台），方便團隊成員重現分析或在新假設上進行快速迭代。  

🔗 **原始教學連結**  
📝 How to Build a Single-Cell RNA-seq Analysis Pipeline with Scanpy for PBMC Clustering, Annotation, and Trajectory Discovery  
👤 Sana Hassan (MarkTechPost)  
🔗 https://www.marktechpost.com/2026/05/08/how-to-build-a-single-cell-rna-seq-analysis-pipeline-with-scanpy-for-pbmc-clustering-annotation-and-trajectory-discovery/  

你有試過用 Scanpy 處理 PBMC 或其他免疫細胞資料嗎？歡迎在留言區分享你的經驗或遇到的挑戰 👇  

#單細胞RNAseq #Scanpy #PBMC #生物資訊 #資料分析教學 #MarkTechPost #SanaHassan #細胞聚類 #軌跡推斷 #interferon反應
