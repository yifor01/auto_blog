---
title: "Show HN: I built a sub-500ms latency voice agent from scratch"
source: Hacker News
url: https://www.ntik.me/posts/voice-agent
score: 117
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-03T19:59:35.432814
---

📌 【400ms 語音代理】從零開始打造實時對話，關鍵在於 TTFT 和地理位置

如果你曾經被 AI 語音助手的「思維停頓」困擾，這篇絕對值得一看。一位開發者從零開始打造語音代理，實現了平均 400ms 的端到端延遲——這意味著從你說完話到對方回應的第一個音節，只花了不到半秒。

🤔 **語音對話的本質是轉換，不是轉錄**

開發者發現，語音對話不是轉錄問題，而是轉換問題。傳統的 VAD (Voice Activity Detection) 單獨使用會失敗，你需要語義上的對話結束檢測。整個系統歸結為一個迴圈：說話 vs 聆聽。兩個關鍵轉換——立即取消干擾、立即回應對話結束——定義了使用者體驗。

🧪 **核心技術決策**

- **串流處理是唯一選擇**：STT → LLM → TTS 必須串流，串列處理根本無法實現自然對話
- **TTFT 為王**：在語音領域，第一個 token 就是關鍵路徑
- **地理位置比提示更重要**：將所有元件放在同一地區，否則在開始之前就輸了

💡 **最關鍵的勝利因素**

Groq 的 ~80ms TTFT 是單一最大的勝利。開發者強調，地理位置比提示更重要——如果你的元件沒有共置，你會在開始之前就輸了。

🎯 **實作細節**

- 完整的 STT → LLM → TTS 迴圈
- 乾淨的干擾處理
- 無預先計算的回應
- 平均 ~400ms 端到端延遲 (電話停止 → 第一音節)

🔗 **論文連結**
📝 Show HN: I built a sub-500ms latency voice agent from scratch
👤 Nick Tikhonov
🔗 GitHub Repo: github.com/NickTikhonov/shuo
🔗 部落格文章：ntik.me/posts/voice-agent

這是個具體的工程突破，解決了語音代理的關鍵瓶頸，並提供了可複製的實踐經驗。對 AI 工程師極具價值。

#AI #VoiceAgent #Engineering #Latency #TTFT #Groq #VoiceAI
