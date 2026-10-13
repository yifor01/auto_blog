---
title: Uber's CISO on building an insider threat program for AI
source: Claude Blog
url: https://claude.com/resources/articles/uber-s-ciso-on-building-an-insider-threat-program-for-ai
model: claude-code/sonnet
generated_at: '2026-10-13T21:56:54.563440'
pinned: true
---

📌 【Claude 客戶故事】Uber CISO：AI agent 也需要「內部威脅」管理

TL;DR：Uber CISO Philip Martin 主張替 AI agent 建立如同人類員工的內部威脅計畫，並搭配 Anthropic 的 Enterprise Frontier Safeguards 落地。

🎣 每家公司都替員工建立內部威脅（insider threat）管理機制，沒有人會質疑這件事的必要性。但當「員工」換成了會自主呼叫工具、跨服務溝通的 AI agent，同樣的防護網卻幾乎不存在。這正是 Uber CISO Philip Martin 在這篇訪談中提出的核心主張。

🤔 **背景：一天 4,000 萬趟行程的資安挑戰**

Uber 經營全球最大的即時媒合平臺之一，每天處理超過 4,000 萬趟行程與外送訂單。Philip Martin 帶領的團隊負責保護 Uber 的資料，以及使用平臺的乘客、司機與外送員。團隊在 Claude Code 問世之前就已經在用 Claude 做威脅建模，當時還得靠人工彙整上下文；現在透過 Claude Fable，Claude 能自行從程式碼、設計文件與 ticket 歷史中蒐集上下文。

🧩 **Enterprise Frontier Safeguards 與 Uber 自研 ADR 的分工**

Martin 指出，Anthropic 與 Uber 在「安全」這件事上有共同的核心關注，只是場景不同：Uber 關注乘客安全與個資保護，Anthropic 則聚焦於防止前沿模型被誤用。Enterprise Frontier Safeguards 讓 Uber 能在不把資料開放給 Anthropic 存取的前提下，取得安全防護機制，並由 Uber 自行決定觸發防護後要採取的風險緩解行動。

搭配這套機制，Uber 近期開源了一款名為 AI Detection and Response（ADR）的工具，用於在 agent 執行環境（harness）中蒐集即時遙測資料並做出即時反應。Martin 形容，這讓團隊同時擁有「自己對 agent 行為的觀察視角」與「Anthropic classifier 輸出的結果」，兩者可以整合進既有的整體偵測環境，運作邏輯類似傳統資安架構。再加上控管 AI 使用邊界的 LLM gateway，三者共同構成 Uber 的整體 AI 資安架構。

💡 **威脅情報的下一步：即時介入與行為模式辨識**

被問到防禦者接下來該優先投入哪裡時，Martin 提出兩個重點：第一是即時偵測與介入，盡可能在使用者於 harness 中輸入 prompt 的當下，就提示「這個工具呼叫、這個連線目的地可能不是你想要的」；第二是理解新出現的行為模式——團隊觀察模型行為趨勢，（部分藉助 LLM 輔助）發現過去未知的行為，並把對應的防護機制回饋進即時平臺，而新的限制又會催生新的行為，形成持續循環。

他也提到一個值得關注的願景：未來每個服務都可能搭配一個深度理解該服務的 agent，這些 agent 之間能像生產環境中的服務一樣互相溝通威脅模型資訊，進一步放大團隊協作效益。

🎯 **實務啟示**

對導入 agentic AI 的企業資安團隊而言，這篇訪談傳遞的訊息很明確：不要把 AI agent 的風險管理視為獨立於既有安全框架之外的新問題，而是把「員工內部威脅計畫」的思路延伸過去——包含資料留存、行為監控、即時介入等機制，都需要有對應的 AI 版本。Uber 將自研的 ADR 與供應商提供的 Enterprise Frontier Safeguards 並行使用，是一個可供參考的分層防護架構。

🔗 **來源**
- 標題：Uber's CISO on building an insider threat program for AI
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/uber-s-ciso-on-building-an-insider-threat-program-for-ai

#AISecurity #InsiderThreat #Anthropic #Claude #Uber #CISO #EnterpriseAI #AgenticAI #AIRiskManagement #CyberSecurity
