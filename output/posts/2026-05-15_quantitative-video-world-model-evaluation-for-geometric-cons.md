---
title: "Quantitative Video World Model Evaluation for Geometric-Consistency"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.15185
score: 111
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:27:17.253583
---

📌 【Tsinghua等最新】PDI‑Bench：量化評估視訊世界模型的幾何一致性  

你以為視訊生成越逼真，就代表它真的懂三維世界嗎？最新量化基準顯示，即使畫質讓人眼前一亮，幾何錯誤仍然普遍存在。  

🤔 **評估視訊世界模型缺少客觀的幾何檢測**  
現有視訊生成評估多依賴人工打分或學習評分器，這些方式主觀且對幾何失靈（如尺度‑深度不匹配、運動不一致、結構剛性違反）診斷力有限。缺乏一套可量化、可重複的幾何一致性度量，使得研究者難以判斷模型是否真正學會了物理世界的結構與運動規律。  

🧪 **基於分割、點追蹤與單目重建的量化流程**  
研究團隊提出 PDI‑Bench（Perspective Distortion Index）。給定一段生成視訊，先透過分割與點追蹤（例如 SAM 2、MegaSaM、CoTracker3）取得物件中心的觀測；再利用單目重建將這些觀測提升到 3D 世界座標；最後計算一組投影幾何殘差，分別捕捉三種失靈維度：尺度‑深度對齊、3D 運動一致性、3D 結構剛性。為了系統化測試，他們建構了 PDI‑Dataset，涵蓋多種旨在壓縮這些幾何約束的場景。  

📊 **PDI 揭露常見感知指標未捕捉到的幾何失靈模式**  
在多個最先進的視訊生成器上進行評估後，PDI‑Bench 一致地指出了幾何方面的失靈模式——這些失靈在常見的感知評分（如 FID、CLIPScore）中往往被掩蓋。該基準提供了一個可診斷的訊號，幫助研究者了解模型在學習真實三維結構與運動方面的不足，進而指導朝向更具物理基礎的視訊世界模型改進。  

🔍 **幾何殘差背後的意義**  
透過將 2D 觀測投射到 3D 空間並檢視投影誤差，PDI‑Bench 能區分是因為深度估計錯誤導致的尺度問題，還是運動場域不一致造成的時間失靈，亦或是物件在時間上剛性被破壞。這三種殘差互補，使得評估不僅能指出「出了什麼問題」，還能提供「為什麼會出問題」的線索。  

⚠️ **樣本場景設計有限，未涵蓋全部真實世界複雜度**  
PDI‑Dataset 雖刻意設計來挑戰尺度‑深度、運動一致性與結構剛性，但仍屬於合成或受控場景；真實世界中的遮擋、非剛形變形、複雜光照等因素未在當前基準中完全體現。此外，該方法依賴於分割與點追蹤的品質，當這些前處理步驟失效時，PDI 的數值可能受到影響。  

🎯 **開放原始碼與資料集，直接作為診斷工具使用**  
論文提供了完整的程式碼與 PDI‑Dataset（https://pdi-bench.github.io/），研究者可直接將其納入現有的視訊生成評估管線。在模型迭代過程中，監控 PDI 的三個殘差分量，有助於快速定位幾何薄弱環節，進而有針對性地調整網路架構、損失函式或訓練資料。  

🔗 **論文連結**  
📝 Quantitative Video World Model Evaluation for Geometric-Consistency  
👤 Jiaxin Wu, Yihao Pi, Yinling Zhang, Yuheng Li, Xueyan Zou (Tsinghua University; UW-Madison; Adobe Research)  
🔗 https://arxiv.org/abs/2605.15185  

你在評估視訊生成模型時，是否也曾感到「畫美但總覺得哪裡不對」？PDI‑Bench 或許能幫你把那種不對的感覺量化出來。歡迎在留言區分享你的經驗或疑問 👇  

#AI #VideoGeneration #WorldModel #CVPR #Tsinghua #AdobeResearch #PDIBench #GeometricConsistency #GenerativeAI #ComputerVision
