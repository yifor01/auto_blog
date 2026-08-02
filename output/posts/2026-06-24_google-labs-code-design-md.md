---
title: google-labs-code/design.md
source: GitHub Trending
url: https://github.com/google-labs-code/design.md
score: 108
model: google/gemma-4-31b-it:free
generated_at: '2026-06-24T20:02:46.447973'
---

📌 【Google Labs】讓 AI 懂設計系統：透過 DESIGN.md 規範視覺識別

TL;DR：一種結合 YAML token 與 Markdown 敘述的新格式，讓 Coding Agent 能精準掌握設計系統。

當你叫 AI 寫前端介面時，最痛苦的往往不是邏輯，而是 AI 產出的 UI 總是「感覺不對」——顏色不統一、間距隨機，或者完全無視品牌調性。

🧩 **將設計規範轉化為 AI 可讀的結構化檔案**

Google Labs 提出的 `DESIGN.md` 旨在為 Coding Agent 提供一個持久且結構化的視覺識別（Visual Identity）理解方式。它不只是簡單的風格指南，而是一種將「精確數值」與「設計意圖」結合的格式規範。

該格式由兩個核心部分組成：
1. **機器可讀的 Design Tokens**：使用 YAML front matter 存放精確數值（如顏色碼、字型大小、圓角與間距），讓 AI 能直接呼叫精確參數。
2. **人類可讀的設計理據 (Design Rationale)**：使用 Markdown 散文描述設計理念，告知 AI 這些數值為何存在以及如何應用。

📊 **從 Token 到視覺呈現的對應關係**

以該專案提供的範例來看，`DESIGN.md` 的運作邏輯如下：

- **精確數值 (Tokens)**：定義 `primary: #1A1C1E`、`tertiary: #B8422E` 以及 `h1: 3rem` 等具體參數。
- **設計意圖 (Prose)**：描述整體風格為「建築極簡主義 (Architectural Minimalism)」與「新聞權威感 (Journalistic Gravitas)」，並將 `tertiary` 顏色定義為唯一的互動驅動色 (sole driver for interaction)。

當 Coding Agent 讀取此檔案後，能將上述定義轉化為實際產出：使用 Public Sans 字型的深墨色標題、溫暖的石灰岩背景，以及使用 "Boston Clay" 色的 Call-to-Action 按鈕。

🎯 **實務啟示：減少 AI 介面開發的溝通成本**

對於開發者而言，這提供了一種將設計系統（Design System）「程式碼化」的新路徑。與其在 Prompt 中反覆描述「請使用深灰色且具有現代感」，不如提供一個標準化的 `DESIGN.md` 檔案，讓 AI 在生成 UI 時有據可依，確保產出的視覺一致性。

🔗 **來源**
- 標題：google-labs-code/design.md
- 機構：google-labs-code
- 連結：https://github.com/google-labs-code/design.md

#AI #DesignSystem #CodingAgent #GoogleLabs #Frontend #UIUX #DesignTokens #YAML #Markdown #WebDevelopment
