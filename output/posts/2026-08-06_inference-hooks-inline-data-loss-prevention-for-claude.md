---
title: 'Inference hooks: inline data loss prevention for Claude Enterprise'
source: Claude Blog
url: https://claude.com/blog/claude-enterprise-inference-hooks
model: tencent/hy3:free
generated_at: '2026-08-06T08:26:03.195369'
pinned: true
---

📌 【Anthropic 新功能】Inference hooks：為 Claude Enterprise 提供即時資料外洩防護 (DLP)

TL;DR：Inference hooks 讓企業能透過單一層級，即時檢查並攔截所有 Claude 請求與工具回傳內容。

隨著企業將 AI 整合進工作流程，資安團隊面臨一個嚴峻挑戰：如何確保員工在與 AI 對話或使用工具時，不會不經意地洩露敏感資料？過去，這種即時攔截（inline enforcement）的能力僅限於 Claude Code 的用戶端 hooks，而現在 Anthropic 推出的 Inference hooks 補足了這項技術缺口。

🧩 **一站式攔截所有 Claude 互動介面**

Inference hooks 提供了一個統一的執行層，讓企業無需針對不同產品進行重複整合，即可保護所有 Claude Enterprise 的使用場景，包含：
- Claude Chat (對話介面)
- Claude Code
- Claude Cowork
- 以及其他 Claude Enterprise 產品

不僅如此，這項機制也涵蓋了所有工具調用（tool calls），無論是透過 MCP 連接器、技能（skills）還是外掛程式（plugins）產生的工具回傳結果，都會經過檢查後才傳送回模型。

⚙️ **運作機制：基於 WebSocket 的即時驗證**

當組織啟動 Inference hooks 後，所有的推論請求都會透過一個經過簽章的 WebSocket 連線路由至企業指定的安全性伺服器。其運作流程如下：
1. **發送請求**：Claude 會將 Prompt（提示詞）及其周邊上下文發送到企業的安全性伺服器。
2. **模型等待**：在模型開始生成內容前，會等待伺服器的裁決。
3. **執行裁決**：伺服器回傳「允許（allow）」或「拒絕（deny）」的指令。
4. **執行結果**：Claude 僅在收到允許指令後才會繼續進行推論。

對於工具調用，當 Claude 呼叫工具時，系統會在工具的回傳結果送回模型之前，執行相同的檢查流程。

💡 **靈活的部署與管理策略**

為了降低導入難度並符合不同企業的風險承受度，Inference hooks 提供了多種部署選項：
- **擴展現有 DLP 方案**：採用開放的 Webhook 協定與公開的 Schema，可直接對接現有的資安工具（如 Netskope、Palo Alto Networks、Proofpoint、Zscaler）或企業自建的 AI 安全伺服器。
- **漸進式部署**：支援「影子模式（Shadow mode，預設總是允許）」、「基於角色的排除機制」以及「百分比分流部署」。
- **自定義容錯**：企業可以根據風險承受能力，自定義失敗策略（failure-policy）、逾時（timeouts）等設定。

🎯 **實務啟示**

對於企業資安工程師而言，這項功能將「資料外洩防護 (DLP)」從事後的日誌審查，轉向了事前的即時攔截。透過單一配置即可覆蓋整個 Claude 生態系，極大地簡化了企業在導入 AI 時的合規性與安全性管理工作。

🔗 **來源**
- 標題：Inference hooks: inline data loss prevention for Claude Enterprise
- 機構／作者：Anthropic
- 連結：https://claude.com/blog/claude-enterprise-inference-hooks

#AI #Anthropic #Claude #EnterpriseAI #DLP #Cybersecurity #DataProtection #MachineLearning #AIInfrastructure #TechNews
