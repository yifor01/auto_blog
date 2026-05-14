---
title: "OpenBMB/VoxCPM"
source: GitHub Trending
url: https://github.com/OpenBMB/VoxCPM
score: 107
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:48:57.638833
---

📌 【OpenBMB】VoxCPM2：免 Token 的多語言 TTS  

你想要一個不需要斷詞、直接說出任何語音的 AI 嗎？VoxCPM2 宣稱只要給文字，就能產出 30 種語言、48kHz 高保真聲音，而且還能只憑描述設計全新聲音。這真的可能嗎？  

🤔 **當下 TTS 仍受離散符號限制**  
多數文字轉語音系統依賴聲學標記（如 phoneme、BPE token）進行中間表示。這種離散化過程雖簡化建模，但往往導致聲音失去細膩的韻律與情感，尤其在跨語言或風格控制上顯得力不從心。  

🧪 **端到端擴散自回歸架構，內建 MiniCPM‑4**  
VoxCPM2 採用 tokenizer‑free 設計：文字直接透過一個端到端的 diffusion‑autoregressive 網路產生連續的語音表示。模型骨幹為 MiniCPM‑4，在超過 200 小時的多語言語音資料上訓練，參數規模達 2B。無需額外的語言標籤，即可處理 30 種支援語言的輸入。  

🎯 **核心能力：多語言合成、聲音設計與可控克隆**  
- **30‑語言多語言**：輸入任意支援語言的文字，直接合成對應語音。  
- **Voice Design**：僅憑自然語言描述（性別、年齡、語氣、情緒、語速等）生成全新聲音，無需參考音檔。  
- **Controllable Cloning**：提供短段參考音訊，可在保留原始 timbre 的同時，透過風格引導調整情緒、語速與表達。  
- **Ultimate Cloning**：同時給出參考音訊及其逐字稿，模型能無縫延伸參考內容，忠實保留 timbre、節奏、情感與風格。  
- **48kHz 高品質**：接受 16kHz 參考輸入，直接輸出 48kHz studio‑level 音訊。  

💡 **為何免 Token 能帶來更自然的表達**  
透過擴散模型在連續空間中逐步精細化語音波形，模型不再受離散詞彙表的限制，能更好捕捉微細的音高變化、氣流聲與情感脈衝。自回歸的生成方式則保留了時間依賴性，使合成結果在長語句上仍具連貫性。這兩者結合，是 VoxCPM2 能在多語言與風格控制上同時表現的關鍵。  

⚠️ **目前已知的限制**  
- 模型體積龐大（2B 參數），推播需較高的運算資源。  
- 公開資訊僅限於 GitHub 儲存庫與簡介，尚未見正式論文或基準測試報告。  
- 訓練資料規模雖已說明，但具體語言分佈、資料來源與清洗過程未詳述。  
- 未提供對比實驗（如與傳統 token‑based TTS 的 MOS、RTF 等指標），因此實際優勢幅度需待社群驗證。  

🎯 **開發者可據此構建的應用**  
- 多語言客服或虛擬助理，無需為每種語言維護別的聲學模型。  
- 互動式故事或遊戲中，即時依據劇情描述生成角色專屬聲音。  
- 聲音品牌化：僅憑品牌語氣描述，快速打造專屬合成聲音。  
- 聲音後製工具：提供參考片段即可進行風格可控的聲音克隆與再創作。  

🔗 **資源連結**  
📂 GitHub：https://github.com/OpenBMB/VoxCPM  
🧩 開源代碼與模型權重皆在該倉庫中提供，歡迎閱讀 README 以取得最新使用說明。  

你是否已嘗試過 VoxCPM2 進行跨語言聲音合成？或是對其聲音設計功能有什麼想法？歡迎在留言區分享你的實驗經驗與觀察 👇  

#OpenBMB #VoxCPM #TextToSpeech #DiffusionModel #MultilingualTTS #VoiceCloning #VoiceDesign #AI音訊 #GitHubTrending #GenAI
