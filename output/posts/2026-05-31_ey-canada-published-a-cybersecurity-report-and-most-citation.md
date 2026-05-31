---
title: "EY Canada published a cybersecurity report and most citations were hallucinated"
source: Hacker News
url: https://gptzero.me/investigations/ey
score: 95
model: tencent/hy3-preview:free
generated_at: 2026-05-31T19:34:58.371090
---

📌 【EY Canada 報導】網安報告引用多為幻覺？

你有見過一份顧問報告，裡面的參考文獻大半是 AI 編出的嗎？這不只是個別錯誤，而是一種正在蔓延的「vibe citing」現象。

🤔 **報告引用被質疑，真實性成疑點**  
今年初，Ernst & Young (EY) Canada 發表了一題為《Points of Attack: Uncovering Cyber Threats and Fraud in Loyalty Systems》的網路安全報告，探討忠誠度計畫的防護措施。報告一經發布，即被新聞、部落格與 AI 搜尋引用，但在 GPTZero 的調查中發現，報告內的許多引用並不存在於實際文獻中。

🧪 **使用 Hallucination Check 工具進行自動化稽核**  
GPTZero 團隊先前開發了「Hallucination Check」工具，專門偵測 LLM 產生的虛假參考文獻。他們將此工具套用於公開的顧問公司報告，建立自動化管線來掃描引用是否對應真實來源。在此管線下，EY Canada 的報告被納入檢查範圍。

 **多數引用被證實為幻覺**  
經過自動化掃描與人工覆核，調查顯示該報告中的「大多數」引用屬於 hallucinations（虛構的文獻）。這些虛假引用不只停留在報告內部，更被外部媒部落格與 AI 搜尋結果引用，進而污染了人類研究者與 AI 代理人所依賴的知識基礎。

💡 **「vibe citing」：檢查引用的摩擦導致錯誤被接受**  
GPTZero 的工程師最早提出「vibe citing」一詞，用來描述在使用 LLM 產生內容時，因核對引用的成本與麻煩，導致人們不經意地接受 AI 編造的參考文獻。當檢查引用的阻力變高時，這種「隨便引用」的習慣就會滋長，使錯誤在學術、諮詢與公共文件中擴散。

⚠️ **調查限制：依賴自動工具，樣本範圍有限**  
本次調查主要依賴 GPTZero 的 Hallucination Check 工具，可能無法捕捉到所有形式的幻覺（例如語義上正確但事實錯誤的引用）。此外，掃描對象目前限於公開的顧問公司報告，未涵蓋所有類型的文獻。因此，結果反映的是已被工具標記的明顯虛假引用，而非全部可能的錯誤。

🎯 **建議引入驗證流程，降低幻覺風險**  
- 在 AI 輔助寫作或報告撰寫流程中，加入自動或半自動的引用事實核驗步驟。  
- 鼓勵使用具備來源追蹤功能的工具（如 GPTZero Hallucination Check、Scholar AI 等）來事先過濾可疑參考文獻。  
- 提高團隊對「vibe citing」現象的認識，將引用檢查視為品質控制的必要環節，而非可選的額外工作。

🔗 **論文連結**  
📝 GPTZero Investigation: EY Canada Cybersecurity Report – Most Citations Hallucinated  
👤 調查團隊：GPTZero（由 smartmic 在 Hacker News 分享）  
🔗 報告：https://gptzero.me/investigations/ey  

你在使用 AI 撰寫報告時，是否也曾遇過類似的引用問題？歡迎在留言區分享你的經驗與應對做法 👇

#AI #Hallucination #VibeCiting #CyberSecurity #EY #GPTZero #ResponsibleAI #TechEthics
