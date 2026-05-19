---
title: "Advancing Narrative Long Video Generation via Training-Free Identity-Aware Memory"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.18733
score: 117
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:30:42.812904
---

📌 【浙江大學 與騰訊優圖實驗室】身份記憶提升長影片生成

你以為更長的影片代表更好的故事？但當 AI 需要跨越多個場景時，角色竟會開始「分身」與「失憶」。

🤔 **長影片生成的致命傷：身份漂移與記憶衰減**  
自回歸式影片生成在視覺保真度與互動性上已有長足進步，但在長時間序列中仍會出現記憶衰減。現有做法要麼透過預設策略壓縮歷史幀，要麼依賴粗糙的隱式注意訊號抽取關鍵幀，這兩種方式都無法應對提示中實體參照的變化，導致身份漂移、角色重複與屬性遺失。

🧪 **LLM 抽取實體 + VLM 驗證的記憶框架**  
我們提出 IAMFlow，一個免訓練的身份感知記憶框架。首先，大型語言模型 (LLM) 從每個提示中抽取出具視覺屬性的實體，並為其分配唯一的全域 ID 以建立身份感知記憶。其次，視覺語言模型 (VLM) 非同步地驗證並細化渲染幀中的屬性，實現顯式的實體追蹤，取代原先的隱式相似度匹配。為保持計算實用性，我們設計了一套推理加速管線，包含非同步視覺驗證、自適應提示過渡與模型量化，使生成速度比現有基線更快。

🔬 **核心發現：無需訓練就贏過最強基線 2.56 分，同時快 1.39 倍**  
我們進一步提出 NarraStream‑Bench，一個專門用於敘事流式影片生成的基準，包含 324 條多提示腳本，橫跨六個維度，並採用三維評估協議（傳統指標 + 多模態大型語言模型評估）。廣泛實驗顯示，即便是免訓練的 IAMFlow，在 NarraStream‑Bench 上仍能取得最佳整體表現，比最強基線高出 2.56 分；在 60 秒多提示設置下，比最高效基線快 1.39 倍。

💡 **深入分析：顯式身份追蹤 vs. 隱式相似度匹配**  
研究團隊指出，關鍵差異在於 IAMFlow 透過 LLM 與 VLM 的協同，將身份資訊顯式地儲存與更新，而非依賴框架內部的隱式相似度。這使得在提示轉換時，實體的視覺屬性能被正確保留，減少了身份漂移與屬性遺失的發生。

⚠️ **研究限制：僅在合成基準上驗證，長期真實場景尚未測試**  
目前的評價皆基於 NarraStream‑Bench 這個合成基準，尚未在真實長片段或使用者生成內容上進行長期驗證。此外，雖然框架是免訓練的，但仍需 LLM 與 VLM 的推理資源，在極端資源受限環境下可能需要顧慮。

🎯 **實務啟示：訓練免費即插即用，適合長片段敘事生成**  
對於需要連貫敘事的長影片生成應用（如電影預告、教學影片或互動故事），IAMFlow 提供了一種無需額外訓練即可插入既有生成管線的解決方案。開發者可直接利用現有的 LLM 與 VLM 模組，透過非同步驗證與量化加速，獲得更一致的角色與更快的生成速度。

🔗 **論文連結**  
📝 Advancing Narrative Long Video Generation via Training-Free Identity-Aware Memory  
👤 Jinzhuo Liu, Jiangning Zhang, Wencan Jiang, Yabiao Wang, Dingkang Liang  
🔗 https://arxiv.org/abs/2605.18733  

你在長影片生成中遇到過身份不一致的問題嗎？歡迎在留言區分享你的經驗與看法 👇  

#AI #VideoGeneration #Multimodal #LLM #VLM #浙江大學 #騰訊優圖 #NarraStreamBench #長影片 #身份追蹤
