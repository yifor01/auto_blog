---
title: "When Correct Isn't Usable: Improving Structured Output Reliability in Small Language Models"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.02363
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-05T19:56:54.011836
---

📌 **【Alomana 研究】數學算對卻無法上線？小模型 JSON 輸出的隱形陷阱**

你是否遇過這種情況：模型把數學題算對了，結果卻因為 JSON 格式少了個括號，導致整個 API 串接直接報錯？這不是模型的智力問題，而是「結構化輸出可靠性」的設計缺陷。

🤔 **任務正確率 85%，但輸出準確率卻是 0%**

在部署語言模型時，我們通常只關注答案是否正確（Task Accuracy）。然而，在實際生產環境中，輸出必須同時滿足「數學正確」且「格式合規」（如嚴格的 JSON 結構）。研究發現，當使用 NAIVE Prompting（無系統提示）時，7B-9B 的小模型在 GSM8K 數學測試中雖有高達 85% 的任務準確率，但因為輸出格式不符合規範，導致最終的「輸出準確率」（Output Accuracy）直接歸零。

🧪 **GSM8K 與 MATH 基準上的 5 種提示策略對決**

Alomana 團隊針對 7-9B 參數量的模型，在 GSM8K 和 MATH 兩大數學基準上進行了嚴格測試。實驗對比了五種提示策略，包含最基礎的 NAIVE、加入格式說明的 REFERENCE，以及技術門檻較高的約束解碼（Constrained Decoding）。

📉 **強制約束解碼讓推理延遲暴增 8 倍**

為了保證 JSON 格式正確，許多開發者會採用約束解碼（Constrained Decoding）。但數據顯示，這種方法雖然能強制語法正確，卻會帶來 3.6 倍到 8.2 倍的推理延遲（Latency），且在部分場景下反而會降低模型的任務表現。

 **AloLab：用黑箱 API 優化提示，輸出準確率飆升至 87%**

研究團隊提出了 **AloLab**，一個不需要微調模型的迭代式系統提示優化器。它的核心在於使用強大的元代理（Meta-agent，即 Claude Sonnet 4.5）來優化目標小模型的系統提示。結果顯示，AloLab 在 GSM8K 上達到了 84-87% 的輸出準確率，且推理延遲與最基礎的 NAIVE 模式幾乎相同。

💡 **就連 GPT-4o 也會犯的格式錯誤**

這個問題不只發生在小模型。實驗發現，在 GPT-4o 上，傳統的 REFERENCE 提示法會因為模型習慣性加上 Markdown 語法（如 ```json ... ```）而導致輸出準確率為 0%。相比之下，AloLab 在 GPT-4o 上達到了 95.2% 的準確率，證明了動態優化提示的有效性。

⚠️ **元代理能力是成敗關鍵，換成 Haiku 效果崩盤**

消融實驗（Ablation Study）指出，AloLab 的效果高度依賴元代理的能力。如果將強大的 Sonnet 4.5 替換為較弱的 Claude 3 Haiku，平均輸出準確率會從 84% 以上掉到 61%，且每次執行的標準差會從不到 1% 飆升至 21.8%，這意味著弱模型產生的優化策略極不穩定。

🎯 **部署小模型時，別再只盯著 Benchmark 分數看**

對於需要在邊緣設備或成本敏感的場景下部署 7B-9B 模型的團隊，這項研究提供了明確的解決方案：
1.  **停止依賴靜態格式提示**：手寫的 JSON 格式說明往往不夠精確。
2.  **避免高延遲的約束解碼**：除非延遲不是考量。
3.  **採用提示優化框架**：利用 AloLab 這類工具，透過黑箱 API 迭代出最佳系統提示，在保持低延遲的同時確保輸出可用性。

🔗 **論文連結**
📝 When Correct Isn't Usable: Improving Structured Output Reliability in Small Language Models
👤 Cosimo Galeone, Minsu Park, Giuseppe Ettorre, Daniele Ligorio @ Alomana
🔗 論文：https://arxiv.org/abs/2605.02363

你在部署 LLM 時，遇過最崩潰的格式錯誤是什麼？歡迎在留言區分享你的除錯經驗 👇

#LLM #AI部署 #結構化輸出 #JSON #小語言模型 #AloLab #NLP #軟體工程
