---
title: "MSAVBench: Towards Comprehensive and Reliable Evaluation of Multi-Shot Audio-Video Generation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.20183
score: 129
model: tencent/hy3-preview:free
generated_at: 2026-05-20T20:47:53.241253
---

📌 【Fudan 等最新研究】MSAVBench：首個多鏡頭音視訊生成基準  

你以為現在的 AI 能流暢生成長片？其實評估這類多鏡頭影片仍是個難題。  

🤔 **多鏡頭音視訊生成評估缺乏全面基準**  
現有基準範圍有限、資料多樣性不足，且依賴固定評估流程，難以系統可靠地衡量新興的多鏡頭音視訊（MSAV）模型。  

🧪 **涵影像、音訊、鏡頭、參考四維度的 MSAVBench 框架**  
我們提出 MSAVBench，第一個綜合性基準與自適應混合評估框架。基準覆蓋影像、音訊、鏡頭與參考四個關鍵面向，支援多種任務設置、最多 15 鏡頭的變化以及具挑戰性的非寫實場景。評估框架透過鏡頭分割的自適應自我校正機制、針對主觀指標的實例級評分規則，以及用於複雜判斷的工具根擬證據提取，來提升穩健性。  

📊 **與人類判斷高度一致，Spearman 相關達 91.5%**  
經過人類評驗驗證，MSAVBench 的排名與人類判斷的 Spearman 相關係數達到 91.5%，顯示其評估結果具高度可信度。  

🔍 **現有模型在導演級控制與細緻同步上仍顯不足**  
對 19 個最新閉源與開源模型的系統評估顯示，當前系統在導演級控制與細緻音視覺同步方面仍有顯著不足；而採用模組化或 Agentic 生成管線的方法，則顯示出縮小開源與閉源差距的潛力。  

⚠️ **基準主要聚焦於現有模型評估，長尾場景與真實製片流程尚需補充**  
此工作的評估範圍限於現有 SOTA 模型的表現，對於極端長尾場景或完整製片流程的適用性尚需後續研究補充。  

🎯 **模組化或 Agentic 生成管線是縮小開源與閉源差距的有希望方向**  
對於從事多模態生成的工程師與研究者，MSAVBench 提供了可直接使用的數據與評估代碼，有助於更客觀地比較模型能力。未來可著重於設計模組化或具代理特性的生成管線，以提升導演級控制與音視訊細緻同步。  

🔗 **論文連結**  
📝 MSAVBench: Towards Comprehensive and Reliable Evaluation of Multi-Shot Audio-Video Generation  
👤 Yujie Wei, Yujin Han, Zhekai Chen, Yongming Li, Kaixun Jiang (Fudan University; The University of Hong Kong; Tongyi Lab, Alibaba Group; Zhejiang University; Peking University)  
🔗 https://arxiv.org/abs/2605.20183  

你對多鏡頭音視訊生成的評估有什麼經驗或看法？歡迎在留言區分享 👇  

#AI #多模態 #視訊生成 #MSAVBench #Fudan #Alibaba #Agentic #評估基準 #CVPR2025
