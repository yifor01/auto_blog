---
title: "Apple Silicon costs more than OpenRouter"
source: Hacker News
url: https://www.williamangel.net/blog/2026/05/17/offline-llm-energy-use.html
score: 77
model: tencent/hy3-preview:free
generated_at: 2026-05-17T19:40:35.724614
---

📌 **Apple Silicon 運行 LLM 成本竟高於 OpenRouter？實測數據揭秘**  

你以為在筆電上跑大型語言模型只要「電費便宜」就划算？實際算下硬體折舊，成本可能遠超你的預期。  

🤔 **本地運行 vs 雲端 API：成本到底誰更勝？**  
隨著 M5 系列 MacBook Pro 的發布，許多開發者開始嘗試在本地執行離線 Agentic 編程助手。但電力只是其中一小塊，硬體的折舊與使用壽命才是主導成本的關鍵。  

🧪 **實測環境與假設**  
- 設備：14 英寸 MBP，M5 Max + 64 GB RAM，售價 $4,299（Apple 官網）  
- 負載功耗：約 50–100 W（滿載推理）  
- 電價：以 $0.20/kWh 計算（約 $0.02/小時電費）  
- 折舊假設：依據 3、5、10 年使用壽命，分別得到年均成本 $1,433、$860、$430，對應小時折舊成本約 $0.164、$0.098、$0.049。  
- 作者認為 5 年是一般使用的合理估計，故取每小時折舊約 $0.098。  

📊 **核心發現：電力+折舊約 $0.12/小時，相當於 ~$1.50/百萬 token**  
- 每小時總成本 ≈ 電費 $0.02 + 折舊 $0.098 ≈ $0.12  
- 在約 50–100 token/秒的推理速度下，這相當於每百萬 token 大約 $1.50 的 amortized 成本。  
- 相同效能的模型在 OpenRouter 上的價格僅為此的 **1/3**，且速度約 **2 倍**。  

💡 **深入分析：折舊才是成本主因**  
電力在整體成本中所佔比例不到 20%，即使把功耗提升到滿載 100 W，每小時也只多花不到 $0.02。相反，硬體的折舊（特別是設備壽命縮短時）會直接把每小時成本提升到 $0.16 以上，使本地解方在純成本上失去競爭力。  

⚠️ **研究限制：基於單一機型與簡化假設**  
- 僅以 M5 Max 64 GB 為例，不同記憶體配置或其他晶片（M5 Pro、M5 Ultra）功耗與售價會不同。  
- 功耗取 50–100 W 的區間平均，實際推理負載可能波動。  
- 未考慮冷啟動、熱節流、網路延遲（雖為離線）以及可能的維護或升級成本。  
- 折舊採用直線法，未計入二手價值或提前淘汰的情況。  

🎯 **實務啟示：依需求選擇本地或雲端**  
- 若首要目標是**最低運算成本與最高吞吐**，OpenRouter 等雲端 API 目前在同等模型下更具經濟性。  
- 若重視**資料隱私、離線環境或對延遲極端敏感**，則需在採購時將硬體折舊納入總體成本模型，並考慮實際使用壽命（是否會因升級需求而提前淘汰）。  
- 在預算有限的情況下，可先以較低階的 MacBook Air 或 M5 Pro 測試，觀察實際功耗與熱情況，再決策是否升級至 Max 版。  

🔗 **部落格原文**  
📝 *Offline Agentic Coding part 3: Apple Silicon costs more than OpenRouter*  
👤 作者：datadrivenangel（Hacker News）  
🔗 https://www.williamangel.net/blog/2026/05/17/offline-llm-energy-use.html  

你目前在本地還是雲端跑 LLM？歡迎在留言區分享你的成本觀察與使用經驗 👇  

#AI #LLM #AppleSilicon #MacBookPro #OpenRouter #成本效益 #離線運算 #HackerNews #科技分享
