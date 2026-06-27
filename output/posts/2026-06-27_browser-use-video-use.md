---
title: browser-use/video-use
source: GitHub Trending
url: https://github.com/browser-use/video-use
score: 95
model: google/gemma-4-31b-it:free
generated_at: '2026-06-27T19:31:20.265081'
---

📌 **【browser-use】用 Claude Code 聊天就能剪片：開源專案 video-use 登場**

TL;DR：透過 Claude Code 與 shell 許可權，將原始素材轉化為成品影片的 100% 開源剪輯工具。

剪輯影片通常意味著面對複雜的選單與繁瑣的時間軸操作，但如果能像對話一樣地告訴 AI「去掉贅字」或「加上字幕」，剪輯流程會變得如何？

🧩 **以對話驅動的自動化剪輯流程**

video-use 讓使用者只需將原始素材放入資料夾，並透過與 Claude Code 聊天，即可獲得最終的 final.mp4 檔案。該專案不依賴預設設定或選單，適用於訪談、教學、旅遊影片或口播內容（talking heads）等各種場景。

💡 **核心功能：從粗剪到後期處理的自動化**

- **精準去冗餘**：自動刪除 filler words（如 umm, uh）以及拍攝片段之間的空白時間。
- **自動調色與音訊最佳化**：支援暖色電影感、中性強烈感或自定義的 ffmpeg 連結進行調色；並在每個剪接點加入 30ms 音訊淡入淡出，避免爆音（pop）。
- **自定義字幕與動畫**：預設將字幕以每組 2 個大寫單詞的形式燒錄進影片，且樣式可調。
- **並行生成動畫疊加**：透過啟動多個子代理（sub-agents），並行呼叫 HyperFrames、Remotion、Manim 或 PIL 來生成動畫效果。
- **自我評估機制**：在向使用者展示結果前，系統會在每個剪接邊界對渲染輸出進行自我評估。
- **狀態持久化**：將對話記憶記錄在 project.md 中，讓使用者在之後的對話 session 中能接續之前的進度。

🛠️ **快速上手與整合方式**

使用者可將設定指令貼入 Claude Code、Codex、Hermes、Openclaw 或任何具有 shell 許可權的 Agent 中：`Set up https://github.com/browser-use/video-use for me.`

安裝過程需遵循以下步驟：
1. 閱讀 `install.md` 進行安裝。
2. 配置 ffmpeg 並將該技能（skill）註冊至所使用的 Agent。
3. 設定 ElevenLabs API key。
4. 參考 `SKILL.md` 瞭解日常用法，並檢視 `helpers/` 資料夾中的剪輯指令碼。
5. 安裝完成後無需手動轉錄，直接通知 Agent 並將素材放入資料夾即可。

🎯 **實務啟示**

對於開發者或內容創作者而言，這代表一種「程式碼即剪輯」的新範式。透過將 ffmpeg 等強大工具封裝在 LLM 的 shell 許可權之下，剪輯從「手動操作介面」轉向「意圖驅動的自動化」。對於需要大量產出短片或簡單教學影片的工程師，這能大幅降低重複性的粗剪時間。

🔗 **來源**
- 標題：browser-use/video-use
- 作者／機構：browser-use
- 連結：https://github.com/browser-use/video-use

#AI #VideoEditing #OpenSource #ClaudeCode #ffmpeg #Automation #LLM #VideoProduction #AgenticWorkflow #browseruse
