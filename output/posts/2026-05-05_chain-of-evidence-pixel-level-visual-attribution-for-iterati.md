---
title: "Chain of Evidence: Pixel-Level Visual Attribution for Iterative Retrieval-Augmented Generation"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.01284
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-05-05T19:43:53.386039
---

📌 【北大x騰訊x港城大】iRAG 新突破：直接在截圖上圈出證據鏈

當我們在處理複雜的多跳問答（Multi-hop QA）時，傳統的 RAG 系統往往只能丟出一段文字，告訴你「答案在這篇文件的某處」。但對於充滿圖表、排版複雜的 PDF 或簡報，純文字解析往往會丟失關鍵的空間邏輯。現在，研究團隊直接讓 AI 看截圖來「圈重點」。

🤔 **純文本解析讓 iRAG 丟失了視覺線索**

Iterative Retrieval-Augmented Generation (iRAG) 雖然強大，但目前的系統大多依賴解析後的文本。這帶來兩個痛點：一是**粗粒度歸因**，用戶得自己在長文中找證據；二是**視覺語義丟失**，將簡報或圖表轉為文字時，空間關係和版面邏輯就消失了。這對於需要理解圖文排版的任務來說，是致命的缺陷。

🧪 **直接在截圖上推理，輸出 Bounding Boxes**

來自北京大學、騰訊及香港城市大學的研究團隊提出了 **Chain of Evidence (CoE)** 框架。與其依賴繁瑣的文檔解析，CoE 直接對檢索到的文檔截圖進行推理。

這是一個 **Retriever-Agnostic（檢索器無關）** 的視覺歸因框架，利用 Vision-Language Model (VLM) 直接在像素級別上定位證據，並輸出精確的 Bounding Box（邊界框），將完整的推理鏈可視化。

 **在 SlideVQA 上大幅超越文本基準**

研究團隊構建了 **Wiki-CoE**（基於 2WikiMultiHopQA 的大規模結構化網頁數據集）和 **SlideVQA**（充滿複雜圖表的簡報數據集）進行測試。

實驗結果顯示，經過微調的 **Qwen3-VL-8B-Instruct** 模型展現了強大的性能。在需要理解視覺版面的場景中，CoE 顯著超越了基於文本的基準方法，證明了直接處理視覺資訊的必要性。

💡 **從「看文字」到「看版面」的推理升級**

CoE 的核心在於它不再依賴格式特定的解析器（Parser），而是讓模型像人類一樣「看」文件。這意味著無論是複雜的圖表還是自由排版的簡報，模型都能捕捉到空間邏輯。這種像素級別的解釋性，讓 iRAG 系統不再是黑盒子，而是能展示具體推理路徑的透明系統。

⚠️ **視覺模型依賴與數據集侷限**

雖然 CoE 在視覺理解上表現出色，但其性能高度依賴底層 VLM 的能力。此外，目前的評測主要集中在結構化網頁和簡報上，對於更複雜的掃描文檔或手寫筆記的泛化能力，還需要進一步驗證。

🎯 **多模態 RAG 與 Agent 可解釋性的實用利器**

對於正在開發多模態 RAG 或 AI Agent 的工程師來說，CoE 提供了一個極具參考價值的實作方案。特別是在處理財報、學術簡報或技術文檔時，這種能夠「看圖說故事」並標註出處的能力，將大幅提升系統的可信度與除錯效率。

🔗 **論文連結**
📝 Chain of Evidence: Pixel-Level Visual Attribution for Iterative Retrieval-Augmented Generation
👤 Peiyang Liu, Ziqiang Cui, Xi Wang, Di Liang, Wei Ye
🏛️ National Engineering Research Center for Software Engineering, Peking University; City University of Hong Kong; Tencent Technology
🔗 論文：https://arxiv.org/abs/2605.01284
💻 開源代碼：https://github.com/PeiYangLiu/CoE.git

你覺得多模態 RAG 最難處理的文檔類型是什麼？歡迎留言討論 👇

#AI #RAG #MultimodalAI #VLM #PekingUniversity #Tencent #資訊檢索 #機器學習 #開源專案
