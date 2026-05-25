---
title: "Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.23163
score: 136
model: tencent/hy3-preview:free
generated_at: 2026-05-25T20:18:41.406367
---

📌 Fast-dDrive：區塊擴散VLA讓自動駕駛更快更準  

你以為擴散模型只能慢？Fast-dDrive 證明它也能在車端實現比自回歸快 12 倍的吞吐量，同時還保有最高的規劃精度。  

🤔 **自動駕駛需要同時兼顧軌跡精度與推理速度**  
端到端的 Vision‑Language‑Action (VLA) 模型必須在高保真軌跡規劃與邊緣硬體的推理效率之間取得平衡。現有的自回歸 VLAs 常受記憶體頻寬限制且容易產生曝露偏移；而完整序列擴散模型則無法重複使用 KV‑cache，並會出現「邏輯洩漏」違背感知‑然後‑規劃的因果順序。  

🧪 **區塊擴散結構化 scaffold 與安全優先訓練**  
Fast-dDrive 採用區塊擴散的設計：在語義單元內部進行雙向細節修飾，同時在單元之間嚴格保持因果順序。利用駕駛 VLAs 傾向輸出結構化的 JSON‑like 內容，研究團隊將結構性標記凍結為 section scaffold，並以 section‑aware 的訓練策略優先學習安全關鍵的規劃決策。  

🚀 **在 WOD‑E2E 與 nuScenes 上達到 SOTA 並將 L2 錯誤降低 22%**  
實驗顯示，Fast-dDrive 在 WOD‑E2E 測試集上取得 SOTA 的 ADE@3s 與 ADE@5s，並擁有最高的 RFS（擴散型 VLA 中最佳）。在 nuScenes 上，平均 L2 誤差降至 0.32 m，相較於先前基線提升 22%。  

💡 **雙向細節修飾與因果約束讓規劃更可靠**  
透過在區塊內部進行雙向細節優化，模型能在保持局部連貫性的同時，跨區塊的因果約束防止了規劃步驟提前使用未來資訊，從而減少因「邏輯洩漏」導致的不合理軌跡。  

⚠️ **實驗主要聚焦單幀預測，長時序行為尚未驗證**  
目前的評估集中在單幀或短窗口的軌跡預測，長時間窗口的行為一致性與累積誤差尚未在實車路況中進行充分驗證。  

🎯 **結合 SGLang 可在邊緣設備達到 12× 提升，適合即時部署**  
當 Fast-dDrive 與 SGLang 推理引擎結合時，吞吐量較自回歸基線提升 12 倍，這意味著在具備相同硬體的車載平台上，可在不犧牲規劃精度的前提下達到即時決策所需的效率。  

🔗 **論文連結**  
📝 Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving  
👤 Kewei Zhang, Jin Wang, Sensen Gao, Chengyue Wu, Yulong Cao (Peking University; NVIDIA; The University of Hong Kong; MIT)  
🔗 https://arxiv.org/abs/2605.23163  

如果你正在研究 VLA‑based 自動駕駛或尋找可在邊緣運行的高效擴散方案，這篇工作提供了一個值得參考的實作路線。歡迎在留言區分享你的看法或實驗經驗！  

#AI #AutonomousDriving #VLA #DiffusionModel #NVIDIA #PekingUniversity #MIT #HKU #SGLang #Fast-dDrive
