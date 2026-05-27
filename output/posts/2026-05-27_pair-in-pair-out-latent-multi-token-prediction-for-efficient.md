---
title: "Pair-In, Pair-Out: Latent Multi-Token Prediction for Efficient LLMs"
source: arXiv
url: http://arxiv.org/abs/2605.27255v1
score: 104
model: tencent/hy3-preview:free
generated_at: 2026-05-27T20:56:14.538644
---

📌 **PIPO：雙端統一提升效率**  

你以為只能壓縮輸入或預測多個 token 來加速 LLM？這篇論文把輸入端的潛在壓縮與輸出端的多標記預測鏡像統一，卻省去了傳統 speculative decoding 必要的驗證器開銷。  

🤔 **輸入與輸出的獨立工作亟需統一**  
現有加速思路要麼專注於輸入側的 latent compression（把多個 token 壓成一個隱藏狀態），要麼專注於輸出側的 speculative decoding / multi‑token prediction（MTP），但兩者多被分開研究。輸出側方法還必須額外跑一次驗證器（verifier）來確認 MTP 生成的草稿 token 是否可靠，這額外的計算成為瓶頸。  

🧪 **將壓縮與展開視為鏡像操作**  
作者提出 **Pair‑In, Pair‑Out (PIPO)**：  
- 輸入端的 latent compressor 視為「摺疊」：把兩個輸入 token 折疊成一個 latent 表示。  
- 輸出端的 MTP head 視為「展開」：把一個隱藏狀態展開為一個額外的輸出 token。  
這兩個過程在數據流上是鏡像的，因此可以共享參數或結構。  

為了在不犧牲可靠性的前提下去除驗證器，PIPO 再加輕量的 **confidence head**，用來決定草稿 token 是否應該被接受。有趣的是，**On‑Policy Distillation (OPD)** 天生符合 speculative decoding 的拒絕取樣標準，所以 confidence head 可以直接在 OPD 訓練過程中同步學習，額外成本可忽略不計。  

📈 **實驗顯示顯著吞吐提升**  
在 Qwen3.5‑4B 與 9B 兩種 backbone 上，分別在 AIME 2025、GPQA‑Diamond、LiveCodeBench v6、LongBench v2 四個基準進行測試：  
- 相較於標準自回歸解碼，PIPO 使 **pass@4** 提升最高達 **+7.15 分**。  
- 首 token 延遲（first‑token‑latency）最高可達 **2.64×** 加速。  
- 每 token 延遲（per‑token‑latency）最高可達 **2.07×** 加速。  

💡 **鏡像設計如何免除驗證器成本**  
因為 compressor 與 MTP head 在數學上是互逆的操作，模型內部已經隱含了對輸入與輸出的一致性約束。當 confidence head 判斷草稿 token 可信時，這個一致性約束已經在前向傳播中被滿足，因而不需要額外的 verifier pass 來重新檢查。同時，將 confidence head 與 OPD 結合訓練，使其學會直接模擬 speculative decoding 的接受/拒絕決策，從而在推理階段實現「零額外開銷」的接受判斷。  

⚠️ **僅在特定模型與基準上驗證**  
目前結果僅基於 Qwen3.5‑4B/9B 在上述四個基準上的表現。不同架構、更大規模模型或更長鏈式思考任務的適用性仍需後續工作進一步探討。  

🎯 **實務啟示：可直接插入現有推理管線**  
對於需要低延遲的 LLM 服務（例如程式碼生成、數學推理或長文摘要），PIPO 提供一種無需額外驗證器即可提升吞吐的端到端方案。實作時，只需在原本的 transformer block 中加入輸入端的 latent compressor、輸出端的 MTP head 與 confidence head，並透過已有的 OPD 訓練流程同步更新 confidence head，即可獲得上述速度提升。  

🔗 **論文連結**  
📝 *Pair-In, Pair-Out: Latent Multi-Token Prediction for Efficient LLMs*  
👤 Wenhui Tan, Minghao Li, Xiaoqian Ma, Siqi Fan, Xiusheng Huang  
🔗 https://arxiv.org/abs/2605.27255v1  

你目前的 LLM 推理管線是否已經在嘗試類似的雙端優化？歡迎在留言區分享你的經驗或疑問！  

#AI #LLM #SpeculativeDecoding #MultiTokenPrediction #PIPO #Qwen3 #推理加速 #機器學習 #arXiv #技術深度
