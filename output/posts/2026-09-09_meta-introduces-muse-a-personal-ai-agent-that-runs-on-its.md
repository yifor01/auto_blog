---
title: Meta Introduces Muse, a Personal AI Agent That Runs on Its Own Dedicated Secure
  Cloud Computer
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/08/meta-introduces-muse-a-personal-ai-agent-that-runs-on-its-own-dedicated-secure-cloud-computer/
model: claude-code/sonnet
generated_at: '2026-09-09T20:07:39.717951'
score: 81
---

📌 【Meta 新品】個人 AI agent Muse，每個使用者配一臺專屬雲端沙箱電腦

TL;DR：Meta 推出能代你談判、訂票、寄信的個人 agent Muse，每位使用者獨享一臺隔離的 Secure VM。

一個 AI agent 幫你去殺價、訂機票、寄郵件，聽起來像是又一個聊天機器人的行銷詞，但 Meta 這次把重點放在了看不見的地方：每個使用者背後，都有一臺專屬的雲端虛擬機在跑。

🤔 **不只是回答問題，而是替你去談判**

Meta 推出的 Muse 是一個會「動手做事」而非只回答問題的個人 AI agent。使用者用訊息描述任務或目標，Muse 會規劃並執行：開瀏覽器、填表單、代替使用者談判。Meta 給出的例子包括把車賣出更好的價格、把帳單金額談低、調整訓練計畫。Muse 也會記住跨對話的脈絡，例如把使用者存下來的 Instagram 食譜影片轉換成購物清單，並記得朋友的飲食限制。任務可以在使用者關掉 App 後繼續執行，只有在寄信、完成購買等敏感步驟時才會暫停等待使用者核准，所有操作都留有完整的稽核紀錄可供查閱。Muse 目前以消費級服務的形式在美國的 iOS、Android 與 muse.ai 上線，提供免費與付費方案；開發者無法自行架設 Muse 本體，但其底層模型 Muse Spark 1.3 已可透過 Meta Model API 與 Muse Code 使用，Meta 也表示未來規劃釋出開放權重版本。

🧩 **一人一臺 Secure VM：systemd-nspawn 沙箱、Sentinel 雙代理審核、憑證代理**

這次發表在安全設計上的著墨最多。Muse 的 agent 執行環境跑在一個 systemd-nspawn runtime cell 裡，經過 syscall 過濾並限制核心權限；真正敏感的安全服務則放在同一臺 VM 上、但這個 cell 之外。另有一個獨立的 Sentinel agent，負責核准每一個 connector 動作與每一次網路請求，同時涵蓋 Layer 4 與 Layer 7：Muse 負責提議動作，只有 Sentinel 能真正放行。憑證的處理採用「代理化（surrogation）」機制：Muse 本身只看得到佔位用的 token，真正的密鑰由 Sentinel 在網路邊界注入，這讓透過 prompt injection 竊取憑證在結構上變得不可能實現，因為根本沒有真的東西可以偷。系統層級還用 eBPF 做汙點追蹤（taint tracking），區分乾淨請求與曾接觸過使用者資料的請求，並依此決定是否需要核准；瀏覽器子 agent 看到的是無障礙樹（accessibility tree）而非原始 DOM，也無法執行 JavaScript；郵件 connector 預設會過濾掉一次性驗證碼與密碼重設連結。

📊 **比前代少 20% 工具呼叫、少 25% token**

底層模型 Muse Spark 1.3 由 Meta Superintelligence Labs 上週發表，鎖定長流程的 agentic 任務：零樣本 CLI 工具呼叫、多工作流程執行緒，以及在雜亂資料來源中的自我修正。Meta 工程師的內部比較顯示，相較於 Muse Spark 1.2，這一版大約少用 20% 的工具呼叫、少用 25% 的 token，Meta 也表示這個模型在抵抗 prompt injection 上已接近業界最先進水準。開發者現在就能在 Muse Code 與 dev.meta.ai 的 Meta Model API 中使用這個模型。

⚠️ **目前僅限美國消費端，無法自架**

Muse 本身是封閉的消費級服務，目前只在美國以 App 與網站形式推出，開發者無法自行部署完整的 Muse 系統；開放權重僅是 Meta 官方揭露的路線圖方向，尚未實際釋出。

🎯 **對工程師而言，值得借鏡的是安全架構而非產品本身**

雖然 Muse 產品本體不可自架，但其安全設計思路，例如把真實憑證與 agent 執行環境物理隔離、用獨立審核 agent 做雙重把關、以無障礙樹取代原始 DOM 降低瀏覽器 agent 的攻擊面，都是在設計任何具備瀏覽器與付款能力的 agent 系統時可以直接參考的模式。

🔗 **來源**
- 標題：Meta Introduces Muse, a Personal AI Agent That Runs on Its Own Dedicated Secure Cloud Computer
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/08/meta-introduces-muse-a-personal-ai-agent-that-runs-on-its-own-dedicated-secure-cloud-computer/

#Meta #AIAgent #MuseAI #AgentSecurity #PromptInjection #eBPF #SandboxIsolation #ConsumerAI #MetaSuperintelligenceLabs #AgenticAI
