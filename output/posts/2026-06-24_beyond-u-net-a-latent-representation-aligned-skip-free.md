---
title: 'Beyond U-Net: A Latent-Representation-Aligned Skip-Free Backbone for Flow-Matching
  Speech Enhancement'
source: arXiv
url: http://arxiv.org/abs/2606.24745v1
score: 87
model: google/gemma-4-31b-it:free
generated_at: '2026-06-24T20:10:43.180753'
---

📌 【研究】捨棄 U-Net Skip Connection，用 LRA 對齊提升語音增強效能

TL;DR：提出一種 Skip-free 架構與 LRA 對齊機制，在 Flow Matching 語音增強中以極少次推論達到更高音質。

在語音增強（Speech Enhancement）領域，擴散模型與基於分數的模型（Score-based models）雖表現強勁，但其反覆疊代的取樣過程導致推論速度慢，難以達到即時部署的需求。

🤔 **Flow Matching 解決速度問題，但 U-Net 仍有缺陷**

為了提升效率，Flow Matching 透過常微分方程式（ODE）將雜訊語音導向乾淨語音，僅需少數次函式評估（Function Evaluations）即可完成，是更高效的替代方案。然而，傳統的 U-Net 架構依賴 Skip Connection（跳躍連線），這可能會將與雜訊相關的低階特徵直接傳遞給解碼器，進而影響最終的還原品質。

🧩 **捨棄 Skip Connection，引入潛在表示對齊 (LRA)**

為了克服上述問題，作者提出了一種「Skip-free」的編碼器-解碼器骨幹架構，並引入潛在表示對齊（Latent Representation Alignment, LRA）機制：

1. **移除跳躍連線**：不再使用 U-Net 的 Skip Connection，避免雜訊特徵的傳遞。
2. **利用預訓練 Codec 導向**：使用一個凍結的 Descript Audio Codec 編碼器-解碼器（不含量化過程）來提取乾淨語音的潛在特徵。
3. **對齊監督機制**：將模型的 Bottleneck（瓶頸層）與解碼器表示，與上述乾淨的潛在特徵進行對齊。這種監督方式能促使模型學習更精簡且乾淨的語音表示。

📊 **五次函式評估即可提升 PESQ 與感知品質**

在 WSJ0-CHiME3 與 VoiceBank-DEMAND 兩個資料集上的實驗結果顯示，該方法提升了 PESQ 指標與感知品質。特別是在 VoiceBank-DEMAND 資料集上，僅需 5 次函式評估即可取得顯著提升。

🎯 **實務啟示**

對於追求即時性（Real-time）的語音處理工程師，這項研究提供了一個新思路：透過對齊預訓練的潛在特徵（Latent Alignment），可以在移除 U-Net 複雜連線的同時，依然維持甚至提升生成品質，進而降低推論延遲。

🔗 **來源**
- 標題：Beyond U-Net: A Latent-Representation-Aligned Skip-Free Backbone for Flow-Matching Speech Enhancement
- 作者／機構：Wangyi Pu, Michele Scarpiniti
- 連結：http://arxiv.org/abs/2606.24745v1

#SpeechEnhancement #FlowMatching #DeepLearning #AudioProcessing #UNet #LRA #GenerativeModels #PESQ #RealTimeAI #AudioCodec
