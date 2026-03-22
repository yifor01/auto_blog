---
title: "ESAA: Event Sourcing for Autonomous Agents in LLM-Based Software Engineering"
source: ChatPaper/AI
url: https://arxiv.org/abs/2602.23193
score: 118
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-02-27T23:18:59.570587
---

📌 **ESAA 架構：用事件溯源模式，讓 AI 代理系統不再「腦袋空空」**

當多個 AI 代理在協作開發軟體時，它們常常面臨一個根本問題：每個代理都像「失憶的天才」，雖然能生成優雅的程式碼，但無法持續追蹤整個專案的狀態變化。這篇論文提出 ESAA (Event Sourcing for Autonomous Agents) 架構，用事件溯源模式解決 LLM 代理系統的狀態管理困境。

🤔 **AI 代理的根本困境：腦袋裡沒有「專案記憶」**

目前的 LLM 代理系統存在三個核心問題：
- 缺乏原生狀態管理：每次對話都是全新的，無法記住過去的行為
- 上下文隨時間衰減：長任務中，代理會逐漸忘記專案細節
- 機率生成 vs 確定執行：LLM 的輸出是機率性的，但軟體執行需要確定性

這些問題在多代理協作時尤其嚴重，想像多個代理同時修改同一個專案，卻沒有人知道「誰改了什麼、為什麼改」。

🧪 **ESAA 架構：用事件溯源解決代理的「失憶症」**

ESAA 的核心設計理念是：**代理只說「我打算做什麼」，系統負責「記錄並執行」**。

架構運作方式：
1. **代理發出意圖**：代理只產生結構化的 JSON 意圖（如 agent.result 或 issue.report），不直接修改檔案
2. **確定性協調器**：驗證意圖、持久化到 append-only 日誌（activity.jsonl）
3. **效果應用**：協調器負責實際的檔案寫入和專案狀態變更
4. **可驗證檢視**：透過 roadmap.json 提供專案狀態的可驗證檢視

這就像給每個代理裝上「專案記憶晶片」，它們可以專注於思考，而系統負責記憶和執行。

⚙️ **關鍵設計特色：讓 AI 協作變得可追蹤**

- **邊界合約 (AGENT_CONTRACT.yaml)**：定義代理的權限和責任範圍
- **元提示檔 (PARCER)**：管理不同代理的個性化設定
- **重播驗證 (esaa verify)**：使用雜湊確保已完成任務的不可變性
- **取證追蹤**：每個事件都有完整的歷程記錄

這些設計確保了多代理系統中的責任歸屬和可追溯性。

📊 **實證驗證：從單代理到多代理的擴展性**

**案例一：單代理著陸頁專案**
- 9 個任務、49 個事件
- 單一代理組合
- 結果：run.status = success, verify_status = ok

**案例二：多代理臨床儀表板系統**
- 50 個任務、86 個事件
- 4 個並行代理跨越 8 個階段
- 使用異構 LLM（Claude Sonnet 4.6、Codex GPT-5、Antigravity/Gemini 3 Pro、Claude Opus 4.6）
- 結果：run.status = success, verify_status = ok

多代理案例特別展示了 ESAA 在真實並行協作中的表現，證明了架構的可擴展性。

🎯 **為什麼這很重要：可信賴的 AI 協作開發**

ESAA 架構解決了 AI 代理系統的一個根本性問題：如何讓機率性的思考者在確定性的世界中可靠地協作。這不僅對軟體工程有重要意義，也為更複雜的多代理系統（如自主規劃、智慧合約等）提供了基礎架構。

🔗 **論文連結**
📝 ESAA: Event Sourcing for Autonomous Agents in LLM-Based Software Engineering
👤 Elzo Brito dos Santos Filho (CPS - Centro de Pesquisa e Desenvolvimento em Software; GitHub; AutoGen; MetaGPT; LangGraph)
🔗 論文：arxiv.org/abs/2602.23193

你認為事件溯源模式還能應用在 AI 系統的哪些場景？歡迎分享你的想法 👇

#AI #LLM #軟體工程 #多代理系統 #事件溯源 #MetaGPT #LangGraph #AutoGen #技術架構
