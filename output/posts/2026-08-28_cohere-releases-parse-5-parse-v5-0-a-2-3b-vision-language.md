---
title: 'Cohere Releases Parse 5 (parse-v5.0): A 2.3B Vision Language Model That Turns
  Enterprise Documents Into Markdown'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/27/cohere-releases-parse-5-parse-v5-0-a-2-3b-vision-language-model-that-turns-enterprise-documents-into-markdown/
model: claude-code/sonnet
generated_at: '2026-08-28T18:02:47.739667'
score: 93
---

📌 免接 OCR:Cohere 用 2.3B 參數 VLM 把企業文件直接解析成 Markdown

TL;DR：Cohere 推出 Parse 5,單一模型完成 PDF/PPT/圖片解析,附表格、版面座標,已上線生產環境。

企業文件擷取的老問題是：先跑 OCR、再接排版還原、再接表格辨識,一條 pipeline 疊三四個模型才能把 PDF 變成可用的結構化資料。Cohere 的做法是把這一整條鏈路壓進一個 22.3 億參數的模型裡。

🤔 **企業文件解析的痛點：層層疊加的 pipeline**

Cohere 發布的 Parse（`parse-v5.0`）鎖定高流量企業文件擷取場景,目標是省去獨立的 OCR 前處理階段,直接一次完成解析。

🧩 **單一模型吃下文字、表格、表單與版面座標**

Parse 是建構在 Cohere Labs 的 North-Micro-Vision-Instruct 架構上的視覺語言模型（VLM）,參數量 23 億,context window 為 8,192 tokens,模型體積約 4.6GB。使用方式是將 PDF、PPT 或 JPEG 頁面編碼為 base64 data URI 輸入,模型會回傳依閱讀順序排列的文字、以 HTML 呈現的表格、清單、表單的 key-value 配對、圖片描述,以及各元素的邊界框（bounding box）座標,整個過程沒有獨立的 OCR 階段。

輸出模式有兩種：預設回傳每頁的 Markdown 字串；設定 `output_format="blocks"` 則回傳型別化的區塊,例如表格區塊會同時附帶其 HTML 內容、邊界框與描述,這個模式讓「引用級別」的可追溯性成為可能。語言支援方面,阿拉伯文、英文、法文、德文、義大利文、日文、韓文、葡萄牙文、西班牙文等 9 種語言列為穩定支援,其餘語言則為零樣本（zero-shot）支援,準確度較低。

📊 **官方 ParseBench 79.2 分,但方法論有但書**

Cohere 公布 Parse 在 ParseBench 上取得 79.2 分,領先 Mistral OCR 4（74.5）、Azure Document Intelligence（74.3）與 Databricks AI Parse（72.4）。但 ParseBench 是 LlamaIndex 針對約 2,078 頁人工驗證的企業文件所建立的基準,原本分五個維度評分：表格、圖表、內容忠實度、語意排版與視覺定位,Cohere 的 79.2 分是取其中三個維度（表格、內容忠實度、語意排版）的平均,略去了圖表與視覺定位這兩個大多數解析器表現最差的維度。對照公開排行榜的完整五維度總分,Mistral OCR 4 為 60.68、Databricks AI Parse 為 60.68、Azure Document Intelligence（Layout）為 59.64,而 Azure 的三維度平均恰好是 74.3,與 Cohere 公布的數字一致,印證了這個計算方式。目前 Parse 5 本身尚未列在該公開排行榜上,榜首的 LlamaParse Agentic 為 84.88 分。換句話說,79.2 是廠商自行選取子維度計算的分數,並非排行榜上的正式名次。

💡 **定價與轉折點：多少頁該租專屬 GPU**

Parse API 定價為每千頁 1.50 美元。若透過 Model Vault 使用專屬實例,Medium 規格為每小時 4 美元或每月 2,500 美元,XL 規格為每小時 7 美元或每月 4,300 美元。換算下來,以每頁 0.0015 美元的 API 計費為基準,Medium 實例約在每月處理 167 萬頁時達到損益兩平,XL 約在 287 萬頁。低於這個量,按量計費的 API 較划算；高於這個量,專屬容量在單純的價格考量上就更有優勢,更不用說資料落地（data residency）需求通常才是企業選擇 Vault 的真正原因。

⚠️ **基準分數只反映部分維度,尚未接受第三方排行榜檢驗**

Cohere 自行公布的 79.2 分只涵蓋 ParseBench 五個維度中的三個,略過圖表與視覺定位這兩個較難的項目,且 Parse 5 目前並未出現在公開排行榜上,因此這個分數更適合當作參考,而非直接的排名依據。

🎯 **實務啟示**

若你的 pipeline 目前仍是 OCR 加多個後處理模型的組合,值得用自己的文件實測 Parse 5,尤其留意圖表與視覺定位這類官方分數沒有涵蓋的場景表現。若處理量已達百萬頁等級,也可以依照上述損益平衡點,評估改用 Model Vault 專屬實例是否更划算。

🔗 **來源**
- 標題：Cohere Releases Parse 5 (parse-v5.0): A 2.3B Vision Language Model That Turns Enterprise Documents Into Markdown
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/08/27/cohere-releases-parse-5-parse-v5-0-a-2-3b-vision-language-model-that-turns-enterprise-documents-into-markdown/

#Cohere #DocumentAI #VisionLanguageModel #OCR #EnterpriseAI #MarkdownParsing #MLOps #AIInfrastructure #DataExtraction #LLM
