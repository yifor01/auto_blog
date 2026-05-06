---
title: "ScrapMem: A Bio-inspired Framework for On-device Personalized Agent Memory via Optical Forgetting"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.03804
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-06T20:35:56.253019
---

📌 【南大/南農大研究】邊緣Agent記憶省93%存儲達SOTA

多模態LLM Agent要部署在邊緣設備，長期記憶的存儲成本一直是核心痛點。
多數方案只能在性能與存儲之間二選一，最新研究卻打破這個權衡。

🤔 **資源受限邊緣端難支撐LLM Agent長期個性化記憶**
大型語言模型（LLM）代理的長期個性化記憶，在資源受限的邊緣設備上面臨顯著挑戰，核心瓶頸來自兩方面：一是多模態數據帶來的高存儲成本，二是複雜多模態信息的處理難度。

🧪 **ScrapMem結合光學遺忘與情景記憶圖設計**
團隊提出ScrapMem框架，核心包含兩項創新機制：首先將多模態數據整合為「剪貼簿頁面（Scrapbook Page）」，導入Optical Forgetting（光學遺忘）光學壓縮機制，透過逐步降低舊記憶的分辨率，壓低存儲成本的同時過濾低價值細節；其次構建Episodic Memory Graph（EM-Graph，情景記憶圖），將關鍵事件組織為因果-時間結構，維持壓縮後的語義一致性。實驗採用多模態基準測試ATM-Bench驗證效果。

💡 **存儲省93%還拿下多模態記憶SOTA**
實驗結果顯示ScrapMem帶來三大核心優勢：
1. 性能達SOTA：在ATM-Bench上取得51.0%的Joint@10分數，刷新該基準的最佳成績
2. 存儲效率極高：透過光學遺忘機制，最多可減少93%的記憶體使用量
3. 召回率提升：透過結構化聚合，Recall@10提升至70.3%

💡 **光學遺忘壓成本，情景圖保語義連貫**
ScrapMem的設計邏輯區分了兩類優化方向：針對舊記憶的低價值細節，用光學遺忘逐步降解析度，在不影響核心信息的情況下壓縮存儲；針對多模態數據的語義連貫性，用EM-Graph梳理事件的因果與時間關係，避免壓縮過程丟失關鍵語義，最終實現降本不降質的效果。

⚠️ **本次公開資訊未提及論文研究限制**
現有提供的摘要與評分資料未包含該論文的研究限制說明，若需了解實驗侷限、適用場景邊界等資訊，建議參考完整論文內容。

🎯 **邊緣Agent記憶部署可參考輕量化壓縮思路**
對於需要在邊緣設備部署多模態LLM Agent的開發者與研究者，ScrapMem的設計具備高度參考價值：一是長期記憶可採用分層壓縮策略，區分高低價值信息；二是多模態記憶需同時兼顧存儲效率與語義連貫性，結構化組織比單純壓縮更有效。

🔗 **論文連結**
📝 論文標題：ScrapMem: A Bio-inspired Framework for On-device Personalized Agent Memory via Optical Forgetting
👤 作者：Jiale Chang, Yuxiang Ren（南京農業大學、南京大學）
🔗 論文連結：https://arxiv.org/abs/2605.03804
📚 來源：ChatPaper/AI、arXiv預印本

你目前在邊緣設備部署Agent時遇到過記憶存儲的問題嗎？歡迎分享你的解決方案 👇

#AI #LLM #Agent #邊緣計算 #記憶機制 #南京大學 #南京農業大學 #ScrapMem
