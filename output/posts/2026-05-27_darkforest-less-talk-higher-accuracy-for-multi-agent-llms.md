---
title: "DarkForest: Less Talk, Higher Accuracy for Multi-Agent LLMs"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.25188
score: 94
model: tencent/hy3-preview:free
generated_at: 2026-05-27T21:11:36.642453
---

📌 DarkForest: Less Talk, Higher Accuracy for Multi-Agent LLMs  

多個 AI 代理互相討論時，常常說得越多，錯誤卻越累積？這篇論文提出一種「少說更準」的方法。  

🤔 **多代理溝通易放大錯誤**  
多代理 LLM 系統需要頻繁交換資訊來達到共識，但每輪溝通都可能把先前的錯誤放大，導致推論品質下降與計算開銷激增。  

🧪 **受控通訊框架 DarkForest**  
作者設計了一個受控通訊框架：先將候選語意進行聚類，再以校準後的信念分配來決定何時與如何傳遞訊息，以抑制錯誤傳播並降低通訊次數。  

📊 **準確度提升、通訊減少**  
實驗顯示，在多個基準任務上，DarkForest 能在保持或提升推論正確率的同時，顯著減少代理間的訊息交換次數。  

💡 **聚類與信念校準的關鍵**  
透過聚類相似的語意候選，框架能在訊息冗餘高的區域合併資訊；校準的信念分配則讓每個代理根據自身不確定度調整發言頻率與內容，使得只有高信息量的訊息才會被傳遞，從而切斷錯誤放大的迴路。  

⚠️ **目前尚未開放程式碼，實驗細節有限**  
論文未公開原始碼或可直接使用的函式庫，實驗規模與基準任務的詳細描述有限，長期在真實多代理應用中的穩定性尚需進一步驗證。  

🎯 **設計啟示：先過濾後再溝通**  
對於需要多代理協同推理的場景（例如自動化客服、協同規劃或模擬環境），開發者可參考其通訊控制思想，先嘗試以聚類與信念校準的方式設計訊息過濾機制，以在不犧牲正確度的前提下降低延遲與運算成本。  

🔗 **論文連結**  
📝 DarkForest: Less Talk, Higher Accuracy for Multi-Agent LLMs  
🔗 https://huggingface.co/papers/2605.25188  

#AI #MultiAgent #LLM #Reasoning #CommunicationOverhead #HuggingFacePapers #DarkForest
