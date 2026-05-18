---
title: "VideoSeeker: Incentivizing Instance-level Video Understanding via Native Agentic Tool Invocation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.16079
score: 99
model: tencent/hy3-preview:free
generated_at: 2026-05-18T20:40:35.292439
---

📌 【USTC & Xiaohongshu 最新研究】VideoSeeker：用視覺提示讓 AI 主動「找」影片中的物體  

你以現在的 LVLM 已經能精準指出影片裡的每個物體？事實上，在需要細膩時空定位的任務上，它們仍常依賴模糊的文字描述，導致使用體驗不佳。  

🤔 **當 LVLM 遇到「找東西」的挑戰**  
現有的大型視覺語言模式在影片理解上表現不錯，但當任務要求精準的時空定位（例如指出某個特定人物在哪幀出現、手部動作的具體位置）時，純文字提示難以提供足夠的空間與時間線索。此外，許多方法把視覺感知與語言推理分離，推理過程以語言為中心，限制了模型主動去捕捉細粒度視覺證據的能力。  

🧪 **四階段自動合成資料管線與工具呼喚訓練**  
研究團隊提出 VideoSeeker，將「視覺提示」納入代理式（agentic）工具呼喚的框架。他們設計了一個全自動的四階段資料合成管線，用來大規模產出高品質的 instance‑level 影片資料。透過 cold‑start 監督學習與強化學習（RL），模型內化了工具呼喚與主動感知的能力，使其能在需要時主動檢索相關影片片段。  

📈 **在細粒度影片理解上平均提升 13.7%**  
實驗顯示，VideoSeeker 在 instance‑level 影片理解任務上相較於現有基線平均提升 **+13.7%**。這個提升不僅超過了 GPT‑4o 與 Gemini‑2.5‑Pro 等強大的閉源模型，也在較一般的影片理解基準上展現了良好的遷移效果。  

💡 **視覺提示與工具呼喚的結合如何改變感知‑推理流程**  
與傳統依賴文字提示的方式不同，VideoSeeker 讓模型先透過視覺線索定位目標，再呼叫工具進行後續的推理或擷取。這種「先看後問」的流程使模型能更直接地利用影片的空間時間資訊，減少對語言描述的依賴，從而在精準定位任務上獲得顯著改善。  

⚠️ **僅報告平均提升，具體任務分布與長期穩定性未詳述**  
論文目前提供了平均改善幅度，但未列出各子任務的具體數據分布，亦未探討模型在長時間序列或較複雜互動場景中的穩定性。這些細節留待後續工作進一步說明。  

🎯 **開放資料與代碼將促進 agentic 多模態研究**  
作者表明相關資料集與程式碼將公開釋放。這對於研究 agentic 行為與 multimodal 理解的工程師而言，提供了可直接建置與實驗的基礎，也有助於社群探索視覺提示在更廣泛的視訊理解應用中的可能性。  

🔗 **論文連結**  
📝 VideoSeeker: Incentivizing Instance-level Video Understanding via Native Agentic Tool Invocation  
👤 Yiming Zhao, Yu Zeng, Wenxuan Huang, Zhen Fang, Qing Miao  
🏫 University of Science and Technology of China; Xiaohongshu Inc.; East China Normal University; Xi’an Jiaotong University  
🔗 https://arxiv.org/abs/2605.16079  

你會如何利用「視覺提示」讓 AI 在影片中更精準地定位目標？歡迎在留言區分享你的想法 👇  

#AI #VideoUnderstanding #AgenticAI #Multimodal #USTC #Xiaohongshu #CVPR #VideoSeeker
