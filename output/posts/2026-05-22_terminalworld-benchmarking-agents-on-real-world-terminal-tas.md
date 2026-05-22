---
title: "TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.22535
score: 102
model: tencent/hy3-preview:free
generated_at: 2026-05-22T21:04:01.885954
---

📌 **TerminalWorld：以真實終端機錄影自動建構大規模基準，評估代理人在指令列工作流上的表現**

你以為現在的 AI 代理人已經能輕鬆應付終端機指令嗎？最新基準顯示，即使是最前沿的模型，在真實終端機工作流上的成功率仍只有六成左右。

🤔 **真實終端機工作流才是真正的考驗**

現有的代理人評估多依賴專家精心設計的小規模任務，難以反映開發者在日常終端機操作中遇到的複雜、多步驟工作流。這導致評估結果可能高估了代理人的實用能力。

🧪 **80,870 條終端機錄影自動轉化為評估任務**

研究團隊提出 **TerminalWorld**，一個可擴充的資料引擎，能自動從「野外」終端機錄影中逆向工程出高保真評估任務。該引擎處理了 80,870 條錄影，產出 1,530 倔經驗證的任務，橫跨 18 個真實類別，指令步驟從簡單的單指令操作到超過 50 步的工作流，涵蓋 1,280 條獨特指令。從中進一步篩選出 200 倔具代表性、經人工複審的 **TerminalWorld-Verified** 子集，作為最終基準。

 **八種前沿模型與六種代理人在 Verified 集上的最高通過率僅 62.5%**

在 TerminalWorld-Verified 上進行的全面基準測試涵蓋了八種前沿語言模型與六種代理人系統。結果顯示，這些系統的最高任務通過率只有 **62.5%**，遠低於理想的完美分數，顯示目前的代理人在處理真實終端機工作流時仍有顯著不足。

💡 **與現有基準的關聯性極弱，凸顯 TerminalWorld 捕捉了不同的能力面向**

TerminalWorld-Verified 的成績與現有專家策劃的基準（例如 Terminal-Bench）僅具弱相關（Pearson r = 0.20）。這說明 TerminalWorld 所測量的終端機能力與既有基準所捕捉的並不完全重疊，提供了一種互補的評估視角。

⚠️ **自動化引擎依賴錄影品質與標註一致性，基準仍隨終端機實踐演變而變動**

TerminalWorld 的優勢在於自動化與擴充性，但其任務品質取決於原始終端機錄影的清晰度與後續驗證過程的一致性。此外，隨著開發者終端機使用習慣的變化，基準內容也需要定期更新以保持貼近真實場景。

🎯 **建議將 TerminalWorld 作為代理人終端機能力的常規評估工具，並結合人工審核提升任務可信度**

- 使用 TerminalWorld-Verified 進行基準測試，可快速得到代理人在多樣真實終端機工作流上的表現基線。
- 於關鍵發展階段，可人工審核部分任務以確保評估的穩定性與可重複性。
- 開放的資料與程式碼（GitHub: https://github.com/EuniAI/TerminalWorld）使團隊能自行擴充或針對特定工具鏈進行微調。

🔗 **論文連結**  
📝 TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks  
👤 Zhaoyang Chu, Jiarui Hu, Xingyu Jiang, Pengyu Zou, Han Li (University College London; Nanjing University; Tencent)  
🔗 https://arxiv.org/abs/2605.22535  
💻 數據與程式碼：https://github.com/EuniAI/TerminalWorld  

你終端機代理人的評估是否仍停留在人工設計的小任務上？歡迎在留言區分享你的看法與經驗 👇

#AI #Agent #Terminal #Benchmark #UCL #NanjingUniversity #Tencent #MachineLearning #CodeAssistant
