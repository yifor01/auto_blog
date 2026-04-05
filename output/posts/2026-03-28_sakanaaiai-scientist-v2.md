---
title: "SakanaAI/AI-Scientist-v2"
source: GitHub Trending
url: https://github.com/SakanaAI/AI-Scientist-v2
score: 127
model: gpt-4o-free
generated_at: 2026-04-05T19:44:41.099044
---

📌 【SakanaAI 最新開源】AI 自主寫出首篇過審論文

你以為 AI 寫論文只是套用固定模板？SakanaAI 最新釋出的 AI-Scientist-v2 徹底移除人類範本依賴，改以「漸進式智能樹狀搜尋」自主提出假說、執行實驗、分析數據並撰寫手稿。它已成為史上首篇完全由 AI 生成、並通過同儕審查的 ICLR Workshop 論文。但這項突破的代價與邊界，可能跟你想的不一樣。

🤔 **從「依樣畫葫蘆」走向開放式科學探索**

過往的自動化科研系統多依賴人類預先定義的框架與範本，這在目標明確的任務中效率極高，卻也限制了 AI 的發散能力。SakanaAI 推出 v2 的核心動機，正是為了打破模板限制，讓系統能跨越多個機器學習領域，真正進行開放式的科學探索。這反映了 AI Agent 發展的重要分水嶺：從「高效執行既定流程」轉向「自主發掘未知知識」。

🧪 **引入實驗管理員與漸進式智能樹狀搜尋**

v2 的架構核心在於 `progressive agentic tree search`。系統不再線性執行指令，而是由 `experiment manager agent` 擔任引導者，動態展開假說分支、評估初步結果、修剪無效路徑，並逐步深化有潛力的研究線索。整個流程覆蓋從文獻理解、程式碼生成、實驗執行到論文撰寫的端到端 (end-to-end) 閉環，實現了高度自主的科研工作流。

📊 **首篇 AI 全自動生成論文通過同儕審查**

該系統已成功產出首篇完全由 AI 撰寫的 Workshop 級別論文，並通過 ICLR 2025 Workshop 的同儕審查。這不僅驗證了 Agentic Tree Search 在學術發表層級的可行性，也證明 AI 已具備將零散研究步驟串聯為完整科學論述的系統性能力。

💡 **探索性強，但成功率與產出穩定性未必優於 v1**

官方明確指出其中的工程 Trade-off：v1 因緊扣人類撰寫的優質範本，成功率高且產出穩定；v2 採開放探索策略，成功率較低，且論文品質不一定優於 v1。v2 的設計哲學並非「取代成熟模板」，而是解決那些缺乏明確起點、需要 AI 自行摸索方向與假設的開放式問題。在科研實務中，這兩者應被視為互補的工具鏈，而非迭代取代關係。

⚠️ **執行 LLM 自寫程式碼的資安風險與不可控性**

開放自主性伴隨實質風險。官方強烈警告，該程式碼庫會直接執行由 LLM 生成的程式碼。這可能引入危險的第三方套件、觸發未經控管的網路存取，或造成系統層級的不可預期行為。在缺乏嚴格沙箱隔離與權限控管的情況下，直接部署於生產環境或連接內部網路將帶來顯著的資安與穩定性隱患。

🎯 **明確任務用 v1，開放探索試 v2，沙箱環境是底線**

實務部署建議依研究階段分流：若目標明確、需快速驗證已知假說，v1 的模板化流程仍是高性價比選擇；若處於早期腦發散、需 AI 協助探索未知 ML 子領域或交叉學科，可嘗試 v2 的樹狀搜尋架構。無論選擇哪一版本，執行 LLM 生成程式碼時務必強制使用隔離沙箱、嚴格限制套件安裝權限與網路存取，並建立人工覆核機制，確保研究過程的可追溯與安全性。

🔗 **專案連結**
📝 The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search
👤 SakanaAI
🔗 GitHub：https://github.com/SakanaAI/AI-Scientist-v2
📂 實驗背景：ICLR 2025 Workshop

你認為 AI 自主科研下一步該優先突破「成功率」還是「安全性」？歡迎在留言區分享你的觀察與實戰經驗 👇

#AI #AgenticAI #MachineLearning #ScientificDiscovery #SakanaAI #ICLR2025 #OpenSource #AIResearch #自動化科研
