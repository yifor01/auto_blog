---
title: 'Prospero: A new coding harness for a more civilized age'
source: Hacker News
url: https://nullprogram.com/blog/2026/10/31/
model: claude-code/sonnet
generated_at: '2026-10-31T20:37:26.593570'
score: 82
---

📌 Prospero：一個拒絕吃掉你記憶體的 Coding Harness

TL;DR：作者嫌現有 coding harness 太肥，自己用 C++ 寫了一個資源佔用少兩個數量級的替代品。

Coding harness 說穿了就是 curl 接上 `popen()`，照理不該吃掉好幾 GB 記憶體。可是這一年作者用過的多數 harness，偏偏都是用 web 技術堆出來的,動輒佔用驚人資源。於是他乾脆自己寫了一個：Prospero。

🤔 **先搞懂什麼是 coding harness**

對不熟悉的讀者,聊天介面是你和 AI 輪流傳訊息；coding harness 則把這個概念延伸，讓 AI 能「呼叫」harness 提供的工具，工具執行後把結果「回覆」給它,像讀寫檔案、跑 shell 指令。AI 會自主地從一次工具呼叫跳到下一次，不斷循環結果，這樣的 AI 就叫 agent。它偶爾會傳訊息跟你報告進度或提問,聊天介面始終都在。

🧩 **用 Dear ImGui 寫介面，資源少兩個數量級**

Prospero 以作者慣用的 C++ 風格寫成，搭配 Dear ImGui 的 docking 介面，功能不打折的前提下，資源用量比其他 harness 少了約兩個數量級。它本身不內建任何模型供應商,你得自己接上 llama.cpp、公司內部的 on-prem 模型、OpenRouter、Anthropic API 或 OpenAI API（不能直接用 Claude 訂閱）。

它支援讓 agent 衍生 subagent 來平行工作或保持自己的 context 乾淨,subagent 之間可以互相傳訊息、協調任務。只要有另一臺機器的 SSH 存取權，或透過 WSL，Prospero 就能把自己的 headless 版本部署過去，讓 agent 直接在那臺機器上操作。Professional Edition 內建 x86／x86-64 與 ARM64 在 macOS、Windows、Linux 上的組合引擎，其中 Windows x86 引擎甚至能跑在 Windows XP 上，照作者說法還能拿它玩接龍和踩地雷。

Prospero 也是少數具備桌面控制能力的 harness：只要模型支援 vision（作者認為值得用的模型都該支援），它就能「看見」你的桌面並操作,點擊、輸入、拖曳,即時測試與除錯 GUI 應用程式，不需要為每個 app 另外接 MCP。這也是不需要 TUI 的原因：harness 引擎本身跑在 headless 系統上，UI 則在你的桌機或筆電，稍加設定後 harness 甚至能在 UI 離線時獨立運作，之後再重新連回去。

⚙️ **設計理念：永不無限等待、不留孤兒行程**

作者把 fuzz 測試campaign當成代表案例：由於 Prospero 夠輕量，在跑 fuzz campaign 的 headless 機器上，Linux 的 OOM killer 不太會優先殺掉它,而是去殺真正吃爆記憶體的 fuzz target。過去他常常隔幾個小時回來檢查,卻發現 harness 行程已經不見了，campaign 根本沒在跑。讓 agent 跑 fuzz campaign 的理由很直接：它能邊跑邊修 bug，讓 campaign 繼續下去。

設定檔放在 `~/.config/prospero/prospero.ini`，純文字好編輯，不用 JSON，也能進版控、複製貼上。INI 檔可以 include 其他檔案，甚至用 URL include 以支援一份共用或集中管理的設定，但透過 URL include 的內容會被限制、硬性禁止設定任何可能出現在 shell 指令裡的項目,即便如此，設定仍可能把環境變數當成 API key、再指向自己控制的 endpoint 來間接外洩，所以還是需要一定信任基礎。

渲染上採用 passive rendering 而非像遊戲一樣逐 vsync 重繪，搭配 settle frame 讓動畫跑完後就閒置,agent 等 build 跑完的時候，Prospero 不會白白啃 GPU。核心原則是「永不無限等待」：每個操作都有 deadline，你若沒即時回應某個權限請求，agent 會因逾時被拒絕、只能想辦法繞過去，但 Prospero 會跳出系統 toast 提醒你。唯一的例外是 Plan 模式,agent 提出計畫或用 `ask_user` 詢問後會無限期等待，因為這時假定你正守在旁邊。Shell 指令逾時會被轉成非同步背景任務，agent 可以持續帶著 timeout 等待、定期被喚醒決定要不要繼續；agent 的 mailbox 也有上限。

另一個長年困擾作者的毛病是 agent 啟動的行程沒人收尾,平行 build 逾時、agent 以為殺掉了部分 build 系統，實際上 build 還在背景繼續跑，agent 再試一次，結果兩個 build 同時搶資源，把整臺機器拖垮。Prospero 的做法是把逾時的同步指令升級為非同步任務，再加上「整個行程樹一起生、一起死」的原則,指令被停止時是真的停止，這在 Windows 上很直接，在 macOS、Linux 上較麻煩，但 Prospero 仍實作到底。

⚠️ **上手前要知道的限制**

Prospero 不附任何模型供應商，一定要自己接 API 或自架推理服務；用 URL include 共用設定仍需要信任對方，因為環境變數仍有被間接讀出的風險；此外它主打的桌面控制與多架構 headless 部署等進階功能，屬於 Professional Edition。

🎯 **實務啟示**

如果你平常跑的是 local LLM 或自架推理服務，又受不了現有 harness 動輒吃掉數 GB 記憶體、或長時間任務跑到一半悄悄卡死，Prospero 的「永不等待、不留孤兒行程」設計值得參考,尤其適合拿來跑需要長時間無人值守、還要能自我修復的任務，像是 fuzz campaign。

🔗 **來源**
- 標題：Prospero: A new coding harness for a more civilized age
- 作者／機構：fovc（Hacker News）
- 連結：https://nullprogram.com/blog/2026/10/31/

#CodingAgent #LocalLLM #OpenWeightModels #DearImGui #Cpp #DevTools #AgentFramework #Fuzzing #LlamaCpp #AIEngineering
