---
title: "Chain-of-Authorization: Internalizing Authorization into Large Language Models via Reasoning Trajectories"
source: ChatPaper/AI
url: https://arxiv.org/abs/2603.22869
score: 113
model: gpt-4o-free
generated_at: 2026-03-25T19:32:21.829426
---

📌 **鏈式授權：讓LLM自己懂權限**  
【Tsinghua University / HKUST(GZ) / Wuhan University】

LLM 會讀到它不該看的資料嗎？一種新方法把授權檢查寫進模型的推理過程，讓未授權的查詢直接被拒絕。  
這麼做能否同時保留模型的實用性，又有效阻擋資料洩漏與惡意提示？

🤔 **授權檢查不該是後補措施**  
現有防護多依賴外部規則或固定過濾，難以應用於需要動態權限判斷的場景。當模型把所有可見資料當作同等知識使用時，敏感資訊外洩與對抗性操作的風险便會提升。這正是本文想解決的核心矛盾：如何讓授權成為模型生成答案的必要前置步驟，而不是事後補救。

🧪 **透過監督微調內嵌授權推理**  
研究團隊提出 Chain-of-Authorization (CoA) 框架。在輸入階段注入權限資訊，並要求模型在給出最終回答前，必須產生一段明確的授權推理軌跡——包含資源審視、身份解析與決策三個階段。經過在涵蓋各種授權狀況的資料上進行監督微調，CoA 讓授權檢查與任務回應成為一體，使得未授權的查詢在推理過程中被直接拒絕。

🔑 **授權成為因果前置，實用性未顯著下降**  廣泛評估顯示，CoA 在授權情境下的表現與基礎模型相當；而在未授權或對抗性輸入上，模型展現出高拒絕率。這意味著授權不再是可選的外掛，而是透過自然語言理解能力主動執行的安全機制。

💡 **權限推理可視化，有助除錯與政策審查**  
因為模型必須先輸出「資源審視 → 身份解析 → 決策」的推理步驟，開發者可以直接檢查這段文字來了解為什麼會被允許或拒絕。這種可見的授權軌跡不僅提升系統透明度，也便於政策調整與除錯工作。

⚠️ **依賴專門訓練資料，泛化能力需進一步觀察**  CoA 的效果取決於用於監督微調的授權標註資料質量與覆蓋度。文件中未提及跨任務或跨域的泛化測試，亦未說明在極長上下文或複雜工具使用場景中的表現。這些屬於作者自身承認的研究限制，後續工作可探索更通用的資料合成方式或少樣本適配策略。

🎯 **將授權視為模型能力的一部分，而非附加防護**  
對於希望在生產環境部署 LLM 的工程團隊，這項研究提供了一種可訓練的內建安全範式：透過監督微調將政策編碼為模型的推理流程，使得授權檢查成為生成過程的必經步驟。未來可結合現有的指令遵循或鏈式思考技術，進一步提升政策表達的靈活性與精細度。

🔗 **論文連結**  
📝 Chain-of-Authorization: Internalizing Authorization into Large Language Models via Reasoning Trajectories  
👤 Yang Li, Yule Liu, Xinlei He, Youjian Zhao, Qi Li  
🔗 https://arxiv.org/abs/2603.22869  

你認為把授權寫進模型推理是未來 AI 安全的必備方向嗎？歡迎留言討論 👇

#AI #LLM #Authorization #AI安全 #Tsinghua #HKUST #WuhanUniversity #ChainofThought #GenAI
