---
title: Lightweight PDF parser with layout, tables, formulas and bounding boxes
source: Hacker News
url: https://github.com/beatrizalmeidaf/papero-pdf-text-extractor
model: claude-code/sonnet
generated_at: '2026-10-02T21:30:54.355500'
score: 93
---

📌 不靠ML模型，papero用幾何法解析PDF版面

TL;DR：papero用純幾何運算還原PDF的閱讀順序、表格與公式，CPU就能跑，適合RAG資料前處理。

把PDF裡的文字挖出來很容易，難的是把「這是第幾欄、這段是不是表格、公式長在哪裡」這些結構資訊找回來——而papero宣稱做到這件事完全不需要ML模型。

🤔 **抽出文字容易，抽出結構才是RAG真正需要的東西**

README指出，讓輸出對RAG、搜尋與LLM真正有用的關鍵，是結構而不是純文字：哪一欄先讀、哪些行其實是一張表格、公式畫在什麼位置。papero選擇用純幾何運算（plain geometry）處理這個問題，因此可以在一般筆電的CPU上跑，不需要GPU或ML模型。

🧩 **靠bounding box撐起的六項核心能力**

根據README，papero的設計圍繞著幾個具體能力展開：閱讀順序（reading order）方面，能處理雙欄、三欄論文的逐欄閱讀順序，並把頁首、頁尾、頁碼、重複的logo另外標記出來；表格方面，能識別有框線、無框線以及LaTeX booktabs風格的表格，還原成列與欄（含跨行的多行儲存格），並可匯出成CSV或Excel；公式方面，能辨識指數、下標、堆疊分數與手繪根號，輸出成LaTeX格式（例如`\frac{5}{12}`、`\sqrt{2}`），並附上該公式區域的裁切圖；每一個區塊都帶有bounding box位置資訊，可用於在RAG回答中精確引用原文位置、或在頁面上疊加標記；圖片與向量圖表會被裁切成PNG，並連同標題、座標軸標籤、圖例一併保留；匯出Word時則盡量保留原始版面，包括欄位、對齊、縮排、行距與字體粗細，雙欄版面匯出後仍是雙欄。另外README也提到幾個細節處理：LaTeX PDF裡被拆成獨立字符畫出的重音符號會被還原（例如「Computa¸ca˜o」還原成「Computação」）、表單產生器常用的隱藏白色文字會被捨棄、掃描頁面會自動跑OCR，DOCX／PPTX／XLSX／EPUB／HTML等格式則透過Apache Tika讀取。

**怎麼用**：`pip install papero-extract`後，用`extract("paper.pdf")`取得文件物件，可呼叫`.to_markdown()`、`.tables`、`.formulas`、`.figures`等屬性取出對應內容；也提供CLI指令（如`papero-extract extract paper.pdf -o paper.md --images`）、批次模式（`papero-extract batch ./documents -o ./dataset`可把一整個資料夾的PDF轉成RAG資料集，連同切好的chunks.jsonl與逐份文件的fidelity報告一起輸出）、以及用Docker compose一次拉起API、Apache Tika與Tesseract服務的REST API模式。

💡 **fidelity報告拿PDF本身當對照，而不是標準答案**

README特別說明，batch模式產出的fidelity報告是拿每份文件去跟它自己的PDF原文比對（沒有外部ground truth），檢查像是PDFium讀到的文字是否都出現在輸出中、閱讀順序有沒有跳欄錯讀、每個「Table N」標題底下是否真的抓到對應表格等訊號——因此作者提醒這份報告該被當成「該去哪裡複查」的指引，而不是精確度分數。瀏覽器版應用也內建同樣的檢查，並提供Compare分頁讓使用者逐頁比對PDF原文與抽取結果。

🎯 **實務啟示**

如果你的RAG流程正在為「表格被拆散」「公式變成亂碼」「多欄論文讀錯順序」所苦，papero提供的bounding box與chunk溯源（每個chunk都記錄來自哪一頁、哪個區塊）值得拿來實測；而且因為全部在CPU上跑、PDF不必上傳到任何服務，對於需要本機處理敏感文件的場景也多一個選項。批次模式附帶的fidelity報告，則可以當成資料集上線前的自動化複查清單，先挑出有問題的文件人工複核，而不是整批盲目信任抽取結果。

🔗 **來源**
- 標題：Lightweight PDF parser with layout, tables, formulas and bounding boxes
- 作者／機構：beatrizalmeidaf
- 連結：https://github.com/beatrizalmeidaf/papero-pdf-text-extractor

#PDFParsing #RAG #DocumentAI #OCR #DataExtraction #OpenSource #LaTeX #NLP #MachineLearning #DeveloperTools
