---
title: "WildTableBench: Benchmarking Multimodal Foundation Models on Table Understanding In the Wild"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.01018
score: 92
model: tencent/hy3-preview:free
generated_at: 2026-05-16T19:36:21.639632
---

📌 WildTableBench: 真實表格理解基準  

你以為多模態模型已能看懂表格？最新基準顯示，它們在結構感知與數值推理上仍有顯著不足。  

🤔 多模態基礎模型在圖像與文字理解上進步快速，但真實世界的表格圖像（如發票、報表）常伴隨複雜佈局與數值計算，現有評估多依賴合成或簡化資料，缺乏對實際應用的檢驗。  

🧪 WildTableBench 建構了第一個以真實表格圖像為基礎的問答資料集，包含開放的資料集與評估腳本，涵蓋結構辨識與數值推理兩類問題。  

 現有多模態基礎模型在該基準上的表現普遍落後，特別是在需要理解表格結構與進行數值運算的題目上，準確率顯著低於合成基準。  

💡 結果顯示模型的結構感知能力是瓶頸；即使能辨識文字，難以正確解析欄位對應與執行跨欄位的加總、平均等運算，導致問答失敗。  

⚠️ 基準目前規模有限，主要收錄特定領域的表格（如財務與行政），未涵蓋所有可能的真實世界表格變體；評估主要聚焦於零樣少樣設定，未探索微調後的上限。  

🎯 工程師可直接使用開放資料集與腳本來診斷自家模型在表格理解上的弱點，針對結構編碼或數值推理模組進行有針對性的改進，亦為未來多模態 Agent 提供具體的評估指標。  

🔗 **論文連結**  
📝 WildTableBench: Benchmarking Multimodal Foundation Models on Table Understanding In the Wild  
🔗 https://huggingface.co/papers/2605.01018  

你的多模態模型在真實表格上表現如何？歡迎在留言區分享測試結果或改進經驗 👇  

#AI #Multimodal #TableUnderstanding #Benchmark #HuggingFace #Agent #開源資料集
