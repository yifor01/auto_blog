---
title: Jul 8, 2026AlignmentAn off switch for dual use knowledge in AI models
source: Anthropic Research
url: https://www.anthropic.com/research/off-switch-dual-use
score: 129
model: google/gemma-4-31b-it:free
generated_at: '2026-07-09T09:44:25.248491'
---

📌 【Anthropic 研究】不只是拒絕，而是讓 AI 具備可開關的「雙用途知識」

TL;DR：Anthropic 提出透過控制模型權重而非僅靠對齊，來精準開關可能被濫用的雙用途知識。

當一個強大的 AI 模型既能幫研究員開發疫苗，也可能被惡意人士用來設計病原體時，我們該如何管理這種「雙用途（Dual Use）」知識？目前的對齊技術（Alignment）大多在做「出口管制」，但真正的風險其實藏在模型的記憶體中。

🤔 **拒絕回答 $\neq$ 刪除知識**

目前業界常用的安全防護（Safeguards）主要分為兩層：訓練模型拒絕有害請求，以及使用分類器篩選輸入與輸出。然而，這些方法僅是在防止危險內容的「輸出」，並沒有改變模型底層儲存的知識。對於執著的攻擊者來說，只要能成功 jailbreak（破解），依然能從模型中提取出那些危險的知識。

🧩 **從「粗暴過濾」演進到「權重控制」**

為了從根源解決問題，Anthropic 與 AE Studio 探索了更強健的保護方式，將重點從「控制輸出」轉向「控制模型知道什麼」：

- **早期方法（資料過濾）**：在預訓練階段就將化學、生物、放射性與核武器等資訊過濾掉。但這種做法過於粗糙，會導致模型能力固定，若需要一個能討論高階病毒學的版本（例如給經過審核的生物安全實驗室使用），就必須重新訓練一個獨立的模型。
- **進階方法（權重切片）**：研究顯示，雙用途知識可以被限制在模型權重的一個「可移除切片（removable slice）」中。

💡 **追求更精準的知識管理**

研究團隊目標是達成三個平衡點：
1. 以最精準（Surgical）的方式限制對雙用途能力的存取。
2. 允許受信任的使用者為了有益目的而存取這些能力。
3. 在上述操作過程中，完全不影響模型在其他任務上的效能。

🎯 **實務啟示**

對於 AI 安全工程師而言，這項研究的方向顯示，未來的安全防禦可能不再僅僅依賴於 SFT 或 RLHF 的拒絕機制，而是在模型權重層級實現「知識模組化」。這意味著 AI 的能力將能根據使用者的許可權，像開關一樣被精確地開啟或關閉，而無需為不同許可權層級維護多個巨大的模型副本。

🔗 **來源**
- 標題：An off switch for dual use knowledge in AI models
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/research/off-switch-dual-use

#AI #AIAlignment #AISafety #DualUse #Anthropic #ModelWeights #Cybersecurity #Biosecurity #MachineLearning #LLM
