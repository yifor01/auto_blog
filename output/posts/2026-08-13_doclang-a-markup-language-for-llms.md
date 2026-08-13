---
title: 'DocLang: a markup language for LLMs'
source: IBM Research
url: https://research.ibm.com/blog/doclang-ai-native-doc-standard?utm_medium=rss&utm_source=rss
model: claude-code/sonnet
generated_at: '2026-08-13T07:33:08.085742'
score: 94
---

📌 DocLang：讓 LLM 讀懂文件結構的 XML 方言

TL;DR：IBM 推出 Docling 的 AI 原生 complement DocLang，用更少 token 精確表達文件結構，降低推理成本。

PDF 告訴印表機把像素放在哪裡，DOCX 告訴文書處理器怎麼排版，但兩者都沒告訴 AI 模型「這是標題，那是圖說」。這正是 IBM 研究團隊想解決的問題。

🤔 背景：文件格式從來不是為機器理解而生

IBM 開源文件解析器 Docling 已幫助企業從舊圖表、客戶檔案、年報等資料中挖掘洞見，擁有 3,200 萬次下載與 64,000 顆 GitHub 星，是 IBM 史上最成功的開源專案，已被整合進 LangChain、Red Hat OpenShift，甚至 IBM 自家的 Granite 系列 LLM。Docling 的主要研究者 Peter Staar 指出，今天使用的文件格式各自為了不同目的設計：PDF 告訴渲染器像素該放哪裡，DOCX 告訴文書處理器如何排版頁面，兩者都不是為了需要理解內容的機器而設計。當這些格式被送進 AI pipeline，閱讀順序會變得模糊、表格會塌陷、圖片會失去圖說、metadata 會消失，而這一切都發生在模型看到內容之前，直接限制了準確度的上限。

🧩 DocLang 是什麼：一份文件只有一種表示法

Docling 會把 PDF、PPT、XLSX、MP4 等非結構化資料轉換成內部表示法，再序列化成 DocLang，一種為 LLM 設計、更易於解讀的受限 XML 方言。DocLang 的唯一任務是讓機器理解文件，它是一個開放標準（類比 JSON 之於資料、HTML 之於網頁），原生編碼語意、版面配置、bounding box 與閱讀順序。與其事後回復結構，DocLang 從一開始就定義好表示法。團隊也採取「一份文件只有一種正確編碼」的立場：兩套正確讀取同一份文件的系統，應該產出位元組層級完全相同的輸出，這個性質是先前的標準都不保證的，也是 DocLang 可訓練、可驗證的關鍵。

選擇 XML 作為基礎，是因為它有乾淨的語意-token 對應關係：每個語意 token 都有明確的開合標籤，例如 `<text>` 與 `</text>`，且直接對應到單一 LLM token，開標籤是一個 token，閉標籤是另一個。這種一對一對應意味著模型不必浪費容量去解析一種模糊的標記方言，文件結構與 token 串流的結構完全一致。團隊把語法字彙量控制在約 1,000 個 token，並把屬性語意推進巢狀元素而非 attribute，以維持這種緊密的對應關係。

💡 從表格辨識到整份文件：OTSL 到 DocTags 再到 DocLang

這個構想源自表格辨識的研究。團隊當初訓練 image-to-sequence 模型讀取表格並輸出 HTML，雖然可行但效率不佳，模型也常產生語法錯誤的 HTML。這促成了 Optimized Table Structure Language（OTSL），於 2023 年發表：如果設計一套精簡、專為目的打造的字彙，而不是借用 HTML，模型會更準確，推理時間下降，輸出也總是語法正確，表示法替模型完成了原本要求它做的工作。這個洞察被延伸到整個頁面，先發展出 DocTags，再有 256M 參數的視覺語言模型 SmolDocling，能一次轉換含表格、公式、程式碼與圖表的頁面，效能可與參數量大 27 倍的模型競爭。過程中團隊也學到什麼不該做：DocTags 並非符合 XML 規範、也不完整，某些文件結構就是無法乾淨表達。DocLang 在此基礎上，建構出同樣 token 高效、機器原生，但符合 XML 規範、完整且 canonical 的表示法。

📊 DocLang 帶來的好處

用更小的模型達到更高準確度，如同 OTSL 與 SmolDocling 所展現的，表示法承擔了更多工作；不會出現幻覺結構，DocLang 的文法讓非法輸出根本無法被表達，不論是非矩形表格或未閉合的元素，整類錯誤直接不可能發生；無損且有根據，完整的表格網格、圖片位置、閱讀順序與 bounding box 都被保留供模型處理；一致性可被建構，每份文件只有一種 canonical 編碼，代表可以拿它訓練、diff、快取與驗證；內建治理機制，個資標記、RAG 權限、訓練限制等資訊存在文件的 head 裡，而非脆弱的 side-car 檔案，合規 metadata 因此與內容綁在一起；也不只限於文件，DocLang 的原語可延伸到音訊逐字稿、圖片與影片片段，對走向多模態的 pipeline是重要特性；此外它是 Linux Foundation 治理下的開放標準，無廠商鎖定，任何工具或 pipeline 都能實作或消費它。

⚠️ 採用之路還有幾道關卡

標準的價值取決於採用它的生態系，沒有實作的規格只是一份文件，這是團隊在推出時就搭配實際支援的原因。完整性與一致性之間的取捨也是挑戰：文件的世界永遠混亂，每次為了涵蓋邊界案例而增加表達力，都可能製造出新的表示方式，要守住「一份文件、一種表示法」同時涵蓋現實世界的複雜度，是持續進行中的設計工作，這也是 DocLang 目前仍停留在 0.x 版本、並把 minor 版本視為可能破壞相容性的原因，團隊選擇把 canonical 形式做對，而非過早凍結。遷移成本是第三個挑戰：任何既有 pipeline 的擁有者都得投入工具與重新訓練的成本才能轉換，團隊認為準確度的提升值得這個投資，但這是不該被忽視的真實成本。另外還有治理風險，要讓標準維持真正開放、不分裂成各廠商專屬版本，這既是技術問題，也是人與流程的問題。

🎯 實務啟示

團隊的採用策略有三部分：先讓 DocLang 在 Linux Foundation 治理下保持免費、開放、中立，不受廠商鎖定；接著讓 DocLang 成為既有工具的原生輸出格式，而不是要求整個生態系重寫 pipeline，目前 Docling 與 ABBYY 的 FineReader Engine（OCR 用的 SDK）已能輸出 DocLang。對於已經在用 Docling 做文件解析、或正在打造 RAG／多模態 pipeline 的工程團隊，DocLang 值得關注之處在於它把「結構理解」從模型的隱性負擔，轉移成表示法本身的顯性保證，對降低 token 用量與提升下游準確度都有直接幫助。

🔗 來源
- 標題：DocLang: a markup language for LLMs
- 作者／機構：IBM Research
- 連結：https://research.ibm.com/blog/doclang-ai-native-doc-standard?utm_medium=rss&utm_source=rss

#DocLang #Docling #IBMResearch #XML #DocumentAI #LLM #RAG #OpenStandard #Multimodal #TokenEfficiency
