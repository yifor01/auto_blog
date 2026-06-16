---
title: microsoft/fara
source: GitHub Trending
url: https://github.com/microsoft/fara
score: 126
model: google/gemma-4-31b-it:free
generated_at: '2026-06-16T21:07:15.875628'
---

📌 【Microsoft 最新研究】Fara-7B：專為「電腦操作」設計的高效 Agentic 模型

當我們討論 AI Agent 時，大多數人關注的是它能「對話」，但真正的挑戰在於它能否像人類一樣「操作電腦」？Microsoft 最近開源了 Fara-7B，這是一個專注於 Computer Use (CUA) 的高效 Agent 模型，並同步釋出了多套嚴謹的評測基準，試圖解決 AI 操作電腦時最棘手的「驗證」與「時效性」問題。

🤔 **AI 操作電腦的痛點：如何定義「成功」？**

讓 AI 操作瀏覽器或桌面軟體並不難，難的是如何客觀評估 AI 的操作路徑是否正確。過去的評測往往依賴簡單的最終結果，但這無法分辨 AI 是「運氣好」還是「真的理解操作邏輯」。此外，許多 Web 任務具有時效性（例如預約 2025 年的機票），一旦日期過期，原本的測試集就失效了。

🧪 **從 WebTailBench V2 到 CUAVerifierBench 的評測設計**

為了讓評估更精準且具持續性，Microsoft 針對 Fara-7B 構建了兩套關鍵基準：

1. **WebTailBench V2**：針對 609 個任務套件進行更新。最核心的改動是將過期的日期（如 2025 年 11 月）向前推移，並重新修訂預計算的評分標準 (Rubrics)，確保測試集在 2026 年依然有效。
2. **CUAVerifierBench**：這是一個由人工標記的基準，專門用來評估「驗證器 (Verifiers)」的表現。簡單來說，就是用來測試「負責打分的 AI 裁判」是否能正確判斷 Agent 的操作軌跡 (Trajectories) 是否正確。

💡 **建立「裁判」的基準，讓 Agent 進化更透明**

CUAVerifierBench 的設計亮點在於它提供了對比分析。研究團隊提供了 `fara7b_om2w_browserbase`（基於 Mind2Web/Browserbase）以及內部測試集，並對比了「盲測 (UV-blind)」與「已知答案 (UV-informed)」的標記結果。

這種設計揭示了一個關鍵洞察：要提升 Agent 的能力，不能只優化模型本身，必須先建立一個強大的「驗證機制」，讓模型知道自己的操作路徑在哪裡出錯。

⚠️ **目前仍處於快速迭代期，部分功能即將推出**

根據 GitHub 更新日誌，Fara-1.5 的 Agent Harness 尚未正式發布（標記為 Coming soon），目前的重點在於 Fara-7B 的基礎能力與評測框架的完善。

🎯 **工程實踐：簡化部署流程，快速建立評測管線**

對於 AI 工程師來說，這次更新最實用的部分在於 `webeval` 套件的去依賴化：
- **移除複雜依賴**：移除了 `autogen-core` 與 `autogen-ext` 的依賴，Chat Completion 客戶端現在完全獨立。
- **快速部署**：不再需要複雜的 submodule 安裝步驟，僅需 `pip install -e .[vllm]` 即可快速啟動，大幅降低了將 CUA 評測整合進 CI/CD 管線的門檻。

🔗 **資源連結**
📝 **專案名稱**：microsoft/fara
👤 **開發團隊**：Microsoft
🔗 **GitHub**：https://github.com/microsoft/fara
📊 **相關數據集**：microsoft/WebTailBench

如果你正在開發能操作瀏覽器或自動化工作流的 AI Agent，Fara-7B 提供的驗證框架比模型本身更值得研究。

你認為 AI Agent 進入「操作電腦」階段後，最大的風險是什麼？歡迎在下方討論 👇

#AI #Agent #Microsoft #ComputerUse #Fara7B #WebTailBench #LLM #自動化
