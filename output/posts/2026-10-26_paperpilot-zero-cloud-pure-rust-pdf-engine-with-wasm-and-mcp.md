---
title: PaperPilot – Zero-Cloud, Pure-Rust PDF Engine with WASM and MCP
source: Hacker News
url: https://github.com/KrushnaVardhanReddy/PaperPilot
model: claude-code/sonnet
generated_at: '2026-10-26T21:58:22.747610'
score: 72
---

📌 PDF 工具全部塞進一顆 Rust 核心,檔案不用離開你的電腦

TL;DR：PaperPilot 用同一套 Rust 引擎同時當 MCP server、CLI、WASM 與桌面 App。

把 PDF 丟給雲端服務做 OCR 或合併,檔案就離開了你的電腦,對接 AI agent 處理文件的場景更是如此。PaperPilot 的做法是反過來：引擎用純 Rust 寫,全部在本機或瀏覽器記憶體內跑完,連 Chromium 跟雲端呼叫都不需要。

🤔 **為誰解決什麼問題**

目標使用者是兩群人：一是需要在本機操作 PDF 的人,二是需要讓 Codex、Claude Code、Kimi Code、Pi、Claude Desktop、Cursor 等 MCP client 具備「合併、分割、OCR、壓縮 PDF」能力的 AI agent 開發者。README 強調「private by default」與「agent-ready」,MCP 支援是一級功能而非事後補上的介面。

🧩 **一顆核心,五種介面**

架構上是單一 Rust workspace 拆成多個 crate：`paperpilot-core`、`paperpilot-pdf`、`paperpilot-nlp`、`paperpilot-gateway`、`paperpilot-mcp`、`paperpilot-wasm`、`paperpilot-storage`,再往外接出五種介面：

- MCP server（stdio)：給 coding agent 用
- CLI：批次與腳本化工作流
- 瀏覽器（WASM)：zero-install,檔案只在瀏覽器記憶體處理
- 桌面 App：Tauri + Svelte 做的檢視器、標註、diff 工具
- 本機 REST API：`localhost:7823`,可從 Python、Node、n8n 呼叫

因為五種介面共用同一顆核心,行為理論上是一致的。底層建構在 `lopdf`、`pdf_oxide`、`rten`（純 Rust 實作的 PaddleOCR）等既有函式庫之上。

🧩 **怎麼用**

接 MCP 的方式是把編譯好的 `paperpilot-mcp` 路徑寫進 `claude_desktop_config.json`：

```json
{
  "mcpServers": {
    "paperpilot": { "command": "/path/to/paperpilot-mcp" }
  }
}
```

重啟 Claude 後就能直接說「合併這兩份 PDF 並壓縮」。CLI 則是這樣用：

```
paperpilot merge --inputs doc1.pdf doc2.pdf --output merged.pdf
paperpilot compress --input in.pdf --quality 75 --output compressed.pdf
paperpilot rotate --input in.pdf --pages 1,3-5 --angle 90 --output out.pdf
```

本機 REST API 啟動後也能直接用 curl 打 `/api/v1/pdf/merge`,文件在 `localhost:7823/docs`。從源始碼建構需要 Rust 1.75 以上、Node.js 與 pnpm。

💡 **這不是重新發明 PDF 解析演算法**

PaperPilot 的賣點不在底層演算法創新,而是把現有的 Rust PDF 生態（lopdf、pdf_oxide、rten）整合成一套跨平臺、行為一致的工具鏈,並把 MCP 當成第一等公民介面。對已經有 PDF 處理需求的 AI agent 開發者來說,省掉的是「自己包一層 MCP wrapper」的工夫。

⚠️ **目前的能力邊界**

README 標示目前是 v0.6,已有的功能是組織（合併/分割/旋轉/刪除頁/重排/抽取頁/小冊子/N-up)、壓縮、文字與 OCR 抽取、安全性（水印、簽章驗證/移除、PII 掃描、深度清理)、Office 資料轉換（Excel 轉 JSON/CSV)。PDF 轉 Markdown/Word/Excel/PowerPoint、加密解密簽署、redaction、表單標註,以及 render/repair/compare 等功能都列在 roadmap（v0.7 至 v1.0),尚未完成。Community Edition 採 Apache 2.0,SSO、RBAC、audit log、DLP 等企業功能則是另外開發的 Enterprise Edition。

🎯 **實務啟示**

如果你在幫 coding agent 接 PDF 工具,又在意文件不能上傳到第三方雲端,PaperPilot 提供了一個開箱即用的本機 MCP server 選項；但目前功能仍偏基礎操作,格式轉換與進階安全功能要等後續版本。

🔗 **來源**
- 標題：PaperPilot – Zero-Cloud, Pure-Rust PDF Engine with WASM and MCP
- 作者／機構：vardhan1237
- 連結：https://github.com/KrushnaVardhanReddy/PaperPilot

#PaperPilot #Rust #MCP #PDF #WASM #AIAgent #OpenSource #LocalFirst #DeveloperTools #ClaudeCode
