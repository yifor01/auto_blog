---
title: "Identity-Consistent Multi-Pose Generation of Contactless Fingerprints"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.03830
score: 109
model: tencent/hy3-preview:free
generated_at: 2026-05-06T20:21:14.328198
---

📌 【清華大學最新研究】用物理與擴散模型，把「非接觸指紋」變成標準座標的可靠訓練資料

非接觸指紋識別雖然衛生又靈活，但手指在 3D 空間自由擺動時造成的嚴重幾何扭曲，讓系統很難對齊傳統接觸式指紋的資料分佈。現有方法多靠顯式幾何校正或影像增強，一旦遇到極端姿態就容易失效。

🤔 **非接觸指紋的自由姿態，正在拉大跨模態的認識落差**

傳統指紋比對建立在「穩定接觸」的假設上，但現實應用中難以避免手指偏移、彎曲或遠近變化。這種由姿態帶來的非線性扭曲，不僅降低識別穩定度，也限制了模型在跨模態場景下的泛化能力。

🧪 **物理啟發的三階段框架，結合擴散模型與 3D 姿態模擬**

清華大學團隊提出 IMPOSE（Identity-Consistent Multi-Pose Generation of Contactless Fingerprints），在 UWA 與 PolyU CL2CB 資料集上進行驗證。方法包含三個階段：
- 以離散碼本表示的潛力擴散模型，生成卷積指紋層級的身份基礎；
- 以 Sauvola 區域自適應二值化作為身份錨點，將卷積模態轉譯至非接觸模態；
- 透過 3D 手指模型的紋理貼圖與投影，進行物理驅動的多姿態模擬。

生成的樣本在紋理拓撲層級保持嚴格身份一致性，並對齊標準指紋座標空間。

 **在 UWA 上將等錯誤率降至 8.74%，在 PolyU CL2CB 上達到 2.26%**

使用 IMPOSE 合成資料微調固定長度密集描述子（FDD），在跨模態比對上達到現行最佳水準；DeepPrint 與 AFRNet 等主流表示方法也獲得穩定提升。進一步結合合成與真實資料的混合策略，展現出最佳整體表現。

💡 **以身份一致性為核心的生成策略，取代單純幾何校正**

與依賴顯式幾何校正或影像增強的方法不同，IMPOSE 將姿態變化視為可模擬的過程，並在生成階段即約束身份一致性。Sauvola 基礎的二值化錨點設計，提供跨模態的穩定對齊依據；而物理驅動的 3D 投影則確保姿態變化符合真實成像規律，降低模型對域差的過度擬合。

⚠️ **樣本與設定受限，長期部署效果仍需驗證**

研究以公開指紋資料集為主，極端場景與大規模部署下的穩定度尚未探討；方法依賴 3D 手指模型與投影設定的精確性，實際應用中若成像條件偏差可能影響生成品質；此外，雖提供開源程式碼與生成樣本，模型在跨裝置、跨環境下的泛化能力仍有待進一步檢驗。

🎯 **合成資料可作為穩健訓練補強，開放實驗有利落地驗證**

- 在指紋識別任務中，物理驅動的多姿態合成資料能有效縮小跨模態域差；
- 結合真實與合成資料的混合訓練策略，比單一資料來源更具穩健性；
- 開源實作與生成樣本提供工程團隊可驗證的基線，適合用於資料擴增與模型微調。

🔗 **論文連結**  
📝 Identity-Consistent Multi-Pose Generation of Contactless Fingerprints  
👤 Zhiyu Pan, Xiongjun Guan, Jianjiang Feng, Jie Zhou（Tsinghua University）  
📑 CVPR / arXiv:2605.03830  
💻 GitHub: https://github.com/Yu-Yy/IMPOSE  

你的團隊是否有使用合成資料來處理生物識別的跨模態問題？歡迎分享經驗與挑戰 👇  

#AI #ComputerVision #Biometrics #DeepLearning #資料合成 #指紋識別 #CVPR #TsinghuaUniversity
