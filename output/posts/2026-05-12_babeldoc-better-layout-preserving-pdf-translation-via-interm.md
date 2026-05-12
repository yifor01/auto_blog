---
title: "BabelDOC: Better Layout-Preserving PDF Translation via Intermediate Representation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.10845
score: 121
model: tencent/hy3-preview:free
generated_at: 2026-05-12T20:25:29.178165
---

📌 **BabelDOC：中間表示實現佈局保留的 PDF 翻譯**  
上海大學、Funstory.ai Limited、上海交通大學  

你曾經試過翻譯 PDF，結果排版全亂、圖表位移？這不是偶發狀況，而是現有翻譯管線在「語言處理」與「版面保留」之間的固有張力。  

🤔 **語言與版面的兩難**  
現行的 Computer-Assisted Translation (CAT) 系統側重文字，常會丟掉結構性元資料；而文件解析工具則專注內容提取，翻譯後難以忠實重繪原始佈局。跨語言溝通需求日益增長，如何同時保證翻譯準確與視覺完整，成為實務上的瓶頸。  

🧪 **基於 Intermediate Representation 的框架設計**  
BabelDOC 提出一個中間表示 (IR)，將視覺版面資訊與語意內容完全 decouple。在此表示層上，可進行：  
- 術語抽取  
- 跨頁上下文建模  
- 詞彙表約束生成  
- 公式佔位  

翻譯完成後，再經由自適應排版引擎將內容重新錨定至原始版面。實驗方面，團隊在一份精心策畫的 200‑頁 PDF 基準集上進行評估，結合人工評分與多模態 LLM-as-a-judge，比較了數種代表性基線。  

📊 **版面忠誠度與術語一致性顯著提升**  
結果顯示，BabelDOC 在版面忠誠度、視覺美感及術語一致性方面優於現有方法，同時保持具競爭力的翻譯精準度。這意味著，在不犧牲語言品質的前提下，文件的原始排版得以更好地保留。  

💡 **為何中間表示能突破瓶頸？**  
將版面與語意分離，使兩個原本相互競爭的任務能各自優化：語言模型專注於準確翻譯，排版引擎則專注於依照原始幾何與樣式重建。這種「先翻譯後排版」的流程，也為後續加入詞彙表控制、公式處理等細粒度需求提供了自然的擴充點。  

⚠️ **評估範圍有限，長尾文件效果尚待驗證**  
目前的實驗僅在 curated 200‑頁基準集上進行，極端複雜或高度非標準的 PDF（例如手繪圖、多層疊加圖形）的表現未在文件中說明。此外，雖然採用了多模態 LLM-as-a-judge，但人工評分的主觀性仍是影響結果的一個因素。  

🎯 **適合多語言技術文件的工程師**  
- 開源工具箱已在 GitHub 上獲得超過 8.4K ★、17 位貢獻者  
- 提供互動式下游應用（如線上預覽、術語編輯）  
- 面對需同時保留圖表、公式與排版的技術手冊、學術論文或產品說明書時，可直接使用 BabelDOC 進行高保真翻譯  

🔗 **論文連結**  
📝 BabelDOC: Better Layout-Preserving PDF Translation via Intermediate Representation  
👤 Qi Yang, Xiangyao Ma, Xiao Wang, Hao Wang, Rui Wang (Shanghai University; Funstory.ai Limited; Shanghai Jiao Tong University)  
🔗 https://arxiv.org/abs/2605.10845  

歡迎在留言區分享你在多語言 PDF 處理上的經驗或對此類中間表示方法的看法 👇  

#AI #PDF翻譯 #佈局保留 #中間表示 #開源工具 #上海大學 #Funstory #機器翻譯 #多語言文件 #GitHub #技術文檔
