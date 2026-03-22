---
title: "Omanic: Towards Step-wise Evaluation of Multi-hop Reasoning in Large Language Models"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2603.16654
score: 123
model: gpt-4o-free
generated_at: 2026-03-18T20:50:48.330798
---

📌 【Omanic】首個具中間步驟標註的 Multi-hop QA 基準，揭露 LLM 推理真實能力  

🎣 你以為模型答對最終問題就代表它真的會推理？研究顯示，僅看最終答案可能掩蓋關鍵失誤。  

🤔 **最終答案無法揭露推理過程**  
現有的多跳問答基準只提供最終答案，無法判斷模型是在正確推理還是僅憑運氣猜中。這使得診斷推理失誤的位置與原因變得極其困難。  

🧪 **Omanic：提供子問題與中間答案的結構化標註**  
研究團隊構建了 Omanic 資源，包含兩部分：  
- **OmanicSynth**：10,296 條機器生成的訓練樣本，具備分解的子問題與對應中間答案；  
- **OmanicBench**：967 條經專家審核的人工標註評估樣本。  這樣的逐步標註使得我們能追蹤模型在每一跳的事實完整性與錯誤傳播情況。  

 **SOTA 模型在 OmanicBench 上僅 73.11% 正確率**  在多選題設定下，現有最強大語言模型的平均正確率為 73.11%，顯示該基準具有較高難度。進一步的逐步分析發現：  
- 鏈式思考（CoT）的表現高度依賴於事實的完整性；  
- 當知識出現缺口時，CoT 的優勢會明顯減弱；  
- 錯誤在後續跳數中會被放大，導致最終答案偏差。  

💡 **在 OmanicSynth 上進行監督微調能帶來跨任務提升**  將 OmanicSynth 用於監督微調後，模型在六個推理與數學基準上的平均成績提升 7.41 點，證明該合成資料具備高品質的監督訊號，且能有效遷移推理能力。  

⚠️ **資料規模與標註層級的限制**  
- 訓練樣本為機器生成，可能遺留合成偏差；  
- 評估樣本數量為 967，雖經專家審核，但規模仍屬中等；  
- 目前僅提供靜態的子問題與中間答案，未涵蓋動態的推理路徑探索。  

🎯 **實務啟示：以過程導向評估與訓練**  
- 在開發或選擇推理模型時，應加入逐步正確度作為指標，而非僅依賴最終答案；  
- 利用類似 Omanic 的結構化資料進行監督微調，可有效提升模型的多跳推理與數學推演能力；  
- 設計 Agent 或鏈式思考時，需關注事項完整性與錯誤傳播的風險，考慮在中間步驟加入檢驗機制。  

🔗 **論文連結**  
📝 Omanic: Towards Step-wise Evaluation of Multi-hop Reasoning in Large Language Models  
👤 Xiaojie Gu, Sherry T. Tong, Aosong Feng, Sophia Simeng Han, Jinghui Lu (The University of Tokyo; Yale University; Stanford University; Xiaomi EV; Soongsil University)  
🔗 arXiv：https://arxiv.org/abs/2603.16654  
💾 數據集：https://huggingface.co/datasets/li-lab/Omanic  
💻 程式碼：https://github.com/XiaojieGu/Omanic  

你在評估 LLM 推理時，會關注中間步驟的正確度嗎？歡迎在留言區分享你的經驗與看法 👇  

#Omanic #MultiHopQA #LLMReasoning #AI評估 #監督微調 #推理能力 #XiaomiEV #大語言模型 #機器學習 #NLP #基準測試 #AI研究 #科技部落格
