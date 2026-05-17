---
title: "yichuan-w/LEANN"
source: GitHub Trending
url: https://github.com/yichuan-w/LEANN
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-05-17T19:25:55.779221
---

📌 **LEANN：全球最小向量索引，筆記型電腦也能做私密 RAG**  

想在本機跑出億級文件的語意搜尋，又不想犧牲隱私或付雲端費用？LEANN 可能是答案。  

🤔 **為什麼需要私人向量資料庫？**  
傳統向量索引龐大且常伴隨遙測收集，使用者在筆電上建立個人知識庫時，儲存空間與隱私成為主要瓶頂。  

🧪 **如何實現？圖形基礎選擇性重新計算 + 高度保留修剪**  
LEANN 採用 graph‑based selective recomputation 與 high‑degree preserving pruning 技術，只在需要時即時計算嵌入向量，而非預先儲存全部向量。這樣的設計同時實現了零遙測與極低的磁碟佔用。  

🚀 **核心聲稱：97% 儲存減少、準確度不損**  
根據專案說明，LEANN 能在不降低檢索準確率的前提下，將傳統方案的儲存需求減少約 97%。它支援將檔案系統、郵件、瀏覽紀錄、聊天記錄（WeChat、iMessage）、即時資料（Slack、Twitter）、程式碼庫以及外部知識庫（例如 6000 萬份文件）全部納入同一個向量索引，全部在本機運作，零雲端成本。  

💡 **與 Claude Code 無縫整合**  
LEANN 提供一個 drop‑in 的 semantic search MCP 服務，完全相容於 Claude Code。開發者無需改變現有工作流程，即可獲得智慧式檢索能力，讓 Claude Code 在本機也能進行語意搜尋。  

⚠️ **目前已知的限制**  
- 實作以開源 Python 專案形式提供，社群正在成長中（GitHub 今日星標約 186）。  
- 尚未公開長期穩定性或大規模基準測試報告。  
- 所有功能依賴於本機的運算資源，極大規模索引仍需足夠的記憶體與 CPU/GPU。  

🎯 **給開發者的實務建議**  
若你希望在筆電上打造私人 AI 助手，且重視資料不離開本機與零遙測，可直接嘗試 LEANN 作為向量後端；特別是搭配 Claude Code 使用時，可即時獲得語意搜尋功能，無需額外設定或改變既有開發流程。  

🔗 **專案連結**  
📂 GitHub：https://github.com/yichuan-w/LEANN  

你有在本機構建 RAG 系統的經驗嗎？歡迎在留言區分享你的使用心得或問題 👇  

#AI #RAG #VectorDatabase #PrivacyFirst #OpenSource #ClaudeCode #LEANN #GitHubTrending
