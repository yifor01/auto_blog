---
title: "MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.15128
score: 126
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:12:09.185970
---

📌 **MemEye：多模態 Agent 記憶的細粒度評估**  

你以為多模態 Agent 能「記住」畫面細節？實際上，現有記憶方法往往只保留文字描述，關鍵視覺證據卻被遺失。  

🤔 **現有基準測試難以區分真正的視覺記憶與文字捷徑**  
長期 Agent 記憶正趨向多模態，但既有評估多依賴字幕或文字痕跡，讓模型能在不保留細緻視覺證據的情況下給出答案。真正需要隨時間推論視覺狀態變化的案例卻十分稀少，導致我們無法知道模型是否真的「看見」並記住了畫面。  

🧪 **MemEye 框架：兩維度評估 + 8 個生活場景任務**  
我們提出 MemEye，從兩個維度衡量記憶能力：一是決定性視覺證據的粒度（從場景層級到像素層級），二是檢索到的證據如何被使用（從單一證據到隨時間演化的綜合推論）。在此框架下，構建了橫跨 8 個生活場景的基準，並設計了消融驗證門檻，以檢測答案的可解性、捷徑抵抗力、視覺必要性以及推論結構。  

🔍 **目前主流方法在細緻視覺保留與狀態變化推論上仍顯不足**  
在 4 種 VLM 骨幹上測試了 13 種記憶方法，結果顯示：大多數架構難以長期保留像素級的視覺細節，也難以根據隨時間變化的畫面進行多步驟推論。實驗進一步指出，長期多模態記憶的關鍵在於證據的路由機制、時間追蹤能力以及細節萃取模組。  

💡 **證據 routing 與 temporal tracking 是改進的核心方向**  
研究團隊指出，單純增大模型或加長上下文並不能解決問題；必須在記憶架構中顯式地設計：  
- 如何將相關視覺證據從感覺層路由到記憶儲存單元  
- 如何在時間序列中追蹤物件或場景的狀態變化  
- 如何在檢索時提取足夠細緻的特徵以支援像素層級推論  

⚠️ **基準僅覆蓋有限場景，長期效果尚待追蹤**  
目前的基準聚焦於 8 個特定生活場景任務，雖然涵蓋了多樣化的視覺變化，但未測試極端長時程（數小時或數天）的記憶保持，亦未探索跨模態干擾更複雜的情境。因此，結果主要反映中短期（分鐘級）的行為。  

🎯 **工程實務：優先設計證據路由與時間追蹤模組**  
- 在記憶層加入可學習的門控機制，決定哪些視覺特徵值得長期保存  
- 引入時間卷積或狀態空間模型，顯式建模畫面隨時間的變化軌跡  
- 在檢索階段使用細粒度特徵對齊 loss，確保像素級資訊不被壓縮遺失  

🔗 **論文連結**  
📝 MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory  
👤 Minghao Guo, Qingyue Jiao, Zeru Shi, Yihao Quan, Boxuan Zhang (Rutgers; Notre Dame; Princeton; UMN)  
🔗 https://arxiv.org/abs/2605.15128  

你的多模態 Agent 記憶設計是否已經考慮到視覺證據的細粒度保留？歡迎在留言區分享你的經驗與思考 👇  

#AI #Multimodal #AgentMemory #MemEye #CVPR2026 #Rutgers #NotreDame #Princeton #UMN #MachineLearning
