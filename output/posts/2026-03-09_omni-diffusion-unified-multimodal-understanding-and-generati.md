---
title: "Omni-Diffusion: Unified Multimodal Understanding and Generation with Masked Discrete Diffusion"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.06577
score: 121
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-09T22:18:23.889306
---

📌 【Omni-Diffusion】擴散模型也能做 MLLM？首個任意模態轉換系統問世

大型語言模型（LLM）的架構設計似乎已經定型：Transformer + 自迴歸預測。但這個「標準答案」真的沒有更好的選擇嗎？

🤔 **擴散模型 vs. 自迴歸：誰才是 MLLM 的靈魂**

目前主流的多模態大語言模型（MLLM）都採用自迴歸架構，透過逐步預測下一個 token 來生成內容。這種方法雖然有效，但存在計算效率與建模複雜度限制。

擴散模型近年來在圖像生成領域大放異彩，透過逐步去噪過程生成高品質圖片。更有趣的是，擴散模型已經成功應用於視覺理解任務，展現了統一建模不同模態的潛力。

🧪 **Omni-Diffusion：完全基於擴散模型的任意模態系統**

南京大學、騰訊優圖與中科院計算所的團隊提出 Omni-Diffusion，這是**第一個完全基於遮罩式離散擴散模型的任意模態轉換系統**。

核心創新在於：Omni-Diffusion 使用統一的遮罩式離散擴散模型直接捕捉多模態 token 的聯合分布，透過單一架構同時支援理解與生成任務。

 **任意模態、任意轉換**

Omni-Diffusion 的特點是支援：
- 任意輸入模態（文字、語音、圖像）
- 任意輸出模態
- 統一的建模方式
- 理解與生成任務

這意味著你可以用圖片+文字輸入，輸出語音；或用語音輸入，輸出圖片+文字，所有任務都透過同一個模型完成。

⚡ **為什麼擴散模型可能更適合 MLLM**

相較於自迴歸模型，擴散模型具有幾個潛在優勢：
- 更好的聯合分布建模能力
- 更穩定的訓練動態
- 更靈活的輸入輸出組合
- 潛在的計算效率提升

💡 **超越現有多模態系統**

在多種評估基準上，Omni-Diffusion 表現與現有處理兩種以上模態的多模態系統相當或更優，證明擴散模型作為 MLLM 骨幹架構的巨大潛力。

🎯 **下一代多模態基礎模型的契機**

這項工作為多模態模型的架構設計開闢了新方向，顯示擴散模型不僅能生成圖片，還能成為統一理解與生成各種模態內容的基礎。

🔗 **論文連結**
📝 Omni-Diffusion: Unified Multimodal Understanding and Generation with Masked Discrete Diffusion
👤 Lijiang Li, Zuwei Long, Yunhang Shen, Heting Gao, Haoyu Cao
🏢 Nanjing University; Tencent Youtu Lab; CASIA
🔗 論文：arxiv.org/abs/2603.06577
🌐 專案頁面：omni-diffusion.github.io

你認為擴散模型會成為 MLLM 的下一個主流架構嗎？歡迎討論！

#AI #擴散模型 #MLLM #多模態 #機器學習 #南京大學 #騰訊優圖 #計算機視覺
