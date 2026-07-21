---
title: browser-use/video-use
source: GitHub Trending
url: https://github.com/browser-use/video-use
score: 89
model: tencent/hy3:free
generated_at: '2026-07-21T08:31:54.109130'
---

📌 【開源專案】透過 Claude Code 進行影片剪輯：video-use 讓 AI 直接接管 ffmpeg

TL;DR：video-use 讓工程師能透過對話式 AI 直接下指令，自動完成影片剪輯、調色與字幕。

當影片剪輯從複雜的 UI 操作轉向自然語言指令，開發者的工作流程將會發生什麼變化？

🧩 **像聊天一樣進行影片後製**

video-use 是一個 100% 開源的工具，核心理念是讓開發者只需將原始素材丟入資料夾，並透過具備 Shell 存取許可權的 Agent（如 Claude Code、Codex 或 Hermes）進行對話，即可獲得最終的 `.mp4` 檔案。它不依賴預設引數或選單，而是針對各種內容（如教學、訪談、旅遊影片）提供高度靈活的編輯能力。

🛠️ **自動化剪輯的核心功能**

這套工具將繁瑣的後製步驟轉化為自動化流程：
- **精準剪輯**：自動切除冗餘的填充詞（如 umm、uh）、錯誤的開場以及鏡頭間的空白。
- **音訊處理**：在每個剪輯點自動加入 30ms 的音訊淡入淡出（audio fades），避免出現爆音（pop）。
- **自動調色**：針對每個片段進行自動色彩分級（可選擇電影感暖色調、中性強烈色調，或自定義 ffmpeg 指令）。
- **字幕生成**：預設以兩字大寫（UPPERCASE）塊狀字幕呈現，且風格完全可自訂。
- **動畫疊加**：透過 HyperFrames、Remotion、Manim 或 PIL 生成動畫疊加層，並由並行的子代理（sub-agents）負責處理。
- **自我評估**：在顯示結果前，會在每個剪輯邊界對渲染輸出進行自我評估。

💾 **具備專案記憶力的編輯流程**

與傳統剪輯軟體不同，video-use 會將 Session 記憶持久化儲存在 `project.md` 中。這意味著你下週繼續工作時，AI 能直接接續上次的進度。

🚀 **如何開始使用**

若要安裝並開始使用，你需要具備 Shell 存取許可權的 Agent，並按照以下步驟操作：
1. 依照 `install.md` 安裝儲存庫、配置 ffmpeg 並註冊 Skill。
2. 設定 ElevenLabs API key（若需要）。
3. 參考 `SKILL.md` 進行日常操作，並參考 `helpers/` 資料夾下的編輯指令碼。
4. 完成安裝後，只需告訴 AI「已準備就緒」，接著將素材丟入資料夾即可。

🎯 **實務啟示**

對於需要頻繁產出影片內容的工程師或內容創作者，video-use 提供了一種「以程式碼與指令為中心」的剪輯思維。透過將複雜的 ffmpeg 指令封裝進 AI Agent 的 Skill 中，開發者可以將精力從繁瑣的剪輯細節中解放出來，轉而專注於內容結構與創意。

🔗 **來源**
- 標題：browser-use/video-use
- 連結：https://github.com/browser-use/video-use

#AI #OpenSource #VideoEditing #ClaudeCode #FFmpeg #Automation #DeveloperTools #AIAGENTS #VideoProduction #MachineLearning
