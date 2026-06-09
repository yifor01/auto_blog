---
title: How an Agent Built a 3D Paris Gallery by Chaining Two Hugging Face Spaces
source: HuggingFace Blog
url: https://huggingface.co/blog/mishig/spaces-agents-md
score: 95
model: google/gemma-4-31b-it:free
generated_at: '2026-06-09T20:38:05.559070'
---

📌 【Hugging Face 最新實踐】AI Agent 串接 Space：從影像生成到 3D 藝廊的自動化路徑

你以為 AI Agent 只能寫 Code 或聊天？這次的實驗證明，Agent 已經能像組裝樂高一樣，直接調用多個 AI 服務來完成複雜的多模態創作。

作者在完全沒有手動操作影像生成器或 3D 重建工具的情況下，僅透過一個 Coding Agent，就成功打造出一個展示巴黎地標的 3D 藝廊。

🤔 **多模態開發的痛點：模型強大，但整合太痛苦**

目前的 AI 開發面臨一個矛盾：我們有頂尖的影像、影片、TTS 或 3D 重建模型，但真正的門檻不在於模型本身，而是在於「整合」。

開發者必須處理 SDK 串接、權重部署、GPU 環境配置以及繁瑣的輸入格式轉換。這種高度碎片化的整合過程，往往讓開發成本遠高於模型調用本身。

🧪 **將 Hugging Face Spaces 視為「可調用的建構塊」**

這次實作的核心理念是將 Hugging Face Spaces 視為一個個獨立的「功能模組」。

作者利用 Coding Agent 串接了兩個不同的 Hugging Face Spaces：
1. **影像生成 Space** $\rightarrow$ 產生巴黎地標的圖片。
2. **3D 重建 Space** $\rightarrow$ 將影像轉換為 3D Gaussian Splats。

Agent 的工作不再是從零開始寫所有邏輯，而是扮演「膠水」的角色，將這些已經驗證過且可運行的服務串接在一起，最後將產出的資產整合進一個電影感的檢視器中。

💡 **「建構塊經濟」正從程式庫擴展至多模態 AI**

這項實踐印證了 Mitchell Hashimoto 提出的「建構塊經濟 (Building Block Economy)」概念：
軟體開發的最有效路徑不再是打造一個巨大的單體應用 (Monolith)，而是由許多小型、文件完善的組件組成。

AI 在從零開始構建複雜系統時可能不夠穩定，但它非常擅長「將成熟的碎片黏合在一起」。以往這種模式主要發生在 npm 封裝庫的程式碼世界，而現在，Hugging Face Spaces 正讓這種模式進入多模態 AI 領域。

🛠️ **關鍵技術：agents.md 讓 Space 變成 API**

為什麼 Agent 能如此精準地調用這些服務？關鍵在於 Hugging Face 引入的 `agents.md`。

現在大多數 Gradio Space 都會公開一個 plain-text 的 `agents.md` 文件，這相當於給 Agent 的「使用說明書」，明確告知 Agent 如何透過 curl 或 API 呼叫該服務。這讓每一個 Space 都變成了一個可被 AI 識別且調用的標準化模組。

🎯 **實務啟示：從「開發功能」轉向「定義介面」**

對於 GenAI 開發者與技術管理者，這帶來一個重要的思考轉向：

- **模組化優先**：與其嘗試開發一個全能的大型應用，不如將功能拆解為多個小型、定義明確的服務。
- **強化可發現性**：確保你的 AI 服務有良好的文件（如 `agents.md`），讓 Agent 能自主發現並調用。
- **Agent as Integrator**：未來多模態應用的開發重心，將從「如何實作模型」轉向「如何定義 Agent 的串接路徑」。

🔗 **詳細內容與 Demo**
📝 How an Agent Built a 3D Paris Gallery by Chaining Two Hugging Face Spaces
👤 Mishig Davaadorj
🔗 完整文章：https://huggingface.co/blog/mishig/spaces-agents-md
👉 成果展示：mishig/monuments-de-paris

如果你正在構思多模態應用，你會選擇從零開發，還是嘗試這種「建構塊串接」的模式？歡迎在下方討論 👇

#AI #GenerativeAI #HuggingFace #AIAgent #3DGaussianSplatting #SoftwareArchitecture #多模態
