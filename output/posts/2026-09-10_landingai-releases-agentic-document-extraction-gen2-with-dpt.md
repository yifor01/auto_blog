---
title: LandingAI Releases Agentic Document Extraction Gen2 with DPT-3 Pro and DPT-3
  Verity
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/09/landingai-releases-agentic-document-extraction-gen2-with-dpt-3-pro-and-dpt-3-verity/
model: claude-code/sonnet
generated_at: '2026-09-10T20:08:46.878999'
score: 80
---

📌 文件解析不再整頁計費，LandingAI把每個字都定位到頁面座標

TL;DR：LandingAI推出ADE Gen2與DPT-3模型家族，把文件解析從扁平分塊改成樹狀結構，並讓每個答案都能溯源回頁面上的具體文字。

如果你的文件解析結果連「這句話到底是掃描出來的原文，還是模型自己補上去的描述」都分不清楚，那PII遮罩、審核UI跟文件比對這些下游應用根本沒辦法自動化。LandingAI這次的Gen2就是衝著這個問題來的。

🤔 **從扁平分塊到樹狀結構**

LandingAI團隊表示，Gen1把一份文件當成一串扁平的區塊清單處理；Gen2則把文件當成一棵樹，計費方式從「按頁計價」改成「按回傳的字元數計價」，並且要求每個答案都能溯源回頁面上具體的一行或一個字。團隊將這次釋出的重點歸納為三個主題：可負擔性（affordability）、agent-ready輸出，以及原子級定位（atomic grounding）。ADE Gen2現已全面可用，開發者可在ADE playground免費開始使用，企業則可選擇美國或歐盟雲端、在AWS/Azure/Google Cloud的自有VPC內執行、部署在Snowflake，或是完全地端（包括air-gapped隔離環境）。

🧩 **兩顆模型分工：Verity管確定性轉錄，Pro管版面理解**

Gen2把解析工作拆成兩個模型，讓不同負載選擇對應的價格。DPT-3 Verity針對數位原生（非掃描）文件做確定性轉錄，對每個字都回傳邊界框與信心分數，主打高量文字、表格與簡單表單欄位的場景。DPT-3 Pro則先讀懂版面再讀文字，能辨識表格、圖表、頁邊註記、簽名等區塊類型並依閱讀順序回傳，也能處理掃描頁、手寫字、非拉丁文字與LaTeX數學式。LandingAI團隊表示Verity的信用點數消耗大約是Pro的四成，並計劃在2026年秋季之間推出兩個模型的自動路由機制。

🧩 **計費機制：頁面加字元的兩段式定價**

舊版DPT-2採取每頁固定3點數的計價方式；DPT-3改成「頁面成分＋輸出字元成分」的兩段式定價。以priority服務層級為例，DPT-3 Pro每頁收1點數，外加每千個輸出字元0.5點數；DPT-3 Verity每頁收0.3點數，外加每千字元0.2點數。standard層級的費率則是priority的一半。文中舉例，一份12頁、回傳48,120個字元的Pro解析，在priority層級約需36.1點數，standard層級大約是其一半，所有點數計算會四捨五入到小數點後一位，且回應的metadata會列出計算所用的每一項輸入。服務層級是第二個可調的槓桿：priority適合有人或agent正在等待結果的場景；standard則以0.5倍價格非同步執行，適合能容忍數分鐘到數小時延遲的批次流程，但同步呼叫一律以priority計價，playground本身也是跑在priority層級上。LandingAI預估混合工作負載可節省25%到80%成本，並宣稱用Verity搭配standard層級解析成本可低於每頁一美分，這些是廠商自陳數字，實際導入前仍需用自己的文件組合實測，因為按字元計價意味著文字密度高的頁面反而可能比舊制更貴。

🧩 **輸出格式：從樹狀結構到逐字定位**

Parse v2的回應包含三個頂層欄位：依閱讀順序排列的markdown、metadata與structure。structure是一個文件節點，底下是頁面節點，頁面節點底下是區塊節點，區塊類型包括text、table、table_cell、figure、marginalia、attestation、logo、card與scan_code。每個區塊都帶有一個「type-index」形式的語意ID（在同一次回應內穩定，但跨重新解析不保證一致），以及一個grounding物件，記錄頁碼、在markdown字串中的範圍與標準化後的邊界框。markdown輸出也做了標準化：圖表用`<figure type="CHART">`這類元素表示，模型生成的描述文字被隔離在`<description>`標籤內，確保轉錄內容不會與模型自己的評論混在一起；簽核類區塊會輸出如`[STAMPED][SIGNED]`的堆疊標籤，`[ILLEGIBLE_SIGNATURE]`與`[ILLEGIBLE_TEXT]`則是固定字面量；表格預設以HTML格式輸出以保留合併儲存格。

最關鍵的能力是原子級定位：每個葉節點區塊都帶有一個atomic_grounding陣列，DPT-3 Pro每個視覺行一筆、DPT-3 Verity每個字一筆。Verity會為每個字附上0到1的信心值（取該字內每個字元最低分數），可作為把不確定轉錄結果送去人工複核的訊號；表格儲存格本身也帶有自己的邊界框，不過Pro目前尚未提供儲存格層級的atomic grounding。Extract V2的引用（citation）就是從這套grounding機制取得，讓一個被抽取出來的欄位能追溯回頁面上的具體文字，這使得依座標做PII遮罩、文件差異比對與審核用UI從「大概對」變成「可精準建構」。

⚠️ **留意的限制**

語意ID只在單次回應內穩定、跨重新解析並不保證一致；Pro模型的表格儲存格層級atomic grounding目前是空的；廠商宣稱的成本節省幅度與每頁不到一美分的數字，都需要用自身文件組合實測驗證。

🎯 **實務啟示**

如果你的下游流程需要「這段抽取結果到底來自頁面哪個位置」這種可稽核性，例如PII遮罩、文件比對或人工複核UI，atomic grounding提供的逐字座標與信心分數，會比傳統扁平分塊的解析結果好用得多；而按字元計價也代表評估成本時，該看的是預期輸出字元量而非單純頁數。

🔗 **來源**
- 標題：LandingAI Releases Agentic Document Extraction Gen2 with DPT-3 Pro and DPT-3 Verity
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/09/landingai-releases-agentic-document-extraction-gen2-with-dpt-3-pro-and-dpt-3-verity/

#LandingAI #DocumentAI #DPT3 #AgenticAI #OCR #DocumentExtraction #DataGrounding #EnterpriseAI #RAG #MLOps
