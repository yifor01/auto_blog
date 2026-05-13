---
title: "Covering Human Action Space for Computer Use: Data Synthesis and Benchmark"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.12501
score: 121
model: tencent/hy3-preview:free
generated_at: 2026-05-13T20:23:14.576533
---

📌 **CUActSpot：覆蓋人類操作空間的電腦使用基準**  

你以為 AI 已經能流暢操作桌面，卻發現它在複雜、低頻的點擊、拖曳、繪圖上總是失誤？問題可能不在模型大小，而在於訓練資料的稀疏。

🤔 **複雜操作才是 AI 失誤的主因**  
針對 GPT‑5.4、Claude 等先進電腦使用代理（CUA）的失敗案例，研究發現 GUI 操作呈現長尾分布：少量複雜且多樣的互動佔據了絕多數任務失敗。這說明資料不足是導致低頻、高難度操作不可靠的關鍵因素。

🧪 **CUActSpot 基準測試與合成資料管線**  
為評估模型在複雜互動上的表現，團隊提出 **CUActSpot** 基準，覆蓋五種模態（GUI、文字、表格、畫布、自然圖像）以及多種動作（點擊、拖曳、繪製等），遠超過以往以點擊為主的測試。  
資料採用 **renderer‑based 合成管線**：為每種模態自動生成場景，擷取螢幕截圖與元素座標，再由 LLM 產生匹配的指令與動作軌跡，構成訓練語料。

📊 **Phi‑Ground‑Any‑4B 在開源模型中脫穎而出**  
在上述合成語料上訓練後，**Phi‑Ground‑Any‑4B**（參數量 4B）在 CUActSpot 上的表現優於所有參數量低於 32B 的開源模型，證明針對性的合成資料能顯著提升複雜互動能力。

💡 **資料稀疏導致長尾失誤，合成資料可彌補**  
研究指出，失誤的根源在於真實世界中複雜互動樣本稀少，導致模型在長尾區域缺乏經驗。透過渲染器生成多樣場景並讓 LLM 標註指令，可以人為補充這些缺失的資料點，從而提升模型在低頻、高難度操作上的穩定性。

⚠️ **基準僅涵蓋五種模態、合成資料依賴 LLM，真實世界差距未知**  
目前 CUActSpot 仍限於 GUI、文字、表格、畫布、自然圖像五種模態；合成資料的品質取決於底層 LLM 的理解能力；尚未在真實桌面環境中進行長期驗證，實際落地效果仍需進一步觀察。

🎯 **工程師可直接使用開源基準與模型評估與改進電腦使用代理**  
論文將基準、合成資料、訓練代碼與 Phi‑Ground‑Any‑4B 模型開源於 **https://github.com/microsoft/Phi-Ground.git**，建議從事 UI 自動化或代理開發的團隊：  
- 使用 CUActSpot 評估自身模型在複雜互動上的弱點；  
- 採用類似的 renderer‑based 合成管線擴充訓練資料；  
- 在低頻、高風險操作前先進行基準測試，以提升系統可信度。

🔗 **論文連結**  
📝 Covering Human Action Space for Computer Use: Data Synthesis and Benchmark  
👤 Miaosen Zhang, Xiaohan Zhao, Zhihong Tan, Zhou Huoshen, Yijia Fan (Southeast University; MBZUAI; Wuhan University; Sun Yat‑sen University; Microsoft)  
🔗 論文：https://arxiv.org/abs/2605.12501  
💻 程式碼與模型：https://github.com/microsoft/Phi-Ground.git  

你在使用 AI 輔助桌面操作時，是否曾遇過「簡單任務做得到，複雜操作總出錯」的情況？歡迎在留言區分享你的經驗與改進想法 👇  

#AI #ComputerUseAgent #CUActSpot #PhiGround #MultimodalBenchmark #DataSynthesis #MicrosoftResearch #UIAutomation #機器學習 #深度學習
