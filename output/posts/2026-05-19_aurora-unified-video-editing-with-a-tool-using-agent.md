---
title: "Aurora: Unified Video Editing with a Tool-Using Agent"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.18748
score: 116
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:32:13.478816
---

📌 【UofR/MIT-IBM/NVIDIA 最新研究】Aurora：工具增強 VLM Agent 統一視訊編輯  

你是否曾經對 AI 說「把天空換成夕陽」，但卻忘了提供參考圖或精確位置？研究顯示，這種未指定的需求是目前視訊編輯模型的主要失敗點。  

🤔 **使用者常未提供模型就緒的條件**  
現有的統一視訊編輯模型（單一 Diffusion Transformer）能同時處理文字、來源視訊與參考圖像，但它假設使用者已經給出「模型就緒」的文字、參考圖以及空間定位。真實的使用請求常常缺少這些資訊，導致生成結果不符合預期。  

🧪 **Agentic 框架 + 監督學習與偏好配對**  
Aurora 由兩部分組成：  
1. 一個工具增強的視覺‑語言模型（VLM）Agent，負責把原始使用者請求映射為符合 Transformer 條件通道的結構化編輯計畫（包括文字、參考圖選取與空間定位）。  
2. 一個統一的視訊 Diffusion Transformer，負責根據 Agent 的計畫進行實際生成。  

訓練過程包含：  
- 使用監督資料學習完整的編輯規劃與參考圖選取。  
- 透過偏好配對（preference pairs）強化工具使用與指令細練的穩健性。  

為評估在文字與視覺未指定情況下的表現，研究團隊建立了 **AgentEdit-Bench**，並在此基準上以及兩個現有的視訊編輯基準上進行實驗。  

🚀 **Aurora 在未指定請求上顯著優於純指令基線**  
實驗結果顯示：  
- 在 AgentEdit-Bench 與兩個現有基準上，Aurora 的編輯品質均優於僅依賴文字指令的基線模型。  
- 訓練好的 VLM Agent 能直接轉移（transfer）到其他凍結（frozen）的視訊編輯模型上，保持同樣的改進幅度。  
這意味著，即使不重新訓練龐大的 Diffusion Transformer，只要 plug-in 一個工具增強的 VLM Agent，即可顯著提升模型對未指定使用者請求的處理能力。  

💡 **工具增強的規劃是解決未指定問題的關鍵**  
實驗進一步顯示，Agent 的「規劃」階段（將文字請求轉換為結構化的條件輸入）是提升性能的主要來源。當 Agent 能正確選取參考圖與給出空間定位時，後續的 Diffusion Transformer 才能在正確的條件下生成符合意圖的視訊。工具使用（例如呼叫圖像檢索或遮罩生成）則使這個規劃過程更具穩健性，減少因模糊請求導致的失敗率。  

⚠️ **評估範圍有限、依賴監督資料**  
作者指出，目前的實驗僅限於構建的 AgentEdit-Bench 與兩個現有基準，尚未進行大規模真實使用者研究；此外，工具增強的 VLM 需要監督資料與偏好配對來訓練，這可能在未見過的編輯類型或領域上的泛化能力仍需進一步驗證。  

🎯 **實務上可直接 plug-in 現有凍結模型**  
對於工程師來說，Aurora 提供了一種低成本的途徑：  
- 不需要重新訓練龐大的視訊 Diffusion Transformer。  
- 只需訓練或取得一個工具增強的 VLM Agent，即可將其接入任何支援統一條件的視訊編輯模型。  
這樣的設計讓系統在面對不完整或模糊的使用者請求時，仍能先進行合理的規劃再進行生成，提升實用互動體驗。  

🔗 **論文連結**  
📝 Aurora: Unified Video Editing with a Tool-Using Agent  
👤 Yongsheng Yu, Ziyun Zeng, Zhiyuan Xiao, Zhenghong Zhou, Hang Hua (UofR; MIT-IBM; NVIDIA)  
🔗 論文：https://arxiv.org/abs/2605.18748  
🌐 Project page：https://yeates.github.io/Aurora-Page  

你認為在視訊編輯中，AI 應該先「理解」再「執行」，還是直接接受模糊指令讓模型自行發揮？歡迎在留言區分享你的看法 👇  

#AI #VideoEditing #AgenticAI #VLM #DiffusionTransformer #UofR #MITIBM #NVIDIA #Aurora #AgentEditBench #GenAI
