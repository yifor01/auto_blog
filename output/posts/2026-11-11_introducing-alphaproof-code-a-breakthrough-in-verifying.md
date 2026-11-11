---
title: 'Introducing AlphaProof Code: a breakthrough in verifying complex software
  at depth'
source: Google DeepMind
url: https://deepmind.google/blog/introducing-alphaproof-code/
model: claude-code/sonnet
generated_at: '2026-11-11T23:38:45.745906'
score: 144
---

📌 【Google DeepMind】AI代理首次完成Signal協議程式碼的形式化驗證

TL;DR：AlphaProof Code讓AI代理寫出數百萬行Lean證明，四週內完成人類團隊過去需要數年的密碼協議驗證。

密碼協議的安全性分析,業界通常只做到「設計層級」就停下來,因為往下驗證到實際編譯後的程式碼,複雜度會呈指數級攀升。這次 Google DeepMind 的團隊選擇不停在設計層級,而是直接把 Signal 協議——保護 Signal、Google Messages 等應用數十億則私訊的加密技術——的實際程式碼,一路驗證到底。

🤔 **形式化驗證為何是「大挑戰」**

形式化驗證(formal verification)是用數學方式證明程式碼執行無誤,是安全保證的最高標準,但過程極度費力。多數密碼協議的驗證停留在設計層級,因為真實世界的漏洞往往藏在「設計」與「實作」之間的落差裡,而把這個落差也納入證明範圍,會讓整個工作量暴增。這也是為什麼在這次之前,從未有任何方法(無論是否用 AI)對一個廣泛部署的協議完成這種深度的驗證。

🧩 **AlphaProof Code:人類定義目標,AI代理產生證明**

AlphaProof Code 是一套多 LLM 的 agentic 框架,把形式化驗證的工作拆解成研究團隊的分工模式:人類專家與 AI 協作,先把 Signal 的安全目標翻譯成正式的數學規格,每一條都經過人類審查;接著由 Gemini Carbon 驅動的 AI 代理群接手,產出以 Lean(一種能數學驗證程式碼正確性的電腦語言)撰寫的證明。完成後,代理會自動稽核整份證明,標出需要人類再次檢視的部分——結果只佔整個程式碼庫的百分之一,因為 Lean 會自動檢查其餘內容,專家可以把審查資源集中在最需要人類判斷的地方。

📊 **四週完成的驗證,過去要花上數年**

AI 代理最終產出了超過六百萬行 Lean 證明,證明 Signal 的核心密碼學程式碼確實滿足專家所定義的安全屬性,包括「設備暫時被攻破前後,訊息仍受保護」這類性質。整個驗證過程只花了四週,相比之下,這類任務歷史上需要專家團隊耗費數年。為了驗證 AlphaProof Code 真的能分辨「正確」與「有漏洞」的程式碼,團隊把兩個曾經真實存在、後來已修復的錯誤,重新植入一份獨立的 Signal 程式碼副本中測試——結果系統在兩種情況下都產出了機器可驗證的證明,指出該版本不安全。

💡 **從「設計安全」走向「程式碼安全」**

Signal 技術長 Ehren Kret 在文中表示,過去的形式化驗證工作必然侷限在較小範圍,而這次的方法讓驗證規模大幅擴張;用 AI 代理把實際執行的程式碼自動翻譯成有效的 Lean 定理,是一項重大突破。隨著 AI 驅動的網路威脅增加,核心協議通過嚴謹的自動定理證明,讓團隊對程式碼的隱私保證更有信心。

⚠️ **仍需持續研究才能擴大規模**

團隊也坦言,要把這套技巧擴展到其他關鍵系統(例如醫療裝置韌體、電網軟體)仍需要持續的研究投入。目前團隊已將形式化驗證成果開源,供社群使用。

🎯 **實務啟示**

對工程團隊而言,這是一個訊號:形式化驗證不再只是學術界的象限,AI 代理有機會把過去「不可能規模化」的驗證工作,壓縮到數週內完成,並讓人力集中在真正需要判斷力的一小部分程式碼。搭配自動化防禦代理(文中提到的 CodeMender),形式化驗證有潛力成為對抗高速 AI 驅動攻擊的重要防線。

🔗 **來源**
- 標題：Introducing AlphaProof Code: a breakthrough in verifying complex software at depth
- 作者／機構：Google DeepMind
- 連結：https://deepmind.google/blog/introducing-alphaproof-code/

#AI #FormalVerification #GoogleDeepMind #Signal #Cryptography #Cybersecurity #LeanProver #AlphaProof #SoftwareSecurity #AgenticAI
