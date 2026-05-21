---
title: "iTryOn: Mastering Interactive Video Virtual Try-On with Spatial-Semantic Guidance"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.21431
score: 112
model: tencent/hy3-preview:free
generated_at: 2026-05-21T20:42:09.450288
---

📌 **iTryOn：互動試衣的新突破**

你以為虛擬試衣只是模特兒走秀？當人開始抓衣服、調整領口時，AI 卻常常失靈。  
這正是現有 Video Virtual Try‑On (VVT) 方法的盲點——它只能處理被動展示的場景，無法應對真實試衣中的人與衣物互動。

🤔 **從被動展示到主動互動：一個被忽視的真實需求**  
傳統 VVT 研究專注於在影片中無縫替換服裝，並已在時間一致性方面取得進展。然而，實際試衣過程中，使用者會主動拉扯、摺疊或調整衣物，這些互動產生的姿態與衣物變形遠比靜態替換複雜。若模型無法理解這種「人‑衣」互動的語意與空間細節，生出的試衣影像會顯得僵硬或不自然。

🧪 **以空間‑語意雙層引導解決互動難題**  
論文提出全新任務 **Interactive Video Virtual Try‑On (Interactive VVT)**，並設計 iTryOn 框架來應對兩大挑戰：  
1. **空間層面的模糊**：標準姿態資訊無法區分手部與衣物的精準接觸點。iTryOn 引入一種 **garment‑agnostic 3D hand prior**，提供細緻的手部先驗，使模型能在空間上正確引導手‑衣接觸。  
2. **語意層面的稀疏**：互動往往只發生在少數幀中，僅靠全域文字描述難以捕捉局部動作。iTryOn 利用 **global caption** 供應全場景語境，同時引入 **time‑stamped action caption** 描述局部互動，並透過新設計的 **Action‑aware Rotational Position Embedding (A‑RoPE)** 使兩種語意資訊在時間上同步。  
整個架構建立在大規模影片 diffusion Transformer 之上，透過 multi‑level interaction injection mechanism 生成複雜的衣物形變與人體動作。

🔍 **在傳統與互動基準上皆表現領先**  
實驗顯示，iTryOn 不僅在既有的 VVT 基準集上達到 **state‑of‑the‑art** 性能，更在新提出的互動設定中取得明顯領先。具體來說，模型能更好地保持衣物在互動過程中的細節（如摺痕、布料拉伸），同時維持時間一致性，使生出的試衣影像更具真實感與可控性。

💡 **空間先驗與語意同步是關鍵創新**  
3D hand prior 提供了模型在缺乏明確姿態標註時的空間約束，減少了手‑衣接觸的猜測。而 A‑RoPE 則讓時間戳的動作描述能與影像幀精準對齊，使模型在互動稀疏時仍能學習到正確的局部變形。這兩層設計的結合，是 iTryOn 能在互動場景中超越既有方法的核心原因。

⚠️ **僅報告概念驗證，程式碼尚未開放**  
目前論文僅提供方法描述與實驗結果，**未發布原始程式碼或線上 demo**，這意味著工程師想直接 reproducing 或移植到產品 pipeline 時仍需自行實作。此外，實驗主要集中在特定服裝類型與互動樣式，長期及更多樣化服飾的泛化能力仍需後續工作驗證。

🎯 **對未來虛擬試衣與互動影像生成的啟示**  
- 若想讓 VVT 系統支援真實試衣中的手部互動，納入 **3D 手部先驗** 或類似的具體空間先驗是一條可行路徑。  
- 對於稀疏發生的互動事件，**時間戳語意標註** 與專門的位置編碼（如 A‑RoPE）能顯著提升模型捕捉局部動作的能力。  
- 研究結果顯示，**將空間與語意兩層引導統一在 diffusion Transformer 框架中**，有助於同時兼容傳統 VVT 與互動 VVT 的需求。

🔗 **論文連結**  
📝 iTryOn: Mastering Interactive Video Virtual Try-On with Spatial-Semantic Guidance  
👤 Jun Zheng, Zhengze Xu, Mengting Chen, Jing Wang, Jinsong Lan  
🏫 Shenzhen Campus of Sun Yat-sen University; Taobao & Tmall Group of Alibaba  
🔗 https://arxiv.org/abs/2605.21431  

你認為未來的虛擬試衣應該如何兼顧「被動展示」與「主動互動」？歡迎在留言區分享你的看法 👇

#AI #ComputerVision #VirtualTryOn #iTryOn #Alibaba #SunYatSenUniversity #DiffusionTransformer #ARVR #FashionTech
