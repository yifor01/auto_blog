---
title: "From Prompt Injection to Persistent Control: Defending Agentic Harness Against Trojan Backdoors"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.31042
score: 98
model: tencent/hy3-preview:free
generated_at: 2026-06-01T22:10:54.994668
---

📌 **多步驟木馬的防禦新策**  

你以為防禦單步提示注入就夠了？研究顯示，攻擊者現在能把惡意提示藏在多個操作步驟中，繞過現有的防禦機制。  

🤔 **LLM 代理的廣泛部署帶來新威脅**  
隨著基於大型語言模型的代理（Agent）在本地環境中被越來越多地使用，傳統的 Prompt‑Injection 防禦只能針對單一步驟的惡意提示。當攻擊者將惡意指令拆解並分散執行於多個步驟時，現有偵測方式往往失效，導致「持續控制」的木馬攻擊得以悄悄佈署。  

🧪 **提出 DASGuard 偵測機制**  
該論文提出了一種名為 **DASGuard** 的新偵測方法，專門設計用於識別跨多個代理操作持續存在的木馬行為。作者強調，這種方法填補了現有防禦在處理多步驟 trojan 攻擊時的空白。  

🔑 **核心貢獻：提供跨步驟惡意偵測的工具**  
DASGuard 的核心思想是將代理的每一步操作視為序列中的觀測點，透過對序列中不一致或可疑模式的統計分析，嘗試捕捉那些在單一步驟中難以察覺的惡意痕跡。如此一來，即使攻擊者將惡意提示分散於多個步驟，系統仍有機會在整個執行流程中發出警報。  

💡 **為何這很重要？**  
- **實用性**：為工程師提供一個具體的偵測工具，可直接嵌入現有的 Agentic Harness 中。  
- **前瞻性**：隨著 LLM 代理在自動化工作流、個人助理及企業應用中的普及，防禦多步驟攻擊將成為安全基礎設施的必要組成。  

⚠️ **已知資訊的限制**  
摘要僅說明了方法的動機與概念，未提供實驗規模、基準比較或實際部署效能的具體數據。如需了解 DASGuard 在不同模型、不同攻擊強度下的精確表現，仍須參考全文實驗章節。  

🎯 **給開發者的建議**  
1. 在評估或部署本地 LLM 代理時，將偵測步驟納入安全檢查清單。  
2. 關注社區對 DASGuard 的開源實作或後續改進，以便快速整合到自家的 Agentic Harness。  
3. 持續監控代理操作序列中的異常點，而非僅依賴單步驟的輸出過濾。  

🔗 **論文連結**  
📝 From Prompt Injection to Persistent Control: Defending Agentic Harness Against Trojan Backdoors  
🔗 https://huggingface.co/papers/2605.31042  

你的 LLM 代理目前有防禦多步驟攻擊的機制嗎？歡迎在留言區分享你的看法或經驗 👇  

#AI安全 #LLM #PromptInjection #AgenticAI #DASGuard #HuggingFace #網路安全 #開發者工具
