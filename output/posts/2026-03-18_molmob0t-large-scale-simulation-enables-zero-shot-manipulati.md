---
title: "MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2603.16861
score: 110
model: gpt-4o-free
generated_at: 2026-03-18T21:27:37.491845
---

📌 MolmoB0T: 大規模模擬讓機器人零樣本操作成為可能

你是否曾想過，機器人能否在未見過真實物體的情況下，直接抓取與操作？一篇最新研究顯示，只要在模擬世界裡喂給它夠多的合成資料，就能達到此目標。

🤔 **從模擬到真實的鴻溝，過去靠真實資料填補**

機器人操作長期受困於 sim-to-real 差距：在模擬中訓練好的政策，往往無法直接搬到真實機器人上，因而需要大量真實世界的微調與實機資料收集，這不僅耗時又昂貴。

🧪 **大規模合成資料 + Vision‑Language 模型 + Flow‑Matching 動作頭**

論文提出 MolmoB0T 框架：利用大規模模擬器產生海量合成影像與動作對，搭配預訓練的 vision‑language 模型理解語言指令，並採用 flow‑matching 動作頭直接輸出連續控制指令。整個訓練過程完全在合成資料上進行，無需任何真實世界微調。

 **零樣本 sim-to-real 轉移，成功率顯著**

在未見過真實物體的情況下，MolmoB0T 能夠直接將模擬中學得的政策搬到真實機器人上，實現高成功率的零樣本操作（具體數據請參考原論文）。這意味著，機器人可以在不收集額外真實資料的情況下，即時適用於新任務與新物體。

💡 **為何合成資料與 VLM 能跨越領域落差**

作者 hypothesise that 大規模多樣化的合成資料讓模型學會對視觉與語言的不變特徵，而 flow‑matching 動作頭則提供了平滑的動作分布，減少了對精確模擬參數的依賴。這種組合讓政策在語義層面上更具泛化能力，從而在真實世界中仍能保持穩定表現。

⚠️ **僅提供概念驗證，真實任務範圍與規模尚待探討**

摘要未詳細說明實驗涵蓋的任務種類、物體多樣性或長時程穩定性，亦未提及在較複雜、非結構化環境中的表現。因此，目前的結果主要作為概念驗證，尚需更廣泛的真實世界評估才能判斷其產業落地潛力。

🎯 **減少真實資料依賴，加速機器人部署**

若該方法能在更多場景下複製，將大幅降低機器人操作所需的真實資料收集成本，使得快速迭代與零樣本適應成為可能，對製造、物流及服務機器人等領域具備直接啟發價值。

🔗 **論文連結**
📝 MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation
🔗 https://huggingface.co/papers/2603.16861

你認為大規模合成資料是否能成為未來機器人學習的主流途徑？歡迎在留言區分享你的看法 👇

#AI #Robotics #Simulation #VisionLanguage #ZeroShot #HuggingFace #MolmoB0T
