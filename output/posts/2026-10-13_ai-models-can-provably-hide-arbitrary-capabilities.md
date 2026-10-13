---
title: AI models can provably hide arbitrary capabilities
source: Hacker News
url: https://arxiv.org/abs/2610.13928
model: claude-code/sonnet
generated_at: '2026-10-13T22:06:43.129933'
score: 90
---

📌 密碼學證明:AI 模型能永遠藏住一項能力不被發現

TL;DR:研究團隊用加密神經網路證明,模型權重中可以藏入無法被標準紅隊方法找出的能力後門。

模型安全評估的整套邏輯,建立在一個假設上:只要有足夠的誘導手段,危險能力終究會被找出來。這篇論文直接打掉這個假設的地基,而且用的是密碼學等級的證明,不是經驗性的「我們試過沒找到」。

🤔 **能力評估的隱藏前提**

Capability evaluation(能力評估)的目的是在部署前揪出模型中危險的潛在行為,但這套方法的可靠性,完全仰賴一個前提:隱藏的能力一定能被誘導出來(elicited)。這篇由 Andis Draguns、Sumeet Ramesh Motwani、Raymond Douglas 與 Christian Schroeder de Witt 共同發表的論文指出,在對抗性條件下,這個前提並不成立。

🧩 **把加密電路藏進模型權重裡**

研究團隊構造了一種後門攻擊:將「加密過的神經網路」嵌入主模型的權重之中,這個隱藏電路只有在收到特定的秘密觸發訊號(secret trigger)時,才會被解密並執行。他們使用的技術稱為「digital lockers(數位鎖)」,在密碼學假設下,即便攻擊者擁有模型權重的完整存取權,這些隱藏電路依然被證明難以被誘導與解讀。論文指出,這項工作把先前只能隱藏固定字串的技術,延伸到可以隱藏任意運算(arbitrary computations)。

📊 **在化學反應預測任務上的驗證**

團隊以 PyTorch 實作了概念驗證(proof of concept),並在一個小型的化學反應預測任務上評估——作者將此任務作為 CBRN(化學、生物、放射性、核)相關能力的替代指標(proxy)。他們測試了四種常見的能力誘導(elicitation)手段:fine-tuning、weight noising(權重加噪)、gradient-based trigger search(梯度式觸發搜尋),以及 latent adversarial training(潛空間對抗訓練)。結果顯示,這些隱藏電路對上述所有方法都表現出抵抗力,配合其密碼學保證,共同揭示了「以誘導為基礎的能力審查」存在根本性的侵限。

💡 **這對模型安全審查意味著什麼**

這篇論文的核心衝擊在於:它不是說「現有的紅隊方法還不夠好,再努力一點就能找到」,而是用密碼學方式證明,在特定構造下,某些隱藏能力原則上就是不可被現有誘導方法找到的——無論審查者多努力嘗試 fine-tuning 或梯度搜尋,都無法觸及那段被加密鎖住的電路。這等於是幫「模型可能藏有審查者找不到的能力」這個長期被視為理論風險的說法,補上了一個具體可實作的構造。研究團隊也公開了模型,供其他人研究防禦方法。

⚠️ **目前侷限於概念驗證規模**

論文中的實驗是在小型化學反應預測任務上進行的概念驗證構造,並非在真實部署規模的大型語言模型上驗證,這點在解讀其對實際模型安全審查的影響時需要留意。

🎯 **實務啟示**

對於負責模型安全評估或紅隊測試的團隊,這篇論文提醒:僅依賴「誘導式」評估(嘗試各種 prompt、fine-tuning、梯度搜尋去挖出危險行為)作為安全保證的唯一手段,存在理論上無法克服的盲區。供應鏈與第三方權重的可信度驗證,可能需要在誘導測試之外,搭配更嚴格的來源控管與結構性檢查。

🔗 **來源**
- 標題:AI Models Can Provably Hide Arbitrary Capabilities
- 作者/機構:Andis Draguns, Sumeet Ramesh Motwani, Raymond Douglas, Christian Schroeder de Witt
- 連結:https://arxiv.org/abs/2610.13928

#AISafety #ModelSecurity #Cryptography #Backdoor #RedTeaming #CapabilityEvaluation #CBRN #AIAlignment #AdversarialML #PyTorch
