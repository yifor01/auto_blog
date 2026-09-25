---
title: A kernel-centric path to real-time video generation on Trainium
source: Amazon Science
url: https://www.amazon.science/blog/a-kernel-centric-path-to-real-time-video-generation-on-trainium
model: claude-code/sonnet
generated_at: '2026-09-25T20:43:48.815970'
score: 115
---

📌 【Amazon 硬體工程】即時影片生成的 Trainium Kernel 最佳化之路

TL;DR：Amazon與Reactor合作，用kernel最佳化法解決Trainium上自回歸擴散模型即時生成影片的效能瓶頸。

想像一段互動式串流影片生成，如果有一幀晚了幾毫秒才送達，使用者體驗立刻崩壞。這正是即時互動影片生成模型必須面對的鐵律：生成速度必須跑贏播放時間軸，慢一步就是失敗。

🤔 **從世界模型到自回歸擴散影片**

2018年，1990年首度提出「世界模型」這個機器學習概念的 Jürgen Schmidhuber，與 David Ha 合著論文，描述一種能「萃取空間與時間中有用表徵」的預測性世界模型。八年過去，隨著巨量訓練資料集、變分自編碼器(VAE)、擴散模型與transformer的結合，今日的世界模型已能把文字、圖片、聲音、影片轉為潛在空間，用來建構並維持能預測狀態變化、回應動作的沉浸式世界模型，並在機器人、交通、氣候模擬、遊戲開發、科學模擬與設計原型中扮演關鍵角色。

Reactor是一個讓開發者、設計師與研究者部署、使用並規模化即時互動AI模型的平臺。共同創辦人暨CTO Bryce Schmidtchen談到，關鍵在於「即時性、低延遲，以及儘可能有效率地做到規模化」，效率涵蓋從如何在晶片(此處是Trainium)上排程推論，到如何盡量把每次forward pass打包到極致。Reactor的全球佈局讓挑戰更嚴峻：需要在世界各地數百個叢集間，讓GPU吐出的每個像素不經過Kubernetes層層跳轉就送上網路，同時銜接支援多種codec、解析度的串流網路，並串接跨語言的API與SDK。

Amazon Neuron Science團隊的principal applied scientist Jun Wu觀察到，影片生成正從產生固定長度的短影片，演進到無限長度或動態長度的影片。要在這種長度下生成高品質畫面，催生了autoregressive diffusion models的興起：這類模型結合大型語言模型式的next-token prediction，與擴散模型的迭代精煉，讓使用者的一次鍵盤輸入能被模型吸收為輸入，並根據前一個生成的影格，正確決定下一步動作或下一個場景。Wu表示，今天多數互動式影片生成模型都採用這種做法。

🧩 **鎖定 Rolling Forcing，拆解三大 kernel 難題**

Wu與同事Mason Fu、Lingfan Yu與已投入即時互動影片生成超過18個月的Reactor團隊合作，選定Rolling Forcing模型作為autoregressive diffusion影片生成在Trainium上的代表性工作負載，原因是它能穩定生成高品質的30秒影片，且模型體積相對較小。真正的難處不在畫質，而在於它必須即時運行：不同於傳統影片生成先離線算完整段影片再回傳，Rolling Forcing這類模型是串流式的，每一幀生成後立即被消費、展示給使用者或回饋成下一次輸入，晚到的一幀就會打斷體驗。

Wu指出，高品質生成擴散模型的挑戰在於序列很長，需要大量記憶體；Rolling Forcing模型雖小，序列長度卻很大。「小模型、長序列、硬性幀率下限」這個組合，正是即時生成之所以嚴苛的原因。Rolling Forcing能達到每秒16幀的標準播放速率，也因此滿足了延遲要求，而Trainium的角色就是提供足夠效能與記憶體，撐住這個長序列工作負載，在16fps以上做到真正即時生成，而非事後才產出好畫面。

兩個團隊因此採取kernel-centric、由下而上的開發方式，目標是讓開發者更容易上手，並聚焦三個對通用編譯器而言特別棘手、且在每次forward pass都會重複發生的挑戰：動態形狀(dynamic shapes)、不尋常的記憶體存取模式、以及繁重的cache管理。動態形狀的部分，一方面源自場景本身的變化，例如鏡頭從投手獨自站在投手丘，幾秒內拉遠帶出所有球員甚至數千名觀眾；另一方面，即時影片生成採用連續滑動視窗(sliding window)不斷生成並淘汰影格，導致attention長度在每次forward pass間都不一樣，且每個視窗還包含denoising與cache清理兩個不同階段，讓靜態編譯變得困難。

除了滑動KV cache的複製，影片生成工作負載還包含rotary position embeddings(RoPE)與attention transpose這類記憶體存取模式高度特定於此工作負載的運算，讓通用編譯器難以充分最佳化。以RoPE為例，在影片生成中必須處理高度、寬度、時間三個軸，而不是LLM中僅有的單一位置軸；Wu解釋，這種3D旋轉嵌入會在最內層維度交錯奇偶元素，若照通用方式編譯，會產生大量瑣碎的小型資料搬移。

💡 **由下而上的意義：把編譯器搞不定的細節交給 kernel**

這三個挑戰之所以值得用kernel-centric的方式處理，是因為它們不是一次性的成本，而是每次forward pass都會重複出現。在其他工作負載上可能只是微不足道的延遲，放進16fps的即時生成節奏裡，卻會不斷累積成明顯的延遲失敗。與其等待通用編譯器慢慢追上，直接下放到kernel層手動最佳化，才能真正撐住即時性的要求。

🎯 **實務啟示**

對想在Trainium或其他客製化AI加速器上部署autoregressive diffusion、即時影片生成模型的工程師而言，這篇文章點出三個該優先檢視的效能熱點：動態序列長度、非典型記憶體存取模式(尤其是3D RoPE)、以及KV cache管理。這些問題在通用編譯器上很難被妥善處理，值得優先評估是否需要投入客製kernel。

🔗 **來源**
- 標題：A kernel-centric path to real-time video generation on Trainium
- 作者／機構：Amazon (Amazon Science)
- 連結：https://www.amazon.science/blog/a-kernel-centric-path-to-real-time-video-generation-on-trainium

#Trainium #WorldModels #VideoGeneration #DiffusionModels #AWS #AIInfrastructure #KernelOptimization #AutoregressiveModels #RealTimeAI #MachineLearning
