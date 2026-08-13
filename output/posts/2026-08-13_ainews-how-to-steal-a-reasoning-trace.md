---
title: '[AINews] How to steal a Reasoning Trace'
source: Latent Space
url: https://www.latent.space/p/ainews-how-to-steal-a-reasoning-trace
model: claude-code/sonnet
generated_at: '2026-08-13T07:28:28.928151'
score: 108
---

📌 加密的推理過程,原來可以被「偷聽」

TL;DR:研究揭露前沿 LLM 加密的思維鏈可被解碼並移植到其他模型,公開分享的 session 甚至可能洩漏個資。

自從 o1 上線以來,前沿實驗室就用加密簽章把模型的推理過程藏起來,理由是擔心被拿去蒸餾(distillation)。這道防線,如今被證明並沒有想像中牢固。

🤔 **為什麼要把思維鏈加密**

自 o1 發表以來,前沿實驗室的推理模型會用加密簽章隱藏其思維鏈(reasoning trace),用意是防止被拿去蒸餾訓練其他模型,儘管這並未阻止中國實驗室互相指控對方確實這麼做。今年 5 月,Matthew Green 首度負責任地披露了第一個突破口,說明如何回放這些加密區塊,並透過延遲時間側通道(side channel)間接還原資訊。而這次的新論文,則展示了更進一步的作法:直接解碼這些加密的「思維」,並將其移植到不同的模型、session 甚至使用者之間。

🧩 **攻擊步驟:回放、注入、重複取樣**

論文描述的技術大致分為幾步:先取得一段合法的、經過加密簽章的推理區塊(來自 API 回應);將這段區塊回放進另一個請求,可能是不同帳號或 session,傳給同一供應商旗下較弱的模型;把它放進 assistant/model 的對話輪次中,並提示或預填(prefill)較弱模型去轉錄附加的推理內容;重複取樣、捨棄拒答的回應,必要時再彙整多次雜訊較大的轉錄結果。針對不同供應商,論文也給出具體範本:對 Claude,是把已簽章的思維區塊回放給 Haiku 4.5,搭配 `<thinking-copy>` 之類的 assistant 預填;對 GPT,是把 `encrypted_content` 推理項目多次注入一段捏造的對話中,取樣多達 50 次輸出,並描述了如何用分段續寫繞過約 50 token 的逐字輸出限制;對 Gemini,則是把 `thought_signature` 附加到模型輪次上,搭配 `<thought>` 預填,再透過重複取樣與結果彙整還原內容。

📊 **7000 筆公開 trace 裡,藏著 62 組 API 金鑰**

研究團隊初步掃描了約 7,000 筆公開分享的推理 trace,結果在解碼後的內容中發現 62 組獨立 API 金鑰、33 個電子郵件地址、33 組密碼等敏感資料,其中部分敏感內容僅出現在推理區塊內,並未出現在使用者可見的對話畫面中。這意味著,任何曾在網路上公開分享過 Claude Code 或 Codex session(含加密推理區塊)的使用者,都有可能在不知情的狀況下洩漏個資。

💡 **是嚴重的隱私問題,還是誇大的蒸餾威脅**

社群對此事的解讀出現分歧。一派認為這是嚴重的隱私與安全問題:公開分享 trace 具有風險,隱藏的思維鏈也並非可靠的監控介面,即便關閉顯式的 thinking 功能,提供 deep_think 之類的工具介面仍可能誘發內部格式的思維鏈輸出。另一派則認為,這次攻擊並不代表能大規模竊取思維鏈去訓練模型,而更像是無狀態分散式推理協議(stateless distributed-inference protocol)在最佳化過程中暴露的副作用,而非一道堅固的機密性防線。論文也提到對齊層面的問題,例如思維鏈摘要器(COT summarizer)有時會隱藏答案。

⚠️ **已負責任揭露,但類似攻擊恐怕不會絕跡**

這篇論文是以負責任揭露(responsible disclosure)的方式進行,目前已有多個相關漏洞被修補,但作者與社群普遍認為,類似的攻擊手法未來仍有可能以其他形式出現。

🎯 **給工程團隊的提醒**

如果你的工作流程涉及公開分享 Claude Code、Codex 等帶有推理內容的 session,現在是重新檢視這個習慣的時候,加密的思維鏈不保證內容不會外洩。對於自建 agent 或工具介面的團隊,也值得檢視沙盒(sandboxing)、telemetry 與工具介面設計,避免思維鏈以非預期的形式重新暴露。

🔗 **來源**
- 標題:[AINews] How to steal a Reasoning Trace
- 作者/機構:Latent Space
- 連結:https://www.latent.space/p/ainews-how-to-steal-a-reasoning-trace

#LLMSecurity #ChainOfThought #AISafety #ReasoningModels #Interpretability #DataPrivacy #ModelExtraction #ResponsibleDisclosure #AIAlignment #FrontierModels
