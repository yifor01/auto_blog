---
title: "ShieldNet: Network-Level Guardrails against Emerging Supply-Chain Injections in Agentic Systems"
source: ChatPaper/AI
url: https://arxiv.org/abs/2604.04426
score: 106
model: gpt-4o-free
generated_at: 2026-04-07T13:46:56.397336
---

📌 AI Agent 供應鏈攻擊的網路層解法

你還在用程式碼掃描器檢查 AI Agent 的外掛工具？最新研究指出，面對惡意 MCP 工具注入，現有防護幾乎失效。真正的威脅偵測，其實不該看程式碼，而該看網路封包。

🤔 **Prompt 注入飽和，供應鏈攻擊成新危機**

隨著 Agentic 系統從實驗走向企業部署，AI 不再只是對話框，而是能直接呼叫第三方 API 與工具的自動化節點。Model Context Protocol (MCP) 等標準的普及，讓工具串接變得容易，但也開啟了新的攻擊面。攻擊者不再需要費心繞過 Prompt 防禦，只需將惡意邏輯嵌入看似正常的第三方工具中，就能在 Agent 執行時靜默劫持流程、外洩敏感資料或觸發未授權操作。

然而，當業界焦點仍停留在 Prompt 注入與輸入輸出過濾時，針對這類供應鏈威脅的評估基準卻是空白。缺乏標準化的測試場域，導致安全團隊難以量化風險，也無法驗證現有防護的有效性。

🧪 **1 萬筆惡意工具基準與 MITM 偵測架構**

為填補此缺口，研究團隊首先建構了 `SC-Inject-Bench`。這個大規模基準測試包含超過 10,000 個惡意 MCP 工具，攻擊手法嚴格對照 MITRE ATT&CK 框架，涵蓋 25 種以上的供應鏈攻擊類型（如依賴混淆、工具劫持、資料外洩等）。測試結果顯示，現有的 MCP 掃描器與基於 LLM 的語義防護在此基準上表現不佳，難以識別經過偽裝的惡意行為。

基於此發現，團隊提出 `ShieldNet` 架構。核心設計理念是「放棄表面工具追蹤，改監控底層網路互動」。架構由三個模組組成：
1. MITM Proxy：攔截 Agent 與外部服務之間的所有網路流量。
2. Event Extractor：從原始封包中提取關鍵行為事件（如異常端點存取、資料傳輸模式）。
3. Lightweight Classifier：將行為特徵輸入輕量級分類模型進行即時偵測。

🔍 **F-1 高達 0.995，誤報率僅 0.8%**

在 `SC-Inject-Bench` 上的嚴格測評顯示，ShieldNet 的偵測 F-1 分數最高達到 0.995，同時將誤報率壓低至 0.8%。與現有 MCP 掃描器及 LLM 語義防護相比，ShieldNet 在多數攻擊類別上呈現壓倒性優勢。更重要的是，該架構引入的執行期開銷極低，證明網路層監控不會成為 Agentic 系統的效能瓶頸。

💡 **從「靜態掃描」轉向「動態行為」的關鍵躍遷**

為什麼傳統掃描會失敗？惡意工具通常會進行代碼混淆或語義偽裝，讓靜態分析與 LLM 的語意理解難以察覺。但工具最終必須執行，一旦觸發惡意行為，就必然會產生特定的網路互動模式（例如向非預期伺服器回傳資料、短時間內密集呼叫特定 API）。

ShieldNet 的設計巧妙在於將防禦層下移：不嘗試解讀工具「說了什麼」，而是觀察工具「做了什麼」。輕量級分類器取代昂貴的 LLM 推理，不僅大幅降低延遲與運算成本，更避免了 LLM 防護常見的幻覺與提示詞繞過問題。這代表 AI 安全防護正從「語義過濾」走向「行為可觀測性」。

⚠️ **聚焦網路層，企業部署需面對架構與隱私挑戰**

ShieldNet 的架構雖高效，但實務部署仍有限制。首先，MITM Proxy 需要修改企業網路拓撲或調整 Agent 的代理設定，在微服務或混合雲環境中可能帶來整合成本。其次，該方法專注於網路層互動，對於不依賴外部通訊的純本地運算側信道攻擊可能無法覆蓋。最後，基準測試雖規模龐大且基於 MITRE 分類學，但仍屬合成環境，真實供應鏈的複雜度與對抗性演變仍需長期追蹤。

🎯 **企業 Agentic 系統應導入網路層可觀測性**

- **不要單點依賴工具市場審核**：第三方 MCP 工具的審核機制無法替代執行期的動態監控，企業應將網路層防護納入 Agentic 堆疊的標準資安規範。
- **平衡效能與偵測精度**：ShieldNet 證明輕量級分類器足以應付高維行為特徵，實戰上可優先採用規則引擎或小型 ML 模型進行第一線過濾，避免過度依賴重型 LLM 防護。
- **提前規劃 MCP 安全標準**：隨著 MCP 成為主流，工具供應商應內建行為宣告與權限最小化機制，資安團隊則需熟悉 MITRE ATT&CK 在 AI 供應鏈的映射，提前佈署類似 ShieldNet 的流量分析節點。

🔗 **論文連結**
📝 ShieldNet: Network-Level Guardrails against Emerging Supply-Chain Injections in Agentic Systems
👤 Zhuowen Yuan, Zhaorun Chen, Zhen Xiang, Nathaniel D. Bastian, Seyyed Hadi Hashemi (UIUC, UChicago, UGA, USMA, eBay, JHU, UCSB, Virtue AI)
🔗 論文：https://arxiv.org/abs/2604.04426

如果你的團隊正在導入 AI Agent 處理關鍵業務，你會優先考慮在工具層還是網路層佈署防護？歡迎在下方分享你的架構設計與實戰經驗 👇

#AISecurity #AgenticAI #MCP #SupplyChainSecurity #NetworkDefense #ShieldNet #資安架構 #企業AI
