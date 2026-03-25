---
title: "Foveated Diffusion: Efficient Spatially Adaptive Image and Video Generation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.23491
score: 125
model: gpt-4o-free
generated_at: 2026-03-25T19:21:40.433922
---

📌 **Foveated Diffusion：依據人類視覺分配 token，實現近乎無損的圖像與影像生成**  
Stanford 大學 — Brian Chao、Lior Yariv、Howard Xiao、Gordon Wetzstein  

🎣 **你以為高解析度生成必須耗費 quadratically 的計算？其實人眼本身就在「省電」——只需在注視點附近保留高解析度，邊緣區域就可大幅降低精度。**  

🤔 **人類視覺的邊緣解析力下降，成為節省計算的契機**  
當使用者的注視位置可知（例如透過眼動追蹤），我們可以利用人類視覺在凹陷區（fovea）具有高解析度，而在周邊區域解析力快速衰減的特性。這意味著，若在生成過程中將 token 密度集中在注視點附近，周邊區域則使用較低密度，理論上不會影響主觀感受，卻能大幅降低所需的計算量。  

🧪 **以遮罩模擬凹陷解析度，產生混解析度 token 進行擴散**  
研究團隊首先構建一個根據 eccentricity（視角偏離度）的遮罩，以此決定各區域應分配多少 token。接著，他們提出一種從高解析度資料直接構建混解析度 token 的原則性方法，使得現有的擴散模型可以後續訓練（post‑train）以適應此種 token 分布，同時保持跨解析度的一致性。最終，在已知注視位置的條件下，以混解析度 token 進行圖像或影像的生成。  

🔍 **生成結果與全解析度幾乎無法區分，但 token 數與生成時間顯著下降**  
透過精心設計的使用者研究，團隊驗證了在人眼無法辨識的前提下，foveated 方式所產出的圖像與影像在主觀感受上與全解析度生成無顯著差異。同時，因為 token 被非均勻分配，總 token 數大幅減少，導致生成速度相應提升。具體的減少比例與加速倍數依實驗設定而異，但論文指出「顯著降低」且「可擴展」至更高解析度與更長影像序列。  

💡 **利用人類視覺特徵的後訓練機制，使現有模型可直接適用**  與從零訓練專用模型不同，此方法的關鍵在於其「後訓練」特性：只要已有標準的擴散或流匹配模型，即可透過提出的混解析度 token 構建方式進行微調，不需重新設計網路架構。這意味著研究者與工程師可以在現有程式碼基礎上快速加入眼動追蹤的適配層，即時獲得計算效益。  

⚠️ **依賴眼動追蹤準確度、使用者研究規模未詳述、長期適用性尚待探索**  
論文的效果建立在注視位置能被正確估計或直接測量的前提上；若眼動追蹤噪聲大或延遲高，可能影響 foveated 分布的正確性。此外，摘要中未透露使用者研究的具體樣本數或統計顯著度，僅說明經過「精心設計」並顯示方法的有效性。最後，雖然方法在圖像與短片段影像上表現良好，但在極長影像或互動式場景中的長期穩定性仍需進一步驗證。  

🎯 **適用於 AR/VR、即時互動式生成等場景，可顯著降低運算成本**  
對於需要即時回饋的擴增實境（AR）或虛擬實境（VR）應用，使用者的注視點往往可透過頭戴裝置的眼動感測器取得。在此情境下，採用 foveated diffusion 能在保持視覺品質的同時，大幅削減 GPU 運算負載，提升桌邊率或延長電池壽命。同時，該方法的後訓練特性意味著開發團隊無需從頭重新訓練大模型，即可在現有 Stable Diffusion、DALL·E 系列或其他流匹配模型上快速實作。  

🔗 **論文連結**  
📝 Foveated Diffusion: Efficient Spatially Adaptive Image and Video Generation  
👤 Brian Chao, Lior Yariv, Howard Xiao, Gordon Wetzstein @ Stanford University  
🔗 https://arxiv.org/abs/2603.23491  

你認為在哪些互動式生成情境中，眼動追蹤配合 foveated 策略會帶來最明顯的體驗提升？歡迎在留言區分享你的想法 👇  

#AI #Diffusion #FoveatedRendering #ARVR #EfficientGeneration #Stanford #ComputerVision #GenerativeAI
