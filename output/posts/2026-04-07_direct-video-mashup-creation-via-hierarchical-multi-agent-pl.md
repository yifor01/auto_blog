---
title: "DIRECT: Video Mashup Creation via Hierarchical Multi-Agent Planning and Intent-Guided Editing"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.04875
score: 118
model: gpt-4o-free
generated_at: 2026-04-07T13:18:39.991273
---

📌 【CVPR】三層多智能體破解影片混剪斷層

你以為 AI 剪片工具只是「把片段拼在一起」？研究顯示，缺乏跨模態協調的自動化剪輯，往往產出畫面跳接突兀、配樂錯位的半成品。當 AI 開始模仿專業製片工業的階層分工，影片混剪的流暢度終於迎來結構性突破。

**🤔 現有 AI 剪片工具「懂單點操作，卻缺全局協調」**
影片混剪（Video Mashup）並非單純的素材拼接，而是需要在語義、視覺與聽覺多個維度上進行精密調度。當前的自動化剪輯框架大多將任務拆解為孤立的模組，忽略跨層級的多模態協同。這導致系統容易陷入局部優化，輸出節奏斷裂、音畫不同步的內容。如何讓 AI 具備專業剪輯師的「全局節奏感」，成為多模態內容生成管線的核心痛點。

**🧪 模擬專業製片管線，拆解為編劇、導演、剪輯師三層協作**
北大與華科團隊將此任務形式化為「多模態一致性滿足問題（MMCSP）」，並提出 DIRECT 框架。該架構模擬真實影視製作流程，設計了階層式多智能體系統：
1. Screenwriter（編劇智能體）：負責全局結構錨定，根據原始素材建立整體敘事骨架。
2. Director（導演智能體）：接收結構資訊，實例化出具體的剪輯意圖與指導策略。
3. Editor（剪輯智能體）：依據導演下發的意圖，執行鏡頭序列的微調與最佳化。
為公平評估，團隊同步推出 Mashup-Bench 基準測試，針對視覺連續性與聽覺對齊設計專屬量化指標。

**📊 在視覺連貫與音畫同步指標上顯著超越現有基線**
實驗結果顯示，DIRECT 在客觀指標與人類主觀評分上均大幅領先現有 SOTA 方法。透過階層化解耦，系統有效避免了傳統端到端模型常見的「局部最優但全局失衡」現象。Mashup-Bench 的評估數據驗證，該框架在處理跨模態對齊時，能維持更高的敘事流暢度與音樂節奏契合率。

**💡 從「指令驅動」走向「意圖引導」的架構躍遷**
DIRECT 的核心價值在於「意圖引導剪輯（Intent-Guided Editing）」的設計理念。傳統框架多依賴硬規則或單一模型直接輸出特徵，容易在複雜情境下產生衝突。DIRECT 透過導演層將抽象的敘事結構轉譯為可執行的剪輯意圖，再交由執行層進行細粒度優化。這種設計不僅符合人類創意工作的認知邏輯，也有效解決了跨模態訊號在傳輸過程中的資訊衰減問題。

**⚠️ 基準測試規模有限，多智能體串聯延遲待優化**
Mashup-Bench 為新提出之基準，資料集規模與場景覆蓋度仍在擴展階段。當前實驗多聚焦於標準時長的混剪任務，對於長篇敘事或極端音畫衝突情境的泛化能力尚待驗證。此外，三層智能體串聯推理的計算開銷與延遲，在實際部署至即時或長影片工作流時，需進一步進行效能調優。

**🎯 自動化內容管線設計，應優先建立「意圖傳遞層」**
對建構 Agentic 影音工作流的工程師而言，DIRECT 證明了「解耦」與「意圖中轉」在複雜多模態任務中的必要性。實務開發時，可避免讓單一模型承擔所有決策，改為設計明確的結構錨定、意圖轉譯與執行優化三階段。這不僅能提升輸出穩定度，也便於針對特定環節（如配樂卡點或轉場特效）進行獨立迭代。

🔗 **論文連結**
📝 DIRECT: Video Mashup Creation via Hierarchical Multi-Agent Planning and Intent-Guided Editing
👤 Ke Li, Maoliang Li, Jialiang Chen, Jiayu Chen, Zihao Zheng @ Peking University & HUST
📅 CVPR (Computer Vision and Pattern Recognition)
🔗 論文：https://arxiv.org/abs/2604.04875
💻 開源程式碼與專案頁面：https://github.com/AK-DREAM/DIRECT

你目前使用的 AI 影音生成或剪輯工具，是否也遇到音畫不同步或轉場生硬的問題？歡迎分享你的工作流設定與觀察 👇

#CVPR #AgenticAI #VideoEditing #多模態AI #影片混剪 #DIRECT #北大團隊 #開源AI #多智能體 #內容生成管線
