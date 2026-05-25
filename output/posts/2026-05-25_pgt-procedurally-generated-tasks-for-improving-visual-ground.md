---
title: "PGT: Procedurally Generated Tasks for improving visual grounding in MLLMs"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.23883
score: 123
model: tencent/hy3-preview:free
generated_at: 2026-05-25T20:22:55.431375
---

📌 **PGT：幾何圖像強化模型理解**

你以為只要喂給模型更多圖像，它就能看得更細膩？其實，問題可能出在「它看到的線索」本身不夠清楚。

🤔 **多模態大語言模型在精細空間推論上仍受限**  
儘管 MLLM 在語言與圖像對齊方面取得長足進步，但對幾何關係、數量與深度等細粒度視覺任務的表現仍有顯著不足。這種 bottleneck 常被歸因於模型架構或解析度，卻忽略了監督訊號的品質。

🧪 **以幾何圖疊加產生密集監督訊號**  
PGT（Procedurally Generated Tasks）透過在圖像上疊加無歧義的幾何基本圖形（如線、點、框架），為每個像素提供顯式的空間標籤。這樣的過程同時：  
1. 產生額外的密集監督，幫助模型學習精細的視覺定位；  
2. 作為低成本診斷工具，可檢測模型在哪類空間推論上失敗，從而將視覺根底與語義先驗分離開來。

 **在 What'sUp 與 CV-Bench-2D 上提升達 +20%**  
- 在 LLaVA-v1.5-Instruct 基礎上加入 PGT 資料進行指令微調，What'sUp 基準提升最高達 **+20%**，CV-Bench-2D 提升 **+13.3%**；  
- 對已有的 SOTA MLLM 直接以 PGT 資料微調，則可獲得最高 **+5.5%**（What'sUp）與 **+8.3%**（CV-Bench-2D）的增益，且一般感知能力未顯著下降。

💡 **幾何 primitives 消除了語義先驗的干擾**  
因為所加的幾何圖形與圖像語義內容無關，模型必須依賴純粹的幾何訊號來完成任務。這種設計使得提升來源更可能是「更好的視覺監督」而非僅僅是模型利用了額外的語義線索。

⚠️ **論文未詳細說明樣本與泛化限制**  
摘要中未具備說明訓練資料規模、模型尺寸範圍或在未見領域的泛化表現；這些資訊需參考全文才能獲得完整評估。

🎯 **可作為低成本診斷與微調工具**  
對工程師而言，PGT 提供一種簡單且無需額外標註成本的方式：  
- 產生幾何圖疊後直接用於微調，即可提升空間推論；  
- 同時作為診斷手段，快速定模型在哪類幾何推論上薄弱，以針對性改進後續資料收集或架構調整。

🔗 **論文連結**  
📝 PGT: Procedurally Generated Tasks for improving visual grounding in MLLMs  
👤 Rim Assouel, Amir Bar, Michal Drozdzal, Adriana Romero-Soriano (Mila - Québec AI Institute; Université de Montréal; FAIR at Meta Superintelligence Labs; McGill University; Canada CIFAR AI Chair)  
🔗 https://arxiv.org/abs/2605.23883

你有試過用幾何圖樣來檢視模型的「看」的方式嗎？歡迎在留言區分享經驗或疑問 👇

#AI #Multimodal #MLLM #VisualGrounding #PGT #Meta #Mila #CVPR2026
