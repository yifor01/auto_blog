---
title: "ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.12481
score: 123
model: tencent/hy3-preview:free
generated_at: 2026-05-13T20:22:18.627209
---

📌 **ToolCUA：最佳 GUI‑Tool 路徑規劃**  

你以為讓 AI 直接點擊畫面就能完成所有操作？實際上，它在決定何時繼續點擊、何時呼叫工具時，常常走錯路，導致效率大打折扣。  

🤔 **混合動作空間讓代理陷入決策困境**  
現有的 Computer Use Agents 既能執行點擊、輸入等原始 GUI 動作，也能調用 API 型工具進行檔案操作。然而，因為缺乏高質量的交錯 GUI‑軌跡、真實工具軌跡成本高且易碎，以及缺少軌跡層級的路徑選擇監督，代理常難以判斷何時該切換到工具，結果產生次序不佳的執行路徑。  

🧪 **分階段訓練管線：從靜態軌跡到線上強化學習**  
研究團隊先提出「交錯 GUI‑Tool 軌跡擴管線」，利用豐富的靜態 GUI 軌跡並合成一個可接地的工具庫，無需人工設計或收集真實工具軌跡即可產出多樣化的交錯軌跡。接著進行「Tool‑Bootstrapped GUI RFT」，結合暖身 SFT 與單輪 RL，強化在關鍵切換點的決策。最後在高保真 GUI‑Tool 環境中以「線上 Agentic RL」優化 ToolCUA，並以「Tool‑Efficient Path 獎勵」引導代理盡量使用工具並縮短執行路徑。  

🚀 **OSWorld‑MCP 上準確率提升約 66%，達 46.85%**  
實驗顯示，ToolCUA 在 OSWorld‑MCP 基準上達到 46.85% 的準確率，相較於基線模型提升約 66%（相對改進）。與僅使用 GUI 動作的設定相比，ToolCUA 進一步提升 3.9%，證明其在混合動作空間中能有效選擇適當的工具與 GUI 操作的組合。  

💡 **訓練範式決定了代理的工具使用品質**  
分階段的訓練讓模型先從靜態軌跡學習基礎 GUI 行為，再透過單輪 RL 強化關鍵切換點的判斷，最後在線上環境中以路徑效率為目標微調。這種「先建立基礎、再強化決策、最後優化路徑」的流程，使得代理不僅學會何時使用工具，也學會如何透過工具縮短整體執行步驟。  

⚠️ **實驗主要聚焦於單一基準與短期表現**  
目前結果僅在 OSWorld‑MCP 上報告，未涵蓋更多樣化的桌面或網頁環境；評估側重於單次任務的成功率，長期穩定性與泛化能力仍需後續工作驗證。  

🎯 **實務上可將分階段訓練視為構建真實數位代理的參考方案**  
對於需要同時處理點擊輸入與 API 呼應的場景（例如桌面自動化、跨應用工作流），可先利用現有的靜態 GUI 資料合成工具庫，再以暖身 SFT + 單輪 RL 強化關鍵決策，最後在真實或高保真模擬環境中以路徑效率為目標進行線上 RL 優化。這樣的管線有助於減少對真實工具軌跡的依賴，同時提升代理在混合動作空間中的路徑選擇品質。  

🔗 **論文連結**  
📝 ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents  
👤 Xuhao Hu, Xi Zhang, Haiyang Xu, Kyle Qiao, Jingyi Yang (Tongyi Lab, Alibaba Group; Fudan University; Shanghai Artificial Intelligence Laboratory)  
🔗 arXiv：https://arxiv.org/abs/2605.12481  
💻 開源實作：https://x-plug.github.io/ToolCUA/  

你在構建 AI 代理時，是否也曾困惑於何時該切換到工具？歡迎在留言區分享你的經驗與想法 👇  

#AI #ComputerUseAgent #GUITool #Alibaba #Fudan #OpenSource #RL #AgenticAI
