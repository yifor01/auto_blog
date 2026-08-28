---
title: Previewing the Model Hardware Standard
source: Anthropic News
url: https://www.anthropic.com/news/model-hardware-standard-research-preview
model: claude-code/sonnet
generated_at: '2026-08-28T17:58:50.404081'
pinned: true
---

📌 Anthropic 推出 Model Hardware Standard，讓 AI agent 操作實驗室機臺

TL;DR：Anthropic 攜手 HHMI Janelia 推出 MHS，讓 AI agent 標準化操控實驗室與產線設備。

實驗室裡最耗時的往往不是實驗本身，而是讓一臺顯微鏡、一支機械手臂、一臺液體處理機彼此「講得上話」。Anthropic 這次要解決的正是這個看似枯燥、卻拖垮無數研究進度的整合問題。

🤔 每臺設備都是一座孤島

公告指出，實驗室或產線要整合硬體設備，過去往往得花上數週甚至數月：多數設備彼此不互通，需要專人打造客製化的整合程式。Anthropic 因此與 HHMI Janelia Research Campus 合作，開發 Model Hardware Standard（MHS），一套讓 AI agent 安全操作實體設備的共用規格。

🧩 標準化驅動程式怎麼運作

MHS 的核心是一支標準化的驅動程式（driver）：介於作業系統與硬體設備之間的翻譯層。公告說明其設計：

- 用一組簡單的原語（primitives）操作任何硬體，例如「read」（讀取溫度）與「write」（設定溫度）。
- 讓每臺設備以標準格式變得可被發現（discoverable），設備與 agent 之間不再需要客製化的「翻譯程式」就能跨網路互相溝通。
- 驅動程式內建標籤，讓使用者能用自然語言直接寫入設備的特性資訊，例如機械手臂的重量，這類過去只存在紙本手冊或工程師個人經驗中的「默會知識」。系統會依據這些標籤自動產生一份參考檔案，說明設備能測量什麼、能調整什麼、安全限制為何，讓 agent 具備操作該設備所需的完整資訊。
- Agent 可透過三種機制控制硬體：MCP（Model Context Protocol）、command line interface，以及程式碼檔案（APIs），三者搭配可用一行程式碼跨多臺設備協調工作。

公告提到，MHS 相容於任何具備可程式化介面的設備，且與模型無關（model-agnostic），任何 agent harness 都能透過 MCP 等標準協定存取。

📊 Agent 在實驗中展現的探索行為

Anthropic 在測試 MHS 時觀察到，Claude 會以近似科學家的方式探索實驗：先調整雷射參數，透過攝影機觀察光束移動結果，再重複這個過程以理解因果關係，最後把學到的東西整理成一支確定性的（deterministic）腳本，讓後續的雷射對準工作只需一行指令即可執行，不必每一步都重新推理。

💡 五個早期試點案例

公告列舉了幾個合作夥伴的早期專案：

- Genentech：以 MHS 打造 BCA 蛋白質檢測（蛋白質濃度標準檢測程序）的自動化概念驗證，協調液體處理機、機械手臂與盤片讀取儀。
- 華盛頓大學 Baker 與 Pinglay 實驗室：博士生 Zihao Song 用 MHS 打造遠端監控儀表板、由 agent 監督的 qPCR 流程（能在適當時機自動停止），以及機械手臂與液體處理機之間的無碰撞交接。
- 卡內基美隆大學：用 MHS 讓 agent 協調液體處理機、盤片讀取儀、機械手臂與監控攝影機（分散在三臺介面互不相容的電腦上），把劑量反應曲線實驗的速度提升到約三倍。
- HHMI Janelia：科學家 Virginie Ruetten 用 MHS 統一了原本需要七套不同廠商程式、彼此沒有共通介面的顯微鏡實驗設備。
- QuEra Computing：這家使用中性原子打造量子電腦的公司，用 MHS 讓 AI agent 控制量子機臺內部分雷射系統。

⚠️ 目前僅開放研究預覽

MHS 目前僅對第一批科學研究實驗室與先進製造商開放研究預覽，尚未開源。公告表示，開放給更多科學、機器人、電子與製造業合作夥伴的目的，是為了共同建立安全性評估與最佳實務，之後才會將標準開源。

🎯 實務啟示

對於管理實驗室或產線自動化的工程團隊，MHS 提出的「標準化驅動程式 + 自然語言標註 + MCP 存取」組合，指出了一條把 agent 從純軟體任務延伸到實體世界的務實路徑：與其為每臺設備寫死客製整合，不如把設備特性宣告成 agent 可讀的規格，讓 agent 自己去學習操作方式、甚至把探索過程固化成可重複執行的腳本。若你的團隊有大量異質硬體需要協調，現在可以申請加入研究預覽，及早了解這套規格的介面設計。

🔗 來源
- 標題：Previewing the Model Hardware Standard
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/news/model-hardware-standard-research-preview

#Anthropic #Claude #MCP #ModelHardwareStandard #LabAutomation #Robotics #AIAgents #ScientificComputing #QuantumComputing #Manufacturing
