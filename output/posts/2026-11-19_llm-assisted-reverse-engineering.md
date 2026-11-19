---
title: LLM assisted reverse engineering
source: Hacker News
url: https://www.slowchronicle.com/posts/llm-assisted-reverse-engineering
model: claude-code/sonnet
generated_at: '2026-11-19T23:47:23.208020'
score: 93
---

📌 二十年老鳥的逆向工程，如何被 AI agent 徹底加速

TL;DR：一位資深 RE 玩家分享用 LLM agent 搭配 Ghidra、假設驅動除錯等技巧，把過去要花數年的硬體破解壓縮到半年內完成。

逆向工程向來是體力活：盯著組合語言、跟著 xref 一路爬，一個功能搞懂往往要耗上數週。這篇 Hacker News 熱文的作者，用二十年的逆向經驗加上 2026 年的 AI agent，描述了他現在的實際工作流程。

🤔 **這套方法是為誰而做**

作者是硬體與軟體駭客，玩逆向工程已有二十年，過去全靠手動分析。現在的目標是把這份「出於好奇心」的愛好，用 AI agent 大幅加速，而不是取代思考——他特別強調自己的經驗仍然用於「引導」agent 走對方向。

🧩 **工具鏈與核心工作流程**

他常用的工具組合：
- **DeepSeek Harness + Deepseek v4.1 Flash** 作主力 AI，偶爾搭配 Codex（Luna 或 Terra），理由是 Deepseek 效能好、速度快又便宜。
- **Ghidra + MCP bridge**：市場上最好的免費反組譯／反編譯工具，透過 MCP bridge 讓 agent 能直接操作。
- **radare2 / kuna**：CLI 反組譯／反編譯工具，不如 Ghidra 精細，但速度快，對 AI 來說可能更好用。

實際流程大致是：

1. 先判斷二進位檔的類型、平臺、建置方式，據此選適合的反編譯工具（作者指出目前的 AI 光看純組合語言，像 x86 或 ARM 指令，也能處理得不錯）。
2. 要求 agent 把所有發現持續寫進 Markdown 筆記。這同時是給自己看的紀錄、避免 agent context 被壓縮或交接給新 agent 後迷路，也讓 agent 本身思路更清楚。
3. 讓 agent 分析基本結構：主要函式、主要分支、匯入函式等。
4. 遇到單靠反組譯/反編譯解不開的部分，可以：
   - 讓 agent 對二進位檔下中斷點做除錯；
   - 啟用或注入 logging 探針記錄行為；
   - 給 agent 外部存取權，例如桌面應用的 computer use，或可透過 API 控制的韌體模擬器；
   - 換個切入角度（例如從跟 xref 改成跟字串）；
   - 親自讀過 agent 的完整對話與思考過程，判斷它是否走進死路並給出建議——作者認為這一步特別需要經驗。

💡 **三把關鍵技能：追問、工具說明、假設驅動除錯**

作者公開了幾個他常用的 agent skill：
- **grill-me**（Matt Pocock）：在輸入有價值時讓 agent 一次只問一個問題，最多問到五題，確保資訊到位。
- **ghidra-decompile-skill**（作者自製）：附帶 22 個 Ghidra 腳本，用於快速、針對性的反編譯，也修正了 GhidraMCP 擴充功能與 Ghidra 版本不匹配的問題。
- **hypothesis-debugging**（作者自製）：強制卡住的 agent 走「提出假設 → 寫入磁碟上的 CSV 假設表 → 設計能明確證實或推翻假設的實驗（探針、logging 等）→ 記錄結果 → 重複」的科學方法循環，避免 agent 無止盡亂猜、原地繞圈。

實作層面，作者偏好兩種工具：用 UV 搭配 Python 快速建環境、寫單檔內嵌依賴的腳本做原型與探針；真正要做的 hack 則盡量用 Rust，理由是語言優雅，加上編譯器嚴格,能立刻給 agent 明確的回饋迴圈。

📊 **半年內達成的成果清單**

作者列出近六個月的戰果：完整逆向並破解 AlphaSmart NEO 打字裝置；完整映射 EmWave 生物反饋裝置與兩臺 Sony Alpha 無反相機的通訊協定，並據此做出自訂的桌面／行動應用，甚至把 A7III 相機改造成無線網路攝影機；為 Arturia MiniFreak、Teenage Engineering OP-Z、Akai MPC Sample 開發自訂韌體；為 Xteink X4 電子書閱讀器做自訂韌體；修好一臺舊款 HP 印表機在 macOS 上失效的驅動程式；破解大量青年時期的授權鎖定棄置軟體；開發輕量版 Evernote 客戶端；以及自製了一套類 Photoshop 編輯器。

⚠️ **這條路仍需要經驗把關**

作者坦言，雖然現在的 LLM 很聰明，但有時仍會陷入狹隘的思路，需要有經驗的人讀過完整對話紀錄,判斷 agent 是否走偏並給出修正方向——這部分仍是作者自身技能，不是純粹丟給 agent 就能解決。

🎯 **實務啟示**

如果你也在做逆向工程或底層系統分析，這篇分享的三個可直接複用的做法是：把發現持續寫成 Markdown 筆記以防 context 流失、用假設驅動的 CSV 循環逼 agent 做可驗證實驗而非亂猜、以及針對自己的工具鏈（Ghidra/radare2）寫專用 skill，避免 agent 因不熟工具而過早放棄。

🔗 **來源**
- 標題：LLM assisted reverse engineering
- 作者／機構：ioma8
- 連結：https://www.slowchronicle.com/posts/llm-assisted-reverse-engineering

#ReverseEngineering #LLMAgents #Ghidra #AIAssistedHacking #HypothesisDriven #Rust #FirmwareHacking #AgentSkills #DeepSeek #HackerNews
