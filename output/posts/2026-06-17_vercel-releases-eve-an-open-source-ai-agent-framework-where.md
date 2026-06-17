---
title: 'Vercel Releases Eve: An Open-Source AI Agent Framework Where Each Agent is
  a Directory of Files Mapped to Capabilities'
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/17/vercel-releases-eve/
score: 96
model: google/gemma-4-31b-it:free
generated_at: '2026-06-17T20:35:18.123048'
---

📌 【Vercel 開源 Eve】用「文件夾結構」定義 AI Agent，告別冗長的開發樣板

開發 AI Agent 最痛苦的往往不是設計 Prompt，而是為了讓 Agent 能在產線運行，得花大量時間搭建基礎設施（Plumbing）與重複撰寫註冊程式碼。

你以為建構一個可擴展的 Agent 需要複雜的框架配置？Vercel 提出一個反直覺的設計：把 Agent 變成一個「資料夾」，文件結構本身就是能力定義。

🤔 **定義能力不應等於搭建基礎設施**

大多數團隊在開發 Agent 時，常發現自己不斷地在重複構建相同的結構以滿足生產環境的需求。Vercel 認為，Agent 應該有其「形狀（Shape）」，而開發者的核心工作應該是定義「它能做什麼」，而不是處理如何讓它在生產環境中穩定運行的底層邏輯。

為了簡化這個過程，Vercel 將其內部運行超過一百個 Agent 的實踐經驗，封裝成這個名為 `eve` 的開源框架。

🧪 **以文件系統為中心的設計：資料夾即契約**

`eve` 採用「Filesystem-first」的設計理念。在 `eve` 中，一個 Agent 就是磁碟上的一個目錄，而這個目錄結構即是該 Agent 的能力契約（Contract）：

- **極簡起步**：最簡單的 Agent 僅需兩個文件：一個定義模型（Model），另一個定義指令（Instructions）。
- **指令即 Prompt**：`instructions.md` 文件會直接成為 `eve` 在每次模型呼叫前加入的 System Prompt。
- **模型配置**：模型定義僅需一行，且透過 AI Gateway 支援供應商的備援機制（Fallbacks）。

🛠️ **能力映射：新增一個文件，即新增一項能力**

`eve` 將 Agent 的各項能力直接映射到文件夾中。開發者不需要撰寫繁瑣的註冊程式碼（Boilerplate），只要在對應路徑新增文件，`eve` 在建置時會自動偵測並完成接線：

- **工具 (Tools)**：一個帶有 Zod 輸入 Schema 的 TypeScript 文件即是一個工具。其檔名與在目錄樹中的位置，直接決定了該工具的定義。
- **擴展能力**：新增 Skill、Channel 或 Schedule 只需要添加對應的文件，系統會自動將其整合進 Agent 之中。

💡 **「Batteries Included」：將基礎設施標準化**

Vercel 將 `eve` 定義為「電池內建」的框架，旨在將團隊重複開發的基礎組件標準化。相較於其他框架需要手動組裝各個碎片，`eve` 直接提供六項產線級能力，讓工程師能將精力集中在 Agent 的邏輯開發而非環境搭建。

目前 Vercel 已將其內部運行的六個真實 Agent 案例公開，證明了該框架在生產環境中的可行性與擴展能力。

🎯 **對工程師的實務啟示：快速原型到產線化的捷徑**

- **降低開發摩擦**：透過單一指令即可完成 Scaffolding 並安裝依賴，極大縮短了從 Idea 到 Demo 的時間。
- **結構化管理**：文件系統的視覺化特質，讓團隊能一眼看出 Agent 具備哪些能力、存放在哪裡以及何時觸發，降低了維護成本。
- **適合快速迭代**：對於需要頻繁實驗不同能力組合的團隊，這種「新增文件 = 新增功能」的模式比傳統的配置檔更直觀。

🔗 **相關資源**
📝 Vercel Releases Eve: An Open-Source AI Agent Framework
👤 Asif Razzaq (MarkTechPost)
🔗 閱讀全文：https://www.marktechpost.com/2026/06/17/vercel-releases-eve/
📦 npm package: `eve` (Apache-2.0 License)

如果你的團隊正深陷於 Agent 的基礎設施開發泥沼，或許這種「文件夾即能力」的設計能提供新的解決方案。

#AI #Vercel #AIAgents #OpenSource #TypeScript #LLMOps #軟體工程
