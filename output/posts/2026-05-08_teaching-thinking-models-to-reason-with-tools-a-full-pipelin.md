---
title: "Teaching Thinking Models to Reason with Tools: A Full-Pipeline Recipe for Tool-Integrated Reasoning"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.06326
score: 125
model: tencent/hy3-preview:free
generated_at: 2026-05-08T19:50:00.784164
---

📌 **思考模型工具推理流程**  
【多校聯手】Zhejiang University、Shanghai AI Laboratory、Peking University、CUHK、Tsinghua、USTC、Shanghai Jiao Tong University  

你以為讓模型學會用工具一定會讓推理更強？研究卻發現，即使模型幾乎不真的呼叫工具，僅僅啟用工具評估也可能讓純文字推理變差。這篇論文提出一套完整流程，如何在不犧牲「不用工具」思考能力的前提下，自然地把工具使用行為注入強大的思考模型。

🤔 **工具評估反而傷害純文字推理**  
作者首先觀察到一個悖論：在啟用工具的評估環境下，即使思考模型幾乎不實際調用工具，其在純文字推理任務上的表現也會下降。這說明單純讓模型看到工具的存在，就可能干擾其原有的推理路徑，因而需要特別的訓練策略來避免這種「認知干擾」。

🧪 **四個關鍵訓練設計點**  
論文將解決方案分為四個可執行的階段，並指出每個階段的設計原則：  

1. **師生軌跡的可學習性** – 監督微調 (SFT) 必須使用那些本質上需要工具才能高效解決的問題作為師生示範，這樣模型才能學到真正有用的工具行為。  
2. **工具軌跡比例控制** – 通过調整訓練資料中工具使用軌跡的比例，可以減輕對純文字推理能力的災難性遺忘。  
3. **以 pass@k 與回覆長度為目標優化** – 不傳統地直接最小化訓練損失，而是優化通過率 (pass@k) 和生成回覆的長度，這樣既能獲得 SFT 的最大收益，又為後續的強化學習保留探索空間。  
4. **穩定的可驗證獎勵強化學習 (RLVR)** – 在合適的 SFT 初始化基礎上，加入明確防止模式崩塌的機制，使用可驗證的獎訊號進行穩定的 RL 訓練，最終得到既能使用工具又不失純文字推理的模型。

🔑 **在 Qwen3 上的實證結果**  
將上述食譜分別套用在 Qwen3‑4B 與 Qwen3‑30B 思考模型上，作者在多個基準測試中觀察到顯著提升。特別是在 AIME 2025 上，4B 模型達到 96.7%，30B 模型達到 99.2%，在同等規模的開源模型中屬於州際領先水準。這些結果表明，該流程成功地讓模型學會在需要時呼叫工具，同時保留了其在無工具情況下的強大推理能力。

💡 **工具使用的兩種互動模式**  
進一步分析顯示，模型在訓練後表現出兩種典型的工具互動方式：  
- **建立理解型**：先讓工具產生中間結果，再針對結果提出追問或自行驗證，最終內化理解。  
- **取代思考型**：過度依賴工具直接給出答案，少量自行推理。  
前者往往對應更高的基準分數，後者則可能導致工具成為「依賴」而非「輔助」。

⚠️ **研究限制**  
- 本研究主要聚焦於數學推理基準（如 AIME），其他領域的工具整合效果尚需進一步驗證。  
- 實驗使用的工具集合與真實世界的工具鏈可能有差異，遷移性有待觀察。  
- 雖然提出了防止模式崩塌的保護機制，但長期訓練穩定性仍需更大規模的實驗確認。

🎯 **給工程師的實務建議**  
- 在準備用於工具整合的監督資料時，優先選擇「必須用工具才能高效解決」的問題，以提升師生軌跡的可學習性。  
- 調整工具軌跡在訓練混合中的比例，可在不犧牲純文字推尋能力的前提下獲得工具使用的提升。  
- 優化目標可考慮 pass@k 與生成長度，而非單純的損失下降，這樣能為後續的強化學習階段保留探索餘地。  
- 若採用強化學習階段，請確保獎勵可驗證，並加入適當的多樣性正則化以防止模型過早收斂於單一工具使用模式。

🔗 **論文連結**  
📝 Teaching Thinking Models to Reason with Tools: A Full-Pipeline Recipe for Tool-Integrated Reasoning  
👤 Qianjia Cheng, Yuchen Zhang, Zhilin Wang, Yuxin Zuo, Shunkai Zhang et al.  
🔗 https://arxiv.org/abs/2605.06326  

你在使用 AI 輔助工具時，是傾向「先讓工具給答案再驗證」还是「自己先思考、工具只作為檢查」？歡迎在留言區分享你的經驗與觀察 👇  

#AI #ToolUse #Reasoning #Qwen3 #ReinforcementLearning #LLM #Agent #ZhejiangUniversity #ShanghaiAILab #PekingUniversity #CUHK #Tsinghua #USTC #SJTU #AIME2025 #OpenSource #MachineLearning
