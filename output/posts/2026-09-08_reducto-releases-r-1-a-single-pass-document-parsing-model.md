---
title: 'Reducto Releases r-1: A Single Pass Document Parsing Model That Cuts Errors
  20% at 1 Cent Per Page'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/07/reducto-releases-r-1-a-single-pass-document-parsing-model-that-cuts-errors-20-at-1-cent-per-page/
model: claude-code/sonnet
generated_at: '2026-09-08T20:10:55.279203'
score: 87
---

📌 Reducto 發表 r-1：文件解析從多階段合併為單次前向，每頁只要 1 美分

TL;DR：Reducto 用單次全頁前向解析取代多階段 agentic OCR，錯誤率降 20%、成本砍到六分之一，但目前僅提供 API，沒有開放權重。

文件解析這件事，過去幾年業界的做法一直是「疊模型」：OCR 一層、版面偵測一層，複雜文件再疊上 agentic 的 vision-language 模型校正。每多一次模型呼叫，就多一次延遲與成本。Reducto 上週發表的 r-1，賭的是反方向：把整個流程壓回一次前向傳遞。

🤔 **多階段疊加的代價，正是 r-1 想解決的問題**

Reducto 原本的 legacy Parse 將 OCR、版面偵測、後處理拆成獨立階段，複雜文件還會額外疊加 agentic vision-language 模型的處理回合。處理財報、保險理賠、合約等文件的團隊，常常需要跨多個供應商路由檔案，再自行疊加後處理才能達到可用的準確率。Reducto 表示，r-1 要解決的正是這種「協調成本」（orchestration cost），而不只是單純拉高字元辨識準確率。

🧩 **單次全頁前向，把七件事一起做**

r-1 是一個架構重寫後的新解析模型家族的第一代，將文字、表格、圖片、版面、閱讀順序、格式與定位資訊全部整合進一次全頁前向傳遞。每個區塊回傳時都會附上頁面相對邊界框（page relative bounding box），把內容對應回頁面上的實際位置。

根據文件，r-1 在單次前向中原生處理：數位文字、掃描件與手寫字；具備周邊頁面脈絡的表格結構（含合併儲存格與巢狀標題）；欄位、頁首、頁尾、側欄與閱讀順序的統一解析；圖片偵測並附上簡短描述；具語意的格式（標題、清單、粗體、底線、刪除線）；以及透過頁面相對邊界框達成的定位能力。Reducto 特別點名密集表格、非典型版面、低品質掃描、浮水印內容、以及不遵循固定範本的文件,是目前仍具挑戰性的長尾案例——一個被漏掉的刪除線可能會讓合約條款的意思整個反過來,一個誤讀的表格則可能讓下游 agent 拿到錯誤的數字。

📊 **官方數字：錯誤率降 20%，成本降到 1 美分**

Reducto 宣稱,r-1 早期預覽版相較於自家 legacy agentic pipeline,錯誤率降低 20%；在內部評測中,面對複雜文件時的表現也優於 Amazon Textract、Azure Document Intelligence 等主流雲端服務與大型 LLM。價格方面,原本的 legacy agentic 模型每頁成本落在 3 到 6 美分之間,r-1 則是統一收費每頁 1 美分,不疊加功能加價或額度費用。

需要提醒的是,這 20% 的錯誤率下降,是相對於 Reducto 自家舊 pipeline 的比較,而非對照第三方基準;與雲端服務、LLM 的比較也是由 Reducto 自行執行,並未公開評測資料集或評測框架,讀者在解讀時應留意這一點。

⚠️ **只能透過 API 使用,沒有開放權重**

r-1 目前是預覽階段,只能透過 Reducto 託管的 Parse API(V3)使用,以設定旗標開啟,沒有開放權重、也無法自行部署本地 checkpoint。Reducto 平臺本身另外支援多租戶雲端、客戶 VPC、地端部署與氣隙(air-gapped)環境,並具備 SOC 2 Type II 認證,較高方案支援 HIPAA 資料處理。若請求未指定 settings.model,系統仍會照舊跑 legacy Parse,不會無聲失敗;Studio 中新建的 pipeline 則預設使用 r-1。若工作流程需要自訂 prompt 或進階圖表擷取,agentic 處理仍會被疊加在 r-1 結果之上,但會增加延遲。Reducto 也預告了下一步:針對速度與成本敏感場景的 r-1 mini,以及依頁面自動選擇模型的路由機制。

🎯 **實務啟示**

若團隊目前用其他解析服務,想比較遷移成本,可向 Reducto 申請最高 5,000 美元的額度做並排比較;若已在使用 Reducto,遷移前應先檢查 r-1 的設定相容性文件,因為部分舊設定可能被忽略或不支援。由於沒有開放權重,選擇這個方案等於綁定 Reducto 的託管服務,這是評估時需要納入的長期考量。

🔗 **來源**
- 標題：Reducto Releases r-1: A Single Pass Document Parsing Model That Cuts Errors 20% at 1 Cent Per Page
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/07/reducto-releases-r-1-a-single-pass-document-parsing-model-that-cuts-errors-20-at-1-cent-per-page/

#DocumentAI #OCR #Reducto #DocumentParsing #LLM #DataExtraction #EnterpriseAI #MLOps #AIProductivity #VisionLanguageModel
