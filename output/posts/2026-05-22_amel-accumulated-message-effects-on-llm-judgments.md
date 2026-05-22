---
title: "AMEL: Accumulated Message Effects on LLM Judgments"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.22714
score: 107
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:45:43.631548
---

📌 【OpenAI/Anthropic/Google 聯合研究】LLM 評分會被先前對話極性偏左右？AMEL 效應揭露  

你以為讓同一段對話連續評分多項目，只是提高效率？實際上，先前的正負評價會悄悄拉偏後續的判斷。  

🤔 **先前對話的極性會偏移後續判斷**  
當 LLM 作為自動評審時，許多工作流會把眾多項目放在同一個對話中。研究團隊想知道：這樣的歷史訊息是否會產生累積效應，使模型朝著對話的整體極性（正或正負）傾斜？  

🧪 **75,898 次 API 呼叫，11 個模型，4 個供應商**  
實驗中，研究團隊讓相同的測試項目分別在「乾淨」的情境下，或在飽和著 predominantly positive / predominantly negative 評價的歷史後進行評分。歷史長度從 5  turn 到 50 turn 均有測試，涵蓋 OpenAI、Anthropic、Google 的商業模型以及四個開源模型。  

📊 **模型會隨對話極性偏移，負面影響更強**  
- 整體效應大小：d = -0.17（p < 10⁻⁴⁶），表示在負面歷史後，模型的判斷會朝負方向偏移約 0.17 個標準差。  
- 在模型本身不確定（高 entropy）的項目上，效應加倍：d = -0.34；在確定性高的項目上則為 d = -0.15。  
- **負面歷史的偏移是正面歷史的 1.62 倍**（t = 13.46, p < 10⁻³⁹, n = 2,481），顯示明顯的 negativity asymmetry。  
- 偏移量**不會隨著歷史長度增長而增加**：5 turn 與 50 turn 的效應相近（Spearman |r| < 0.01；OLS slope p = 0.80）。  

🔍 **擴大模型有幫助但無法消除**  
隨著模型能力提升，偏移會減小，但仍存在：  
- Anthropic：Haiku -0.22 → Opus -0.17  
- OpenAI：Nano -0.34 → GPT-5.2 -0.17  
這表明僅靠 scaling 無法完全消除 AMEL。  

💡 **機制探討：連續的機率分布位移**  
後續分析發現，token 機率分布會隨著歷史極性**連續**位移，而不是在某個閾值才突變。負面與正面的偏移在 token 層面與語意層面皆有貢獻，但目前樣本 size 下無法精確劃分兩者的比例。此外，歷史中哪五個 turn 帶有偏見**不影響結果**；只要數量相同，位置無關。  

⚠️ **研究限制**  
- 雖然樣本龐大（75,898 次呼叫），但仍屬於特定的評分任務與模型家族，其他類型任務的普遍性需進一步驗證。  
- 論文未深入探討不同提示工程或訊息壓縮技巧對 AMEL 的影響。  

🎯 **實務啟示：評估管線的簡單修正**  
1. **最直接的做法**：每個項目使用全新的對話情境（fresh context per item），即可將歷史偏移歸零。  
2. 若因效率考量必須批次處理：**在歷史中平衡正負評價的數量**，可減少淨偏移。  
3. 在設計自動評審流程時，應該監控歷史極性的分布，特別是當模型對某些項目本身不確定時，這類項目最易受偏影響。  

🔗 **論文連結**  
📝 AMEL: Accumulated Message Effects on LLM Judgments  
👤 Sid-ali Temkit (OpenAI; Anthropic; Google)  
🔗 https://arxiv.org/abs/2605.22714  

你在使用 LLM 做程式碼審查、內容審核或模型輸出評分時，是否已經為每個項件開啟新的對話？歡迎在留言區分享你的做法與經驗 👇  

#AI #LLM #EvaluationBias #AMEL #OpenAI #Anthropic #Google #機器學習 #自動評審 #技術研究
