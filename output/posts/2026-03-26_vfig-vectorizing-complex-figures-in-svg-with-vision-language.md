---
title: "VFIG: Vectorizing Complex Figures in SVG with Vision-Language Models"
source: ChatPaper/AI
url: https://arxiv.org/abs/2603.24575
score: 106
model: gpt-4o-free
generated_at: 2026-03-26T19:47:18.759024
---

📌 【UW &Allen Institute 最新研究】VFIG：讓點陣圖變回可編輯的 SVG，開源資料與基準同步釋出  

你以手機截圖或論文中的 PNG 圖表，只要打開就能直接修改嗎？事實上，一旦失去原始 SVG 檔案，即使是簡單的線條調整也可能需要重新從零繪製，這對研究人員與設計師來說是個沉重的負擔。  

🤔 **原始向量檔案常見遺失，修改成本高昂**  
在技術說明與數位設計工作流程中，向量圖（SVG）解析度無上限且可語意編輯，但實務上原始檔案經常遺失或無法取得，只剩下點陣版（PNG/JPEG）。手動復原不僅耗時，更需要專業知識來辨識原始的幾何意圖。  

🧪 **66K 圖‑SVG 配對資料庫與粗到細訓練課程**  
研究團隊建立了 VFIG‑DATA，包含 66,000 份高品質的論文圖表與程式生成圖的 SVG 配對。針對 SVG 由基本圖元與局部階層結構組成的特點，他們提出粗到細的訓練流程：先以監督微調（SFT）學會基本圖元，再透過強化學習（RL）優化整體圖形忠誠度、佈局一致性以及拓樸邊界案例。  

📊 **開源模型中表現最佳，與 GPT-5.2 持平**  
在新設計的 VFIG‑BENCH 評估套件上，VFIG 達到 VLM‑Judge 分數 0.829，這不僅是目前開源模型中的最高分，也與 GPT-5.2 的表現相當。評估指標特別關注圖形的結構完整度，而非僅看像素相似度。  

💡 **結構完整度才是關鍵，而非僅看像素相似度**  
傳統的圖像到向量轉換常優先保持外觀相似，卻可能忽略圖元間的拓樸關係與層級結構。VFIG 透過課程式學習，使模型在學會基本圖元後，進一步優化全局結構，從而產出更易於後續編輯的 SVG。  

⚠️ **資料多來自論文圖與程式生成，真實設計圖表複雜度仍需驗證**  
VFIG‑DATA 主要來源於真實論文圖表與程式產生的圖形，雖然數量龐大且品質高，但尚未大規模涵蓋產業級的複雜設計圖（例如電路原理圖或建築立面圖），因此長期在專業設計場景的適用性仍需進一步驗證。  

🎯 **設計師與研究者可直接使用 VFIG-DATA 與 VFIG-BENCH 進行評估與微調**  
隨著開源資料與基準的公開，團隊希望社群能在現有工作流程中直接引用 VFIG，或利用 VFIG‑DATA 進行領域適應微調。對於需要經常修改圖表的研究團隊而言，這意味著可以大幅減少手動重繪的時間，將焦點放在內容創作而非檔案復原上。  

🔗 **論文連結**  
📝 VFIG: Vectorizing Complex Figures in SVG with Vision-Language Models  
👤 Qijia He, Xunmei Liu, Hammaad Memon, Ziang Li, Zixian Ma  
🏫 University of Washington; Allen Institute for Artificial Intelligence; UNC-Chapel Hill  
🔗 https://arxiv.org/abs/2603.24575  

你是否曾因找不到原始 SVG 而浪費時間重畫圖表？歡迎在留言區分享你的經驗或對此技術的看法 👇  #AI #SVG #VisionLanguageModel #UW #AllenInstitute #UNC #OpenSource #圖表編輯 #技術繪圖 #VFIG
