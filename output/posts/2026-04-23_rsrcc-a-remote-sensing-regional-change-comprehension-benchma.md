---
title: "RSRCC: A Remote Sensing Regional Change Comprehension Benchmark Constructed via Retrieval-Augmented Best-of-N Ranking"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.20623
score: 104
model: tencent/hy3-preview:free
generated_at: 2026-04-23T19:57:33.702825
---

📌 【Google Research】首個遙感細粒度變化問答基準RSRCC

現有的遙感變化檢測技術，只能識別「哪裡發生了變化」，卻無法用自然語言解釋「具體變成了什麼」。
過往的遙感變化描述數據集大多僅覆蓋圖像級的整體差異，針對局部區域的細粒度語義推理幾乎是空白。
Google Research 最新提出的 RSRCC 基準，正是為填補這個缺口而生。

🤔 **遙感變化檢測有定位無解釋，細粒度推理數據空白**
傳統遙感變化檢測（Change Detection）的核心能力是定位變化區域，但不具備自然語言解釋變化語義的能力。現有的遙感變化描述（Change Captioning）數據集多聚焦於兩張圖像的整體差異描述，未針對局部特定變化區域設計推理任務，導致模型難以學習細粒度的語義理解能力。此類能力對多模態遙感應用具重要潛在價值，但過往缺乏對應的基準數據支撐。

🧪 **12.6萬問答對，分層半監督流程構建**
RSRCC 是首個專門針對細粒度變化推理設計的遙感變化問答（VQA）基準，共包含 12.6 萬（126k）個問答實例，拆分為 8.7 萬訓練集、1.71 萬驗證集與 2.2 萬測試集。據作者所知，這是首個明確為細粒度推理監督設計的遙感變化問答基準，所有問題均圍繞局部、特定變化區域設計，要求模型針對具體語義變化進行推理。

其構建採用分層半監督策展管道，核心流程分為三步：首先從語義分割掩碼中提取候選變化區域，接著透過圖文嵌入模型進行初步篩選，最後以檢索增強的視覺-語言策展結合 Best-of-N 排序作為最終歧義解決階段，確保數據質量。

 **首個細粒度遙感變化問答基準，構建流程可擴展過濾噪聲**
RSRCC 填補了過往遙感變化問答數據集僅覆蓋圖像級描述的空白，為細粒度語義推理提供了專門的評測與訓練基準。其採用的構建流程透過自動化候選提取、初篩與檢索增強驗證結合 Best-of-N 排序的設計，可在大規模數據構建場景下有效過濾噪聲與模糊候選，同時保留具語義意義的變化樣本，解決了傳統人工標註成本高、噪聲多的痛點。

💡 **檢索增強Best-of-N排序，解決大規模數據歧義問題**
不同於過往依賴全人工標註的數據集構建方式，RSRCC 的半監督策展流程大幅降低了標註成本，同時透過檢索增強的視覺-語言驗證提升語義匹配準確性，Best-of-N 排序則作為最終歧義解決機制，有效過濾模糊樣本。這種可擴展的構建範式不僅適用於遙感場景，也可為其他多模態數據集的構建提供參考。

⚠️ **公開摘要未提及明確限制，詳情參考全文**
目前公開的論文摘要未明確列出研究限制，完整說明請參考論文全文。

🎯 **新基準與方法，助力多模態遙感研究落地**
對於遙感與多模態 AI 研究者，RSRCC 提供了首個細粒度變化問答的評測基準，可用於驗證模型的局部語義推理能力；其提出的檢索增強 Best-of-N 排序構建流程，也可為大規模多模態數據集構建提供技術參考。工程師可透過 Hugging Face 直接獲取公開數據集，用於相關模型的訓練與優化，探索多模態遙感場景的潛在應用。

🔗 **論文連結**
📝 論文標題：RSRCC: A Remote Sensing Regional Change Comprehension Benchmark Constructed via Retrieval-Augmented Best-of-N Ranking
👤 作者：Roie Kazoom, Yotam Gigi, George Leifman, Tomer Shekel, Genady Beryozkin @ Google Research
📚 來源：Computer Vision and Pattern Recognition (ChatPaper)
🔗 論文連結：https://arxiv.org/abs/2604.20623
📦 數據集連結：https://huggingface.co/datasets/google/RSRCC

你認為細粒度語義推理能力，對遙感 AI 的實際落地有多重要？歡迎在留言區分享你的看法 👇

#GoogleResearch #遙感AI #多模態學習 #計算機視覺 #數據集 #RSRCC #AI研究 #遙感應用
