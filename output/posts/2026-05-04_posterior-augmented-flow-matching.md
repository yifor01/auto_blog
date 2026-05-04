---
title: "Posterior Augmented Flow Matching"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.00825
score: 119
model: tencent/hy3-preview:free
generated_at: 2026-05-04T20:02:02.503280
---

📌 【PAFM】用「多終端混合理想」修補 Flow Matching 的記憶化漏洞

Flow matching 讓影像生成更快更穩，但高維圖像的空間太廣、軌跡太稀疏，模型常靠「記住特定起訖對」來走捷徑，導致 flow collapse：多樣輸入被壓縮成相似輸出。最新研究指出，這不僅拉低生成品質，更會放大梯度方差，讓訓練更不穩定。

🤔 **用單一目標學高維影像，模型被迫走捷徑**

在 flow matching 中，每個訓練樣本只提供單一時間軸上的單一點與單一終點；到了高維影像空間，這種「點對點」的監督極度稀疏。模型容易將不同起點導向過度趨同的終點，以記憶特定配對來應付訓練，導致泛化受阻、梯度方差居高不下。

🧪 **後驗混合目標取代單一終點的 flow matching**

研究團隊提出 Posterior-Augmented Flow Matching (PAFM)，在理論上擴充 flow matching 的監督機制。PAFM 不要求單一終點，而是對給定中間態與條件，建構「合理終點」的近似後驗期望；並將該後驗分解為：

- 該中間態在假設終點下的似然  
- 該終點在條件下的先驗機率  

再透過重要性取樣組成多終點混合目標，讓每個中間態同時向多條合理延續軌跡學習。

📈 **在 SiT 與 MMDiT 上穩定提升 3.4 FID50K**

- 架構：SiT-B/2、SiT-XL/2、MMDiT  
- 條件設定：類別條件（ImageNet）與文字條件（CC12M）  
- 生成指標：FID50K 最多改善 3.4  
- 計算開銷：幾乎無顯著增加  

結果顯示，PAFM 在不同模型尺度與任務中一致降低梯度方差、提升穩定性，並有效緩解 flow collapse。

💡 **從「記住配對」轉向「聚合合理延續」**

PAFM 的關鍵在於用混合後驗取代單一監督：每個中間態不再被單一終點牽引，而是匯整許多合理終點的訊號。這使模型被迫學習更廣泛的延續空間，降低對特定起訖對的依賴，並在梯度更新中取得更低方差的估計。

⚠️ **依賴近似後驗與重要性取樣的品質**

方法效果取決於近似後驗的建構是否合理，且重要性取樣的效率會隨候選終點數量而變化；研究未探討極端高階語意條件或極高解析度設定下的穩定性長尾問題。

🎯 **對 DiT/SiT 訓練與調參的具體啟示**

- 可直接替換現有 flow matching 損失，無需大幅調整架構  
- 適合用於提升大尺寸影像模型的訓練穩定性與收斂品質  
- 開源實作可用於快速驗證與消融分析  

🔗 **論文連結**  
📝 Posterior Augmented Flow Matching  
👤 George Stoica, Sayak Paul, Matthew Wallingford, Vivek Ramanujan, Abhay Nori  
👥 Georgia Tech; University of Washington; Hugging Face; Ai25; UC Irvine  
🔗 論文：arxiv.org/abs/2605.00825  
💻 程式碼：github.com/gstoica27/PAFM.git  

你在訓練 DiT/SiT 時是否曾遇到 flow collapse 或梯度方差過大的問題？你會嘗試用多終點混合目標來穩定訓練嗎？歡迎留言討論 👇

#AI #生成模型 #FlowMatching #DiT #SiT #影像生成 #機械學習 #研究解析
