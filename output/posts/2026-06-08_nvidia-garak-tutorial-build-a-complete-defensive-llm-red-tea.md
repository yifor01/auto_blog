---
title: 'NVIDIA garak Tutorial: Build a Complete Defensive LLM Red-Teaming Workflow
  with Custom Probes and Detectors'
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/06/nvidia-garak-tutorial-build-a-complete-defensive-llm-red-teaming-workflow-with-custom-probes-and-detectors/
score: 96
model: google/gemma-4-31b-it:free
generated_at: '2026-06-08T20:41:40.085322'
---

📌 【NVIDIA Garak】打造 LLM 紅隊測試工作流：從自動化掃描到自訂探針實作

當企業將 LLM 部署至生產環境時，最擔心的不是模型不夠聰明，而是模型會不會被「誘導」輸出有害內容。如何系統化地測試模型的安全性，而非僅靠隨機的 Prompt 嘗試？

🤔 **隨機測試不足以應對 LLM 安全威脅**

許多開發者在測試模型安全性時，往往依賴手動輸入一些惡意指令來觀察反應。然而，這種方式缺乏系統性且難以量化。為了建立真正的防禦體系，我們需要一套標準化的「紅隊測試 (Red-Teaming)」工作流，能夠自動化地發起攻擊、偵測漏洞並量化風險。

🧪 **從環境搭建到端到端安全掃描**

這篇由 Sana Hassan 提供的教學詳細展示了如何使用 NVIDIA 的開源框架 `garak` 建立一套完整的防禦性紅隊工作流。其核心流程並非單次掃描，而是涵蓋了從插件探索到漏洞分析的完整生命週期：

1. **基礎配置**：安裝 `garak` 並透過 shell 指令在 Notebook 中快速部署。
2. **插件探索**：檢查內建的 Probes (探針)、Detectors (偵測器)、Generators (生成器) 與 Buffs。
3. **驗證與實測**：先以 Test Generator 進行 Dry run 確認環境，隨後對 Hugging Face 的真實模型執行多探針掃描 (Multi-probe scan)。
4. **量化分析**：利用 pandas 與 NumPy 解析 JSONL 報告，計算安全分數與攻擊成功率 (Attack Success Rates)。

💡 **核心機制：探針 (Probes) 與偵測器 (Detectors) 的協作**

`garak` 的強大之處在於其模組化設計，讓安全工程師能精準定義「如何攻擊」以及「如何判定失敗」：

- **Probes (探針)**：負責產生攻擊性輸入。教學中展示了如何建立「自訂探針」，使用固定 Prompt 來測試特定的漏洞場景。
- **Detectors (偵測器)**：負責分析模型輸出。教學示範了如何定義「自訂偵測器」，用來標記 (flag) 潛在的不安全輸出。
- **分析閉環**：透過提取被標記的 Prompt 與對應的偵測分數，開發者能直觀地理解模型在哪些特定行為上存在漏洞，而非僅僅得到一個「安全/不安全」的結論。

⚠️ **實作限制：依賴環境配置與模型存取**

此工作流的執行效率高度依賴於對 Hugging Face 模型權限的存取以及環境變數的正確配置。此外，自訂偵測器的準確度將直接影響漏洞判定結果，需要工程師根據具體的業務場景定義精準的標記邏輯。

🎯 **安全工程實踐：建立量化的安全基準線**

對於 AI 工程師與安全研究員，建議將 `garak` 整合進 CI/CD 流程中：
- **量化風險**：不要只看單一案例，應利用 AVID 導出功能與安全分數建立模型版本的安全基準線 (Baseline)。
- **針對性強化**：利用自訂探針針對業務高風險場景（如個資外洩、有害指令）進行壓力測試。
- **閉環優化**：根據偵測器標記的「Hit」案例，反過來優化模型的 System Prompt 或微調對齊 (Alignment) 策略。

🔗 **教學資源**
📝 NVIDIA garak Tutorial: Build a Complete Defensive LLM Red-Teaming Workflow with Custom Probes and Detectors
👤 作者：Sana Hassan
🔗 文章連結：https://www.marktechpost.com/2026/06/06/nvidia-garak-tutorial-build-a-complete-defensive-llm-red-teaming-workflow-with-custom-probes-and-detectors/

你目前在 LLM 安全測試中，最擔心的漏洞是什麼？歡迎在下方分享你的經驗 👇

#AI #LLMSecurity #RedTeaming #NVIDIA #Garak #AI安全 #模型防禦 #MachineLearning
