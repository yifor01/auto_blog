---
title: 'Genspark Open Sources GenOffice: A Free, Ad-Free AI Office Suite for macOS
  and Windows with Docs, Sheets, Slides, PDF'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/03/genspark-open-sources-genoffice-a-free-ad-free-ai-office-suite-for-macos-and-windows-with-docs-sheets-slides-pdf/
model: tencent/hy3:free
generated_at: '2026-08-05T08:54:21.255949'
score: 72
---

📌 【Genspark 開源】打造 AI 原生辦公套件：GenOffice 釋出，主打無廣告與高相容性

TL;DR：GenOffice 是基於 Electron 的 AI 原生辦公套件，提供 Docs、Sheets、Slides 與 PDF 工具。

隨著 AI 整合進生產力工具成為趨勢，Genspark 推出了開源辦公套件 GenOffice（目前版本 0.4.110）。這不是在傳統工具上「外掛」一個對話框，而是將 AI 編輯直接融入工作流程的 AI 原生設計。目前該專案已在 macOS (Apple Silicon) 與 Windows (x64) 上提供安裝檔。

🧩 **以 AI 編輯為核心的五合一架構**

GenOffice 採用 Electron 架構，由五個應用程式共享一個引擎層，涵蓋文字處理、試算表、簡報編輯及 PDF 工具：

- **Docs (文件)**：採用 TipTap 流式編輯器，支援區塊級別 (block-granular) 的 AI 編輯，並具備快照 (snapshots) 與差異比對 (diffs) 功能。
- **Sheets (試算表)**：基於開源的 Univer 核心，並透過 Rust 撰寫的 sidecar 進行 XLSX 的匯入與匯出。
- **Slides (簡報)**：內建解析與渲染引擎，支援母版、圖表、裁剪、手寫筆觸與文字塑形 (text shaping)。
- **PDF**：基於 pdf.js 與 pdf-lib，提供註解、表單、大綱、印章與簽章功能。
- **Shell**：提供主畫面、分頁管理與自動更新。

📊 **解決 Office 檔案相容性痛點的技術路徑**

針對使用者最擔心的檔案毀損問題，GenOffice 採用了「局部更新」的策略：

- **精準修補 (Narrow Patches)**：以原始檔案作為「真相來源」(source-of-truth)，僅針對被修改的區塊 (dirty blocks) 轉換為 OOXML 片段，並重新拼接回原始的 XML 結構。
- **保留原始位元組**：未更動的區塊會保留原始位元組，確保開啟與儲存後，在 Microsoft Word 中的排版不會毀損。
- **高度還原**：分頁檢視能重現原始行距，並支援追蹤修訂、註解、樣式、公式與手寫筆觸。

🛡️ **極致的安全防禦設計**

雖然目前處於 Alpha 階段，但其 `SECURITY.md` 展現了高度的安全性考量：

- **沙箱隔離**：每個文件視窗均開啟 `contextIsolation: true`、`nodeIntegration: false` 與 `sandbox: true`。
- **指令限制**：簡報的佈局指令碼會透過 Acorn 解析，並在受限的 AST 解釋器中執行，完全禁止使用 `eval`、`Function` 或任何具備網路/IPC 橋接能力的語法。
- **惡意內容隔離**：針對匯出時可能產生的 AI 生成 HTML，系統會將其放在一個完全隔離、無預載載入 (no preload) 且具備看門狗超時 (watchdog timeout) 機制的隱藏視窗中進行渲染。

⚠️ **Alpha 階段的限制與使用建議**

- **AI 功能需帳號**：由於模型呼叫是透過伺服器端代理，使用 AI 功能需要 Genspark 帳號。
- **企業導入建議**：由於目前為 Alpha 版本且 AI 路徑需連至雲端，受監管行業的企業在部署前需先完成審查與 DPIA 評估。
- **授權限制**：專案採用 Apache License 2.0，允許商業修改，但 `ee/` 目錄保留給未來的企業版模組使用，且商用時不得使用 GenOffice 與 Genspark 的商標。

🎯 **實務啟示**

對於新創公司與中小企業而言，GenOffice 提供了一個免授權費、無廣告且高相容性的生產力工具選擇。對於工程師，其「局部修補 XML」而非「重新生成整個檔案」的設計思路，是處理複雜文件格式相容性時非常值得參考的實作模式。

🔗 **來源**
- 標題：Genspark Open Sources GenOffice: A Free, Ad-Free AI Office Suite for macOS and Windows with Docs, Sheets, Slides, PDF
- 連結：https://www.marktechpost.com/2026/08/03/genspark-open-sources-genoffice-a-free-ad-free-ai-office-suite-for-macos-and-windows-with-docs-sheets-slides-pdf/

#AI #OpenSource #GenOffice #Genspark #Productivity #Electron #Rust #SoftwareArchitecture #CyberSecurity #OfficeSuite
