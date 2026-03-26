---
title: "Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.24326
score: 101
model: gpt-4o-free
generated_at: 2026-03-26T19:56:43.620434
---

📌 PaddleOCR-VL 解析  

文件圖片越清晰，AI 模型似乎越吃力？  
高解析度帶來的視覺token爆炸讓計算成本飆升。  
我們發現，大量背景區域正是效率殺手。  

🤔 **高解析度提升精度卻伴隨 token 平方爆炸**  文件解析是一項細粒度任務，圖片解析度越高模型表現越好，但這同時會導致視覺token數量呈平方增長，計算開銷急劇上升。研究指出，這種效率低下主要來自於圖像中大量與任務無關的背景區域，例如純白邊距或無意義紋理，造成資源浪費。  🧪 **Valid Region Focus Module 與 0.9B 輕量 VL 模型的粗到細設計**  
為了減少無效token的處理，團隊提出 PaddleOCR-VL 的粗到細架構。首先引入一個輕量的 Valid Region Focus Module（VRFM），該模組利用定位與上下文關係預測的能力，識別出圖像中語意相關的有效視覺token。然後，在 VRFM 的引導下，訓練一個緊湊但強大的 0.9B 參數視覺語言模型（PaddleOCR-VL‑0.9B），專注於這些有效區域進行細部識別，避免直接處理整張大圖。  

🚀 **在頁級與元素級解析上實現 SOTA，同時大幅降低資源消耗**  
廣泛實驗顯示，PaddleOCR-VL 在頁級解析與元素級識別兩個維度均達到最先進表現，優於現有方案，並與頂尖視覺語言模型具備強競爭力。由於只處理經 VRFM 篩選出的有效區域，模型在推理時使用了顯著較少的視覺token與參數，從而在保持或提升準確度的同時實現更快的推理速度。  

💡 **透過定位與上下文預測抑制背景冗餘，讓模型聚焦有意義區域**  VRFM 的核心在於同時利用空間定位資訊與語義上下文關係，能夠區分出文件內容（文字、表格、圖表）與純粹背景。這使得後續的 0.9B VL 模型不必在冗餘區域上做無用運算，有效降低了計算複雜度，同時保留了進行精細辨識所需的特徵。  

⚠️ **目前未見具體限制說明，需進一步驗證長效與跨語言表現**  
根據所提供的摘要，論文未詳細說明實驗使用的資料集規模、消融實驗結果，亦未探討在極端低解析度、高噪聲或多語言文件上的泛化能力，這些屬於後續工作可以補充的方向。  

🎯 **開源程式碼與 0.9B 模型讓工程師可直接降低 OCR 系統的計算成本**  
論文同時開放了原始碼與預訓練模型（GitHub：https://github.com/PaddlePaddle/PaddleOCR），工程師可將 VRFM 與 0.9B VL 模型直接嵌入現有的文件理解流程，顯著削減視覺token數量與參數量，從而在不犧牲精度的前提下提升系統吞吐量與降低硬體需求。  

🔗 **論文連結**  
📝 Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing  
👤 Cheng Cui, Ting Sun, Suyin Liang, Tingquan Gao, Zelun Zhang（PaddlePaddle Team, Baidu Inc.; Xi’an Jiaotong University）  
🔗 論文：https://arxiv.org/abs/2603.24326  
💻 原始碼與模型：https://github.com/PaddlePaddle/PaddleOCR  

你是否也在為高解析度文件處理的算力瓶頸而煩惱？歡迎在留言區分享你的經驗或想法 👇  

#OCR #文件理解 #視覺語言模型 #PaddlePaddle #AI效率 #機器學習 #CVPR2026
