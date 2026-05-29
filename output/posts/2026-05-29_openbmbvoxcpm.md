---
title: "OpenBMB/VoxCPM"
source: GitHub Trending
url: https://github.com/OpenBMB/VoxCPM
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-05-29T20:57:11.225813
---

📌 OpenBMB 發布 VoxCPM2：Tokenizer‑Free 多語言 TTS  

你是否曾想過，不用任何語音標記，直接從文字生成 30 種語言、48kHz 高保真語音？這個新模型卻用了一種完全不同的方式……  

🤔 **多語言語音合成仍受離散標記限制**  
現有的文字轉語音系統多依賴離散語音標記（token），這在跨語言、風格控制以及高保真輸出時會帶來資訊損失與合成 artefact。開發者常需要額外的語言標籤或參考音訊才能達到多語言或聲音設計的效果。  

🧪 **端到端擴散自回歸架構，直接建模連續語音表示**  
VoxCPM2 採用 tokenizer‑free 的設計，透過擴散與自回歸的結合，直接從文字產出連續的語音表示。模型基於 MiniCPM-4 骨幹，參數規模達 2B，訓練資料超過 200 小時多語言語音（超過 2M 小時），支援 30 種語言輸入，無需額外語言標籤。  

🎯 **聲音設計、可控克隆與終極克隆皆可實現**  
- **Voice Design**：僅憑自然語言描述（性別、年齡、語氣、情緒、語速）即可生成全新聲音，無需參考音訊。  
- **Controllable Cloning**：提供短片段參考音訊，可在保留原始音色的同時，透過風格引導調整情緒、語速與表達。  
- **Ultimate Cloning**：同時給出參考音訊及其文字稿，模型能無縫接續參考內容，忠實保留音色、節奏、情緒與風格。  
- **高保真輸出**：接受 16kHz 參考音訊，直接產出 48kHz studio‑level 音訊。  

💡 **去標記化帶來的表達自由與資源需求**  
因為模型不依賴離散標記，它能更細緻地捕捉語音的連續變化，這使得多語言合成、聲音風格控制與高保真複製變得更自然。然而，這種端到端的擴散自回歸架構通常需要較大的計算資源（尤其是在推理階段），且目前尚未公開詳細的消融實驗或與其他 TTS 模型的基準比較，使得效能上的絕對優勢仍需社群進一步驗證。  

🎯 **適用於多語言應用、互動式聲音創作與個性化語音助理**  
- 開發者可直接呼叫模型產出 30 種語言的語音，適合全球化產品本地化。  
- 透過文字描述即可設計品牌專屬聲音，減少對錄製室與配音演員的依賴。  
- 在客服、虛擬角色或遊戲中，可即時克隆使用者聲音並依情境調整表達。  
- 由於模型已在 GitHub 開源（https://github.com/OpenBMB/VoxCPM），團隊可自行在 MiniCPM-4 基礎上進行微調或部署到自有硬體。  

🔗 **項目連結**  
📂 VoxCPM2: Tokenizer‑Free TTS for Multilingual Speech Generation, Creative Voice Design, and True-to-Life Cloning  
👤 OpenBMB  
🔗 https://github.com/OpenBMB/VoxCPM  

你有試過用文字描述來設計聲音嗎？歡迎在留言區分享你的想法或使用經驗 👇  

#OpenBMB #VoxCPM #TextToSpeech #MultilingualTTS #VoiceCloning #VoiceDesign #GenerativeAI #GitHubTrending #AI音訊 #語音合成
