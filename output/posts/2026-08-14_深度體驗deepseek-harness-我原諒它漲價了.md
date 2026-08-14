---
title: 深度體驗DeepSeek Harness，我原諒它漲價了
source: 量子位
url: https://www.qbitai.com/2026/08/472208.html
model: claude-code/sonnet
generated_at: '2026-08-14T07:29:53.481685'
score: 93
---

📌 DeepSeek 開源 Harness：把 Agent 執行時做成「一切皆外掛」的作業系統

TL;DR：DeepSeek 開源 DSH，用全外掛架構挑戰 Codex 封閉核心。

如果一套 Agent 框架的說明文件裡反覆出現同一個詞「Cordis」，還教你怎麼從零打造外掛接進官方核心，這就不只是一款工具，更像一套開放作業系統。量子位作者 Jay 內測 DeepSeek Harness（DSH）近半個月，甚至把手邊所有 Vibe Coding 專案都從 Codex 遷移過來，最終的感觸是：這是一套徹頭徹尾為「自進化」與「DIY」而生的框架。

🤔 從安裝到上手：一個網頁介面，四種 Agent 預設

DSH 提供兩種安裝方式，一是在已有 Node.js 環境下用 npx @deepseek-ai/dsh web 快速啟動 Web UI，二是直接 git clone 官方 GitHub 倉庫。啟動後需先填入 DeepSeek 平臺的 API Key（也支援接入其他模型），介面外觀與 DeepSeek 網頁版相近，差別在於對話列表變成了本地專案管理列表。

開啟新會話前，除了選工作目錄，還要選擇 Agent 預設：標準模式涵蓋檔案編輯、Shell、檔案與網頁檢索、Skills、計劃模式、目標追蹤、子代理與工作流等完整能力；PTC 模式在此之上加入 Code Mode SDK，讓模型能寫 TypeScript 程式組合多步操作；極簡模式只保留 bash 與 str_replace_editor 兩個工具，用於基準測試與最小化復現；創造模式則額外提供執行時檢查、外掛實驗與 preset 撰寫指引。使用者也能自訂預設。

🧩 核心設計：Cordis，Agent 世界的樂高底板

DSH 的一切，包括模型、工具、策略、儲存與上下文管理，都被拆成可插拔的外掛，官方稱之為「一切皆外掛」架構，這塊底板就叫 Cordis。開發者若不滿意某個外掛，可以直接拔下替換；有魔改需求，也能照規則寫一個新外掛插上去，倉庫的 Doc 資料夾甚至提供從零構建外掛、接入官方 Harness 的完整教程，還內建了一個專門用來魔改 Cordis 本身的 Skill。

這與目前主流 Agent 框架的思路明顯不同。文章指出，即便 Codex 的 Harness 已經開源，骨子裡仍是類似 iPhone 的封閉哲學：用 Rust 寫單體核心以直接掌控記憶體與併發，MCP 工具、hooks、skills 等擴充只能掛在核心外部，無法觸碰主幹。DSH 選擇把 Cordis 作為一等公民開放出來，目前官方已內建超過 100 個外掛，社群也已經產出了 TUI 介面、懷舊 QQ 風格皮膚、鯨魚專屬 emoji 等成果，甚至有人做出了作者一直缺的側邊欄外掛。

DSH 另一個實用設計是「軌跡」（Trajectory）功能。不同於經過潤色的 Chat 摘要，軌跡能直接檢視原始事件級記錄，隨時回放整個會話內部發生的細節，方便定位模型在哪個環節出錯、每個環節花費多少成本。倉庫中還內建了多個開發向 Skill，例如用於審查 PR 的 dsh-code-review、尋找程式碼簡化空間的 dsh-find-simplifications，以及管理文件與文案規範的 dsh-doc-standards、dsh-prose-standard。此外，即便沒開計劃模式，DSH 在指令不明確時也會主動提問並給出建議選項，這點與 Codex 的行為不同。

📊 同題實測：一句 Prompt 直出，長任務不繞彎子

作者讓 V4 Flash 分別在 DSH 與 Codex 底下、以相同模型與推理強度跑同幾個 demo。經典的「鵜鶘腳踏車」測試中兩者差異不大，Codex 的產出審美甚至更好。但在「豬八戒 3D 白模」測試中，只給了一句簡單任務指令，Codex 六分鐘就交付、幾乎沒有返工，成品觀感卻很差；DSH 則直接跑了 20 分鐘。作者認為，DSH 驅動下模型的長程任務能力明顯更強，社群回饋中也有使用者反映曾連續跑了 10 個小時。作者自己測試的第一人稱射擊遊戲 demo 同樣只給了一句提示，蹲下、換彈、瞄準、NPC 等功能都是模型自行完成。文章也建議不必先讓 AI 寫一份詳細 Prompt，直接語音講清需求即可，過度詳細的指令反而會限制模型發揮。

介面下方還有一張即時的 Token 消耗統計表，可檢視 Token 用量與快取命中率，內測期間快取命中率大多落在 99% 左右，也曾出現過幾次降到 60 到 70% 的情況。

💡 醉翁之意：普通使用者也能參與模型的自進化

文章認為，DeepSeek 這套外掛化架構，是目前看到比較能落地的「自進化」路線圖之一：在 Cordis 協議下，模型可以在不打斷任務的前提下自己寫外掛、自己裝上，再配合使用者生態，理論上能從大量 Agent 實例中篩出優質外掛回饋主線。不過文章也坦言，就目前而言，Cordis 對一般使用者的體驗提升還不明顯，這是一個需要生態與時間累積的功能，短期內主要對開發者與極客使用者有吸引力。

⚠️ 尚未打磨的地方

DSH 目前沒有 Electron 桌面應用，只能透過瀏覽器 Web UI 使用；經典 Agent 三欄佈局中的右側欄尚未做出來，不像 Codex 內建瀏覽器、檔案管理、預覽甚至能在對話中播放影片。V4 模型本身不具備視覺能力，圖片附件功能需要額外搭配多模態模型才能使用。此外，DeepSeek API 即將於 8 月 17 日調漲價格，尤其是快取部分，這會直接影響長時間跑 Agent 任務的成本。

🎯 實務啟示

如果你是喜歡動手改造工具鏈的工程師，DSH 的價值不在於模型能力本身多強，而在於它把整個 Agent 執行時開放成可拆解的積木。想客製上下文管理策略、換掉某個工具實作，或替特定場景寫專屬預設，都可以直接動手，這是目前多數封閉 Harness 做不到的自由度。

🔗 來源
- 標題：深度體驗DeepSeek Harness，我原諒它漲價了
- 作者／機構：Jay（量子位）
- 連結：https://www.qbitai.com/2026/08/472208.html

#DeepSeek #AIAgent #OpenSource #CodingAgent #LLM #DeveloperTools #AgentFramework #VibeCoding #PluginArchitecture #AIEngineering
