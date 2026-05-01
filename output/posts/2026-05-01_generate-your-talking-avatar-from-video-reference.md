---
title: "Generate Your Talking Avatar from Video Reference"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.27918
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-01T20:11:50.369920
---

📌 【HeyGen Research】用影片取代圖片，生成跨場景高保真 Talking Avatar

目前大多數數位人技術都依賴一張靜態圖片作為參考，這就像試圖用一張「照片」去推測一個人的所有動態表情。但 HeyGen Research 與學術界的最新合作指出，這種單一視角的限制，正是導致合成效果在換背景時顯得僵硬、缺乏表情連貫性的核心原因。

🤔 **單張圖像的瓶頸：缺乏時間維度與跨場景適應力**

現有的 Talking Avatar 方法多採用 Image-to-Video 管線，這在目標場景與參考圖一致時表現尚可。然而，一旦涉及背景替換或跨場景遷移，單張圖像提供的外觀訊息過於稀疏，無法捕捉細微的表情變化與時間序列上的動態特徵，導致生成結果的身分一致性和真實感大幅下降。

🧪 **TAVR 框架：引入視頻參考與三階段訓練**

南洋理工大學、墨爾本大學與 HeyGen Research 團隊提出了 TAVR (Talking Avatar generation from Video Reference)。不同於傳統做法，TAVR 接受「跨場景影片」作為輸入。為了處理更長的時間上下文並解決場景差異，團隊設計了三個關鍵技術環節：

1. **Token 選擇模組**：有效過濾並提取影片中的關鍵特徵。
2. **三階段訓練**：
   - **同場景預訓練**：建立基礎的外觀複製能力。
   - **跨場景微調**：讓模型學會在不同場景下維持身分特徵。
   - **強化學習對齊**：利用身分獎勵（Identity-based rewards）最大化生成結果與目標人物的相似度。

 **跨場景表現超越基準，已部署至生產環境**

研究團隊構建了一個包含 158 組精選跨場景視頻對的新基準 (Benchmark)。實驗結果顯示，TAVR 在定量指標與定性觀察上均穩定超越現有基準模型。特別值得一提的是，這項技術已經從實驗室走向實戰，目前**已部署於 HeyGen 的生產環境**中，這意味著該技術具備極高的實用性與穩定性。

💡 **從「複製外觀」到「理解身分」的技術演進**

TAVR 的核心突破在於將參考源從「空間維度（圖片）」擴展到「時空維度（影片）」。透過強化學習階段的身分獎勵機制，模型不僅是在模仿像素，而是在嘗試最大化身分特徵的保留。這解決了過去生成式模型在跨場景時容易出現的「身分漂移」問題。

⚠️ **數據集規模與場景多樣性的挑戰**

雖然論文構建了 158 組的專用基準，但相較於大型視覺模型的訓練數據，這個規模仍屬有限。此外，模型在極端光照或大幅度動作下的泛化能力，仍需在更廣泛的生產數據中持續驗證。

🎯 **數位人產品化的關鍵一步**

對於開發者與內容創作者而言，TAVR 證明了影片級參考在生成質量上的必要性。這也提示我們，未來在訓練客製化 Avatar 時，提供一段高質量、多角度的參考影片，將比單張照片帶來更自然的生成效果。

🔗 **論文連結**
📝 Generate Your Talking Avatar from Video Reference
👤 Zujin Guo, Zhenhui Ye, Yi Ren, Yuanming Li, Ce Chen
🏫 Nanyang Technological University; University of Melbourne; HeyGen Research
🔗 論文：https://arxiv.org/abs/2604.27918
🔗 HeyGen Research：https://www.heygen.com/research

你覺得數位人生成最難解決的技術難點是什麼？是表情細膩度還是聲音同步？歡迎留言討論 👇

#AI #ComputerVision #TalkingAvatar #HeyGen #數位人 #生成式AI #Deepfake #NTU #多模態學習
