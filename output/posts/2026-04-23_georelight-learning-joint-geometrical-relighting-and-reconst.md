---
title: "GeoRelight: Learning Joint Geometrical Relighting and Reconstruction with Flexible Multi-Modal Diffusion Transformers"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.20715
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-04-23T19:55:34.916075
---

📌 【Meta 研究】聯合幾何與重打光的多模態 DiT

單張人像重打光（Relighting）是業界長期的痛點，現有方法要麼誤差層層累積，要麼忽略3D幾何導致光影違和。
Meta 團隊提出全新框架 GeoRelight，用統一模型同時解幾何重建與重打光，物理一致性顯著提升。
這項研究對3D人像渲染、虛擬化身等應用極具參考價值。

🤔 **單張人像重打光是病態問題，現有方法難兼顧精度與物理一致性**
單張2D人像圖像模糊了3D幾何、固有外觀與光照資訊，要從單張圖還原任意光照下的效果，本質上是病態（Ill-posed）問題。現有方法分為兩類：一類是順序管線，先估計3D幾何再執行重打光，容易出現誤差累積；另一類則不顯式利用3D幾何資訊，重打光的物理一致性嚴重受限。事實上，重打光與3D幾何估計是互為助力的任務，卻鮮少有研究將兩者統一優化。

🧪 **統一多模態擴散Transformer結合兩大核心技術**
Meta Codec Avatars Lab 聯合圖賓根大學、馬克斯普朗克資訊學研究所的團隊提出 GeoRelight，核心是一個統一的多模態擴散Transformer（DiT），同時輸出3D幾何與重打光結果。關鍵技術突破包含兩項：
1. 各向同性 NDC 正交深度（iNOD）：一種無失真的3D表徵，可相容潛在擴散模型的訓練流程，解決傳統3D表徵的變形問題。
2. 策略性混合數據訓練法：結合高品質合成數據與自動標註的真實數據，平衡數據多樣性與標註成本。

💡 **聯合優化幾何與重打光，效果優於現有方法**
實驗結果顯示，GeoRelight 的效能優於傳統順序管線模型，也勝過過往未顯式利用3D幾何的重打光系統，驗證了聯合優化的有效性。

💡 **幾何與重打光互為助力，統一建模解決痛點**
重打光需要精準的3D幾何資訊計算光照傳播，而3D幾何重建也需要正確的光照資訊還原物體表面屬性，兩者聯合優化可互相修正誤差，避免順序管線的誤差傳遞；同時顯式引入幾何約束，也讓重打光的結果更符合物理規律，解決過往方法光影違和的問題。

⚠️ **摘要未提及具體限制，完整細節待查**
本篇貼文僅基於論文公開摘要撰寫，摘要中未提及作者說明的研究限制，也未提供具體實驗數據與對比基線。有興趣的讀者可參考完整論文了解詳細實驗設計與限制說明。

🎯 **3D人像渲染可參考聯合建模思路**
這項研究對3D人像渲染、AR/VR虛擬化身（如Meta Codec Avatars）等領域極具參考價值。開發者可借鑒其聯合優化幾何與光照的思路，提升渲染結果的物理一致性。若後續有開源實作，工程師可快速試驗相關技術，降低開發門檻。

🔗 **論文連結**
📝 論文標題：GeoRelight: Learning Joint Geometrical Relighting and Reconstruction with Flexible Multi-Modal Diffusion Transformers
👤 作者：Yuxuan Xue, Ruofan Liang, Egor Zakharov, Timur Bagautdinov, Chen Cao（機構：Codec Avatars Lab, Meta; University of Tübingen; Max Planck Institute for Informatics, Saarland Informatics Campus）
📚 來源：Computer Vision and Pattern Recognition
🔗 論文連結：https://arxiv.org/abs/2604.20715

#AI #ComputerVision #3D渲染 #MetaAI #DiffusionModel #人像處理 #機器學習 #虛擬化身
