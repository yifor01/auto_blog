---
title: "SynAE: A Framework for Measuring the Quality of Synthetic Data for Tool-Calling Agent Evaluations"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.22564
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:22:38.420584
---

📌 【CMU & Microsoft Research】SynAE：評估工具調用 Agent 合成資料品質的多軸框架  

真實的工具調用 Agent 執行追蹤資料常因敏感、 proprietary 或過於稀疏而無法直接用於測試，團隊遂轉而使用合成資料來補足或取代真實基準——然而，我們缺乏系統化的方式來量測這些合成資料與真實資料的相似程度。  

🤔 **當真實資料不足時，合成資料真的能可靠地模擬 Agent 行為嗎？**  

🧪 **四個維度的量測框架**  
SynAE 從四個層面評估合成資料的品質：(i) 任務說明與中間回應，（ii）工具調用，（iii）最終輸出，（iv）下游評估表現。每個層面都針對「有效性（validity）」、「忠實度（fidelity）」與「多樣性（diversity）」進行量化，使評估不再依賴單一指標。  

🔍 **基於近期 Agent 基準的驗證與失敗模式測試**  
研究團隊使用最近公開的 Agent 基準來計算 SynAE 各項分數，並透過可控的合成資料生成方案故意引入已知的品質問題（例如工具調用錯誤、回覆偏離任務等），觀察框架是否能捕捉到這些細微的偏差。結果顯示，不同失敗模式在不同維度上會產生獨特的分數變化，證實單一指標無法全面反映合成資料的優劣。  

💡 **多軸評估才能揭示合成資料的真實品質**  
SynAE 的核心洞察是：有效性、忠實度與多樣性三者各自捕捉資料品質的不同面向，只有同時考慮它們才能避免誤判。例如，一份資料可能在工具調用上非常忠實，但任務說明的多樣性不足；僅看忠實度會過高評價其品質，而加入多樣性指標後則會顯露不足之處。  

⚠️ **目前僅提供框架與示範，長期適用性仍待觀察**  
本工作提出了評估方法並開放了原始碼與線上 Demo，但尚未針對不同領域的 Agent（例如多模態或長 horizon 任務）進行廣泛驗證，亦未探討合成資料在訓練階段而非僅評估階段的影響。  

🎯 **工程師可直接採用，持續監控多個品質面向**  
- 將 SynAE 整合到現有的 Agent 測試管線，產出 validity、fidelity、diversity 三組分數。  
- 當任何一項分數顯著下落時，檢查對應的生成程式或資料來源，避免單一指標誤導決策。  
- 開源程式碼：https://github.com/wsqwsq/SynAE  
- 線上 Demo：https://synae-2026-synae-demo.static.hf.space/index.html  

🔗 **論文連結**  
📝 SynAE: A Framework for Measuring the Quality of Synthetic Data for Tool-Calling Agent Evaluations  
👤 Shuaiqi Wang, Aadyaa Maddi, Zinan Lin, Giulia Fanti (Carnegie Mellon University; Microsoft Research)  
🔗 arXiv：https://arxiv.org/abs/2605.22564  

你目前在評估工具調用 Agent 時，是否也在使用合成資料？歡迎在留言區分享你的經驗或對 SynAE 的看法 👇  

#AI #AgentEvaluation #SyntheticData #CMU #MicrosoftResearch #SynAE #機器學習 #測試框架 #資料中心AI
