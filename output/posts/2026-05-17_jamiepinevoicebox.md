---
title: "jamiepine/voicebox"
source: GitHub Trending
url: https://github.com/jamiepine/voicebox
score: 107
model: tencent/hy3-preview:free
generated_at: 2026-05-17T19:28:22.010815
---

📌 【jamiepine/voicebox】本地開源語音工作室，替代 ElevenLabs 與 WisprFlow  

想要在本機完成聲音克隆、語音合成、全域熱鍵聽寫，且資料不離開電腦？這個專案把七種 TTS 引擎與語音克隆整合成一個桌面應用。  

🤔 **本地優先的語音 I/O 堆疊**  
現有的商業聲音服務通常將輸入（如 WisprFlow）與輸出（如 ElevenLabs）分離於不同雲端平台。Voicebox 的設計目標是同時提供輸入與輸出功能，並將所有模型、聲音資料與捕獲內容完全保留在使用者本機，達成完整的隱私保護。  

🧪 **整合七種 TTS 引擎與語音克隆功能**  
Voicebox 捆綁了以下開源 TTS 引擎：Qwen3‑TTS、Qwen CustomVoice、LuxTTS、Chatterbox Multilingual、Chatterbox Turbo、HumeAI TADA 以及 Kokoro。同時支援：  
- 零樣本聲音克隆（僅需數秒參考音訊）  
- 50+ 預設聲音（來自 Kokoro 與 Qwen CustomVoice）  
- 23 種語言合成（從英語、阿拉伯文、日文、希伯來文、斯瓦希里文等）  
- 全域熱鍵聽寫，可直接輸入至任何文字欄位  
- 為 MCP‑aware AI agent 指定專屬聲音（透過內建本地 LLM 進行後處理與人格切換）  

💬 **核心功能：零樣本聲音克隆、多語言合成、全域熱鍵聽寫、MCP‑aware Agent 語音**  
- **語音合成**：透過上述任意引擎產生語音，可調整音高、混響、延遲、合聲、壓濾等後處理效果。  
- **表達式語音**：Chatterbox Turbo 支援 paralinguistic 標記，例如 [laugh]、[sigh]、[gasp]，讓合成語音更具自然感。  
- **聽寫**：全域熱鍵啟動後，語音輸入會即時轉寫至焦點文字欄位，適合筆記或程式碼註解。  
- **本地 LLM 細化**：內建的小型語言模型用於聲音後處理與人格（ persona ）切換，使同一聲音可根據情境產生不同風格的輸出。  

💡 **隱私與本地運行的設計考量**  
因為所有模型與資料均在使用者機器上執行，Voicebox 避免了將聲音樣本或合成結果上傳至第三方伺服器。這對於需要符合資料保護規範（如 GDPR、HIPAA）或 simplesmente 不希望聲音指紋外洩的使用者而言，是一個重要的設計優勢。  

⚠️ **目前仍依賴社群維護、文件與除錯資源有限**  
專案為開源個人維倉庫，文件與範例主要集中在安裝與基本使用；進階除錯、效能調校或跨平台打包（如 macOS、Windows、Linux）的說明較為簡略，可能需要自行閱讀原始碼或參考 Issues 區。  

🎯 **適合希望自建語音管線、關注資料隱私的開發者**  
如果您正在構建語音代理、輔助工具或需要在本機完成語音輸入／輸出的應用，Voicebox 提供了一個可直接下載、零設定即可使用的全功能聲音工作室。透過其內建的熱鍵聽寫與多引擎切換，可快速驗證不同 TTS 模型的聲音特性，同時不必擔心聲音資料外洩。  

🔗 **專案連結**  
📂 jamiepine/voicebox  
🔗 https://github.com/jamiepine/voicebox  

您是否已經在本機試過聲音克隆或熱鍵聽寫？歡迎在留言區分享您的使用體驗或改進建議 👇  

#AI #Voicebox #TTS #VoiceCloning #OpenSource #PrivacyFirst #GitHubTrending #jamiepine #語音合成 #聽寫 #MCP #開源工具
